---
title: "Renet to Lightyear 1"
date: 2024-04-12T14:44:48-04:00
draft: false
tags:
- rust
- bevy
- networking
- unfinished
---

Notes from my effort to replace `bevy_renet` with `lightyear` in my "WIP" game.

Renet is a popular server authoritative networking library for the Bevy game engine. I started using it for a new game I'm working on and really liked its simplicity from the start. Eventually though, I realized I wanted to target WASM for my game and Renet does not currently support websockets or webtransport. Another up and coming library is [lightyear](https://github.com/cBournhonesque/lightyear) - its got a very active main contributor/maintainer in the Bevy Discord and it comes with support for WASM via websockets or webtransport and also supports crossplay between protocols as well as advanced replication features like client side prediction, rollback and snapshot interpolation, and many more!


## Replacing Renet

I had already refactored much of my game to expect Events that had been converted from network packets from Renet, so *most* of the logic was decoupled from the networking implementation. The main issue would be the "networked entities", which in lightyear, would be handled for me via the components replication protocol.

Light year supports a few replication sync modes, simple, once, and full - I had to decide on which to use for each of the components that I would replicate from server to client. In general, marker components could be "once" and positional or constantly changing components, like `Transform` or `Health` could be "full".


## Unsolved Mysteries

```bash
lightyear::shared::replication::send
```