# Results vs. 3.12.0

- fork: python
- ref: 3663b2ad54c9e15775a6
- machine: windows-amd64
- commit hash: 3663b2a
- commit date: 2025-08-16
- overall geometric mean: 1.522x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.48x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 216 ms: 1.29x faster                                                             |
| docutils       | 1.98 sec                                                        | 1.62 sec: 1.22x faster                                                           |
| Geometric mean | (ref)                                                           | 1.26x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization     | 364 ms                                                          | 204 ms: 1.79x faster                                                             |
| async_tree_io              | 693 ms                                                          | 389 ms: 1.78x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 382 ms: 1.77x faster                                                             |
| async_tree_none            | 298 ms                                                          | 172 ms: 1.73x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 330 ms: 1.71x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 166 ms: 1.67x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 213 ms: 1.65x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 336 ms: 1.62x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.72x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 54.6 ms: 2.33x faster                                                            |
| float          | 76.7 ms                                                         | 43.9 ms: 1.75x faster                                                            |
| pidigits       | 199 ms                                                          | 145 ms: 1.38x faster                                                             |
| Geometric mean | (ref)                                                           | 1.77x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 78.0 ms: 1.65x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.52 ms: 1.34x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 13.1 ms: 1.15x faster                                                            |
| regex_dna      | 127 ms                                                          | 114 ms: 1.12x faster                                                             |
| Geometric mean | (ref)                                                           | 1.30x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 105 us: 2.00x faster                                                             |
| tomli_loads          | 2.20 sec                                                        | 1.10 sec: 1.99x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 35.2 ms: 1.51x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 50.2 ms: 1.44x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 199 us: 1.43x faster                                                             |
| json_loads           | 20.4 us                                                         | 14.2 us: 1.43x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 5.39 ms: 1.37x faster                                                            |
| xml_etree_parse      | 113 ms                                                          | 87.7 ms: 1.29x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 61.1 ms: 1.27x faster                                                            |
| unpickle             | 9.71 us                                                         | 8.39 us: 1.16x faster                                                            |
| unpickle_list        | 2.95 us                                                         | 2.75 us: 1.07x faster                                                            |
| pickle_list          | 3.37 us                                                         | 3.21 us: 1.05x faster                                                            |
| pickle               | 7.79 us                                                         | 7.43 us: 1.05x faster                                                            |
| Geometric mean       | (ref)                                                           | 1.33x faster                                                                     |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup | 22.4 ms                                                         | 25.3 ms: 1.13x slower                                                            |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                     |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.20 ms: 1.91x faster                                                            |
| django_template | 36.9 ms                                                         | 23.9 ms: 1.54x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.72x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 1.25 sec: 14.17x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 29.1 ms: 3.15x faster                                                            |
| mdp                        | 1.91 sec                                                        | 801 ms: 2.39x faster                                                             |
| nbody                      | 127 ms                                                          | 54.6 ms: 2.33x faster                                                            |
| deepcopy_memo              | 38.4 us                                                         | 17.8 us: 2.16x faster                                                            |
| deepcopy                   | 360 us                                                          | 168 us: 2.15x faster                                                             |
| generators                 | 38.5 ms                                                         | 18.9 ms: 2.04x faster                                                            |
| unpickle_pure_python       | 210 us                                                          | 105 us: 2.00x faster                                                             |
| tomli_loads                | 2.20 sec                                                        | 1.10 sec: 1.99x faster                                                           |
| unpack_sequence            | 62.5 ns                                                         | 32.5 ns: 1.92x faster                                                            |
| mako                       | 9.96 ms                                                         | 5.20 ms: 1.91x faster                                                            |
| logging_silent             | 101 ns                                                          | 55.2 ns: 1.83x faster                                                            |
| scimark_fft                | 271 ms                                                          | 149 ms: 1.82x faster                                                             |
| comprehensions             | 19.2 us                                                         | 10.5 us: 1.82x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 204 ms: 1.79x faster                                                             |
| async_tree_io              | 693 ms                                                          | 389 ms: 1.78x faster                                                             |
| go                         | 137 ms                                                          | 77.2 ms: 1.78x faster                                                            |
| asyncio_tcp                | 662 ms                                                          | 373 ms: 1.78x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 382 ms: 1.77x faster                                                             |
| deepcopy_reduce            | 3.23 us                                                         | 1.83 us: 1.76x faster                                                            |
| float                      | 76.7 ms                                                         | 43.9 ms: 1.75x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.21 ms: 1.74x faster                                                            |
| async_tree_none            | 298 ms                                                          | 172 ms: 1.73x faster                                                             |
| raytrace                   | 308 ms                                                          | 178 ms: 1.73x faster                                                             |
| chaos                      | 69.4 ms                                                         | 40.2 ms: 1.73x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 330 ms: 1.71x faster                                                             |
| hexiom                     | 6.82 ms                                                         | 3.99 ms: 1.71x faster                                                            |
| fannkuch                   | 354 ms                                                          | 207 ms: 1.71x faster                                                             |
| pprint_pformat             | 1.50 sec                                                        | 891 ms: 1.68x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 166 ms: 1.67x faster                                                             |
| scimark_sor                | 130 ms                                                          | 78.2 ms: 1.66x faster                                                            |
| regex_compile              | 129 ms                                                          | 78.0 ms: 1.65x faster                                                            |
| pprint_safe_repr           | 721 ms                                                          | 436 ms: 1.65x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 213 ms: 1.65x faster                                                             |
| pyflate                    | 424 ms                                                          | 260 ms: 1.63x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 336 ms: 1.62x faster                                                             |
| logging_simple             | 9.75 us                                                         | 6.04 us: 1.61x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 2.22 ms: 1.61x faster                                                            |
| logging_format             | 10.4 us                                                         | 6.47 us: 1.61x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 58.6 ms: 1.59x faster                                                            |
| spectral_norm              | 104 ms                                                          | 65.7 ms: 1.58x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 42.1 ms: 1.58x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 60.0 ms: 1.56x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 44.8 ms: 1.55x faster                                                            |
| django_template            | 36.9 ms                                                         | 23.9 ms: 1.54x faster                                                            |
| richards                   | 41.3 ms                                                         | 26.9 ms: 1.54x faster                                                            |
| richards_super             | 46.5 ms                                                         | 30.6 ms: 1.52x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 13.8 ms: 1.51x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 35.2 ms: 1.51x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 38.7 ms: 1.51x faster                                                            |
| json                       | 4.15 ms                                                         | 2.89 ms: 1.44x faster                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 50.2 ms: 1.44x faster                                                            |
| pickle_pure_python         | 286 us                                                          | 199 us: 1.43x faster                                                             |
| sympy_sum                  | 123 ms                                                          | 85.7 ms: 1.43x faster                                                            |
| json_loads                 | 20.4 us                                                         | 14.2 us: 1.43x faster                                                            |
| sympy_str                  | 240 ms                                                          | 168 ms: 1.42x faster                                                             |
| pycparser                  | 978 ms                                                          | 688 ms: 1.42x faster                                                             |
| sympy_integrate            | 17.5 ms                                                         | 12.4 ms: 1.41x faster                                                            |
| telco                      | 5.51 ms                                                         | 3.94 ms: 1.40x faster                                                            |
| pidigits                   | 199 ms                                                          | 145 ms: 1.38x faster                                                             |
| json_dumps                 | 7.40 ms                                                         | 5.39 ms: 1.37x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.51 us: 1.37x faster                                                            |
| sympy_expand               | 398 ms                                                          | 290 ms: 1.37x faster                                                             |
| regex_effbot               | 2.04 ms                                                         | 1.52 ms: 1.34x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 833 us: 1.32x faster                                                             |
| async_generators           | 313 ms                                                          | 238 ms: 1.32x faster                                                             |
| 2to3                       | 280 ms                                                          | 216 ms: 1.29x faster                                                             |
| xml_etree_parse            | 113 ms                                                          | 87.7 ms: 1.29x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 61.1 ms: 1.27x faster                                                            |
| meteor_contest             | 86.9 ms                                                         | 69.1 ms: 1.26x faster                                                            |
| docutils                   | 1.98 sec                                                        | 1.62 sec: 1.22x faster                                                           |
| typing_runtime_protocols   | 126 us                                                          | 104 us: 1.21x faster                                                             |
| unpickle                   | 9.71 us                                                         | 8.39 us: 1.16x faster                                                            |
| regex_v8                   | 15.0 ms                                                         | 13.1 ms: 1.15x faster                                                            |
| regex_dna                  | 127 ms                                                          | 114 ms: 1.12x faster                                                             |
| unpickle_list              | 2.95 us                                                         | 2.75 us: 1.07x faster                                                            |
| pickle_list                | 3.37 us                                                         | 3.21 us: 1.05x faster                                                            |
| pickle                     | 7.79 us                                                         | 7.43 us: 1.05x faster                                                            |
| coverage                   | 48.4 ms                                                         | 49.7 ms: 1.03x slower                                                            |
| python_startup             | 22.4 ms                                                         | 25.3 ms: 1.13x slower                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 92.8 ms: 1.23x slower                                                            |
| gc_traversal               | 1.44 ms                                                         | 2.20 ms: 1.53x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.31 ms: 2.01x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.53x faster                                                                     |

Benchmark hidden because not significant (2): python_startup_no_site, pickle_dict
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250816-3.15.0a0-3663b2a-JIT/bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.522x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.53x
- 95% likely to have a speedup of 1.52x
- 99% likely to have a speedup of 1.48x

# Memory
- memory change: unknown