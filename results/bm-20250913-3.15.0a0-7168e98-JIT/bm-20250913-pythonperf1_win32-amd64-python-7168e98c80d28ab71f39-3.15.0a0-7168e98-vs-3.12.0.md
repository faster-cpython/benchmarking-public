# Results vs. 3.12.0

- fork: python
- ref: 7168e98c80d28ab71f39
- machine: windows-amd64
- commit hash: 7168e98
- commit date: 2025-09-13
- overall geometric mean: 1.546x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.48x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 214 ms: 1.31x faster                                                             |
| docutils       | 1.98 sec                                                        | 1.61 sec: 1.23x faster                                                           |
| Geometric mean | (ref)                                                           | 1.27x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization     | 364 ms                                                          | 198 ms: 1.83x faster                                                             |
| async_tree_io              | 693 ms                                                          | 380 ms: 1.83x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 375 ms: 1.81x faster                                                             |
| async_tree_none            | 298 ms                                                          | 168 ms: 1.77x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 327 ms: 1.72x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 163 ms: 1.70x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 209 ms: 1.68x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 332 ms: 1.64x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.75x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 53.1 ms: 2.39x faster                                                            |
| float          | 76.7 ms                                                         | 43.5 ms: 1.76x faster                                                            |
| pidigits       | 199 ms                                                          | 149 ms: 1.34x faster                                                             |
| Geometric mean | (ref)                                                           | 1.78x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 76.9 ms: 1.68x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.55 ms: 1.32x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 13.3 ms: 1.13x faster                                                            |
| regex_dna      | 127 ms                                                          | 115 ms: 1.10x faster                                                             |
| Geometric mean | (ref)                                                           | 1.29x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 103 us: 2.04x faster                                                             |
| tomli_loads          | 2.20 sec                                                        | 1.08 sec: 2.04x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 34.6 ms: 1.54x faster                                                            |
| json_loads           | 20.4 us                                                         | 13.7 us: 1.48x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 196 us: 1.46x faster                                                             |
| xml_etree_generate   | 72.1 ms                                                         | 50.8 ms: 1.42x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 5.35 ms: 1.38x faster                                                            |
| xml_etree_parse      | 113 ms                                                          | 84.5 ms: 1.34x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 61.5 ms: 1.26x faster                                                            |
| unpickle             | 9.71 us                                                         | 8.65 us: 1.12x faster                                                            |
| unpickle_list        | 2.95 us                                                         | 2.69 us: 1.09x faster                                                            |
| pickle_list          | 3.37 us                                                         | 3.26 us: 1.03x faster                                                            |
| Geometric mean       | (ref)                                                           | 1.34x faster                                                                     |

Benchmark hidden because not significant (2): pickle, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 18.8 ms: 1.01x faster                                                            |
| python_startup         | 22.4 ms                                                         | 24.8 ms: 1.11x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.05x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.27 ms: 1.89x faster                                                            |
| django_template | 36.9 ms                                                         | 24.7 ms: 1.50x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.68x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 1.37 sec: 12.89x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 28.6 ms: 3.19x faster                                                            |
| mdp                        | 1.91 sec                                                        | 789 ms: 2.42x faster                                                             |
| nbody                      | 127 ms                                                          | 53.1 ms: 2.39x faster                                                            |
| deepcopy_memo              | 38.4 us                                                         | 16.4 us: 2.33x faster                                                            |
| deepcopy                   | 360 us                                                          | 163 us: 2.21x faster                                                             |
| unpickle_pure_python       | 210 us                                                          | 103 us: 2.04x faster                                                             |
| tomli_loads                | 2.20 sec                                                        | 1.08 sec: 2.04x faster                                                           |
| generators                 | 38.5 ms                                                         | 19.1 ms: 2.02x faster                                                            |
| unpack_sequence            | 62.5 ns                                                         | 32.8 ns: 1.90x faster                                                            |
| logging_silent             | 101 ns                                                          | 53.4 ns: 1.89x faster                                                            |
| mako                       | 9.96 ms                                                         | 5.27 ms: 1.89x faster                                                            |
| richards                   | 41.3 ms                                                         | 22.2 ms: 1.87x faster                                                            |
| scimark_fft                | 271 ms                                                          | 146 ms: 1.85x faster                                                             |
| go                         | 137 ms                                                          | 74.7 ms: 1.84x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 198 ms: 1.83x faster                                                             |
| deepcopy_reduce            | 3.23 us                                                         | 1.76 us: 1.83x faster                                                            |
| async_tree_io              | 693 ms                                                          | 380 ms: 1.83x faster                                                             |
| comprehensions             | 19.2 us                                                         | 10.6 us: 1.82x faster                                                            |
| raytrace                   | 308 ms                                                          | 170 ms: 1.82x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 375 ms: 1.81x faster                                                             |
| pprint_pformat             | 1.50 sec                                                        | 841 ms: 1.78x faster                                                             |
| richards_super             | 46.5 ms                                                         | 26.2 ms: 1.78x faster                                                            |
| async_tree_none            | 298 ms                                                          | 168 ms: 1.77x faster                                                             |
| float                      | 76.7 ms                                                         | 43.5 ms: 1.76x faster                                                            |
| pprint_safe_repr           | 721 ms                                                          | 412 ms: 1.75x faster                                                             |
| chaos                      | 69.4 ms                                                         | 39.7 ms: 1.75x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 38.5 ms: 1.73x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 327 ms: 1.72x faster                                                             |
| scimark_sor                | 130 ms                                                          | 75.8 ms: 1.71x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 163 ms: 1.70x faster                                                             |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.28 ms: 1.69x faster                                                            |
| fannkuch                   | 354 ms                                                          | 209 ms: 1.69x faster                                                             |
| regex_compile              | 129 ms                                                          | 76.9 ms: 1.68x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 209 ms: 1.68x faster                                                             |
| pyflate                    | 424 ms                                                          | 253 ms: 1.68x faster                                                             |
| hexiom                     | 6.82 ms                                                         | 4.07 ms: 1.68x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 2.15 ms: 1.66x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 332 ms: 1.64x faster                                                             |
| logging_simple             | 9.75 us                                                         | 6.01 us: 1.62x faster                                                            |
| logging_format             | 10.4 us                                                         | 6.43 us: 1.62x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 59.1 ms: 1.58x faster                                                            |
| spectral_norm              | 104 ms                                                          | 66.0 ms: 1.57x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 44.7 ms: 1.55x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 60.6 ms: 1.55x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 34.6 ms: 1.54x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 38.8 ms: 1.51x faster                                                            |
| django_template            | 36.9 ms                                                         | 24.7 ms: 1.50x faster                                                            |
| json_loads                 | 20.4 us                                                         | 13.7 us: 1.48x faster                                                            |
| telco                      | 5.51 ms                                                         | 3.74 ms: 1.48x faster                                                            |
| pickle_pure_python         | 286 us                                                          | 196 us: 1.46x faster                                                             |
| sympy_str                  | 240 ms                                                          | 166 ms: 1.44x faster                                                             |
| sympy_sum                  | 123 ms                                                          | 85.2 ms: 1.44x faster                                                            |
| json                       | 4.15 ms                                                         | 2.90 ms: 1.43x faster                                                            |
| pycparser                  | 978 ms                                                          | 687 ms: 1.42x faster                                                             |
| xml_etree_generate         | 72.1 ms                                                         | 50.8 ms: 1.42x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 12.4 ms: 1.41x faster                                                            |
| json_dumps                 | 7.40 ms                                                         | 5.35 ms: 1.38x faster                                                            |
| sympy_expand               | 398 ms                                                          | 289 ms: 1.38x faster                                                             |
| coroutines                 | 20.9 ms                                                         | 15.3 ms: 1.37x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.51 us: 1.37x faster                                                            |
| asyncio_tcp                | 662 ms                                                          | 484 ms: 1.37x faster                                                             |
| pidigits                   | 199 ms                                                          | 149 ms: 1.34x faster                                                             |
| xml_etree_parse            | 113 ms                                                          | 84.5 ms: 1.34x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.55 ms: 1.32x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 843 us: 1.31x faster                                                             |
| 2to3                       | 280 ms                                                          | 214 ms: 1.31x faster                                                             |
| async_generators           | 313 ms                                                          | 242 ms: 1.29x faster                                                             |
| xml_etree_iterparse        | 77.6 ms                                                         | 61.5 ms: 1.26x faster                                                            |
| docutils                   | 1.98 sec                                                        | 1.61 sec: 1.23x faster                                                           |
| typing_runtime_protocols   | 126 us                                                          | 103 us: 1.23x faster                                                             |
| meteor_contest             | 86.9 ms                                                         | 71.8 ms: 1.21x faster                                                            |
| regex_v8                   | 15.0 ms                                                         | 13.3 ms: 1.13x faster                                                            |
| unpickle                   | 9.71 us                                                         | 8.65 us: 1.12x faster                                                            |
| regex_dna                  | 127 ms                                                          | 115 ms: 1.10x faster                                                             |
| unpickle_list              | 2.95 us                                                         | 2.69 us: 1.09x faster                                                            |
| pickle_list                | 3.37 us                                                         | 3.26 us: 1.03x faster                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 18.8 ms: 1.01x faster                                                            |
| coverage                   | 48.4 ms                                                         | 49.5 ms: 1.02x slower                                                            |
| python_startup             | 22.4 ms                                                         | 24.8 ms: 1.11x slower                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 87.9 ms: 1.17x slower                                                            |
| gc_traversal               | 1.44 ms                                                         | 2.09 ms: 1.45x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.27 ms: 1.95x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.54x faster                                                                     |

Benchmark hidden because not significant (2): pickle, pickle_dict
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250913-3.15.0a0-7168e98-JIT/bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.546x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.55x
- 95% likely to have a speedup of 1.53x
- 99% likely to have a speedup of 1.48x

# Memory
- memory change: unknown