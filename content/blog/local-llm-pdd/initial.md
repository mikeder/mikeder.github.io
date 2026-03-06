---
title: "Local Coding LLM - Initial Setup"
date: 2026-03-06T09:32:15-05:00
draft: true
---

Exploring options for running an AI coding assistant at home, using hardware I already have. My initial research gave me a couple interesting options to try out:


1. llama.cpp - llama-server can run GGUF format models, supports downloading directly from HuggingFace and provides a basic chat interface built into the server. Can run inference directly on the CPU but would perform better with GPU access.
2. lmstudio - can run models of various formats, comes with a nice GUI for browsing, downloading and running models. Will make use of available GPU by default (doesn't require custom compilation like llama.cpp).


## Attempt 1

Executor: llama.cpp
Model: TeichAI/Qwen3-14B-Claude-4.5-Opus-High-Reasoning-Distill-GGUF:Q4_K_M
Hardware: Intel i7 4790k, 16GB DDR3 1600

Command:

```bash
meder@liquidwhite:bin$ ./llama-server -hf TeichAI/Qwen3-14B-Claude-4.5-Opus-High-Reasoning-Distill-GGUF:Q4_K_M --host 0.0.0.0
```

Result:
- Tokens: 10,492 tokens
- Time: 1h 41min 42s
- 1.72 t/s (avg. started ~3-4 t/s)

[Result Output](./prompt-results/attempt-1.md)

## Attempt 2

Executor: llama.cpp
Model: TeichAI/Qwen3-14B-Claude-4.5-Opus-High-Reasoning-Distill-GGUF:Q4_K_M
Hardware: Intel i7 4790k, 16GB DDR3 1600

Command:

```bash
meder@liquidwhite:bin$ ./llama-server -hf Qwen/Qwen2.5-Coder-7B-Instruct-GGUF:Q4_K_M --host 0.0.0.0
```

Result:
- Tokens: 446 tokens
- Time: 1min 4s
- 6.94 t/s

[Result Output](./prompt-results/attempt-2.md)
