# Results vs. 3.12.0

- fork: python
- ref: 75f40595e555e7d016cf
- machine: windows-amd64
- commit hash: 75f4059
- commit date: 2025-06-30
- overall geometric mean: 1.305x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 229 ms: 1.22x faster                                                             |
| docutils       | 1.98 sec                                                        | 2.94 sec: 1.48x slower                                                           |
| Geometric mean | (ref)                                                           | 1.10x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 334 ms: 2.03x faster                                                             |
| async_tree_io              | 693 ms                                                          | 354 ms: 1.96x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 153 ms: 1.81x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 197 ms: 1.78x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 316 ms: 1.73x faster                                                             |
| async_tree_none            | 298 ms                                                          | 175 ms: 1.71x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 215 ms: 1.69x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 337 ms: 1.67x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.79x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 46.2 ms: 1.66x faster                                                            |
| nbody          | 127 ms                                                          | 85.9 ms: 1.48x faster                                                            |
| pidigits       | 199 ms                                                          | 137 ms: 1.46x faster                                                             |
| Geometric mean | (ref)                                                           | 1.53x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 95.9 ms: 1.35x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.62 ms: 1.26x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 13.5 ms: 1.12x faster                                                            |
| regex_dna      | 127 ms                                                          | 114 ms: 1.11x faster                                                             |
| Geometric mean | (ref)                                                           | 1.21x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 156 us: 1.34x faster                                                             |
| xml_etree_iterparse  | 77.6 ms                                                         | 58.8 ms: 1.32x faster                                                            |
| json_loads           | 20.4 us                                                         | 16.1 us: 1.26x faster                                                            |
| xml_etree_parse      | 113 ms                                                          | 90.4 ms: 1.25x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 237 us: 1.20x faster                                                             |
| xml_etree_process    | 53.2 ms                                                         | 45.9 ms: 1.16x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 63.3 ms: 1.14x faster                                                            |
| pickle_list          | 3.37 us                                                         | 3.03 us: 1.11x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 6.67 ms: 1.11x faster                                                            |
| pickle_dict          | 19.9 us                                                         | 20.2 us: 1.01x slower                                                            |
| unpickle_list        | 2.95 us                                                         | 3.06 us: 1.04x slower                                                            |
| pickle               | 7.79 us                                                         | 8.22 us: 1.05x slower                                                            |
| unpickle             | 9.71 us                                                         | 10.5 us: 1.08x slower                                                            |
| tomli_loads          | 2.20 sec                                                        | 2.72 sec: 1.24x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.10x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.4 ms: 1.02x slower                                                            |
| python_startup         | 22.4 ms                                                         | 25.6 ms: 1.15x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.9 ms                                                         | 28.2 ms: 1.31x faster                                                            |
| mako            | 9.96 ms                                                         | 9.89 ms: 1.01x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.15x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 2.45 sec: 7.20x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 32.3 ms: 2.83x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 334 ms: 2.03x faster                                                             |
| async_tree_io              | 693 ms                                                          | 354 ms: 1.96x faster                                                             |
| deepcopy_memo              | 38.4 us                                                         | 21.1 us: 1.82x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 153 ms: 1.81x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 197 ms: 1.78x faster                                                             |
| deepcopy                   | 360 us                                                          | 204 us: 1.76x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 316 ms: 1.73x faster                                                             |
| async_tree_none            | 298 ms                                                          | 175 ms: 1.71x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 215 ms: 1.69x faster                                                             |
| unpack_sequence            | 62.5 ns                                                         | 37.1 ns: 1.68x faster                                                            |
| generators                 | 38.5 ms                                                         | 23.0 ms: 1.67x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 337 ms: 1.67x faster                                                             |
| float                      | 76.7 ms                                                         | 46.2 ms: 1.66x faster                                                            |
| logging_silent             | 101 ns                                                          | 62.1 ns: 1.63x faster                                                            |
| mdp                        | 1.91 sec                                                        | 1.18 sec: 1.62x faster                                                           |
| comprehensions             | 19.2 us                                                         | 12.1 us: 1.59x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.34 us: 1.54x faster                                                            |
| scimark_sor                | 130 ms                                                          | 87.4 ms: 1.48x faster                                                            |
| go                         | 137 ms                                                          | 92.7 ms: 1.48x faster                                                            |
| nbody                      | 127 ms                                                          | 85.9 ms: 1.48x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 2.19 us: 1.47x faster                                                            |
| hexiom                     | 6.82 ms                                                         | 4.64 ms: 1.47x faster                                                            |
| chaos                      | 69.4 ms                                                         | 47.5 ms: 1.46x faster                                                            |
| pidigits                   | 199 ms                                                          | 137 ms: 1.46x faster                                                             |
| deltablue                  | 3.58 ms                                                         | 2.46 ms: 1.46x faster                                                            |
| logging_simple             | 9.75 us                                                         | 6.77 us: 1.44x faster                                                            |
| logging_format             | 10.4 us                                                         | 7.31 us: 1.42x faster                                                            |
| raytrace                   | 308 ms                                                          | 216 ms: 1.42x faster                                                             |
| coroutines                 | 20.9 ms                                                         | 14.8 ms: 1.41x faster                                                            |
| spectral_norm              | 104 ms                                                          | 74.4 ms: 1.40x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 67.4 ms: 1.38x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 43.1 ms: 1.36x faster                                                            |
| regex_compile              | 129 ms                                                          | 95.9 ms: 1.35x faster                                                            |
| json                       | 4.15 ms                                                         | 3.09 ms: 1.34x faster                                                            |
| unpickle_pure_python       | 210 us                                                          | 156 us: 1.34x faster                                                             |
| pyflate                    | 424 ms                                                          | 318 ms: 1.33x faster                                                             |
| pycparser                  | 978 ms                                                          | 739 ms: 1.32x faster                                                             |
| xml_etree_iterparse        | 77.6 ms                                                         | 58.8 ms: 1.32x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 50.5 ms: 1.32x faster                                                            |
| django_template            | 36.9 ms                                                         | 28.2 ms: 1.31x faster                                                            |
| scimark_fft                | 271 ms                                                          | 212 ms: 1.28x faster                                                             |
| nqueens                    | 93.7 ms                                                         | 73.9 ms: 1.27x faster                                                            |
| json_loads                 | 20.4 us                                                         | 16.1 us: 1.26x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.62 ms: 1.26x faster                                                            |
| pprint_safe_repr           | 721 ms                                                          | 573 ms: 1.26x faster                                                             |
| sympy_str                  | 240 ms                                                          | 191 ms: 1.25x faster                                                             |
| xml_etree_parse            | 113 ms                                                          | 90.4 ms: 1.25x faster                                                            |
| sympy_sum                  | 123 ms                                                          | 98.7 ms: 1.25x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.14 ms: 1.23x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 14.3 ms: 1.23x faster                                                            |
| 2to3                       | 280 ms                                                          | 229 ms: 1.22x faster                                                             |
| sympy_expand               | 398 ms                                                          | 328 ms: 1.21x faster                                                             |
| richards                   | 41.3 ms                                                         | 34.1 ms: 1.21x faster                                                            |
| pickle_pure_python         | 286 us                                                          | 237 us: 1.20x faster                                                             |
| crypto_pyaes               | 69.2 ms                                                         | 57.5 ms: 1.20x faster                                                            |
| async_generators           | 313 ms                                                          | 261 ms: 1.20x faster                                                             |
| asyncio_tcp                | 662 ms                                                          | 556 ms: 1.19x faster                                                             |
| richards_super             | 46.5 ms                                                         | 39.6 ms: 1.17x faster                                                            |
| gc_traversal               | 1.44 ms                                                         | 1.23 ms: 1.17x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 45.9 ms: 1.16x faster                                                            |
| fannkuch                   | 354 ms                                                          | 310 ms: 1.14x faster                                                             |
| xml_etree_generate         | 72.1 ms                                                         | 63.3 ms: 1.14x faster                                                            |
| regex_v8                   | 15.0 ms                                                         | 13.5 ms: 1.12x faster                                                            |
| regex_dna                  | 127 ms                                                          | 114 ms: 1.11x faster                                                             |
| pickle_list                | 3.37 us                                                         | 3.03 us: 1.11x faster                                                            |
| json_dumps                 | 7.40 ms                                                         | 6.67 ms: 1.11x faster                                                            |
| meteor_contest             | 86.9 ms                                                         | 86.0 ms: 1.01x faster                                                            |
| telco                      | 5.51 ms                                                         | 5.47 ms: 1.01x faster                                                            |
| mako                       | 9.96 ms                                                         | 9.89 ms: 1.01x faster                                                            |
| pickle_dict                | 19.9 us                                                         | 20.2 us: 1.01x slower                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 19.4 ms: 1.02x slower                                                            |
| typing_runtime_protocols   | 126 us                                                          | 130 us: 1.03x slower                                                             |
| unpickle_list              | 2.95 us                                                         | 3.06 us: 1.04x slower                                                            |
| pickle                     | 7.79 us                                                         | 8.22 us: 1.05x slower                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 79.8 ms: 1.06x slower                                                            |
| unpickle                   | 9.71 us                                                         | 10.5 us: 1.08x slower                                                            |
| python_startup             | 22.4 ms                                                         | 25.6 ms: 1.15x slower                                                            |
| pprint_pformat             | 1.50 sec                                                        | 1.74 sec: 1.16x slower                                                           |
| tomli_loads                | 2.20 sec                                                        | 2.72 sec: 1.24x slower                                                           |
| coverage                   | 48.4 ms                                                         | 66.9 ms: 1.38x slower                                                            |
| docutils                   | 1.98 sec                                                        | 2.94 sec: 1.48x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.06 ms: 1.63x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.31x faster                                                                     |

Benchmark hidden because not significant (1): bench_thread_pool
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250630-3.15.0a0-75f4059-NOGIL/bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.305x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: unknown