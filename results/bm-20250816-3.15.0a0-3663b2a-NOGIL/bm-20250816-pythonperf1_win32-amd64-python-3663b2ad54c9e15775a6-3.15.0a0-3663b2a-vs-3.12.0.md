# Results vs. 3.12.0

- fork: python
- ref: 3663b2ad54c9e15775a6
- machine: windows-amd64
- commit hash: 3663b2a
- commit date: 2025-08-16
- overall geometric mean: 1.338x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 223 ms: 1.25x faster                                                             |
| docutils       | 1.98 sec                                                        | 2.75 sec: 1.39x slower                                                           |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 325 ms: 2.09x faster                                                             |
| async_tree_io              | 693 ms                                                          | 347 ms: 2.00x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 147 ms: 1.89x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 190 ms: 1.84x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 307 ms: 1.78x faster                                                             |
| async_tree_none            | 298 ms                                                          | 169 ms: 1.77x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 209 ms: 1.74x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 329 ms: 1.71x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.85x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 46.1 ms: 1.66x faster                                                            |
| nbody          | 127 ms                                                          | 82.1 ms: 1.55x faster                                                            |
| pidigits       | 199 ms                                                          | 135 ms: 1.48x faster                                                             |
| Geometric mean | (ref)                                                           | 1.56x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 93.0 ms: 1.39x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.56 ms: 1.31x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 13.2 ms: 1.14x faster                                                            |
| regex_dna      | 127 ms                                                          | 115 ms: 1.11x faster                                                             |
| Geometric mean | (ref)                                                           | 1.23x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 157 us: 1.34x faster                                                             |
| xml_etree_iterparse  | 77.6 ms                                                         | 60.3 ms: 1.29x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 5.81 ms: 1.27x faster                                                            |
| json_loads           | 20.4 us                                                         | 16.1 us: 1.27x faster                                                            |
| xml_etree_parse      | 113 ms                                                          | 89.7 ms: 1.26x faster                                                            |
| xml_etree_process    | 53.2 ms                                                         | 44.4 ms: 1.20x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 240 us: 1.19x faster                                                             |
| xml_etree_generate   | 72.1 ms                                                         | 62.4 ms: 1.16x faster                                                            |
| pickle_list          | 3.37 us                                                         | 3.10 us: 1.09x faster                                                            |
| pickle               | 7.79 us                                                         | 7.70 us: 1.01x faster                                                            |
| unpickle             | 9.71 us                                                         | 9.78 us: 1.01x slower                                                            |
| unpickle_list        | 2.95 us                                                         | 2.98 us: 1.01x slower                                                            |
| tomli_loads          | 2.20 sec                                                        | 2.53 sec: 1.15x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.13x faster                                                                     |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.4 ms: 1.02x slower                                                            |
| python_startup         | 22.4 ms                                                         | 25.6 ms: 1.15x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.9 ms                                                         | 26.7 ms: 1.38x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.18x faster                                                                     |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 1.91 sec: 9.22x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 28.6 ms: 3.20x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 325 ms: 2.09x faster                                                             |
| async_tree_io              | 693 ms                                                          | 347 ms: 2.00x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 147 ms: 1.89x faster                                                             |
| mdp                        | 1.91 sec                                                        | 1.03 sec: 1.86x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 190 ms: 1.84x faster                                                             |
| deepcopy_memo              | 38.4 us                                                         | 21.0 us: 1.83x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 307 ms: 1.78x faster                                                             |
| async_tree_none            | 298 ms                                                          | 169 ms: 1.77x faster                                                             |
| deepcopy                   | 360 us                                                          | 206 us: 1.75x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 209 ms: 1.74x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 329 ms: 1.71x faster                                                             |
| unpack_sequence            | 62.5 ns                                                         | 37.3 ns: 1.67x faster                                                            |
| float                      | 76.7 ms                                                         | 46.1 ms: 1.66x faster                                                            |
| logging_silent             | 101 ns                                                          | 61.3 ns: 1.65x faster                                                            |
| generators                 | 38.5 ms                                                         | 23.4 ms: 1.65x faster                                                            |
| comprehensions             | 19.2 us                                                         | 12.0 us: 1.60x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.34 us: 1.55x faster                                                            |
| nbody                      | 127 ms                                                          | 82.1 ms: 1.55x faster                                                            |
| asyncio_tcp                | 662 ms                                                          | 429 ms: 1.54x faster                                                             |
| chaos                      | 69.4 ms                                                         | 45.5 ms: 1.52x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 2.13 us: 1.51x faster                                                            |
| go                         | 137 ms                                                          | 91.2 ms: 1.51x faster                                                            |
| hexiom                     | 6.82 ms                                                         | 4.56 ms: 1.50x faster                                                            |
| raytrace                   | 308 ms                                                          | 206 ms: 1.49x faster                                                             |
| pidigits                   | 199 ms                                                          | 135 ms: 1.48x faster                                                             |
| deltablue                  | 3.58 ms                                                         | 2.45 ms: 1.47x faster                                                            |
| scimark_sor                | 130 ms                                                          | 88.7 ms: 1.46x faster                                                            |
| logging_simple             | 9.75 us                                                         | 6.68 us: 1.46x faster                                                            |
| logging_format             | 10.4 us                                                         | 7.16 us: 1.45x faster                                                            |
| spectral_norm              | 104 ms                                                          | 72.3 ms: 1.44x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 41.0 ms: 1.43x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 65.5 ms: 1.42x faster                                                            |
| regex_compile              | 129 ms                                                          | 93.0 ms: 1.39x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 15.1 ms: 1.38x faster                                                            |
| django_template            | 36.9 ms                                                         | 26.7 ms: 1.38x faster                                                            |
| pyflate                    | 424 ms                                                          | 311 ms: 1.36x faster                                                             |
| pycparser                  | 978 ms                                                          | 720 ms: 1.36x faster                                                             |
| unpickle_pure_python       | 210 us                                                          | 157 us: 1.34x faster                                                             |
| json                       | 4.15 ms                                                         | 3.12 ms: 1.33x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 50.6 ms: 1.31x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.56 ms: 1.31x faster                                                            |
| sympy_str                  | 240 ms                                                          | 185 ms: 1.29x faster                                                             |
| xml_etree_iterparse        | 77.6 ms                                                         | 60.3 ms: 1.29x faster                                                            |
| sympy_sum                  | 123 ms                                                          | 95.9 ms: 1.28x faster                                                            |
| pprint_safe_repr           | 721 ms                                                          | 565 ms: 1.27x faster                                                             |
| json_dumps                 | 7.40 ms                                                         | 5.81 ms: 1.27x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.04 ms: 1.27x faster                                                            |
| json_loads                 | 20.4 us                                                         | 16.1 us: 1.27x faster                                                            |
| scimark_fft                | 271 ms                                                          | 214 ms: 1.27x faster                                                             |
| sympy_integrate            | 17.5 ms                                                         | 13.9 ms: 1.26x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 89.7 ms: 1.26x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 74.3 ms: 1.26x faster                                                            |
| sympy_expand               | 398 ms                                                          | 316 ms: 1.26x faster                                                             |
| 2to3                       | 280 ms                                                          | 223 ms: 1.25x faster                                                             |
| async_generators           | 313 ms                                                          | 255 ms: 1.23x faster                                                             |
| crypto_pyaes               | 69.2 ms                                                         | 56.8 ms: 1.22x faster                                                            |
| richards                   | 41.3 ms                                                         | 34.3 ms: 1.20x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 44.4 ms: 1.20x faster                                                            |
| pickle_pure_python         | 286 us                                                          | 240 us: 1.19x faster                                                             |
| gc_traversal               | 1.44 ms                                                         | 1.22 ms: 1.19x faster                                                            |
| richards_super             | 46.5 ms                                                         | 40.0 ms: 1.16x faster                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 62.4 ms: 1.16x faster                                                            |
| fannkuch                   | 354 ms                                                          | 306 ms: 1.16x faster                                                             |
| regex_v8                   | 15.0 ms                                                         | 13.2 ms: 1.14x faster                                                            |
| telco                      | 5.51 ms                                                         | 4.88 ms: 1.13x faster                                                            |
| regex_dna                  | 127 ms                                                          | 115 ms: 1.11x faster                                                             |
| pickle_list                | 3.37 us                                                         | 3.10 us: 1.09x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 1.08 ms: 1.02x faster                                                            |
| meteor_contest             | 86.9 ms                                                         | 85.8 ms: 1.01x faster                                                            |
| pickle                     | 7.79 us                                                         | 7.70 us: 1.01x faster                                                            |
| unpickle                   | 9.71 us                                                         | 9.78 us: 1.01x slower                                                            |
| unpickle_list              | 2.95 us                                                         | 2.98 us: 1.01x slower                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 19.4 ms: 1.02x slower                                                            |
| typing_runtime_protocols   | 126 us                                                          | 129 us: 1.02x slower                                                             |
| bench_mp_pool              | 75.4 ms                                                         | 77.7 ms: 1.03x slower                                                            |
| python_startup             | 22.4 ms                                                         | 25.6 ms: 1.15x slower                                                            |
| tomli_loads                | 2.20 sec                                                        | 2.53 sec: 1.15x slower                                                           |
| coverage                   | 48.4 ms                                                         | 66.3 ms: 1.37x slower                                                            |
| docutils                   | 1.98 sec                                                        | 2.75 sec: 1.39x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.04 ms: 1.59x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.35x faster                                                                     |

Benchmark hidden because not significant (3): pprint_pformat, mako, pickle_dict
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250816-3.15.0a0-3663b2a-NOGIL/bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.338x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: unknown