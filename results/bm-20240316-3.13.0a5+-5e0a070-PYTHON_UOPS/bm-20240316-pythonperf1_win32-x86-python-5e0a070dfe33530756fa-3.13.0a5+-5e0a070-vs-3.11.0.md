# Results vs. 3.11.0

- fork: python
- ref: 5e0a070dfe33530756fa
- machine: windows-x86
- commit hash: 5e0a070
- commit date: 2024-03-16
- overall geometric mean: 1.21x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 282 ms                                                          | 245 ms: 1.15x faster                                                            |
| chameleon      | 8.08 ms                                                         | 6.11 ms: 1.32x faster                                                           |
| docutils       | 2.10 sec                                                        | 1.83 sec: 1.14x faster                                                          |
| html5lib       | 54.3 ms                                                         | 48.0 ms: 1.13x faster                                                           |
| tornado_http   | 118 ms                                                          | 98.6 ms: 1.20x faster                                                           |
| Geometric mean | (ref)                                                           | 1.19x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none            | 343 ms                                                          | 252 ms: 1.36x faster                                                            |
| async_tree_memoization     | 408 ms                                                          | 316 ms: 1.29x faster                                                            |
| async_tree_io_tg           | 746 ms                                                          | 588 ms: 1.27x faster                                                            |
| async_tree_memoization_tg  | 378 ms                                                          | 299 ms: 1.26x faster                                                            |
| async_tree_none_tg         | 301 ms                                                          | 240 ms: 1.26x faster                                                            |
| async_tree_io              | 754 ms                                                          | 603 ms: 1.25x faster                                                            |
| async_tree_cpu_io_mixed    | 590 ms                                                          | 511 ms: 1.16x faster                                                            |
| async_tree_cpu_io_mixed_tg | 577 ms                                                          | 507 ms: 1.14x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.25x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 126 ms                                                          | 77.0 ms: 1.64x faster                                                           |
| float          | 76.1 ms                                                         | 57.0 ms: 1.33x faster                                                           |
| pidigits       | 203 ms                                                          | 199 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                           | 1.30x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                          | 117 ms: 1.26x faster                                                            |
| regex_dna      | 122 ms                                                          | 120 ms: 1.01x faster                                                            |
| regex_effbot   | 1.82 ms                                                         | 1.91 ms: 1.04x slower                                                           |
| regex_v8       | 15.2 ms                                                         | 16.1 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.31 sec                                                        | 1.55 sec: 1.49x faster                                                          |
| pickle_pure_python   | 309 us                                                          | 216 us: 1.43x faster                                                            |
| json_dumps           | 9.80 ms                                                         | 7.04 ms: 1.39x faster                                                           |
| unpickle_pure_python | 231 us                                                          | 167 us: 1.39x faster                                                            |
| xml_etree_process    | 55.0 ms                                                         | 42.9 ms: 1.28x faster                                                           |
| xml_etree_generate   | 71.6 ms                                                         | 61.1 ms: 1.17x faster                                                           |
| unpickle_list        | 3.28 us                                                         | 2.83 us: 1.16x faster                                                           |
| xml_etree_iterparse  | 75.6 ms                                                         | 68.4 ms: 1.10x faster                                                           |
| xml_etree_parse      | 114 ms                                                          | 109 ms: 1.05x faster                                                            |
| pickle               | 7.99 us                                                         | 7.79 us: 1.03x faster                                                           |
| pickle_dict          | 20.1 us                                                         | 19.9 us: 1.01x faster                                                           |
| pickle_list          | 3.27 us                                                         | 3.30 us: 1.01x slower                                                           |
| json_loads           | 20.0 us                                                         | 20.6 us: 1.03x slower                                                           |
| unpickle             | 9.23 us                                                         | 9.79 us: 1.06x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.16x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 22.0 ms                                                         | 22.2 ms: 1.01x slower                                                           |
| python_startup_no_site | 18.8 ms                                                         | 20.0 ms: 1.06x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.04x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 10.3 ms                                                         | 6.99 ms: 1.47x faster                                                           |
| genshi_text     | 26.8 ms                                                         | 19.8 ms: 1.35x faster                                                           |
| genshi_xml      | 61.2 ms                                                         | 45.6 ms: 1.34x faster                                                           |
| django_template | 37.4 ms                                                         | 30.3 ms: 1.24x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.35x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols   | 478 us                                                          | 92.5 us: 5.17x faster                                                           |
| generators                 | 52.2 ms                                                         | 22.9 ms: 2.28x faster                                                           |
| logging_silent             | 119 ns                                                          | 60.2 ns: 1.98x faster                                                           |
| pylint                     | 418 ms                                                          | 226 ms: 1.85x faster                                                            |
| richards_super             | 58.7 ms                                                         | 33.2 ms: 1.77x faster                                                           |
| deltablue                  | 4.10 ms                                                         | 2.36 ms: 1.73x faster                                                           |
| comprehensions             | 22.1 us                                                         | 13.3 us: 1.66x faster                                                           |
| richards                   | 48.8 ms                                                         | 29.6 ms: 1.65x faster                                                           |
| coroutines                 | 23.7 ms                                                         | 14.4 ms: 1.65x faster                                                           |
| nbody                      | 126 ms                                                          | 77.0 ms: 1.64x faster                                                           |
| deepcopy_memo              | 40.0 us                                                         | 24.5 us: 1.63x faster                                                           |
| chaos                      | 84.4 ms                                                         | 52.9 ms: 1.60x faster                                                           |
| spectral_norm              | 122 ms                                                          | 77.3 ms: 1.57x faster                                                           |
| sqlglot_parse              | 1.49 ms                                                         | 956 us: 1.56x faster                                                            |
| sqlglot_transpile          | 1.78 ms                                                         | 1.19 ms: 1.49x faster                                                           |
| tomli_loads                | 2.31 sec                                                        | 1.55 sec: 1.49x faster                                                          |
| scimark_sor                | 135 ms                                                          | 91.6 ms: 1.48x faster                                                           |
| mako                       | 10.3 ms                                                         | 6.99 ms: 1.47x faster                                                           |
| crypto_pyaes               | 79.4 ms                                                         | 54.7 ms: 1.45x faster                                                           |
| raytrace                   | 327 ms                                                          | 226 ms: 1.45x faster                                                            |
| scimark_monte_carlo        | 70.8 ms                                                         | 49.4 ms: 1.43x faster                                                           |
| pickle_pure_python         | 309 us                                                          | 216 us: 1.43x faster                                                            |
| pyflate                    | 471 ms                                                          | 335 ms: 1.41x faster                                                            |
| scimark_fft                | 291 ms                                                          | 207 ms: 1.41x faster                                                            |
| unpack_sequence            | 65.2 ns                                                         | 46.5 ns: 1.40x faster                                                           |
| json_dumps                 | 9.80 ms                                                         | 7.04 ms: 1.39x faster                                                           |
| deepcopy                   | 381 us                                                          | 275 us: 1.39x faster                                                            |
| hexiom                     | 7.51 ms                                                         | 5.42 ms: 1.39x faster                                                           |
| unpickle_pure_python       | 231 us                                                          | 167 us: 1.39x faster                                                            |
| deepcopy_reduce            | 3.32 us                                                         | 2.40 us: 1.38x faster                                                           |
| fannkuch                   | 399 ms                                                          | 289 ms: 1.38x faster                                                            |
| scimark_sparse_mat_mult    | 4.23 ms                                                         | 3.07 ms: 1.38x faster                                                           |
| sympy_sum                  | 149 ms                                                          | 108 ms: 1.37x faster                                                            |
| nqueens                    | 111 ms                                                          | 81.3 ms: 1.37x faster                                                           |
| logging_simple             | 10.8 us                                                         | 7.89 us: 1.37x faster                                                           |
| async_tree_none            | 343 ms                                                          | 252 ms: 1.36x faster                                                            |
| pprint_pformat             | 1.70 sec                                                        | 1.25 sec: 1.36x faster                                                          |
| genshi_text                | 26.8 ms                                                         | 19.8 ms: 1.35x faster                                                           |
| genshi_xml                 | 61.2 ms                                                         | 45.6 ms: 1.34x faster                                                           |
| pprint_safe_repr           | 819 ms                                                          | 612 ms: 1.34x faster                                                            |
| float                      | 76.1 ms                                                         | 57.0 ms: 1.33x faster                                                           |
| logging_format             | 11.5 us                                                         | 8.62 us: 1.33x faster                                                           |
| sympy_str                  | 283 ms                                                          | 214 ms: 1.33x faster                                                            |
| chameleon                  | 8.08 ms                                                         | 6.11 ms: 1.32x faster                                                           |
| sympy_integrate            | 19.9 ms                                                         | 15.2 ms: 1.31x faster                                                           |
| scimark_lu                 | 102 ms                                                          | 78.4 ms: 1.30x faster                                                           |
| async_tree_memoization     | 408 ms                                                          | 316 ms: 1.29x faster                                                            |
| xml_etree_process          | 55.0 ms                                                         | 42.9 ms: 1.28x faster                                                           |
| async_tree_io_tg           | 746 ms                                                          | 588 ms: 1.27x faster                                                            |
| async_tree_memoization_tg  | 378 ms                                                          | 299 ms: 1.26x faster                                                            |
| regex_compile              | 148 ms                                                          | 117 ms: 1.26x faster                                                            |
| async_tree_none_tg         | 301 ms                                                          | 240 ms: 1.26x faster                                                            |
| mdp                        | 2.07 sec                                                        | 1.65 sec: 1.25x faster                                                          |
| go                         | 147 ms                                                          | 117 ms: 1.25x faster                                                            |
| async_tree_io              | 754 ms                                                          | 603 ms: 1.25x faster                                                            |
| sqlglot_optimize           | 51.8 ms                                                         | 41.8 ms: 1.24x faster                                                           |
| sympy_expand               | 462 ms                                                          | 373 ms: 1.24x faster                                                            |
| asyncio_tcp                | 787 ms                                                          | 635 ms: 1.24x faster                                                            |
| django_template            | 37.4 ms                                                         | 30.3 ms: 1.24x faster                                                           |
| pycparser                  | 1.04 sec                                                        | 852 ms: 1.22x faster                                                            |
| tornado_http               | 118 ms                                                          | 98.6 ms: 1.20x faster                                                           |
| meteor_contest             | 90.9 ms                                                         | 76.1 ms: 1.19x faster                                                           |
| xml_etree_generate         | 71.6 ms                                                         | 61.1 ms: 1.17x faster                                                           |
| unpickle_list              | 3.28 us                                                         | 2.83 us: 1.16x faster                                                           |
| async_tree_cpu_io_mixed    | 590 ms                                                          | 511 ms: 1.16x faster                                                            |
| 2to3                       | 282 ms                                                          | 245 ms: 1.15x faster                                                            |
| docutils                   | 2.10 sec                                                        | 1.83 sec: 1.14x faster                                                          |
| async_tree_cpu_io_mixed_tg | 577 ms                                                          | 507 ms: 1.14x faster                                                            |
| html5lib                   | 54.3 ms                                                         | 48.0 ms: 1.13x faster                                                           |
| sqlite_synth               | 2.15 us                                                         | 1.90 us: 1.13x faster                                                           |
| bench_thread_pool          | 1.14 ms                                                         | 1.02 ms: 1.11x faster                                                           |
| json                       | 4.78 ms                                                         | 4.30 ms: 1.11x faster                                                           |
| xml_etree_iterparse        | 75.6 ms                                                         | 68.4 ms: 1.10x faster                                                           |
| xml_etree_parse            | 114 ms                                                          | 109 ms: 1.05x faster                                                            |
| pickle                     | 7.99 us                                                         | 7.79 us: 1.03x faster                                                           |
| pidigits                   | 203 ms                                                          | 199 ms: 1.02x faster                                                            |
| asyncio_tcp_ssl            | 17.1 sec                                                        | 16.8 sec: 1.02x faster                                                          |
| bench_mp_pool              | 70.9 ms                                                         | 70.0 ms: 1.01x faster                                                           |
| regex_dna                  | 122 ms                                                          | 120 ms: 1.01x faster                                                            |
| pickle_dict                | 20.1 us                                                         | 19.9 us: 1.01x faster                                                           |
| python_startup             | 22.0 ms                                                         | 22.2 ms: 1.01x slower                                                           |
| pickle_list                | 3.27 us                                                         | 3.30 us: 1.01x slower                                                           |
| gc_traversal               | 1.38 ms                                                         | 1.40 ms: 1.02x slower                                                           |
| json_loads                 | 20.0 us                                                         | 20.6 us: 1.03x slower                                                           |
| regex_effbot               | 1.82 ms                                                         | 1.91 ms: 1.04x slower                                                           |
| regex_v8                   | 15.2 ms                                                         | 16.1 ms: 1.06x slower                                                           |
| unpickle                   | 9.23 us                                                         | 9.79 us: 1.06x slower                                                           |
| python_startup_no_site     | 18.8 ms                                                         | 20.0 ms: 1.06x slower                                                           |
| create_gc_cycles           | 618 us                                                          | 660 us: 1.07x slower                                                            |
| pathlib                    | 79.9 ms                                                         | 86.4 ms: 1.08x slower                                                           |
| async_generators           | 260 ms                                                          | 285 ms: 1.10x slower                                                            |
| telco                      | 5.29 ms                                                         | 6.21 ms: 1.17x slower                                                           |
| sqlglot_normalize          | 113 ms                                                          | 212 ms: 1.87x slower                                                            |
| coverage                   | 58.0 ms                                                         | 474 ms: 8.17x slower                                                            |
| thrift                     | 801 us                                                          | 11.3 ms: 14.06x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.21x faster                                                                    |
Ignored benchmarks (7) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1_win32-x86-python-v3.11.0-3.11.0-deaf509.json: aiohttp, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.21x


# Memory

- memory change: unknown