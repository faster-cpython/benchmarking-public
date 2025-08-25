# Results vs. 3.12.0

- fork: python
- ref: 6fcac09401e336b25833
- machine: windows-amd64
- commit hash: 6fcac09
- commit date: 2025-08-23
- overall geometric mean: 1.339x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 222 ms: 1.26x faster                                                             |
| docutils       | 1.98 sec                                                        | 2.77 sec: 1.40x slower                                                           |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 324 ms: 2.09x faster                                                             |
| async_tree_io              | 693 ms                                                          | 349 ms: 1.99x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 144 ms: 1.92x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 187 ms: 1.87x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 306 ms: 1.79x faster                                                             |
| async_tree_none            | 298 ms                                                          | 170 ms: 1.75x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 209 ms: 1.74x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 328 ms: 1.72x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.85x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 45.5 ms: 1.68x faster                                                            |
| nbody          | 127 ms                                                          | 81.3 ms: 1.56x faster                                                            |
| pidigits       | 199 ms                                                          | 135 ms: 1.48x faster                                                             |
| Geometric mean | (ref)                                                           | 1.57x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 93.8 ms: 1.38x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.49 ms: 1.36x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 12.8 ms: 1.18x faster                                                            |
| regex_dna      | 127 ms                                                          | 111 ms: 1.14x faster                                                             |
| Geometric mean | (ref)                                                           | 1.26x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 156 us: 1.35x faster                                                             |
| xml_etree_iterparse  | 77.6 ms                                                         | 58.3 ms: 1.33x faster                                                            |
| json_loads           | 20.4 us                                                         | 15.7 us: 1.29x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 5.90 ms: 1.25x faster                                                            |
| xml_etree_parse      | 113 ms                                                          | 90.5 ms: 1.25x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 233 us: 1.23x faster                                                             |
| xml_etree_process    | 53.2 ms                                                         | 44.5 ms: 1.20x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 61.7 ms: 1.17x faster                                                            |
| pickle_list          | 3.37 us                                                         | 2.95 us: 1.14x faster                                                            |
| unpickle_list        | 2.95 us                                                         | 3.00 us: 1.02x slower                                                            |
| unpickle             | 9.71 us                                                         | 9.98 us: 1.03x slower                                                            |
| tomli_loads          | 2.20 sec                                                        | 2.60 sec: 1.18x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.13x faster                                                                     |

Benchmark hidden because not significant (2): pickle, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup | 22.4 ms                                                         | 25.5 ms: 1.14x slower                                                            |
| Geometric mean | (ref)                                                           | 1.07x slower                                                                     |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.9 ms                                                         | 27.1 ms: 1.36x faster                                                            |
| mako            | 9.96 ms                                                         | 10.1 ms: 1.01x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.16x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 2.00 sec: 8.82x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 30.2 ms: 3.03x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 324 ms: 2.09x faster                                                             |
| async_tree_io              | 693 ms                                                          | 349 ms: 1.99x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 144 ms: 1.92x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 187 ms: 1.87x faster                                                             |
| deepcopy_memo              | 38.4 us                                                         | 20.7 us: 1.86x faster                                                            |
| deepcopy                   | 360 us                                                          | 200 us: 1.80x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 306 ms: 1.79x faster                                                             |
| mdp                        | 1.91 sec                                                        | 1.07 sec: 1.78x faster                                                           |
| async_tree_none            | 298 ms                                                          | 170 ms: 1.75x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 209 ms: 1.74x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 328 ms: 1.72x faster                                                             |
| float                      | 76.7 ms                                                         | 45.5 ms: 1.68x faster                                                            |
| unpack_sequence            | 62.5 ns                                                         | 37.7 ns: 1.66x faster                                                            |
| logging_silent             | 101 ns                                                          | 61.9 ns: 1.63x faster                                                            |
| comprehensions             | 19.2 us                                                         | 11.9 us: 1.61x faster                                                            |
| asyncio_tcp                | 662 ms                                                          | 423 ms: 1.57x faster                                                             |
| sqlite_synth               | 2.07 us                                                         | 1.33 us: 1.56x faster                                                            |
| nbody                      | 127 ms                                                          | 81.3 ms: 1.56x faster                                                            |
| generators                 | 38.5 ms                                                         | 24.9 ms: 1.55x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 2.12 us: 1.52x faster                                                            |
| chaos                      | 69.4 ms                                                         | 46.3 ms: 1.50x faster                                                            |
| go                         | 137 ms                                                          | 92.1 ms: 1.49x faster                                                            |
| hexiom                     | 6.82 ms                                                         | 4.59 ms: 1.49x faster                                                            |
| pidigits                   | 199 ms                                                          | 135 ms: 1.48x faster                                                             |
| scimark_sor                | 130 ms                                                          | 88.0 ms: 1.47x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 2.43 ms: 1.47x faster                                                            |
| logging_simple             | 9.75 us                                                         | 6.63 us: 1.47x faster                                                            |
| raytrace                   | 308 ms                                                          | 211 ms: 1.46x faster                                                             |
| logging_format             | 10.4 us                                                         | 7.16 us: 1.45x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 40.8 ms: 1.43x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 65.2 ms: 1.43x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 14.8 ms: 1.41x faster                                                            |
| spectral_norm              | 104 ms                                                          | 73.5 ms: 1.41x faster                                                            |
| regex_compile              | 129 ms                                                          | 93.8 ms: 1.38x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.49 ms: 1.36x faster                                                            |
| django_template            | 36.9 ms                                                         | 27.1 ms: 1.36x faster                                                            |
| pycparser                  | 978 ms                                                          | 721 ms: 1.36x faster                                                             |
| json                       | 4.15 ms                                                         | 3.07 ms: 1.35x faster                                                            |
| pyflate                    | 424 ms                                                          | 314 ms: 1.35x faster                                                             |
| unpickle_pure_python       | 210 us                                                          | 156 us: 1.35x faster                                                             |
| xml_etree_iterparse        | 77.6 ms                                                         | 58.3 ms: 1.33x faster                                                            |
| json_loads                 | 20.4 us                                                         | 15.7 us: 1.29x faster                                                            |
| pprint_safe_repr           | 721 ms                                                          | 558 ms: 1.29x faster                                                             |
| scimark_fft                | 271 ms                                                          | 210 ms: 1.29x faster                                                             |
| scimark_monte_carlo        | 66.4 ms                                                         | 51.6 ms: 1.29x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 73.1 ms: 1.28x faster                                                            |
| sympy_str                  | 240 ms                                                          | 187 ms: 1.28x faster                                                             |
| sympy_sum                  | 123 ms                                                          | 96.2 ms: 1.28x faster                                                            |
| 2to3                       | 280 ms                                                          | 222 ms: 1.26x faster                                                             |
| sympy_integrate            | 17.5 ms                                                         | 14.0 ms: 1.26x faster                                                            |
| json_dumps                 | 7.40 ms                                                         | 5.90 ms: 1.25x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 90.5 ms: 1.25x faster                                                            |
| sympy_expand               | 398 ms                                                          | 318 ms: 1.25x faster                                                             |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.09 ms: 1.25x faster                                                            |
| async_generators           | 313 ms                                                          | 254 ms: 1.23x faster                                                             |
| crypto_pyaes               | 69.2 ms                                                         | 56.2 ms: 1.23x faster                                                            |
| gc_traversal               | 1.44 ms                                                         | 1.17 ms: 1.23x faster                                                            |
| pickle_pure_python         | 286 us                                                          | 233 us: 1.23x faster                                                             |
| xml_etree_process          | 53.2 ms                                                         | 44.5 ms: 1.20x faster                                                            |
| regex_v8                   | 15.0 ms                                                         | 12.8 ms: 1.18x faster                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 61.7 ms: 1.17x faster                                                            |
| fannkuch                   | 354 ms                                                          | 304 ms: 1.16x faster                                                             |
| richards                   | 41.3 ms                                                         | 35.9 ms: 1.15x faster                                                            |
| pickle_list                | 3.37 us                                                         | 2.95 us: 1.14x faster                                                            |
| regex_dna                  | 127 ms                                                          | 111 ms: 1.14x faster                                                             |
| telco                      | 5.51 ms                                                         | 4.84 ms: 1.14x faster                                                            |
| richards_super             | 46.5 ms                                                         | 41.1 ms: 1.13x faster                                                            |
| meteor_contest             | 86.9 ms                                                         | 85.7 ms: 1.01x faster                                                            |
| typing_runtime_protocols   | 126 us                                                          | 128 us: 1.01x slower                                                             |
| mako                       | 9.96 ms                                                         | 10.1 ms: 1.01x slower                                                            |
| unpickle_list              | 2.95 us                                                         | 3.00 us: 1.02x slower                                                            |
| unpickle                   | 9.71 us                                                         | 9.98 us: 1.03x slower                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 77.8 ms: 1.03x slower                                                            |
| python_startup             | 22.4 ms                                                         | 25.5 ms: 1.14x slower                                                            |
| tomli_loads                | 2.20 sec                                                        | 2.60 sec: 1.18x slower                                                           |
| coverage                   | 48.4 ms                                                         | 66.8 ms: 1.38x slower                                                            |
| docutils                   | 1.98 sec                                                        | 2.77 sec: 1.40x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 994 us: 1.52x slower                                                             |
| Geometric mean             | (ref)                                                           | 1.35x faster                                                                     |

Benchmark hidden because not significant (5): pickle, pickle_dict, python_startup_no_site, bench_thread_pool, pprint_pformat
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250823-3.15.0a0-6fcac09-NOGIL/bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.339x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: unknown