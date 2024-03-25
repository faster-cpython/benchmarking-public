# Results vs. 3.11.0

- fork: python
- ref: d610d821fd210dce63a1
- machine: windows-x86
- commit hash: d610d82
- commit date: 2024-03-23
- overall geometric mean: 1.16x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 282 ms                                                          | 262 ms: 1.08x faster                                                            |
| chameleon      | 8.08 ms                                                         | 6.15 ms: 1.31x faster                                                           |
| docutils       | 2.10 sec                                                        | 1.93 sec: 1.09x faster                                                          |
| html5lib       | 54.3 ms                                                         | 46.6 ms: 1.16x faster                                                           |
| tornado_http   | 118 ms                                                          | 99.2 ms: 1.19x faster                                                           |
| Geometric mean | (ref)                                                           | 1.16x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none            | 343 ms                                                          | 237 ms: 1.45x faster                                                            |
| async_tree_io_tg           | 746 ms                                                          | 522 ms: 1.43x faster                                                            |
| async_tree_memoization     | 408 ms                                                          | 292 ms: 1.40x faster                                                            |
| async_tree_none_tg         | 301 ms                                                          | 216 ms: 1.39x faster                                                            |
| async_tree_memoization_tg  | 378 ms                                                          | 273 ms: 1.38x faster                                                            |
| async_tree_io              | 754 ms                                                          | 559 ms: 1.35x faster                                                            |
| async_tree_cpu_io_mixed_tg | 577 ms                                                          | 484 ms: 1.19x faster                                                            |
| async_tree_cpu_io_mixed    | 590 ms                                                          | 515 ms: 1.15x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.34x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 76.1 ms                                                         | 52.7 ms: 1.44x faster                                                           |
| nbody          | 126 ms                                                          | 97.1 ms: 1.30x faster                                                           |
| pidigits       | 203 ms                                                          | 201 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                           | 1.24x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                          | 113 ms: 1.31x faster                                                            |
| regex_effbot   | 1.82 ms                                                         | 1.91 ms: 1.05x slower                                                           |
| regex_v8       | 15.2 ms                                                         | 16.1 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                    |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 9.80 ms                                                         | 6.81 ms: 1.44x faster                                                           |
| pickle_pure_python   | 309 us                                                          | 224 us: 1.38x faster                                                            |
| unpickle_pure_python | 231 us                                                          | 168 us: 1.37x faster                                                            |
| tomli_loads          | 2.31 sec                                                        | 1.71 sec: 1.35x faster                                                          |
| xml_etree_process    | 55.0 ms                                                         | 44.0 ms: 1.25x faster                                                           |
| unpickle_list        | 3.28 us                                                         | 2.72 us: 1.20x faster                                                           |
| xml_etree_generate   | 71.6 ms                                                         | 62.4 ms: 1.15x faster                                                           |
| xml_etree_iterparse  | 75.6 ms                                                         | 66.7 ms: 1.13x faster                                                           |
| xml_etree_parse      | 114 ms                                                          | 108 ms: 1.06x faster                                                            |
| pickle_dict          | 20.1 us                                                         | 19.8 us: 1.01x faster                                                           |
| pickle               | 7.99 us                                                         | 7.88 us: 1.01x faster                                                           |
| json_loads           | 20.0 us                                                         | 20.3 us: 1.01x slower                                                           |
| unpickle             | 9.23 us                                                         | 10.0 us: 1.08x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.15x faster                                                                    |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 22.0 ms                                                         | 26.1 ms: 1.19x slower                                                           |
| python_startup_no_site | 18.8 ms                                                         | 23.3 ms: 1.24x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.21x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 10.3 ms                                                         | 7.20 ms: 1.43x faster                                                           |
| genshi_xml      | 61.2 ms                                                         | 49.8 ms: 1.23x faster                                                           |
| django_template | 37.4 ms                                                         | 32.7 ms: 1.14x faster                                                           |
| genshi_text     | 26.8 ms                                                         | 23.8 ms: 1.13x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.23x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols   | 478 us                                                          | 93.9 us: 5.09x faster                                                           |
| generators                 | 52.2 ms                                                         | 25.0 ms: 2.08x faster                                                           |
| pylint                     | 418 ms                                                          | 240 ms: 1.74x faster                                                            |
| logging_silent             | 119 ns                                                          | 69.4 ns: 1.72x faster                                                           |
| spectral_norm              | 122 ms                                                          | 71.6 ms: 1.70x faster                                                           |
| coroutines                 | 23.7 ms                                                         | 15.1 ms: 1.57x faster                                                           |
| deltablue                  | 4.10 ms                                                         | 2.62 ms: 1.57x faster                                                           |
| unpack_sequence            | 65.2 ns                                                         | 44.3 ns: 1.47x faster                                                           |
| deepcopy_memo              | 40.0 us                                                         | 27.3 us: 1.47x faster                                                           |
| sqlglot_parse              | 1.49 ms                                                         | 1.03 ms: 1.45x faster                                                           |
| async_tree_none            | 343 ms                                                          | 237 ms: 1.45x faster                                                            |
| float                      | 76.1 ms                                                         | 52.7 ms: 1.44x faster                                                           |
| json_dumps                 | 9.80 ms                                                         | 6.81 ms: 1.44x faster                                                           |
| async_tree_io_tg           | 746 ms                                                          | 522 ms: 1.43x faster                                                            |
| mako                       | 10.3 ms                                                         | 7.20 ms: 1.43x faster                                                           |
| richards_super             | 58.7 ms                                                         | 41.3 ms: 1.42x faster                                                           |
| comprehensions             | 22.1 us                                                         | 15.6 us: 1.42x faster                                                           |
| chaos                      | 84.4 ms                                                         | 59.7 ms: 1.41x faster                                                           |
| async_tree_memoization     | 408 ms                                                          | 292 ms: 1.40x faster                                                            |
| sqlglot_transpile          | 1.78 ms                                                         | 1.28 ms: 1.40x faster                                                           |
| async_tree_none_tg         | 301 ms                                                          | 216 ms: 1.39x faster                                                            |
| async_tree_memoization_tg  | 378 ms                                                          | 273 ms: 1.38x faster                                                            |
| pickle_pure_python         | 309 us                                                          | 224 us: 1.38x faster                                                            |
| unpickle_pure_python       | 231 us                                                          | 168 us: 1.37x faster                                                            |
| tomli_loads                | 2.31 sec                                                        | 1.71 sec: 1.35x faster                                                          |
| async_tree_io              | 754 ms                                                          | 559 ms: 1.35x faster                                                            |
| scimark_sparse_mat_mult    | 4.23 ms                                                         | 3.14 ms: 1.35x faster                                                           |
| richards                   | 48.8 ms                                                         | 36.3 ms: 1.34x faster                                                           |
| sympy_sum                  | 149 ms                                                          | 111 ms: 1.34x faster                                                            |
| deepcopy                   | 381 us                                                          | 289 us: 1.32x faster                                                            |
| chameleon                  | 8.08 ms                                                         | 6.15 ms: 1.31x faster                                                           |
| scimark_sor                | 135 ms                                                          | 103 ms: 1.31x faster                                                            |
| sympy_str                  | 283 ms                                                          | 217 ms: 1.31x faster                                                            |
| regex_compile              | 148 ms                                                          | 113 ms: 1.31x faster                                                            |
| crypto_pyaes               | 79.4 ms                                                         | 61.0 ms: 1.30x faster                                                           |
| nbody                      | 126 ms                                                          | 97.1 ms: 1.30x faster                                                           |
| deepcopy_reduce            | 3.32 us                                                         | 2.59 us: 1.28x faster                                                           |
| logging_simple             | 10.8 us                                                         | 8.44 us: 1.28x faster                                                           |
| logging_format             | 11.5 us                                                         | 9.06 us: 1.26x faster                                                           |
| xml_etree_process          | 55.0 ms                                                         | 44.0 ms: 1.25x faster                                                           |
| pyflate                    | 471 ms                                                          | 377 ms: 1.25x faster                                                            |
| asyncio_tcp                | 787 ms                                                          | 634 ms: 1.24x faster                                                            |
| hexiom                     | 7.51 ms                                                         | 6.07 ms: 1.24x faster                                                           |
| sympy_expand               | 462 ms                                                          | 375 ms: 1.23x faster                                                            |
| genshi_xml                 | 61.2 ms                                                         | 49.8 ms: 1.23x faster                                                           |
| pycparser                  | 1.04 sec                                                        | 854 ms: 1.22x faster                                                            |
| nqueens                    | 111 ms                                                          | 92.2 ms: 1.21x faster                                                           |
| unpickle_list              | 3.28 us                                                         | 2.72 us: 1.20x faster                                                           |
| scimark_lu                 | 102 ms                                                          | 85.0 ms: 1.20x faster                                                           |
| sympy_integrate            | 19.9 ms                                                         | 16.6 ms: 1.20x faster                                                           |
| scimark_fft                | 291 ms                                                          | 244 ms: 1.20x faster                                                            |
| tornado_http               | 118 ms                                                          | 99.2 ms: 1.19x faster                                                           |
| async_tree_cpu_io_mixed_tg | 577 ms                                                          | 484 ms: 1.19x faster                                                            |
| fannkuch                   | 399 ms                                                          | 337 ms: 1.19x faster                                                            |
| raytrace                   | 327 ms                                                          | 280 ms: 1.17x faster                                                            |
| html5lib                   | 54.3 ms                                                         | 46.6 ms: 1.16x faster                                                           |
| json                       | 4.78 ms                                                         | 4.11 ms: 1.16x faster                                                           |
| go                         | 147 ms                                                          | 127 ms: 1.16x faster                                                            |
| mdp                        | 2.07 sec                                                        | 1.79 sec: 1.16x faster                                                          |
| xml_etree_generate         | 71.6 ms                                                         | 62.4 ms: 1.15x faster                                                           |
| async_tree_cpu_io_mixed    | 590 ms                                                          | 515 ms: 1.15x faster                                                            |
| django_template            | 37.4 ms                                                         | 32.7 ms: 1.14x faster                                                           |
| xml_etree_iterparse        | 75.6 ms                                                         | 66.7 ms: 1.13x faster                                                           |
| pprint_pformat             | 1.70 sec                                                        | 1.50 sec: 1.13x faster                                                          |
| genshi_text                | 26.8 ms                                                         | 23.8 ms: 1.13x faster                                                           |
| bench_thread_pool          | 1.14 ms                                                         | 1.01 ms: 1.12x faster                                                           |
| sqlglot_optimize           | 51.8 ms                                                         | 46.2 ms: 1.12x faster                                                           |
| pprint_safe_repr           | 819 ms                                                          | 731 ms: 1.12x faster                                                            |
| sqlite_synth               | 2.15 us                                                         | 1.92 us: 1.12x faster                                                           |
| meteor_contest             | 90.9 ms                                                         | 83.3 ms: 1.09x faster                                                           |
| docutils                   | 2.10 sec                                                        | 1.93 sec: 1.09x faster                                                          |
| scimark_monte_carlo        | 70.8 ms                                                         | 65.6 ms: 1.08x faster                                                           |
| 2to3                       | 282 ms                                                          | 262 ms: 1.08x faster                                                            |
| xml_etree_parse            | 114 ms                                                          | 108 ms: 1.06x faster                                                            |
| asyncio_tcp_ssl            | 17.1 sec                                                        | 16.7 sec: 1.02x faster                                                          |
| pickle_dict                | 20.1 us                                                         | 19.8 us: 1.01x faster                                                           |
| pickle                     | 7.99 us                                                         | 7.88 us: 1.01x faster                                                           |
| pidigits                   | 203 ms                                                          | 201 ms: 1.01x faster                                                            |
| json_loads                 | 20.0 us                                                         | 20.3 us: 1.01x slower                                                           |
| bench_mp_pool              | 70.9 ms                                                         | 74.1 ms: 1.04x slower                                                           |
| regex_effbot               | 1.82 ms                                                         | 1.91 ms: 1.05x slower                                                           |
| create_gc_cycles           | 618 us                                                          | 646 us: 1.05x slower                                                            |
| regex_v8                   | 15.2 ms                                                         | 16.1 ms: 1.06x slower                                                           |
| pathlib                    | 79.9 ms                                                         | 86.4 ms: 1.08x slower                                                           |
| unpickle                   | 9.23 us                                                         | 10.0 us: 1.08x slower                                                           |
| async_generators           | 260 ms                                                          | 293 ms: 1.13x slower                                                            |
| python_startup             | 22.0 ms                                                         | 26.1 ms: 1.19x slower                                                           |
| telco                      | 5.29 ms                                                         | 6.46 ms: 1.22x slower                                                           |
| python_startup_no_site     | 18.8 ms                                                         | 23.3 ms: 1.24x slower                                                           |
| sqlglot_normalize          | 113 ms                                                          | 240 ms: 2.12x slower                                                            |
| coverage                   | 58.0 ms                                                         | 484 ms: 8.35x slower                                                            |
| thrift                     | 801 us                                                          | 11.0 ms: 13.75x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.16x faster                                                                    |

Benchmark hidden because not significant (3): pickle_list, regex_dna, gc_traversal
Ignored benchmarks (7) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509.json: aiohttp, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.15x


# Memory

- memory change: unknown