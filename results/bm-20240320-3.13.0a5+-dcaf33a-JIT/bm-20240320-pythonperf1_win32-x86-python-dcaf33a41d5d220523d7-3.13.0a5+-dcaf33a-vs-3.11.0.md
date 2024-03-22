# Results vs. 3.11.0

- fork: python
- ref: dcaf33a41d5d220523d7
- machine: windows-x86
- commit hash: dcaf33a
- commit date: 2024-03-20
- overall geometric mean: 1.01x slower
- HPT reliability: 99.47%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240320-pythonperf1_win32-x86-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 282 ms                                                          | 266 ms: 1.06x faster                                                            |
| chameleon      | 8.08 ms                                                         | 5.84 ms: 1.38x faster                                                           |
| docutils       | 2.10 sec                                                        | 2.45 sec: 1.17x slower                                                          |
| html5lib       | 54.3 ms                                                         | 50.2 ms: 1.08x faster                                                           |
| tornado_http   | 118 ms                                                          | 97.2 ms: 1.22x faster                                                           |
| Geometric mean | (ref)                                                           | 1.11x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240320-pythonperf1_win32-x86-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 590 ms                                                          | 1.57 sec: 2.65x slower                                                          |
| async_tree_cpu_io_mixed_tg | 577 ms                                                          | 1.61 sec: 2.79x slower                                                          |
| async_tree_none            | 343 ms                                                          | 1.20 sec: 3.50x slower                                                          |
| async_tree_memoization     | 408 ms                                                          | 1.47 sec: 3.59x slower                                                          |
| async_tree_memoization_tg  | 378 ms                                                          | 1.47 sec: 3.91x slower                                                          |
| async_tree_none_tg         | 301 ms                                                          | 1.24 sec: 4.11x slower                                                          |
| async_tree_io              | 754 ms                                                          | 4.63 sec: 6.15x slower                                                          |
| async_tree_io_tg           | 746 ms                                                          | 4.73 sec: 6.34x slower                                                          |
| Geometric mean             | (ref)                                                           | 3.94x slower                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240320-pythonperf1_win32-x86-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 126 ms                                                          | 100 ms: 1.26x faster                                                            |
| pidigits       | 203 ms                                                          | 199 ms: 1.02x faster                                                            |
| float          | 76.1 ms                                                         | 82.2 ms: 1.08x slower                                                           |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240320-pythonperf1_win32-x86-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                          | 110 ms: 1.35x faster                                                            |
| regex_dna      | 122 ms                                                          | 124 ms: 1.02x slower                                                            |
| regex_v8       | 15.2 ms                                                         | 16.0 ms: 1.06x slower                                                           |
| regex_effbot   | 1.82 ms                                                         | 1.95 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240320-pythonperf1_win32-x86-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 309 us                                                          | 215 us: 1.44x faster                                                            |
| json_dumps           | 9.80 ms                                                         | 6.93 ms: 1.41x faster                                                           |
| tomli_loads          | 2.31 sec                                                        | 1.72 sec: 1.35x faster                                                          |
| unpickle_pure_python | 231 us                                                          | 174 us: 1.33x faster                                                            |
| xml_etree_process    | 55.0 ms                                                         | 47.6 ms: 1.16x faster                                                           |
| unpickle_list        | 3.28 us                                                         | 3.04 us: 1.08x faster                                                           |
| xml_etree_generate   | 71.6 ms                                                         | 69.1 ms: 1.04x faster                                                           |
| pickle_dict          | 20.1 us                                                         | 20.0 us: 1.00x faster                                                           |
| json_loads           | 20.0 us                                                         | 20.1 us: 1.00x slower                                                           |
| pickle_list          | 3.27 us                                                         | 3.46 us: 1.06x slower                                                           |
| unpickle             | 9.23 us                                                         | 10.5 us: 1.14x slower                                                           |
| xml_etree_parse      | 114 ms                                                          | 133 ms: 1.17x slower                                                            |
| xml_etree_iterparse  | 75.6 ms                                                         | 93.8 ms: 1.24x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.07x faster                                                                    |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240320-pythonperf1_win32-x86-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 22.0 ms                                                         | 26.6 ms: 1.21x slower                                                           |
| python_startup_no_site | 18.8 ms                                                         | 24.2 ms: 1.29x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.25x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240320-pythonperf1_win32-x86-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 10.3 ms                                                         | 7.15 ms: 1.44x faster                                                           |
| genshi_xml      | 61.2 ms                                                         | 50.0 ms: 1.23x faster                                                           |
| django_template | 37.4 ms                                                         | 31.1 ms: 1.20x faster                                                           |
| genshi_text     | 26.8 ms                                                         | 22.8 ms: 1.18x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.26x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240320-pythonperf1_win32-x86-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols   | 478 us                                                          | 98.8 us: 4.84x faster                                                           |
| generators                 | 52.2 ms                                                         | 22.4 ms: 2.33x faster                                                           |
| logging_silent             | 119 ns                                                          | 60.6 ns: 1.97x faster                                                           |
| spectral_norm              | 122 ms                                                          | 71.6 ms: 1.70x faster                                                           |
| coroutines                 | 23.7 ms                                                         | 14.9 ms: 1.59x faster                                                           |
| deepcopy_memo              | 40.0 us                                                         | 25.2 us: 1.59x faster                                                           |
| deltablue                  | 4.10 ms                                                         | 2.67 ms: 1.54x faster                                                           |
| comprehensions             | 22.1 us                                                         | 14.4 us: 1.53x faster                                                           |
| unpack_sequence            | 65.2 ns                                                         | 43.1 ns: 1.51x faster                                                           |
| sqlglot_parse              | 1.49 ms                                                         | 1.03 ms: 1.44x faster                                                           |
| pickle_pure_python         | 309 us                                                          | 215 us: 1.44x faster                                                            |
| mako                       | 10.3 ms                                                         | 7.15 ms: 1.44x faster                                                           |
| richards_super             | 58.7 ms                                                         | 40.9 ms: 1.43x faster                                                           |
| json_dumps                 | 9.80 ms                                                         | 6.93 ms: 1.41x faster                                                           |
| sympy_sum                  | 149 ms                                                          | 105 ms: 1.41x faster                                                            |
| sqlglot_transpile          | 1.78 ms                                                         | 1.29 ms: 1.39x faster                                                           |
| chaos                      | 84.4 ms                                                         | 60.9 ms: 1.39x faster                                                           |
| chameleon                  | 8.08 ms                                                         | 5.84 ms: 1.38x faster                                                           |
| richards                   | 48.8 ms                                                         | 35.7 ms: 1.37x faster                                                           |
| scimark_sor                | 135 ms                                                          | 99.3 ms: 1.36x faster                                                           |
| scimark_sparse_mat_mult    | 4.23 ms                                                         | 3.13 ms: 1.35x faster                                                           |
| tomli_loads                | 2.31 sec                                                        | 1.72 sec: 1.35x faster                                                          |
| regex_compile              | 148 ms                                                          | 110 ms: 1.35x faster                                                            |
| sympy_str                  | 283 ms                                                          | 211 ms: 1.34x faster                                                            |
| unpickle_pure_python       | 231 us                                                          | 174 us: 1.33x faster                                                            |
| deepcopy_reduce            | 3.32 us                                                         | 2.51 us: 1.32x faster                                                           |
| deepcopy                   | 381 us                                                          | 289 us: 1.32x faster                                                            |
| sympy_integrate            | 19.9 ms                                                         | 15.3 ms: 1.30x faster                                                           |
| crypto_pyaes               | 79.4 ms                                                         | 61.5 ms: 1.29x faster                                                           |
| logging_simple             | 10.8 us                                                         | 8.38 us: 1.29x faster                                                           |
| logging_format             | 11.5 us                                                         | 9.02 us: 1.27x faster                                                           |
| hexiom                     | 7.51 ms                                                         | 5.98 ms: 1.26x faster                                                           |
| nbody                      | 126 ms                                                          | 100 ms: 1.26x faster                                                            |
| pyflate                    | 471 ms                                                          | 376 ms: 1.25x faster                                                            |
| asyncio_tcp                | 787 ms                                                          | 629 ms: 1.25x faster                                                            |
| sympy_expand               | 462 ms                                                          | 371 ms: 1.24x faster                                                            |
| raytrace                   | 327 ms                                                          | 264 ms: 1.24x faster                                                            |
| nqueens                    | 111 ms                                                          | 90.2 ms: 1.24x faster                                                           |
| scimark_lu                 | 102 ms                                                          | 83.3 ms: 1.23x faster                                                           |
| genshi_xml                 | 61.2 ms                                                         | 50.0 ms: 1.23x faster                                                           |
| scimark_fft                | 291 ms                                                          | 239 ms: 1.22x faster                                                            |
| tornado_http               | 118 ms                                                          | 97.2 ms: 1.22x faster                                                           |
| fannkuch                   | 399 ms                                                          | 329 ms: 1.21x faster                                                            |
| django_template            | 37.4 ms                                                         | 31.1 ms: 1.20x faster                                                           |
| mdp                        | 2.07 sec                                                        | 1.74 sec: 1.19x faster                                                          |
| genshi_text                | 26.8 ms                                                         | 22.8 ms: 1.18x faster                                                           |
| go                         | 147 ms                                                          | 126 ms: 1.16x faster                                                            |
| pprint_pformat             | 1.70 sec                                                        | 1.46 sec: 1.16x faster                                                          |
| xml_etree_process          | 55.0 ms                                                         | 47.6 ms: 1.16x faster                                                           |
| pprint_safe_repr           | 819 ms                                                          | 715 ms: 1.15x faster                                                            |
| sqlglot_optimize           | 51.8 ms                                                         | 45.8 ms: 1.13x faster                                                           |
| bench_thread_pool          | 1.14 ms                                                         | 1.01 ms: 1.12x faster                                                           |
| json                       | 4.78 ms                                                         | 4.30 ms: 1.11x faster                                                           |
| sqlite_synth               | 2.15 us                                                         | 1.95 us: 1.10x faster                                                           |
| scimark_monte_carlo        | 70.8 ms                                                         | 64.6 ms: 1.10x faster                                                           |
| meteor_contest             | 90.9 ms                                                         | 83.4 ms: 1.09x faster                                                           |
| gc_traversal               | 1.38 ms                                                         | 1.27 ms: 1.08x faster                                                           |
| html5lib                   | 54.3 ms                                                         | 50.2 ms: 1.08x faster                                                           |
| unpickle_list              | 3.28 us                                                         | 3.04 us: 1.08x faster                                                           |
| 2to3                       | 282 ms                                                          | 266 ms: 1.06x faster                                                            |
| pycparser                  | 1.04 sec                                                        | 989 ms: 1.05x faster                                                            |
| xml_etree_generate         | 71.6 ms                                                         | 69.1 ms: 1.04x faster                                                           |
| pylint                     | 418 ms                                                          | 405 ms: 1.03x faster                                                            |
| asyncio_tcp_ssl            | 17.1 sec                                                        | 16.7 sec: 1.02x faster                                                          |
| pidigits                   | 203 ms                                                          | 199 ms: 1.02x faster                                                            |
| pickle_dict                | 20.1 us                                                         | 20.0 us: 1.00x faster                                                           |
| json_loads                 | 20.0 us                                                         | 20.1 us: 1.00x slower                                                           |
| regex_dna                  | 122 ms                                                          | 124 ms: 1.02x slower                                                            |
| regex_v8                   | 15.2 ms                                                         | 16.0 ms: 1.06x slower                                                           |
| pickle_list                | 3.27 us                                                         | 3.46 us: 1.06x slower                                                           |
| bench_mp_pool              | 70.9 ms                                                         | 75.6 ms: 1.07x slower                                                           |
| regex_effbot               | 1.82 ms                                                         | 1.95 ms: 1.07x slower                                                           |
| create_gc_cycles           | 618 us                                                          | 664 us: 1.07x slower                                                            |
| pathlib                    | 79.9 ms                                                         | 86.3 ms: 1.08x slower                                                           |
| float                      | 76.1 ms                                                         | 82.2 ms: 1.08x slower                                                           |
| unpickle                   | 9.23 us                                                         | 10.5 us: 1.14x slower                                                           |
| xml_etree_parse            | 114 ms                                                          | 133 ms: 1.17x slower                                                            |
| docutils                   | 2.10 sec                                                        | 2.45 sec: 1.17x slower                                                          |
| python_startup             | 22.0 ms                                                         | 26.6 ms: 1.21x slower                                                           |
| telco                      | 5.29 ms                                                         | 6.53 ms: 1.23x slower                                                           |
| async_generators           | 260 ms                                                          | 322 ms: 1.24x slower                                                            |
| xml_etree_iterparse        | 75.6 ms                                                         | 93.8 ms: 1.24x slower                                                           |
| python_startup_no_site     | 18.8 ms                                                         | 24.2 ms: 1.29x slower                                                           |
| sqlglot_normalize          | 113 ms                                                          | 221 ms: 1.95x slower                                                            |
| async_tree_cpu_io_mixed    | 590 ms                                                          | 1.57 sec: 2.65x slower                                                          |
| async_tree_cpu_io_mixed_tg | 577 ms                                                          | 1.61 sec: 2.79x slower                                                          |
| async_tree_none            | 343 ms                                                          | 1.20 sec: 3.50x slower                                                          |
| async_tree_memoization     | 408 ms                                                          | 1.47 sec: 3.59x slower                                                          |
| async_tree_memoization_tg  | 378 ms                                                          | 1.47 sec: 3.91x slower                                                          |
| async_tree_none_tg         | 301 ms                                                          | 1.24 sec: 4.11x slower                                                          |
| async_tree_io              | 754 ms                                                          | 4.63 sec: 6.15x slower                                                          |
| async_tree_io_tg           | 746 ms                                                          | 4.73 sec: 6.34x slower                                                          |
| coverage                   | 58.0 ms                                                         | 508 ms: 8.75x slower                                                            |
| thrift                     | 801 us                                                          | 10.8 ms: 13.54x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): pickle
Ignored benchmarks (7) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509.json: aiohttp, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 99.47% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x


# Memory

- memory change: unknown