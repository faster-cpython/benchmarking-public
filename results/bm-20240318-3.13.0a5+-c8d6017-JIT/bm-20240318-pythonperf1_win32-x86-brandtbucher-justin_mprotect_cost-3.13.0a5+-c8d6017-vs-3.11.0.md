# Results vs. 3.11.0

- fork: brandtbucher
- ref: justin_mprotect_cost
- machine: windows-x86
- commit hash: c8d6017
- commit date: 2024-03-18
- overall geometric mean: 1.17x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240318-pythonperf1_win32-x86-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 282 ms                                                          | 255 ms: 1.11x faster                                                                  |
| chameleon      | 8.08 ms                                                         | 5.84 ms: 1.38x faster                                                                 |
| docutils       | 2.10 sec                                                        | 1.81 sec: 1.16x faster                                                                |
| html5lib       | 54.3 ms                                                         | 44.9 ms: 1.21x faster                                                                 |
| tornado_http   | 118 ms                                                          | 95.9 ms: 1.23x faster                                                                 |
| Geometric mean | (ref)                                                           | 1.22x faster                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240318-pythonperf1_win32-x86-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_none            | 343 ms                                                          | 258 ms: 1.33x faster                                                                  |
| async_tree_memoization     | 408 ms                                                          | 320 ms: 1.28x faster                                                                  |
| async_tree_io_tg           | 746 ms                                                          | 598 ms: 1.25x faster                                                                  |
| async_tree_none_tg         | 301 ms                                                          | 242 ms: 1.24x faster                                                                  |
| async_tree_memoization_tg  | 378 ms                                                          | 306 ms: 1.23x faster                                                                  |
| async_tree_io              | 754 ms                                                          | 616 ms: 1.22x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 577 ms                                                          | 505 ms: 1.14x faster                                                                  |
| async_tree_cpu_io_mixed    | 590 ms                                                          | 519 ms: 1.14x faster                                                                  |
| Geometric mean             | (ref)                                                           | 1.23x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240318-pythonperf1_win32-x86-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| float          | 76.1 ms                                                         | 55.4 ms: 1.37x faster                                                                 |
| nbody          | 126 ms                                                          | 95.9 ms: 1.31x faster                                                                 |
| pidigits       | 203 ms                                                          | 199 ms: 1.02x faster                                                                  |
| Geometric mean | (ref)                                                           | 1.23x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240318-pythonperf1_win32-x86-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                          | 108 ms: 1.37x faster                                                                  |
| regex_dna      | 122 ms                                                          | 121 ms: 1.01x faster                                                                  |
| regex_effbot   | 1.82 ms                                                         | 1.89 ms: 1.04x slower                                                                 |
| regex_v8       | 15.2 ms                                                         | 16.2 ms: 1.06x slower                                                                 |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240318-pythonperf1_win32-x86-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| pickle_pure_python   | 309 us                                                          | 209 us: 1.48x faster                                                                  |
| unpickle_pure_python | 231 us                                                          | 164 us: 1.41x faster                                                                  |
| json_dumps           | 9.80 ms                                                         | 7.07 ms: 1.39x faster                                                                 |
| tomli_loads          | 2.31 sec                                                        | 1.68 sec: 1.38x faster                                                                |
| xml_etree_process    | 55.0 ms                                                         | 42.8 ms: 1.28x faster                                                                 |
| xml_etree_generate   | 71.6 ms                                                         | 62.0 ms: 1.16x faster                                                                 |
| xml_etree_iterparse  | 75.6 ms                                                         | 67.0 ms: 1.13x faster                                                                 |
| unpickle_list        | 3.28 us                                                         | 2.93 us: 1.12x faster                                                                 |
| xml_etree_parse      | 114 ms                                                          | 108 ms: 1.06x faster                                                                  |
| pickle_dict          | 20.1 us                                                         | 19.8 us: 1.02x faster                                                                 |
| json_loads           | 20.0 us                                                         | 19.8 us: 1.01x faster                                                                 |
| pickle               | 7.99 us                                                         | 8.03 us: 1.01x slower                                                                 |
| unpickle             | 9.23 us                                                         | 9.96 us: 1.08x slower                                                                 |
| Geometric mean       | (ref)                                                           | 1.15x faster                                                                          |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240318-pythonperf1_win32-x86-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 22.0 ms                                                         | 25.1 ms: 1.14x slower                                                                 |
| python_startup_no_site | 18.8 ms                                                         | 23.0 ms: 1.22x slower                                                                 |
| Geometric mean         | (ref)                                                           | 1.18x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240318-pythonperf1_win32-x86-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako            | 10.3 ms                                                         | 7.00 ms: 1.47x faster                                                                 |
| django_template | 37.4 ms                                                         | 29.1 ms: 1.28x faster                                                                 |
| genshi_xml      | 61.2 ms                                                         | 48.5 ms: 1.26x faster                                                                 |
| genshi_text     | 26.8 ms                                                         | 21.8 ms: 1.23x faster                                                                 |
| Geometric mean  | (ref)                                                           | 1.31x faster                                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240318-pythonperf1_win32-x86-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| typing_runtime_protocols   | 478 us                                                          | 97.7 us: 4.90x faster                                                                 |
| generators                 | 52.2 ms                                                         | 22.2 ms: 2.35x faster                                                                 |
| logging_silent             | 119 ns                                                          | 60.0 ns: 1.99x faster                                                                 |
| pylint                     | 418 ms                                                          | 227 ms: 1.84x faster                                                                  |
| coroutines                 | 23.7 ms                                                         | 14.0 ms: 1.70x faster                                                                 |
| spectral_norm              | 122 ms                                                          | 71.7 ms: 1.70x faster                                                                 |
| deltablue                  | 4.10 ms                                                         | 2.49 ms: 1.65x faster                                                                 |
| deepcopy_memo              | 40.0 us                                                         | 24.4 us: 1.64x faster                                                                 |
| richards_super             | 58.7 ms                                                         | 37.7 ms: 1.56x faster                                                                 |
| sqlglot_parse              | 1.49 ms                                                         | 972 us: 1.53x faster                                                                  |
| comprehensions             | 22.1 us                                                         | 14.6 us: 1.51x faster                                                                 |
| pickle_pure_python         | 309 us                                                          | 209 us: 1.48x faster                                                                  |
| mako                       | 10.3 ms                                                         | 7.00 ms: 1.47x faster                                                                 |
| sqlglot_transpile          | 1.78 ms                                                         | 1.22 ms: 1.46x faster                                                                 |
| richards                   | 48.8 ms                                                         | 33.8 ms: 1.44x faster                                                                 |
| unpack_sequence            | 65.2 ns                                                         | 45.2 ns: 1.44x faster                                                                 |
| unpickle_pure_python       | 231 us                                                          | 164 us: 1.41x faster                                                                  |
| chaos                      | 84.4 ms                                                         | 60.1 ms: 1.40x faster                                                                 |
| sympy_sum                  | 149 ms                                                          | 107 ms: 1.39x faster                                                                  |
| json_dumps                 | 9.80 ms                                                         | 7.07 ms: 1.39x faster                                                                 |
| scimark_sor                | 135 ms                                                          | 97.7 ms: 1.38x faster                                                                 |
| chameleon                  | 8.08 ms                                                         | 5.84 ms: 1.38x faster                                                                 |
| tomli_loads                | 2.31 sec                                                        | 1.68 sec: 1.38x faster                                                                |
| float                      | 76.1 ms                                                         | 55.4 ms: 1.37x faster                                                                 |
| regex_compile              | 148 ms                                                          | 108 ms: 1.37x faster                                                                  |
| scimark_sparse_mat_mult    | 4.23 ms                                                         | 3.11 ms: 1.36x faster                                                                 |
| deepcopy                   | 381 us                                                          | 281 us: 1.36x faster                                                                  |
| deepcopy_reduce            | 3.32 us                                                         | 2.45 us: 1.35x faster                                                                 |
| logging_simple             | 10.8 us                                                         | 7.98 us: 1.35x faster                                                                 |
| sympy_str                  | 283 ms                                                          | 211 ms: 1.34x faster                                                                  |
| logging_format             | 11.5 us                                                         | 8.62 us: 1.33x faster                                                                 |
| async_tree_none            | 343 ms                                                          | 258 ms: 1.33x faster                                                                  |
| nbody                      | 126 ms                                                          | 95.9 ms: 1.31x faster                                                                 |
| sympy_integrate            | 19.9 ms                                                         | 15.3 ms: 1.30x faster                                                                 |
| crypto_pyaes               | 79.4 ms                                                         | 61.3 ms: 1.30x faster                                                                 |
| xml_etree_process          | 55.0 ms                                                         | 42.8 ms: 1.28x faster                                                                 |
| django_template            | 37.4 ms                                                         | 29.1 ms: 1.28x faster                                                                 |
| async_tree_memoization     | 408 ms                                                          | 320 ms: 1.28x faster                                                                  |
| genshi_xml                 | 61.2 ms                                                         | 48.5 ms: 1.26x faster                                                                 |
| pyflate                    | 471 ms                                                          | 375 ms: 1.26x faster                                                                  |
| hexiom                     | 7.51 ms                                                         | 5.99 ms: 1.25x faster                                                                 |
| sympy_expand               | 462 ms                                                          | 370 ms: 1.25x faster                                                                  |
| async_tree_io_tg           | 746 ms                                                          | 598 ms: 1.25x faster                                                                  |
| scimark_lu                 | 102 ms                                                          | 82.1 ms: 1.25x faster                                                                 |
| go                         | 147 ms                                                          | 118 ms: 1.24x faster                                                                  |
| async_tree_none_tg         | 301 ms                                                          | 242 ms: 1.24x faster                                                                  |
| asyncio_tcp                | 787 ms                                                          | 634 ms: 1.24x faster                                                                  |
| pycparser                  | 1.04 sec                                                        | 841 ms: 1.24x faster                                                                  |
| scimark_fft                | 291 ms                                                          | 236 ms: 1.24x faster                                                                  |
| tornado_http               | 118 ms                                                          | 95.9 ms: 1.23x faster                                                                 |
| async_tree_memoization_tg  | 378 ms                                                          | 306 ms: 1.23x faster                                                                  |
| genshi_text                | 26.8 ms                                                         | 21.8 ms: 1.23x faster                                                                 |
| async_tree_io              | 754 ms                                                          | 616 ms: 1.22x faster                                                                  |
| raytrace                   | 327 ms                                                          | 269 ms: 1.22x faster                                                                  |
| html5lib                   | 54.3 ms                                                         | 44.9 ms: 1.21x faster                                                                 |
| mdp                        | 2.07 sec                                                        | 1.73 sec: 1.20x faster                                                                |
| nqueens                    | 111 ms                                                          | 94.1 ms: 1.18x faster                                                                 |
| fannkuch                   | 399 ms                                                          | 342 ms: 1.17x faster                                                                  |
| docutils                   | 2.10 sec                                                        | 1.81 sec: 1.16x faster                                                                |
| xml_etree_generate         | 71.6 ms                                                         | 62.0 ms: 1.16x faster                                                                 |
| pprint_pformat             | 1.70 sec                                                        | 1.48 sec: 1.14x faster                                                                |
| async_tree_cpu_io_mixed_tg | 577 ms                                                          | 505 ms: 1.14x faster                                                                  |
| json                       | 4.78 ms                                                         | 4.19 ms: 1.14x faster                                                                 |
| async_tree_cpu_io_mixed    | 590 ms                                                          | 519 ms: 1.14x faster                                                                  |
| xml_etree_iterparse        | 75.6 ms                                                         | 67.0 ms: 1.13x faster                                                                 |
| pprint_safe_repr           | 819 ms                                                          | 728 ms: 1.12x faster                                                                  |
| unpickle_list              | 3.28 us                                                         | 2.93 us: 1.12x faster                                                                 |
| scimark_monte_carlo        | 70.8 ms                                                         | 63.4 ms: 1.12x faster                                                                 |
| bench_thread_pool          | 1.14 ms                                                         | 1.02 ms: 1.11x faster                                                                 |
| sqlglot_optimize           | 51.8 ms                                                         | 46.7 ms: 1.11x faster                                                                 |
| 2to3                       | 282 ms                                                          | 255 ms: 1.11x faster                                                                  |
| sqlite_synth               | 2.15 us                                                         | 1.94 us: 1.11x faster                                                                 |
| meteor_contest             | 90.9 ms                                                         | 82.7 ms: 1.10x faster                                                                 |
| xml_etree_parse            | 114 ms                                                          | 108 ms: 1.06x faster                                                                  |
| pidigits                   | 203 ms                                                          | 199 ms: 1.02x faster                                                                  |
| asyncio_tcp_ssl            | 17.1 sec                                                        | 16.8 sec: 1.02x faster                                                                |
| pickle_dict                | 20.1 us                                                         | 19.8 us: 1.02x faster                                                                 |
| json_loads                 | 20.0 us                                                         | 19.8 us: 1.01x faster                                                                 |
| regex_dna                  | 122 ms                                                          | 121 ms: 1.01x faster                                                                  |
| pickle                     | 7.99 us                                                         | 8.03 us: 1.01x slower                                                                 |
| gc_traversal               | 1.38 ms                                                         | 1.40 ms: 1.01x slower                                                                 |
| bench_mp_pool              | 70.9 ms                                                         | 73.2 ms: 1.03x slower                                                                 |
| regex_effbot               | 1.82 ms                                                         | 1.89 ms: 1.04x slower                                                                 |
| regex_v8                   | 15.2 ms                                                         | 16.2 ms: 1.06x slower                                                                 |
| create_gc_cycles           | 618 us                                                          | 662 us: 1.07x slower                                                                  |
| pathlib                    | 79.9 ms                                                         | 86.1 ms: 1.08x slower                                                                 |
| unpickle                   | 9.23 us                                                         | 9.96 us: 1.08x slower                                                                 |
| python_startup             | 22.0 ms                                                         | 25.1 ms: 1.14x slower                                                                 |
| async_generators           | 260 ms                                                          | 300 ms: 1.15x slower                                                                  |
| python_startup_no_site     | 18.8 ms                                                         | 23.0 ms: 1.22x slower                                                                 |
| telco                      | 5.29 ms                                                         | 6.57 ms: 1.24x slower                                                                 |
| sqlglot_normalize          | 113 ms                                                          | 226 ms: 2.00x slower                                                                  |
| coverage                   | 58.0 ms                                                         | 501 ms: 8.63x slower                                                                  |
| thrift                     | 801 us                                                          | 10.8 ms: 13.43x slower                                                                |
| Geometric mean             | (ref)                                                           | 1.17x faster                                                                          |

Benchmark hidden because not significant (1): pickle_list
Ignored benchmarks (7) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509.json: aiohttp, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.16x


# Memory

- memory change: unknown