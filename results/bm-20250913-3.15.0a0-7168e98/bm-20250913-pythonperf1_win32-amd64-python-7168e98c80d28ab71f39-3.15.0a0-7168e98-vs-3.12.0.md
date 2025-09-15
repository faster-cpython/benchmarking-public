# Results vs. 3.12.0

- fork: python
- ref: 7168e98c80d28ab71f39
- machine: windows-amd64
- commit hash: 7168e98
- commit date: 2025-09-13
- overall geometric mean: 1.476x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.42x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 216 ms: 1.29x faster                                                             |
| docutils       | 1.98 sec                                                        | 1.61 sec: 1.23x faster                                                           |
| Geometric mean | (ref)                                                           | 1.26x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization     | 364 ms                                                          | 199 ms: 1.83x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 377 ms: 1.79x faster                                                             |
| async_tree_io              | 693 ms                                                          | 388 ms: 1.79x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 324 ms: 1.74x faster                                                             |
| async_tree_none            | 298 ms                                                          | 172 ms: 1.73x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 204 ms: 1.71x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 164 ms: 1.69x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 331 ms: 1.65x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.74x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 65.3 ms: 1.94x faster                                                            |
| float          | 76.7 ms                                                         | 42.7 ms: 1.80x faster                                                            |
| pidigits       | 199 ms                                                          | 148 ms: 1.34x faster                                                             |
| Geometric mean | (ref)                                                           | 1.67x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 79.8 ms: 1.62x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.61 ms: 1.26x faster                                                            |
| regex_dna      | 127 ms                                                          | 120 ms: 1.06x faster                                                             |
| regex_v8       | 15.0 ms                                                         | 14.4 ms: 1.05x faster                                                            |
| Geometric mean | (ref)                                                           | 1.23x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.35 sec: 1.63x faster                                                           |
| unpickle_pure_python | 210 us                                                          | 135 us: 1.56x faster                                                             |
| json_loads           | 20.4 us                                                         | 14.3 us: 1.43x faster                                                            |
| xml_etree_process    | 53.2 ms                                                         | 38.7 ms: 1.38x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 5.46 ms: 1.36x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 212 us: 1.35x faster                                                             |
| xml_etree_generate   | 72.1 ms                                                         | 55.4 ms: 1.30x faster                                                            |
| xml_etree_parse      | 113 ms                                                          | 88.9 ms: 1.27x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 63.9 ms: 1.21x faster                                                            |
| unpickle             | 9.71 us                                                         | 8.52 us: 1.14x faster                                                            |
| unpickle_list        | 2.95 us                                                         | 2.84 us: 1.04x faster                                                            |
| pickle_list          | 3.37 us                                                         | 3.27 us: 1.03x faster                                                            |
| pickle_dict          | 19.9 us                                                         | 19.7 us: 1.01x faster                                                            |
| Geometric mean       | (ref)                                                           | 1.25x faster                                                                     |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 18.9 ms: 1.01x faster                                                            |
| python_startup         | 22.4 ms                                                         | 25.5 ms: 1.14x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.06x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 6.51 ms: 1.53x faster                                                            |
| django_template | 36.9 ms                                                         | 24.5 ms: 1.51x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.52x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 1.32 sec: 13.35x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 28.8 ms: 3.17x faster                                                            |
| mdp                        | 1.91 sec                                                        | 810 ms: 2.36x faster                                                             |
| deepcopy_memo              | 38.4 us                                                         | 16.5 us: 2.33x faster                                                            |
| deepcopy                   | 360 us                                                          | 165 us: 2.19x faster                                                             |
| unpack_sequence            | 62.5 ns                                                         | 31.1 ns: 2.01x faster                                                            |
| generators                 | 38.5 ms                                                         | 19.3 ms: 2.00x faster                                                            |
| nbody                      | 127 ms                                                          | 65.3 ms: 1.94x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 199 ms: 1.83x faster                                                             |
| go                         | 137 ms                                                          | 75.7 ms: 1.81x faster                                                            |
| float                      | 76.7 ms                                                         | 42.7 ms: 1.80x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 377 ms: 1.79x faster                                                             |
| deepcopy_reduce            | 3.23 us                                                         | 1.80 us: 1.79x faster                                                            |
| logging_silent             | 101 ns                                                          | 56.5 ns: 1.79x faster                                                            |
| async_tree_io              | 693 ms                                                          | 388 ms: 1.79x faster                                                             |
| comprehensions             | 19.2 us                                                         | 10.9 us: 1.75x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 324 ms: 1.74x faster                                                             |
| async_tree_none            | 298 ms                                                          | 172 ms: 1.73x faster                                                             |
| raytrace                   | 308 ms                                                          | 178 ms: 1.73x faster                                                             |
| chaos                      | 69.4 ms                                                         | 40.4 ms: 1.72x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 204 ms: 1.71x faster                                                             |
| scimark_sor                | 130 ms                                                          | 76.1 ms: 1.71x faster                                                            |
| hexiom                     | 6.82 ms                                                         | 4.00 ms: 1.71x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 39.3 ms: 1.69x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 164 ms: 1.69x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 331 ms: 1.65x faster                                                             |
| spectral_norm              | 104 ms                                                          | 63.4 ms: 1.64x faster                                                            |
| tomli_loads                | 2.20 sec                                                        | 1.35 sec: 1.63x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.21 ms: 1.62x faster                                                            |
| regex_compile              | 129 ms                                                          | 79.8 ms: 1.62x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 57.7 ms: 1.62x faster                                                            |
| logging_simple             | 9.75 us                                                         | 6.08 us: 1.60x faster                                                            |
| logging_format             | 10.4 us                                                         | 6.55 us: 1.59x faster                                                            |
| unpickle_pure_python       | 210 us                                                          | 135 us: 1.56x faster                                                             |
| richards                   | 41.3 ms                                                         | 27.0 ms: 1.53x faster                                                            |
| mako                       | 9.96 ms                                                         | 6.51 ms: 1.53x faster                                                            |
| scimark_fft                | 271 ms                                                          | 178 ms: 1.52x faster                                                             |
| nqueens                    | 93.7 ms                                                         | 61.8 ms: 1.52x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.55 ms: 1.51x faster                                                            |
| pprint_pformat             | 1.50 sec                                                        | 992 ms: 1.51x faster                                                             |
| django_template            | 36.9 ms                                                         | 24.5 ms: 1.51x faster                                                            |
| pyflate                    | 424 ms                                                          | 282 ms: 1.50x faster                                                             |
| richards_super             | 46.5 ms                                                         | 31.0 ms: 1.50x faster                                                            |
| pprint_safe_repr           | 721 ms                                                          | 488 ms: 1.48x faster                                                             |
| crypto_pyaes               | 69.2 ms                                                         | 47.6 ms: 1.45x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 40.4 ms: 1.45x faster                                                            |
| sympy_str                  | 240 ms                                                          | 168 ms: 1.43x faster                                                             |
| json_loads                 | 20.4 us                                                         | 14.3 us: 1.43x faster                                                            |
| json                       | 4.15 ms                                                         | 2.91 ms: 1.43x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 12.4 ms: 1.42x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 14.7 ms: 1.42x faster                                                            |
| sympy_sum                  | 123 ms                                                          | 86.8 ms: 1.42x faster                                                            |
| sympy_expand               | 398 ms                                                          | 286 ms: 1.39x faster                                                             |
| async_generators           | 313 ms                                                          | 227 ms: 1.38x faster                                                             |
| pycparser                  | 978 ms                                                          | 710 ms: 1.38x faster                                                             |
| xml_etree_process          | 53.2 ms                                                         | 38.7 ms: 1.38x faster                                                            |
| json_dumps                 | 7.40 ms                                                         | 5.46 ms: 1.36x faster                                                            |
| pickle_pure_python         | 286 us                                                          | 212 us: 1.35x faster                                                             |
| pidigits                   | 199 ms                                                          | 148 ms: 1.34x faster                                                             |
| asyncio_tcp                | 662 ms                                                          | 494 ms: 1.34x faster                                                             |
| sqlite_synth               | 2.07 us                                                         | 1.57 us: 1.32x faster                                                            |
| fannkuch                   | 354 ms                                                          | 268 ms: 1.32x faster                                                             |
| telco                      | 5.51 ms                                                         | 4.23 ms: 1.30x faster                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 55.4 ms: 1.30x faster                                                            |
| 2to3                       | 280 ms                                                          | 216 ms: 1.29x faster                                                             |
| bench_thread_pool          | 1.10 ms                                                         | 861 us: 1.28x faster                                                             |
| xml_etree_parse            | 113 ms                                                          | 88.9 ms: 1.27x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.61 ms: 1.26x faster                                                            |
| docutils                   | 1.98 sec                                                        | 1.61 sec: 1.23x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 63.9 ms: 1.21x faster                                                            |
| typing_runtime_protocols   | 126 us                                                          | 104 us: 1.21x faster                                                             |
| meteor_contest             | 86.9 ms                                                         | 72.2 ms: 1.20x faster                                                            |
| unpickle                   | 9.71 us                                                         | 8.52 us: 1.14x faster                                                            |
| regex_dna                  | 127 ms                                                          | 120 ms: 1.06x faster                                                             |
| regex_v8                   | 15.0 ms                                                         | 14.4 ms: 1.05x faster                                                            |
| unpickle_list              | 2.95 us                                                         | 2.84 us: 1.04x faster                                                            |
| pickle_list                | 3.37 us                                                         | 3.27 us: 1.03x faster                                                            |
| pickle_dict                | 19.9 us                                                         | 19.7 us: 1.01x faster                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 18.9 ms: 1.01x faster                                                            |
| coverage                   | 48.4 ms                                                         | 50.8 ms: 1.05x slower                                                            |
| python_startup             | 22.4 ms                                                         | 25.5 ms: 1.14x slower                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 89.9 ms: 1.19x slower                                                            |
| gc_traversal               | 1.44 ms                                                         | 2.06 ms: 1.43x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.29 ms: 1.97x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.48x faster                                                                     |

Benchmark hidden because not significant (1): pickle
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250913-3.15.0a0-7168e98/bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.476x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.46x
- 95% likely to have a speedup of 1.44x
- 99% likely to have a speedup of 1.42x

# Memory
- memory change: unknown