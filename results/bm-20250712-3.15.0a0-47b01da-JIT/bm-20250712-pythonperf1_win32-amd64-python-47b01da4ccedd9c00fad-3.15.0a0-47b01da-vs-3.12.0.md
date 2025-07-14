# Results vs. 3.12.0

- fork: python
- ref: 47b01da4ccedd9c00fad
- machine: windows-amd64
- commit hash: 47b01da
- commit date: 2025-07-12
- overall geometric mean: 1.504x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.46x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 219 ms: 1.28x faster                                                             |
| docutils       | 1.98 sec                                                        | 1.66 sec: 1.19x faster                                                           |
| Geometric mean | (ref)                                                           | 1.23x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization     | 364 ms                                                          | 200 ms: 1.81x faster                                                             |
| async_tree_none            | 298 ms                                                          | 165 ms: 1.80x faster                                                             |
| async_tree_io              | 693 ms                                                          | 388 ms: 1.78x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 390 ms: 1.74x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 330 ms: 1.71x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 208 ms: 1.69x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 167 ms: 1.66x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 337 ms: 1.62x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.72x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 54.6 ms: 2.33x faster                                                            |
| float          | 76.7 ms                                                         | 43.4 ms: 1.77x faster                                                            |
| pidigits       | 199 ms                                                          | 146 ms: 1.37x faster                                                             |
| Geometric mean | (ref)                                                           | 1.78x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 79.2 ms: 1.63x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.63 ms: 1.25x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 14.0 ms: 1.07x faster                                                            |
| regex_dna      | 127 ms                                                          | 120 ms: 1.05x faster                                                             |
| Geometric mean | (ref)                                                           | 1.23x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 107 us: 1.96x faster                                                             |
| tomli_loads          | 2.20 sec                                                        | 1.13 sec: 1.95x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 35.3 ms: 1.51x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 50.5 ms: 1.43x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 201 us: 1.42x faster                                                             |
| json_loads           | 20.4 us                                                         | 14.3 us: 1.42x faster                                                            |
| xml_etree_parse      | 113 ms                                                          | 86.5 ms: 1.31x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 61.3 ms: 1.27x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 6.23 ms: 1.19x faster                                                            |
| unpickle             | 9.71 us                                                         | 8.54 us: 1.14x faster                                                            |
| unpickle_list        | 2.95 us                                                         | 2.76 us: 1.07x faster                                                            |
| pickle               | 7.79 us                                                         | 7.86 us: 1.01x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.30x faster                                                                     |

Benchmark hidden because not significant (2): pickle_dict, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.3 ms: 1.01x slower                                                            |
| python_startup         | 22.4 ms                                                         | 25.4 ms: 1.14x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.07x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.38 ms: 1.85x faster                                                            |
| django_template | 36.9 ms                                                         | 24.6 ms: 1.50x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.67x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 1.42 sec: 12.43x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 30.0 ms: 3.05x faster                                                            |
| mdp                        | 1.91 sec                                                        | 800 ms: 2.39x faster                                                             |
| nbody                      | 127 ms                                                          | 54.6 ms: 2.33x faster                                                            |
| deepcopy_memo              | 38.4 us                                                         | 18.1 us: 2.13x faster                                                            |
| deepcopy                   | 360 us                                                          | 171 us: 2.10x faster                                                             |
| unpickle_pure_python       | 210 us                                                          | 107 us: 1.96x faster                                                             |
| tomli_loads                | 2.20 sec                                                        | 1.13 sec: 1.95x faster                                                           |
| generators                 | 38.5 ms                                                         | 20.2 ms: 1.91x faster                                                            |
| unpack_sequence            | 62.5 ns                                                         | 33.3 ns: 1.88x faster                                                            |
| mako                       | 9.96 ms                                                         | 5.38 ms: 1.85x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 200 ms: 1.81x faster                                                             |
| scimark_fft                | 271 ms                                                          | 149 ms: 1.81x faster                                                             |
| comprehensions             | 19.2 us                                                         | 10.6 us: 1.81x faster                                                            |
| logging_silent             | 101 ns                                                          | 56.1 ns: 1.80x faster                                                            |
| async_tree_none            | 298 ms                                                          | 165 ms: 1.80x faster                                                             |
| go                         | 137 ms                                                          | 76.4 ms: 1.80x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 1.80 us: 1.79x faster                                                            |
| async_tree_io              | 693 ms                                                          | 388 ms: 1.78x faster                                                             |
| float                      | 76.7 ms                                                         | 43.4 ms: 1.77x faster                                                            |
| scimark_sor                | 130 ms                                                          | 74.5 ms: 1.74x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 390 ms: 1.74x faster                                                             |
| chaos                      | 69.4 ms                                                         | 40.0 ms: 1.74x faster                                                            |
| raytrace                   | 308 ms                                                          | 178 ms: 1.73x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 330 ms: 1.71x faster                                                             |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.28 ms: 1.69x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 208 ms: 1.69x faster                                                             |
| pyflate                    | 424 ms                                                          | 253 ms: 1.68x faster                                                             |
| deltablue                  | 3.58 ms                                                         | 2.14 ms: 1.68x faster                                                            |
| spectral_norm              | 104 ms                                                          | 62.0 ms: 1.68x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 39.9 ms: 1.66x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 167 ms: 1.66x faster                                                             |
| hexiom                     | 6.82 ms                                                         | 4.11 ms: 1.66x faster                                                            |
| fannkuch                   | 354 ms                                                          | 213 ms: 1.66x faster                                                             |
| pprint_pformat             | 1.50 sec                                                        | 912 ms: 1.64x faster                                                             |
| regex_compile              | 129 ms                                                          | 79.2 ms: 1.63x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 57.7 ms: 1.62x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 337 ms: 1.62x faster                                                             |
| pprint_safe_repr           | 721 ms                                                          | 447 ms: 1.61x faster                                                             |
| logging_simple             | 9.75 us                                                         | 6.09 us: 1.60x faster                                                            |
| logging_format             | 10.4 us                                                         | 6.54 us: 1.59x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 58.8 ms: 1.59x faster                                                            |
| richards                   | 41.3 ms                                                         | 26.9 ms: 1.54x faster                                                            |
| richards_super             | 46.5 ms                                                         | 30.3 ms: 1.53x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 45.4 ms: 1.53x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 35.3 ms: 1.51x faster                                                            |
| django_template            | 36.9 ms                                                         | 24.6 ms: 1.50x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 14.2 ms: 1.47x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 40.2 ms: 1.45x faster                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 50.5 ms: 1.43x faster                                                            |
| pickle_pure_python         | 286 us                                                          | 201 us: 1.42x faster                                                             |
| json_loads                 | 20.4 us                                                         | 14.3 us: 1.42x faster                                                            |
| pycparser                  | 978 ms                                                          | 696 ms: 1.41x faster                                                             |
| sympy_sum                  | 123 ms                                                          | 87.4 ms: 1.41x faster                                                            |
| sympy_str                  | 240 ms                                                          | 173 ms: 1.38x faster                                                             |
| sympy_integrate            | 17.5 ms                                                         | 12.7 ms: 1.38x faster                                                            |
| json                       | 4.15 ms                                                         | 3.02 ms: 1.38x faster                                                            |
| pidigits                   | 199 ms                                                          | 146 ms: 1.37x faster                                                             |
| sympy_expand               | 398 ms                                                          | 295 ms: 1.35x faster                                                             |
| sqlite_synth               | 2.07 us                                                         | 1.55 us: 1.33x faster                                                            |
| asyncio_tcp                | 662 ms                                                          | 500 ms: 1.32x faster                                                             |
| xml_etree_parse            | 113 ms                                                          | 86.5 ms: 1.31x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 845 us: 1.30x faster                                                             |
| 2to3                       | 280 ms                                                          | 219 ms: 1.28x faster                                                             |
| telco                      | 5.51 ms                                                         | 4.33 ms: 1.27x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 61.3 ms: 1.27x faster                                                            |
| async_generators           | 313 ms                                                          | 248 ms: 1.27x faster                                                             |
| regex_effbot               | 2.04 ms                                                         | 1.63 ms: 1.25x faster                                                            |
| typing_runtime_protocols   | 126 us                                                          | 102 us: 1.24x faster                                                             |
| meteor_contest             | 86.9 ms                                                         | 70.5 ms: 1.23x faster                                                            |
| docutils                   | 1.98 sec                                                        | 1.66 sec: 1.19x faster                                                           |
| json_dumps                 | 7.40 ms                                                         | 6.23 ms: 1.19x faster                                                            |
| unpickle                   | 9.71 us                                                         | 8.54 us: 1.14x faster                                                            |
| regex_v8                   | 15.0 ms                                                         | 14.0 ms: 1.07x faster                                                            |
| unpickle_list              | 2.95 us                                                         | 2.76 us: 1.07x faster                                                            |
| regex_dna                  | 127 ms                                                          | 120 ms: 1.05x faster                                                             |
| pickle                     | 7.79 us                                                         | 7.86 us: 1.01x slower                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 19.3 ms: 1.01x slower                                                            |
| coverage                   | 48.4 ms                                                         | 49.7 ms: 1.03x slower                                                            |
| python_startup             | 22.4 ms                                                         | 25.4 ms: 1.14x slower                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 94.7 ms: 1.26x slower                                                            |
| gc_traversal               | 1.44 ms                                                         | 2.13 ms: 1.48x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.32 ms: 2.02x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.50x faster                                                                     |

Benchmark hidden because not significant (2): pickle_dict, pickle_list
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250712-3.15.0a0-47b01da-JIT/bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.504x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.52x
- 95% likely to have a speedup of 1.50x
- 99% likely to have a speedup of 1.46x

# Memory
- memory change: unknown