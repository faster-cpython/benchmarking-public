# Results vs. 3.11.0

- fork: python
- ref: 8c094c3095feb4de2efe
- machine: windows-x86
- commit hash: 8c094c3
- commit date: 2024-03-13
- overall geometric mean: 1.17x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240313-pythonperf1_win32-x86-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 282 ms                                                          | 258 ms: 1.09x faster                                                            |
| chameleon      | 8.08 ms                                                         | 5.67 ms: 1.42x faster                                                           |
| docutils       | 2.10 sec                                                        | 1.83 sec: 1.15x faster                                                          |
| html5lib       | 54.3 ms                                                         | 46.0 ms: 1.18x faster                                                           |
| tornado_http   | 118 ms                                                          | 96.2 ms: 1.23x faster                                                           |
| Geometric mean | (ref)                                                           | 1.21x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240313-pythonperf1_win32-x86-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none            | 343 ms                                                          | 256 ms: 1.34x faster                                                            |
| async_tree_memoization     | 408 ms                                                          | 319 ms: 1.28x faster                                                            |
| async_tree_memoization_tg  | 378 ms                                                          | 302 ms: 1.25x faster                                                            |
| async_tree_none_tg         | 301 ms                                                          | 241 ms: 1.25x faster                                                            |
| async_tree_io_tg           | 746 ms                                                          | 600 ms: 1.24x faster                                                            |
| async_tree_io              | 754 ms                                                          | 618 ms: 1.22x faster                                                            |
| async_tree_cpu_io_mixed_tg | 577 ms                                                          | 493 ms: 1.17x faster                                                            |
| async_tree_cpu_io_mixed    | 590 ms                                                          | 507 ms: 1.16x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.24x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240313-pythonperf1_win32-x86-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 76.1 ms                                                         | 53.9 ms: 1.41x faster                                                           |
| nbody          | 126 ms                                                          | 95.1 ms: 1.32x faster                                                           |
| pidigits       | 203 ms                                                          | 198 ms: 1.03x faster                                                            |
| Geometric mean | (ref)                                                           | 1.24x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240313-pythonperf1_win32-x86-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                          | 109 ms: 1.36x faster                                                            |
| regex_effbot   | 1.82 ms                                                         | 1.89 ms: 1.04x slower                                                           |
| regex_v8       | 15.2 ms                                                         | 16.0 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                    |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240313-pythonperf1_win32-x86-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 309 us                                                          | 210 us: 1.47x faster                                                            |
| json_dumps           | 9.80 ms                                                         | 6.91 ms: 1.42x faster                                                           |
| unpickle_pure_python | 231 us                                                          | 167 us: 1.39x faster                                                            |
| tomli_loads          | 2.31 sec                                                        | 1.71 sec: 1.35x faster                                                          |
| xml_etree_process    | 55.0 ms                                                         | 42.7 ms: 1.29x faster                                                           |
| xml_etree_generate   | 71.6 ms                                                         | 61.7 ms: 1.16x faster                                                           |
| unpickle_list        | 3.28 us                                                         | 2.88 us: 1.14x faster                                                           |
| xml_etree_iterparse  | 75.6 ms                                                         | 67.4 ms: 1.12x faster                                                           |
| xml_etree_parse      | 114 ms                                                          | 108 ms: 1.06x faster                                                            |
| json_loads           | 20.0 us                                                         | 19.8 us: 1.01x faster                                                           |
| pickle               | 7.99 us                                                         | 7.89 us: 1.01x faster                                                           |
| pickle_dict          | 20.1 us                                                         | 20.0 us: 1.01x faster                                                           |
| pickle_list          | 3.27 us                                                         | 3.31 us: 1.01x slower                                                           |
| unpickle             | 9.23 us                                                         | 10.2 us: 1.10x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.15x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240313-pythonperf1_win32-x86-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 22.0 ms                                                         | 26.4 ms: 1.20x slower                                                           |
| python_startup_no_site | 18.8 ms                                                         | 23.9 ms: 1.27x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.23x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240313-pythonperf1_win32-x86-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 10.3 ms                                                         | 6.94 ms: 1.48x faster                                                           |
| django_template | 37.4 ms                                                         | 30.0 ms: 1.25x faster                                                           |
| genshi_xml      | 61.2 ms                                                         | 49.7 ms: 1.23x faster                                                           |
| genshi_text     | 26.8 ms                                                         | 22.7 ms: 1.18x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.28x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240313-pythonperf1_win32-x86-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols   | 478 us                                                          | 96.4 us: 4.96x faster                                                           |
| generators                 | 52.2 ms                                                         | 22.2 ms: 2.35x faster                                                           |
| logging_silent             | 119 ns                                                          | 61.1 ns: 1.95x faster                                                           |
| pylint                     | 418 ms                                                          | 228 ms: 1.84x faster                                                            |
| spectral_norm              | 122 ms                                                          | 72.2 ms: 1.68x faster                                                           |
| coroutines                 | 23.7 ms                                                         | 14.2 ms: 1.68x faster                                                           |
| deepcopy_memo              | 40.0 us                                                         | 24.2 us: 1.66x faster                                                           |
| deltablue                  | 4.10 ms                                                         | 2.55 ms: 1.61x faster                                                           |
| sqlglot_parse              | 1.49 ms                                                         | 960 us: 1.55x faster                                                            |
| richards_super             | 58.7 ms                                                         | 39.0 ms: 1.50x faster                                                           |
| comprehensions             | 22.1 us                                                         | 14.7 us: 1.50x faster                                                           |
| unpack_sequence            | 65.2 ns                                                         | 43.7 ns: 1.49x faster                                                           |
| mako                       | 10.3 ms                                                         | 6.94 ms: 1.48x faster                                                           |
| sqlglot_transpile          | 1.78 ms                                                         | 1.21 ms: 1.48x faster                                                           |
| pickle_pure_python         | 309 us                                                          | 210 us: 1.47x faster                                                            |
| chaos                      | 84.4 ms                                                         | 58.8 ms: 1.44x faster                                                           |
| scimark_sor                | 135 ms                                                          | 94.8 ms: 1.43x faster                                                           |
| chameleon                  | 8.08 ms                                                         | 5.67 ms: 1.42x faster                                                           |
| json_dumps                 | 9.80 ms                                                         | 6.91 ms: 1.42x faster                                                           |
| float                      | 76.1 ms                                                         | 53.9 ms: 1.41x faster                                                           |
| richards                   | 48.8 ms                                                         | 34.7 ms: 1.41x faster                                                           |
| unpickle_pure_python       | 231 us                                                          | 167 us: 1.39x faster                                                            |
| sympy_sum                  | 149 ms                                                          | 108 ms: 1.38x faster                                                            |
| deepcopy                   | 381 us                                                          | 279 us: 1.37x faster                                                            |
| regex_compile              | 148 ms                                                          | 109 ms: 1.36x faster                                                            |
| tomli_loads                | 2.31 sec                                                        | 1.71 sec: 1.35x faster                                                          |
| deepcopy_reduce            | 3.32 us                                                         | 2.46 us: 1.35x faster                                                           |
| async_tree_none            | 343 ms                                                          | 256 ms: 1.34x faster                                                            |
| sympy_str                  | 283 ms                                                          | 212 ms: 1.34x faster                                                            |
| nbody                      | 126 ms                                                          | 95.1 ms: 1.32x faster                                                           |
| scimark_sparse_mat_mult    | 4.23 ms                                                         | 3.20 ms: 1.32x faster                                                           |
| logging_simple             | 10.8 us                                                         | 8.21 us: 1.32x faster                                                           |
| logging_format             | 11.5 us                                                         | 8.82 us: 1.30x faster                                                           |
| crypto_pyaes               | 79.4 ms                                                         | 61.3 ms: 1.30x faster                                                           |
| xml_etree_process          | 55.0 ms                                                         | 42.7 ms: 1.29x faster                                                           |
| sympy_integrate            | 19.9 ms                                                         | 15.4 ms: 1.29x faster                                                           |
| async_tree_memoization     | 408 ms                                                          | 319 ms: 1.28x faster                                                            |
| pyflate                    | 471 ms                                                          | 374 ms: 1.26x faster                                                            |
| asyncio_tcp                | 787 ms                                                          | 628 ms: 1.25x faster                                                            |
| async_tree_memoization_tg  | 378 ms                                                          | 302 ms: 1.25x faster                                                            |
| async_tree_none_tg         | 301 ms                                                          | 241 ms: 1.25x faster                                                            |
| sympy_expand               | 462 ms                                                          | 370 ms: 1.25x faster                                                            |
| django_template            | 37.4 ms                                                         | 30.0 ms: 1.25x faster                                                           |
| async_tree_io_tg           | 746 ms                                                          | 600 ms: 1.24x faster                                                            |
| hexiom                     | 7.51 ms                                                         | 6.04 ms: 1.24x faster                                                           |
| nqueens                    | 111 ms                                                          | 90.0 ms: 1.24x faster                                                           |
| fannkuch                   | 399 ms                                                          | 324 ms: 1.23x faster                                                            |
| genshi_xml                 | 61.2 ms                                                         | 49.7 ms: 1.23x faster                                                           |
| raytrace                   | 327 ms                                                          | 266 ms: 1.23x faster                                                            |
| tornado_http               | 118 ms                                                          | 96.2 ms: 1.23x faster                                                           |
| scimark_fft                | 291 ms                                                          | 239 ms: 1.22x faster                                                            |
| async_tree_io              | 754 ms                                                          | 618 ms: 1.22x faster                                                            |
| pycparser                  | 1.04 sec                                                        | 860 ms: 1.21x faster                                                            |
| scimark_lu                 | 102 ms                                                          | 84.3 ms: 1.21x faster                                                           |
| mdp                        | 2.07 sec                                                        | 1.71 sec: 1.21x faster                                                          |
| go                         | 147 ms                                                          | 123 ms: 1.20x faster                                                            |
| html5lib                   | 54.3 ms                                                         | 46.0 ms: 1.18x faster                                                           |
| genshi_text                | 26.8 ms                                                         | 22.7 ms: 1.18x faster                                                           |
| json                       | 4.78 ms                                                         | 4.08 ms: 1.17x faster                                                           |
| async_tree_cpu_io_mixed_tg | 577 ms                                                          | 493 ms: 1.17x faster                                                            |
| async_tree_cpu_io_mixed    | 590 ms                                                          | 507 ms: 1.16x faster                                                            |
| xml_etree_generate         | 71.6 ms                                                         | 61.7 ms: 1.16x faster                                                           |
| docutils                   | 2.10 sec                                                        | 1.83 sec: 1.15x faster                                                          |
| pprint_pformat             | 1.70 sec                                                        | 1.49 sec: 1.14x faster                                                          |
| unpickle_list              | 3.28 us                                                         | 2.88 us: 1.14x faster                                                           |
| pprint_safe_repr           | 819 ms                                                          | 722 ms: 1.13x faster                                                            |
| bench_thread_pool          | 1.14 ms                                                         | 1.01 ms: 1.13x faster                                                           |
| scimark_monte_carlo        | 70.8 ms                                                         | 63.0 ms: 1.12x faster                                                           |
| xml_etree_iterparse        | 75.6 ms                                                         | 67.4 ms: 1.12x faster                                                           |
| sqlglot_optimize           | 51.8 ms                                                         | 46.4 ms: 1.12x faster                                                           |
| sqlite_synth               | 2.15 us                                                         | 1.93 us: 1.11x faster                                                           |
| meteor_contest             | 90.9 ms                                                         | 82.2 ms: 1.11x faster                                                           |
| 2to3                       | 282 ms                                                          | 258 ms: 1.09x faster                                                            |
| xml_etree_parse            | 114 ms                                                          | 108 ms: 1.06x faster                                                            |
| pidigits                   | 203 ms                                                          | 198 ms: 1.03x faster                                                            |
| asyncio_tcp_ssl            | 17.1 sec                                                        | 16.8 sec: 1.02x faster                                                          |
| json_loads                 | 20.0 us                                                         | 19.8 us: 1.01x faster                                                           |
| pickle                     | 7.99 us                                                         | 7.89 us: 1.01x faster                                                           |
| pickle_dict                | 20.1 us                                                         | 20.0 us: 1.01x faster                                                           |
| pickle_list                | 3.27 us                                                         | 3.31 us: 1.01x slower                                                           |
| gc_traversal               | 1.38 ms                                                         | 1.40 ms: 1.02x slower                                                           |
| regex_effbot               | 1.82 ms                                                         | 1.89 ms: 1.04x slower                                                           |
| bench_mp_pool              | 70.9 ms                                                         | 74.6 ms: 1.05x slower                                                           |
| regex_v8                   | 15.2 ms                                                         | 16.0 ms: 1.06x slower                                                           |
| pathlib                    | 79.9 ms                                                         | 86.0 ms: 1.08x slower                                                           |
| create_gc_cycles           | 618 us                                                          | 667 us: 1.08x slower                                                            |
| unpickle                   | 9.23 us                                                         | 10.2 us: 1.10x slower                                                           |
| async_generators           | 260 ms                                                          | 297 ms: 1.14x slower                                                            |
| telco                      | 5.29 ms                                                         | 6.33 ms: 1.20x slower                                                           |
| python_startup             | 22.0 ms                                                         | 26.4 ms: 1.20x slower                                                           |
| python_startup_no_site     | 18.8 ms                                                         | 23.9 ms: 1.27x slower                                                           |
| sqlglot_normalize          | 113 ms                                                          | 227 ms: 2.01x slower                                                            |
| coverage                   | 58.0 ms                                                         | 495 ms: 8.53x slower                                                            |
| thrift                     | 801 us                                                          | 10.7 ms: 13.41x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.17x faster                                                                    |

Benchmark hidden because not significant (1): regex_dna
Ignored benchmarks (7) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509.json: aiohttp, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.16x


# Memory

- memory change: unknown