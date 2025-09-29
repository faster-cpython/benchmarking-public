# Results vs. 3.12.0

- fork: python
- ref: 48d0d0dd9733eae4935f
- machine: windows-amd64
- commit hash: 48d0d0d
- commit date: 2025-09-26
- overall geometric mean: 1.454x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.41x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 214 ms: 1.30x faster                                                             |
| docutils       | 1.98 sec                                                        | 1.62 sec: 1.23x faster                                                           |
| Geometric mean | (ref)                                                           | 1.26x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io              | 693 ms                                                          | 381 ms: 1.82x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 204 ms: 1.79x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 384 ms: 1.76x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 326 ms: 1.73x faster                                                             |
| async_tree_none            | 298 ms                                                          | 173 ms: 1.72x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 206 ms: 1.70x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 168 ms: 1.65x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 336 ms: 1.63x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.72x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 68.5 ms: 1.85x faster                                                            |
| float          | 76.7 ms                                                         | 44.7 ms: 1.72x faster                                                            |
| pidigits       | 199 ms                                                          | 151 ms: 1.32x faster                                                             |
| Geometric mean | (ref)                                                           | 1.61x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 81.4 ms: 1.59x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.55 ms: 1.31x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 14.3 ms: 1.05x faster                                                            |
| regex_dna      | 127 ms                                                          | 121 ms: 1.05x faster                                                             |
| Geometric mean | (ref)                                                           | 1.23x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.41 sec: 1.56x faster                                                           |
| unpickle_pure_python | 210 us                                                          | 138 us: 1.52x faster                                                             |
| json_loads           | 20.4 us                                                         | 14.4 us: 1.41x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 5.41 ms: 1.37x faster                                                            |
| xml_etree_process    | 53.2 ms                                                         | 39.5 ms: 1.35x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 218 us: 1.31x faster                                                             |
| xml_etree_generate   | 72.1 ms                                                         | 56.8 ms: 1.27x faster                                                            |
| xml_etree_parse      | 113 ms                                                          | 90.2 ms: 1.25x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 64.9 ms: 1.20x faster                                                            |
| unpickle             | 9.71 us                                                         | 8.68 us: 1.12x faster                                                            |
| unpickle_list        | 2.95 us                                                         | 2.81 us: 1.05x faster                                                            |
| pickle_dict          | 19.9 us                                                         | 19.4 us: 1.03x faster                                                            |
| pickle_list          | 3.37 us                                                         | 3.31 us: 1.02x faster                                                            |
| Geometric mean       | (ref)                                                           | 1.23x faster                                                                     |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup | 22.4 ms                                                         | 25.4 ms: 1.14x slower                                                            |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                     |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.9 ms                                                         | 24.7 ms: 1.50x faster                                                            |
| mako            | 9.96 ms                                                         | 6.89 ms: 1.45x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.47x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 1.31 sec: 13.50x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 29.7 ms: 3.08x faster                                                            |
| mdp                        | 1.91 sec                                                        | 814 ms: 2.35x faster                                                             |
| deepcopy_memo              | 38.4 us                                                         | 17.5 us: 2.19x faster                                                            |
| deepcopy                   | 360 us                                                          | 167 us: 2.15x faster                                                             |
| generators                 | 38.5 ms                                                         | 19.7 ms: 1.96x faster                                                            |
| nbody                      | 127 ms                                                          | 68.5 ms: 1.85x faster                                                            |
| async_tree_io              | 693 ms                                                          | 381 ms: 1.82x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 204 ms: 1.79x faster                                                             |
| deepcopy_reduce            | 3.23 us                                                         | 1.81 us: 1.78x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 384 ms: 1.76x faster                                                             |
| unpack_sequence            | 62.5 ns                                                         | 35.8 ns: 1.74x faster                                                            |
| go                         | 137 ms                                                          | 78.8 ms: 1.74x faster                                                            |
| logging_silent             | 101 ns                                                          | 58.4 ns: 1.73x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 326 ms: 1.73x faster                                                             |
| async_tree_none            | 298 ms                                                          | 173 ms: 1.72x faster                                                             |
| float                      | 76.7 ms                                                         | 44.7 ms: 1.72x faster                                                            |
| raytrace                   | 308 ms                                                          | 180 ms: 1.71x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 206 ms: 1.70x faster                                                             |
| comprehensions             | 19.2 us                                                         | 11.3 us: 1.69x faster                                                            |
| chaos                      | 69.4 ms                                                         | 41.8 ms: 1.66x faster                                                            |
| scimark_sor                | 130 ms                                                          | 78.5 ms: 1.65x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 168 ms: 1.65x faster                                                             |
| hexiom                     | 6.82 ms                                                         | 4.14 ms: 1.65x faster                                                            |
| logging_simple             | 9.75 us                                                         | 5.99 us: 1.63x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 336 ms: 1.63x faster                                                             |
| scimark_monte_carlo        | 66.4 ms                                                         | 41.2 ms: 1.61x faster                                                            |
| logging_format             | 10.4 us                                                         | 6.45 us: 1.61x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 2.23 ms: 1.61x faster                                                            |
| regex_compile              | 129 ms                                                          | 81.4 ms: 1.59x faster                                                            |
| tomli_loads                | 2.20 sec                                                        | 1.41 sec: 1.56x faster                                                           |
| spectral_norm              | 104 ms                                                          | 67.1 ms: 1.55x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 60.3 ms: 1.55x faster                                                            |
| scimark_fft                | 271 ms                                                          | 177 ms: 1.53x faster                                                             |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.53 ms: 1.52x faster                                                            |
| asyncio_tcp                | 662 ms                                                          | 435 ms: 1.52x faster                                                             |
| unpickle_pure_python       | 210 us                                                          | 138 us: 1.52x faster                                                             |
| django_template            | 36.9 ms                                                         | 24.7 ms: 1.50x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 63.0 ms: 1.49x faster                                                            |
| richards_super             | 46.5 ms                                                         | 31.3 ms: 1.48x faster                                                            |
| richards                   | 41.3 ms                                                         | 27.9 ms: 1.48x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 39.6 ms: 1.48x faster                                                            |
| pprint_pformat             | 1.50 sec                                                        | 1.02 sec: 1.46x faster                                                           |
| pyflate                    | 424 ms                                                          | 290 ms: 1.46x faster                                                             |
| crypto_pyaes               | 69.2 ms                                                         | 47.8 ms: 1.45x faster                                                            |
| mako                       | 9.96 ms                                                         | 6.89 ms: 1.45x faster                                                            |
| pprint_safe_repr           | 721 ms                                                          | 501 ms: 1.44x faster                                                             |
| coroutines                 | 20.9 ms                                                         | 14.5 ms: 1.44x faster                                                            |
| sympy_str                  | 240 ms                                                          | 168 ms: 1.42x faster                                                             |
| json                       | 4.15 ms                                                         | 2.92 ms: 1.42x faster                                                            |
| json_loads                 | 20.4 us                                                         | 14.4 us: 1.41x faster                                                            |
| sympy_sum                  | 123 ms                                                          | 87.4 ms: 1.41x faster                                                            |
| sympy_expand               | 398 ms                                                          | 286 ms: 1.39x faster                                                             |
| pycparser                  | 978 ms                                                          | 702 ms: 1.39x faster                                                             |
| sympy_integrate            | 17.5 ms                                                         | 12.6 ms: 1.39x faster                                                            |
| json_dumps                 | 7.40 ms                                                         | 5.41 ms: 1.37x faster                                                            |
| async_generators           | 313 ms                                                          | 230 ms: 1.36x faster                                                             |
| xml_etree_process          | 53.2 ms                                                         | 39.5 ms: 1.35x faster                                                            |
| fannkuch                   | 354 ms                                                          | 268 ms: 1.32x faster                                                             |
| pidigits                   | 199 ms                                                          | 151 ms: 1.32x faster                                                             |
| pickle_pure_python         | 286 us                                                          | 218 us: 1.31x faster                                                             |
| regex_effbot               | 2.04 ms                                                         | 1.55 ms: 1.31x faster                                                            |
| 2to3                       | 280 ms                                                          | 214 ms: 1.30x faster                                                             |
| sqlite_synth               | 2.07 us                                                         | 1.59 us: 1.30x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 852 us: 1.29x faster                                                             |
| telco                      | 5.51 ms                                                         | 4.29 ms: 1.29x faster                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 56.8 ms: 1.27x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 90.2 ms: 1.25x faster                                                            |
| docutils                   | 1.98 sec                                                        | 1.62 sec: 1.23x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 64.9 ms: 1.20x faster                                                            |
| typing_runtime_protocols   | 126 us                                                          | 106 us: 1.19x faster                                                             |
| meteor_contest             | 86.9 ms                                                         | 73.9 ms: 1.18x faster                                                            |
| unpickle                   | 9.71 us                                                         | 8.68 us: 1.12x faster                                                            |
| regex_v8                   | 15.0 ms                                                         | 14.3 ms: 1.05x faster                                                            |
| regex_dna                  | 127 ms                                                          | 121 ms: 1.05x faster                                                             |
| unpickle_list              | 2.95 us                                                         | 2.81 us: 1.05x faster                                                            |
| pickle_dict                | 19.9 us                                                         | 19.4 us: 1.03x faster                                                            |
| pickle_list                | 3.37 us                                                         | 3.31 us: 1.02x faster                                                            |
| coverage                   | 48.4 ms                                                         | 49.3 ms: 1.02x slower                                                            |
| python_startup             | 22.4 ms                                                         | 25.4 ms: 1.14x slower                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 90.6 ms: 1.20x slower                                                            |
| gc_traversal               | 1.44 ms                                                         | 2.10 ms: 1.46x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.28 ms: 1.97x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.46x faster                                                                     |

Benchmark hidden because not significant (2): python_startup_no_site, pickle
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250926-3.15.0a0-48d0d0d/bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.454x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.44x
- 95% likely to have a speedup of 1.43x
- 99% likely to have a speedup of 1.41x

# Memory
- memory change: unknown