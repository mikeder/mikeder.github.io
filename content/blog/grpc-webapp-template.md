---
title: "gRPC WebApp Example"
date: 2022-06-30T15:43:17-04:00
draft: true
---

Notes for developing a gRPC based web application, for fun and learning.

Use [connect-go](https://github.com/bufbuild/connect-go) for server/client transport.
 - supports gRPC, JSON REST and Connect
 - no need for JSON REST translation proxy

Use [connect-grpcreflect-go](https://github.com/bufbuild/connect-grpcreflect-go) for reflection.

Use OAuth2 with GitHub provider to start.
Use React frontend.

Use GitHub actions for linting, building and publishing packages.
 - [golangci-lint](https://github.com/golangci/golangci-lint-action)
 - go build/test
 - go sematic release
 - GH packages release ( docker image to ghcr.io )

Deploy to AWS or Azure, scripts to use CLI to provision resources.

## Functionality Considerations

1. Auth via OAuth2 login.
1. User generated public and private lists.
1. Share option for lists w/ shortcode/QR code generation.
1. Tracing and Metrics emitted via OpenTelemetry.

