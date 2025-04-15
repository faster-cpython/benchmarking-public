# Faster CPython Benchmark Infrastructure

🔒 [▶️ START A BENCHMARK RUN](../../actions/workflows/benchmark.yml)

## Results

Here are some recent and important revisions. 👉 [Complete list of results](RESULTS.md).

[Currently failing benchmarks](failures.md).

**Key:** 📄: table, 📈: time plot, 🧠: memory plot

<!-- START table -->
- [Most recent  pystats on main (718d234)](results/bm-20250412-3.14.0a7%2B-718d234/bm-20250412-azure-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-pystats.md)
- [Most recent PYTHON_UOPS pystats on main (9d34f60)](results/bm-20240215-3.13.0a4-9d34f60-PYTHON_UOPS/bm-20240215-azure-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60-pystats.md)
- [Most recent JIT pystats on main (8421b64)](results/bm-20250408-3.14.0a7%2B-8421b64-JIT/bm-20250408-azure-x86_64-python-8421b648e91981e393a7-3.14.0a7%2B-8421b64-pystats.md)

## linux aarch64 (arminc)
| date | fork/ref | hash/flags | vs. 3.10.4: | vs. 3.12.0: | vs. 3.13.0: | vs. base: |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| [2025-04-12](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL) | python/718d234e4086a65d78c8 | 718d234 (NOGIL) | 1.181x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.svg) | 1.054x ↓<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.svg) | 1.063x ↓<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.svg) | 1.128x ↓<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.svg)[🧠](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base-mem.svg) |
| [2025-04-12](results/bm-20250412-3.14.0a7%2B-718d234-JIT) | python/718d234e4086a65d78c8 | 718d234 (JIT) | 1.318x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.svg) | 1.041x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.svg) | 1.043x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.svg) | 1.025x ↓<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.svg)[🧠](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base-mem.svg) |
| [2025-04-12](results/bm-20250412-3.14.0a7%2B-718d234-CLANG) | python/718d234e4086a65d78c8 | 718d234 (CLANG) | 1.375x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-CLANG/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-CLANG/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.svg) | 1.088x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-CLANG/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-CLANG/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.svg) | 1.085x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-CLANG/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-CLANG/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.svg) | 1.010x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-CLANG/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-CLANG/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.svg)[🧠](results/bm-20250412-3.14.0a7%2B-718d234-CLANG/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base-mem.svg) |
| [2025-04-12](results/bm-20250412-3.14.0a7%2B-718d234) | python/718d234e4086a65d78c8 | 718d234 | 1.359x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.svg) | 1.074x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.svg) | 1.069x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.svg) |  |

## linux x86_64 (linux)
| date | fork/ref | hash/flags | vs. 3.10.4: | vs. 3.12.0: | vs. 3.13.0: | vs. base: |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| [2025-04-15](results/bm-20250415-3.14.0a7%2B-89a680f) | mdboom/pyframe_clearexceptc | 89a680f | 1.461x ↑<br>[📄](results/bm-20250415-3.14.0a7%2B-89a680f/bm-20250415-linux-x86_64-mdboom-pyframe_clearexceptc-3.14.0a7%2B-89a680f-vs-3.10.4.md)[📈](results/bm-20250415-3.14.0a7%2B-89a680f/bm-20250415-linux-x86_64-mdboom-pyframe_clearexceptc-3.14.0a7%2B-89a680f-vs-3.10.4.svg) | 1.127x ↑<br>[📄](results/bm-20250415-3.14.0a7%2B-89a680f/bm-20250415-linux-x86_64-mdboom-pyframe_clearexceptc-3.14.0a7%2B-89a680f-vs-3.12.0.md)[📈](results/bm-20250415-3.14.0a7%2B-89a680f/bm-20250415-linux-x86_64-mdboom-pyframe_clearexceptc-3.14.0a7%2B-89a680f-vs-3.12.0.svg) | 1.056x ↑<br>[📄](results/bm-20250415-3.14.0a7%2B-89a680f/bm-20250415-linux-x86_64-mdboom-pyframe_clearexceptc-3.14.0a7%2B-89a680f-vs-3.13.0.md)[📈](results/bm-20250415-3.14.0a7%2B-89a680f/bm-20250415-linux-x86_64-mdboom-pyframe_clearexceptc-3.14.0a7%2B-89a680f-vs-3.13.0.svg) |  |
| [2025-04-15](results/bm-20250415-3.14.0a7%2B-b1b1252) | faster-cpython/fix_132508 | b1b1252 | 1.465x ↑<br>[📄](results/bm-20250415-3.14.0a7%2B-b1b1252/bm-20250415-linux-x86_64-faster%252dcpython-fix_132508-3.14.0a7%2B-b1b1252-vs-3.10.4.md)[📈](results/bm-20250415-3.14.0a7%2B-b1b1252/bm-20250415-linux-x86_64-faster%252dcpython-fix_132508-3.14.0a7%2B-b1b1252-vs-3.10.4.svg) | 1.130x ↑<br>[📄](results/bm-20250415-3.14.0a7%2B-b1b1252/bm-20250415-linux-x86_64-faster%252dcpython-fix_132508-3.14.0a7%2B-b1b1252-vs-3.12.0.md)[📈](results/bm-20250415-3.14.0a7%2B-b1b1252/bm-20250415-linux-x86_64-faster%252dcpython-fix_132508-3.14.0a7%2B-b1b1252-vs-3.12.0.svg) | 1.058x ↑<br>[📄](results/bm-20250415-3.14.0a7%2B-b1b1252/bm-20250415-linux-x86_64-faster%252dcpython-fix_132508-3.14.0a7%2B-b1b1252-vs-3.13.0.md)[📈](results/bm-20250415-3.14.0a7%2B-b1b1252/bm-20250415-linux-x86_64-faster%252dcpython-fix_132508-3.14.0a7%2B-b1b1252-vs-3.13.0.svg) | 1.000x ↑<br>[📄](results/bm-20250415-3.14.0a7%2B-b1b1252/bm-20250415-linux-x86_64-faster%252dcpython-fix_132508-3.14.0a7%2B-b1b1252-vs-base.md)[📈](results/bm-20250415-3.14.0a7%2B-b1b1252/bm-20250415-linux-x86_64-faster%252dcpython-fix_132508-3.14.0a7%2B-b1b1252-vs-base.svg)[🧠](results/bm-20250415-3.14.0a7%2B-b1b1252/bm-20250415-linux-x86_64-faster%252dcpython-fix_132508-3.14.0a7%2B-b1b1252-vs-base-mem.svg) |
| [2025-04-14](results/bm-20250414-3.14.0a7%2B-844596c) | python/844596c09fc812a58ac1 | 844596c | 1.466x ↑<br>[📄](results/bm-20250414-3.14.0a7%2B-844596c/bm-20250414-linux-x86_64-python-844596c09fc812a58ac1-3.14.0a7%2B-844596c-vs-3.10.4.md)[📈](results/bm-20250414-3.14.0a7%2B-844596c/bm-20250414-linux-x86_64-python-844596c09fc812a58ac1-3.14.0a7%2B-844596c-vs-3.10.4.svg) | 1.130x ↑<br>[📄](results/bm-20250414-3.14.0a7%2B-844596c/bm-20250414-linux-x86_64-python-844596c09fc812a58ac1-3.14.0a7%2B-844596c-vs-3.12.0.md)[📈](results/bm-20250414-3.14.0a7%2B-844596c/bm-20250414-linux-x86_64-python-844596c09fc812a58ac1-3.14.0a7%2B-844596c-vs-3.12.0.svg) | 1.058x ↑<br>[📄](results/bm-20250414-3.14.0a7%2B-844596c/bm-20250414-linux-x86_64-python-844596c09fc812a58ac1-3.14.0a7%2B-844596c-vs-3.13.0.md)[📈](results/bm-20250414-3.14.0a7%2B-844596c/bm-20250414-linux-x86_64-python-844596c09fc812a58ac1-3.14.0a7%2B-844596c-vs-3.13.0.svg) |  |
| [2025-04-12](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL) | python/718d234e4086a65d78c8 | 718d234 (NOGIL) | 1.327x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL/bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL/bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.svg) | 1.037x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL/bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL/bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.svg) | 1.033x ↓<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL/bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL/bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.svg) | 1.087x ↓<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL/bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL/bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.svg)[🧠](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL/bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base-mem.svg) |
| [2025-04-12](results/bm-20250412-3.14.0a7%2B-718d234-JIT) | python/718d234e4086a65d78c8 | 718d234 (JIT) | 1.468x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.svg) | 1.132x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.svg) | 1.059x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.svg) | 1.001x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.svg)[🧠](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base-mem.svg) |
| [2025-04-12](results/bm-20250412-3.14.0a7%2B-718d234-CLANG) | python/718d234e4086a65d78c8 | 718d234 (CLANG) | 1.516x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-CLANG/bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-CLANG/bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.svg) | 1.168x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-CLANG/bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-CLANG/bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.svg) | 1.092x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-CLANG/bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-CLANG/bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.svg) | 1.032x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-CLANG/bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-CLANG/bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.svg)[🧠](results/bm-20250412-3.14.0a7%2B-718d234-CLANG/bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base-mem.svg) |
| [2025-04-12](results/bm-20250412-3.14.0a7%2B-718d234) | python/718d234e4086a65d78c8 | 718d234 | 1.465x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234/bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234/bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.svg) | 1.130x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234/bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234/bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.svg) | 1.058x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234/bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234/bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.svg) |  |
| [2025-04-12](results/bm-20250412-3.14.0a7%2B-3d9cf36) | iritkatriel/dicts_plus | 3d9cf36 | 1.474x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-3d9cf36/bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7%2B-3d9cf36-vs-3.10.4.md)[📈](results/bm-20250412-3.14.0a7%2B-3d9cf36/bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7%2B-3d9cf36-vs-3.10.4.svg) | 1.136x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-3d9cf36/bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7%2B-3d9cf36-vs-3.12.0.md)[📈](results/bm-20250412-3.14.0a7%2B-3d9cf36/bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7%2B-3d9cf36-vs-3.12.0.svg) | 1.064x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-3d9cf36/bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7%2B-3d9cf36-vs-3.13.0.md)[📈](results/bm-20250412-3.14.0a7%2B-3d9cf36/bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7%2B-3d9cf36-vs-3.13.0.svg) | 1.009x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-3d9cf36/bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7%2B-3d9cf36-vs-base.md)[📈](results/bm-20250412-3.14.0a7%2B-3d9cf36/bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7%2B-3d9cf36-vs-base.svg)[🧠](results/bm-20250412-3.14.0a7%2B-3d9cf36/bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7%2B-3d9cf36-vs-base-mem.svg) |
| [2025-04-10](results/bm-20250410-3.14.0a7%2B-07b8d31) | python/07b8d3117fdbc4e5be55 | 07b8d31 | 1.459x ↑<br>[📄](results/bm-20250410-3.14.0a7%2B-07b8d31/bm-20250410-linux-x86_64-python-07b8d3117fdbc4e5be55-3.14.0a7%2B-07b8d31-vs-3.10.4.md)[📈](results/bm-20250410-3.14.0a7%2B-07b8d31/bm-20250410-linux-x86_64-python-07b8d3117fdbc4e5be55-3.14.0a7%2B-07b8d31-vs-3.10.4.svg) | 1.125x ↑<br>[📄](results/bm-20250410-3.14.0a7%2B-07b8d31/bm-20250410-linux-x86_64-python-07b8d3117fdbc4e5be55-3.14.0a7%2B-07b8d31-vs-3.12.0.md)[📈](results/bm-20250410-3.14.0a7%2B-07b8d31/bm-20250410-linux-x86_64-python-07b8d3117fdbc4e5be55-3.14.0a7%2B-07b8d31-vs-3.12.0.svg) | 1.054x ↑<br>[📄](results/bm-20250410-3.14.0a7%2B-07b8d31/bm-20250410-linux-x86_64-python-07b8d3117fdbc4e5be55-3.14.0a7%2B-07b8d31-vs-3.13.0.md)[📈](results/bm-20250410-3.14.0a7%2B-07b8d31/bm-20250410-linux-x86_64-python-07b8d3117fdbc4e5be55-3.14.0a7%2B-07b8d31-vs-3.13.0.svg) |  |
| [2025-04-08](results/bm-20250408-3.14.0a7%2B-77f3e29) | eendebakpt/list_freelist_plus | 77f3e29 | 1.474x ↑<br>[📄](results/bm-20250408-3.14.0a7%2B-77f3e29/bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7%2B-77f3e29-vs-3.10.4.md)[📈](results/bm-20250408-3.14.0a7%2B-77f3e29/bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7%2B-77f3e29-vs-3.10.4.svg) | 1.137x ↑<br>[📄](results/bm-20250408-3.14.0a7%2B-77f3e29/bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7%2B-77f3e29-vs-3.12.0.md)[📈](results/bm-20250408-3.14.0a7%2B-77f3e29/bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7%2B-77f3e29-vs-3.12.0.svg) | 1.064x ↑<br>[📄](results/bm-20250408-3.14.0a7%2B-77f3e29/bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7%2B-77f3e29-vs-3.13.0.md)[📈](results/bm-20250408-3.14.0a7%2B-77f3e29/bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7%2B-77f3e29-vs-3.13.0.svg) | 1.003x ↓<br>[📄](results/bm-20250408-3.14.0a7%2B-77f3e29/bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7%2B-77f3e29-vs-base.md)[📈](results/bm-20250408-3.14.0a7%2B-77f3e29/bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7%2B-77f3e29-vs-base.svg)[🧠](results/bm-20250408-3.14.0a7%2B-77f3e29/bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7%2B-77f3e29-vs-base-mem.svg) |
| [2025-04-08](results/bm-20250408-3.14.0a7%2B-f5f1ac8) | python/f5f1ac84b3b9d688b9e7 | f5f1ac8 | 1.477x ↑<br>[📄](results/bm-20250408-3.14.0a7%2B-f5f1ac8/bm-20250408-linux-x86_64-python-f5f1ac84b3b9d688b9e7-3.14.0a7%2B-f5f1ac8-vs-3.10.4.md)[📈](results/bm-20250408-3.14.0a7%2B-f5f1ac8/bm-20250408-linux-x86_64-python-f5f1ac84b3b9d688b9e7-3.14.0a7%2B-f5f1ac8-vs-3.10.4.svg) | 1.139x ↑<br>[📄](results/bm-20250408-3.14.0a7%2B-f5f1ac8/bm-20250408-linux-x86_64-python-f5f1ac84b3b9d688b9e7-3.14.0a7%2B-f5f1ac8-vs-3.12.0.md)[📈](results/bm-20250408-3.14.0a7%2B-f5f1ac8/bm-20250408-linux-x86_64-python-f5f1ac84b3b9d688b9e7-3.14.0a7%2B-f5f1ac8-vs-3.12.0.svg) | 1.066x ↑<br>[📄](results/bm-20250408-3.14.0a7%2B-f5f1ac8/bm-20250408-linux-x86_64-python-f5f1ac84b3b9d688b9e7-3.14.0a7%2B-f5f1ac8-vs-3.13.0.md)[📈](results/bm-20250408-3.14.0a7%2B-f5f1ac8/bm-20250408-linux-x86_64-python-f5f1ac84b3b9d688b9e7-3.14.0a7%2B-f5f1ac8-vs-3.13.0.svg) |  |
| [2025-04-08](results/bm-20250408-3.14.0a7%2B-8421b64) | brandtbucher/8421b648e91981e393a7 | 8421b64 | 1.478x ↑<br>[📄](results/bm-20250408-3.14.0a7%2B-8421b64/bm-20250408-linux-x86_64-brandtbucher-8421b648e91981e393a7-3.14.0a7%2B-8421b64-vs-3.10.4.md)[📈](results/bm-20250408-3.14.0a7%2B-8421b64/bm-20250408-linux-x86_64-brandtbucher-8421b648e91981e393a7-3.14.0a7%2B-8421b64-vs-3.10.4.svg) | 1.139x ↑<br>[📄](results/bm-20250408-3.14.0a7%2B-8421b64/bm-20250408-linux-x86_64-brandtbucher-8421b648e91981e393a7-3.14.0a7%2B-8421b64-vs-3.12.0.md)[📈](results/bm-20250408-3.14.0a7%2B-8421b64/bm-20250408-linux-x86_64-brandtbucher-8421b648e91981e393a7-3.14.0a7%2B-8421b64-vs-3.12.0.svg) | 1.066x ↑<br>[📄](results/bm-20250408-3.14.0a7%2B-8421b64/bm-20250408-linux-x86_64-brandtbucher-8421b648e91981e393a7-3.14.0a7%2B-8421b64-vs-3.13.0.md)[📈](results/bm-20250408-3.14.0a7%2B-8421b64/bm-20250408-linux-x86_64-brandtbucher-8421b648e91981e393a7-3.14.0a7%2B-8421b64-vs-3.13.0.svg) |  |

## linux x86_64 (pythonperf2)
| date | fork/ref | hash/flags | vs. 3.10.4: | vs. 3.12.0: | vs. 3.13.0: | vs. base: |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| [2025-04-15](results/bm-20250415-3.14.0a7%2B-2ff5eb8) | python/2ff5eb8582939eb9182d | 2ff5eb8 | 1.374x ↑<br>[📄](results/bm-20250415-3.14.0a7%2B-2ff5eb8/bm-20250415-pythonperf2-x86_64-python-2ff5eb8582939eb9182d-3.14.0a7%2B-2ff5eb8-vs-3.10.4.md)[📈](results/bm-20250415-3.14.0a7%2B-2ff5eb8/bm-20250415-pythonperf2-x86_64-python-2ff5eb8582939eb9182d-3.14.0a7%2B-2ff5eb8-vs-3.10.4.svg) | 1.068x ↑<br>[📄](results/bm-20250415-3.14.0a7%2B-2ff5eb8/bm-20250415-pythonperf2-x86_64-python-2ff5eb8582939eb9182d-3.14.0a7%2B-2ff5eb8-vs-3.12.0.md)[📈](results/bm-20250415-3.14.0a7%2B-2ff5eb8/bm-20250415-pythonperf2-x86_64-python-2ff5eb8582939eb9182d-3.14.0a7%2B-2ff5eb8-vs-3.12.0.svg) | 1.079x ↑<br>[📄](results/bm-20250415-3.14.0a7%2B-2ff5eb8/bm-20250415-pythonperf2-x86_64-python-2ff5eb8582939eb9182d-3.14.0a7%2B-2ff5eb8-vs-3.13.0.md)[📈](results/bm-20250415-3.14.0a7%2B-2ff5eb8/bm-20250415-pythonperf2-x86_64-python-2ff5eb8582939eb9182d-3.14.0a7%2B-2ff5eb8-vs-3.13.0.svg) |  |
| [2025-04-12](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL) | python/718d234e4086a65d78c8 | 718d234 (NOGIL) | 1.254x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL/bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL/bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.svg) | 1.011x ↓<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL/bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL/bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.svg) | 1.005x ↓<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL/bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL/bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.svg) | 1.081x ↓<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL/bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL/bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.svg)[🧠](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL/bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base-mem.svg) |
| [2025-04-12](results/bm-20250412-3.14.0a7%2B-718d234-JIT) | python/718d234e4086a65d78c8 | 718d234 (JIT) | 1.368x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.svg) | 1.064x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.svg) | 1.075x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.svg) | 1.004x ↓<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.svg)[🧠](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base-mem.svg) |
| [2025-04-12](results/bm-20250412-3.14.0a7%2B-718d234-CLANG) | python/718d234e4086a65d78c8 | 718d234 (CLANG) | 1.421x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-CLANG/bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-CLANG/bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.svg) | 1.103x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-CLANG/bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-CLANG/bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.svg) | 1.113x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-CLANG/bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-CLANG/bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.svg) | 1.032x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-CLANG/bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-CLANG/bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.svg)[🧠](results/bm-20250412-3.14.0a7%2B-718d234-CLANG/bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base-mem.svg) |
| [2025-04-12](results/bm-20250412-3.14.0a7%2B-718d234) | python/718d234e4086a65d78c8 | 718d234 | 1.375x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234/bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234/bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.svg) | 1.068x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234/bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234/bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.svg) | 1.079x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234/bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234/bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.svg) |  |

## windows amd64 (pythonperf1)
| date | fork/ref | hash/flags | vs. 3.10.4: | vs. 3.12.0: | vs. 3.13.0: | vs. base: |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| [2025-04-12](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL) | python/718d234e4086a65d78c8 | 718d234 (NOGIL) | 1.158x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL/bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL/bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.svg) | 1.000x ↓<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL/bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL/bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.svg) | 1.050x ↓<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL/bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL/bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.svg) | 1.100x ↓<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL/bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL/bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.svg) |
| [2025-04-12](results/bm-20250412-3.14.0a7%2B-718d234-JIT) | python/718d234e4086a65d78c8 | 718d234 (JIT) | 1.292x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.svg) | 1.101x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.svg) | 1.035x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.svg) | 1.013x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.svg) |
| [2025-04-12](results/bm-20250412-3.14.0a7%2B-718d234-CLANG) | python/718d234e4086a65d78c8 | 718d234 (CLANG) | 1.513x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-CLANG/bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-CLANG/bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.svg) | 1.283x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-CLANG/bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-CLANG/bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.svg) | 1.197x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-CLANG/bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-CLANG/bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.svg) | 1.175x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-CLANG/bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-CLANG/bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.svg) |
| [2025-04-12](results/bm-20250412-3.14.0a7%2B-718d234) | python/718d234e4086a65d78c8 | 718d234 | 1.275x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234/bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234/bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.svg) | 1.084x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234/bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234/bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.svg) | 1.021x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234/bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234/bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.svg) |  |

## windows amd64 (pythonperf1_win32)
| date | fork/ref | hash/flags | vs. 3.10.4: | vs. 3.12.0: | vs. 3.13.0: | vs. base: |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| [2025-03-07](results/bm-20250307-3.14.0a5%2B-06bc3bd) | brandtbucher/msvc_musttail | 06bc3bd | 1.391x ↑<br>[📄](results/bm-20250307-3.14.0a5%2B-06bc3bd/bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5%2B-06bc3bd-vs-3.10.4.md)[📈](results/bm-20250307-3.14.0a5%2B-06bc3bd/bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5%2B-06bc3bd-vs-3.10.4.svg) | 1.407x ↑<br>[📄](results/bm-20250307-3.14.0a5%2B-06bc3bd/bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5%2B-06bc3bd-vs-3.12.0.md)[📈](results/bm-20250307-3.14.0a5%2B-06bc3bd/bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5%2B-06bc3bd-vs-3.12.0.svg) | 1.203x ↑<br>[📄](results/bm-20250307-3.14.0a5%2B-06bc3bd/bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5%2B-06bc3bd-vs-3.13.0.md)[📈](results/bm-20250307-3.14.0a5%2B-06bc3bd/bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5%2B-06bc3bd-vs-3.13.0.svg) |  |
| [2025-03-07](results/bm-20250225-3.14.0a5%2B-f963239) | brandtbucher/msvc_musttail | 06bc3bd | 1.391x ↑<br>[📄](results/bm-20250225-3.14.0a5%2B-f963239/bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5%2B-06bc3bd-vs-3.10.4.md)[📈](results/bm-20250225-3.14.0a5%2B-f963239/bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5%2B-06bc3bd-vs-3.10.4.svg) | 1.407x ↑<br>[📄](results/bm-20250225-3.14.0a5%2B-f963239/bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5%2B-06bc3bd-vs-3.12.0.md)[📈](results/bm-20250225-3.14.0a5%2B-f963239/bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5%2B-06bc3bd-vs-3.12.0.svg) | 1.203x ↑<br>[📄](results/bm-20250225-3.14.0a5%2B-f963239/bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5%2B-06bc3bd-vs-3.13.0.md)[📈](results/bm-20250225-3.14.0a5%2B-f963239/bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5%2B-06bc3bd-vs-3.13.0.svg) |  |

## windows x86 (pythonperf1_win32)
| date | fork/ref | hash/flags | vs. 3.10.4: | vs. 3.12.0: | vs. 3.13.0: | vs. base: |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| [2025-04-12](results/bm-20250412-3.14.0a7%2B-718d234-JIT) | python/718d234e4086a65d78c8 | 718d234 (JIT) | 1.079x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-pythonperf1_win32-x86-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-pythonperf1_win32-x86-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.svg) | 1.102x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-pythonperf1_win32-x86-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-pythonperf1_win32-x86-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.svg) | 1.057x ↓<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-pythonperf1_win32-x86-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-pythonperf1_win32-x86-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.svg) | 1.071x ↓<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-pythonperf1_win32-x86-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-pythonperf1_win32-x86-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.svg) |
| [2025-04-12](results/bm-20250412-3.14.0a7%2B-718d234) | python/718d234e4086a65d78c8 | 718d234 | 1.164x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234/bm-20250412-pythonperf1_win32-x86-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234/bm-20250412-pythonperf1_win32-x86-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.svg) | 1.190x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234/bm-20250412-pythonperf1_win32-x86-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234/bm-20250412-pythonperf1_win32-x86-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.svg) | 1.015x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234/bm-20250412-pythonperf1_win32-x86-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234/bm-20250412-pythonperf1_win32-x86-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.svg) |  |
| [2025-04-05](results/bm-20250405-3.14.0a6%2B-85bc489-NOGIL) | python/85bc489b649fe261f962 | 85bc489 (NOGIL) | 1.078x ↑<br>[📄](results/bm-20250405-3.14.0a6%2B-85bc489-NOGIL/bm-20250405-pythonperf1_win32-x86-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-3.10.4.md)[📈](results/bm-20250405-3.14.0a6%2B-85bc489-NOGIL/bm-20250405-pythonperf1_win32-x86-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-3.10.4.svg) | 1.114x ↑<br>[📄](results/bm-20250405-3.14.0a6%2B-85bc489-NOGIL/bm-20250405-pythonperf1_win32-x86-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-3.12.0.md)[📈](results/bm-20250405-3.14.0a6%2B-85bc489-NOGIL/bm-20250405-pythonperf1_win32-x86-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-3.12.0.svg) | 1.045x ↓<br>[📄](results/bm-20250405-3.14.0a6%2B-85bc489-NOGIL/bm-20250405-pythonperf1_win32-x86-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-3.13.0.md)[📈](results/bm-20250405-3.14.0a6%2B-85bc489-NOGIL/bm-20250405-pythonperf1_win32-x86-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-3.13.0.svg) | 1.090x ↓<br>[📄](results/bm-20250405-3.14.0a6%2B-85bc489-NOGIL/bm-20250405-pythonperf1_win32-x86-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-base.md)[📈](results/bm-20250405-3.14.0a6%2B-85bc489-NOGIL/bm-20250405-pythonperf1_win32-x86-python-85bc489b649fe261f962-3.14.0a6%2B-85bc489-vs-base.svg) |

## darwin arm64 (darwin)
| date | fork/ref | hash/flags | vs. 3.10.4: | vs. 3.12.0: | vs. 3.13.0: | vs. base: |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| [2025-04-12](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL) | python/718d234e4086a65d78c8 | 718d234 (NOGIL) | 1.213x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL/bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL/bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.svg) | 1.032x ↓<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL/bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL/bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.svg) | 1.030x ↓<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL/bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL/bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.svg) | 1.003x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL/bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL/bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.svg)[🧠](results/bm-20250412-3.14.0a7%2B-718d234-NOGIL/bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base-mem.svg) |
| [2025-04-12](results/bm-20250412-3.14.0a7%2B-718d234-JIT) | python/718d234e4086a65d78c8 | 718d234 (JIT) | 1.399x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.svg) | 1.099x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.svg) | 1.101x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.svg) | 1.143x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.svg)[🧠](results/bm-20250412-3.14.0a7%2B-718d234-JIT/bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base-mem.svg) |
| [2025-04-12](results/bm-20250412-3.14.0a7%2B-718d234-CLANG) | python/718d234e4086a65d78c8 | 718d234 (CLANG) | 1.476x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-CLANG/bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-CLANG/bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.svg) | 1.159x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-CLANG/bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-CLANG/bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.svg) | 1.160x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-CLANG/bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-CLANG/bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.svg) | 1.206x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234-CLANG/bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234-CLANG/bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.svg)[🧠](results/bm-20250412-3.14.0a7%2B-718d234-CLANG/bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base-mem.svg) |
| [2025-04-12](results/bm-20250412-3.14.0a7%2B-718d234) | python/718d234e4086a65d78c8 | 718d234 | 1.226x ↑<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234/bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234/bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.svg) | 1.036x ↓<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234/bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234/bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.svg) | 1.034x ↓<br>[📄](results/bm-20250412-3.14.0a7%2B-718d234/bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.md)[📈](results/bm-20250412-3.14.0a7%2B-718d234/bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.svg) |  |


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
