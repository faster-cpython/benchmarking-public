# Results vs. 3.12.0

- fork: python
- ref: 3663b2ad54c9e15775a6
- machine: windows-amd64
- commit hash: 3663b2a
- commit date: 2025-08-16
- overall geometric mean: 1.480x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.44x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 218 ms: 1.28x faster                                                             |
| docutils       | 1.98 sec                                                        | 1.59 sec: 1.25x faster                                                           |
| Geometric mean | (ref)                                                           | 1.27x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io              | 693 ms                                                          | 383 ms: 1.81x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 204 ms: 1.79x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 386 ms: 1.75x faster                                                             |
| async_tree_none            | 298 ms                                                          | 172 ms: 1.73x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 328 ms: 1.72x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 208 ms: 1.68x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 166 ms: 1.67x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 338 ms: 1.62x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.72x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 63.5 ms: 2.00x faster                                                            |
| float          | 76.7 ms                                                         | 42.6 ms: 1.80x faster                                                            |
| pidigits       | 199 ms                                                          | 144 ms: 1.38x faster                                                             |
| Geometric mean | (ref)                                                           | 1.71x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 79.0 ms: 1.63x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.52 ms: 1.34x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 13.9 ms: 1.09x faster                                                            |
| regex_dna      | 127 ms                                                          | 118 ms: 1.08x faster                                                             |
| Geometric mean | (ref)                                                           | 1.26x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 133 us: 1.58x faster                                                             |
| tomli_loads          | 2.20 sec                                                        | 1.42 sec: 1.55x faster                                                           |
| json_loads           | 20.4 us                                                         | 13.9 us: 1.47x faster                                                            |
| xml_etree_process    | 53.2 ms                                                         | 38.8 ms: 1.37x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 5.43 ms: 1.36x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 212 us: 1.35x faster                                                             |
| xml_etree_parse      | 113 ms                                                          | 87.6 ms: 1.29x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 56.6 ms: 1.28x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 64.3 ms: 1.21x faster                                                            |
| unpickle             | 9.71 us                                                         | 8.50 us: 1.14x faster                                                            |
| pickle_list          | 3.37 us                                                         | 3.27 us: 1.03x faster                                                            |
| unpickle_list        | 2.95 us                                                         | 2.88 us: 1.02x faster                                                            |
| pickle               | 7.79 us                                                         | 7.93 us: 1.02x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.24x faster                                                                     |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup | 22.4 ms                                                         | 25.3 ms: 1.13x slower                                                            |
| Geometric mean | (ref)                                                           | 1.07x slower                                                                     |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 6.58 ms: 1.51x faster                                                            |
| django_template | 36.9 ms                                                         | 24.5 ms: 1.51x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.51x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 1.23 sec: 14.30x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 28.5 ms: 3.21x faster                                                            |
| mdp                        | 1.91 sec                                                        | 794 ms: 2.41x faster                                                             |
| deepcopy                   | 360 us                                                          | 169 us: 2.13x faster                                                             |
| deepcopy_memo              | 38.4 us                                                         | 18.3 us: 2.10x faster                                                            |
| nbody                      | 127 ms                                                          | 63.5 ms: 2.00x faster                                                            |
| generators                 | 38.5 ms                                                         | 19.3 ms: 1.99x faster                                                            |
| unpack_sequence            | 62.5 ns                                                         | 32.1 ns: 1.94x faster                                                            |
| logging_silent             | 101 ns                                                          | 55.0 ns: 1.84x faster                                                            |
| async_tree_io              | 693 ms                                                          | 383 ms: 1.81x faster                                                             |
| float                      | 76.7 ms                                                         | 42.6 ms: 1.80x faster                                                            |
| asyncio_tcp                | 662 ms                                                          | 369 ms: 1.79x faster                                                             |
| go                         | 137 ms                                                          | 76.6 ms: 1.79x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 204 ms: 1.79x faster                                                             |
| raytrace                   | 308 ms                                                          | 174 ms: 1.77x faster                                                             |
| deepcopy_reduce            | 3.23 us                                                         | 1.83 us: 1.77x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 386 ms: 1.75x faster                                                             |
| async_tree_none            | 298 ms                                                          | 172 ms: 1.73x faster                                                             |
| comprehensions             | 19.2 us                                                         | 11.1 us: 1.72x faster                                                            |
| chaos                      | 69.4 ms                                                         | 40.3 ms: 1.72x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 328 ms: 1.72x faster                                                             |
| scimark_sor                | 130 ms                                                          | 76.0 ms: 1.71x faster                                                            |
| hexiom                     | 6.82 ms                                                         | 4.02 ms: 1.70x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 208 ms: 1.68x faster                                                             |
| logging_simple             | 9.75 us                                                         | 5.83 us: 1.67x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 166 ms: 1.67x faster                                                             |
| scimark_monte_carlo        | 66.4 ms                                                         | 39.8 ms: 1.67x faster                                                            |
| logging_format             | 10.4 us                                                         | 6.26 us: 1.66x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 2.18 ms: 1.65x faster                                                            |
| regex_compile              | 129 ms                                                          | 79.0 ms: 1.63x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 57.6 ms: 1.62x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 338 ms: 1.62x faster                                                             |
| spectral_norm              | 104 ms                                                          | 64.6 ms: 1.61x faster                                                            |
| unpickle_pure_python       | 210 us                                                          | 133 us: 1.58x faster                                                             |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.47 ms: 1.56x faster                                                            |
| tomli_loads                | 2.20 sec                                                        | 1.42 sec: 1.55x faster                                                           |
| richards                   | 41.3 ms                                                         | 26.7 ms: 1.55x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 60.6 ms: 1.55x faster                                                            |
| richards_super             | 46.5 ms                                                         | 30.5 ms: 1.52x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 38.5 ms: 1.52x faster                                                            |
| scimark_fft                | 271 ms                                                          | 179 ms: 1.52x faster                                                             |
| mako                       | 9.96 ms                                                         | 6.58 ms: 1.51x faster                                                            |
| django_template            | 36.9 ms                                                         | 24.5 ms: 1.51x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 46.0 ms: 1.51x faster                                                            |
| pprint_pformat             | 1.50 sec                                                        | 998 ms: 1.50x faster                                                             |
| pprint_safe_repr           | 721 ms                                                          | 489 ms: 1.47x faster                                                             |
| pyflate                    | 424 ms                                                          | 289 ms: 1.47x faster                                                             |
| json_loads                 | 20.4 us                                                         | 13.9 us: 1.47x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 12.2 ms: 1.44x faster                                                            |
| sympy_str                  | 240 ms                                                          | 167 ms: 1.44x faster                                                             |
| sympy_sum                  | 123 ms                                                          | 85.6 ms: 1.43x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 14.6 ms: 1.43x faster                                                            |
| json                       | 4.15 ms                                                         | 2.93 ms: 1.42x faster                                                            |
| sympy_expand               | 398 ms                                                          | 282 ms: 1.41x faster                                                             |
| pycparser                  | 978 ms                                                          | 694 ms: 1.41x faster                                                             |
| pidigits                   | 199 ms                                                          | 144 ms: 1.38x faster                                                             |
| async_generators           | 313 ms                                                          | 227 ms: 1.38x faster                                                             |
| xml_etree_process          | 53.2 ms                                                         | 38.8 ms: 1.37x faster                                                            |
| json_dumps                 | 7.40 ms                                                         | 5.43 ms: 1.36x faster                                                            |
| pickle_pure_python         | 286 us                                                          | 212 us: 1.35x faster                                                             |
| fannkuch                   | 354 ms                                                          | 262 ms: 1.35x faster                                                             |
| regex_effbot               | 2.04 ms                                                         | 1.52 ms: 1.34x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.57 us: 1.32x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 839 us: 1.31x faster                                                             |
| xml_etree_parse            | 113 ms                                                          | 87.6 ms: 1.29x faster                                                            |
| 2to3                       | 280 ms                                                          | 218 ms: 1.28x faster                                                             |
| xml_etree_generate         | 72.1 ms                                                         | 56.6 ms: 1.28x faster                                                            |
| telco                      | 5.51 ms                                                         | 4.40 ms: 1.25x faster                                                            |
| docutils                   | 1.98 sec                                                        | 1.59 sec: 1.25x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 70.9 ms: 1.23x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 64.3 ms: 1.21x faster                                                            |
| typing_runtime_protocols   | 126 us                                                          | 105 us: 1.21x faster                                                             |
| unpickle                   | 9.71 us                                                         | 8.50 us: 1.14x faster                                                            |
| regex_v8                   | 15.0 ms                                                         | 13.9 ms: 1.09x faster                                                            |
| regex_dna                  | 127 ms                                                          | 118 ms: 1.08x faster                                                             |
| pickle_list                | 3.37 us                                                         | 3.27 us: 1.03x faster                                                            |
| unpickle_list              | 2.95 us                                                         | 2.88 us: 1.02x faster                                                            |
| pickle                     | 7.79 us                                                         | 7.93 us: 1.02x slower                                                            |
| coverage                   | 48.4 ms                                                         | 49.7 ms: 1.03x slower                                                            |
| python_startup             | 22.4 ms                                                         | 25.3 ms: 1.13x slower                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 91.7 ms: 1.22x slower                                                            |
| gc_traversal               | 1.44 ms                                                         | 2.06 ms: 1.43x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.26 ms: 1.93x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.49x faster                                                                     |

Benchmark hidden because not significant (2): pickle_dict, python_startup_no_site
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250816-3.15.0a0-3663b2a/bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.480x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.47x
- 95% likely to have a speedup of 1.45x
- 99% likely to have a speedup of 1.44x

# Memory
- memory change: unknown