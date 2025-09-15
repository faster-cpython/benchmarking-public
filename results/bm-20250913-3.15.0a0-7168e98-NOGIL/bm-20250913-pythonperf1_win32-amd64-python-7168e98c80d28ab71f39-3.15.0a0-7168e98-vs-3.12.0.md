# Results vs. 3.12.0

- fork: python
- ref: 7168e98c80d28ab71f39
- machine: windows-amd64
- commit hash: 7168e98
- commit date: 2025-09-13
- overall geometric mean: 1.324x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 227 ms: 1.23x faster                                                             |
| docutils       | 1.98 sec                                                        | 2.84 sec: 1.43x slower                                                           |
| Geometric mean | (ref)                                                           | 1.08x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 339 ms: 2.00x faster                                                             |
| async_tree_io              | 693 ms                                                          | 356 ms: 1.95x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 153 ms: 1.81x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 199 ms: 1.76x faster                                                             |
| async_tree_none            | 298 ms                                                          | 172 ms: 1.73x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 319 ms: 1.71x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 216 ms: 1.69x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 335 ms: 1.68x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.79x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 46.3 ms: 1.65x faster                                                            |
| nbody          | 127 ms                                                          | 81.4 ms: 1.56x faster                                                            |
| pidigits       | 199 ms                                                          | 138 ms: 1.44x faster                                                             |
| Geometric mean | (ref)                                                           | 1.55x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 94.7 ms: 1.36x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.59 ms: 1.29x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 13.3 ms: 1.13x faster                                                            |
| regex_dna      | 127 ms                                                          | 116 ms: 1.10x faster                                                             |
| Geometric mean | (ref)                                                           | 1.22x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 157 us: 1.34x faster                                                             |
| xml_etree_iterparse  | 77.6 ms                                                         | 59.6 ms: 1.30x faster                                                            |
| json_loads           | 20.4 us                                                         | 16.0 us: 1.27x faster                                                            |
| xml_etree_parse      | 113 ms                                                          | 92.9 ms: 1.22x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 6.11 ms: 1.21x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 238 us: 1.20x faster                                                             |
| xml_etree_process    | 53.2 ms                                                         | 44.8 ms: 1.19x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 64.1 ms: 1.13x faster                                                            |
| pickle_list          | 3.37 us                                                         | 3.07 us: 1.10x faster                                                            |
| pickle               | 7.79 us                                                         | 7.91 us: 1.01x slower                                                            |
| pickle_dict          | 19.9 us                                                         | 20.3 us: 1.02x slower                                                            |
| unpickle             | 9.71 us                                                         | 10.0 us: 1.03x slower                                                            |
| unpickle_list        | 2.95 us                                                         | 3.20 us: 1.09x slower                                                            |
| tomli_loads          | 2.20 sec                                                        | 2.41 sec: 1.09x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.11x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup | 22.4 ms                                                         | 25.2 ms: 1.13x slower                                                            |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                     |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.9 ms                                                         | 27.3 ms: 1.35x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.16x faster                                                                     |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 2.21 sec: 7.98x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 29.0 ms: 3.16x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 339 ms: 2.00x faster                                                             |
| deepcopy_memo              | 38.4 us                                                         | 19.5 us: 1.97x faster                                                            |
| async_tree_io              | 693 ms                                                          | 356 ms: 1.95x faster                                                             |
| deepcopy                   | 360 us                                                          | 190 us: 1.89x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 153 ms: 1.81x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 199 ms: 1.76x faster                                                             |
| async_tree_none            | 298 ms                                                          | 172 ms: 1.73x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 319 ms: 1.71x faster                                                             |
| generators                 | 38.5 ms                                                         | 22.7 ms: 1.70x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 216 ms: 1.69x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 335 ms: 1.68x faster                                                             |
| float                      | 76.7 ms                                                         | 46.3 ms: 1.65x faster                                                            |
| mdp                        | 1.91 sec                                                        | 1.16 sec: 1.65x faster                                                           |
| logging_silent             | 101 ns                                                          | 61.5 ns: 1.64x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 2.05 us: 1.57x faster                                                            |
| nbody                      | 127 ms                                                          | 81.4 ms: 1.56x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.35 us: 1.54x faster                                                            |
| comprehensions             | 19.2 us                                                         | 12.5 us: 1.53x faster                                                            |
| asyncio_tcp                | 662 ms                                                          | 441 ms: 1.50x faster                                                             |
| go                         | 137 ms                                                          | 91.4 ms: 1.50x faster                                                            |
| scimark_sor                | 130 ms                                                          | 87.1 ms: 1.49x faster                                                            |
| unpack_sequence            | 62.5 ns                                                         | 42.1 ns: 1.48x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 2.42 ms: 1.48x faster                                                            |
| spectral_norm              | 104 ms                                                          | 70.1 ms: 1.48x faster                                                            |
| hexiom                     | 6.82 ms                                                         | 4.65 ms: 1.47x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 14.3 ms: 1.46x faster                                                            |
| logging_simple             | 9.75 us                                                         | 6.72 us: 1.45x faster                                                            |
| chaos                      | 69.4 ms                                                         | 47.8 ms: 1.45x faster                                                            |
| pidigits                   | 199 ms                                                          | 138 ms: 1.44x faster                                                             |
| logging_format             | 10.4 us                                                         | 7.22 us: 1.44x faster                                                            |
| raytrace                   | 308 ms                                                          | 214 ms: 1.44x faster                                                             |
| scimark_lu                 | 93.2 ms                                                         | 65.4 ms: 1.42x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 42.9 ms: 1.36x faster                                                            |
| regex_compile              | 129 ms                                                          | 94.7 ms: 1.36x faster                                                            |
| django_template            | 36.9 ms                                                         | 27.3 ms: 1.35x faster                                                            |
| json                       | 4.15 ms                                                         | 3.09 ms: 1.34x faster                                                            |
| pyflate                    | 424 ms                                                          | 316 ms: 1.34x faster                                                             |
| unpickle_pure_python       | 210 us                                                          | 157 us: 1.34x faster                                                             |
| scimark_monte_carlo        | 66.4 ms                                                         | 50.9 ms: 1.31x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 59.6 ms: 1.30x faster                                                            |
| pycparser                  | 978 ms                                                          | 761 ms: 1.29x faster                                                             |
| regex_effbot               | 2.04 ms                                                         | 1.59 ms: 1.29x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 73.2 ms: 1.28x faster                                                            |
| scimark_fft                | 271 ms                                                          | 212 ms: 1.28x faster                                                             |
| pprint_safe_repr           | 721 ms                                                          | 565 ms: 1.28x faster                                                             |
| json_loads                 | 20.4 us                                                         | 16.0 us: 1.27x faster                                                            |
| sympy_sum                  | 123 ms                                                          | 97.0 ms: 1.27x faster                                                            |
| sympy_str                  | 240 ms                                                          | 189 ms: 1.27x faster                                                             |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.09 ms: 1.25x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 14.1 ms: 1.25x faster                                                            |
| sympy_expand               | 398 ms                                                          | 319 ms: 1.25x faster                                                             |
| richards                   | 41.3 ms                                                         | 33.2 ms: 1.24x faster                                                            |
| 2to3                       | 280 ms                                                          | 227 ms: 1.23x faster                                                             |
| xml_etree_parse            | 113 ms                                                          | 92.9 ms: 1.22x faster                                                            |
| json_dumps                 | 7.40 ms                                                         | 6.11 ms: 1.21x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 57.6 ms: 1.20x faster                                                            |
| pickle_pure_python         | 286 us                                                          | 238 us: 1.20x faster                                                             |
| richards_super             | 46.5 ms                                                         | 39.1 ms: 1.19x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 44.8 ms: 1.19x faster                                                            |
| async_generators           | 313 ms                                                          | 265 ms: 1.18x faster                                                             |
| telco                      | 5.51 ms                                                         | 4.80 ms: 1.15x faster                                                            |
| fannkuch                   | 354 ms                                                          | 309 ms: 1.15x faster                                                             |
| gc_traversal               | 1.44 ms                                                         | 1.27 ms: 1.14x faster                                                            |
| regex_v8                   | 15.0 ms                                                         | 13.3 ms: 1.13x faster                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 64.1 ms: 1.13x faster                                                            |
| pickle_list                | 3.37 us                                                         | 3.07 us: 1.10x faster                                                            |
| regex_dna                  | 127 ms                                                          | 116 ms: 1.10x faster                                                             |
| pickle                     | 7.79 us                                                         | 7.91 us: 1.01x slower                                                            |
| meteor_contest             | 86.9 ms                                                         | 88.2 ms: 1.02x slower                                                            |
| pickle_dict                | 19.9 us                                                         | 20.3 us: 1.02x slower                                                            |
| unpickle                   | 9.71 us                                                         | 10.0 us: 1.03x slower                                                            |
| typing_runtime_protocols   | 126 us                                                          | 132 us: 1.04x slower                                                             |
| unpickle_list              | 2.95 us                                                         | 3.20 us: 1.09x slower                                                            |
| tomli_loads                | 2.20 sec                                                        | 2.41 sec: 1.09x slower                                                           |
| python_startup             | 22.4 ms                                                         | 25.2 ms: 1.13x slower                                                            |
| pprint_pformat             | 1.50 sec                                                        | 1.73 sec: 1.16x slower                                                           |
| coverage                   | 48.4 ms                                                         | 67.6 ms: 1.39x slower                                                            |
| docutils                   | 1.98 sec                                                        | 2.84 sec: 1.43x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.01 ms: 1.56x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.33x faster                                                                     |

Benchmark hidden because not significant (4): python_startup_no_site, bench_mp_pool, mako, bench_thread_pool
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250913-3.15.0a0-7168e98-NOGIL/bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.324x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: unknown