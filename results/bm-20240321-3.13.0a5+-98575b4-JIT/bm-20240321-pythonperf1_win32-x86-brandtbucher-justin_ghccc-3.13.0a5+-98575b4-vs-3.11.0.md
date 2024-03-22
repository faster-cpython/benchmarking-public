# Results vs. 3.11.0

- fork: brandtbucher
- ref: justin_ghccc
- machine: windows-x86
- commit hash: 98575b4
- commit date: 2024-03-21
- overall geometric mean: 1.05x faster
- HPT reliability: 99.88%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240321-pythonperf1_win32-x86-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 282 ms                                                          | 259 ms: 1.09x faster                                                          |
| chameleon      | 8.08 ms                                                         | 5.92 ms: 1.37x faster                                                         |
| docutils       | 2.10 sec                                                        | 2.42 sec: 1.16x slower                                                        |
| html5lib       | 54.3 ms                                                         | 48.9 ms: 1.11x faster                                                         |
| tornado_http   | 118 ms                                                          | 101 ms: 1.17x faster                                                          |
| Geometric mean | (ref)                                                           | 1.11x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240321-pythonperf1_win32-x86-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 590 ms                                                          | 1.58 sec: 2.68x slower                                                        |
| async_tree_cpu_io_mixed_tg | 577 ms                                                          | 1.63 sec: 2.83x slower                                                        |
| async_tree_none            | 343 ms                                                          | 1.21 sec: 3.53x slower                                                        |
| async_tree_memoization     | 408 ms                                                          | 1.46 sec: 3.57x slower                                                        |
| async_tree_memoization_tg  | 378 ms                                                          | 1.49 sec: 3.96x slower                                                        |
| async_tree_none_tg         | 301 ms                                                          | 1.25 sec: 4.16x slower                                                        |
| async_tree_io              | 754 ms                                                          | 4.63 sec: 6.15x slower                                                        |
| async_tree_io_tg           | 746 ms                                                          | 4.75 sec: 6.37x slower                                                        |
| Geometric mean             | (ref)                                                           | 3.97x slower                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240321-pythonperf1_win32-x86-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 126 ms                                                          | 53.7 ms: 2.35x faster                                                         |
| pidigits       | 203 ms                                                          | 197 ms: 1.03x faster                                                          |
| Geometric mean | (ref)                                                           | 1.35x faster                                                                  |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240321-pythonperf1_win32-x86-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                          | 101 ms: 1.46x faster                                                          |
| regex_dna      | 122 ms                                                          | 118 ms: 1.03x faster                                                          |
| regex_v8       | 15.2 ms                                                         | 15.9 ms: 1.05x slower                                                         |
| regex_effbot   | 1.82 ms                                                         | 1.93 ms: 1.06x slower                                                         |
| Geometric mean | (ref)                                                           | 1.08x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240321-pythonperf1_win32-x86-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| unpickle_pure_python | 231 us                                                          | 136 us: 1.70x faster                                                          |
| tomli_loads          | 2.31 sec                                                        | 1.42 sec: 1.63x faster                                                        |
| json_dumps           | 9.80 ms                                                         | 6.95 ms: 1.41x faster                                                         |
| pickle_pure_python   | 309 us                                                          | 228 us: 1.35x faster                                                          |
| unpickle_list        | 3.28 us                                                         | 2.61 us: 1.26x faster                                                         |
| xml_etree_process    | 55.0 ms                                                         | 47.9 ms: 1.15x faster                                                         |
| xml_etree_generate   | 71.6 ms                                                         | 65.9 ms: 1.09x faster                                                         |
| pickle               | 7.99 us                                                         | 7.67 us: 1.04x faster                                                         |
| pickle_list          | 3.27 us                                                         | 3.15 us: 1.04x faster                                                         |
| pickle_dict          | 20.1 us                                                         | 19.8 us: 1.01x faster                                                         |
| json_loads           | 20.0 us                                                         | 20.1 us: 1.00x slower                                                         |
| unpickle             | 9.23 us                                                         | 9.88 us: 1.07x slower                                                         |
| xml_etree_parse      | 114 ms                                                          | 130 ms: 1.14x slower                                                          |
| xml_etree_iterparse  | 75.6 ms                                                         | 88.7 ms: 1.17x slower                                                         |
| Geometric mean       | (ref)                                                           | 1.14x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240321-pythonperf1_win32-x86-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 22.0 ms                                                         | 26.3 ms: 1.20x slower                                                         |
| python_startup_no_site | 18.8 ms                                                         | 23.7 ms: 1.26x slower                                                         |
| Geometric mean         | (ref)                                                           | 1.23x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240321-pythonperf1_win32-x86-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|-----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 10.3 ms                                                         | 5.46 ms: 1.88x faster                                                         |
| genshi_text     | 26.8 ms                                                         | 21.7 ms: 1.23x faster                                                         |
| django_template | 37.4 ms                                                         | 31.1 ms: 1.20x faster                                                         |
| genshi_xml      | 61.2 ms                                                         | 51.0 ms: 1.20x faster                                                         |
| Geometric mean  | (ref)                                                           | 1.35x faster                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240321-pythonperf1_win32-x86-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| typing_runtime_protocols   | 478 us                                                          | 90.9 us: 5.26x faster                                                         |
| spectral_norm              | 122 ms                                                          | 51.1 ms: 2.38x faster                                                         |
| nbody                      | 126 ms                                                          | 53.7 ms: 2.35x faster                                                         |
| generators                 | 52.2 ms                                                         | 24.0 ms: 2.18x faster                                                         |
| comprehensions             | 22.1 us                                                         | 11.6 us: 1.90x faster                                                         |
| mako                       | 10.3 ms                                                         | 5.46 ms: 1.88x faster                                                         |
| logging_silent             | 119 ns                                                          | 67.7 ns: 1.76x faster                                                         |
| fannkuch                   | 399 ms                                                          | 231 ms: 1.73x faster                                                          |
| scimark_fft                | 291 ms                                                          | 170 ms: 1.71x faster                                                          |
| pyflate                    | 471 ms                                                          | 276 ms: 1.71x faster                                                          |
| unpickle_pure_python       | 231 us                                                          | 136 us: 1.70x faster                                                          |
| scimark_sparse_mat_mult    | 4.23 ms                                                         | 2.50 ms: 1.70x faster                                                         |
| scimark_monte_carlo        | 70.8 ms                                                         | 42.6 ms: 1.66x faster                                                         |
| hexiom                     | 7.51 ms                                                         | 4.55 ms: 1.65x faster                                                         |
| crypto_pyaes               | 79.4 ms                                                         | 48.2 ms: 1.65x faster                                                         |
| deltablue                  | 4.10 ms                                                         | 2.49 ms: 1.64x faster                                                         |
| tomli_loads                | 2.31 sec                                                        | 1.42 sec: 1.63x faster                                                        |
| richards_super             | 58.7 ms                                                         | 36.0 ms: 1.63x faster                                                         |
| chaos                      | 84.4 ms                                                         | 53.0 ms: 1.59x faster                                                         |
| deepcopy_memo              | 40.0 us                                                         | 25.4 us: 1.58x faster                                                         |
| richards                   | 48.8 ms                                                         | 31.0 ms: 1.58x faster                                                         |
| coroutines                 | 23.7 ms                                                         | 15.2 ms: 1.56x faster                                                         |
| scimark_sor                | 135 ms                                                          | 90.9 ms: 1.49x faster                                                         |
| sqlglot_parse              | 1.49 ms                                                         | 1.01 ms: 1.47x faster                                                         |
| regex_compile              | 148 ms                                                          | 101 ms: 1.46x faster                                                          |
| nqueens                    | 111 ms                                                          | 78.5 ms: 1.42x faster                                                         |
| pprint_pformat             | 1.70 sec                                                        | 1.20 sec: 1.42x faster                                                        |
| json_dumps                 | 9.80 ms                                                         | 6.95 ms: 1.41x faster                                                         |
| sympy_sum                  | 149 ms                                                          | 106 ms: 1.41x faster                                                          |
| sqlglot_transpile          | 1.78 ms                                                         | 1.27 ms: 1.41x faster                                                         |
| pprint_safe_repr           | 819 ms                                                          | 585 ms: 1.40x faster                                                          |
| logging_simple             | 10.8 us                                                         | 7.83 us: 1.38x faster                                                         |
| chameleon                  | 8.08 ms                                                         | 5.92 ms: 1.37x faster                                                         |
| pickle_pure_python         | 309 us                                                          | 228 us: 1.35x faster                                                          |
| logging_format             | 11.5 us                                                         | 8.48 us: 1.35x faster                                                         |
| sympy_str                  | 283 ms                                                          | 210 ms: 1.35x faster                                                          |
| raytrace                   | 327 ms                                                          | 244 ms: 1.34x faster                                                          |
| scimark_lu                 | 102 ms                                                          | 76.7 ms: 1.33x faster                                                         |
| deepcopy                   | 381 us                                                          | 291 us: 1.31x faster                                                          |
| deepcopy_reduce            | 3.32 us                                                         | 2.56 us: 1.30x faster                                                         |
| go                         | 147 ms                                                          | 114 ms: 1.29x faster                                                          |
| sympy_integrate            | 19.9 ms                                                         | 15.5 ms: 1.28x faster                                                         |
| unpickle_list              | 3.28 us                                                         | 2.61 us: 1.26x faster                                                         |
| sympy_expand               | 462 ms                                                          | 372 ms: 1.24x faster                                                          |
| genshi_text                | 26.8 ms                                                         | 21.7 ms: 1.23x faster                                                         |
| meteor_contest             | 90.9 ms                                                         | 74.3 ms: 1.22x faster                                                         |
| sqlglot_optimize           | 51.8 ms                                                         | 43.1 ms: 1.20x faster                                                         |
| django_template            | 37.4 ms                                                         | 31.1 ms: 1.20x faster                                                         |
| asyncio_tcp                | 787 ms                                                          | 654 ms: 1.20x faster                                                          |
| genshi_xml                 | 61.2 ms                                                         | 51.0 ms: 1.20x faster                                                         |
| mdp                        | 2.07 sec                                                        | 1.73 sec: 1.19x faster                                                        |
| tornado_http               | 118 ms                                                          | 101 ms: 1.17x faster                                                          |
| xml_etree_process          | 55.0 ms                                                         | 47.9 ms: 1.15x faster                                                         |
| json                       | 4.78 ms                                                         | 4.22 ms: 1.13x faster                                                         |
| bench_thread_pool          | 1.14 ms                                                         | 1.01 ms: 1.13x faster                                                         |
| sqlite_synth               | 2.15 us                                                         | 1.91 us: 1.13x faster                                                         |
| html5lib                   | 54.3 ms                                                         | 48.9 ms: 1.11x faster                                                         |
| pycparser                  | 1.04 sec                                                        | 951 ms: 1.10x faster                                                          |
| 2to3                       | 282 ms                                                          | 259 ms: 1.09x faster                                                          |
| xml_etree_generate         | 71.6 ms                                                         | 65.9 ms: 1.09x faster                                                         |
| gc_traversal               | 1.38 ms                                                         | 1.28 ms: 1.07x faster                                                         |
| pickle                     | 7.99 us                                                         | 7.67 us: 1.04x faster                                                         |
| pickle_list                | 3.27 us                                                         | 3.15 us: 1.04x faster                                                         |
| regex_dna                  | 122 ms                                                          | 118 ms: 1.03x faster                                                          |
| pidigits                   | 203 ms                                                          | 197 ms: 1.03x faster                                                          |
| pylint                     | 418 ms                                                          | 412 ms: 1.02x faster                                                          |
| asyncio_tcp_ssl            | 17.1 sec                                                        | 16.8 sec: 1.01x faster                                                        |
| pickle_dict                | 20.1 us                                                         | 19.8 us: 1.01x faster                                                         |
| json_loads                 | 20.0 us                                                         | 20.1 us: 1.00x slower                                                         |
| regex_v8                   | 15.2 ms                                                         | 15.9 ms: 1.05x slower                                                         |
| regex_effbot               | 1.82 ms                                                         | 1.93 ms: 1.06x slower                                                         |
| unpickle                   | 9.23 us                                                         | 9.88 us: 1.07x slower                                                         |
| bench_mp_pool              | 70.9 ms                                                         | 76.2 ms: 1.07x slower                                                         |
| pathlib                    | 79.9 ms                                                         | 86.5 ms: 1.08x slower                                                         |
| create_gc_cycles           | 618 us                                                          | 670 us: 1.09x slower                                                          |
| telco                      | 5.29 ms                                                         | 5.80 ms: 1.10x slower                                                         |
| unpack_sequence            | 65.2 ns                                                         | 73.1 ns: 1.12x slower                                                         |
| xml_etree_parse            | 114 ms                                                          | 130 ms: 1.14x slower                                                          |
| docutils                   | 2.10 sec                                                        | 2.42 sec: 1.16x slower                                                        |
| xml_etree_iterparse        | 75.6 ms                                                         | 88.7 ms: 1.17x slower                                                         |
| python_startup             | 22.0 ms                                                         | 26.3 ms: 1.20x slower                                                         |
| async_generators           | 260 ms                                                          | 315 ms: 1.21x slower                                                          |
| python_startup_no_site     | 18.8 ms                                                         | 23.7 ms: 1.26x slower                                                         |
| sqlglot_normalize          | 113 ms                                                          | 216 ms: 1.91x slower                                                          |
| async_tree_cpu_io_mixed    | 590 ms                                                          | 1.58 sec: 2.68x slower                                                        |
| async_tree_cpu_io_mixed_tg | 577 ms                                                          | 1.63 sec: 2.83x slower                                                        |
| async_tree_none            | 343 ms                                                          | 1.21 sec: 3.53x slower                                                        |
| async_tree_memoization     | 408 ms                                                          | 1.46 sec: 3.57x slower                                                        |
| async_tree_memoization_tg  | 378 ms                                                          | 1.49 sec: 3.96x slower                                                        |
| async_tree_none_tg         | 301 ms                                                          | 1.25 sec: 4.16x slower                                                        |
| async_tree_io              | 754 ms                                                          | 4.63 sec: 6.15x slower                                                        |
| async_tree_io_tg           | 746 ms                                                          | 4.75 sec: 6.37x slower                                                        |
| coverage                   | 58.0 ms                                                         | 513 ms: 8.84x slower                                                          |
| thrift                     | 801 us                                                          | 11.1 ms: 13.81x slower                                                        |
| Geometric mean             | (ref)                                                           | 1.05x faster                                                                  |

Benchmark hidden because not significant (1): float
Ignored benchmarks (7) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509.json: aiohttp, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 99.88% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.02x


# Memory

- memory change: unknown