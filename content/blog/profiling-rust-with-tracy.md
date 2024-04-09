---
title: "Profiling Rust With Tracy"
date: 2024-04-09T09:54:14-04:00
draft: false
---

Profiling a Rust application using Tracy


1. Install Tracy tools with Homebrew (MacOS)

    ```bash
    $ brew install tracy
    ```

2. Start the `tracy-capture` server listening for an application, capture its trace to a file with `-o`
    
    ```bash
    $ tracy-capture -o server.tracy
    ```

3. Start the application, in my case a Bevy game, with the tracy features enabled

    ```bash
    $ cargo run --release --features bevy/trace_tracy --bin app -- server
    ```

4. Run the application for some amount of time to capture the actions you need profiled
5. Stop the application and open the trace file

    ```bash
    $ tracy server.tracy
    ```

_note:_ you likely need to set the logging filter to `trace` for the module(s) you want to show up in the trace.