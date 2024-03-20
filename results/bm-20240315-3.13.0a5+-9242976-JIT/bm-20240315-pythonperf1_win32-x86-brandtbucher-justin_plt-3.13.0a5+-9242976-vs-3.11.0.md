# Results vs. 3.11.0

- fork: brandtbucher
- ref: justin_plt
- machine: windows-x86
- commit hash: 9242976
- commit date: 2024-03-15
- overall geometric mean: 1.15x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240315-pythonperf1_win32-x86-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 282 ms                                                          | 262 ms: 1.08x faster                                                        |
| chameleon      | 8.08 ms                                                         | 5.91 ms: 1.37x faster                                                       |
| docutils       | 2.10 sec                                                        | 1.87 sec: 1.12x faster                                                      |
| html5lib       | 54.3 ms                                                         | 46.4 ms: 1.17x faster                                                       |
| tornado_http   | 118 ms                                                          | 98.4 ms: 1.20x faster                                                       |
| Geometric mean | (ref)                                                           | 1.18x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240315-pythonperf1_win32-x86-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 343 ms                                                          | 261 ms: 1.32x faster                                                        |
| async_tree_memoization     | 408 ms                                                          | 320 ms: 1.27x faster                                                        |
| async_tree_memoization_tg  | 378 ms                                                          | 307 ms: 1.23x faster                                                        |
| async_tree_none_tg         | 301 ms                                                          | 245 ms: 1.23x faster                                                        |
| async_tree_io_tg           | 746 ms                                                          | 608 ms: 1.23x faster                                                        |
| async_tree_io              | 754 ms                                                          | 623 ms: 1.21x faster                                                        |
| async_tree_cpu_io_mixed_tg | 577 ms                                                          | 498 ms: 1.16x faster                                                        |
| async_tree_cpu_io_mixed    | 590 ms                                                          | 510 ms: 1.16x faster                                                        |
| Geometric mean             | (ref)                                                           | 1.22x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240315-pythonperf1_win32-x86-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.1 ms                                                         | 54.7 ms: 1.39x faster                                                       |
| nbody          | 126 ms                                                          | 98.8 ms: 1.27x faster                                                       |
| pidigits       | 203 ms                                                          | 199 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                           | 1.22x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240315-pythonperf1_win32-x86-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                          | 112 ms: 1.32x faster                                                        |
| regex_effbot   | 1.82 ms                                                         | 1.89 ms: 1.03x slower                                                       |
| regex_v8       | 15.2 ms                                                         | 16.2 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240315-pythonperf1_win32-x86-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.80 ms                                                         | 6.98 ms: 1.40x faster                                                       |
| pickle_pure_python   | 309 us                                                          | 224 us: 1.38x faster                                                        |
| tomli_loads          | 2.31 sec                                                        | 1.71 sec: 1.36x faster                                                      |
| unpickle_pure_python | 231 us                                                          | 174 us: 1.33x faster                                                        |
| xml_etree_process    | 55.0 ms                                                         | 45.2 ms: 1.22x faster                                                       |
| unpickle_list        | 3.28 us                                                         | 2.88 us: 1.14x faster                                                       |
| xml_etree_iterparse  | 75.6 ms                                                         | 67.0 ms: 1.13x faster                                                       |
| xml_etree_generate   | 71.6 ms                                                         | 64.0 ms: 1.12x faster                                                       |
| xml_etree_parse      | 114 ms                                                          | 107 ms: 1.06x faster                                                        |
| pickle_list          | 3.27 us                                                         | 3.19 us: 1.02x faster                                                       |
| pickle_dict          | 20.1 us                                                         | 20.0 us: 1.01x faster                                                       |
| pickle               | 7.99 us                                                         | 8.02 us: 1.00x slower                                                       |
| unpickle             | 9.23 us                                                         | 10.2 us: 1.11x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.14x faster                                                                |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240315-pythonperf1_win32-x86-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 22.0 ms                                                         | 25.8 ms: 1.17x slower                                                       |
| python_startup_no_site | 18.8 ms                                                         | 23.6 ms: 1.26x slower                                                       |
| Geometric mean         | (ref)                                                           | 1.21x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240315-pythonperf1_win32-x86-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.3 ms                                                         | 6.88 ms: 1.49x faster                                                       |
| genshi_xml      | 61.2 ms                                                         | 50.9 ms: 1.20x faster                                                       |
| django_template | 37.4 ms                                                         | 31.7 ms: 1.18x faster                                                       |
| genshi_text     | 26.8 ms                                                         | 23.4 ms: 1.14x faster                                                       |
| Geometric mean  | (ref)                                                           | 1.25x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240315-pythonperf1_win32-x86-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols   | 478 us                                                          | 99.4 us: 4.81x faster                                                       |
| generators                 | 52.2 ms                                                         | 24.3 ms: 2.14x faster                                                       |
| pylint                     | 418 ms                                                          | 235 ms: 1.78x faster                                                        |
| logging_silent             | 119 ns                                                          | 67.8 ns: 1.76x faster                                                       |
| spectral_norm              | 122 ms                                                          | 73.2 ms: 1.66x faster                                                       |
| coroutines                 | 23.7 ms                                                         | 15.0 ms: 1.58x faster                                                       |
| deltablue                  | 4.10 ms                                                         | 2.69 ms: 1.52x faster                                                       |
| mako                       | 10.3 ms                                                         | 6.88 ms: 1.49x faster                                                       |
| comprehensions             | 22.1 us                                                         | 14.9 us: 1.48x faster                                                       |
| unpack_sequence            | 65.2 ns                                                         | 44.0 ns: 1.48x faster                                                       |
| sqlglot_parse              | 1.49 ms                                                         | 1.01 ms: 1.48x faster                                                       |
| deepcopy_memo              | 40.0 us                                                         | 27.1 us: 1.48x faster                                                       |
| richards_super             | 58.7 ms                                                         | 40.8 ms: 1.44x faster                                                       |
| chaos                      | 84.4 ms                                                         | 59.1 ms: 1.43x faster                                                       |
| sqlglot_transpile          | 1.78 ms                                                         | 1.27 ms: 1.41x faster                                                       |
| json_dumps                 | 9.80 ms                                                         | 6.98 ms: 1.40x faster                                                       |
| float                      | 76.1 ms                                                         | 54.7 ms: 1.39x faster                                                       |
| pickle_pure_python         | 309 us                                                          | 224 us: 1.38x faster                                                        |
| chameleon                  | 8.08 ms                                                         | 5.91 ms: 1.37x faster                                                       |
| scimark_sparse_mat_mult    | 4.23 ms                                                         | 3.11 ms: 1.36x faster                                                       |
| tomli_loads                | 2.31 sec                                                        | 1.71 sec: 1.36x faster                                                      |
| richards                   | 48.8 ms                                                         | 36.0 ms: 1.36x faster                                                       |
| unpickle_pure_python       | 231 us                                                          | 174 us: 1.33x faster                                                        |
| sympy_sum                  | 149 ms                                                          | 112 ms: 1.32x faster                                                        |
| regex_compile              | 148 ms                                                          | 112 ms: 1.32x faster                                                        |
| crypto_pyaes               | 79.4 ms                                                         | 60.2 ms: 1.32x faster                                                       |
| async_tree_none            | 343 ms                                                          | 261 ms: 1.32x faster                                                        |
| deepcopy                   | 381 us                                                          | 291 us: 1.31x faster                                                        |
| logging_simple             | 10.8 us                                                         | 8.31 us: 1.30x faster                                                       |
| sympy_str                  | 283 ms                                                          | 220 ms: 1.29x faster                                                        |
| scimark_sor                | 135 ms                                                          | 106 ms: 1.28x faster                                                        |
| logging_format             | 11.5 us                                                         | 8.96 us: 1.28x faster                                                       |
| deepcopy_reduce            | 3.32 us                                                         | 2.60 us: 1.28x faster                                                       |
| nbody                      | 126 ms                                                          | 98.8 ms: 1.27x faster                                                       |
| async_tree_memoization     | 408 ms                                                          | 320 ms: 1.27x faster                                                        |
| pyflate                    | 471 ms                                                          | 377 ms: 1.25x faster                                                        |
| sympy_integrate            | 19.9 ms                                                         | 16.0 ms: 1.25x faster                                                       |
| async_tree_memoization_tg  | 378 ms                                                          | 307 ms: 1.23x faster                                                        |
| async_tree_none_tg         | 301 ms                                                          | 245 ms: 1.23x faster                                                        |
| async_tree_io_tg           | 746 ms                                                          | 608 ms: 1.23x faster                                                        |
| asyncio_tcp                | 787 ms                                                          | 641 ms: 1.23x faster                                                        |
| scimark_fft                | 291 ms                                                          | 237 ms: 1.23x faster                                                        |
| hexiom                     | 7.51 ms                                                         | 6.12 ms: 1.23x faster                                                       |
| raytrace                   | 327 ms                                                          | 269 ms: 1.22x faster                                                        |
| xml_etree_process          | 55.0 ms                                                         | 45.2 ms: 1.22x faster                                                       |
| async_tree_io              | 754 ms                                                          | 623 ms: 1.21x faster                                                        |
| genshi_xml                 | 61.2 ms                                                         | 50.9 ms: 1.20x faster                                                       |
| tornado_http               | 118 ms                                                          | 98.4 ms: 1.20x faster                                                       |
| sympy_expand               | 462 ms                                                          | 388 ms: 1.19x faster                                                        |
| pycparser                  | 1.04 sec                                                        | 878 ms: 1.19x faster                                                        |
| fannkuch                   | 399 ms                                                          | 338 ms: 1.18x faster                                                        |
| django_template            | 37.4 ms                                                         | 31.7 ms: 1.18x faster                                                       |
| go                         | 147 ms                                                          | 125 ms: 1.17x faster                                                        |
| mdp                        | 2.07 sec                                                        | 1.76 sec: 1.17x faster                                                      |
| nqueens                    | 111 ms                                                          | 95.0 ms: 1.17x faster                                                       |
| html5lib                   | 54.3 ms                                                         | 46.4 ms: 1.17x faster                                                       |
| async_tree_cpu_io_mixed_tg | 577 ms                                                          | 498 ms: 1.16x faster                                                        |
| async_tree_cpu_io_mixed    | 590 ms                                                          | 510 ms: 1.16x faster                                                        |
| scimark_lu                 | 102 ms                                                          | 88.9 ms: 1.15x faster                                                       |
| genshi_text                | 26.8 ms                                                         | 23.4 ms: 1.14x faster                                                       |
| unpickle_list              | 3.28 us                                                         | 2.88 us: 1.14x faster                                                       |
| json                       | 4.78 ms                                                         | 4.21 ms: 1.14x faster                                                       |
| sqlite_synth               | 2.15 us                                                         | 1.89 us: 1.13x faster                                                       |
| xml_etree_iterparse        | 75.6 ms                                                         | 67.0 ms: 1.13x faster                                                       |
| docutils                   | 2.10 sec                                                        | 1.87 sec: 1.12x faster                                                      |
| xml_etree_generate         | 71.6 ms                                                         | 64.0 ms: 1.12x faster                                                       |
| pprint_pformat             | 1.70 sec                                                        | 1.52 sec: 1.12x faster                                                      |
| scimark_monte_carlo        | 70.8 ms                                                         | 64.0 ms: 1.11x faster                                                       |
| pprint_safe_repr           | 819 ms                                                          | 746 ms: 1.10x faster                                                        |
| meteor_contest             | 90.9 ms                                                         | 82.9 ms: 1.10x faster                                                       |
| bench_thread_pool          | 1.14 ms                                                         | 1.04 ms: 1.09x faster                                                       |
| sqlglot_optimize           | 51.8 ms                                                         | 48.0 ms: 1.08x faster                                                       |
| 2to3                       | 282 ms                                                          | 262 ms: 1.08x faster                                                        |
| xml_etree_parse            | 114 ms                                                          | 107 ms: 1.06x faster                                                        |
| pickle_list                | 3.27 us                                                         | 3.19 us: 1.02x faster                                                       |
| pidigits                   | 203 ms                                                          | 199 ms: 1.02x faster                                                        |
| asyncio_tcp_ssl            | 17.1 sec                                                        | 16.7 sec: 1.02x faster                                                      |
| pickle_dict                | 20.1 us                                                         | 20.0 us: 1.01x faster                                                       |
| pickle                     | 7.99 us                                                         | 8.02 us: 1.00x slower                                                       |
| gc_traversal               | 1.38 ms                                                         | 1.42 ms: 1.03x slower                                                       |
| regex_effbot               | 1.82 ms                                                         | 1.89 ms: 1.03x slower                                                       |
| bench_mp_pool              | 70.9 ms                                                         | 74.7 ms: 1.05x slower                                                       |
| regex_v8                   | 15.2 ms                                                         | 16.2 ms: 1.07x slower                                                       |
| create_gc_cycles           | 618 us                                                          | 661 us: 1.07x slower                                                        |
| pathlib                    | 79.9 ms                                                         | 86.1 ms: 1.08x slower                                                       |
| unpickle                   | 9.23 us                                                         | 10.2 us: 1.11x slower                                                       |
| async_generators           | 260 ms                                                          | 292 ms: 1.12x slower                                                        |
| python_startup             | 22.0 ms                                                         | 25.8 ms: 1.17x slower                                                       |
| telco                      | 5.29 ms                                                         | 6.62 ms: 1.25x slower                                                       |
| python_startup_no_site     | 18.8 ms                                                         | 23.6 ms: 1.26x slower                                                       |
| sqlglot_normalize          | 113 ms                                                          | 241 ms: 2.13x slower                                                        |
| coverage                   | 58.0 ms                                                         | 489 ms: 8.42x slower                                                        |
| thrift                     | 801 us                                                          | 10.9 ms: 13.61x slower                                                      |
| Geometric mean             | (ref)                                                           | 1.15x faster                                                                |

Benchmark hidden because not significant (2): regex_dna, json_loads
Ignored benchmarks (7) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509.json: aiohttp, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.14x


# Memory

- memory change: unknown