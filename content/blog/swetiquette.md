---
title: "Software Engineering Etiquette"
date: 2025-04-23T20:52:46-04:00
draft: false
---

Building things that people can depend on requires a degree of planning and a willingness to stick to best practices, despite minor upfront timeline inconveniences. When things change, those changes should be documented and communicated to those people that rely on it, quickly and reliably.

I had a conversation at work today about a piece of software my team was integrating with, suddenly failing to return results to a request our server was making. The particular request was environment specific, and it was working earlier in the morning and in the next environment up. While talking with the team that owned the malfunctioning software, they discovered that the request had been changed or renamed and no longer matched the documentation we had been given for our integration. This normally wouldn't be a problem, they could just provide us new documentation, we'd update our code, and everything should be happy again. Except they couldn't provide updated documentation. It didn't exist and the change that was made to their software was done in a way that it wasn't clear what people using it would need to do to get things working again.

How does this happen and what can be done to avoid it in the future?

1. Define the application interface with an Interface Definition Language (IDL) and use tooling to generate documentation, server stubs and client code. See protocol buffers
2. Apply linting to the interface definition to keep naming consistent and enforce documentation standards.
3. Enforce breaking change detection at the interface level. This prevents breaking changes to an interface that has already be consumed by clients.

## Interface Definition Language

My preferred IDL is protocol buffers, they're widely used, have great tooling and can be used to represent not only web API's but also custom message protocols. There are a number of code generation tools out there, such as `buf` and `protoc`, the former being a more modern alternative the the latter.


## Linting

Linting at the API definition level allows you to enforce consistency across the API methods, naming, documentation, field types, etc. 

Examples of lint complaints that should be addressed prior to merging a feature to main:

```bash
meder@astro:gorustadmin$ buf lint
proto/rustadmin/v1/rustadmin.proto:5:1:Service "RustAdminService" should have a non-empty comment for documentation.
proto/rustadmin/v1/rustadmin.proto:6:3:RPC "AddServer" should have a non-empty comment for documentation.
proto/rustadmin/v1/rustadmin.proto:7:3:RPC "GetServerList" should have a non-empty comment for documentation.
proto/rustadmin/v1/rustadmin.proto:8:3:RPC "GetServerStatus" should have a non-empty comment for documentation.
proto/rustadmin/v1/rustadmin.proto:9:3:RPC "GetConsole" should have a non-empty comment for documentation.
proto/rustadmin/v1/rustadmin.proto:10:3:RPC "GetChat" should have a non-empty comment for documentation.
proto/rustadmin/v1/rustadmin.proto:11:3:RPC "GivePlayerKit" should have a non-empty comment for documentation.
proto/rustadmin/v1/rustadmin.proto:14:1:Message "AddServerRequest" should have a non-empty comment for documentation.
proto/rustadmin/v1/rustadmin.proto:15:3:Field "name" should have a non-empty comment for documentation.
proto/rustadmin/v1/rustadmin.proto:16:3:Field "address" should have a non-empty comment for documentation.
proto/rustadmin/v1/rustadmin.proto:17:3:Field "rcon_password" should have a non-empty comment for documentation.
```

When these issues are addressed prior to merging a feature to main, the documentation and resulting generated code are all kept to the same standard and up-to-date as soon as the feature is done. You don't have to manually update documentation to match the implementation, the documentation is automatically generated and kept up to date by a repeatable process.

## Breaking Change Detection

The `buf` cli tool also supports breaking change detection, which is very helpful in ensuring there are no breaking changes to the API contract with clients. It is commonly used to check local changes against either a remote git repository or buf registry package.

The following change should be obvious that it is breaking, but could easily slip through a manual code review. Enforcing breaking change detection as part of a CI/CD system can catch and prevent this type of change from being submitted. Instead a new version of the message should be created to support this type of change.


```diff
diff --git a/proto/rustadmin/v1/rustadmin.proto b/proto/rustadmin/v1/rustadmin.proto
index 910c674..8c25aa5 100644
--- a/proto/rustadmin/v1/rustadmin.proto
+++ b/proto/rustadmin/v1/rustadmin.proto
@@ -18,7 +18,7 @@ message AddServerRequest {
 }

 message AddServerResponse {
-  string server_id = 1;
+  int32 server_id = 1;
 }
```

### Check Against Remote Git

To check for breaking changes against a remote git repository, run `buf breaking` as follows:

```bash
meder@astro:gorustadmin$ buf breaking --against 'https://git.sqweeb.net/mikeder/gorustadmin.git#branch=main'
proto/rustadmin/v1/rustadmin.proto:21:3:Field "1" with name "server_id" on message "AddServerResponse" changed type from "string" to "int32".
```

