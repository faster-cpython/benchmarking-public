# Results vs. 3.12.0

- fork: python
- ref: 880c9526f91960b9cba5
- machine: windows-amd64
- commit hash: 880c952
- commit date: 2025-10-04
- overall geometric mean: 1.364x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 222 ms: 1.26x faster                                                             |
| docutils       | 1.98 sec                                                        | 2.79 sec: 1.41x slower                                                           |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 324 ms: 2.09x faster                                                             |
| async_tree_io              | 693 ms                                                          | 347 ms: 1.99x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 145 ms: 1.92x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 187 ms: 1.87x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 305 ms: 1.79x faster                                                             |
| async_tree_none            | 298 ms                                                          | 168 ms: 1.77x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 209 ms: 1.74x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 327 ms: 1.72x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.86x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 46.2 ms: 1.66x faster                                                            |
| nbody          | 127 ms                                                          | 78.6 ms: 1.61x faster                                                            |
| pidigits       | 199 ms                                                          | 137 ms: 1.45x faster                                                             |
| Geometric mean | (ref)                                                           | 1.57x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 91.3 ms: 1.41x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.54 ms: 1.33x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 12.7 ms: 1.19x faster                                                            |
| regex_dna      | 127 ms                                                          | 111 ms: 1.14x faster                                                             |
| Geometric mean | (ref)                                                           | 1.26x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 149 us: 1.41x faster                                                             |
| xml_etree_iterparse  | 77.6 ms                                                         | 58.6 ms: 1.32x faster                                                            |
| json_loads           | 20.4 us                                                         | 15.9 us: 1.28x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 224 us: 1.27x faster                                                             |
| xml_etree_parse      | 113 ms                                                          | 90.6 ms: 1.25x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 6.11 ms: 1.21x faster                                                            |
| xml_etree_process    | 53.2 ms                                                         | 44.6 ms: 1.19x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 61.9 ms: 1.17x faster                                                            |
| pickle_list          | 3.37 us                                                         | 3.06 us: 1.10x faster                                                            |
| pickle_dict          | 19.9 us                                                         | 19.8 us: 1.01x faster                                                            |
| unpickle             | 9.71 us                                                         | 10.2 us: 1.05x slower                                                            |
| unpickle_list        | 2.95 us                                                         | 3.17 us: 1.08x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.14x faster                                                                     |

Benchmark hidden because not significant (2): pickle, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.3 ms: 1.01x slower                                                            |
| python_startup         | 22.4 ms                                                         | 25.8 ms: 1.15x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.9 ms                                                         | 26.2 ms: 1.41x faster                                                            |
| mako            | 9.96 ms                                                         | 9.70 ms: 1.03x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.20x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 2.36 sec: 7.49x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 28.9 ms: 3.17x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 324 ms: 2.09x faster                                                             |
| deepcopy_memo              | 38.4 us                                                         | 18.5 us: 2.07x faster                                                            |
| async_tree_io              | 693 ms                                                          | 347 ms: 1.99x faster                                                             |
| deepcopy                   | 360 us                                                          | 184 us: 1.95x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 145 ms: 1.92x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 187 ms: 1.87x faster                                                             |
| generators                 | 38.5 ms                                                         | 20.9 ms: 1.84x faster                                                            |
| mdp                        | 1.91 sec                                                        | 1.05 sec: 1.82x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 305 ms: 1.79x faster                                                             |
| async_tree_none            | 298 ms                                                          | 168 ms: 1.77x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 209 ms: 1.74x faster                                                             |
| unpack_sequence            | 62.5 ns                                                         | 36.1 ns: 1.73x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 327 ms: 1.72x faster                                                             |
| logging_silent             | 101 ns                                                          | 58.9 ns: 1.71x faster                                                            |
| comprehensions             | 19.2 us                                                         | 11.5 us: 1.66x faster                                                            |
| float                      | 76.7 ms                                                         | 46.2 ms: 1.66x faster                                                            |
| nbody                      | 127 ms                                                          | 78.6 ms: 1.61x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 2.06 us: 1.57x faster                                                            |
| go                         | 137 ms                                                          | 89.4 ms: 1.54x faster                                                            |
| scimark_sor                | 130 ms                                                          | 84.8 ms: 1.53x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 2.34 ms: 1.53x faster                                                            |
| hexiom                     | 6.82 ms                                                         | 4.46 ms: 1.53x faster                                                            |
| logging_simple             | 9.75 us                                                         | 6.43 us: 1.52x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 61.5 ms: 1.51x faster                                                            |
| chaos                      | 69.4 ms                                                         | 46.0 ms: 1.51x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.38 us: 1.50x faster                                                            |
| raytrace                   | 308 ms                                                          | 207 ms: 1.48x faster                                                             |
| logging_format             | 10.4 us                                                         | 7.05 us: 1.48x faster                                                            |
| pidigits                   | 199 ms                                                          | 137 ms: 1.45x faster                                                             |
| scimark_fft                | 271 ms                                                          | 188 ms: 1.44x faster                                                             |
| regex_compile              | 129 ms                                                          | 91.3 ms: 1.41x faster                                                            |
| unpickle_pure_python       | 210 us                                                          | 149 us: 1.41x faster                                                             |
| spectral_norm              | 104 ms                                                          | 73.6 ms: 1.41x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 14.8 ms: 1.41x faster                                                            |
| django_template            | 36.9 ms                                                         | 26.2 ms: 1.41x faster                                                            |
| pycparser                  | 978 ms                                                          | 694 ms: 1.41x faster                                                             |
| dulwich_log                | 58.5 ms                                                         | 41.8 ms: 1.40x faster                                                            |
| pyflate                    | 424 ms                                                          | 304 ms: 1.39x faster                                                             |
| json                       | 4.15 ms                                                         | 3.04 ms: 1.37x faster                                                            |
| pprint_safe_repr           | 721 ms                                                          | 542 ms: 1.33x faster                                                             |
| scimark_monte_carlo        | 66.4 ms                                                         | 50.0 ms: 1.33x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.54 ms: 1.33x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 58.6 ms: 1.32x faster                                                            |
| sympy_str                  | 240 ms                                                          | 182 ms: 1.32x faster                                                             |
| sympy_sum                  | 123 ms                                                          | 93.7 ms: 1.31x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.96 ms: 1.30x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 72.0 ms: 1.30x faster                                                            |
| richards                   | 41.3 ms                                                         | 32.1 ms: 1.29x faster                                                            |
| json_loads                 | 20.4 us                                                         | 15.9 us: 1.28x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 13.7 ms: 1.28x faster                                                            |
| sympy_expand               | 398 ms                                                          | 312 ms: 1.28x faster                                                             |
| pickle_pure_python         | 286 us                                                          | 224 us: 1.27x faster                                                             |
| 2to3                       | 280 ms                                                          | 222 ms: 1.26x faster                                                             |
| async_generators           | 313 ms                                                          | 251 ms: 1.25x faster                                                             |
| xml_etree_parse            | 113 ms                                                          | 90.6 ms: 1.25x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 55.7 ms: 1.24x faster                                                            |
| richards_super             | 46.5 ms                                                         | 37.6 ms: 1.24x faster                                                            |
| asyncio_tcp                | 662 ms                                                          | 536 ms: 1.24x faster                                                             |
| json_dumps                 | 7.40 ms                                                         | 6.11 ms: 1.21x faster                                                            |
| gc_traversal               | 1.44 ms                                                         | 1.20 ms: 1.20x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 44.6 ms: 1.19x faster                                                            |
| regex_v8                   | 15.0 ms                                                         | 12.7 ms: 1.19x faster                                                            |
| fannkuch                   | 354 ms                                                          | 301 ms: 1.18x faster                                                             |
| xml_etree_generate         | 72.1 ms                                                         | 61.9 ms: 1.17x faster                                                            |
| regex_dna                  | 127 ms                                                          | 111 ms: 1.14x faster                                                             |
| telco                      | 5.51 ms                                                         | 4.91 ms: 1.12x faster                                                            |
| pickle_list                | 3.37 us                                                         | 3.06 us: 1.10x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 1.03 ms: 1.08x faster                                                            |
| mako                       | 9.96 ms                                                         | 9.70 ms: 1.03x faster                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 74.3 ms: 1.01x faster                                                            |
| pickle_dict                | 19.9 us                                                         | 19.8 us: 1.01x faster                                                            |
| meteor_contest             | 86.9 ms                                                         | 87.7 ms: 1.01x slower                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 19.3 ms: 1.01x slower                                                            |
| typing_runtime_protocols   | 126 us                                                          | 128 us: 1.01x slower                                                             |
| unpickle                   | 9.71 us                                                         | 10.2 us: 1.05x slower                                                            |
| unpickle_list              | 2.95 us                                                         | 3.17 us: 1.08x slower                                                            |
| python_startup             | 22.4 ms                                                         | 25.8 ms: 1.15x slower                                                            |
| coverage                   | 48.4 ms                                                         | 67.7 ms: 1.40x slower                                                            |
| docutils                   | 1.98 sec                                                        | 2.79 sec: 1.41x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.02 ms: 1.56x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.36x faster                                                                     |

Benchmark hidden because not significant (3): pickle, tomli_loads, pprint_pformat
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20251004-3.15.0a0-880c952-NOGIL/bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.364x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: unknown