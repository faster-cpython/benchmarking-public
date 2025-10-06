# Results vs. 3.12.0

- fork: python
- ref: 880c9526f91960b9cba5
- machine: windows-amd64
- commit hash: 880c952
- commit date: 2025-10-04
- overall geometric mean: 1.476x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.43x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 217 ms: 1.29x faster                                                             |
| docutils       | 1.98 sec                                                        | 1.60 sec: 1.24x faster                                                           |
| Geometric mean | (ref)                                                           | 1.27x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io              | 693 ms                                                          | 386 ms: 1.79x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 204 ms: 1.78x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 388 ms: 1.74x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 327 ms: 1.73x faster                                                             |
| async_tree_none            | 298 ms                                                          | 175 ms: 1.70x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 209 ms: 1.68x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 169 ms: 1.64x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 341 ms: 1.60x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.71x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 63.5 ms: 2.00x faster                                                            |
| float          | 76.7 ms                                                         | 43.4 ms: 1.77x faster                                                            |
| pidigits       | 199 ms                                                          | 146 ms: 1.37x faster                                                             |
| Geometric mean | (ref)                                                           | 1.69x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 80.1 ms: 1.61x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.56 ms: 1.31x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 14.0 ms: 1.08x faster                                                            |
| regex_dna      | 127 ms                                                          | 120 ms: 1.06x faster                                                             |
| Geometric mean | (ref)                                                           | 1.25x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.37 sec: 1.60x faster                                                           |
| unpickle_pure_python | 210 us                                                          | 135 us: 1.55x faster                                                             |
| json_loads           | 20.4 us                                                         | 14.0 us: 1.45x faster                                                            |
| xml_etree_process    | 53.2 ms                                                         | 38.6 ms: 1.38x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 210 us: 1.36x faster                                                             |
| json_dumps           | 7.40 ms                                                         | 5.50 ms: 1.35x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 55.2 ms: 1.31x faster                                                            |
| xml_etree_parse      | 113 ms                                                          | 86.5 ms: 1.31x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 62.7 ms: 1.24x faster                                                            |
| unpickle             | 9.71 us                                                         | 8.68 us: 1.12x faster                                                            |
| pickle_list          | 3.37 us                                                         | 3.24 us: 1.04x faster                                                            |
| unpickle_list        | 2.95 us                                                         | 2.84 us: 1.04x faster                                                            |
| pickle_dict          | 19.9 us                                                         | 19.3 us: 1.03x faster                                                            |
| pickle               | 7.79 us                                                         | 7.71 us: 1.01x faster                                                            |
| Geometric mean       | (ref)                                                           | 1.26x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup | 22.4 ms                                                         | 25.3 ms: 1.13x slower                                                            |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                     |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.9 ms                                                         | 24.4 ms: 1.51x faster                                                            |
| mako            | 9.96 ms                                                         | 6.80 ms: 1.46x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.49x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 1.24 sec: 14.26x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 29.1 ms: 3.15x faster                                                            |
| mdp                        | 1.91 sec                                                        | 798 ms: 2.39x faster                                                             |
| deepcopy_memo              | 38.4 us                                                         | 16.7 us: 2.29x faster                                                            |
| deepcopy                   | 360 us                                                          | 167 us: 2.16x faster                                                             |
| nbody                      | 127 ms                                                          | 63.5 ms: 2.00x faster                                                            |
| generators                 | 38.5 ms                                                         | 19.5 ms: 1.98x faster                                                            |
| unpack_sequence            | 62.5 ns                                                         | 32.0 ns: 1.95x faster                                                            |
| logging_silent             | 101 ns                                                          | 55.8 ns: 1.81x faster                                                            |
| async_tree_io              | 693 ms                                                          | 386 ms: 1.79x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 204 ms: 1.78x faster                                                             |
| deepcopy_reduce            | 3.23 us                                                         | 1.81 us: 1.78x faster                                                            |
| go                         | 137 ms                                                          | 77.6 ms: 1.77x faster                                                            |
| float                      | 76.7 ms                                                         | 43.4 ms: 1.77x faster                                                            |
| comprehensions             | 19.2 us                                                         | 11.0 us: 1.74x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 388 ms: 1.74x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 327 ms: 1.73x faster                                                             |
| raytrace                   | 308 ms                                                          | 179 ms: 1.72x faster                                                             |
| chaos                      | 69.4 ms                                                         | 40.5 ms: 1.71x faster                                                            |
| async_tree_none            | 298 ms                                                          | 175 ms: 1.70x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 209 ms: 1.68x faster                                                             |
| hexiom                     | 6.82 ms                                                         | 4.10 ms: 1.66x faster                                                            |
| scimark_sor                | 130 ms                                                          | 78.3 ms: 1.66x faster                                                            |
| logging_simple             | 9.75 us                                                         | 5.92 us: 1.65x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 169 ms: 1.64x faster                                                             |
| deltablue                  | 3.58 ms                                                         | 2.19 ms: 1.64x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 40.6 ms: 1.64x faster                                                            |
| logging_format             | 10.4 us                                                         | 6.43 us: 1.62x faster                                                            |
| scimark_fft                | 271 ms                                                          | 168 ms: 1.61x faster                                                             |
| regex_compile              | 129 ms                                                          | 80.1 ms: 1.61x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 341 ms: 1.60x faster                                                             |
| tomli_loads                | 2.20 sec                                                        | 1.37 sec: 1.60x faster                                                           |
| asyncio_tcp                | 662 ms                                                          | 416 ms: 1.59x faster                                                             |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.43 ms: 1.59x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 58.9 ms: 1.58x faster                                                            |
| spectral_norm              | 104 ms                                                          | 66.9 ms: 1.55x faster                                                            |
| unpickle_pure_python       | 210 us                                                          | 135 us: 1.55x faster                                                             |
| pprint_pformat             | 1.50 sec                                                        | 986 ms: 1.52x faster                                                             |
| richards_super             | 46.5 ms                                                         | 30.6 ms: 1.52x faster                                                            |
| richards                   | 41.3 ms                                                         | 27.2 ms: 1.52x faster                                                            |
| django_template            | 36.9 ms                                                         | 24.4 ms: 1.51x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 62.3 ms: 1.50x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 39.1 ms: 1.50x faster                                                            |
| pyflate                    | 424 ms                                                          | 287 ms: 1.48x faster                                                             |
| pprint_safe_repr           | 721 ms                                                          | 488 ms: 1.48x faster                                                             |
| mako                       | 9.96 ms                                                         | 6.80 ms: 1.46x faster                                                            |
| json_loads                 | 20.4 us                                                         | 14.0 us: 1.45x faster                                                            |
| sympy_str                  | 240 ms                                                          | 165 ms: 1.45x faster                                                             |
| crypto_pyaes               | 69.2 ms                                                         | 47.7 ms: 1.45x faster                                                            |
| sympy_sum                  | 123 ms                                                          | 84.9 ms: 1.45x faster                                                            |
| json                       | 4.15 ms                                                         | 2.88 ms: 1.44x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 12.2 ms: 1.44x faster                                                            |
| sympy_expand               | 398 ms                                                          | 282 ms: 1.41x faster                                                             |
| coroutines                 | 20.9 ms                                                         | 14.8 ms: 1.41x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 38.6 ms: 1.38x faster                                                            |
| pycparser                  | 978 ms                                                          | 712 ms: 1.37x faster                                                             |
| pidigits                   | 199 ms                                                          | 146 ms: 1.37x faster                                                             |
| async_generators           | 313 ms                                                          | 230 ms: 1.36x faster                                                             |
| pickle_pure_python         | 286 us                                                          | 210 us: 1.36x faster                                                             |
| json_dumps                 | 7.40 ms                                                         | 5.50 ms: 1.35x faster                                                            |
| fannkuch                   | 354 ms                                                          | 267 ms: 1.32x faster                                                             |
| sqlite_synth               | 2.07 us                                                         | 1.57 us: 1.32x faster                                                            |
| telco                      | 5.51 ms                                                         | 4.18 ms: 1.32x faster                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 55.2 ms: 1.31x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 86.5 ms: 1.31x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.56 ms: 1.31x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 846 us: 1.30x faster                                                             |
| 2to3                       | 280 ms                                                          | 217 ms: 1.29x faster                                                             |
| docutils                   | 1.98 sec                                                        | 1.60 sec: 1.24x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 62.7 ms: 1.24x faster                                                            |
| typing_runtime_protocols   | 126 us                                                          | 105 us: 1.21x faster                                                             |
| meteor_contest             | 86.9 ms                                                         | 72.1 ms: 1.20x faster                                                            |
| unpickle                   | 9.71 us                                                         | 8.68 us: 1.12x faster                                                            |
| regex_v8                   | 15.0 ms                                                         | 14.0 ms: 1.08x faster                                                            |
| regex_dna                  | 127 ms                                                          | 120 ms: 1.06x faster                                                             |
| pickle_list                | 3.37 us                                                         | 3.24 us: 1.04x faster                                                            |
| unpickle_list              | 2.95 us                                                         | 2.84 us: 1.04x faster                                                            |
| pickle_dict                | 19.9 us                                                         | 19.3 us: 1.03x faster                                                            |
| pickle                     | 7.79 us                                                         | 7.71 us: 1.01x faster                                                            |
| coverage                   | 48.4 ms                                                         | 49.0 ms: 1.01x slower                                                            |
| python_startup             | 22.4 ms                                                         | 25.3 ms: 1.13x slower                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 89.5 ms: 1.19x slower                                                            |
| gc_traversal               | 1.44 ms                                                         | 2.08 ms: 1.44x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.26 ms: 1.94x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.48x faster                                                                     |

Benchmark hidden because not significant (1): python_startup_no_site
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20251004-3.15.0a0-880c952/bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.476x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.47x
- 95% likely to have a speedup of 1.45x
- 99% likely to have a speedup of 1.43x

# Memory
- memory change: unknown