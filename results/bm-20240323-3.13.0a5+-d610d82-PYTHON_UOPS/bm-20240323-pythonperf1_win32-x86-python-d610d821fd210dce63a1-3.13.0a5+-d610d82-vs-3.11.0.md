# Results vs. 3.11.0

- fork: python
- ref: d610d821fd210dce63a1
- machine: windows-x86
- commit hash: d610d82
- commit date: 2024-03-23
- overall geometric mean: 1.24x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 282 ms                                                          | 241 ms: 1.17x faster                                                            |
| chameleon      | 8.08 ms                                                         | 5.93 ms: 1.36x faster                                                           |
| docutils       | 2.10 sec                                                        | 1.88 sec: 1.12x faster                                                          |
| html5lib       | 54.3 ms                                                         | 47.0 ms: 1.16x faster                                                           |
| tornado_http   | 118 ms                                                          | 97.5 ms: 1.21x faster                                                           |
| Geometric mean | (ref)                                                           | 1.20x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none            | 343 ms                                                          | 221 ms: 1.55x faster                                                            |
| async_tree_io_tg           | 746 ms                                                          | 488 ms: 1.53x faster                                                            |
| async_tree_memoization     | 408 ms                                                          | 272 ms: 1.50x faster                                                            |
| async_tree_none_tg         | 301 ms                                                          | 201 ms: 1.50x faster                                                            |
| async_tree_memoization_tg  | 378 ms                                                          | 252 ms: 1.50x faster                                                            |
| async_tree_io              | 754 ms                                                          | 522 ms: 1.44x faster                                                            |
| async_tree_cpu_io_mixed_tg | 577 ms                                                          | 455 ms: 1.27x faster                                                            |
| async_tree_cpu_io_mixed    | 590 ms                                                          | 468 ms: 1.26x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.44x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 126 ms                                                          | 76.4 ms: 1.65x faster                                                           |
| float          | 76.1 ms                                                         | 53.8 ms: 1.41x faster                                                           |
| pidigits       | 203 ms                                                          | 199 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                           | 1.33x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                          | 117 ms: 1.27x faster                                                            |
| regex_dna      | 122 ms                                                          | 126 ms: 1.03x slower                                                            |
| regex_v8       | 15.2 ms                                                         | 16.1 ms: 1.06x slower                                                           |
| regex_effbot   | 1.82 ms                                                         | 1.94 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 309 us                                                          | 211 us: 1.47x faster                                                            |
| tomli_loads          | 2.31 sec                                                        | 1.59 sec: 1.45x faster                                                          |
| unpickle_pure_python | 231 us                                                          | 161 us: 1.43x faster                                                            |
| json_dumps           | 9.80 ms                                                         | 6.85 ms: 1.43x faster                                                           |
| xml_etree_process    | 55.0 ms                                                         | 41.4 ms: 1.33x faster                                                           |
| xml_etree_generate   | 71.6 ms                                                         | 59.1 ms: 1.21x faster                                                           |
| unpickle_list        | 3.28 us                                                         | 2.76 us: 1.19x faster                                                           |
| xml_etree_iterparse  | 75.6 ms                                                         | 65.7 ms: 1.15x faster                                                           |
| xml_etree_parse      | 114 ms                                                          | 107 ms: 1.06x faster                                                            |
| pickle               | 7.99 us                                                         | 7.73 us: 1.03x faster                                                           |
| pickle_dict          | 20.1 us                                                         | 19.9 us: 1.01x faster                                                           |
| json_loads           | 20.0 us                                                         | 20.4 us: 1.02x slower                                                           |
| unpickle             | 9.23 us                                                         | 9.99 us: 1.08x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.18x faster                                                                    |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 22.0 ms                                                         | 22.5 ms: 1.02x slower                                                           |
| python_startup_no_site | 18.8 ms                                                         | 20.2 ms: 1.07x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.05x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 10.3 ms                                                         | 6.85 ms: 1.50x faster                                                           |
| genshi_xml      | 61.2 ms                                                         | 46.5 ms: 1.32x faster                                                           |
| genshi_text     | 26.8 ms                                                         | 20.5 ms: 1.31x faster                                                           |
| django_template | 37.4 ms                                                         | 30.3 ms: 1.23x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.34x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols   | 478 us                                                          | 89.5 us: 5.34x faster                                                           |
| generators                 | 52.2 ms                                                         | 23.0 ms: 2.27x faster                                                           |
| logging_silent             | 119 ns                                                          | 60.8 ns: 1.96x faster                                                           |
| pylint                     | 418 ms                                                          | 228 ms: 1.84x faster                                                            |
| richards_super             | 58.7 ms                                                         | 32.8 ms: 1.79x faster                                                           |
| deltablue                  | 4.10 ms                                                         | 2.30 ms: 1.78x faster                                                           |
| comprehensions             | 22.1 us                                                         | 12.9 us: 1.71x faster                                                           |
| spectral_norm              | 122 ms                                                          | 72.3 ms: 1.68x faster                                                           |
| richards                   | 48.8 ms                                                         | 29.2 ms: 1.67x faster                                                           |
| nbody                      | 126 ms                                                          | 76.4 ms: 1.65x faster                                                           |
| deepcopy_memo              | 40.0 us                                                         | 24.4 us: 1.64x faster                                                           |
| chaos                      | 84.4 ms                                                         | 51.9 ms: 1.63x faster                                                           |
| coroutines                 | 23.7 ms                                                         | 14.7 ms: 1.61x faster                                                           |
| sqlglot_parse              | 1.49 ms                                                         | 942 us: 1.58x faster                                                            |
| unpack_sequence            | 65.2 ns                                                         | 41.6 ns: 1.57x faster                                                           |
| async_tree_none            | 343 ms                                                          | 221 ms: 1.55x faster                                                            |
| async_tree_io_tg           | 746 ms                                                          | 488 ms: 1.53x faster                                                            |
| fannkuch                   | 399 ms                                                          | 261 ms: 1.53x faster                                                            |
| raytrace                   | 327 ms                                                          | 217 ms: 1.51x faster                                                            |
| async_tree_memoization     | 408 ms                                                          | 272 ms: 1.50x faster                                                            |
| mako                       | 10.3 ms                                                         | 6.85 ms: 1.50x faster                                                           |
| async_tree_none_tg         | 301 ms                                                          | 201 ms: 1.50x faster                                                            |
| async_tree_memoization_tg  | 378 ms                                                          | 252 ms: 1.50x faster                                                            |
| sqlglot_transpile          | 1.78 ms                                                         | 1.20 ms: 1.49x faster                                                           |
| scimark_monte_carlo        | 70.8 ms                                                         | 47.9 ms: 1.48x faster                                                           |
| scimark_sor                | 135 ms                                                          | 91.6 ms: 1.48x faster                                                           |
| crypto_pyaes               | 79.4 ms                                                         | 54.0 ms: 1.47x faster                                                           |
| pickle_pure_python         | 309 us                                                          | 211 us: 1.47x faster                                                            |
| nqueens                    | 111 ms                                                          | 76.0 ms: 1.47x faster                                                           |
| tomli_loads                | 2.31 sec                                                        | 1.59 sec: 1.45x faster                                                          |
| async_tree_io              | 754 ms                                                          | 522 ms: 1.44x faster                                                            |
| pprint_pformat             | 1.70 sec                                                        | 1.18 sec: 1.43x faster                                                          |
| unpickle_pure_python       | 231 us                                                          | 161 us: 1.43x faster                                                            |
| pyflate                    | 471 ms                                                          | 329 ms: 1.43x faster                                                            |
| hexiom                     | 7.51 ms                                                         | 5.25 ms: 1.43x faster                                                           |
| json_dumps                 | 9.80 ms                                                         | 6.85 ms: 1.43x faster                                                           |
| pprint_safe_repr           | 819 ms                                                          | 574 ms: 1.43x faster                                                            |
| scimark_fft                | 291 ms                                                          | 205 ms: 1.42x faster                                                            |
| float                      | 76.1 ms                                                         | 53.8 ms: 1.41x faster                                                           |
| scimark_sparse_mat_mult    | 4.23 ms                                                         | 3.01 ms: 1.41x faster                                                           |
| deepcopy                   | 381 us                                                          | 275 us: 1.38x faster                                                            |
| sympy_sum                  | 149 ms                                                          | 108 ms: 1.38x faster                                                            |
| logging_simple             | 10.8 us                                                         | 7.88 us: 1.37x faster                                                           |
| chameleon                  | 8.08 ms                                                         | 5.93 ms: 1.36x faster                                                           |
| deepcopy_reduce            | 3.32 us                                                         | 2.44 us: 1.36x faster                                                           |
| logging_format             | 11.5 us                                                         | 8.47 us: 1.35x faster                                                           |
| xml_etree_process          | 55.0 ms                                                         | 41.4 ms: 1.33x faster                                                           |
| sympy_str                  | 283 ms                                                          | 213 ms: 1.33x faster                                                            |
| genshi_xml                 | 61.2 ms                                                         | 46.5 ms: 1.32x faster                                                           |
| sympy_integrate            | 19.9 ms                                                         | 15.2 ms: 1.31x faster                                                           |
| genshi_text                | 26.8 ms                                                         | 20.5 ms: 1.31x faster                                                           |
| go                         | 147 ms                                                          | 113 ms: 1.31x faster                                                            |
| scimark_lu                 | 102 ms                                                          | 79.6 ms: 1.29x faster                                                           |
| mdp                        | 2.07 sec                                                        | 1.61 sec: 1.29x faster                                                          |
| asyncio_tcp                | 787 ms                                                          | 617 ms: 1.27x faster                                                            |
| async_tree_cpu_io_mixed_tg | 577 ms                                                          | 455 ms: 1.27x faster                                                            |
| regex_compile              | 148 ms                                                          | 117 ms: 1.27x faster                                                            |
| async_tree_cpu_io_mixed    | 590 ms                                                          | 468 ms: 1.26x faster                                                            |
| pycparser                  | 1.04 sec                                                        | 838 ms: 1.25x faster                                                            |
| sqlglot_optimize           | 51.8 ms                                                         | 42.0 ms: 1.23x faster                                                           |
| django_template            | 37.4 ms                                                         | 30.3 ms: 1.23x faster                                                           |
| sympy_expand               | 462 ms                                                          | 377 ms: 1.23x faster                                                            |
| tornado_http               | 118 ms                                                          | 97.5 ms: 1.21x faster                                                           |
| xml_etree_generate         | 71.6 ms                                                         | 59.1 ms: 1.21x faster                                                           |
| meteor_contest             | 90.9 ms                                                         | 76.5 ms: 1.19x faster                                                           |
| unpickle_list              | 3.28 us                                                         | 2.76 us: 1.19x faster                                                           |
| 2to3                       | 282 ms                                                          | 241 ms: 1.17x faster                                                            |
| html5lib                   | 54.3 ms                                                         | 47.0 ms: 1.16x faster                                                           |
| xml_etree_iterparse        | 75.6 ms                                                         | 65.7 ms: 1.15x faster                                                           |
| json                       | 4.78 ms                                                         | 4.17 ms: 1.15x faster                                                           |
| docutils                   | 2.10 sec                                                        | 1.88 sec: 1.12x faster                                                          |
| bench_thread_pool          | 1.14 ms                                                         | 1.02 ms: 1.11x faster                                                           |
| sqlite_synth               | 2.15 us                                                         | 1.93 us: 1.11x faster                                                           |
| xml_etree_parse            | 114 ms                                                          | 107 ms: 1.06x faster                                                            |
| pickle                     | 7.99 us                                                         | 7.73 us: 1.03x faster                                                           |
| pidigits                   | 203 ms                                                          | 199 ms: 1.02x faster                                                            |
| bench_mp_pool              | 70.9 ms                                                         | 69.5 ms: 1.02x faster                                                           |
| asyncio_tcp_ssl            | 17.1 sec                                                        | 16.8 sec: 1.01x faster                                                          |
| pickle_dict                | 20.1 us                                                         | 19.9 us: 1.01x faster                                                           |
| json_loads                 | 20.0 us                                                         | 20.4 us: 1.02x slower                                                           |
| python_startup             | 22.0 ms                                                         | 22.5 ms: 1.02x slower                                                           |
| regex_dna                  | 122 ms                                                          | 126 ms: 1.03x slower                                                            |
| async_generators           | 260 ms                                                          | 270 ms: 1.04x slower                                                            |
| create_gc_cycles           | 618 us                                                          | 652 us: 1.06x slower                                                            |
| regex_v8                   | 15.2 ms                                                         | 16.1 ms: 1.06x slower                                                           |
| regex_effbot               | 1.82 ms                                                         | 1.94 ms: 1.06x slower                                                           |
| python_startup_no_site     | 18.8 ms                                                         | 20.2 ms: 1.07x slower                                                           |
| pathlib                    | 79.9 ms                                                         | 86.0 ms: 1.08x slower                                                           |
| unpickle                   | 9.23 us                                                         | 9.99 us: 1.08x slower                                                           |
| telco                      | 5.29 ms                                                         | 6.03 ms: 1.14x slower                                                           |
| sqlglot_normalize          | 113 ms                                                          | 215 ms: 1.90x slower                                                            |
| coverage                   | 58.0 ms                                                         | 469 ms: 8.09x slower                                                            |
| thrift                     | 801 us                                                          | 11.0 ms: 13.77x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.24x faster                                                                    |

Benchmark hidden because not significant (2): gc_traversal, pickle_list
Ignored benchmarks (7) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509.json: aiohttp, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x


# Memory

- memory change: unknown