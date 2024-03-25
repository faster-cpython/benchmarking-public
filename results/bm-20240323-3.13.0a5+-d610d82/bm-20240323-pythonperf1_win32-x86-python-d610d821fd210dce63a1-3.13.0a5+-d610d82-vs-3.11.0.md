# Results vs. 3.11.0

- fork: python
- ref: d610d821fd210dce63a1
- machine: windows-x86
- commit hash: d610d82
- commit date: 2024-03-23
- overall geometric mean: 1.30x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 282 ms                                                          | 228 ms: 1.24x faster                                                            |
| chameleon      | 8.08 ms                                                         | 5.65 ms: 1.43x faster                                                           |
| docutils       | 2.10 sec                                                        | 1.75 sec: 1.20x faster                                                          |
| html5lib       | 54.3 ms                                                         | 42.6 ms: 1.27x faster                                                           |
| tornado_http   | 118 ms                                                          | 93.9 ms: 1.26x faster                                                           |
| Geometric mean | (ref)                                                           | 1.28x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none            | 343 ms                                                          | 215 ms: 1.59x faster                                                            |
| async_tree_memoization     | 408 ms                                                          | 265 ms: 1.54x faster                                                            |
| async_tree_io_tg           | 746 ms                                                          | 489 ms: 1.53x faster                                                            |
| async_tree_none_tg         | 301 ms                                                          | 198 ms: 1.52x faster                                                            |
| async_tree_memoization_tg  | 378 ms                                                          | 250 ms: 1.51x faster                                                            |
| async_tree_io              | 754 ms                                                          | 520 ms: 1.45x faster                                                            |
| async_tree_cpu_io_mixed    | 590 ms                                                          | 461 ms: 1.28x faster                                                            |
| async_tree_cpu_io_mixed_tg | 577 ms                                                          | 458 ms: 1.26x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.45x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 126 ms                                                          | 77.3 ms: 1.63x faster                                                           |
| float          | 76.1 ms                                                         | 51.5 ms: 1.48x faster                                                           |
| pidigits       | 203 ms                                                          | 197 ms: 1.03x faster                                                            |
| Geometric mean | (ref)                                                           | 1.35x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                          | 94.4 ms: 1.56x faster                                                           |
| regex_dna      | 122 ms                                                          | 118 ms: 1.03x faster                                                            |
| regex_effbot   | 1.82 ms                                                         | 1.90 ms: 1.04x slower                                                           |
| regex_v8       | 15.2 ms                                                         | 15.8 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                           | 1.10x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_pure_python | 231 us                                                          | 139 us: 1.66x faster                                                            |
| json_dumps           | 9.80 ms                                                         | 6.60 ms: 1.48x faster                                                           |
| pickle_pure_python   | 309 us                                                          | 211 us: 1.47x faster                                                            |
| tomli_loads          | 2.31 sec                                                        | 1.60 sec: 1.44x faster                                                          |
| xml_etree_process    | 55.0 ms                                                         | 40.8 ms: 1.35x faster                                                           |
| xml_etree_generate   | 71.6 ms                                                         | 59.1 ms: 1.21x faster                                                           |
| xml_etree_iterparse  | 75.6 ms                                                         | 64.7 ms: 1.17x faster                                                           |
| unpickle_list        | 3.28 us                                                         | 2.81 us: 1.16x faster                                                           |
| xml_etree_parse      | 114 ms                                                          | 107 ms: 1.06x faster                                                            |
| pickle               | 7.99 us                                                         | 7.85 us: 1.02x faster                                                           |
| json_loads           | 20.0 us                                                         | 20.0 us: 1.00x faster                                                           |
| pickle_list          | 3.27 us                                                         | 3.34 us: 1.02x slower                                                           |
| unpickle             | 9.23 us                                                         | 9.75 us: 1.06x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.19x faster                                                                    |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 22.0 ms                                                         | 22.3 ms: 1.01x slower                                                           |
| python_startup_no_site | 18.8 ms                                                         | 19.7 ms: 1.05x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.03x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 61.2 ms                                                         | 40.1 ms: 1.53x faster                                                           |
| mako            | 10.3 ms                                                         | 6.83 ms: 1.50x faster                                                           |
| genshi_text     | 26.8 ms                                                         | 18.4 ms: 1.46x faster                                                           |
| django_template | 37.4 ms                                                         | 28.6 ms: 1.31x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.45x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols   | 478 us                                                          | 89.9 us: 5.32x faster                                                           |
| generators                 | 52.2 ms                                                         | 22.3 ms: 2.34x faster                                                           |
| logging_silent             | 119 ns                                                          | 57.3 ns: 2.08x faster                                                           |
| pylint                     | 418 ms                                                          | 216 ms: 1.93x faster                                                            |
| comprehensions             | 22.1 us                                                         | 11.4 us: 1.93x faster                                                           |
| deltablue                  | 4.10 ms                                                         | 2.13 ms: 1.92x faster                                                           |
| spectral_norm              | 122 ms                                                          | 66.6 ms: 1.83x faster                                                           |
| richards_super             | 58.7 ms                                                         | 32.4 ms: 1.81x faster                                                           |
| hexiom                     | 7.51 ms                                                         | 4.19 ms: 1.79x faster                                                           |
| chaos                      | 84.4 ms                                                         | 48.0 ms: 1.76x faster                                                           |
| deepcopy_memo              | 40.0 us                                                         | 23.0 us: 1.74x faster                                                           |
| sqlglot_parse              | 1.49 ms                                                         | 859 us: 1.73x faster                                                            |
| scimark_lu                 | 102 ms                                                          | 59.8 ms: 1.71x faster                                                           |
| richards                   | 48.8 ms                                                         | 28.9 ms: 1.69x faster                                                           |
| unpack_sequence            | 65.2 ns                                                         | 39.3 ns: 1.66x faster                                                           |
| unpickle_pure_python       | 231 us                                                          | 139 us: 1.66x faster                                                            |
| raytrace                   | 327 ms                                                          | 198 ms: 1.65x faster                                                            |
| scimark_sor                | 135 ms                                                          | 82.2 ms: 1.65x faster                                                           |
| sqlglot_transpile          | 1.78 ms                                                         | 1.08 ms: 1.65x faster                                                           |
| nbody                      | 126 ms                                                          | 77.3 ms: 1.63x faster                                                           |
| coroutines                 | 23.7 ms                                                         | 14.6 ms: 1.63x faster                                                           |
| nqueens                    | 111 ms                                                          | 69.8 ms: 1.60x faster                                                           |
| async_tree_none            | 343 ms                                                          | 215 ms: 1.59x faster                                                            |
| regex_compile              | 148 ms                                                          | 94.4 ms: 1.56x faster                                                           |
| scimark_monte_carlo        | 70.8 ms                                                         | 45.4 ms: 1.56x faster                                                           |
| async_tree_memoization     | 408 ms                                                          | 265 ms: 1.54x faster                                                            |
| pprint_pformat             | 1.70 sec                                                        | 1.11 sec: 1.53x faster                                                          |
| genshi_xml                 | 61.2 ms                                                         | 40.1 ms: 1.53x faster                                                           |
| async_tree_io_tg           | 746 ms                                                          | 489 ms: 1.53x faster                                                            |
| crypto_pyaes               | 79.4 ms                                                         | 52.1 ms: 1.52x faster                                                           |
| async_tree_none_tg         | 301 ms                                                          | 198 ms: 1.52x faster                                                            |
| pprint_safe_repr           | 819 ms                                                          | 540 ms: 1.52x faster                                                            |
| async_tree_memoization_tg  | 378 ms                                                          | 250 ms: 1.51x faster                                                            |
| pyflate                    | 471 ms                                                          | 312 ms: 1.51x faster                                                            |
| go                         | 147 ms                                                          | 97.5 ms: 1.51x faster                                                           |
| sympy_sum                  | 149 ms                                                          | 98.9 ms: 1.51x faster                                                           |
| mako                       | 10.3 ms                                                         | 6.83 ms: 1.50x faster                                                           |
| json_dumps                 | 9.80 ms                                                         | 6.60 ms: 1.48x faster                                                           |
| float                      | 76.1 ms                                                         | 51.5 ms: 1.48x faster                                                           |
| pickle_pure_python         | 309 us                                                          | 211 us: 1.47x faster                                                            |
| scimark_sparse_mat_mult    | 4.23 ms                                                         | 2.89 ms: 1.46x faster                                                           |
| sympy_str                  | 283 ms                                                          | 194 ms: 1.46x faster                                                            |
| genshi_text                | 26.8 ms                                                         | 18.4 ms: 1.46x faster                                                           |
| deepcopy                   | 381 us                                                          | 263 us: 1.45x faster                                                            |
| fannkuch                   | 399 ms                                                          | 276 ms: 1.45x faster                                                            |
| async_tree_io              | 754 ms                                                          | 520 ms: 1.45x faster                                                            |
| tomli_loads                | 2.31 sec                                                        | 1.60 sec: 1.44x faster                                                          |
| scimark_fft                | 291 ms                                                          | 202 ms: 1.44x faster                                                            |
| chameleon                  | 8.08 ms                                                         | 5.65 ms: 1.43x faster                                                           |
| sympy_integrate            | 19.9 ms                                                         | 13.9 ms: 1.43x faster                                                           |
| logging_simple             | 10.8 us                                                         | 7.64 us: 1.42x faster                                                           |
| deepcopy_reduce            | 3.32 us                                                         | 2.35 us: 1.41x faster                                                           |
| logging_format             | 11.5 us                                                         | 8.28 us: 1.38x faster                                                           |
| sqlglot_optimize           | 51.8 ms                                                         | 38.1 ms: 1.36x faster                                                           |
| sympy_expand               | 462 ms                                                          | 342 ms: 1.35x faster                                                            |
| xml_etree_process          | 55.0 ms                                                         | 40.8 ms: 1.35x faster                                                           |
| pycparser                  | 1.04 sec                                                        | 776 ms: 1.34x faster                                                            |
| mdp                        | 2.07 sec                                                        | 1.56 sec: 1.32x faster                                                          |
| django_template            | 37.4 ms                                                         | 28.6 ms: 1.31x faster                                                           |
| async_tree_cpu_io_mixed    | 590 ms                                                          | 461 ms: 1.28x faster                                                            |
| html5lib                   | 54.3 ms                                                         | 42.6 ms: 1.27x faster                                                           |
| tornado_http               | 118 ms                                                          | 93.9 ms: 1.26x faster                                                           |
| async_tree_cpu_io_mixed_tg | 577 ms                                                          | 458 ms: 1.26x faster                                                            |
| asyncio_tcp                | 787 ms                                                          | 629 ms: 1.25x faster                                                            |
| 2to3                       | 282 ms                                                          | 228 ms: 1.24x faster                                                            |
| xml_etree_generate         | 71.6 ms                                                         | 59.1 ms: 1.21x faster                                                           |
| meteor_contest             | 90.9 ms                                                         | 75.1 ms: 1.21x faster                                                           |
| docutils                   | 2.10 sec                                                        | 1.75 sec: 1.20x faster                                                          |
| bench_thread_pool          | 1.14 ms                                                         | 963 us: 1.18x faster                                                            |
| xml_etree_iterparse        | 75.6 ms                                                         | 64.7 ms: 1.17x faster                                                           |
| unpickle_list              | 3.28 us                                                         | 2.81 us: 1.16x faster                                                           |
| json                       | 4.78 ms                                                         | 4.16 ms: 1.15x faster                                                           |
| sqlite_synth               | 2.15 us                                                         | 1.92 us: 1.12x faster                                                           |
| xml_etree_parse            | 114 ms                                                          | 107 ms: 1.06x faster                                                            |
| bench_mp_pool              | 70.9 ms                                                         | 68.1 ms: 1.04x faster                                                           |
| pidigits                   | 203 ms                                                          | 197 ms: 1.03x faster                                                            |
| regex_dna                  | 122 ms                                                          | 118 ms: 1.03x faster                                                            |
| asyncio_tcp_ssl            | 17.1 sec                                                        | 16.7 sec: 1.02x faster                                                          |
| pickle                     | 7.99 us                                                         | 7.85 us: 1.02x faster                                                           |
| json_loads                 | 20.0 us                                                         | 20.0 us: 1.00x faster                                                           |
| python_startup             | 22.0 ms                                                         | 22.3 ms: 1.01x slower                                                           |
| gc_traversal               | 1.38 ms                                                         | 1.40 ms: 1.02x slower                                                           |
| pickle_list                | 3.27 us                                                         | 3.34 us: 1.02x slower                                                           |
| async_generators           | 260 ms                                                          | 267 ms: 1.03x slower                                                            |
| regex_effbot               | 1.82 ms                                                         | 1.90 ms: 1.04x slower                                                           |
| regex_v8                   | 15.2 ms                                                         | 15.8 ms: 1.04x slower                                                           |
| python_startup_no_site     | 18.8 ms                                                         | 19.7 ms: 1.05x slower                                                           |
| create_gc_cycles           | 618 us                                                          | 646 us: 1.05x slower                                                            |
| unpickle                   | 9.23 us                                                         | 9.75 us: 1.06x slower                                                           |
| pathlib                    | 79.9 ms                                                         | 86.3 ms: 1.08x slower                                                           |
| telco                      | 5.29 ms                                                         | 6.17 ms: 1.17x slower                                                           |
| sqlglot_normalize          | 113 ms                                                          | 196 ms: 1.73x slower                                                            |
| coverage                   | 58.0 ms                                                         | 476 ms: 8.20x slower                                                            |
| thrift                     | 801 us                                                          | 9.78 ms: 12.22x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.30x faster                                                                    |

Benchmark hidden because not significant (1): pickle_dict
Ignored benchmarks (7) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509.json: aiohttp, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.30x


# Memory

- memory change: unknown