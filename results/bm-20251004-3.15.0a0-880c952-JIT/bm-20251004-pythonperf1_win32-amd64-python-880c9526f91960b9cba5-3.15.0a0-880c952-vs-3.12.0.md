# Results vs. 3.12.0

- fork: python
- ref: 880c9526f91960b9cba5
- machine: windows-amd64
- commit hash: 880c952
- commit date: 2025-10-04
- overall geometric mean: 1.541x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.49x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 213 ms: 1.31x faster                                                             |
| docutils       | 1.98 sec                                                        | 1.61 sec: 1.23x faster                                                           |
| Geometric mean | (ref)                                                           | 1.27x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization     | 364 ms                                                          | 200 ms: 1.82x faster                                                             |
| async_tree_io              | 693 ms                                                          | 382 ms: 1.81x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 376 ms: 1.80x faster                                                             |
| async_tree_none            | 298 ms                                                          | 170 ms: 1.75x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 164 ms: 1.69x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 336 ms: 1.68x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 210 ms: 1.67x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 341 ms: 1.60x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.73x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 53.6 ms: 2.37x faster                                                            |
| float          | 76.7 ms                                                         | 43.0 ms: 1.78x faster                                                            |
| pidigits       | 199 ms                                                          | 148 ms: 1.35x faster                                                             |
| Geometric mean | (ref)                                                           | 1.79x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 76.4 ms: 1.69x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.55 ms: 1.32x faster                                                            |
| regex_dna      | 127 ms                                                          | 114 ms: 1.12x faster                                                             |
| regex_v8       | 15.0 ms                                                         | 13.7 ms: 1.10x faster                                                            |
| Geometric mean | (ref)                                                           | 1.29x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.08 sec: 2.03x faster                                                           |
| unpickle_pure_python | 210 us                                                          | 105 us: 2.00x faster                                                             |
| xml_etree_process    | 53.2 ms                                                         | 34.5 ms: 1.54x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 48.8 ms: 1.48x faster                                                            |
| json_loads           | 20.4 us                                                         | 13.9 us: 1.46x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 201 us: 1.42x faster                                                             |
| json_dumps           | 7.40 ms                                                         | 5.38 ms: 1.38x faster                                                            |
| xml_etree_parse      | 113 ms                                                          | 86.6 ms: 1.31x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 60.3 ms: 1.29x faster                                                            |
| unpickle             | 9.71 us                                                         | 8.70 us: 1.12x faster                                                            |
| unpickle_list        | 2.95 us                                                         | 2.70 us: 1.09x faster                                                            |
| pickle_list          | 3.37 us                                                         | 3.28 us: 1.03x faster                                                            |
| pickle_dict          | 19.9 us                                                         | 19.6 us: 1.02x faster                                                            |
| Geometric mean       | (ref)                                                           | 1.33x faster                                                                     |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup | 22.4 ms                                                         | 25.4 ms: 1.14x slower                                                            |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                     |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.33 ms: 1.87x faster                                                            |
| django_template | 36.9 ms                                                         | 24.4 ms: 1.51x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.68x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 1.39 sec: 12.73x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 29.4 ms: 3.11x faster                                                            |
| mdp                        | 1.91 sec                                                        | 784 ms: 2.44x faster                                                             |
| deepcopy_memo              | 38.4 us                                                         | 16.1 us: 2.38x faster                                                            |
| nbody                      | 127 ms                                                          | 53.6 ms: 2.37x faster                                                            |
| deepcopy                   | 360 us                                                          | 162 us: 2.22x faster                                                             |
| tomli_loads                | 2.20 sec                                                        | 1.08 sec: 2.03x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 105 us: 2.00x faster                                                             |
| scimark_fft                | 271 ms                                                          | 136 ms: 1.99x faster                                                             |
| generators                 | 38.5 ms                                                         | 19.4 ms: 1.98x faster                                                            |
| mako                       | 9.96 ms                                                         | 5.33 ms: 1.87x faster                                                            |
| comprehensions             | 19.2 us                                                         | 10.5 us: 1.84x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 1.76 us: 1.83x faster                                                            |
| logging_silent             | 101 ns                                                          | 55.2 ns: 1.83x faster                                                            |
| go                         | 137 ms                                                          | 75.2 ms: 1.83x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 200 ms: 1.82x faster                                                             |
| async_tree_io              | 693 ms                                                          | 382 ms: 1.81x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 376 ms: 1.80x faster                                                             |
| pprint_pformat             | 1.50 sec                                                        | 835 ms: 1.80x faster                                                             |
| float                      | 76.7 ms                                                         | 43.0 ms: 1.78x faster                                                            |
| raytrace                   | 308 ms                                                          | 174 ms: 1.77x faster                                                             |
| pprint_safe_repr           | 721 ms                                                          | 409 ms: 1.76x faster                                                             |
| unpack_sequence            | 62.5 ns                                                         | 35.6 ns: 1.75x faster                                                            |
| async_tree_none            | 298 ms                                                          | 170 ms: 1.75x faster                                                             |
| chaos                      | 69.4 ms                                                         | 40.0 ms: 1.73x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.23 ms: 1.73x faster                                                            |
| pyflate                    | 424 ms                                                          | 246 ms: 1.72x faster                                                             |
| logging_simple             | 9.75 us                                                         | 5.73 us: 1.70x faster                                                            |
| hexiom                     | 6.82 ms                                                         | 4.03 ms: 1.69x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 164 ms: 1.69x faster                                                             |
| regex_compile              | 129 ms                                                          | 76.4 ms: 1.69x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 336 ms: 1.68x faster                                                             |
| scimark_sor                | 130 ms                                                          | 77.5 ms: 1.68x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 210 ms: 1.67x faster                                                             |
| scimark_monte_carlo        | 66.4 ms                                                         | 39.9 ms: 1.67x faster                                                            |
| logging_format             | 10.4 us                                                         | 6.29 us: 1.65x faster                                                            |
| fannkuch                   | 354 ms                                                          | 217 ms: 1.63x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 341 ms: 1.60x faster                                                             |
| scimark_lu                 | 93.2 ms                                                         | 58.3 ms: 1.60x faster                                                            |
| spectral_norm              | 104 ms                                                          | 65.0 ms: 1.60x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 44.1 ms: 1.57x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 59.7 ms: 1.57x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 2.30 ms: 1.56x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 34.5 ms: 1.54x faster                                                            |
| richards                   | 41.3 ms                                                         | 27.0 ms: 1.53x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 38.2 ms: 1.53x faster                                                            |
| richards_super             | 46.5 ms                                                         | 30.5 ms: 1.52x faster                                                            |
| django_template            | 36.9 ms                                                         | 24.4 ms: 1.51x faster                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 48.8 ms: 1.48x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 14.2 ms: 1.47x faster                                                            |
| sympy_sum                  | 123 ms                                                          | 83.9 ms: 1.47x faster                                                            |
| json_loads                 | 20.4 us                                                         | 13.9 us: 1.46x faster                                                            |
| pycparser                  | 978 ms                                                          | 676 ms: 1.45x faster                                                             |
| json                       | 4.15 ms                                                         | 2.88 ms: 1.44x faster                                                            |
| sympy_str                  | 240 ms                                                          | 166 ms: 1.44x faster                                                             |
| pickle_pure_python         | 286 us                                                          | 201 us: 1.42x faster                                                             |
| sympy_integrate            | 17.5 ms                                                         | 12.3 ms: 1.42x faster                                                            |
| telco                      | 5.51 ms                                                         | 3.90 ms: 1.41x faster                                                            |
| sympy_expand               | 398 ms                                                          | 285 ms: 1.40x faster                                                             |
| json_dumps                 | 7.40 ms                                                         | 5.38 ms: 1.38x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.53 us: 1.35x faster                                                            |
| pidigits                   | 199 ms                                                          | 148 ms: 1.35x faster                                                             |
| bench_thread_pool          | 1.10 ms                                                         | 818 us: 1.35x faster                                                             |
| asyncio_tcp                | 662 ms                                                          | 496 ms: 1.33x faster                                                             |
| regex_effbot               | 2.04 ms                                                         | 1.55 ms: 1.32x faster                                                            |
| 2to3                       | 280 ms                                                          | 213 ms: 1.31x faster                                                             |
| async_generators           | 313 ms                                                          | 240 ms: 1.31x faster                                                             |
| xml_etree_parse            | 113 ms                                                          | 86.6 ms: 1.31x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 60.3 ms: 1.29x faster                                                            |
| typing_runtime_protocols   | 126 us                                                          | 101 us: 1.25x faster                                                             |
| docutils                   | 1.98 sec                                                        | 1.61 sec: 1.23x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 72.5 ms: 1.20x faster                                                            |
| regex_dna                  | 127 ms                                                          | 114 ms: 1.12x faster                                                             |
| unpickle                   | 9.71 us                                                         | 8.70 us: 1.12x faster                                                            |
| regex_v8                   | 15.0 ms                                                         | 13.7 ms: 1.10x faster                                                            |
| unpickle_list              | 2.95 us                                                         | 2.70 us: 1.09x faster                                                            |
| pickle_list                | 3.37 us                                                         | 3.28 us: 1.03x faster                                                            |
| pickle_dict                | 19.9 us                                                         | 19.6 us: 1.02x faster                                                            |
| python_startup             | 22.4 ms                                                         | 25.4 ms: 1.14x slower                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 88.5 ms: 1.17x slower                                                            |
| gc_traversal               | 1.44 ms                                                         | 2.06 ms: 1.43x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.27 ms: 1.96x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.53x faster                                                                     |

Benchmark hidden because not significant (3): python_startup_no_site, coverage, pickle
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20251004-3.15.0a0-880c952-JIT/bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.541x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.54x
- 95% likely to have a speedup of 1.53x
- 99% likely to have a speedup of 1.49x

# Memory
- memory change: unknown