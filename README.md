# Faster CPython Benchmark Infrastructure

🔒 [▶️ START A BENCHMARK RUN](../../actions/workflows/benchmark.yml)

## Results

Here are some recent and important revisions. 👉 [Complete list of results](RESULTS.md).

[Currently failing benchmarks](failures.md).

**Key:** 📄: table, 📈: time plot, 🧠: memory plot

<!-- START table -->
- [Most recent  pystats on main (800d37f)](results/bm-20250719-3.15.0a0-800d37f/bm-20250719-azure-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f-pystats.md)
- [Most recent PYTHON_UOPS pystats on main (800d37f)](results/bm-20250719-3.15.0a0-800d37f-PYTHON_UOPS/bm-20250719-azure-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f-pystats.md)
- [Most recent JIT pystats on main (0240ef4)](results/bm-20250707-3.15.0a0-0240ef4-JIT/bm-20250707-azure-x86_64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4-pystats.md)

## linux aarch64 (arminc)
| date | fork/ref | hash/flags | vs. 3.10.4: | vs. 3.12.0: | vs. 3.13.0: | vs. base: |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| [2025-07-26](results/bm-20250726-3.15.0a0-a852c7b-NOGIL) | python/a852c7bdd48979218a0c | a852c7b (NOGIL) | 1.141x ↑<br>[📄](results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.10.4.md)[📈](results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.10.4.svg) | 1.087x ↓<br>[📄](results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.12.0.md)[📈](results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.12.0.svg) | 1.098x ↓<br>[📄](results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.13.0.md)[📈](results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.13.0.svg) | 1.126x ↓<br>[📄](results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-base.md)[📈](results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-base.svg)[🧠](results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-base-mem.svg) |
| [2025-07-26](results/bm-20250726-3.15.0a0-a852c7b-JIT) | python/a852c7bdd48979218a0c | a852c7b (JIT) | 1.288x ↑<br>[📄](results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.10.4.md)[📈](results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.10.4.svg) | 1.018x ↑<br>[📄](results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.12.0.md)[📈](results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.12.0.svg) | 1.010x ↑<br>[📄](results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.13.0.md)[📈](results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.13.0.svg) | 1.013x ↓<br>[📄](results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-base.md)[📈](results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-base.svg)[🧠](results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-base-mem.svg) |
| [2025-07-26](results/bm-20250726-3.15.0a0-a852c7b) | python/a852c7bdd48979218a0c | a852c7b | 1.308x ↑<br>[📄](results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.10.4.md)[📈](results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.10.4.svg) | 1.036x ↑<br>[📄](results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.12.0.md)[📈](results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.12.0.svg) | 1.027x ↑<br>[📄](results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.13.0.md)[📈](results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.13.0.svg) |  |
| [2025-07-25](results/bm-20250725-3.15.0a0-a6ef3b7-JIT) | brandtbucher/jit_shim | a6ef3b7 (JIT) | 1.295x ↑<br>[📄](results/bm-20250725-3.15.0a0-a6ef3b7-JIT/bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-3.10.4.md)[📈](results/bm-20250725-3.15.0a0-a6ef3b7-JIT/bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-3.10.4.svg) | 1.024x ↑<br>[📄](results/bm-20250725-3.15.0a0-a6ef3b7-JIT/bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-3.12.0.md)[📈](results/bm-20250725-3.15.0a0-a6ef3b7-JIT/bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-3.12.0.svg) | 1.015x ↑<br>[📄](results/bm-20250725-3.15.0a0-a6ef3b7-JIT/bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-3.13.0.md)[📈](results/bm-20250725-3.15.0a0-a6ef3b7-JIT/bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-3.13.0.svg) | 1.003x ↑<br>[📄](results/bm-20250725-3.15.0a0-a6ef3b7-JIT/bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-base.md)[📈](results/bm-20250725-3.15.0a0-a6ef3b7-JIT/bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-base.svg)[🧠](results/bm-20250725-3.15.0a0-a6ef3b7-JIT/bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-base-mem.svg) |
| [2025-07-25](results/bm-20250725-3.15.0a0-1e69cd1-JIT) | python/1e69cd1634e4f0f8c375 | 1e69cd1 (JIT) | 1.283x ↑<br>[📄](results/bm-20250725-3.15.0a0-1e69cd1-JIT/bm-20250725-arminc-aarch64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1-vs-3.10.4.md)[📈](results/bm-20250725-3.15.0a0-1e69cd1-JIT/bm-20250725-arminc-aarch64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1-vs-3.10.4.svg) | 1.016x ↑<br>[📄](results/bm-20250725-3.15.0a0-1e69cd1-JIT/bm-20250725-arminc-aarch64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1-vs-3.12.0.md)[📈](results/bm-20250725-3.15.0a0-1e69cd1-JIT/bm-20250725-arminc-aarch64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1-vs-3.12.0.svg) | 1.007x ↑<br>[📄](results/bm-20250725-3.15.0a0-1e69cd1-JIT/bm-20250725-arminc-aarch64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1-vs-3.13.0.md)[📈](results/bm-20250725-3.15.0a0-1e69cd1-JIT/bm-20250725-arminc-aarch64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1-vs-3.13.0.svg) |  |

## linux aarch64 (arminc_clang)
| date | fork/ref | hash/flags | vs. 3.10.4: | vs. 3.12.0: | vs. 3.13.0: | vs. base: |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| [2025-05-24](results/bm-20250524-3.15.0a0-2fd09b0-TAILCALL) | python/2fd09b011031f3c00c34 | 2fd09b0 (TAILCALL) |  |  |  |  |
| [2025-05-18](results/bm-20250518-3.15.0a0-009e7b3-TAILCALL) | python/009e7b36981fd07f7cca | 009e7b3 (TAILCALL) |  |  |  |  |
| [2025-05-10](results/bm-20250510-3.15.0a0-1a87b6e-TAILCALL) | python/1a87b6e9ae6da255f304 | 1a87b6e (TAILCALL) |  |  |  |  |

## linux x86_64 (linux)
| date | fork/ref | hash/flags | vs. 3.10.4: | vs. 3.12.0: | vs. 3.13.0: | vs. base: |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| [2025-07-02](results/bm-20250702-3.15.0a0-fa43a1e-JIT) | python/fa43a1e0f8caf00a1589 | fa43a1e (JIT) | 1.422x ↑<br>[📄](results/bm-20250702-3.15.0a0-fa43a1e-JIT/bm-20250702-linux-x86_64-python-fa43a1e0f8caf00a1589-3.15.0a0-fa43a1e-vs-3.10.4.md)[📈](results/bm-20250702-3.15.0a0-fa43a1e-JIT/bm-20250702-linux-x86_64-python-fa43a1e0f8caf00a1589-3.15.0a0-fa43a1e-vs-3.10.4.svg) | 1.093x ↑<br>[📄](results/bm-20250702-3.15.0a0-fa43a1e-JIT/bm-20250702-linux-x86_64-python-fa43a1e0f8caf00a1589-3.15.0a0-fa43a1e-vs-3.12.0.md)[📈](results/bm-20250702-3.15.0a0-fa43a1e-JIT/bm-20250702-linux-x86_64-python-fa43a1e0f8caf00a1589-3.15.0a0-fa43a1e-vs-3.12.0.svg) | 1.024x ↑<br>[📄](results/bm-20250702-3.15.0a0-fa43a1e-JIT/bm-20250702-linux-x86_64-python-fa43a1e0f8caf00a1589-3.15.0a0-fa43a1e-vs-3.13.0.md)[📈](results/bm-20250702-3.15.0a0-fa43a1e-JIT/bm-20250702-linux-x86_64-python-fa43a1e0f8caf00a1589-3.15.0a0-fa43a1e-vs-3.13.0.svg) |  |
| [2025-07-02](results/bm-20250702-3.15.0a0-ebec717-JIT) | brandtbucher/jit_up_6_12 | ebec717 (JIT) | 1.424x ↑<br>[📄](results/bm-20250702-3.15.0a0-ebec717-JIT/bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717-vs-3.10.4.md)[📈](results/bm-20250702-3.15.0a0-ebec717-JIT/bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717-vs-3.10.4.svg) | 1.094x ↑<br>[📄](results/bm-20250702-3.15.0a0-ebec717-JIT/bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717-vs-3.12.0.md)[📈](results/bm-20250702-3.15.0a0-ebec717-JIT/bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717-vs-3.12.0.svg) | 1.025x ↑<br>[📄](results/bm-20250702-3.15.0a0-ebec717-JIT/bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717-vs-3.13.0.md)[📈](results/bm-20250702-3.15.0a0-ebec717-JIT/bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717-vs-3.13.0.svg) | 1.001x ↑<br>[📄](results/bm-20250702-3.15.0a0-ebec717-JIT/bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717-vs-base.md)[📈](results/bm-20250702-3.15.0a0-ebec717-JIT/bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717-vs-base.svg)[🧠](results/bm-20250702-3.15.0a0-ebec717-JIT/bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717-vs-base-mem.svg) |
| [2025-07-02](results/bm-20250702-3.15.0a0-6c99b17-JIT) | brandtbucher/jit_up_6_6 | 6c99b17 (JIT) | 1.421x ↑<br>[📄](results/bm-20250702-3.15.0a0-6c99b17-JIT/bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17-vs-3.10.4.md)[📈](results/bm-20250702-3.15.0a0-6c99b17-JIT/bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17-vs-3.10.4.svg) | 1.092x ↑<br>[📄](results/bm-20250702-3.15.0a0-6c99b17-JIT/bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17-vs-3.12.0.md)[📈](results/bm-20250702-3.15.0a0-6c99b17-JIT/bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17-vs-3.12.0.svg) | 1.023x ↑<br>[📄](results/bm-20250702-3.15.0a0-6c99b17-JIT/bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17-vs-3.13.0.md)[📈](results/bm-20250702-3.15.0a0-6c99b17-JIT/bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17-vs-3.13.0.svg) | 1.000x ↓<br>[📄](results/bm-20250702-3.15.0a0-6c99b17-JIT/bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17-vs-base.md)[📈](results/bm-20250702-3.15.0a0-6c99b17-JIT/bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17-vs-base.svg)[🧠](results/bm-20250702-3.15.0a0-6c99b17-JIT/bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17-vs-base-mem.svg) |

## linux x86_64 (linux_clang)
| date | fork/ref | hash/flags | vs. 3.10.4: | vs. 3.12.0: | vs. 3.13.0: | vs. base: |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| [2025-06-30](results/bm-20250630-3.15.0a0-75f4059-TAILCALL) | python/75f40595e555e7d016cf | 75f4059 (TAILCALL) |  |  |  |  |
| [2025-06-21](results/bm-20250621-3.15.0a0-b14986c-TAILCALL) | python/b14986c91464b06e9016 | b14986c (TAILCALL) |  |  |  |  |
| [2025-06-17](results/bm-20250617-3.15.0a0-fba5dde-TAILCALL) | python/fba5dded6df3c2b19435 | fba5dde (TAILCALL) |  |  |  |  |

## linux x86_64 (pythonperf2)
| date | fork/ref | hash/flags | vs. 3.10.4: | vs. 3.12.0: | vs. 3.13.0: | vs. base: |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| [2025-07-26](results/bm-20250726-3.15.0a0-a852c7b-NOGIL) | python/a852c7bdd48979218a0c | a852c7b (NOGIL) | 1.201x ↑<br>[📄](results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-pythonperf2-x86_64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.10.4.md)[📈](results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-pythonperf2-x86_64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.10.4.svg) | 1.051x ↓<br>[📄](results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-pythonperf2-x86_64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.12.0.md)[📈](results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-pythonperf2-x86_64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.12.0.svg) | 1.051x ↓<br>[📄](results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-pythonperf2-x86_64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.13.0.md)[📈](results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-pythonperf2-x86_64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.13.0.svg) | 1.086x ↓<br>[📄](results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-pythonperf2-x86_64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-base.md)[📈](results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-pythonperf2-x86_64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-base.svg)[🧠](results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-pythonperf2-x86_64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-base-mem.svg) |
| [2025-07-26](results/bm-20250726-3.15.0a0-a852c7b-JIT) | python/a852c7bdd48979218a0c | a852c7b (JIT) | 1.332x ↑<br>[📄](results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-pythonperf2-x86_64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.10.4.md)[📈](results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-pythonperf2-x86_64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.10.4.svg) | 1.035x ↑<br>[📄](results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-pythonperf2-x86_64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.12.0.md)[📈](results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-pythonperf2-x86_64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.12.0.svg) | 1.041x ↑<br>[📄](results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-pythonperf2-x86_64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.13.0.md)[📈](results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-pythonperf2-x86_64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.13.0.svg) | 1.005x ↑<br>[📄](results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-pythonperf2-x86_64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-base.md)[📈](results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-pythonperf2-x86_64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-base.svg)[🧠](results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-pythonperf2-x86_64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-base-mem.svg) |
| [2025-07-26](results/bm-20250726-3.15.0a0-a852c7b) | python/a852c7bdd48979218a0c | a852c7b | 1.325x ↑<br>[📄](results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-pythonperf2-x86_64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.10.4.md)[📈](results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-pythonperf2-x86_64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.10.4.svg) | 1.028x ↑<br>[📄](results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-pythonperf2-x86_64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.12.0.md)[📈](results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-pythonperf2-x86_64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.12.0.svg) | 1.035x ↑<br>[📄](results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-pythonperf2-x86_64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.13.0.md)[📈](results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-pythonperf2-x86_64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.13.0.svg) |  |

## linux x86_64 (pythonperf2_clang)
| date | fork/ref | hash/flags | vs. 3.10.4: | vs. 3.12.0: | vs. 3.13.0: | vs. base: |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| [2025-07-08](results/bm-20250708-3.15.0a0-997a858-JIT) | brandtbucher/jit_targets | 997a858 (JIT) |  |  |  | 1.003x ↓<br>[📄](results/bm-20250708-3.15.0a0-997a858-JIT/bm-20250708-pythonperf2_clang-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-base.md)[📈](results/bm-20250708-3.15.0a0-997a858-JIT/bm-20250708-pythonperf2_clang-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-base.svg)[🧠](results/bm-20250708-3.15.0a0-997a858-JIT/bm-20250708-pythonperf2_clang-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-base-mem.svg) |
| [2025-07-07](results/bm-20250707-3.15.0a0-0240ef4-JIT) | python/0240ef4705d835e27beb | 0240ef4 (JIT) |  |  |  |  |
| [2025-06-28](results/bm-20250628-3.15.0a0-6448067-JIT) | brandtbucher/jit_oz | 6448067 (JIT) |  |  |  | 1.015x ↓<br>[📄](results/bm-20250628-3.15.0a0-6448067-JIT/bm-20250628-pythonperf2_clang-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067-vs-base.md)[📈](results/bm-20250628-3.15.0a0-6448067-JIT/bm-20250628-pythonperf2_clang-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067-vs-base.svg)[🧠](results/bm-20250628-3.15.0a0-6448067-JIT/bm-20250628-pythonperf2_clang-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067-vs-base-mem.svg) |

## windows amd64 (pythonperf1)
| date | fork/ref | hash/flags | vs. 3.10.4: | vs. 3.12.0: | vs. 3.13.0: | vs. base: |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| [2025-07-26](results/bm-20250726-3.15.0a0-a852c7b-NOGIL) | python/a852c7bdd48979218a0c | a852c7b (NOGIL) | 1.118x ↑<br>[📄](results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.10.4.md)[📈](results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.10.4.svg) | 1.034x ↓<br>[📄](results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.12.0.md)[📈](results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.12.0.svg) | 1.090x ↓<br>[📄](results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.13.0.md)[📈](results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.13.0.svg) | 1.119x ↓<br>[📄](results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-base.md)[📈](results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-base.svg) |
| [2025-07-26](results/bm-20250726-3.15.0a0-a852c7b-JIT) | python/a852c7bdd48979218a0c | a852c7b (JIT) | 1.302x ↑<br>[📄](results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.10.4.md)[📈](results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.10.4.svg) | 1.111x ↑<br>[📄](results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.12.0.md)[📈](results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.12.0.svg) | 1.066x ↑<br>[📄](results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.13.0.md)[📈](results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.13.0.svg) | 1.033x ↑<br>[📄](results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-base.md)[📈](results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-base.svg) |
| [2025-07-26](results/bm-20250726-3.15.0a0-a852c7b) | python/a852c7bdd48979218a0c | a852c7b | 1.258x ↑<br>[📄](results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.10.4.md)[📈](results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.10.4.svg) | 1.073x ↑<br>[📄](results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.12.0.md)[📈](results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.12.0.svg) | 1.033x ↑<br>[📄](results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.13.0.md)[📈](results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.13.0.svg) |  |
| [2025-07-25](results/bm-20250725-3.15.0a0-a6ef3b7-JIT) | brandtbucher/jit_shim | a6ef3b7 (JIT) | 1.300x ↑<br>[📄](results/bm-20250725-3.15.0a0-a6ef3b7-JIT/bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-3.10.4.md)[📈](results/bm-20250725-3.15.0a0-a6ef3b7-JIT/bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-3.10.4.svg) | 1.107x ↑<br>[📄](results/bm-20250725-3.15.0a0-a6ef3b7-JIT/bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-3.12.0.md)[📈](results/bm-20250725-3.15.0a0-a6ef3b7-JIT/bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-3.12.0.svg) | 1.064x ↑<br>[📄](results/bm-20250725-3.15.0a0-a6ef3b7-JIT/bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-3.13.0.md)[📈](results/bm-20250725-3.15.0a0-a6ef3b7-JIT/bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-3.13.0.svg) | 1.002x ↓<br>[📄](results/bm-20250725-3.15.0a0-a6ef3b7-JIT/bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-base.md)[📈](results/bm-20250725-3.15.0a0-a6ef3b7-JIT/bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-base.svg) |
| [2025-07-25](results/bm-20250725-3.15.0a0-1e69cd1-JIT) | python/1e69cd1634e4f0f8c375 | 1e69cd1 (JIT) | 1.307x ↑<br>[📄](results/bm-20250725-3.15.0a0-1e69cd1-JIT/bm-20250725-pythonperf1-amd64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1-vs-3.10.4.md)[📈](results/bm-20250725-3.15.0a0-1e69cd1-JIT/bm-20250725-pythonperf1-amd64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1-vs-3.10.4.svg) | 1.114x ↑<br>[📄](results/bm-20250725-3.15.0a0-1e69cd1-JIT/bm-20250725-pythonperf1-amd64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1-vs-3.12.0.md)[📈](results/bm-20250725-3.15.0a0-1e69cd1-JIT/bm-20250725-pythonperf1-amd64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1-vs-3.12.0.svg) | 1.069x ↑<br>[📄](results/bm-20250725-3.15.0a0-1e69cd1-JIT/bm-20250725-pythonperf1-amd64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1-vs-3.13.0.md)[📈](results/bm-20250725-3.15.0a0-1e69cd1-JIT/bm-20250725-pythonperf1-amd64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1-vs-3.13.0.svg) |  |
| [2025-07-25](results/bm-20250725-3.15.0a0-021fc09-PYTHON_UOPS) | faster-cpython/check_periodic_at_en | 021fc09 (T2) | 1.156x ↑<br>[📄](results/bm-20250725-3.15.0a0-021fc09-PYTHON_UOPS/bm-20250725-pythonperf1-amd64-faster%252dcpython-check_periodic_at_en-3.15.0a0-021fc09-vs-3.10.4.md)[📈](results/bm-20250725-3.15.0a0-021fc09-PYTHON_UOPS/bm-20250725-pythonperf1-amd64-faster%252dcpython-check_periodic_at_en-3.15.0a0-021fc09-vs-3.10.4.svg) | 1.016x ↓<br>[📄](results/bm-20250725-3.15.0a0-021fc09-PYTHON_UOPS/bm-20250725-pythonperf1-amd64-faster%252dcpython-check_periodic_at_en-3.15.0a0-021fc09-vs-3.12.0.md)[📈](results/bm-20250725-3.15.0a0-021fc09-PYTHON_UOPS/bm-20250725-pythonperf1-amd64-faster%252dcpython-check_periodic_at_en-3.15.0a0-021fc09-vs-3.12.0.svg) | 1.050x ↓<br>[📄](results/bm-20250725-3.15.0a0-021fc09-PYTHON_UOPS/bm-20250725-pythonperf1-amd64-faster%252dcpython-check_periodic_at_en-3.15.0a0-021fc09-vs-3.13.0.md)[📈](results/bm-20250725-3.15.0a0-021fc09-PYTHON_UOPS/bm-20250725-pythonperf1-amd64-faster%252dcpython-check_periodic_at_en-3.15.0a0-021fc09-vs-3.13.0.svg) |  |

## windows amd64 (pythonperf1_clang)
| date | fork/ref | hash/flags | vs. 3.10.4: | vs. 3.12.0: | vs. 3.13.0: | vs. base: |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| [2025-07-26](results/bm-20250726-3.15.0a0-a852c7b-TAILCALL) | python/a852c7bdd48979218a0c | a852c7b (TAILCALL) |  |  |  |  |
| [2025-07-19](results/bm-20250719-3.15.0a0-800d37f-TAILCALL) | python/800d37feca2e0ea33439 | 800d37f (TAILCALL) |  |  |  |  |
| [2025-07-12](results/bm-20250712-3.15.0a0-47b01da-TAILCALL) | python/47b01da4ccedd9c00fad | 47b01da (TAILCALL) |  |  |  |  |

## windows amd64 (pythonperf1_win32)
| date | fork/ref | hash/flags | vs. 3.10.4: | vs. 3.12.0: | vs. 3.13.0: | vs. base: |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| [2025-07-26](results/bm-20250726-3.15.0a0-a852c7b-NOGIL) | python/a852c7bdd48979218a0c | a852c7b (NOGIL) | 1.272x ↑<br>[📄](results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.10.4.md)[📈](results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.10.4.svg) | 1.306x ↑<br>[📄](results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.12.0.md)[📈](results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.12.0.svg) | 1.103x ↑<br>[📄](results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.13.0.md)[📈](results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.13.0.svg) | 1.106x ↓<br>[📄](results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-base.md)[📈](results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-base.svg) |
| [2025-07-26](results/bm-20250726-3.15.0a0-a852c7b-JIT) | python/a852c7bdd48979218a0c | a852c7b (JIT) | 1.458x ↑<br>[📄](results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.10.4.md)[📈](results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.10.4.svg) | 1.478x ↑<br>[📄](results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.12.0.md)[📈](results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.12.0.svg) | 1.275x ↑<br>[📄](results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.13.0.md)[📈](results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.13.0.svg) | 1.034x ↑<br>[📄](results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-base.md)[📈](results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-base.svg) |
| [2025-07-26](results/bm-20250726-3.15.0a0-a852c7b) | python/a852c7bdd48979218a0c | a852c7b | 1.408x ↑<br>[📄](results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.10.4.md)[📈](results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.10.4.svg) | 1.425x ↑<br>[📄](results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.12.0.md)[📈](results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.12.0.svg) | 1.233x ↑<br>[📄](results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.13.0.md)[📈](results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.13.0.svg) |  |

## windows amd64 (pythonperf1_win32_clang)
| date | fork/ref | hash/flags | vs. 3.10.4: | vs. 3.12.0: | vs. 3.13.0: | vs. base: |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| [2025-07-26](results/bm-20250726-3.15.0a0-a852c7b-TAILCALL) | python/a852c7bdd48979218a0c | a852c7b (TAILCALL) |  |  |  |  |
| [2025-07-19](results/bm-20250719-3.15.0a0-800d37f-TAILCALL) | python/800d37feca2e0ea33439 | 800d37f (TAILCALL) |  |  |  |  |
| [2025-07-12](results/bm-20250712-3.15.0a0-47b01da-TAILCALL) | python/47b01da4ccedd9c00fad | 47b01da (TAILCALL) |  |  |  |  |

## windows x86 (pythonperf1_win32)
| date | fork/ref | hash/flags | vs. 3.10.4: | vs. 3.12.0: | vs. 3.13.0: | vs. base: |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| [2025-05-24](results/bm-20250524-3.15.0a0-2fd09b0-NOGIL) | python/2fd09b011031f3c00c34 | 2fd09b0 (NOGIL) | 1.052x ↑<br>[📄](results/bm-20250524-3.15.0a0-2fd09b0-NOGIL/bm-20250524-pythonperf1_win32-x86-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.10.4.md)[📈](results/bm-20250524-3.15.0a0-2fd09b0-NOGIL/bm-20250524-pythonperf1_win32-x86-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.10.4.svg) | 1.085x ↑<br>[📄](results/bm-20250524-3.15.0a0-2fd09b0-NOGIL/bm-20250524-pythonperf1_win32-x86-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.12.0.md)[📈](results/bm-20250524-3.15.0a0-2fd09b0-NOGIL/bm-20250524-pythonperf1_win32-x86-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.12.0.svg) | 1.067x ↓<br>[📄](results/bm-20250524-3.15.0a0-2fd09b0-NOGIL/bm-20250524-pythonperf1_win32-x86-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.13.0.md)[📈](results/bm-20250524-3.15.0a0-2fd09b0-NOGIL/bm-20250524-pythonperf1_win32-x86-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.13.0.svg) |  |
| [2025-05-10](results/bm-20250510-3.15.0a0-1a87b6e-NOGIL) | python/1a87b6e9ae6da255f304 | 1a87b6e (NOGIL) | 1.013x ↑<br>[📄](results/bm-20250510-3.15.0a0-1a87b6e-NOGIL/bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.10.4.md)[📈](results/bm-20250510-3.15.0a0-1a87b6e-NOGIL/bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.10.4.svg) | 1.046x ↑<br>[📄](results/bm-20250510-3.15.0a0-1a87b6e-NOGIL/bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.12.0.md)[📈](results/bm-20250510-3.15.0a0-1a87b6e-NOGIL/bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.12.0.svg) | 1.101x ↓<br>[📄](results/bm-20250510-3.15.0a0-1a87b6e-NOGIL/bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.13.0.md)[📈](results/bm-20250510-3.15.0a0-1a87b6e-NOGIL/bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.13.0.svg) | 1.123x ↓<br>[📄](results/bm-20250510-3.15.0a0-1a87b6e-NOGIL/bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-base.md)[📈](results/bm-20250510-3.15.0a0-1a87b6e-NOGIL/bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-base.svg) |
| [2025-05-10](results/bm-20250510-3.15.0a0-1a87b6e-JIT) | python/1a87b6e9ae6da255f304 | 1a87b6e (JIT) | 1.069x ↑<br>[📄](results/bm-20250510-3.15.0a0-1a87b6e-JIT/bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.10.4.md)[📈](results/bm-20250510-3.15.0a0-1a87b6e-JIT/bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.10.4.svg) | 1.090x ↑<br>[📄](results/bm-20250510-3.15.0a0-1a87b6e-JIT/bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.12.0.md)[📈](results/bm-20250510-3.15.0a0-1a87b6e-JIT/bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.12.0.svg) | 1.036x ↓<br>[📄](results/bm-20250510-3.15.0a0-1a87b6e-JIT/bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.13.0.md)[📈](results/bm-20250510-3.15.0a0-1a87b6e-JIT/bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.13.0.svg) | 1.061x ↓<br>[📄](results/bm-20250510-3.15.0a0-1a87b6e-JIT/bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-base.md)[📈](results/bm-20250510-3.15.0a0-1a87b6e-JIT/bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-base.svg) |

## windows x86 (pythonperf1_win32_clang)
| date | fork/ref | hash/flags | vs. 3.10.4: | vs. 3.12.0: | vs. 3.13.0: | vs. base: |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| [2025-03-08](results/bm-20250308-3.14.0a5%2B-a3990df-TAILCALL) | python/a3990df6121880e8c678 | a3990df (TAILCALL) |  |  |  |  |
| [2025-03-06](results/bm-20250306-3.14.0a5%2B-37fb620-TAILCALL) | Fidget-Spinner/clang_hot | 37fb620 (TAILCALL) |  |  |  |  |
| [2025-03-01](results/bm-20250301-3.14.0a5%2B-c9932a9-TAILCALL) | python/c9932a9ec8a3077933a8 | c9932a9 (TAILCALL) |  |  |  |  |

## darwin arm64 (darwin)
| date | fork/ref | hash/flags | vs. 3.10.4: | vs. 3.12.0: | vs. 3.13.0: | vs. base: |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| [2025-07-28](results/bm-20250728-3.15.0a0-0887346-JIT) | brandtbucher/macos_10_15 | 0887346 (JIT) | 1.350x ↑<br>[📄](results/bm-20250728-3.15.0a0-0887346-JIT/bm-20250728-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-0887346-vs-3.10.4.md)[📈](results/bm-20250728-3.15.0a0-0887346-JIT/bm-20250728-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-0887346-vs-3.10.4.svg) | 1.065x ↑<br>[📄](results/bm-20250728-3.15.0a0-0887346-JIT/bm-20250728-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-0887346-vs-3.12.0.md)[📈](results/bm-20250728-3.15.0a0-0887346-JIT/bm-20250728-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-0887346-vs-3.12.0.svg) | 1.067x ↑<br>[📄](results/bm-20250728-3.15.0a0-0887346-JIT/bm-20250728-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-0887346-vs-3.13.0.md)[📈](results/bm-20250728-3.15.0a0-0887346-JIT/bm-20250728-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-0887346-vs-3.13.0.svg) | 1.140x ↑<br>[📄](results/bm-20250728-3.15.0a0-0887346-JIT/bm-20250728-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-0887346-vs-base.md)[📈](results/bm-20250728-3.15.0a0-0887346-JIT/bm-20250728-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-0887346-vs-base.svg)[🧠](results/bm-20250728-3.15.0a0-0887346-JIT/bm-20250728-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-0887346-vs-base-mem.svg) |
| [2025-07-26](results/bm-20250726-3.15.0a0-a852c7b-NOGIL) | python/a852c7bdd48979218a0c | a852c7b (NOGIL) | 1.133x ↑<br>[📄](results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-darwin-arm64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.10.4.md)[📈](results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-darwin-arm64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.10.4.svg) | 1.089x ↓<br>[📄](results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-darwin-arm64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.12.0.md)[📈](results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-darwin-arm64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.12.0.svg) | 1.087x ↓<br>[📄](results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-darwin-arm64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.13.0.md)[📈](results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-darwin-arm64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.13.0.svg) | 1.019x ↓<br>[📄](results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-darwin-arm64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-base.md)[📈](results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-darwin-arm64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-base.svg)[🧠](results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-darwin-arm64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-base-mem.svg) |
| [2025-07-26](results/bm-20250726-3.15.0a0-a852c7b-JIT) | python/a852c7bdd48979218a0c | a852c7b (JIT) | 1.192x ↑<br>[📄](results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-darwin-arm64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.10.4.md)[📈](results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-darwin-arm64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.10.4.svg) | 1.058x ↓<br>[📄](results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-darwin-arm64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.12.0.md)[📈](results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-darwin-arm64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.12.0.svg) | 1.056x ↓<br>[📄](results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-darwin-arm64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.13.0.md)[📈](results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-darwin-arm64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.13.0.svg) | 1.016x ↑<br>[📄](results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-darwin-arm64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-base.md)[📈](results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-darwin-arm64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-base.svg)[🧠](results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-darwin-arm64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-base-mem.svg) |
| [2025-07-26](results/bm-20250726-3.15.0a0-a852c7b) | python/a852c7bdd48979218a0c | a852c7b | 1.173x ↑<br>[📄](results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-darwin-arm64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.10.4.md)[📈](results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-darwin-arm64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.10.4.svg) | 1.073x ↓<br>[📄](results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-darwin-arm64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.12.0.md)[📈](results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-darwin-arm64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.12.0.svg) | 1.071x ↓<br>[📄](results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-darwin-arm64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.13.0.md)[📈](results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-darwin-arm64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b-vs-3.13.0.svg) |  |
| [2025-07-25](results/bm-20250725-3.15.0a0-a6ef3b7-JIT) | brandtbucher/jit_shim | a6ef3b7 (JIT) | 1.190x ↑<br>[📄](results/bm-20250725-3.15.0a0-a6ef3b7-JIT/bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-3.10.4.md)[📈](results/bm-20250725-3.15.0a0-a6ef3b7-JIT/bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-3.10.4.svg) | 1.062x ↓<br>[📄](results/bm-20250725-3.15.0a0-a6ef3b7-JIT/bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-3.12.0.md)[📈](results/bm-20250725-3.15.0a0-a6ef3b7-JIT/bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-3.12.0.svg) | 1.060x ↓<br>[📄](results/bm-20250725-3.15.0a0-a6ef3b7-JIT/bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-3.13.0.md)[📈](results/bm-20250725-3.15.0a0-a6ef3b7-JIT/bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-3.13.0.svg) | 1.004x ↑<br>[📄](results/bm-20250725-3.15.0a0-a6ef3b7-JIT/bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-base.md)[📈](results/bm-20250725-3.15.0a0-a6ef3b7-JIT/bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-base.svg)[🧠](results/bm-20250725-3.15.0a0-a6ef3b7-JIT/bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-base-mem.svg) |
| [2025-07-25](results/bm-20250725-3.15.0a0-1e69cd1-JIT) | python/1e69cd1634e4f0f8c375 | 1e69cd1 (JIT) | 1.185x ↑<br>[📄](results/bm-20250725-3.15.0a0-1e69cd1-JIT/bm-20250725-darwin-arm64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1-vs-3.10.4.md)[📈](results/bm-20250725-3.15.0a0-1e69cd1-JIT/bm-20250725-darwin-arm64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1-vs-3.10.4.svg) | 1.065x ↓<br>[📄](results/bm-20250725-3.15.0a0-1e69cd1-JIT/bm-20250725-darwin-arm64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1-vs-3.12.0.md)[📈](results/bm-20250725-3.15.0a0-1e69cd1-JIT/bm-20250725-darwin-arm64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1-vs-3.12.0.svg) | 1.064x ↓<br>[📄](results/bm-20250725-3.15.0a0-1e69cd1-JIT/bm-20250725-darwin-arm64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1-vs-3.13.0.md)[📈](results/bm-20250725-3.15.0a0-1e69cd1-JIT/bm-20250725-darwin-arm64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1-vs-3.13.0.svg) |  |

## darwin arm64 (darwin_clang)
| date | fork/ref | hash/flags | vs. 3.10.4: | vs. 3.12.0: | vs. 3.13.0: | vs. base: |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| [2025-07-26](results/bm-20250726-3.15.0a0-a852c7b-TAILCALL) | python/a852c7bdd48979218a0c | a852c7b (TAILCALL) |  |  |  |  |
| [2025-07-12](results/bm-20250712-3.15.0a0-47b01da-TAILCALL) | python/47b01da4ccedd9c00fad | 47b01da (TAILCALL) |  |  |  |  |
| [2025-07-08](results/bm-20250708-3.15.0a0-997a858-JIT) | brandtbucher/jit_targets | 997a858 (JIT) |  |  |  | 1.017x ↑<br>[📄](results/bm-20250708-3.15.0a0-997a858-JIT/bm-20250708-darwin_clang-arm64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-base.md)[📈](results/bm-20250708-3.15.0a0-997a858-JIT/bm-20250708-darwin_clang-arm64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-base.svg)[🧠](results/bm-20250708-3.15.0a0-997a858-JIT/bm-20250708-darwin_clang-arm64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-base-mem.svg) |


<!-- END table -->

`*` indicates that the exact same versions of pyperformance was not used.

For the results above, the "faster/slower" result is a geometric mean of each of the benchmarks.

## Longitudinal results

Below are longitudinal timing results. There are also [🧠 longitudinal memory results](memory.md).

![Longitudinal speed improvement](/longitudinal.svg)

![Effect of different configurations](/configs.svg)

The results have a resolution of 0.001 (0.1%).

- linux: Intel® Xeon® W-2255 CPU @ 3.70GHz, running Ubuntu 20.04 LTS, gcc 9.4.0
- linux2: 12th Gen Intel® Core™ i9-12900 @ 2.40 GHz, running Ubuntu 22.04 LTS, gcc 11.3.0
- linux-aarch64: ARM Neoverse N1, running Ubuntu 22.04 LTS, gcc 11.4.0
- macos: M1 arm64 Mac® Mini, running macOS 13.2.1, clang 1400.0.29.202
- windows: 12th Gen Intel® Core™ i9-12900 @ 2.40 GHz, running Windows 11 Pro (21H2, 22000.1696), MSVC v143

## Data changes

This is a CHANGELOG of how any derived data has changed:

- 2024-11-26: The longitudinal plots and index tables now use geometric mean rather than HPT.
- 2024-06-27: The HPT values (and the longitudinal plots that are based on them) now correctly exclude any benchmarks in `excluded_benchmarks.txt`.

## Documentation

### Running benchmarks from the GitHub web UI

Visit the 🔒 [benchmark action](../../actions/workflows/benchmark.yml) and click the "Run Workflow" button.

The available parameters are:

- `fork`: The fork of CPython to benchmark.
  If benchmarking a pull request, this would normally be your GitHub username.
- `ref`: The branch, tag or commit SHA to benchmark.
  If a SHA, it must be the full SHA, since finding it by a prefix is not supported.
- `machine`: The machine to run on.
  One of `linux-amd64` (default), `windows-amd64`, `darwin-arm64` or `all`.
- `benchmark_base`: If checked, the base of the selected branch will also be benchmarked.
  The base is determined by running `git merge-base upstream/main $ref`.
- `pystats`: If checked, collect the pystats from running the benchmarks.
- A choice of configurations (documented below).

To watch the progress of the benchmark, select it from the 🔒 [benchmark action page](../../actions/workflows/benchmark.yml).
It may be canceled from there as well.
To show only your benchmark workflows, select your GitHub ID from the "Actor" dropdown.

When the benchmarking is complete, the results are published to this repository and will appear in the [master table](RESULTS.md).
Each set of benchmarks will have:

- The raw `.json` results from pyperformance.
- Comparisons against important reference releases, as well as the merge base of the branch if `benchmark_base` was selected. These include
  - A markdown table produced by `pyperf compare_to`.
  - A set of "violin" plots showing the distribution of results for each benchmark.
  - A set of plots showing the memory change for each benchmark (for immediate bases only, on non-Windows platforms).

The most convenient way to get results locally is to clone this repo and `git pull` from it.

### Running benchmarks from the GitHub CLI

To automate benchmarking runs, it may be more convenient to use the [GitHub CLI](https://cli.github.com/).
Once you have `gh` installed and configured, you can run benchmarks by cloning this repository and then from inside it:

```bash
$ gh workflow run benchmark.yml -f fork=me -f ref=my_branch
```

Any of the parameters described above are available at the commandline using the `-f key=value` syntax.

### Collecting Linux perf profiling data

To collect Linux perf sampling profile data for a benchmarking run, run the `_benchmark` action and check the `perf` checkbox.

The results will be available as "artifacts" on the run page after the run -- they are not committed directly to the repository.

The `python -m bench_runner profiling_plot` command can be used to turn the raw perf results into tables and graphs.

### Creating a custom comparison

If the default comparisons generated by this tool aren't sufficient, you can check
out the repo and use the same infrastructure to generate any arbitrary
comparison.

Check out a local copy of this repo:

```sh
$ git clone https://github.com/faster-cpython/benchmarking-public
```

Create a new virtual environment, activate it and install the dependencies into it:

```sh
$ cd benchmarking-public
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Run `bench_runner`'s `compare` tool:

```text
usage:
        Generate a set of comparisons between arbitrary commits. The commits
        must already exist in the dataset.

       [-h] --output-dir OUTPUT_DIR [--type {1:n,n:n}] commit [commit ...]

positional arguments:
  commit                Commits to compare. Must be a git commit hash prefix. May optionally have a friendly name
                        after a comma, e.g. c0ffee,main. If ends with a "T", use the Tier 2 run for that commit. If
                        ends with a "J", use the JIT run for that commit. If ends with a "N", use the NOGIL run for
                        that commit.

options:
  -h, --help            show this help message and exit
  --output-dir OUTPUT_DIR
                        Directory to output results to.
  --type {1:n,n:n}      Compare the first commit to all others, or do the full product of all commits
```

For example:

```sh
$ python -m bench_runner compare e418fc3,default e418fc3J,jit --output comparison --type 1:n
```

### Developer docs

The infrastructure to make all of this work is the [bench_runner
project](https://github.com/faster-cpython/bench_runner). Look there for more
detailed developer docs.

### Details about how results are collected

The easiest way to reproduce what is here is to use the [bench_runner
project](https://github.com/faster-cpython/bench_runner) library directly, but
if you want to run parts of it in a different context or better understand how the
numbers are calculated, this section describes some of the things that the
benchmarking infrastructure does.

#### Benchmarks from pyperformance and python-macrobenchmarks

These results combine benchmarks that live in the
[pyperformance](https://github.com/python/pyperformance) and
[pyston/python-macrobenchmarks](https://github.com/pyston/python-macrobenchmarks)
projects, so running the default set from `pyperformance` will definitely
produce different results. To combine these benchmarks in the same run, clone
both repos side-by-side in the same directory and [use a manifest
file](https://github.com/faster-cpython/bench_runner/blob/main/bench_runner/templates/benchmarks.manifest)
to combine them. This file should be passed to `pyperformance run`:

```
pyperformance run --manifest benchmarks.manifest
```

#### Different configurations

Benchmarks and stats collection can happen in three different configurations.
Here "configuration" may be a combination of both build-time and run-time flags:

- Default: A PGO build of CPython (`./configure --enable-optimizations
--with-lto=yes`).
- Tier 2: The same build as above, but with the `PYTHON_UOPS` environment
  variable set at runtime to use the Tier 2 interpreter.
- JIT: A JIT and PGO build of CPython (`./configure --enable-optimizations
--with-lto=yes --enable-experimental-jit`).
- Free-threading: Build a free-threaded build of CPython (`./configure --enable-free-threading`).
- Tail-calling: Build with the latest Clang, and build Python with the tail-calling
  interpreter (`./configure --with-tail-call`).

Information about the configuration of the run is in the `README.md` at the root
of each run directory. The directory name will also include `PYTHON_UOPS` for
Tier 2, `JIT` for JIT, `NOGIL` for free-threading and `CLANG` for tail calling.

To reduce the number of unknown variables when comparing results, runs are
always compared against runs of the same configuration. Be aware that sometimes
the base commit on main may predate the configuration becoming available, for
example, before the JIT compiler was merged into main. (Exception to this
rule are the weekly benchmarks of upstream main, there Tier 2, JIT, NOGIL and CLANG
configurations are compared against default configurations of the same commit,
but that isn't relevant for the common case of testing a pull request).

An additional sharp edge is that, by default, `pyperformance` does not pass
environment variables to the child process that actually does the work.
Therefore for a Tier 2 configuration, the `--inherit-environ=PYTHON_UOPS` flag
must be passed to `pyperformance run` when running benchmarks.

For detailed information, see how configurations affect [build time flags in the
Github Actions
configuration.](https://github.com/faster-cpython/bench_runner/blob/main/bench_runner/templates/_benchmark.src.yml).

#### Timing benchmarks

Timing benchmarks are notoriously noisy. There are a few techniques to reduce this:

- Where available (on Linux), we use [`pyperf
tune`](https://pyperf.readthedocs.io/en/latest/system.html) to set CPU
  affinity and other things that make the benchmarks more reproducible. For
  this reason, we know that the benchmarks are more predictable on Linux than on
  the other platforms.
- `pyperf` has the concept of "warmup" runs, while caches are warming up and
  other things about the system are still stabilizing. These runs are excluded
  from the timing results. This is generally effective at reducing variability,
  but also may exclude real work done during optimization, for example.

#### pystats

`pystats` are a set of counters in CPython that measure things like the number
of times each bytecode instruction is executed. (Detailed documentation of all
of the counters should be added to CPython in the future).

Checking the `pystats` box will generate pystats results automatically.

##### Collecting pystats locally

Collecting `pystats` requires a special build of CPython with `pystats` enabled:
(`./configure --enable-pystats`).

`pystats` must also be enabled at runtime, either using the `-Xpystats` command
line argument or `sys._stats_on()`. `pyperformance`/`pyperf` handles this step
automatically when running on a pystats-enabled build. Stats collection is
enabled during actual benchmarking code, and disabled while running the
"benchmarking harness" code in `pyperf` itself. `pyperf` has the concept of
"warmup" runs, which allow things like cache lines to warmup before actually
timing benchmarks. While they aren't included in the timing benchmarks, these
warmup runs are included in pystats collection since often Tier 2/JIT traces are
created during warmup, and we don't want the stats to appear as if the traces
ran but were not created.

Any statistics collected are then dumped at exit to the `/tmp/py_stats`
directory with a random filename. Lastly, the `Tools/scripts/summarize_stats.py`
script (in the CPython repo) is used to read all of the files from
`/tmp/py_stats` and produce a human-readable markdown summary and a JSON file
with aggregate data. Because of this design, it is imperative that:

- The `/tmp/py_stats` directory is cleared before data collection.
- No other Python processes are run that could also produce pystats data.
  Especially, this means benchmarks can not run in parallel.

For more information, see the actual code to [collect
pystats](https://github.com/faster-cpython/bench_runner/blob/main/bench_runner/templates/_pystats.src.yml).

### HPT

Hierarchical performance testing (HPT) is a method introduced in this paper:

> T. Chen, Y. Chen, Q. Guo, O. Temam, Y. Wu and W. Hu,
> "Statistical performance comparisons of computers,"
> IEEE International Symposium on High-Performance Comp Architecture,
> New Orleans, LA, USA, 2012, pp. 1-12,
> doi: 10.1109/HPCA.2012.6169043.

From the abstract:

> In traditional performance comparisons, the impact of performance variability
> is usually ignored (i.e., the means of performance measurements are compared
> regardless of the variability), or in the few cases where it is factored in
> using parametric confidence techniques, the confidence is either erroneously
> computed based on the distribution of performance measurements (with the
> implicit assumption that it obeys the normal law), instead of the distribution
> of sample mean of performance measurements, or too few measurements are
> considered for the distribution of sample mean to be normal. … We propose a
> non-parametric Hierarchical Performance Testing (HPT) framework for
> performance comparison, which is significantly more practical than standard
> parametric techniques because it does not require to collect a large number of
> measurements in order to achieve a normal distribution of the sample mean.

For each result, we compute a reliability score, as well as the estimated
speedup at the 90th, 95th and 99th percentile.

**The inclusion of HPT scores is considered experimental as we learn about their
usefulness for decision-making.**
