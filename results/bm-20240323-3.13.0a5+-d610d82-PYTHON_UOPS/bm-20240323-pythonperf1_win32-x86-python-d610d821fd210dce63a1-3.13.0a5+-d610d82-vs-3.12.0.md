# Results vs. 3.12.0

- fork: python
- ref: d610d821fd210dce63a1
- machine: windows-x86
- commit hash: d610d82
- commit date: 2024-03-23
- overall geometric mean: 1.17x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 241 ms: 1.16x faster                                                            |
| chameleon      | 7.75 ms                                                         | 5.93 ms: 1.31x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.88 sec: 1.06x faster                                                          |
| tornado_http   | 105 ms                                                          | 97.5 ms: 1.08x faster                                                           |
| Geometric mean | (ref)                                                           | 1.15x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 252 ms: 1.39x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 488 ms: 1.39x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 201 ms: 1.38x faster                                                            |
| async_tree_none            | 298 ms                                                          | 221 ms: 1.35x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 272 ms: 1.34x faster                                                            |
| async_tree_io              | 693 ms                                                          | 522 ms: 1.33x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 468 ms: 1.20x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 455 ms: 1.20x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.32x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 76.4 ms: 1.66x faster                                                           |
| float          | 76.7 ms                                                         | 53.8 ms: 1.42x faster                                                           |
| pidigits       | 199 ms                                                          | 199 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                           | 1.33x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 117 ms: 1.11x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.94 ms: 1.05x faster                                                           |
| regex_dna      | 127 ms                                                          | 126 ms: 1.01x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 16.1 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.59 sec: 1.38x faster                                                          |
| pickle_pure_python   | 286 us                                                          | 211 us: 1.36x faster                                                            |
| unpickle_pure_python | 210 us                                                          | 161 us: 1.30x faster                                                            |
| xml_etree_process    | 53.2 ms                                                         | 41.4 ms: 1.29x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 59.1 ms: 1.22x faster                                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 65.7 ms: 1.18x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 6.85 ms: 1.08x faster                                                           |
| unpickle_list        | 2.95 us                                                         | 2.76 us: 1.07x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 107 ms: 1.05x faster                                                            |
| pickle_list          | 3.37 us                                                         | 3.30 us: 1.02x faster                                                           |
| pickle               | 7.79 us                                                         | 7.73 us: 1.01x faster                                                           |
| unpickle             | 9.71 us                                                         | 9.99 us: 1.03x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.13x faster                                                                    |

Benchmark hidden because not significant (2): pickle_dict, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 22.4 ms                                                         | 22.5 ms: 1.01x slower                                                           |
| python_startup_no_site | 19.1 ms                                                         | 20.2 ms: 1.06x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.03x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 6.85 ms: 1.45x faster                                                           |
| django_template | 36.9 ms                                                         | 30.3 ms: 1.22x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.33x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| generators                 | 38.5 ms                                                         | 23.0 ms: 1.68x faster                                                           |
| logging_silent             | 101 ns                                                          | 60.8 ns: 1.66x faster                                                           |
| nbody                      | 127 ms                                                          | 76.4 ms: 1.66x faster                                                           |
| deepcopy_memo              | 38.4 us                                                         | 24.4 us: 1.58x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.30 ms: 1.56x faster                                                           |
| unpack_sequence            | 62.5 ns                                                         | 41.6 ns: 1.50x faster                                                           |
| comprehensions             | 19.2 us                                                         | 12.9 us: 1.49x faster                                                           |
| mako                       | 9.96 ms                                                         | 6.85 ms: 1.45x faster                                                           |
| spectral_norm              | 104 ms                                                          | 72.3 ms: 1.44x faster                                                           |
| float                      | 76.7 ms                                                         | 53.8 ms: 1.42x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 14.7 ms: 1.42x faster                                                           |
| raytrace                   | 308 ms                                                          | 217 ms: 1.42x faster                                                            |
| scimark_sor                | 130 ms                                                          | 91.6 ms: 1.42x faster                                                           |
| richards_super             | 46.5 ms                                                         | 32.8 ms: 1.42x faster                                                           |
| richards                   | 41.3 ms                                                         | 29.2 ms: 1.41x faster                                                           |
| typing_runtime_protocols   | 126 us                                                          | 89.5 us: 1.41x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 252 ms: 1.39x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 488 ms: 1.39x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 47.9 ms: 1.39x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 201 ms: 1.38x faster                                                            |
| tomli_loads                | 2.20 sec                                                        | 1.59 sec: 1.38x faster                                                          |
| pickle_pure_python         | 286 us                                                          | 211 us: 1.36x faster                                                            |
| fannkuch                   | 354 ms                                                          | 261 ms: 1.35x faster                                                            |
| async_tree_none            | 298 ms                                                          | 221 ms: 1.35x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 272 ms: 1.34x faster                                                            |
| chaos                      | 69.4 ms                                                         | 51.9 ms: 1.34x faster                                                           |
| async_tree_io              | 693 ms                                                          | 522 ms: 1.33x faster                                                            |
| sqlglot_parse              | 1.25 ms                                                         | 942 us: 1.32x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 2.44 us: 1.32x faster                                                           |
| scimark_fft                | 271 ms                                                          | 205 ms: 1.32x faster                                                            |
| deepcopy                   | 360 us                                                          | 275 us: 1.31x faster                                                            |
| chameleon                  | 7.75 ms                                                         | 5.93 ms: 1.31x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 161 us: 1.30x faster                                                            |
| hexiom                     | 6.82 ms                                                         | 5.25 ms: 1.30x faster                                                           |
| pyflate                    | 424 ms                                                          | 329 ms: 1.29x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 41.4 ms: 1.29x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.01 ms: 1.28x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 54.0 ms: 1.28x faster                                                           |
| sqlglot_transpile          | 1.53 ms                                                         | 1.20 ms: 1.28x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.18 sec: 1.27x faster                                                          |
| pprint_safe_repr           | 721 ms                                                          | 574 ms: 1.26x faster                                                            |
| logging_simple             | 9.75 us                                                         | 7.88 us: 1.24x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 76.0 ms: 1.23x faster                                                           |
| logging_format             | 10.4 us                                                         | 8.47 us: 1.23x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 59.1 ms: 1.22x faster                                                           |
| go                         | 137 ms                                                          | 113 ms: 1.22x faster                                                            |
| django_template            | 36.9 ms                                                         | 30.3 ms: 1.22x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 468 ms: 1.20x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 455 ms: 1.20x faster                                                            |
| mdp                        | 1.91 sec                                                        | 1.61 sec: 1.19x faster                                                          |
| xml_etree_iterparse        | 77.6 ms                                                         | 65.7 ms: 1.18x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 79.6 ms: 1.17x faster                                                           |
| pycparser                  | 978 ms                                                          | 838 ms: 1.17x faster                                                            |
| 2to3                       | 280 ms                                                          | 241 ms: 1.16x faster                                                            |
| async_generators           | 313 ms                                                          | 270 ms: 1.16x faster                                                            |
| sqlglot_optimize           | 48.5 ms                                                         | 42.0 ms: 1.15x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 15.2 ms: 1.15x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 108 ms: 1.14x faster                                                            |
| meteor_contest             | 86.9 ms                                                         | 76.5 ms: 1.14x faster                                                           |
| sympy_str                  | 240 ms                                                          | 213 ms: 1.12x faster                                                            |
| regex_compile              | 129 ms                                                          | 117 ms: 1.11x faster                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 69.5 ms: 1.09x faster                                                           |
| json_dumps                 | 7.40 ms                                                         | 6.85 ms: 1.08x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.02 ms: 1.08x faster                                                           |
| tornado_http               | 105 ms                                                          | 97.5 ms: 1.08x faster                                                           |
| asyncio_tcp                | 662 ms                                                          | 617 ms: 1.07x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.93 us: 1.07x faster                                                           |
| unpickle_list              | 2.95 us                                                         | 2.76 us: 1.07x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 86.0 ms: 1.06x faster                                                           |
| docutils                   | 1.98 sec                                                        | 1.88 sec: 1.06x faster                                                          |
| sympy_expand               | 398 ms                                                          | 377 ms: 1.06x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 107 ms: 1.05x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.94 ms: 1.05x faster                                                           |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.8 sec: 1.05x faster                                                          |
| gc_traversal               | 1.44 ms                                                         | 1.38 ms: 1.04x faster                                                           |
| pickle_list                | 3.37 us                                                         | 3.30 us: 1.02x faster                                                           |
| regex_dna                  | 127 ms                                                          | 126 ms: 1.01x faster                                                            |
| pickle                     | 7.79 us                                                         | 7.73 us: 1.01x faster                                                           |
| pidigits                   | 199 ms                                                          | 199 ms: 1.00x faster                                                            |
| python_startup             | 22.4 ms                                                         | 22.5 ms: 1.01x slower                                                           |
| unpickle                   | 9.71 us                                                         | 9.99 us: 1.03x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 20.2 ms: 1.06x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 16.1 ms: 1.07x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.03 ms: 1.09x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 215 ms: 2.14x slower                                                            |
| coverage                   | 48.4 ms                                                         | 469 ms: 9.69x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.17x faster                                                                    |

Benchmark hidden because not significant (4): pickle_dict, create_gc_cycles, json_loads, json
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240323-3.13.0a5+-d610d82-PYTHON_UOPS/bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json: genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.15x


# Memory

- memory change: unknown