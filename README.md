# Faster CPython Benchmark Infrastructure

🔒 [▶️ START A BENCHMARK RUN](../../actions/workflows/benchmark.yml)

## Results

Here are some recent and important revisions. 👉 [Complete list of results](RESULTS.md).

[Currently failing benchmarks](failures.md).

**Key:** 📄: table, 📈: time plot, 🧠: memory plot

<!-- START table -->
[Most recent pystats on main (61b35f7)](results/bm-20250118-3.14.0a4%2B-61b35f7-PYTHON_UOPS/bm-20250118-azure-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-pystats.md)

## linux aarch64 (arminc)
| date | fork/ref | hash/flags | vs. 3.10.4: | vs. 3.12.0: | vs. 3.13.0: | vs. base: |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| [2025-01-18](results/bm-20250118-3.14.0a4%2B-61b35f7-NOGIL) | python/61b35f74aa4a6ac60663 | 61b35f7 (NOGIL) | 1.092x ↑<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7-NOGIL/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.10.4.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7-NOGIL/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.10.4.svg) | 1.132x ↓<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7-NOGIL/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.12.0.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7-NOGIL/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.12.0.svg) | 1.134x ↓<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7-NOGIL/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.13.0.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7-NOGIL/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.13.0.svg) | 1.172x ↓<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7-NOGIL/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-base.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7-NOGIL/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-base.svg)[🧠](results/bm-20250118-3.14.0a4%2B-61b35f7-NOGIL/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-base-mem.svg) |
| [2025-01-18](results/bm-20250118-3.14.0a4%2B-61b35f7) | python/61b35f74aa4a6ac60663 | 61b35f7 | 1.327x ↑<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.10.4.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.10.4.svg) | 1.044x ↑<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.12.0.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.12.0.svg) | 1.044x ↑<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.13.0.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.13.0.svg) |  |
| [2025-01-18](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT) | python/61b35f74aa4a6ac60663 | 61b35f7 (JIT) | 1.218x ↑<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.10.4.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.10.4.svg) | 1.037x ↓<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.12.0.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.12.0.svg) | 1.031x ↓<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.13.0.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.13.0.svg) | 1.072x ↓<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-base.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-base.svg)[🧠](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-base-mem.svg) |
| [2025-01-16](results/bm-20250116-3.14.0a4%2B-df5d01c-CLANG) | Fidget-Spinner/tail_call | df5d01c (CLANG) | 1.355x ↑<br>[📄](results/bm-20250116-3.14.0a4%2B-df5d01c-CLANG/bm-20250116-arminc-aarch64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-3.10.4.md)[📈](results/bm-20250116-3.14.0a4%2B-df5d01c-CLANG/bm-20250116-arminc-aarch64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-3.10.4.svg) | 1.062x ↑<br>[📄](results/bm-20250116-3.14.0a4%2B-df5d01c-CLANG/bm-20250116-arminc-aarch64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-3.12.0.md)[📈](results/bm-20250116-3.14.0a4%2B-df5d01c-CLANG/bm-20250116-arminc-aarch64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-3.12.0.svg) | 1.060x ↑<br>[📄](results/bm-20250116-3.14.0a4%2B-df5d01c-CLANG/bm-20250116-arminc-aarch64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-3.13.0.md)[📈](results/bm-20250116-3.14.0a4%2B-df5d01c-CLANG/bm-20250116-arminc-aarch64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-3.13.0.svg) | 1.085x ↑<br>[📄](results/bm-20250116-3.14.0a4%2B-df5d01c-CLANG/bm-20250116-arminc-aarch64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-base.md)[📈](results/bm-20250116-3.14.0a4%2B-df5d01c-CLANG/bm-20250116-arminc-aarch64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-base.svg)[🧠](results/bm-20250116-3.14.0a4%2B-df5d01c-CLANG/bm-20250116-arminc-aarch64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-base-mem.svg) |
| [2025-01-16](results/bm-20250116-3.14.0a4%2B-313b96e-CLANG) | python/313b96eb8b8d0ad3bac5 | 313b96e (CLANG) | 1.238x ↑<br>[📄](results/bm-20250116-3.14.0a4%2B-313b96e-CLANG/bm-20250116-arminc-aarch64-python-313b96eb8b8d0ad3bac5-3.14.0a4%2B-313b96e-vs-3.10.4.md)[📈](results/bm-20250116-3.14.0a4%2B-313b96e-CLANG/bm-20250116-arminc-aarch64-python-313b96eb8b8d0ad3bac5-3.14.0a4%2B-313b96e-vs-3.10.4.svg) | 1.023x ↓<br>[📄](results/bm-20250116-3.14.0a4%2B-313b96e-CLANG/bm-20250116-arminc-aarch64-python-313b96eb8b8d0ad3bac5-3.14.0a4%2B-313b96e-vs-3.12.0.md)[📈](results/bm-20250116-3.14.0a4%2B-313b96e-CLANG/bm-20250116-arminc-aarch64-python-313b96eb8b8d0ad3bac5-3.14.0a4%2B-313b96e-vs-3.12.0.svg) | 1.018x ↓<br>[📄](results/bm-20250116-3.14.0a4%2B-313b96e-CLANG/bm-20250116-arminc-aarch64-python-313b96eb8b8d0ad3bac5-3.14.0a4%2B-313b96e-vs-3.13.0.md)[📈](results/bm-20250116-3.14.0a4%2B-313b96e-CLANG/bm-20250116-arminc-aarch64-python-313b96eb8b8d0ad3bac5-3.14.0a4%2B-313b96e-vs-3.13.0.svg) |  |

## linux x86_64 (linux)
| date | fork/ref | hash/flags | vs. 3.10.4: | vs. 3.12.0: | vs. 3.13.0: | vs. base: |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| [2025-01-18](results/bm-20250118-3.14.0a4%2B-61b35f7-NOGIL) | python/61b35f74aa4a6ac60663 | 61b35f7 (NOGIL) | 1.237x ↑<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7-NOGIL/bm-20250118-linux-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.10.4.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7-NOGIL/bm-20250118-linux-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.10.4.svg) | 1.038x ↓<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7-NOGIL/bm-20250118-linux-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.12.0.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7-NOGIL/bm-20250118-linux-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.12.0.svg) | 1.099x ↓<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7-NOGIL/bm-20250118-linux-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.13.0.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7-NOGIL/bm-20250118-linux-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.13.0.svg) | 1.138x ↓<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7-NOGIL/bm-20250118-linux-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-base.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7-NOGIL/bm-20250118-linux-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-base.svg)[🧠](results/bm-20250118-3.14.0a4%2B-61b35f7-NOGIL/bm-20250118-linux-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-base-mem.svg) |
| [2025-01-18](results/bm-20250118-3.14.0a4%2B-61b35f7) | python/61b35f74aa4a6ac60663 | 61b35f7 | 1.449x ↑<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7/bm-20250118-linux-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.10.4.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7/bm-20250118-linux-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.10.4.svg) | 1.114x ↑<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7/bm-20250118-linux-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.12.0.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7/bm-20250118-linux-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.12.0.svg) | 1.046x ↑<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7/bm-20250118-linux-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.13.0.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7/bm-20250118-linux-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.13.0.svg) |  |
| [2025-01-18](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT) | python/61b35f74aa4a6ac60663 | 61b35f7 (JIT) | 1.440x ↑<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-linux-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.10.4.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-linux-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.10.4.svg) | 1.112x ↑<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-linux-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.12.0.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-linux-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.12.0.svg) | 1.040x ↑<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-linux-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.13.0.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-linux-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.13.0.svg) | 1.006x ↓<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-linux-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-base.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-linux-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-base.svg)[🧠](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-linux-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-base-mem.svg) |
| [2025-01-17](results/bm-20250117-3.14.0a4%2B-e43ac58) | iritkatriel/binaryops | e43ac58 | 1.451x ↑<br>[📄](results/bm-20250117-3.14.0a4%2B-e43ac58/bm-20250117-linux-x86_64-iritkatriel-binaryops-3.14.0a4%2B-e43ac58-vs-3.10.4.md)[📈](results/bm-20250117-3.14.0a4%2B-e43ac58/bm-20250117-linux-x86_64-iritkatriel-binaryops-3.14.0a4%2B-e43ac58-vs-3.10.4.svg) | 1.117x ↑<br>[📄](results/bm-20250117-3.14.0a4%2B-e43ac58/bm-20250117-linux-x86_64-iritkatriel-binaryops-3.14.0a4%2B-e43ac58-vs-3.12.0.md)[📈](results/bm-20250117-3.14.0a4%2B-e43ac58/bm-20250117-linux-x86_64-iritkatriel-binaryops-3.14.0a4%2B-e43ac58-vs-3.12.0.svg) | 1.049x ↑<br>[📄](results/bm-20250117-3.14.0a4%2B-e43ac58/bm-20250117-linux-x86_64-iritkatriel-binaryops-3.14.0a4%2B-e43ac58-vs-3.13.0.md)[📈](results/bm-20250117-3.14.0a4%2B-e43ac58/bm-20250117-linux-x86_64-iritkatriel-binaryops-3.14.0a4%2B-e43ac58-vs-3.13.0.svg) | 1.002x ↑<br>[📄](results/bm-20250117-3.14.0a4%2B-e43ac58/bm-20250117-linux-x86_64-iritkatriel-binaryops-3.14.0a4%2B-e43ac58-vs-base.md)[📈](results/bm-20250117-3.14.0a4%2B-e43ac58/bm-20250117-linux-x86_64-iritkatriel-binaryops-3.14.0a4%2B-e43ac58-vs-base.svg)[🧠](results/bm-20250117-3.14.0a4%2B-e43ac58/bm-20250117-linux-x86_64-iritkatriel-binaryops-3.14.0a4%2B-e43ac58-vs-base-mem.svg) |
| [2025-01-17](results/bm-20250117-3.14.0a4%2B-e537b8b-NOGIL) | kumaraditya303/gc | e537b8b (NOGIL) | 1.241x ↑<br>[📄](results/bm-20250117-3.14.0a4%2B-e537b8b-NOGIL/bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4%2B-e537b8b-vs-3.10.4.md)[📈](results/bm-20250117-3.14.0a4%2B-e537b8b-NOGIL/bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4%2B-e537b8b-vs-3.10.4.svg) | 1.035x ↓<br>[📄](results/bm-20250117-3.14.0a4%2B-e537b8b-NOGIL/bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4%2B-e537b8b-vs-3.12.0.md)[📈](results/bm-20250117-3.14.0a4%2B-e537b8b-NOGIL/bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4%2B-e537b8b-vs-3.12.0.svg) | 1.096x ↓<br>[📄](results/bm-20250117-3.14.0a4%2B-e537b8b-NOGIL/bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4%2B-e537b8b-vs-3.13.0.md)[📈](results/bm-20250117-3.14.0a4%2B-e537b8b-NOGIL/bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4%2B-e537b8b-vs-3.13.0.svg) | 1.003x ↓<br>[📄](results/bm-20250117-3.14.0a4%2B-e537b8b-NOGIL/bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4%2B-e537b8b-vs-base.md)[📈](results/bm-20250117-3.14.0a4%2B-e537b8b-NOGIL/bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4%2B-e537b8b-vs-base.svg)[🧠](results/bm-20250117-3.14.0a4%2B-e537b8b-NOGIL/bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4%2B-e537b8b-vs-base-mem.svg) |
| [2025-01-17](results/bm-20250117-3.14.0a4%2B-e537b8b) | kumaraditya303/gc | e537b8b | 1.453x ↑<br>[📄](results/bm-20250117-3.14.0a4%2B-e537b8b/bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4%2B-e537b8b-vs-3.10.4.md)[📈](results/bm-20250117-3.14.0a4%2B-e537b8b/bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4%2B-e537b8b-vs-3.10.4.svg) | 1.118x ↑<br>[📄](results/bm-20250117-3.14.0a4%2B-e537b8b/bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4%2B-e537b8b-vs-3.12.0.md)[📈](results/bm-20250117-3.14.0a4%2B-e537b8b/bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4%2B-e537b8b-vs-3.12.0.svg) | 1.050x ↑<br>[📄](results/bm-20250117-3.14.0a4%2B-e537b8b/bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4%2B-e537b8b-vs-3.13.0.md)[📈](results/bm-20250117-3.14.0a4%2B-e537b8b/bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4%2B-e537b8b-vs-3.13.0.svg) | 1.001x ↓<br>[📄](results/bm-20250117-3.14.0a4%2B-e537b8b/bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4%2B-e537b8b-vs-base.md)[📈](results/bm-20250117-3.14.0a4%2B-e537b8b/bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4%2B-e537b8b-vs-base.svg)[🧠](results/bm-20250117-3.14.0a4%2B-e537b8b/bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4%2B-e537b8b-vs-base-mem.svg) |
| [2025-01-17](results/bm-20250117-3.14.0a4%2B-d95ba9f) | python/d95ba9fa1110534b7247 | d95ba9f | 1.454x ↑<br>[📄](results/bm-20250117-3.14.0a4%2B-d95ba9f/bm-20250117-linux-x86_64-python-d95ba9fa1110534b7247-3.14.0a4%2B-d95ba9f-vs-3.10.4.md)[📈](results/bm-20250117-3.14.0a4%2B-d95ba9f/bm-20250117-linux-x86_64-python-d95ba9fa1110534b7247-3.14.0a4%2B-d95ba9f-vs-3.10.4.svg) | 1.119x ↑<br>[📄](results/bm-20250117-3.14.0a4%2B-d95ba9f/bm-20250117-linux-x86_64-python-d95ba9fa1110534b7247-3.14.0a4%2B-d95ba9f-vs-3.12.0.md)[📈](results/bm-20250117-3.14.0a4%2B-d95ba9f/bm-20250117-linux-x86_64-python-d95ba9fa1110534b7247-3.14.0a4%2B-d95ba9f-vs-3.12.0.svg) | 1.051x ↑<br>[📄](results/bm-20250117-3.14.0a4%2B-d95ba9f/bm-20250117-linux-x86_64-python-d95ba9fa1110534b7247-3.14.0a4%2B-d95ba9f-vs-3.13.0.md)[📈](results/bm-20250117-3.14.0a4%2B-d95ba9f/bm-20250117-linux-x86_64-python-d95ba9fa1110534b7247-3.14.0a4%2B-d95ba9f-vs-3.13.0.svg) |  |
| [2025-01-17](results/bm-20250117-3.14.0a4%2B-d95ba9f-NOGIL) | python/d95ba9fa1110534b7247 | d95ba9f (NOGIL) | 1.246x ↑<br>[📄](results/bm-20250117-3.14.0a4%2B-d95ba9f-NOGIL/bm-20250117-linux-x86_64-python-d95ba9fa1110534b7247-3.14.0a4%2B-d95ba9f-vs-3.10.4.md)[📈](results/bm-20250117-3.14.0a4%2B-d95ba9f-NOGIL/bm-20250117-linux-x86_64-python-d95ba9fa1110534b7247-3.14.0a4%2B-d95ba9f-vs-3.10.4.svg) | 1.031x ↓<br>[📄](results/bm-20250117-3.14.0a4%2B-d95ba9f-NOGIL/bm-20250117-linux-x86_64-python-d95ba9fa1110534b7247-3.14.0a4%2B-d95ba9f-vs-3.12.0.md)[📈](results/bm-20250117-3.14.0a4%2B-d95ba9f-NOGIL/bm-20250117-linux-x86_64-python-d95ba9fa1110534b7247-3.14.0a4%2B-d95ba9f-vs-3.12.0.svg) | 1.093x ↓<br>[📄](results/bm-20250117-3.14.0a4%2B-d95ba9f-NOGIL/bm-20250117-linux-x86_64-python-d95ba9fa1110534b7247-3.14.0a4%2B-d95ba9f-vs-3.13.0.md)[📈](results/bm-20250117-3.14.0a4%2B-d95ba9f-NOGIL/bm-20250117-linux-x86_64-python-d95ba9fa1110534b7247-3.14.0a4%2B-d95ba9f-vs-3.13.0.svg) | 1.137x ↓<br>[📄](results/bm-20250117-3.14.0a4%2B-d95ba9f-NOGIL/bm-20250117-linux-x86_64-python-d95ba9fa1110534b7247-3.14.0a4%2B-d95ba9f-vs-base.md)[📈](results/bm-20250117-3.14.0a4%2B-d95ba9f-NOGIL/bm-20250117-linux-x86_64-python-d95ba9fa1110534b7247-3.14.0a4%2B-d95ba9f-vs-base.svg)[🧠](results/bm-20250117-3.14.0a4%2B-d95ba9f-NOGIL/bm-20250117-linux-x86_64-python-d95ba9fa1110534b7247-3.14.0a4%2B-d95ba9f-vs-base-mem.svg) |
| [2025-01-16](results/bm-20250116-3.14.0a4%2B-c57fe46) | iritkatriel/binaryops | c57fe46 | 1.442x ↑<br>[📄](results/bm-20250116-3.14.0a4%2B-c57fe46/bm-20250116-linux-x86_64-iritkatriel-binaryops-3.14.0a4%2B-c57fe46-vs-3.10.4.md)[📈](results/bm-20250116-3.14.0a4%2B-c57fe46/bm-20250116-linux-x86_64-iritkatriel-binaryops-3.14.0a4%2B-c57fe46-vs-3.10.4.svg) | 1.109x ↑<br>[📄](results/bm-20250116-3.14.0a4%2B-c57fe46/bm-20250116-linux-x86_64-iritkatriel-binaryops-3.14.0a4%2B-c57fe46-vs-3.12.0.md)[📈](results/bm-20250116-3.14.0a4%2B-c57fe46/bm-20250116-linux-x86_64-iritkatriel-binaryops-3.14.0a4%2B-c57fe46-vs-3.12.0.svg) | 1.042x ↑<br>[📄](results/bm-20250116-3.14.0a4%2B-c57fe46/bm-20250116-linux-x86_64-iritkatriel-binaryops-3.14.0a4%2B-c57fe46-vs-3.13.0.md)[📈](results/bm-20250116-3.14.0a4%2B-c57fe46/bm-20250116-linux-x86_64-iritkatriel-binaryops-3.14.0a4%2B-c57fe46-vs-3.13.0.svg) | 1.004x ↓<br>[📄](results/bm-20250116-3.14.0a4%2B-c57fe46/bm-20250116-linux-x86_64-iritkatriel-binaryops-3.14.0a4%2B-c57fe46-vs-base.md)[📈](results/bm-20250116-3.14.0a4%2B-c57fe46/bm-20250116-linux-x86_64-iritkatriel-binaryops-3.14.0a4%2B-c57fe46-vs-base.svg)[🧠](results/bm-20250116-3.14.0a4%2B-c57fe46/bm-20250116-linux-x86_64-iritkatriel-binaryops-3.14.0a4%2B-c57fe46-vs-base-mem.svg) |
| [2025-01-16](results/bm-20250116-3.14.0a4%2B-3893a92) | python/3893a92d956363fa2443 | 3893a92 | 1.449x ↑<br>[📄](results/bm-20250116-3.14.0a4%2B-3893a92/bm-20250116-linux-x86_64-python-3893a92d956363fa2443-3.14.0a4%2B-3893a92-vs-3.10.4.md)[📈](results/bm-20250116-3.14.0a4%2B-3893a92/bm-20250116-linux-x86_64-python-3893a92d956363fa2443-3.14.0a4%2B-3893a92-vs-3.10.4.svg) | 1.115x ↑<br>[📄](results/bm-20250116-3.14.0a4%2B-3893a92/bm-20250116-linux-x86_64-python-3893a92d956363fa2443-3.14.0a4%2B-3893a92-vs-3.12.0.md)[📈](results/bm-20250116-3.14.0a4%2B-3893a92/bm-20250116-linux-x86_64-python-3893a92d956363fa2443-3.14.0a4%2B-3893a92-vs-3.12.0.svg) | 1.047x ↑<br>[📄](results/bm-20250116-3.14.0a4%2B-3893a92/bm-20250116-linux-x86_64-python-3893a92d956363fa2443-3.14.0a4%2B-3893a92-vs-3.13.0.md)[📈](results/bm-20250116-3.14.0a4%2B-3893a92/bm-20250116-linux-x86_64-python-3893a92d956363fa2443-3.14.0a4%2B-3893a92-vs-3.13.0.svg) | 1.003x ↑<br>[📄](results/bm-20250116-3.14.0a4%2B-3893a92/bm-20250116-linux-x86_64-python-3893a92d956363fa2443-3.14.0a4%2B-3893a92-vs-base.md)[📈](results/bm-20250116-3.14.0a4%2B-3893a92/bm-20250116-linux-x86_64-python-3893a92d956363fa2443-3.14.0a4%2B-3893a92-vs-base.svg)[🧠](results/bm-20250116-3.14.0a4%2B-3893a92/bm-20250116-linux-x86_64-python-3893a92d956363fa2443-3.14.0a4%2B-3893a92-vs-base-mem.svg) |
| [2025-01-16](results/bm-20250116-3.14.0a4%2B-27494dd) | python/27494dd9ad6032c29e27 | 27494dd | 1.448x ↑<br>[📄](results/bm-20250116-3.14.0a4%2B-27494dd/bm-20250116-linux-x86_64-python-27494dd9ad6032c29e27-3.14.0a4%2B-27494dd-vs-3.10.4.md)[📈](results/bm-20250116-3.14.0a4%2B-27494dd/bm-20250116-linux-x86_64-python-27494dd9ad6032c29e27-3.14.0a4%2B-27494dd-vs-3.10.4.svg) | 1.113x ↑<br>[📄](results/bm-20250116-3.14.0a4%2B-27494dd/bm-20250116-linux-x86_64-python-27494dd9ad6032c29e27-3.14.0a4%2B-27494dd-vs-3.12.0.md)[📈](results/bm-20250116-3.14.0a4%2B-27494dd/bm-20250116-linux-x86_64-python-27494dd9ad6032c29e27-3.14.0a4%2B-27494dd-vs-3.12.0.svg) | 1.047x ↑<br>[📄](results/bm-20250116-3.14.0a4%2B-27494dd/bm-20250116-linux-x86_64-python-27494dd9ad6032c29e27-3.14.0a4%2B-27494dd-vs-3.13.0.md)[📈](results/bm-20250116-3.14.0a4%2B-27494dd/bm-20250116-linux-x86_64-python-27494dd9ad6032c29e27-3.14.0a4%2B-27494dd-vs-3.13.0.svg) |  |
| [2025-01-16](results/bm-20250116-3.14.0a4%2B-e81fe94) | python/e81fe940c9bd092f6de5 | e81fe94 | 1.444x ↑<br>[📄](results/bm-20250116-3.14.0a4%2B-e81fe94/bm-20250116-linux-x86_64-python-e81fe940c9bd092f6de5-3.14.0a4%2B-e81fe94-vs-3.10.4.md)[📈](results/bm-20250116-3.14.0a4%2B-e81fe94/bm-20250116-linux-x86_64-python-e81fe940c9bd092f6de5-3.14.0a4%2B-e81fe94-vs-3.10.4.svg) | 1.111x ↑<br>[📄](results/bm-20250116-3.14.0a4%2B-e81fe94/bm-20250116-linux-x86_64-python-e81fe940c9bd092f6de5-3.14.0a4%2B-e81fe94-vs-3.12.0.md)[📈](results/bm-20250116-3.14.0a4%2B-e81fe94/bm-20250116-linux-x86_64-python-e81fe940c9bd092f6de5-3.14.0a4%2B-e81fe94-vs-3.12.0.svg) | 1.043x ↑<br>[📄](results/bm-20250116-3.14.0a4%2B-e81fe94/bm-20250116-linux-x86_64-python-e81fe940c9bd092f6de5-3.14.0a4%2B-e81fe94-vs-3.13.0.md)[📈](results/bm-20250116-3.14.0a4%2B-e81fe94/bm-20250116-linux-x86_64-python-e81fe940c9bd092f6de5-3.14.0a4%2B-e81fe94-vs-3.13.0.svg) |  |
| [2025-01-16](results/bm-20250116-3.14.0a4%2B-6ac95d4) | faster-cpython/no_conditional_stack | 6ac95d4 | 1.440x ↑<br>[📄](results/bm-20250116-3.14.0a4%2B-6ac95d4/bm-20250116-linux-x86_64-faster%252dcpython-no_conditional_stack-3.14.0a4%2B-6ac95d4-vs-3.10.4.md)[📈](results/bm-20250116-3.14.0a4%2B-6ac95d4/bm-20250116-linux-x86_64-faster%252dcpython-no_conditional_stack-3.14.0a4%2B-6ac95d4-vs-3.10.4.svg) | 1.108x ↑<br>[📄](results/bm-20250116-3.14.0a4%2B-6ac95d4/bm-20250116-linux-x86_64-faster%252dcpython-no_conditional_stack-3.14.0a4%2B-6ac95d4-vs-3.12.0.md)[📈](results/bm-20250116-3.14.0a4%2B-6ac95d4/bm-20250116-linux-x86_64-faster%252dcpython-no_conditional_stack-3.14.0a4%2B-6ac95d4-vs-3.12.0.svg) | 1.041x ↑<br>[📄](results/bm-20250116-3.14.0a4%2B-6ac95d4/bm-20250116-linux-x86_64-faster%252dcpython-no_conditional_stack-3.14.0a4%2B-6ac95d4-vs-3.13.0.md)[📈](results/bm-20250116-3.14.0a4%2B-6ac95d4/bm-20250116-linux-x86_64-faster%252dcpython-no_conditional_stack-3.14.0a4%2B-6ac95d4-vs-3.13.0.svg) | 1.004x ↓<br>[📄](results/bm-20250116-3.14.0a4%2B-6ac95d4/bm-20250116-linux-x86_64-faster%252dcpython-no_conditional_stack-3.14.0a4%2B-6ac95d4-vs-base.md)[📈](results/bm-20250116-3.14.0a4%2B-6ac95d4/bm-20250116-linux-x86_64-faster%252dcpython-no_conditional_stack-3.14.0a4%2B-6ac95d4-vs-base.svg)[🧠](results/bm-20250116-3.14.0a4%2B-6ac95d4/bm-20250116-linux-x86_64-faster%252dcpython-no_conditional_stack-3.14.0a4%2B-6ac95d4-vs-base-mem.svg) |
| [2025-01-15](results/bm-20250115-3.14.0a4%2B-5501f0a-JIT) | brandtbucher/tier_two_refcounts | 5501f0a (JIT) | 1.426x ↑<br>[📄](results/bm-20250115-3.14.0a4%2B-5501f0a-JIT/bm-20250115-linux-x86_64-brandtbucher-tier_two_refcounts-3.14.0a4%2B-5501f0a-vs-3.10.4.md)[📈](results/bm-20250115-3.14.0a4%2B-5501f0a-JIT/bm-20250115-linux-x86_64-brandtbucher-tier_two_refcounts-3.14.0a4%2B-5501f0a-vs-3.10.4.svg) | 1.101x ↑<br>[📄](results/bm-20250115-3.14.0a4%2B-5501f0a-JIT/bm-20250115-linux-x86_64-brandtbucher-tier_two_refcounts-3.14.0a4%2B-5501f0a-vs-3.12.0.md)[📈](results/bm-20250115-3.14.0a4%2B-5501f0a-JIT/bm-20250115-linux-x86_64-brandtbucher-tier_two_refcounts-3.14.0a4%2B-5501f0a-vs-3.12.0.svg) | 1.030x ↑<br>[📄](results/bm-20250115-3.14.0a4%2B-5501f0a-JIT/bm-20250115-linux-x86_64-brandtbucher-tier_two_refcounts-3.14.0a4%2B-5501f0a-vs-3.13.0.md)[📈](results/bm-20250115-3.14.0a4%2B-5501f0a-JIT/bm-20250115-linux-x86_64-brandtbucher-tier_two_refcounts-3.14.0a4%2B-5501f0a-vs-3.13.0.svg) | 1.004x ↓<br>[📄](results/bm-20250115-3.14.0a4%2B-5501f0a-JIT/bm-20250115-linux-x86_64-brandtbucher-tier_two_refcounts-3.14.0a4%2B-5501f0a-vs-base.md)[📈](results/bm-20250115-3.14.0a4%2B-5501f0a-JIT/bm-20250115-linux-x86_64-brandtbucher-tier_two_refcounts-3.14.0a4%2B-5501f0a-vs-base.svg)[🧠](results/bm-20250115-3.14.0a4%2B-5501f0a-JIT/bm-20250115-linux-x86_64-brandtbucher-tier_two_refcounts-3.14.0a4%2B-5501f0a-vs-base-mem.svg) |
| [2025-01-15](results/bm-20250115-3.14.0a4%2B-6daa4a6-JIT) | brandtbucher/justin_binary_op_swa | 6daa4a6 (JIT) | 1.426x ↑<br>[📄](results/bm-20250115-3.14.0a4%2B-6daa4a6-JIT/bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4%2B-6daa4a6-vs-3.10.4.md)[📈](results/bm-20250115-3.14.0a4%2B-6daa4a6-JIT/bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4%2B-6daa4a6-vs-3.10.4.svg) | 1.102x ↑<br>[📄](results/bm-20250115-3.14.0a4%2B-6daa4a6-JIT/bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4%2B-6daa4a6-vs-3.12.0.md)[📈](results/bm-20250115-3.14.0a4%2B-6daa4a6-JIT/bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4%2B-6daa4a6-vs-3.12.0.svg) | 1.031x ↑<br>[📄](results/bm-20250115-3.14.0a4%2B-6daa4a6-JIT/bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4%2B-6daa4a6-vs-3.13.0.md)[📈](results/bm-20250115-3.14.0a4%2B-6daa4a6-JIT/bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4%2B-6daa4a6-vs-3.13.0.svg) | 1.004x ↓<br>[📄](results/bm-20250115-3.14.0a4%2B-6daa4a6-JIT/bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4%2B-6daa4a6-vs-base.md)[📈](results/bm-20250115-3.14.0a4%2B-6daa4a6-JIT/bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4%2B-6daa4a6-vs-base.svg)[🧠](results/bm-20250115-3.14.0a4%2B-6daa4a6-JIT/bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4%2B-6daa4a6-vs-base-mem.svg) |

## linux x86_64 (pythonperf2)
| date | fork/ref | hash/flags | vs. 3.10.4: | vs. 3.12.0: | vs. 3.13.0: | vs. base: |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| [2025-01-18](results/bm-20250118-3.14.0a4%2B-61b35f7-NOGIL) | python/61b35f74aa4a6ac60663 | 61b35f7 (NOGIL) | 1.188x ↑<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7-NOGIL/bm-20250118-pythonperf2-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.10.4.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7-NOGIL/bm-20250118-pythonperf2-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.10.4.svg) | 1.069x ↓<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7-NOGIL/bm-20250118-pythonperf2-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.12.0.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7-NOGIL/bm-20250118-pythonperf2-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.12.0.svg) | 1.060x ↓<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7-NOGIL/bm-20250118-pythonperf2-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.13.0.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7-NOGIL/bm-20250118-pythonperf2-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.13.0.svg) | 1.120x ↓<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7-NOGIL/bm-20250118-pythonperf2-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-base.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7-NOGIL/bm-20250118-pythonperf2-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-base.svg)[🧠](results/bm-20250118-3.14.0a4%2B-61b35f7-NOGIL/bm-20250118-pythonperf2-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-base-mem.svg) |
| [2025-01-18](results/bm-20250118-3.14.0a4%2B-61b35f7) | python/61b35f74aa4a6ac60663 | 61b35f7 | 1.361x ↑<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7/bm-20250118-pythonperf2-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.10.4.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7/bm-20250118-pythonperf2-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.10.4.svg) | 1.056x ↑<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7/bm-20250118-pythonperf2-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.12.0.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7/bm-20250118-pythonperf2-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.12.0.svg) | 1.068x ↑<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7/bm-20250118-pythonperf2-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.13.0.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7/bm-20250118-pythonperf2-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.13.0.svg) |  |
| [2025-01-18](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT) | python/61b35f74aa4a6ac60663 | 61b35f7 (JIT) | 1.312x ↑<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-pythonperf2-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.10.4.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-pythonperf2-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.10.4.svg) | 1.021x ↑<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-pythonperf2-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.12.0.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-pythonperf2-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.12.0.svg) | 1.032x ↑<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-pythonperf2-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.13.0.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-pythonperf2-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.13.0.svg) | 1.033x ↓<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-pythonperf2-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-base.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-pythonperf2-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-base.svg)[🧠](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-pythonperf2-x86_64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-base-mem.svg) |
| [2025-01-16](results/bm-20250116-3.14.0a4%2B-df5d01c-CLANG) | Fidget-Spinner/tail_call | df5d01c (CLANG) | 1.397x ↑<br>[📄](results/bm-20250116-3.14.0a4%2B-df5d01c-CLANG/bm-20250116-pythonperf2-x86_64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-3.10.4.md)[📈](results/bm-20250116-3.14.0a4%2B-df5d01c-CLANG/bm-20250116-pythonperf2-x86_64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-3.10.4.svg) | 1.082x ↑<br>[📄](results/bm-20250116-3.14.0a4%2B-df5d01c-CLANG/bm-20250116-pythonperf2-x86_64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-3.12.0.md)[📈](results/bm-20250116-3.14.0a4%2B-df5d01c-CLANG/bm-20250116-pythonperf2-x86_64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-3.12.0.svg) | 1.093x ↑<br>[📄](results/bm-20250116-3.14.0a4%2B-df5d01c-CLANG/bm-20250116-pythonperf2-x86_64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-3.13.0.md)[📈](results/bm-20250116-3.14.0a4%2B-df5d01c-CLANG/bm-20250116-pythonperf2-x86_64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-3.13.0.svg) | 1.062x ↑<br>[📄](results/bm-20250116-3.14.0a4%2B-df5d01c-CLANG/bm-20250116-pythonperf2-x86_64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-base.md)[📈](results/bm-20250116-3.14.0a4%2B-df5d01c-CLANG/bm-20250116-pythonperf2-x86_64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-base.svg)[🧠](results/bm-20250116-3.14.0a4%2B-df5d01c-CLANG/bm-20250116-pythonperf2-x86_64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-base-mem.svg) |
| [2025-01-16](results/bm-20250116-3.14.0a4%2B-09f3d0f-CLANG) | mdboom/tail_call_no_preserv | 09f3d0f (CLANG) | 1.350x ↑<br>[📄](results/bm-20250116-3.14.0a4%2B-09f3d0f-CLANG/bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4%2B-09f3d0f-vs-3.10.4.md)[📈](results/bm-20250116-3.14.0a4%2B-09f3d0f-CLANG/bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4%2B-09f3d0f-vs-3.10.4.svg) | 1.046x ↑<br>[📄](results/bm-20250116-3.14.0a4%2B-09f3d0f-CLANG/bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4%2B-09f3d0f-vs-3.12.0.md)[📈](results/bm-20250116-3.14.0a4%2B-09f3d0f-CLANG/bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4%2B-09f3d0f-vs-3.12.0.svg) | 1.059x ↑<br>[📄](results/bm-20250116-3.14.0a4%2B-09f3d0f-CLANG/bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4%2B-09f3d0f-vs-3.13.0.md)[📈](results/bm-20250116-3.14.0a4%2B-09f3d0f-CLANG/bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4%2B-09f3d0f-vs-3.13.0.svg) | 1.029x ↑<br>[📄](results/bm-20250116-3.14.0a4%2B-09f3d0f-CLANG/bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4%2B-09f3d0f-vs-base.md)[📈](results/bm-20250116-3.14.0a4%2B-09f3d0f-CLANG/bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4%2B-09f3d0f-vs-base.svg)[🧠](results/bm-20250116-3.14.0a4%2B-09f3d0f-CLANG/bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4%2B-09f3d0f-vs-base-mem.svg) |
| [2025-01-16](results/bm-20250116-3.14.0a4%2B-313b96e-CLANG) | python/313b96eb8b8d0ad3bac5 | 313b96e (CLANG) | 1.308x ↑<br>[📄](results/bm-20250116-3.14.0a4%2B-313b96e-CLANG/bm-20250116-pythonperf2-x86_64-python-313b96eb8b8d0ad3bac5-3.14.0a4%2B-313b96e-vs-3.10.4.md)[📈](results/bm-20250116-3.14.0a4%2B-313b96e-CLANG/bm-20250116-pythonperf2-x86_64-python-313b96eb8b8d0ad3bac5-3.14.0a4%2B-313b96e-vs-3.10.4.svg) | 1.014x ↑<br>[📄](results/bm-20250116-3.14.0a4%2B-313b96e-CLANG/bm-20250116-pythonperf2-x86_64-python-313b96eb8b8d0ad3bac5-3.14.0a4%2B-313b96e-vs-3.12.0.md)[📈](results/bm-20250116-3.14.0a4%2B-313b96e-CLANG/bm-20250116-pythonperf2-x86_64-python-313b96eb8b8d0ad3bac5-3.14.0a4%2B-313b96e-vs-3.12.0.svg) | 1.030x ↑<br>[📄](results/bm-20250116-3.14.0a4%2B-313b96e-CLANG/bm-20250116-pythonperf2-x86_64-python-313b96eb8b8d0ad3bac5-3.14.0a4%2B-313b96e-vs-3.13.0.md)[📈](results/bm-20250116-3.14.0a4%2B-313b96e-CLANG/bm-20250116-pythonperf2-x86_64-python-313b96eb8b8d0ad3bac5-3.14.0a4%2B-313b96e-vs-3.13.0.svg) |  |

## windows amd64 (pythonperf1)
| date | fork/ref | hash/flags | vs. 3.10.4: | vs. 3.12.0: | vs. 3.13.0: | vs. base: |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| [2025-01-18](results/bm-20250118-3.14.0a4%2B-61b35f7) | python/61b35f74aa4a6ac60663 | 61b35f7 | 1.146x ↑<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7/bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.10.4.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7/bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.10.4.svg) | 1.028x ↓<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7/bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.12.0.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7/bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.12.0.svg) | 1.054x ↓<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7/bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.13.0.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7/bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.13.0.svg) |  |
| [2025-01-18](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT) | python/61b35f74aa4a6ac60663 | 61b35f7 (JIT) | 1.236x ↑<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.10.4.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.10.4.svg) | 1.056x ↑<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.12.0.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.12.0.svg) | 1.017x ↑<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.13.0.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.13.0.svg) | 1.075x ↑<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-base.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-base.svg) |
| [2025-01-11](results/bm-20250111-3.14.0a3%2B-22a4421) | python/22a442181d5f1ac496da | 22a4421 | 1.221x ↑<br>[📄](results/bm-20250111-3.14.0a3%2B-22a4421/bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.10.4.md)[📈](results/bm-20250111-3.14.0a3%2B-22a4421/bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.10.4.svg) | 1.035x ↑<br>[📄](results/bm-20250111-3.14.0a3%2B-22a4421/bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.12.0.md)[📈](results/bm-20250111-3.14.0a3%2B-22a4421/bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.12.0.svg) | 1.004x ↑<br>[📄](results/bm-20250111-3.14.0a3%2B-22a4421/bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.13.0.md)[📈](results/bm-20250111-3.14.0a3%2B-22a4421/bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.13.0.svg) |  |

## windows x86 (pythonperf1_win32)
| date | fork/ref | hash/flags | vs. 3.10.4: | vs. 3.12.0: | vs. 3.13.0: | vs. base: |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| [2025-01-18](results/bm-20250118-3.14.0a4%2B-61b35f7) | python/61b35f74aa4a6ac60663 | 61b35f7 | 1.025x ↑<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7/bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.10.4.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7/bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.10.4.svg) | 1.037x ↑<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7/bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.12.0.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7/bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.12.0.svg) | 1.079x ↓<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7/bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.13.0.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7/bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.13.0.svg) |  |
| [2025-01-18](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT) | python/61b35f74aa4a6ac60663 | 61b35f7 (JIT) | 1.008x ↓<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.10.4.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.10.4.svg) | 1.008x ↑<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.12.0.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.12.0.svg) | 1.107x ↓<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.13.0.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.13.0.svg) | 1.030x ↓<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-base.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-base.svg) |
| [2025-01-11](results/bm-20250111-3.14.0a3%2B-22a4421) | python/22a442181d5f1ac496da | 22a4421 | 1.156x ↑<br>[📄](results/bm-20250111-3.14.0a3%2B-22a4421/bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.10.4.md)[📈](results/bm-20250111-3.14.0a3%2B-22a4421/bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.10.4.svg) | 1.166x ↑<br>[📄](results/bm-20250111-3.14.0a3%2B-22a4421/bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.12.0.md)[📈](results/bm-20250111-3.14.0a3%2B-22a4421/bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.12.0.svg) | 1.037x ↑<br>[📄](results/bm-20250111-3.14.0a3%2B-22a4421/bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.13.0.md)[📈](results/bm-20250111-3.14.0a3%2B-22a4421/bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.13.0.svg) |  |

## darwin arm64 (darwin)
| date | fork/ref | hash/flags | vs. 3.10.4: | vs. 3.12.0: | vs. 3.13.0: | vs. base: |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| [2025-01-18](results/bm-20250118-3.14.0a4%2B-61b35f7-NOGIL) | python/61b35f74aa4a6ac60663 | 61b35f7 (NOGIL) | 1.296x ↑<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7-NOGIL/bm-20250118-darwin-arm64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.10.4.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7-NOGIL/bm-20250118-darwin-arm64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.10.4.svg) | 1.042x ↑<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7-NOGIL/bm-20250118-darwin-arm64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.12.0.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7-NOGIL/bm-20250118-darwin-arm64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.12.0.svg) | 1.045x ↑<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7-NOGIL/bm-20250118-darwin-arm64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.13.0.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7-NOGIL/bm-20250118-darwin-arm64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.13.0.svg) | 1.071x ↓<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7-NOGIL/bm-20250118-darwin-arm64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-base.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7-NOGIL/bm-20250118-darwin-arm64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-base.svg)[🧠](results/bm-20250118-3.14.0a4%2B-61b35f7-NOGIL/bm-20250118-darwin-arm64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-base-mem.svg) |
| [2025-01-18](results/bm-20250118-3.14.0a4%2B-61b35f7) | python/61b35f74aa4a6ac60663 | 61b35f7 | 1.404x ↑<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7/bm-20250118-darwin-arm64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.10.4.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7/bm-20250118-darwin-arm64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.10.4.svg) | 1.120x ↑<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7/bm-20250118-darwin-arm64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.12.0.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7/bm-20250118-darwin-arm64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.12.0.svg) | 1.124x ↑<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7/bm-20250118-darwin-arm64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.13.0.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7/bm-20250118-darwin-arm64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.13.0.svg) |  |
| [2025-01-18](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT) | python/61b35f74aa4a6ac60663 | 61b35f7 (JIT) | 1.342x ↑<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-darwin-arm64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.10.4.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-darwin-arm64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.10.4.svg) | 1.073x ↑<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-darwin-arm64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.12.0.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-darwin-arm64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.12.0.svg) | 1.077x ↑<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-darwin-arm64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.13.0.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-darwin-arm64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-3.13.0.svg) | 1.041x ↓<br>[📄](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-darwin-arm64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-base.md)[📈](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-darwin-arm64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-base.svg)[🧠](results/bm-20250118-3.14.0a4%2B-61b35f7-JIT/bm-20250118-darwin-arm64-python-61b35f74aa4a6ac60663-3.14.0a4%2B-61b35f7-vs-base-mem.svg) |
| [2025-01-16](results/bm-20250116-3.14.0a4%2B-df5d01c-CLANG) | Fidget-Spinner/tail_call | df5d01c (CLANG) | 1.466x ↑<br>[📄](results/bm-20250116-3.14.0a4%2B-df5d01c-CLANG/bm-20250116-darwin-arm64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-3.10.4.md)[📈](results/bm-20250116-3.14.0a4%2B-df5d01c-CLANG/bm-20250116-darwin-arm64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-3.10.4.svg) | 1.170x ↑<br>[📄](results/bm-20250116-3.14.0a4%2B-df5d01c-CLANG/bm-20250116-darwin-arm64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-3.12.0.md)[📈](results/bm-20250116-3.14.0a4%2B-df5d01c-CLANG/bm-20250116-darwin-arm64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-3.12.0.svg) | 1.173x ↑<br>[📄](results/bm-20250116-3.14.0a4%2B-df5d01c-CLANG/bm-20250116-darwin-arm64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-3.13.0.md)[📈](results/bm-20250116-3.14.0a4%2B-df5d01c-CLANG/bm-20250116-darwin-arm64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-3.13.0.svg) | 1.117x ↑<br>[📄](results/bm-20250116-3.14.0a4%2B-df5d01c-CLANG/bm-20250116-darwin-arm64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-base.md)[📈](results/bm-20250116-3.14.0a4%2B-df5d01c-CLANG/bm-20250116-darwin-arm64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-base.svg)[🧠](results/bm-20250116-3.14.0a4%2B-df5d01c-CLANG/bm-20250116-darwin-arm64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-base-mem.svg) |
| [2025-01-16](results/bm-20250116-3.14.0a4%2B-313b96e-CLANG) | python/313b96eb8b8d0ad3bac5 | 313b96e (CLANG) | 1.310x ↑<br>[📄](results/bm-20250116-3.14.0a4%2B-313b96e-CLANG/bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4%2B-313b96e-vs-3.10.4.md)[📈](results/bm-20250116-3.14.0a4%2B-313b96e-CLANG/bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4%2B-313b96e-vs-3.10.4.svg) | 1.048x ↑<br>[📄](results/bm-20250116-3.14.0a4%2B-313b96e-CLANG/bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4%2B-313b96e-vs-3.12.0.md)[📈](results/bm-20250116-3.14.0a4%2B-313b96e-CLANG/bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4%2B-313b96e-vs-3.12.0.svg) | 1.051x ↑<br>[📄](results/bm-20250116-3.14.0a4%2B-313b96e-CLANG/bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4%2B-313b96e-vs-3.13.0.md)[📈](results/bm-20250116-3.14.0a4%2B-313b96e-CLANG/bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4%2B-313b96e-vs-3.13.0.svg) |  |


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

Information about the configuration of the run is in the `README.md` at the root
of each run directory. The directory name will also include `PYTHON_UOPS` for
Tier 2 and `JIT` for JIT.

To reduce the number of unknown variables when comparing results, runs are
always compared against runs of the same configuration. Be aware that sometimes
the base commit on main may predate the configuration becoming available, for
example, before the JIT compiler was merged into main. (An exception to this
rule are the weekly benchmarks of upstream main, there Tier 2 and JIT
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
- We also use the Hierarchical Performance Testing (HPT) method (see below) to
  statistically reduce the effect of benchmarks that have more variability. This
  is a different method than the simple geometric mean that `pyperf` uses by
  default. We provide both numbers in our results.

#### pystats

`pystats` are a set of counters in CPython that measure things like the number
of times each bytecode instruction is executed. (Detailed documentation of all
of the counters should be added to CPython in the future).

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
