# Results vs. 3.12.0

- fork: python
- ref: d610d821fd210dce63a1
- machine: windows-x86
- commit hash: d610d82
- commit date: 2024-03-23
- overall geometric mean: 1.22x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 228 ms: 1.23x faster                                                            |
| chameleon      | 7.75 ms                                                         | 5.65 ms: 1.37x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.75 sec: 1.14x faster                                                          |
| tornado_http   | 105 ms                                                          | 93.9 ms: 1.12x faster                                                           |
| Geometric mean | (ref)                                                           | 1.21x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 250 ms: 1.40x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 198 ms: 1.40x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 489 ms: 1.38x faster                                                            |
| async_tree_none            | 298 ms                                                          | 215 ms: 1.38x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 265 ms: 1.37x faster                                                            |
| async_tree_io              | 693 ms                                                          | 520 ms: 1.33x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 461 ms: 1.22x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 458 ms: 1.19x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.33x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 77.3 ms: 1.64x faster                                                           |
| float          | 76.7 ms                                                         | 51.5 ms: 1.49x faster                                                           |
| pidigits       | 199 ms                                                          | 197 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                           | 1.35x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 94.4 ms: 1.37x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.90 ms: 1.07x faster                                                           |
| regex_dna      | 127 ms                                                          | 118 ms: 1.07x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 15.8 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                           | 1.11x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 139 us: 1.51x faster                                                            |
| tomli_loads          | 2.20 sec                                                        | 1.60 sec: 1.37x faster                                                          |
| pickle_pure_python   | 286 us                                                          | 211 us: 1.36x faster                                                            |
| xml_etree_process    | 53.2 ms                                                         | 40.8 ms: 1.31x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 59.1 ms: 1.22x faster                                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 64.7 ms: 1.20x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 6.60 ms: 1.12x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 107 ms: 1.05x faster                                                            |
| unpickle_list        | 2.95 us                                                         | 2.81 us: 1.05x faster                                                           |
| json_loads           | 20.4 us                                                         | 20.0 us: 1.02x faster                                                           |
| pickle_list          | 3.37 us                                                         | 3.34 us: 1.01x faster                                                           |
| unpickle             | 9.71 us                                                         | 9.75 us: 1.00x slower                                                           |
| pickle               | 7.79 us                                                         | 7.85 us: 1.01x slower                                                           |
| pickle_dict          | 19.9 us                                                         | 20.2 us: 1.01x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.14x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.7 ms: 1.03x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 6.83 ms: 1.46x faster                                                           |
| django_template | 36.9 ms                                                         | 28.6 ms: 1.29x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.37x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| logging_silent             | 101 ns                                                          | 57.3 ns: 1.76x faster                                                           |
| generators                 | 38.5 ms                                                         | 22.3 ms: 1.72x faster                                                           |
| comprehensions             | 19.2 us                                                         | 11.4 us: 1.68x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.13 ms: 1.68x faster                                                           |
| deepcopy_memo              | 38.4 us                                                         | 23.0 us: 1.67x faster                                                           |
| nbody                      | 127 ms                                                          | 77.3 ms: 1.64x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 4.19 ms: 1.63x faster                                                           |
| unpack_sequence            | 62.5 ns                                                         | 39.3 ns: 1.59x faster                                                           |
| scimark_sor                | 130 ms                                                          | 82.2 ms: 1.58x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 59.8 ms: 1.56x faster                                                           |
| spectral_norm              | 104 ms                                                          | 66.6 ms: 1.56x faster                                                           |
| raytrace                   | 308 ms                                                          | 198 ms: 1.55x faster                                                            |
| unpickle_pure_python       | 210 us                                                          | 139 us: 1.51x faster                                                            |
| float                      | 76.7 ms                                                         | 51.5 ms: 1.49x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 45.4 ms: 1.46x faster                                                           |
| mako                       | 9.96 ms                                                         | 6.83 ms: 1.46x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 859 us: 1.45x faster                                                            |
| chaos                      | 69.4 ms                                                         | 48.0 ms: 1.45x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 14.6 ms: 1.43x faster                                                           |
| richards_super             | 46.5 ms                                                         | 32.4 ms: 1.43x faster                                                           |
| richards                   | 41.3 ms                                                         | 28.9 ms: 1.43x faster                                                           |
| sqlglot_transpile          | 1.53 ms                                                         | 1.08 ms: 1.41x faster                                                           |
| go                         | 137 ms                                                          | 97.5 ms: 1.41x faster                                                           |
| typing_runtime_protocols   | 126 us                                                          | 89.9 us: 1.40x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 250 ms: 1.40x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 198 ms: 1.40x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 489 ms: 1.38x faster                                                            |
| async_tree_none            | 298 ms                                                          | 215 ms: 1.38x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 2.35 us: 1.37x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 265 ms: 1.37x faster                                                            |
| chameleon                  | 7.75 ms                                                         | 5.65 ms: 1.37x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.60 sec: 1.37x faster                                                          |
| deepcopy                   | 360 us                                                          | 263 us: 1.37x faster                                                            |
| regex_compile              | 129 ms                                                          | 94.4 ms: 1.37x faster                                                           |
| pyflate                    | 424 ms                                                          | 312 ms: 1.36x faster                                                            |
| pickle_pure_python         | 286 us                                                          | 211 us: 1.36x faster                                                            |
| pprint_pformat             | 1.50 sec                                                        | 1.11 sec: 1.36x faster                                                          |
| scimark_fft                | 271 ms                                                          | 202 ms: 1.34x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 69.8 ms: 1.34x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.89 ms: 1.33x faster                                                           |
| pprint_safe_repr           | 721 ms                                                          | 540 ms: 1.33x faster                                                            |
| async_tree_io              | 693 ms                                                          | 520 ms: 1.33x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 52.1 ms: 1.33x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 40.8 ms: 1.31x faster                                                           |
| django_template            | 36.9 ms                                                         | 28.6 ms: 1.29x faster                                                           |
| fannkuch                   | 354 ms                                                          | 276 ms: 1.28x faster                                                            |
| logging_simple             | 9.75 us                                                         | 7.64 us: 1.28x faster                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 38.1 ms: 1.27x faster                                                           |
| pycparser                  | 978 ms                                                          | 776 ms: 1.26x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 13.9 ms: 1.26x faster                                                           |
| logging_format             | 10.4 us                                                         | 8.28 us: 1.26x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 98.9 ms: 1.24x faster                                                           |
| sympy_str                  | 240 ms                                                          | 194 ms: 1.23x faster                                                            |
| 2to3                       | 280 ms                                                          | 228 ms: 1.23x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 461 ms: 1.22x faster                                                            |
| mdp                        | 1.91 sec                                                        | 1.56 sec: 1.22x faster                                                          |
| xml_etree_generate         | 72.1 ms                                                         | 59.1 ms: 1.22x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 64.7 ms: 1.20x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 458 ms: 1.19x faster                                                            |
| async_generators           | 313 ms                                                          | 267 ms: 1.17x faster                                                            |
| sympy_expand               | 398 ms                                                          | 342 ms: 1.16x faster                                                            |
| meteor_contest             | 86.9 ms                                                         | 75.1 ms: 1.16x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 963 us: 1.14x faster                                                            |
| docutils                   | 1.98 sec                                                        | 1.75 sec: 1.14x faster                                                          |
| json_dumps                 | 7.40 ms                                                         | 6.60 ms: 1.12x faster                                                           |
| tornado_http               | 105 ms                                                          | 93.9 ms: 1.12x faster                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 68.1 ms: 1.11x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.92 us: 1.08x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.90 ms: 1.07x faster                                                           |
| regex_dna                  | 127 ms                                                          | 118 ms: 1.07x faster                                                            |
| pathlib                    | 91.4 ms                                                         | 86.3 ms: 1.06x faster                                                           |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.7 sec: 1.06x faster                                                          |
| xml_etree_parse            | 113 ms                                                          | 107 ms: 1.05x faster                                                            |
| asyncio_tcp                | 662 ms                                                          | 629 ms: 1.05x faster                                                            |
| unpickle_list              | 2.95 us                                                         | 2.81 us: 1.05x faster                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.40 ms: 1.03x faster                                                           |
| json_loads                 | 20.4 us                                                         | 20.0 us: 1.02x faster                                                           |
| pidigits                   | 199 ms                                                          | 197 ms: 1.01x faster                                                            |
| pickle_list                | 3.37 us                                                         | 3.34 us: 1.01x faster                                                           |
| unpickle                   | 9.71 us                                                         | 9.75 us: 1.00x slower                                                           |
| pickle                     | 7.79 us                                                         | 7.85 us: 1.01x slower                                                           |
| pickle_dict                | 19.9 us                                                         | 20.2 us: 1.01x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 19.7 ms: 1.03x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 15.8 ms: 1.05x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.17 ms: 1.12x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 196 ms: 1.95x slower                                                            |
| coverage                   | 48.4 ms                                                         | 476 ms: 9.82x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.22x faster                                                                    |

Benchmark hidden because not significant (3): create_gc_cycles, python_startup, json
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240323-3.13.0a5+-d610d82/bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json: genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.21x


# Memory

- memory change: unknown