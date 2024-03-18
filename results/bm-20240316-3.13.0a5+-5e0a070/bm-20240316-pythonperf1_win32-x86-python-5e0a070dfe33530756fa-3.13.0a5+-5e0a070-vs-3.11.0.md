# Results vs. 3.11.0

- fork: python
- ref: 5e0a070dfe33530756fa
- machine: windows-x86
- commit hash: 5e0a070
- commit date: 2024-03-16
- overall geometric mean: 1.30x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 282 ms                                                          | 230 ms: 1.23x faster                                                            |
| chameleon      | 8.08 ms                                                         | 5.50 ms: 1.47x faster                                                           |
| docutils       | 2.10 sec                                                        | 1.70 sec: 1.23x faster                                                          |
| html5lib       | 54.3 ms                                                         | 42.1 ms: 1.29x faster                                                           |
| tornado_http   | 118 ms                                                          | 93.8 ms: 1.26x faster                                                           |
| Geometric mean | (ref)                                                           | 1.29x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none            | 343 ms                                                          | 241 ms: 1.42x faster                                                            |
| async_tree_memoization     | 408 ms                                                          | 303 ms: 1.35x faster                                                            |
| async_tree_memoization_tg  | 378 ms                                                          | 284 ms: 1.33x faster                                                            |
| async_tree_io_tg           | 746 ms                                                          | 569 ms: 1.31x faster                                                            |
| async_tree_none_tg         | 301 ms                                                          | 230 ms: 1.31x faster                                                            |
| async_tree_io              | 754 ms                                                          | 585 ms: 1.29x faster                                                            |
| async_tree_cpu_io_mixed    | 590 ms                                                          | 497 ms: 1.19x faster                                                            |
| async_tree_cpu_io_mixed_tg | 577 ms                                                          | 500 ms: 1.15x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.29x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 126 ms                                                          | 75.2 ms: 1.68x faster                                                           |
| float          | 76.1 ms                                                         | 52.9 ms: 1.44x faster                                                           |
| pidigits       | 203 ms                                                          | 199 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                           | 1.35x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                          | 94.8 ms: 1.56x faster                                                           |
| regex_dna      | 122 ms                                                          | 117 ms: 1.04x faster                                                            |
| regex_effbot   | 1.82 ms                                                         | 1.90 ms: 1.04x slower                                                           |
| regex_v8       | 15.2 ms                                                         | 16.0 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                           | 1.10x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_pure_python | 231 us                                                          | 140 us: 1.65x faster                                                            |
| pickle_pure_python   | 309 us                                                          | 199 us: 1.55x faster                                                            |
| json_dumps           | 9.80 ms                                                         | 6.60 ms: 1.48x faster                                                           |
| tomli_loads          | 2.31 sec                                                        | 1.59 sec: 1.45x faster                                                          |
| xml_etree_process    | 55.0 ms                                                         | 41.0 ms: 1.34x faster                                                           |
| xml_etree_generate   | 71.6 ms                                                         | 58.0 ms: 1.24x faster                                                           |
| unpickle_list        | 3.28 us                                                         | 2.80 us: 1.17x faster                                                           |
| xml_etree_iterparse  | 75.6 ms                                                         | 65.2 ms: 1.16x faster                                                           |
| xml_etree_parse      | 114 ms                                                          | 107 ms: 1.06x faster                                                            |
| pickle_list          | 3.27 us                                                         | 3.20 us: 1.02x faster                                                           |
| json_loads           | 20.0 us                                                         | 19.8 us: 1.01x faster                                                           |
| pickle_dict          | 20.1 us                                                         | 19.9 us: 1.01x faster                                                           |
| unpickle             | 9.23 us                                                         | 9.81 us: 1.06x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.20x faster                                                                    |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 22.0 ms                                                         | 22.2 ms: 1.01x slower                                                           |
| python_startup_no_site | 18.8 ms                                                         | 19.8 ms: 1.06x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.03x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 26.8 ms                                                         | 17.7 ms: 1.51x faster                                                           |
| mako            | 10.3 ms                                                         | 6.82 ms: 1.51x faster                                                           |
| genshi_xml      | 61.2 ms                                                         | 41.2 ms: 1.49x faster                                                           |
| django_template | 37.4 ms                                                         | 27.9 ms: 1.34x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.46x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols   | 478 us                                                          | 87.8 us: 5.45x faster                                                           |
| generators                 | 52.2 ms                                                         | 21.9 ms: 2.38x faster                                                           |
| logging_silent             | 119 ns                                                          | 57.2 ns: 2.08x faster                                                           |
| comprehensions             | 22.1 us                                                         | 11.0 us: 2.00x faster                                                           |
| pylint                     | 418 ms                                                          | 214 ms: 1.95x faster                                                            |
| deltablue                  | 4.10 ms                                                         | 2.15 ms: 1.91x faster                                                           |
| richards_super             | 58.7 ms                                                         | 31.7 ms: 1.85x faster                                                           |
| spectral_norm              | 122 ms                                                          | 66.4 ms: 1.83x faster                                                           |
| deepcopy_memo              | 40.0 us                                                         | 22.4 us: 1.79x faster                                                           |
| richards                   | 48.8 ms                                                         | 28.1 ms: 1.74x faster                                                           |
| sqlglot_parse              | 1.49 ms                                                         | 857 us: 1.74x faster                                                            |
| hexiom                     | 7.51 ms                                                         | 4.32 ms: 1.74x faster                                                           |
| scimark_sor                | 135 ms                                                          | 77.9 ms: 1.74x faster                                                           |
| scimark_lu                 | 102 ms                                                          | 58.9 ms: 1.74x faster                                                           |
| chaos                      | 84.4 ms                                                         | 48.7 ms: 1.73x faster                                                           |
| raytrace                   | 327 ms                                                          | 191 ms: 1.71x faster                                                            |
| coroutines                 | 23.7 ms                                                         | 14.1 ms: 1.68x faster                                                           |
| nbody                      | 126 ms                                                          | 75.2 ms: 1.68x faster                                                           |
| unpack_sequence            | 65.2 ns                                                         | 39.2 ns: 1.67x faster                                                           |
| unpickle_pure_python       | 231 us                                                          | 140 us: 1.65x faster                                                            |
| sqlglot_transpile          | 1.78 ms                                                         | 1.09 ms: 1.63x faster                                                           |
| nqueens                    | 111 ms                                                          | 69.2 ms: 1.61x faster                                                           |
| scimark_monte_carlo        | 70.8 ms                                                         | 44.1 ms: 1.61x faster                                                           |
| regex_compile              | 148 ms                                                          | 94.8 ms: 1.56x faster                                                           |
| pickle_pure_python         | 309 us                                                          | 199 us: 1.55x faster                                                            |
| go                         | 147 ms                                                          | 95.2 ms: 1.54x faster                                                           |
| sympy_sum                  | 149 ms                                                          | 97.6 ms: 1.53x faster                                                           |
| pyflate                    | 471 ms                                                          | 309 ms: 1.52x faster                                                            |
| genshi_text                | 26.8 ms                                                         | 17.7 ms: 1.51x faster                                                           |
| mako                       | 10.3 ms                                                         | 6.82 ms: 1.51x faster                                                           |
| pprint_pformat             | 1.70 sec                                                        | 1.13 sec: 1.50x faster                                                          |
| crypto_pyaes               | 79.4 ms                                                         | 53.0 ms: 1.50x faster                                                           |
| genshi_xml                 | 61.2 ms                                                         | 41.2 ms: 1.49x faster                                                           |
| json_dumps                 | 9.80 ms                                                         | 6.60 ms: 1.48x faster                                                           |
| deepcopy                   | 381 us                                                          | 258 us: 1.48x faster                                                            |
| pprint_safe_repr           | 819 ms                                                          | 556 ms: 1.47x faster                                                            |
| chameleon                  | 8.08 ms                                                         | 5.50 ms: 1.47x faster                                                           |
| sympy_str                  | 283 ms                                                          | 194 ms: 1.46x faster                                                            |
| logging_simple             | 10.8 us                                                         | 7.41 us: 1.46x faster                                                           |
| fannkuch                   | 399 ms                                                          | 274 ms: 1.46x faster                                                            |
| deepcopy_reduce            | 3.32 us                                                         | 2.27 us: 1.46x faster                                                           |
| tomli_loads                | 2.31 sec                                                        | 1.59 sec: 1.45x faster                                                          |
| scimark_sparse_mat_mult    | 4.23 ms                                                         | 2.91 ms: 1.45x faster                                                           |
| scimark_fft                | 291 ms                                                          | 202 ms: 1.44x faster                                                            |
| float                      | 76.1 ms                                                         | 52.9 ms: 1.44x faster                                                           |
| sympy_integrate            | 19.9 ms                                                         | 13.9 ms: 1.44x faster                                                           |
| logging_format             | 11.5 us                                                         | 8.00 us: 1.43x faster                                                           |
| async_tree_none            | 343 ms                                                          | 241 ms: 1.42x faster                                                            |
| sqlglot_optimize           | 51.8 ms                                                         | 37.6 ms: 1.38x faster                                                           |
| sympy_expand               | 462 ms                                                          | 337 ms: 1.37x faster                                                            |
| async_tree_memoization     | 408 ms                                                          | 303 ms: 1.35x faster                                                            |
| django_template            | 37.4 ms                                                         | 27.9 ms: 1.34x faster                                                           |
| xml_etree_process          | 55.0 ms                                                         | 41.0 ms: 1.34x faster                                                           |
| async_tree_memoization_tg  | 378 ms                                                          | 284 ms: 1.33x faster                                                            |
| async_tree_io_tg           | 746 ms                                                          | 569 ms: 1.31x faster                                                            |
| async_tree_none_tg         | 301 ms                                                          | 230 ms: 1.31x faster                                                            |
| pycparser                  | 1.04 sec                                                        | 802 ms: 1.30x faster                                                            |
| mdp                        | 2.07 sec                                                        | 1.60 sec: 1.29x faster                                                          |
| html5lib                   | 54.3 ms                                                         | 42.1 ms: 1.29x faster                                                           |
| async_tree_io              | 754 ms                                                          | 585 ms: 1.29x faster                                                            |
| asyncio_tcp                | 787 ms                                                          | 623 ms: 1.26x faster                                                            |
| tornado_http               | 118 ms                                                          | 93.8 ms: 1.26x faster                                                           |
| xml_etree_generate         | 71.6 ms                                                         | 58.0 ms: 1.24x faster                                                           |
| docutils                   | 2.10 sec                                                        | 1.70 sec: 1.23x faster                                                          |
| 2to3                       | 282 ms                                                          | 230 ms: 1.23x faster                                                            |
| meteor_contest             | 90.9 ms                                                         | 75.7 ms: 1.20x faster                                                           |
| async_tree_cpu_io_mixed    | 590 ms                                                          | 497 ms: 1.19x faster                                                            |
| bench_thread_pool          | 1.14 ms                                                         | 968 us: 1.17x faster                                                            |
| unpickle_list              | 3.28 us                                                         | 2.80 us: 1.17x faster                                                           |
| xml_etree_iterparse        | 75.6 ms                                                         | 65.2 ms: 1.16x faster                                                           |
| async_tree_cpu_io_mixed_tg | 577 ms                                                          | 500 ms: 1.15x faster                                                            |
| json                       | 4.78 ms                                                         | 4.15 ms: 1.15x faster                                                           |
| sqlite_synth               | 2.15 us                                                         | 1.91 us: 1.13x faster                                                           |
| xml_etree_parse            | 114 ms                                                          | 107 ms: 1.06x faster                                                            |
| bench_mp_pool              | 70.9 ms                                                         | 68.0 ms: 1.04x faster                                                           |
| regex_dna                  | 122 ms                                                          | 117 ms: 1.04x faster                                                            |
| pickle_list                | 3.27 us                                                         | 3.20 us: 1.02x faster                                                           |
| pidigits                   | 203 ms                                                          | 199 ms: 1.02x faster                                                            |
| asyncio_tcp_ssl            | 17.1 sec                                                        | 16.7 sec: 1.02x faster                                                          |
| json_loads                 | 20.0 us                                                         | 19.8 us: 1.01x faster                                                           |
| pickle_dict                | 20.1 us                                                         | 19.9 us: 1.01x faster                                                           |
| python_startup             | 22.0 ms                                                         | 22.2 ms: 1.01x slower                                                           |
| async_generators           | 260 ms                                                          | 264 ms: 1.02x slower                                                            |
| create_gc_cycles           | 618 us                                                          | 638 us: 1.03x slower                                                            |
| regex_effbot               | 1.82 ms                                                         | 1.90 ms: 1.04x slower                                                           |
| regex_v8                   | 15.2 ms                                                         | 16.0 ms: 1.05x slower                                                           |
| python_startup_no_site     | 18.8 ms                                                         | 19.8 ms: 1.06x slower                                                           |
| unpickle                   | 9.23 us                                                         | 9.81 us: 1.06x slower                                                           |
| pathlib                    | 79.9 ms                                                         | 85.7 ms: 1.07x slower                                                           |
| telco                      | 5.29 ms                                                         | 5.75 ms: 1.09x slower                                                           |
| sqlglot_normalize          | 113 ms                                                          | 192 ms: 1.70x slower                                                            |
| coverage                   | 58.0 ms                                                         | 453 ms: 7.81x slower                                                            |
| thrift                     | 801 us                                                          | 9.64 ms: 12.04x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.30x faster                                                                    |

Benchmark hidden because not significant (2): pickle, gc_traversal
Ignored benchmarks (7) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509.json: aiohttp, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.28x


# Memory

- memory change: unknown