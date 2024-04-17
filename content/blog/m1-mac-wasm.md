---
title: "M1 Macs, Rust & WASM"
date: 2024-04-17T13:35:12-04:00
draft: false
---

Getting setup for compiling Rust to WASM and serving w/ Trunk on M1 Mac.


1. Install `wasm32-unknown-unknown` target with `rustup`

    ```bash
    $ rustup target add wasm32-unknown-unknown
    ```

2. Install `wasm-bindgen-cli`

    ```bash
    $ cargo install --locked wasm-bindgen-cli
    ```

3. Test compiling a project w/ the new wasm target

    ```bash
    $ cargo build --target wasm32-unknown-unknown
    ```

    If this fails due to [No available targets are compatible with triple "wasm32-unknown-unknown" #103](https://github.com/rust-lang/libz-sys/issues/103), install an updated version of `clang` via Homebrew.

    Original version:
    ```bash
    $ clang --version
    Apple clang version 15.0.0 (clang-1500.3.9.4)
    Target: arm64-apple-darwin23.1.0
    Thread model: posix
    InstalledDir: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin
    ```

    Update via Homebrew
    ```bash
    $ brew install llvm
    ```

    Use newer version from Brew
    ```bash
    export PATH="/opt/homebrew/opt/llvm/bin:$PATH"
    export CC=/opt/homebrew/opt/llvm/bin/clang
    export AR=/opt/homebrew/opt/llvm/bin/llvm-ar
    ```

    Updated version:
    ```bash
    $ clang --version
    Homebrew clang version 17.0.6
    Target: arm64-apple-darwin23.1.0
    Thread model: posix
    InstalledDir: /opt/homebrew/opt/llvm/bin
    ```

## References

[Trunk](https://trunkrs.dev/)

[No available targets are compatible with triple "wasm32-unknown-unknown" #103](https://github.com/rust-lang/libz-sys/issues/103)

[Unrelated project installation w/ notes on LLVM/Clang install](https://learn.sapio-lang.org/ch01-01-installation.html)