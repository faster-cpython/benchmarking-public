# Faster CPython Benchmark Infrastructure

🔒 [▶️ START A BENCHMARK RUN](../../actions/workflows/benchmark.yml)

## Results

Here are some recent and important revisions. 👉 [Complete list of results](RESULTS.md).

[Currently failing benchmarks](failures.md).

**Key:** 📄: table, 📈: time plot, 🧠: memory plot

<!-- START table -->
- [Most recent  pystats on main (4f18916)](results/bm-20250426-3.14.0a7%2B-4f18916/bm-20250426-azure-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-pystats.md)
- [Most recent PYTHON_UOPS pystats on main (4f18916)](results/bm-20250426-3.14.0a7%2B-4f18916-PYTHON_UOPS/bm-20250426-azure-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-pystats.md)
- [Most recent JIT pystats on main (c9f3f5b)](results/bm-20250425-3.14.0a7%2B-c9f3f5b-JIT/bm-20250425-azure-x86_64-python-c9f3f5b4ed52d7bed607-3.14.0a7%2B-c9f3f5b-pystats.md)

## linux aarch64 (arminc)
| date | fork/ref | hash/flags | vs. 3.10.4: | vs. 3.12.0: | vs. 3.13.0: | vs. base: |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| [2025-04-26](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL) | python/4f18916c5c28321f363e | 4f18916 (NOGIL) | 1.184x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.svg) | 1.054x ↓<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.svg) | 1.064x ↓<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.svg) | 1.123x ↓<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base.svg)[🧠](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base-mem.svg) |
| [2025-04-26](results/bm-20250426-3.14.0a7%2B-4f18916-JIT) | python/4f18916c5c28321f363e | 4f18916 (JIT) | 1.314x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.svg) | 1.039x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.svg) | 1.043x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.svg) | 1.025x ↓<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base.svg)[🧠](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base-mem.svg) |
| [2025-04-26](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG) | python/4f18916c5c28321f363e | 4f18916 (CLANG) | 1.374x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.svg) | 1.084x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.svg) | 1.083x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.svg) | 1.015x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base.svg)[🧠](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base-mem.svg) |
| [2025-04-26](results/bm-20250426-3.14.0a7%2B-4f18916) | python/4f18916c5c28321f363e | 4f18916 | 1.352x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.svg) | 1.070x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.svg) | 1.065x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.svg) |  |
| [2025-04-25](results/bm-20250425-3.14.0a7%2B-17718b0) | python/17718b0503e5d1c98725 | 17718b0 | 1.352x ↑<br>[📄](results/bm-20250425-3.14.0a7%2B-17718b0/bm-20250425-arminc-aarch64-python-17718b0503e5d1c98725-3.14.0a7%2B-17718b0-vs-3.10.4.md)[📈](results/bm-20250425-3.14.0a7%2B-17718b0/bm-20250425-arminc-aarch64-python-17718b0503e5d1c98725-3.14.0a7%2B-17718b0-vs-3.10.4.svg) | 1.068x ↑<br>[📄](results/bm-20250425-3.14.0a7%2B-17718b0/bm-20250425-arminc-aarch64-python-17718b0503e5d1c98725-3.14.0a7%2B-17718b0-vs-3.12.0.md)[📈](results/bm-20250425-3.14.0a7%2B-17718b0/bm-20250425-arminc-aarch64-python-17718b0503e5d1c98725-3.14.0a7%2B-17718b0-vs-3.12.0.svg) | 1.065x ↑<br>[📄](results/bm-20250425-3.14.0a7%2B-17718b0/bm-20250425-arminc-aarch64-python-17718b0503e5d1c98725-3.14.0a7%2B-17718b0-vs-3.13.0.md)[📈](results/bm-20250425-3.14.0a7%2B-17718b0/bm-20250425-arminc-aarch64-python-17718b0503e5d1c98725-3.14.0a7%2B-17718b0-vs-3.13.0.svg) |  |
| [2025-04-25](results/bm-20250425-3.14.0a7%2B-dac50cc) | JelleZijlstra/sunder_io | dac50cc | 1.355x ↑<br>[📄](results/bm-20250425-3.14.0a7%2B-dac50cc/bm-20250425-arminc-aarch64-JelleZijlstra-sunder_io-3.14.0a7%2B-dac50cc-vs-3.10.4.md)[📈](results/bm-20250425-3.14.0a7%2B-dac50cc/bm-20250425-arminc-aarch64-JelleZijlstra-sunder_io-3.14.0a7%2B-dac50cc-vs-3.10.4.svg) | 1.072x ↑<br>[📄](results/bm-20250425-3.14.0a7%2B-dac50cc/bm-20250425-arminc-aarch64-JelleZijlstra-sunder_io-3.14.0a7%2B-dac50cc-vs-3.12.0.md)[📈](results/bm-20250425-3.14.0a7%2B-dac50cc/bm-20250425-arminc-aarch64-JelleZijlstra-sunder_io-3.14.0a7%2B-dac50cc-vs-3.12.0.svg) | 1.067x ↑<br>[📄](results/bm-20250425-3.14.0a7%2B-dac50cc/bm-20250425-arminc-aarch64-JelleZijlstra-sunder_io-3.14.0a7%2B-dac50cc-vs-3.13.0.md)[📈](results/bm-20250425-3.14.0a7%2B-dac50cc/bm-20250425-arminc-aarch64-JelleZijlstra-sunder_io-3.14.0a7%2B-dac50cc-vs-3.13.0.svg) | 1.002x ↑<br>[📄](results/bm-20250425-3.14.0a7%2B-dac50cc/bm-20250425-arminc-aarch64-JelleZijlstra-sunder_io-3.14.0a7%2B-dac50cc-vs-base.md)[📈](results/bm-20250425-3.14.0a7%2B-dac50cc/bm-20250425-arminc-aarch64-JelleZijlstra-sunder_io-3.14.0a7%2B-dac50cc-vs-base.svg)[🧠](results/bm-20250425-3.14.0a7%2B-dac50cc/bm-20250425-arminc-aarch64-JelleZijlstra-sunder_io-3.14.0a7%2B-dac50cc-vs-base-mem.svg) |
| [2025-04-21](results/bm-20250421-3.14.0a7%2B-ea8ec95) | python/ea8ec95cfadbf58a11ef | ea8ec95 | 1.348x ↑<br>[📄](results/bm-20250421-3.14.0a7%2B-ea8ec95/bm-20250421-arminc-aarch64-python-ea8ec95cfadbf58a11ef-3.14.0a7%2B-ea8ec95-vs-3.10.4.md)[📈](results/bm-20250421-3.14.0a7%2B-ea8ec95/bm-20250421-arminc-aarch64-python-ea8ec95cfadbf58a11ef-3.14.0a7%2B-ea8ec95-vs-3.10.4.svg) | 1.064x ↑<br>[📄](results/bm-20250421-3.14.0a7%2B-ea8ec95/bm-20250421-arminc-aarch64-python-ea8ec95cfadbf58a11ef-3.14.0a7%2B-ea8ec95-vs-3.12.0.md)[📈](results/bm-20250421-3.14.0a7%2B-ea8ec95/bm-20250421-arminc-aarch64-python-ea8ec95cfadbf58a11ef-3.14.0a7%2B-ea8ec95-vs-3.12.0.svg) | 1.063x ↑<br>[📄](results/bm-20250421-3.14.0a7%2B-ea8ec95/bm-20250421-arminc-aarch64-python-ea8ec95cfadbf58a11ef-3.14.0a7%2B-ea8ec95-vs-3.13.0.md)[📈](results/bm-20250421-3.14.0a7%2B-ea8ec95/bm-20250421-arminc-aarch64-python-ea8ec95cfadbf58a11ef-3.14.0a7%2B-ea8ec95-vs-3.13.0.svg) |  |

## linux x86_64 (linux)
| date | fork/ref | hash/flags | vs. 3.10.4: | vs. 3.12.0: | vs. 3.13.0: | vs. base: |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| [2025-04-26](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL) | python/4f18916c5c28321f363e | 4f18916 (NOGIL) | 1.328x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-linux-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-linux-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.svg) | 1.037x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-linux-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-linux-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.svg) | 1.032x ↓<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-linux-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-linux-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.svg) | 1.072x ↓<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-linux-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-linux-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base.svg)[🧠](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-linux-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base-mem.svg) |
| [2025-04-26](results/bm-20250426-3.14.0a7%2B-4f18916-JIT) | python/4f18916c5c28321f363e | 4f18916 (JIT) | 1.458x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-linux-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-linux-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.svg) | 1.126x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-linux-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-linux-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.svg) | 1.053x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-linux-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-linux-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.svg) | 1.000x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-linux-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-linux-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base.svg)[🧠](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-linux-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base-mem.svg) |
| [2025-04-26](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG) | python/4f18916c5c28321f363e | 4f18916 (CLANG) | 1.516x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG/bm-20250426-linux-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG/bm-20250426-linux-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.svg) | 1.168x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG/bm-20250426-linux-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG/bm-20250426-linux-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.svg) | 1.092x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG/bm-20250426-linux-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG/bm-20250426-linux-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.svg) | 1.039x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG/bm-20250426-linux-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG/bm-20250426-linux-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base.svg)[🧠](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG/bm-20250426-linux-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base-mem.svg) |
| [2025-04-26](results/bm-20250426-3.14.0a7%2B-4f18916) | python/4f18916c5c28321f363e | 4f18916 | 1.457x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916/bm-20250426-linux-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916/bm-20250426-linux-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.svg) | 1.123x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916/bm-20250426-linux-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916/bm-20250426-linux-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.svg) | 1.051x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916/bm-20250426-linux-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916/bm-20250426-linux-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.svg) |  |
| [2025-04-25](results/bm-20250425-3.14.0a7%2B-17718b0) | python/17718b0503e5d1c98725 | 17718b0 | 1.448x ↑<br>[📄](results/bm-20250425-3.14.0a7%2B-17718b0/bm-20250425-linux-x86_64-python-17718b0503e5d1c98725-3.14.0a7%2B-17718b0-vs-3.10.4.md)[📈](results/bm-20250425-3.14.0a7%2B-17718b0/bm-20250425-linux-x86_64-python-17718b0503e5d1c98725-3.14.0a7%2B-17718b0-vs-3.10.4.svg) | 1.117x ↑<br>[📄](results/bm-20250425-3.14.0a7%2B-17718b0/bm-20250425-linux-x86_64-python-17718b0503e5d1c98725-3.14.0a7%2B-17718b0-vs-3.12.0.md)[📈](results/bm-20250425-3.14.0a7%2B-17718b0/bm-20250425-linux-x86_64-python-17718b0503e5d1c98725-3.14.0a7%2B-17718b0-vs-3.12.0.svg) | 1.047x ↑<br>[📄](results/bm-20250425-3.14.0a7%2B-17718b0/bm-20250425-linux-x86_64-python-17718b0503e5d1c98725-3.14.0a7%2B-17718b0-vs-3.13.0.md)[📈](results/bm-20250425-3.14.0a7%2B-17718b0/bm-20250425-linux-x86_64-python-17718b0503e5d1c98725-3.14.0a7%2B-17718b0-vs-3.13.0.svg) |  |
| [2025-04-21](results/bm-20250421-3.14.0a7%2B-ea8ec95) | python/ea8ec95cfadbf58a11ef | ea8ec95 | 1.453x ↑<br>[📄](results/bm-20250421-3.14.0a7%2B-ea8ec95/bm-20250421-linux-x86_64-python-ea8ec95cfadbf58a11ef-3.14.0a7%2B-ea8ec95-vs-3.10.4.md)[📈](results/bm-20250421-3.14.0a7%2B-ea8ec95/bm-20250421-linux-x86_64-python-ea8ec95cfadbf58a11ef-3.14.0a7%2B-ea8ec95-vs-3.10.4.svg) | 1.119x ↑<br>[📄](results/bm-20250421-3.14.0a7%2B-ea8ec95/bm-20250421-linux-x86_64-python-ea8ec95cfadbf58a11ef-3.14.0a7%2B-ea8ec95-vs-3.12.0.md)[📈](results/bm-20250421-3.14.0a7%2B-ea8ec95/bm-20250421-linux-x86_64-python-ea8ec95cfadbf58a11ef-3.14.0a7%2B-ea8ec95-vs-3.12.0.svg) | 1.049x ↑<br>[📄](results/bm-20250421-3.14.0a7%2B-ea8ec95/bm-20250421-linux-x86_64-python-ea8ec95cfadbf58a11ef-3.14.0a7%2B-ea8ec95-vs-3.13.0.md)[📈](results/bm-20250421-3.14.0a7%2B-ea8ec95/bm-20250421-linux-x86_64-python-ea8ec95cfadbf58a11ef-3.14.0a7%2B-ea8ec95-vs-3.13.0.svg) |  |
| [2024-12-30](results/bm-20241230-3.14.0a3%2B-3480124) | python/348012432155271cfbee | 3480124 | 1.421x ↑<br>[📄](results/bm-20241230-3.14.0a3%2B-3480124/bm-20241230-linux-x86_64-python-348012432155271cfbee-3.14.0a3%2B-3480124-vs-3.10.4.md)[📈](results/bm-20241230-3.14.0a3%2B-3480124/bm-20241230-linux-x86_64-python-348012432155271cfbee-3.14.0a3%2B-3480124-vs-3.10.4.svg) | 1.096x ↑<br>[📄](results/bm-20241230-3.14.0a3%2B-3480124/bm-20241230-linux-x86_64-python-348012432155271cfbee-3.14.0a3%2B-3480124-vs-3.12.0.md)[📈](results/bm-20241230-3.14.0a3%2B-3480124/bm-20241230-linux-x86_64-python-348012432155271cfbee-3.14.0a3%2B-3480124-vs-3.12.0.svg) | 1.038x ↑<br>[📄](results/bm-20241230-3.14.0a3%2B-3480124/bm-20241230-linux-x86_64-python-348012432155271cfbee-3.14.0a3%2B-3480124-vs-3.13.0.md)[📈](results/bm-20241230-3.14.0a3%2B-3480124/bm-20241230-linux-x86_64-python-348012432155271cfbee-3.14.0a3%2B-3480124-vs-3.13.0.svg) |  |
| [2024-12-23](results/bm-20241223-3.14.0a3%2B-180d417) | python/180d417e9f9456defd4c | 180d417 | 1.421x ↑<br>[📄](results/bm-20241223-3.14.0a3%2B-180d417/bm-20241223-linux-x86_64-python-180d417e9f9456defd4c-3.14.0a3%2B-180d417-vs-3.10.4.md)[📈](results/bm-20241223-3.14.0a3%2B-180d417/bm-20241223-linux-x86_64-python-180d417e9f9456defd4c-3.14.0a3%2B-180d417-vs-3.10.4.svg) | 1.095x ↑<br>[📄](results/bm-20241223-3.14.0a3%2B-180d417/bm-20241223-linux-x86_64-python-180d417e9f9456defd4c-3.14.0a3%2B-180d417-vs-3.12.0.md)[📈](results/bm-20241223-3.14.0a3%2B-180d417/bm-20241223-linux-x86_64-python-180d417e9f9456defd4c-3.14.0a3%2B-180d417-vs-3.12.0.svg) | 1.038x ↑<br>[📄](results/bm-20241223-3.14.0a3%2B-180d417/bm-20241223-linux-x86_64-python-180d417e9f9456defd4c-3.14.0a3%2B-180d417-vs-3.13.0.md)[📈](results/bm-20241223-3.14.0a3%2B-180d417/bm-20241223-linux-x86_64-python-180d417e9f9456defd4c-3.14.0a3%2B-180d417-vs-3.13.0.svg) |  |
| [2024-12-16](results/bm-20241216-3.14.0a2%2B-e4981e3) | python/e4981e33b82ac14cca0f | e4981e3 | 1.421x ↑<br>[📄](results/bm-20241216-3.14.0a2%2B-e4981e3/bm-20241216-linux-x86_64-python-e4981e33b82ac14cca0f-3.14.0a2%2B-e4981e3-vs-3.10.4.md)[📈](results/bm-20241216-3.14.0a2%2B-e4981e3/bm-20241216-linux-x86_64-python-e4981e33b82ac14cca0f-3.14.0a2%2B-e4981e3-vs-3.10.4.svg) | 1.096x ↑<br>[📄](results/bm-20241216-3.14.0a2%2B-e4981e3/bm-20241216-linux-x86_64-python-e4981e33b82ac14cca0f-3.14.0a2%2B-e4981e3-vs-3.12.0.md)[📈](results/bm-20241216-3.14.0a2%2B-e4981e3/bm-20241216-linux-x86_64-python-e4981e33b82ac14cca0f-3.14.0a2%2B-e4981e3-vs-3.12.0.svg) | 1.038x ↑<br>[📄](results/bm-20241216-3.14.0a2%2B-e4981e3/bm-20241216-linux-x86_64-python-e4981e33b82ac14cca0f-3.14.0a2%2B-e4981e3-vs-3.13.0.md)[📈](results/bm-20241216-3.14.0a2%2B-e4981e3/bm-20241216-linux-x86_64-python-e4981e33b82ac14cca0f-3.14.0a2%2B-e4981e3-vs-3.13.0.svg) |  |
| [2024-12-09](results/bm-20241209-3.14.0a2%2B-be07edf) | python/be07edf511365ce554c0 | be07edf | 1.414x ↑<br>[📄](results/bm-20241209-3.14.0a2%2B-be07edf/bm-20241209-linux-x86_64-python-be07edf511365ce554c0-3.14.0a2%2B-be07edf-vs-3.10.4.md)[📈](results/bm-20241209-3.14.0a2%2B-be07edf/bm-20241209-linux-x86_64-python-be07edf511365ce554c0-3.14.0a2%2B-be07edf-vs-3.10.4.svg) | 1.088x ↑<br>[📄](results/bm-20241209-3.14.0a2%2B-be07edf/bm-20241209-linux-x86_64-python-be07edf511365ce554c0-3.14.0a2%2B-be07edf-vs-3.12.0.md)[📈](results/bm-20241209-3.14.0a2%2B-be07edf/bm-20241209-linux-x86_64-python-be07edf511365ce554c0-3.14.0a2%2B-be07edf-vs-3.12.0.svg) | 1.032x ↑<br>[📄](results/bm-20241209-3.14.0a2%2B-be07edf/bm-20241209-linux-x86_64-python-be07edf511365ce554c0-3.14.0a2%2B-be07edf-vs-3.13.0.md)[📈](results/bm-20241209-3.14.0a2%2B-be07edf/bm-20241209-linux-x86_64-python-be07edf511365ce554c0-3.14.0a2%2B-be07edf-vs-3.13.0.svg) |  |
| [2024-12-02](results/bm-20241202-3.14.0a2%2B-2950bc5) | python/2950bc50af8fc2539e64 | 2950bc5 | 1.379x ↑<br>[📄](results/bm-20241202-3.14.0a2%2B-2950bc5/bm-20241202-linux-x86_64-python-2950bc50af8fc2539e64-3.14.0a2%2B-2950bc5-vs-3.10.4.md)[📈](results/bm-20241202-3.14.0a2%2B-2950bc5/bm-20241202-linux-x86_64-python-2950bc50af8fc2539e64-3.14.0a2%2B-2950bc5-vs-3.10.4.svg) | 1.047x ↑<br>[📄](results/bm-20241202-3.14.0a2%2B-2950bc5/bm-20241202-linux-x86_64-python-2950bc50af8fc2539e64-3.14.0a2%2B-2950bc5-vs-3.12.0.md)[📈](results/bm-20241202-3.14.0a2%2B-2950bc5/bm-20241202-linux-x86_64-python-2950bc50af8fc2539e64-3.14.0a2%2B-2950bc5-vs-3.12.0.svg) | 1.006x ↓<br>[📄](results/bm-20241202-3.14.0a2%2B-2950bc5/bm-20241202-linux-x86_64-python-2950bc50af8fc2539e64-3.14.0a2%2B-2950bc5-vs-3.13.0.md)[📈](results/bm-20241202-3.14.0a2%2B-2950bc5/bm-20241202-linux-x86_64-python-2950bc50af8fc2539e64-3.14.0a2%2B-2950bc5-vs-3.13.0.svg) |  |
| [2024-11-25](results/bm-20241125-3.14.0a2%2B-c595eae) | python/c595eae84c7f665eced0 | c595eae | 1.386x ↑<br>[📄](results/bm-20241125-3.14.0a2%2B-c595eae/bm-20241125-linux-x86_64-python-c595eae84c7f665eced0-3.14.0a2%2B-c595eae-vs-3.10.4.md)[📈](results/bm-20241125-3.14.0a2%2B-c595eae/bm-20241125-linux-x86_64-python-c595eae84c7f665eced0-3.14.0a2%2B-c595eae-vs-3.10.4.svg) | 1.053x ↑<br>[📄](results/bm-20241125-3.14.0a2%2B-c595eae/bm-20241125-linux-x86_64-python-c595eae84c7f665eced0-3.14.0a2%2B-c595eae-vs-3.12.0.md)[📈](results/bm-20241125-3.14.0a2%2B-c595eae/bm-20241125-linux-x86_64-python-c595eae84c7f665eced0-3.14.0a2%2B-c595eae-vs-3.12.0.svg) | 1.001x ↓<br>[📄](results/bm-20241125-3.14.0a2%2B-c595eae/bm-20241125-linux-x86_64-python-c595eae84c7f665eced0-3.14.0a2%2B-c595eae-vs-3.13.0.md)[📈](results/bm-20241125-3.14.0a2%2B-c595eae/bm-20241125-linux-x86_64-python-c595eae84c7f665eced0-3.14.0a2%2B-c595eae-vs-3.13.0.svg) |  |
| [2024-11-18](results/bm-20241118-3.14.0a1%2B-ce453e6) | python/ce453e6c2ffda657d9d7 | ce453e6 | 1.384x ↑<br>[📄](results/bm-20241118-3.14.0a1%2B-ce453e6/bm-20241118-linux-x86_64-python-ce453e6c2ffda657d9d7-3.14.0a1%2B-ce453e6-vs-3.10.4.md)[📈](results/bm-20241118-3.14.0a1%2B-ce453e6/bm-20241118-linux-x86_64-python-ce453e6c2ffda657d9d7-3.14.0a1%2B-ce453e6-vs-3.10.4.svg) | 1.053x ↑<br>[📄](results/bm-20241118-3.14.0a1%2B-ce453e6/bm-20241118-linux-x86_64-python-ce453e6c2ffda657d9d7-3.14.0a1%2B-ce453e6-vs-3.12.0.md)[📈](results/bm-20241118-3.14.0a1%2B-ce453e6/bm-20241118-linux-x86_64-python-ce453e6c2ffda657d9d7-3.14.0a1%2B-ce453e6-vs-3.12.0.svg) | 1.004x ↓<br>[📄](results/bm-20241118-3.14.0a1%2B-ce453e6/bm-20241118-linux-x86_64-python-ce453e6c2ffda657d9d7-3.14.0a1%2B-ce453e6-vs-3.13.0.md)[📈](results/bm-20241118-3.14.0a1%2B-ce453e6/bm-20241118-linux-x86_64-python-ce453e6c2ffda657d9d7-3.14.0a1%2B-ce453e6-vs-3.13.0.svg) |  |
| [2024-11-10](results/bm-20241110-3.14.0a1%2B-434b297) | python/434b29767f2fdef9f35c | 434b297 | 1.376x ↑<br>[📄](results/bm-20241110-3.14.0a1%2B-434b297/bm-20241110-linux-x86_64-python-434b29767f2fdef9f35c-3.14.0a1%2B-434b297-vs-3.10.4.md)[📈](results/bm-20241110-3.14.0a1%2B-434b297/bm-20241110-linux-x86_64-python-434b29767f2fdef9f35c-3.14.0a1%2B-434b297-vs-3.10.4.svg) | 1.048x ↑<br>[📄](results/bm-20241110-3.14.0a1%2B-434b297/bm-20241110-linux-x86_64-python-434b29767f2fdef9f35c-3.14.0a1%2B-434b297-vs-3.12.0.md)[📈](results/bm-20241110-3.14.0a1%2B-434b297/bm-20241110-linux-x86_64-python-434b29767f2fdef9f35c-3.14.0a1%2B-434b297-vs-3.12.0.svg) | 1.009x ↓<br>[📄](results/bm-20241110-3.14.0a1%2B-434b297/bm-20241110-linux-x86_64-python-434b29767f2fdef9f35c-3.14.0a1%2B-434b297-vs-3.13.0.md)[📈](results/bm-20241110-3.14.0a1%2B-434b297/bm-20241110-linux-x86_64-python-434b29767f2fdef9f35c-3.14.0a1%2B-434b297-vs-3.13.0.svg) |  |
| [2024-11-03](results/bm-20241103-3.14.0a1%2B-081706f) | python/081706f873b7d1a10b27 | 081706f | 1.375x ↑<br>[📄](results/bm-20241103-3.14.0a1%2B-081706f/bm-20241103-linux-x86_64-python-081706f873b7d1a10b27-3.14.0a1%2B-081706f-vs-3.10.4.md)[📈](results/bm-20241103-3.14.0a1%2B-081706f/bm-20241103-linux-x86_64-python-081706f873b7d1a10b27-3.14.0a1%2B-081706f-vs-3.10.4.svg) | 1.047x ↑<br>[📄](results/bm-20241103-3.14.0a1%2B-081706f/bm-20241103-linux-x86_64-python-081706f873b7d1a10b27-3.14.0a1%2B-081706f-vs-3.12.0.md)[📈](results/bm-20241103-3.14.0a1%2B-081706f/bm-20241103-linux-x86_64-python-081706f873b7d1a10b27-3.14.0a1%2B-081706f-vs-3.12.0.svg) | 1.011x ↓<br>[📄](results/bm-20241103-3.14.0a1%2B-081706f/bm-20241103-linux-x86_64-python-081706f873b7d1a10b27-3.14.0a1%2B-081706f-vs-3.13.0.md)[📈](results/bm-20241103-3.14.0a1%2B-081706f/bm-20241103-linux-x86_64-python-081706f873b7d1a10b27-3.14.0a1%2B-081706f-vs-3.13.0.svg) |  |
| [2024-10-28](results/bm-20241028-3.14.0a1%2B-2544159) | python/25441592db179e9f5e6c | 2544159 | 1.394x ↑<br>[📄](results/bm-20241028-3.14.0a1%2B-2544159/bm-20241028-linux-x86_64-python-25441592db179e9f5e6c-3.14.0a1%2B-2544159-vs-3.10.4.md)[📈](results/bm-20241028-3.14.0a1%2B-2544159/bm-20241028-linux-x86_64-python-25441592db179e9f5e6c-3.14.0a1%2B-2544159-vs-3.10.4.svg) | 1.059x ↑<br>[📄](results/bm-20241028-3.14.0a1%2B-2544159/bm-20241028-linux-x86_64-python-25441592db179e9f5e6c-3.14.0a1%2B-2544159-vs-3.12.0.md)[📈](results/bm-20241028-3.14.0a1%2B-2544159/bm-20241028-linux-x86_64-python-25441592db179e9f5e6c-3.14.0a1%2B-2544159-vs-3.12.0.svg) | 1.000x ↑<br>[📄](results/bm-20241028-3.14.0a1%2B-2544159/bm-20241028-linux-x86_64-python-25441592db179e9f5e6c-3.14.0a1%2B-2544159-vs-3.13.0.md)[📈](results/bm-20241028-3.14.0a1%2B-2544159/bm-20241028-linux-x86_64-python-25441592db179e9f5e6c-3.14.0a1%2B-2544159-vs-3.13.0.svg) |  |
| [2024-10-20](results/bm-20241020-3.14.0a1%2B-9256be7) | python/9256be7ff0ab035cfd26 | 9256be7 | 1.393x ↑<br>[📄](results/bm-20241020-3.14.0a1%2B-9256be7/bm-20241020-linux-x86_64-python-9256be7ff0ab035cfd26-3.14.0a1%2B-9256be7-vs-3.10.4.md)[📈](results/bm-20241020-3.14.0a1%2B-9256be7/bm-20241020-linux-x86_64-python-9256be7ff0ab035cfd26-3.14.0a1%2B-9256be7-vs-3.10.4.svg) | 1.060x ↑<br>[📄](results/bm-20241020-3.14.0a1%2B-9256be7/bm-20241020-linux-x86_64-python-9256be7ff0ab035cfd26-3.14.0a1%2B-9256be7-vs-3.12.0.md)[📈](results/bm-20241020-3.14.0a1%2B-9256be7/bm-20241020-linux-x86_64-python-9256be7ff0ab035cfd26-3.14.0a1%2B-9256be7-vs-3.12.0.svg) | 1.000x ↑<br>[📄](results/bm-20241020-3.14.0a1%2B-9256be7/bm-20241020-linux-x86_64-python-9256be7ff0ab035cfd26-3.14.0a1%2B-9256be7-vs-3.13.0.md)[📈](results/bm-20241020-3.14.0a1%2B-9256be7/bm-20241020-linux-x86_64-python-9256be7ff0ab035cfd26-3.14.0a1%2B-9256be7-vs-3.13.0.svg) |  |
| [2024-10-13](results/bm-20241013-3.14.0a0-cfc27bc) | python/cfc27bc50fe165330f22 | cfc27bc | 1.394x ↑<br>[📄](results/bm-20241013-3.14.0a0-cfc27bc/bm-20241013-linux-x86_64-python-cfc27bc50fe165330f22-3.14.0a0-cfc27bc-vs-3.10.4.md)[📈](results/bm-20241013-3.14.0a0-cfc27bc/bm-20241013-linux-x86_64-python-cfc27bc50fe165330f22-3.14.0a0-cfc27bc-vs-3.10.4.svg) | 1.062x ↑<br>[📄](results/bm-20241013-3.14.0a0-cfc27bc/bm-20241013-linux-x86_64-python-cfc27bc50fe165330f22-3.14.0a0-cfc27bc-vs-3.12.0.md)[📈](results/bm-20241013-3.14.0a0-cfc27bc/bm-20241013-linux-x86_64-python-cfc27bc50fe165330f22-3.14.0a0-cfc27bc-vs-3.12.0.svg) | 1.001x ↑<br>[📄](results/bm-20241013-3.14.0a0-cfc27bc/bm-20241013-linux-x86_64-python-cfc27bc50fe165330f22-3.14.0a0-cfc27bc-vs-3.13.0.md)[📈](results/bm-20241013-3.14.0a0-cfc27bc/bm-20241013-linux-x86_64-python-cfc27bc50fe165330f22-3.14.0a0-cfc27bc-vs-3.13.0.svg) |  |
| [2024-10-06](results/bm-20241006-3.14.0a0-31516c9) | python/31516c98dd7097047ba1 | 31516c9 | 1.401x ↑<br>[📄](results/bm-20241006-3.14.0a0-31516c9/bm-20241006-linux-x86_64-python-31516c98dd7097047ba1-3.14.0a0-31516c9-vs-3.10.4.md)[📈](results/bm-20241006-3.14.0a0-31516c9/bm-20241006-linux-x86_64-python-31516c98dd7097047ba1-3.14.0a0-31516c9-vs-3.10.4.svg) | 1.069x ↑<br>[📄](results/bm-20241006-3.14.0a0-31516c9/bm-20241006-linux-x86_64-python-31516c98dd7097047ba1-3.14.0a0-31516c9-vs-3.12.0.md)[📈](results/bm-20241006-3.14.0a0-31516c9/bm-20241006-linux-x86_64-python-31516c98dd7097047ba1-3.14.0a0-31516c9-vs-3.12.0.svg) | 1.012x ↑<br>[📄](results/bm-20241006-3.14.0a0-31516c9/bm-20241006-linux-x86_64-python-31516c98dd7097047ba1-3.14.0a0-31516c9-vs-3.13.0.md)[📈](results/bm-20241006-3.14.0a0-31516c9/bm-20241006-linux-x86_64-python-31516c98dd7097047ba1-3.14.0a0-31516c9-vs-3.13.0.svg) |  |
| [2024-09-29](results/bm-20240929-3.14.0a0-6f4d64b) | python/6f4d64b048133c60d407 | 6f4d64b | 1.404x ↑<br>[📄](results/bm-20240929-3.14.0a0-6f4d64b/bm-20240929-linux-x86_64-python-6f4d64b048133c60d407-3.14.0a0-6f4d64b-vs-3.10.4.md)[📈](results/bm-20240929-3.14.0a0-6f4d64b/bm-20240929-linux-x86_64-python-6f4d64b048133c60d407-3.14.0a0-6f4d64b-vs-3.10.4.svg) | 1.070x ↑<br>[📄](results/bm-20240929-3.14.0a0-6f4d64b/bm-20240929-linux-x86_64-python-6f4d64b048133c60d407-3.14.0a0-6f4d64b-vs-3.12.0.md)[📈](results/bm-20240929-3.14.0a0-6f4d64b/bm-20240929-linux-x86_64-python-6f4d64b048133c60d407-3.14.0a0-6f4d64b-vs-3.12.0.svg) | 1.013x ↑<br>[📄](results/bm-20240929-3.14.0a0-6f4d64b/bm-20240929-linux-x86_64-python-6f4d64b048133c60d407-3.14.0a0-6f4d64b-vs-3.13.0.md)[📈](results/bm-20240929-3.14.0a0-6f4d64b/bm-20240929-linux-x86_64-python-6f4d64b048133c60d407-3.14.0a0-6f4d64b-vs-3.13.0.svg) |  |
| [2024-09-23](results/bm-20240923-3.14.0a0-6ab6348) | python/6ab634840c662ae07d90 | 6ab6348 | 1.403x ↑<br>[📄](results/bm-20240923-3.14.0a0-6ab6348/bm-20240923-linux-x86_64-python-6ab634840c662ae07d90-3.14.0a0-6ab6348-vs-3.10.4.md)[📈](results/bm-20240923-3.14.0a0-6ab6348/bm-20240923-linux-x86_64-python-6ab634840c662ae07d90-3.14.0a0-6ab6348-vs-3.10.4.svg) | 1.069x ↑<br>[📄](results/bm-20240923-3.14.0a0-6ab6348/bm-20240923-linux-x86_64-python-6ab634840c662ae07d90-3.14.0a0-6ab6348-vs-3.12.0.md)[📈](results/bm-20240923-3.14.0a0-6ab6348/bm-20240923-linux-x86_64-python-6ab634840c662ae07d90-3.14.0a0-6ab6348-vs-3.12.0.svg) | 1.014x ↑<br>[📄](results/bm-20240923-3.14.0a0-6ab6348/bm-20240923-linux-x86_64-python-6ab634840c662ae07d90-3.14.0a0-6ab6348-vs-3.13.0.md)[📈](results/bm-20240923-3.14.0a0-6ab6348/bm-20240923-linux-x86_64-python-6ab634840c662ae07d90-3.14.0a0-6ab6348-vs-3.13.0.svg) |  |
| [2024-09-16](results/bm-20240916-3.14.0a0-9aa1f60) | python/9aa1f60e2dedd8a67c42 | 9aa1f60 | 1.401x ↑<br>[📄](results/bm-20240916-3.14.0a0-9aa1f60/bm-20240916-linux-x86_64-python-9aa1f60e2dedd8a67c42-3.14.0a0-9aa1f60-vs-3.10.4.md)[📈](results/bm-20240916-3.14.0a0-9aa1f60/bm-20240916-linux-x86_64-python-9aa1f60e2dedd8a67c42-3.14.0a0-9aa1f60-vs-3.10.4.svg) | 1.068x ↑<br>[📄](results/bm-20240916-3.14.0a0-9aa1f60/bm-20240916-linux-x86_64-python-9aa1f60e2dedd8a67c42-3.14.0a0-9aa1f60-vs-3.12.0.md)[📈](results/bm-20240916-3.14.0a0-9aa1f60/bm-20240916-linux-x86_64-python-9aa1f60e2dedd8a67c42-3.14.0a0-9aa1f60-vs-3.12.0.svg) | 1.012x ↑<br>[📄](results/bm-20240916-3.14.0a0-9aa1f60/bm-20240916-linux-x86_64-python-9aa1f60e2dedd8a67c42-3.14.0a0-9aa1f60-vs-3.13.0.md)[📈](results/bm-20240916-3.14.0a0-9aa1f60/bm-20240916-linux-x86_64-python-9aa1f60e2dedd8a67c42-3.14.0a0-9aa1f60-vs-3.13.0.svg) |  |
| [2024-09-08](results/bm-20240908-3.14.0a0-93b61bc) | python/93b61bc1245fb318a11d | 93b61bc | 1.402x ↑<br>[📄](results/bm-20240908-3.14.0a0-93b61bc/bm-20240908-linux-x86_64-python-93b61bc1245fb318a11d-3.14.0a0-93b61bc-vs-3.10.4.md)[📈](results/bm-20240908-3.14.0a0-93b61bc/bm-20240908-linux-x86_64-python-93b61bc1245fb318a11d-3.14.0a0-93b61bc-vs-3.10.4.svg) | 1.070x ↑<br>[📄](results/bm-20240908-3.14.0a0-93b61bc/bm-20240908-linux-x86_64-python-93b61bc1245fb318a11d-3.14.0a0-93b61bc-vs-3.12.0.md)[📈](results/bm-20240908-3.14.0a0-93b61bc/bm-20240908-linux-x86_64-python-93b61bc1245fb318a11d-3.14.0a0-93b61bc-vs-3.12.0.svg) | 1.012x ↑<br>[📄](results/bm-20240908-3.14.0a0-93b61bc/bm-20240908-linux-x86_64-python-93b61bc1245fb318a11d-3.14.0a0-93b61bc-vs-3.13.0.md)[📈](results/bm-20240908-3.14.0a0-93b61bc/bm-20240908-linux-x86_64-python-93b61bc1245fb318a11d-3.14.0a0-93b61bc-vs-3.13.0.svg) |  |
| [2024-09-01](results/bm-20240901-3.14.0a0-e3f76e5) | python/e3f76e5cfb6196e31c2a | e3f76e5 | 1.398x ↑<br>[📄](results/bm-20240901-3.14.0a0-e3f76e5/bm-20240901-linux-x86_64-python-e3f76e5cfb6196e31c2a-3.14.0a0-e3f76e5-vs-3.10.4.md)[📈](results/bm-20240901-3.14.0a0-e3f76e5/bm-20240901-linux-x86_64-python-e3f76e5cfb6196e31c2a-3.14.0a0-e3f76e5-vs-3.10.4.svg) | 1.066x ↑<br>[📄](results/bm-20240901-3.14.0a0-e3f76e5/bm-20240901-linux-x86_64-python-e3f76e5cfb6196e31c2a-3.14.0a0-e3f76e5-vs-3.12.0.md)[📈](results/bm-20240901-3.14.0a0-e3f76e5/bm-20240901-linux-x86_64-python-e3f76e5cfb6196e31c2a-3.14.0a0-e3f76e5-vs-3.12.0.svg) | 1.008x ↑<br>[📄](results/bm-20240901-3.14.0a0-e3f76e5/bm-20240901-linux-x86_64-python-e3f76e5cfb6196e31c2a-3.14.0a0-e3f76e5-vs-3.13.0.md)[📈](results/bm-20240901-3.14.0a0-e3f76e5/bm-20240901-linux-x86_64-python-e3f76e5cfb6196e31c2a-3.14.0a0-e3f76e5-vs-3.13.0.svg) |  |
| [2024-06-09](results/bm-20240609-3.14.0a0-0ae8579) | python/0ae8579b85f9b0cd3f28 | 0ae8579 | 1.395x ↑<br>[📄](results/bm-20240609-3.14.0a0-0ae8579/bm-20240609-linux-x86_64-python-0ae8579b85f9b0cd3f28-3.14.0a0-0ae8579-vs-3.10.4.md)[📈](results/bm-20240609-3.14.0a0-0ae8579/bm-20240609-linux-x86_64-python-0ae8579b85f9b0cd3f28-3.14.0a0-0ae8579-vs-3.10.4.svg) | 1.059x ↑<br>[📄](results/bm-20240609-3.14.0a0-0ae8579/bm-20240609-linux-x86_64-python-0ae8579b85f9b0cd3f28-3.14.0a0-0ae8579-vs-3.12.0.md)[📈](results/bm-20240609-3.14.0a0-0ae8579/bm-20240609-linux-x86_64-python-0ae8579b85f9b0cd3f28-3.14.0a0-0ae8579-vs-3.12.0.svg) | 1.006x ↓<br>[📄](results/bm-20240609-3.14.0a0-0ae8579/bm-20240609-linux-x86_64-python-0ae8579b85f9b0cd3f28-3.14.0a0-0ae8579-vs-3.13.0.md)[📈](results/bm-20240609-3.14.0a0-0ae8579/bm-20240609-linux-x86_64-python-0ae8579b85f9b0cd3f28-3.14.0a0-0ae8579-vs-3.13.0.svg) |  |
| [2024-06-02](results/bm-20240602-3.14.0a0-117a8ac) | python/117a8acdab997b73ada8 | 117a8ac | 1.385x ↑<br>[📄](results/bm-20240602-3.14.0a0-117a8ac/bm-20240602-linux-x86_64-python-117a8acdab997b73ada8-3.14.0a0-117a8ac-vs-3.10.4.md)[📈](results/bm-20240602-3.14.0a0-117a8ac/bm-20240602-linux-x86_64-python-117a8acdab997b73ada8-3.14.0a0-117a8ac-vs-3.10.4.svg) | 1.052x ↑<br>[📄](results/bm-20240602-3.14.0a0-117a8ac/bm-20240602-linux-x86_64-python-117a8acdab997b73ada8-3.14.0a0-117a8ac-vs-3.12.0.md)[📈](results/bm-20240602-3.14.0a0-117a8ac/bm-20240602-linux-x86_64-python-117a8acdab997b73ada8-3.14.0a0-117a8ac-vs-3.12.0.svg) | 1.012x ↓<br>[📄](results/bm-20240602-3.14.0a0-117a8ac/bm-20240602-linux-x86_64-python-117a8acdab997b73ada8-3.14.0a0-117a8ac-vs-3.13.0.md)[📈](results/bm-20240602-3.14.0a0-117a8ac/bm-20240602-linux-x86_64-python-117a8acdab997b73ada8-3.14.0a0-117a8ac-vs-3.13.0.svg) |  |

## linux x86_64 (pythonperf2)
| date | fork/ref | hash/flags | vs. 3.10.4: | vs. 3.12.0: | vs. 3.13.0: | vs. base: |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| [2025-04-28](results/bm-20250428-3.14.0a7%2B-a455573) | faster-cpython/get_iter_stats | a455573 | 1.374x ↑<br>[📄](results/bm-20250428-3.14.0a7%2B-a455573/bm-20250428-pythonperf2-x86_64-faster%252dcpython-get_iter_stats-3.14.0a7%2B-a455573-vs-3.10.4.md)[📈](results/bm-20250428-3.14.0a7%2B-a455573/bm-20250428-pythonperf2-x86_64-faster%252dcpython-get_iter_stats-3.14.0a7%2B-a455573-vs-3.10.4.svg) | 1.046x ↑<br>[📄](results/bm-20250428-3.14.0a7%2B-a455573/bm-20250428-pythonperf2-x86_64-faster%252dcpython-get_iter_stats-3.14.0a7%2B-a455573-vs-3.12.0.md)[📈](results/bm-20250428-3.14.0a7%2B-a455573/bm-20250428-pythonperf2-x86_64-faster%252dcpython-get_iter_stats-3.14.0a7%2B-a455573-vs-3.12.0.svg) | 1.072x ↑<br>[📄](results/bm-20250428-3.14.0a7%2B-a455573/bm-20250428-pythonperf2-x86_64-faster%252dcpython-get_iter_stats-3.14.0a7%2B-a455573-vs-3.13.0.md)[📈](results/bm-20250428-3.14.0a7%2B-a455573/bm-20250428-pythonperf2-x86_64-faster%252dcpython-get_iter_stats-3.14.0a7%2B-a455573-vs-3.13.0.svg) |  |
| [2025-04-26](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL) | python/4f18916c5c28321f363e | 4f18916 (NOGIL) | 1.250x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-pythonperf2-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-pythonperf2-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.svg) | 1.046x ↓<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-pythonperf2-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-pythonperf2-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.svg) | 1.024x ↓<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-pythonperf2-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-pythonperf2-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.svg) | 1.087x ↓<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-pythonperf2-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-pythonperf2-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base.svg)[🧠](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-pythonperf2-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base-mem.svg) |
| [2025-04-26](results/bm-20250426-3.14.0a7%2B-4f18916-JIT) | python/4f18916c5c28321f363e | 4f18916 (JIT) | 1.362x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-pythonperf2-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-pythonperf2-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.svg) | 1.038x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-pythonperf2-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-pythonperf2-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.svg) | 1.063x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-pythonperf2-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-pythonperf2-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.svg) | 1.003x ↓<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-pythonperf2-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-pythonperf2-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base.svg)[🧠](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-pythonperf2-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base-mem.svg) |
| [2025-04-26](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG) | python/4f18916c5c28321f363e | 4f18916 (CLANG) | 1.414x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG/bm-20250426-pythonperf2-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG/bm-20250426-pythonperf2-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.svg) | 1.076x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG/bm-20250426-pythonperf2-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG/bm-20250426-pythonperf2-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.svg) | 1.103x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG/bm-20250426-pythonperf2-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG/bm-20250426-pythonperf2-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.svg) | 1.037x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG/bm-20250426-pythonperf2-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG/bm-20250426-pythonperf2-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base.svg)[🧠](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG/bm-20250426-pythonperf2-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base-mem.svg) |
| [2025-04-26](results/bm-20250426-3.14.0a7%2B-4f18916) | python/4f18916c5c28321f363e | 4f18916 | 1.364x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916/bm-20250426-pythonperf2-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916/bm-20250426-pythonperf2-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.svg) | 1.038x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916/bm-20250426-pythonperf2-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916/bm-20250426-pythonperf2-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.svg) | 1.064x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916/bm-20250426-pythonperf2-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916/bm-20250426-pythonperf2-x86_64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.svg) |  |

## windows amd64 (pythonperf1)
| date | fork/ref | hash/flags | vs. 3.10.4: | vs. 3.12.0: | vs. 3.13.0: | vs. base: |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| [2025-04-26](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL) | python/4f18916c5c28321f363e | 4f18916 (NOGIL) | 1.183x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.svg) | 1.022x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.svg) | 1.029x ↓<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.svg) | 1.079x ↓<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base.svg) |
| [2025-04-26](results/bm-20250426-3.14.0a7%2B-4f18916-JIT) | python/4f18916c5c28321f363e | 4f18916 (JIT) | 1.286x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.svg) | 1.096x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.svg) | 1.031x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.svg) | 1.010x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base.svg) |
| [2025-04-26](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG) | python/4f18916c5c28321f363e | 4f18916 (CLANG) | 1.507x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG/bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG/bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.svg) | 1.278x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG/bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG/bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.svg) | 1.193x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG/bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG/bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.svg) | 1.172x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG/bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG/bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base.svg) |
| [2025-04-26](results/bm-20250426-3.14.0a7%2B-4f18916) | python/4f18916c5c28321f363e | 4f18916 | 1.271x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916/bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916/bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.svg) | 1.082x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916/bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916/bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.svg) | 1.020x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916/bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916/bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.svg) |  |

## windows amd64 (pythonperf1_win32)
| date | fork/ref | hash/flags | vs. 3.10.4: | vs. 3.12.0: | vs. 3.13.0: | vs. base: |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| [2025-03-07](results/bm-20250307-3.14.0a5%2B-06bc3bd) | brandtbucher/msvc_musttail | 06bc3bd | 1.391x ↑<br>[📄](results/bm-20250307-3.14.0a5%2B-06bc3bd/bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5%2B-06bc3bd-vs-3.10.4.md)[📈](results/bm-20250307-3.14.0a5%2B-06bc3bd/bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5%2B-06bc3bd-vs-3.10.4.svg) | 1.407x ↑<br>[📄](results/bm-20250307-3.14.0a5%2B-06bc3bd/bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5%2B-06bc3bd-vs-3.12.0.md)[📈](results/bm-20250307-3.14.0a5%2B-06bc3bd/bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5%2B-06bc3bd-vs-3.12.0.svg) | 1.203x ↑<br>[📄](results/bm-20250307-3.14.0a5%2B-06bc3bd/bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5%2B-06bc3bd-vs-3.13.0.md)[📈](results/bm-20250307-3.14.0a5%2B-06bc3bd/bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5%2B-06bc3bd-vs-3.13.0.svg) |  |
| [2025-03-07](results/bm-20250225-3.14.0a5%2B-f963239) | brandtbucher/msvc_musttail | 06bc3bd | 1.391x ↑<br>[📄](results/bm-20250225-3.14.0a5%2B-f963239/bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5%2B-06bc3bd-vs-3.10.4.md)[📈](results/bm-20250225-3.14.0a5%2B-f963239/bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5%2B-06bc3bd-vs-3.10.4.svg) | 1.407x ↑<br>[📄](results/bm-20250225-3.14.0a5%2B-f963239/bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5%2B-06bc3bd-vs-3.12.0.md)[📈](results/bm-20250225-3.14.0a5%2B-f963239/bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5%2B-06bc3bd-vs-3.12.0.svg) | 1.203x ↑<br>[📄](results/bm-20250225-3.14.0a5%2B-f963239/bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5%2B-06bc3bd-vs-3.13.0.md)[📈](results/bm-20250225-3.14.0a5%2B-f963239/bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5%2B-06bc3bd-vs-3.13.0.svg) |  |

## windows x86 (pythonperf1_win32)
| date | fork/ref | hash/flags | vs. 3.10.4: | vs. 3.12.0: | vs. 3.13.0: | vs. base: |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| [2025-04-26](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL) | python/4f18916c5c28321f363e | 4f18916 (NOGIL) | 1.034x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-pythonperf1_win32-x86-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-pythonperf1_win32-x86-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.svg) | 1.068x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-pythonperf1_win32-x86-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-pythonperf1_win32-x86-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.svg) | 1.084x ↓<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-pythonperf1_win32-x86-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-pythonperf1_win32-x86-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.svg) | 1.118x ↓<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-pythonperf1_win32-x86-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-pythonperf1_win32-x86-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base.svg) |
| [2025-04-26](results/bm-20250426-3.14.0a7%2B-4f18916-JIT) | python/4f18916c5c28321f363e | 4f18916 (JIT) | 1.054x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-pythonperf1_win32-x86-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-pythonperf1_win32-x86-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.svg) | 1.077x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-pythonperf1_win32-x86-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-pythonperf1_win32-x86-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.svg) | 1.078x ↓<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-pythonperf1_win32-x86-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-pythonperf1_win32-x86-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.svg) | 1.085x ↓<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-pythonperf1_win32-x86-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-pythonperf1_win32-x86-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base.svg) |
| [2025-04-26](results/bm-20250426-3.14.0a7%2B-4f18916) | python/4f18916c5c28321f363e | 4f18916 | 1.152x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916/bm-20250426-pythonperf1_win32-x86-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916/bm-20250426-pythonperf1_win32-x86-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.svg) | 1.179x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916/bm-20250426-pythonperf1_win32-x86-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916/bm-20250426-pythonperf1_win32-x86-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.svg) | 1.006x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916/bm-20250426-pythonperf1_win32-x86-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916/bm-20250426-pythonperf1_win32-x86-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.svg) |  |

## darwin arm64 (darwin)
| date | fork/ref | hash/flags | vs. 3.10.4: | vs. 3.12.0: | vs. 3.13.0: | vs. base: |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| [2025-04-26](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL) | python/4f18916c5c28321f363e | 4f18916 (NOGIL) | 1.370x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.svg) | 1.092x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.svg) | 1.094x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.svg) | 1.010x ↓<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base.svg)[🧠](results/bm-20250426-3.14.0a7%2B-4f18916-NOGIL/bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base-mem.svg) |
| [2025-04-26](results/bm-20250426-3.14.0a7%2B-4f18916-JIT) | python/4f18916c5c28321f363e | 4f18916 (JIT) | 1.261x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.svg) | 1.008x ↓<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.svg) | 1.007x ↓<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.svg) | 1.099x ↓<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base.svg)[🧠](results/bm-20250426-3.14.0a7%2B-4f18916-JIT/bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base-mem.svg) |
| [2025-04-26](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG) | python/4f18916c5c28321f363e | 4f18916 (CLANG) | 1.472x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG/bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG/bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.svg) | 1.156x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG/bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG/bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.svg) | 1.158x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG/bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG/bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.svg) | 1.052x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG/bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG/bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base.svg)[🧠](results/bm-20250426-3.14.0a7%2B-4f18916-CLANG/bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-base-mem.svg) |
| [2025-04-26](results/bm-20250426-3.14.0a7%2B-4f18916) | python/4f18916c5c28321f363e | 4f18916 | 1.401x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916/bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916/bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.10.4.svg) | 1.101x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916/bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916/bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.12.0.svg) | 1.102x ↑<br>[📄](results/bm-20250426-3.14.0a7%2B-4f18916/bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.md)[📈](results/bm-20250426-3.14.0a7%2B-4f18916/bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7%2B-4f18916-vs-3.13.0.svg) |  |


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
