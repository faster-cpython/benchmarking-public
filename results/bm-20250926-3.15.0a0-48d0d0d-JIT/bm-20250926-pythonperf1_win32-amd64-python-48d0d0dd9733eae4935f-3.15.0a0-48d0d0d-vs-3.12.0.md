# Results vs. 3.12.0

- fork: python
- ref: 48d0d0dd9733eae4935f
- machine: windows-amd64
- commit hash: 48d0d0d
- commit date: 2025-09-26
- overall geometric mean: 1.537x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.48x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 214 ms: 1.31x faster                                                             |
| docutils       | 1.98 sec                                                        | 1.62 sec: 1.23x faster                                                           |
| Geometric mean | (ref)                                                           | 1.27x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io              | 693 ms                                                          | 383 ms: 1.81x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 201 ms: 1.81x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 378 ms: 1.79x faster                                                             |
| async_tree_none            | 298 ms                                                          | 170 ms: 1.75x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 330 ms: 1.71x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 166 ms: 1.68x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 210 ms: 1.67x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 334 ms: 1.63x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.73x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 53.8 ms: 2.36x faster                                                            |
| float          | 76.7 ms                                                         | 39.7 ms: 1.93x faster                                                            |
| pidigits       | 199 ms                                                          | 147 ms: 1.36x faster                                                             |
| Geometric mean | (ref)                                                           | 1.84x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 76.8 ms: 1.68x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.54 ms: 1.32x faster                                                            |
| regex_dna      | 127 ms                                                          | 118 ms: 1.08x faster                                                             |
| regex_v8       | 15.0 ms                                                         | 14.4 ms: 1.04x faster                                                            |
| Geometric mean | (ref)                                                           | 1.26x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 104 us: 2.02x faster                                                             |
| tomli_loads          | 2.20 sec                                                        | 1.09 sec: 2.02x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 34.7 ms: 1.53x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 196 us: 1.46x faster                                                             |
| xml_etree_generate   | 72.1 ms                                                         | 49.7 ms: 1.45x faster                                                            |
| json_loads           | 20.4 us                                                         | 14.0 us: 1.45x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 5.41 ms: 1.37x faster                                                            |
| xml_etree_parse      | 113 ms                                                          | 86.0 ms: 1.31x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 60.9 ms: 1.27x faster                                                            |
| unpickle             | 9.71 us                                                         | 8.71 us: 1.11x faster                                                            |
| unpickle_list        | 2.95 us                                                         | 2.78 us: 1.06x faster                                                            |
| pickle_list          | 3.37 us                                                         | 3.32 us: 1.01x faster                                                            |
| pickle               | 7.79 us                                                         | 8.01 us: 1.03x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.32x faster                                                                     |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 18.9 ms: 1.01x faster                                                            |
| python_startup         | 22.4 ms                                                         | 25.2 ms: 1.13x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.06x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.31 ms: 1.88x faster                                                            |
| django_template | 36.9 ms                                                         | 24.0 ms: 1.54x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.70x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 1.38 sec: 12.78x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 29.3 ms: 3.12x faster                                                            |
| mdp                        | 1.91 sec                                                        | 787 ms: 2.43x faster                                                             |
| nbody                      | 127 ms                                                          | 53.8 ms: 2.36x faster                                                            |
| deepcopy_memo              | 38.4 us                                                         | 16.7 us: 2.30x faster                                                            |
| deepcopy                   | 360 us                                                          | 163 us: 2.21x faster                                                             |
| unpickle_pure_python       | 210 us                                                          | 104 us: 2.02x faster                                                             |
| tomli_loads                | 2.20 sec                                                        | 1.09 sec: 2.02x faster                                                           |
| scimark_fft                | 271 ms                                                          | 135 ms: 2.01x faster                                                             |
| generators                 | 38.5 ms                                                         | 19.2 ms: 2.00x faster                                                            |
| float                      | 76.7 ms                                                         | 39.7 ms: 1.93x faster                                                            |
| unpack_sequence            | 62.5 ns                                                         | 33.3 ns: 1.88x faster                                                            |
| mako                       | 9.96 ms                                                         | 5.31 ms: 1.88x faster                                                            |
| logging_silent             | 101 ns                                                          | 54.3 ns: 1.86x faster                                                            |
| go                         | 137 ms                                                          | 75.5 ms: 1.82x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 1.78 us: 1.81x faster                                                            |
| async_tree_io              | 693 ms                                                          | 383 ms: 1.81x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 201 ms: 1.81x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 378 ms: 1.79x faster                                                             |
| comprehensions             | 19.2 us                                                         | 10.7 us: 1.79x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.16 ms: 1.78x faster                                                            |
| raytrace                   | 308 ms                                                          | 173 ms: 1.78x faster                                                             |
| pprint_pformat             | 1.50 sec                                                        | 856 ms: 1.75x faster                                                             |
| async_tree_none            | 298 ms                                                          | 170 ms: 1.75x faster                                                             |
| chaos                      | 69.4 ms                                                         | 40.0 ms: 1.74x faster                                                            |
| hexiom                     | 6.82 ms                                                         | 3.93 ms: 1.73x faster                                                            |
| pprint_safe_repr           | 721 ms                                                          | 416 ms: 1.73x faster                                                             |
| pyflate                    | 424 ms                                                          | 247 ms: 1.72x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 330 ms: 1.71x faster                                                             |
| fannkuch                   | 354 ms                                                          | 209 ms: 1.69x faster                                                             |
| regex_compile              | 129 ms                                                          | 76.8 ms: 1.68x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 166 ms: 1.68x faster                                                             |
| deltablue                  | 3.58 ms                                                         | 2.14 ms: 1.67x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 210 ms: 1.67x faster                                                             |
| scimark_monte_carlo        | 66.4 ms                                                         | 40.0 ms: 1.66x faster                                                            |
| scimark_sor                | 130 ms                                                          | 78.6 ms: 1.65x faster                                                            |
| logging_simple             | 9.75 us                                                         | 5.94 us: 1.64x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 334 ms: 1.63x faster                                                             |
| logging_format             | 10.4 us                                                         | 6.43 us: 1.62x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 58.6 ms: 1.59x faster                                                            |
| spectral_norm              | 104 ms                                                          | 65.8 ms: 1.58x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 59.5 ms: 1.57x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 44.8 ms: 1.54x faster                                                            |
| richards                   | 41.3 ms                                                         | 26.8 ms: 1.54x faster                                                            |
| django_template            | 36.9 ms                                                         | 24.0 ms: 1.54x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 34.7 ms: 1.53x faster                                                            |
| richards_super             | 46.5 ms                                                         | 30.3 ms: 1.53x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 38.9 ms: 1.50x faster                                                            |
| pickle_pure_python         | 286 us                                                          | 196 us: 1.46x faster                                                             |
| sympy_sum                  | 123 ms                                                          | 84.7 ms: 1.45x faster                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 49.7 ms: 1.45x faster                                                            |
| json_loads                 | 20.4 us                                                         | 14.0 us: 1.45x faster                                                            |
| sympy_str                  | 240 ms                                                          | 166 ms: 1.44x faster                                                             |
| json                       | 4.15 ms                                                         | 2.89 ms: 1.44x faster                                                            |
| pycparser                  | 978 ms                                                          | 683 ms: 1.43x faster                                                             |
| sympy_integrate            | 17.5 ms                                                         | 12.3 ms: 1.42x faster                                                            |
| telco                      | 5.51 ms                                                         | 3.91 ms: 1.41x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 15.0 ms: 1.40x faster                                                            |
| sympy_expand               | 398 ms                                                          | 288 ms: 1.38x faster                                                             |
| json_dumps                 | 7.40 ms                                                         | 5.41 ms: 1.37x faster                                                            |
| pidigits                   | 199 ms                                                          | 147 ms: 1.36x faster                                                             |
| sqlite_synth               | 2.07 us                                                         | 1.52 us: 1.36x faster                                                            |
| asyncio_tcp                | 662 ms                                                          | 491 ms: 1.35x faster                                                             |
| regex_effbot               | 2.04 ms                                                         | 1.54 ms: 1.32x faster                                                            |
| async_generators           | 313 ms                                                          | 238 ms: 1.31x faster                                                             |
| xml_etree_parse            | 113 ms                                                          | 86.0 ms: 1.31x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 840 us: 1.31x faster                                                             |
| 2to3                       | 280 ms                                                          | 214 ms: 1.31x faster                                                             |
| xml_etree_iterparse        | 77.6 ms                                                         | 60.9 ms: 1.27x faster                                                            |
| typing_runtime_protocols   | 126 us                                                          | 102 us: 1.24x faster                                                             |
| docutils                   | 1.98 sec                                                        | 1.62 sec: 1.23x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 72.5 ms: 1.20x faster                                                            |
| unpickle                   | 9.71 us                                                         | 8.71 us: 1.11x faster                                                            |
| regex_dna                  | 127 ms                                                          | 118 ms: 1.08x faster                                                             |
| unpickle_list              | 2.95 us                                                         | 2.78 us: 1.06x faster                                                            |
| regex_v8                   | 15.0 ms                                                         | 14.4 ms: 1.04x faster                                                            |
| pickle_list                | 3.37 us                                                         | 3.32 us: 1.01x faster                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 18.9 ms: 1.01x faster                                                            |
| coverage                   | 48.4 ms                                                         | 49.0 ms: 1.01x slower                                                            |
| pickle                     | 7.79 us                                                         | 8.01 us: 1.03x slower                                                            |
| python_startup             | 22.4 ms                                                         | 25.2 ms: 1.13x slower                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 89.3 ms: 1.18x slower                                                            |
| gc_traversal               | 1.44 ms                                                         | 2.10 ms: 1.46x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.27 ms: 1.96x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.53x faster                                                                     |

Benchmark hidden because not significant (1): pickle_dict
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250926-3.15.0a0-48d0d0d-JIT/bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.537x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.54x
- 95% likely to have a speedup of 1.53x
- 99% likely to have a speedup of 1.48x

# Memory
- memory change: unknown