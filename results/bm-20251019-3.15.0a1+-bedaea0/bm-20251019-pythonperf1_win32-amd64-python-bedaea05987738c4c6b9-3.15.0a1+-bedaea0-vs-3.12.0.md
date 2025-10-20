# Results vs. 3.12.0

- fork: python
- ref: bedaea05987738c4c6b9
- machine: windows-amd64
- commit hash: bedaea0
- commit date: 2025-10-19
- overall geometric mean: 1.455x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.40x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 219 ms: 1.28x faster                                                              |
| docutils       | 1.98 sec                                                        | 1.63 sec: 1.22x faster                                                            |
| Geometric mean | (ref)                                                           | 1.25x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_io              | 693 ms                                                          | 382 ms: 1.82x faster                                                              |
| async_tree_memoization     | 364 ms                                                          | 203 ms: 1.80x faster                                                              |
| async_tree_io_tg           | 677 ms                                                          | 383 ms: 1.77x faster                                                              |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 326 ms: 1.73x faster                                                              |
| async_tree_memoization_tg  | 350 ms                                                          | 208 ms: 1.69x faster                                                              |
| async_tree_none            | 298 ms                                                          | 177 ms: 1.68x faster                                                              |
| async_tree_none_tg         | 278 ms                                                          | 166 ms: 1.67x faster                                                              |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 334 ms: 1.64x faster                                                              |
| Geometric mean             | (ref)                                                           | 1.72x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 67.9 ms: 1.87x faster                                                             |
| float          | 76.7 ms                                                         | 44.8 ms: 1.71x faster                                                             |
| pidigits       | 199 ms                                                          | 148 ms: 1.35x faster                                                              |
| Geometric mean | (ref)                                                           | 1.63x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 81.0 ms: 1.59x faster                                                             |
| regex_effbot   | 2.04 ms                                                         | 1.50 ms: 1.36x faster                                                             |
| regex_v8       | 15.0 ms                                                         | 13.5 ms: 1.12x faster                                                             |
| regex_dna      | 127 ms                                                          | 115 ms: 1.11x faster                                                              |
| Geometric mean | (ref)                                                           | 1.28x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.42 sec: 1.55x faster                                                            |
| unpickle_pure_python | 210 us                                                          | 138 us: 1.52x faster                                                              |
| json_loads           | 20.4 us                                                         | 14.5 us: 1.40x faster                                                             |
| xml_etree_process    | 53.2 ms                                                         | 39.3 ms: 1.36x faster                                                             |
| json_dumps           | 7.40 ms                                                         | 5.53 ms: 1.34x faster                                                             |
| pickle_pure_python   | 286 us                                                          | 218 us: 1.31x faster                                                              |
| xml_etree_parse      | 113 ms                                                          | 87.5 ms: 1.29x faster                                                             |
| xml_etree_generate   | 72.1 ms                                                         | 57.1 ms: 1.26x faster                                                             |
| xml_etree_iterparse  | 77.6 ms                                                         | 65.1 ms: 1.19x faster                                                             |
| unpickle             | 9.71 us                                                         | 8.59 us: 1.13x faster                                                             |
| unpickle_list        | 2.95 us                                                         | 2.79 us: 1.06x faster                                                             |
| pickle_list          | 3.37 us                                                         | 3.31 us: 1.02x faster                                                             |
| pickle               | 7.79 us                                                         | 8.04 us: 1.03x slower                                                             |
| Geometric mean       | (ref)                                                           | 1.23x faster                                                                      |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup | 22.4 ms                                                         | 26.1 ms: 1.17x slower                                                             |
| Geometric mean | (ref)                                                           | 1.08x slower                                                                      |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 6.61 ms: 1.51x faster                                                             |
| django_template | 36.9 ms                                                         | 25.2 ms: 1.47x faster                                                             |
| Geometric mean  | (ref)                                                           | 1.49x faster                                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 1.27 sec: 13.85x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 29.4 ms: 3.11x faster                                                             |
| mdp                        | 1.91 sec                                                        | 823 ms: 2.32x faster                                                              |
| deepcopy_memo              | 38.4 us                                                         | 17.3 us: 2.21x faster                                                             |
| deepcopy                   | 360 us                                                          | 168 us: 2.15x faster                                                              |
| generators                 | 38.5 ms                                                         | 19.6 ms: 1.97x faster                                                             |
| unpack_sequence            | 62.5 ns                                                         | 32.8 ns: 1.90x faster                                                             |
| nbody                      | 127 ms                                                          | 67.9 ms: 1.87x faster                                                             |
| async_tree_io              | 693 ms                                                          | 382 ms: 1.82x faster                                                              |
| async_tree_memoization     | 364 ms                                                          | 203 ms: 1.80x faster                                                              |
| deepcopy_reduce            | 3.23 us                                                         | 1.81 us: 1.78x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 383 ms: 1.77x faster                                                              |
| logging_silent             | 101 ns                                                          | 57.7 ns: 1.75x faster                                                             |
| go                         | 137 ms                                                          | 78.8 ms: 1.74x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 326 ms: 1.73x faster                                                              |
| float                      | 76.7 ms                                                         | 44.8 ms: 1.71x faster                                                             |
| comprehensions             | 19.2 us                                                         | 11.2 us: 1.71x faster                                                             |
| raytrace                   | 308 ms                                                          | 183 ms: 1.69x faster                                                              |
| async_tree_memoization_tg  | 350 ms                                                          | 208 ms: 1.69x faster                                                              |
| async_tree_none            | 298 ms                                                          | 177 ms: 1.68x faster                                                              |
| async_tree_none_tg         | 278 ms                                                          | 166 ms: 1.67x faster                                                              |
| asyncio_tcp                | 662 ms                                                          | 398 ms: 1.67x faster                                                              |
| scimark_sor                | 130 ms                                                          | 78.0 ms: 1.67x faster                                                             |
| chaos                      | 69.4 ms                                                         | 41.7 ms: 1.66x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 334 ms: 1.64x faster                                                              |
| deltablue                  | 3.58 ms                                                         | 2.22 ms: 1.61x faster                                                             |
| hexiom                     | 6.82 ms                                                         | 4.23 ms: 1.61x faster                                                             |
| logging_simple             | 9.75 us                                                         | 6.08 us: 1.60x faster                                                             |
| regex_compile              | 129 ms                                                          | 81.0 ms: 1.59x faster                                                             |
| logging_format             | 10.4 us                                                         | 6.57 us: 1.58x faster                                                             |
| scimark_lu                 | 93.2 ms                                                         | 59.0 ms: 1.58x faster                                                             |
| scimark_monte_carlo        | 66.4 ms                                                         | 42.2 ms: 1.58x faster                                                             |
| tomli_loads                | 2.20 sec                                                        | 1.42 sec: 1.55x faster                                                            |
| scimark_fft                | 271 ms                                                          | 175 ms: 1.55x faster                                                              |
| unpickle_pure_python       | 210 us                                                          | 138 us: 1.52x faster                                                              |
| mako                       | 9.96 ms                                                         | 6.61 ms: 1.51x faster                                                             |
| spectral_norm              | 104 ms                                                          | 69.6 ms: 1.49x faster                                                             |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.60 ms: 1.48x faster                                                             |
| pprint_pformat             | 1.50 sec                                                        | 1.01 sec: 1.48x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 63.3 ms: 1.48x faster                                                             |
| richards                   | 41.3 ms                                                         | 28.1 ms: 1.47x faster                                                             |
| pyflate                    | 424 ms                                                          | 289 ms: 1.47x faster                                                              |
| django_template            | 36.9 ms                                                         | 25.2 ms: 1.47x faster                                                             |
| richards_super             | 46.5 ms                                                         | 31.7 ms: 1.46x faster                                                             |
| pprint_safe_repr           | 721 ms                                                          | 493 ms: 1.46x faster                                                              |
| dulwich_log                | 58.5 ms                                                         | 40.3 ms: 1.45x faster                                                             |
| crypto_pyaes               | 69.2 ms                                                         | 48.0 ms: 1.44x faster                                                             |
| sympy_str                  | 240 ms                                                          | 169 ms: 1.42x faster                                                              |
| coroutines                 | 20.9 ms                                                         | 14.8 ms: 1.42x faster                                                             |
| json_loads                 | 20.4 us                                                         | 14.5 us: 1.40x faster                                                             |
| sympy_sum                  | 123 ms                                                          | 87.5 ms: 1.40x faster                                                             |
| sympy_integrate            | 17.5 ms                                                         | 12.5 ms: 1.40x faster                                                             |
| json                       | 4.15 ms                                                         | 2.98 ms: 1.40x faster                                                             |
| pycparser                  | 978 ms                                                          | 702 ms: 1.39x faster                                                              |
| sympy_expand               | 398 ms                                                          | 289 ms: 1.38x faster                                                              |
| regex_effbot               | 2.04 ms                                                         | 1.50 ms: 1.36x faster                                                             |
| xml_etree_process          | 53.2 ms                                                         | 39.3 ms: 1.36x faster                                                             |
| pidigits                   | 199 ms                                                          | 148 ms: 1.35x faster                                                              |
| json_dumps                 | 7.40 ms                                                         | 5.53 ms: 1.34x faster                                                             |
| async_generators           | 313 ms                                                          | 237 ms: 1.32x faster                                                              |
| fannkuch                   | 354 ms                                                          | 269 ms: 1.31x faster                                                              |
| pickle_pure_python         | 286 us                                                          | 218 us: 1.31x faster                                                              |
| sqlite_synth               | 2.07 us                                                         | 1.59 us: 1.30x faster                                                             |
| xml_etree_parse            | 113 ms                                                          | 87.5 ms: 1.29x faster                                                             |
| telco                      | 5.51 ms                                                         | 4.26 ms: 1.29x faster                                                             |
| 2to3                       | 280 ms                                                          | 219 ms: 1.28x faster                                                              |
| bench_thread_pool          | 1.10 ms                                                         | 863 us: 1.28x faster                                                              |
| xml_etree_generate         | 72.1 ms                                                         | 57.1 ms: 1.26x faster                                                             |
| typing_runtime_protocols   | 126 us                                                          | 103 us: 1.22x faster                                                              |
| docutils                   | 1.98 sec                                                        | 1.63 sec: 1.22x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 65.1 ms: 1.19x faster                                                             |
| meteor_contest             | 86.9 ms                                                         | 73.4 ms: 1.18x faster                                                             |
| unpickle                   | 9.71 us                                                         | 8.59 us: 1.13x faster                                                             |
| regex_v8                   | 15.0 ms                                                         | 13.5 ms: 1.12x faster                                                             |
| regex_dna                  | 127 ms                                                          | 115 ms: 1.11x faster                                                              |
| unpickle_list              | 2.95 us                                                         | 2.79 us: 1.06x faster                                                             |
| pickle_list                | 3.37 us                                                         | 3.31 us: 1.02x faster                                                             |
| coverage                   | 48.4 ms                                                         | 49.4 ms: 1.02x slower                                                             |
| pickle                     | 7.79 us                                                         | 8.04 us: 1.03x slower                                                             |
| python_startup             | 22.4 ms                                                         | 26.1 ms: 1.17x slower                                                             |
| bench_mp_pool              | 75.4 ms                                                         | 90.2 ms: 1.20x slower                                                             |
| gc_traversal               | 1.44 ms                                                         | 2.11 ms: 1.47x slower                                                             |
| create_gc_cycles           | 652 us                                                          | 1.28 ms: 1.97x slower                                                             |
| Geometric mean             | (ref)                                                           | 1.46x faster                                                                      |

Benchmark hidden because not significant (2): pickle_dict, python_startup_no_site
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20251019-3.15.0a1+-bedaea0/bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.455x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.45x
- 95% likely to have a speedup of 1.43x
- 99% likely to have a speedup of 1.40x

# Memory
- memory change: unknown