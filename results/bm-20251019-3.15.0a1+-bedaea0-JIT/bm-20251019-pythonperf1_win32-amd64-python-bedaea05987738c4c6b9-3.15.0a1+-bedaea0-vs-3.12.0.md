# Results vs. 3.12.0

- fork: python
- ref: bedaea05987738c4c6b9
- machine: windows-amd64
- commit hash: bedaea0
- commit date: 2025-10-19
- overall geometric mean: 1.536x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.49x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 217 ms: 1.29x faster                                                              |
| docutils       | 1.98 sec                                                        | 1.60 sec: 1.24x faster                                                            |
| Geometric mean | (ref)                                                           | 1.26x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization     | 364 ms                                                          | 198 ms: 1.84x faster                                                              |
| async_tree_io              | 693 ms                                                          | 387 ms: 1.79x faster                                                              |
| async_tree_io_tg           | 677 ms                                                          | 380 ms: 1.78x faster                                                              |
| async_tree_none            | 298 ms                                                          | 170 ms: 1.75x faster                                                              |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 327 ms: 1.72x faster                                                              |
| async_tree_none_tg         | 278 ms                                                          | 164 ms: 1.70x faster                                                              |
| async_tree_memoization_tg  | 350 ms                                                          | 210 ms: 1.67x faster                                                              |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 334 ms: 1.63x faster                                                              |
| Geometric mean             | (ref)                                                           | 1.73x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 54.2 ms: 2.34x faster                                                             |
| float          | 76.7 ms                                                         | 41.0 ms: 1.87x faster                                                             |
| pidigits       | 199 ms                                                          | 146 ms: 1.36x faster                                                              |
| Geometric mean | (ref)                                                           | 1.82x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 76.8 ms: 1.68x faster                                                             |
| regex_effbot   | 2.04 ms                                                         | 1.54 ms: 1.32x faster                                                             |
| regex_dna      | 127 ms                                                          | 117 ms: 1.09x faster                                                              |
| regex_v8       | 15.0 ms                                                         | 14.5 ms: 1.04x faster                                                             |
| Geometric mean | (ref)                                                           | 1.26x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.09 sec: 2.01x faster                                                            |
| unpickle_pure_python | 210 us                                                          | 106 us: 1.98x faster                                                              |
| xml_etree_process    | 53.2 ms                                                         | 35.3 ms: 1.51x faster                                                             |
| pickle_pure_python   | 286 us                                                          | 196 us: 1.46x faster                                                              |
| xml_etree_generate   | 72.1 ms                                                         | 49.5 ms: 1.46x faster                                                             |
| json_loads           | 20.4 us                                                         | 14.0 us: 1.45x faster                                                             |
| json_dumps           | 7.40 ms                                                         | 5.36 ms: 1.38x faster                                                             |
| xml_etree_parse      | 113 ms                                                          | 88.0 ms: 1.29x faster                                                             |
| xml_etree_iterparse  | 77.6 ms                                                         | 63.1 ms: 1.23x faster                                                             |
| unpickle             | 9.71 us                                                         | 8.62 us: 1.13x faster                                                             |
| pickle_dict          | 19.9 us                                                         | 18.6 us: 1.07x faster                                                             |
| unpickle_list        | 2.95 us                                                         | 2.78 us: 1.06x faster                                                             |
| pickle_list          | 3.37 us                                                         | 3.18 us: 1.06x faster                                                             |
| pickle               | 7.79 us                                                         | 7.40 us: 1.05x faster                                                             |
| Geometric mean       | (ref)                                                           | 1.34x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 18.8 ms: 1.01x faster                                                             |
| python_startup         | 22.4 ms                                                         | 25.2 ms: 1.13x slower                                                             |
| Geometric mean         | (ref)                                                           | 1.05x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.28 ms: 1.89x faster                                                             |
| django_template | 36.9 ms                                                         | 23.7 ms: 1.56x faster                                                             |
| Geometric mean  | (ref)                                                           | 1.71x faster                                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 1.34 sec: 13.18x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 29.1 ms: 3.14x faster                                                             |
| mdp                        | 1.91 sec                                                        | 785 ms: 2.44x faster                                                              |
| nbody                      | 127 ms                                                          | 54.2 ms: 2.34x faster                                                             |
| deepcopy_memo              | 38.4 us                                                         | 17.1 us: 2.25x faster                                                             |
| deepcopy                   | 360 us                                                          | 166 us: 2.17x faster                                                              |
| generators                 | 38.5 ms                                                         | 19.1 ms: 2.01x faster                                                             |
| tomli_loads                | 2.20 sec                                                        | 1.09 sec: 2.01x faster                                                            |
| scimark_fft                | 271 ms                                                          | 136 ms: 1.99x faster                                                              |
| unpickle_pure_python       | 210 us                                                          | 106 us: 1.98x faster                                                              |
| mako                       | 9.96 ms                                                         | 5.28 ms: 1.89x faster                                                             |
| unpack_sequence            | 62.5 ns                                                         | 33.2 ns: 1.88x faster                                                             |
| float                      | 76.7 ms                                                         | 41.0 ms: 1.87x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 198 ms: 1.84x faster                                                              |
| logging_silent             | 101 ns                                                          | 55.2 ns: 1.83x faster                                                             |
| comprehensions             | 19.2 us                                                         | 10.5 us: 1.82x faster                                                             |
| go                         | 137 ms                                                          | 75.8 ms: 1.81x faster                                                             |
| async_tree_io              | 693 ms                                                          | 387 ms: 1.79x faster                                                              |
| async_tree_io_tg           | 677 ms                                                          | 380 ms: 1.78x faster                                                              |
| raytrace                   | 308 ms                                                          | 174 ms: 1.77x faster                                                              |
| deepcopy_reduce            | 3.23 us                                                         | 1.83 us: 1.77x faster                                                             |
| async_tree_none            | 298 ms                                                          | 170 ms: 1.75x faster                                                              |
| pprint_pformat             | 1.50 sec                                                        | 856 ms: 1.75x faster                                                              |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.22 ms: 1.74x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 327 ms: 1.72x faster                                                              |
| pyflate                    | 424 ms                                                          | 247 ms: 1.72x faster                                                              |
| pprint_safe_repr           | 721 ms                                                          | 423 ms: 1.70x faster                                                              |
| fannkuch                   | 354 ms                                                          | 208 ms: 1.70x faster                                                              |
| chaos                      | 69.4 ms                                                         | 40.9 ms: 1.70x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 164 ms: 1.70x faster                                                              |
| hexiom                     | 6.82 ms                                                         | 4.03 ms: 1.69x faster                                                             |
| regex_compile              | 129 ms                                                          | 76.8 ms: 1.68x faster                                                             |
| scimark_sor                | 130 ms                                                          | 77.8 ms: 1.67x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 210 ms: 1.67x faster                                                              |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 334 ms: 1.63x faster                                                              |
| scimark_monte_carlo        | 66.4 ms                                                         | 40.9 ms: 1.63x faster                                                             |
| logging_simple             | 9.75 us                                                         | 6.00 us: 1.62x faster                                                             |
| deltablue                  | 3.58 ms                                                         | 2.22 ms: 1.62x faster                                                             |
| spectral_norm              | 104 ms                                                          | 64.3 ms: 1.62x faster                                                             |
| logging_format             | 10.4 us                                                         | 6.44 us: 1.62x faster                                                             |
| nqueens                    | 93.7 ms                                                         | 59.0 ms: 1.59x faster                                                             |
| scimark_lu                 | 93.2 ms                                                         | 59.7 ms: 1.56x faster                                                             |
| django_template            | 36.9 ms                                                         | 23.7 ms: 1.56x faster                                                             |
| richards                   | 41.3 ms                                                         | 26.7 ms: 1.55x faster                                                             |
| crypto_pyaes               | 69.2 ms                                                         | 44.9 ms: 1.54x faster                                                             |
| richards_super             | 46.5 ms                                                         | 30.6 ms: 1.52x faster                                                             |
| dulwich_log                | 58.5 ms                                                         | 38.7 ms: 1.51x faster                                                             |
| xml_etree_process          | 53.2 ms                                                         | 35.3 ms: 1.51x faster                                                             |
| asyncio_tcp                | 662 ms                                                          | 450 ms: 1.47x faster                                                              |
| json                       | 4.15 ms                                                         | 2.83 ms: 1.47x faster                                                             |
| coroutines                 | 20.9 ms                                                         | 14.3 ms: 1.46x faster                                                             |
| pickle_pure_python         | 286 us                                                          | 196 us: 1.46x faster                                                              |
| xml_etree_generate         | 72.1 ms                                                         | 49.5 ms: 1.46x faster                                                             |
| sympy_sum                  | 123 ms                                                          | 84.7 ms: 1.45x faster                                                             |
| json_loads                 | 20.4 us                                                         | 14.0 us: 1.45x faster                                                             |
| sympy_str                  | 240 ms                                                          | 166 ms: 1.44x faster                                                              |
| pycparser                  | 978 ms                                                          | 680 ms: 1.44x faster                                                              |
| telco                      | 5.51 ms                                                         | 3.86 ms: 1.43x faster                                                             |
| sympy_integrate            | 17.5 ms                                                         | 12.5 ms: 1.41x faster                                                             |
| sympy_expand               | 398 ms                                                          | 288 ms: 1.38x faster                                                              |
| json_dumps                 | 7.40 ms                                                         | 5.36 ms: 1.38x faster                                                             |
| pidigits                   | 199 ms                                                          | 146 ms: 1.36x faster                                                              |
| sqlite_synth               | 2.07 us                                                         | 1.55 us: 1.34x faster                                                             |
| bench_thread_pool          | 1.10 ms                                                         | 831 us: 1.33x faster                                                              |
| regex_effbot               | 2.04 ms                                                         | 1.54 ms: 1.32x faster                                                             |
| async_generators           | 313 ms                                                          | 239 ms: 1.31x faster                                                              |
| 2to3                       | 280 ms                                                          | 217 ms: 1.29x faster                                                              |
| xml_etree_parse            | 113 ms                                                          | 88.0 ms: 1.29x faster                                                             |
| typing_runtime_protocols   | 126 us                                                          | 101 us: 1.25x faster                                                              |
| docutils                   | 1.98 sec                                                        | 1.60 sec: 1.24x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 63.1 ms: 1.23x faster                                                             |
| meteor_contest             | 86.9 ms                                                         | 70.6 ms: 1.23x faster                                                             |
| unpickle                   | 9.71 us                                                         | 8.62 us: 1.13x faster                                                             |
| regex_dna                  | 127 ms                                                          | 117 ms: 1.09x faster                                                              |
| pickle_dict                | 19.9 us                                                         | 18.6 us: 1.07x faster                                                             |
| unpickle_list              | 2.95 us                                                         | 2.78 us: 1.06x faster                                                             |
| pickle_list                | 3.37 us                                                         | 3.18 us: 1.06x faster                                                             |
| pickle                     | 7.79 us                                                         | 7.40 us: 1.05x faster                                                             |
| regex_v8                   | 15.0 ms                                                         | 14.5 ms: 1.04x faster                                                             |
| python_startup_no_site     | 19.1 ms                                                         | 18.8 ms: 1.01x faster                                                             |
| coverage                   | 48.4 ms                                                         | 50.3 ms: 1.04x slower                                                             |
| python_startup             | 22.4 ms                                                         | 25.2 ms: 1.13x slower                                                             |
| bench_mp_pool              | 75.4 ms                                                         | 89.0 ms: 1.18x slower                                                             |
| gc_traversal               | 1.44 ms                                                         | 2.08 ms: 1.44x slower                                                             |
| create_gc_cycles           | 652 us                                                          | 1.26 ms: 1.94x slower                                                             |
| Geometric mean             | (ref)                                                           | 1.53x faster                                                                      |
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20251019-3.15.0a1+-bedaea0-JIT/bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.536x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.54x
- 95% likely to have a speedup of 1.53x
- 99% likely to have a speedup of 1.49x

# Memory
- memory change: unknown