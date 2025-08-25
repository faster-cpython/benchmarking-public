# Results vs. 3.12.0

- fork: python
- ref: 6fcac09401e336b25833
- machine: windows-amd64
- commit hash: 6fcac09
- commit date: 2025-08-23
- overall geometric mean: 1.526x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.48x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 214 ms: 1.31x faster                                                             |
| docutils       | 1.98 sec                                                        | 1.61 sec: 1.24x faster                                                           |
| Geometric mean | (ref)                                                           | 1.27x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization     | 364 ms                                                          | 201 ms: 1.81x faster                                                             |
| async_tree_io              | 693 ms                                                          | 389 ms: 1.78x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 381 ms: 1.78x faster                                                             |
| async_tree_none            | 298 ms                                                          | 170 ms: 1.75x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 329 ms: 1.71x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 208 ms: 1.68x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 166 ms: 1.67x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 333 ms: 1.64x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.73x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 53.0 ms: 2.39x faster                                                            |
| float          | 76.7 ms                                                         | 43.6 ms: 1.76x faster                                                            |
| pidigits       | 199 ms                                                          | 145 ms: 1.38x faster                                                             |
| Geometric mean | (ref)                                                           | 1.80x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 78.1 ms: 1.65x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.57 ms: 1.30x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 13.1 ms: 1.15x faster                                                            |
| regex_dna      | 127 ms                                                          | 116 ms: 1.10x faster                                                             |
| Geometric mean | (ref)                                                           | 1.28x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 104 us: 2.02x faster                                                             |
| tomli_loads          | 2.20 sec                                                        | 1.09 sec: 2.02x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 35.4 ms: 1.51x faster                                                            |
| json_loads           | 20.4 us                                                         | 13.9 us: 1.46x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 201 us: 1.42x faster                                                             |
| xml_etree_generate   | 72.1 ms                                                         | 51.1 ms: 1.41x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 5.38 ms: 1.37x faster                                                            |
| xml_etree_parse      | 113 ms                                                          | 85.5 ms: 1.32x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 61.6 ms: 1.26x faster                                                            |
| unpickle             | 9.71 us                                                         | 8.61 us: 1.13x faster                                                            |
| unpickle_list        | 2.95 us                                                         | 2.69 us: 1.09x faster                                                            |
| pickle_dict          | 19.9 us                                                         | 19.5 us: 1.02x faster                                                            |
| pickle_list          | 3.37 us                                                         | 3.33 us: 1.01x faster                                                            |
| pickle               | 7.79 us                                                         | 7.72 us: 1.01x faster                                                            |
| Geometric mean       | (ref)                                                           | 1.33x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup | 22.4 ms                                                         | 25.2 ms: 1.13x slower                                                            |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                     |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.20 ms: 1.91x faster                                                            |
| django_template | 36.9 ms                                                         | 24.1 ms: 1.53x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.71x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 1.24 sec: 14.22x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 30.1 ms: 3.03x faster                                                            |
| mdp                        | 1.91 sec                                                        | 788 ms: 2.43x faster                                                             |
| nbody                      | 127 ms                                                          | 53.0 ms: 2.39x faster                                                            |
| deepcopy                   | 360 us                                                          | 170 us: 2.12x faster                                                             |
| unpickle_pure_python       | 210 us                                                          | 104 us: 2.02x faster                                                             |
| tomli_loads                | 2.20 sec                                                        | 1.09 sec: 2.02x faster                                                           |
| generators                 | 38.5 ms                                                         | 19.2 ms: 2.00x faster                                                            |
| deepcopy_memo              | 38.4 us                                                         | 19.8 us: 1.94x faster                                                            |
| mako                       | 9.96 ms                                                         | 5.20 ms: 1.91x faster                                                            |
| comprehensions             | 19.2 us                                                         | 10.3 us: 1.87x faster                                                            |
| logging_silent             | 101 ns                                                          | 54.4 ns: 1.86x faster                                                            |
| unpack_sequence            | 62.5 ns                                                         | 34.4 ns: 1.82x faster                                                            |
| scimark_fft                | 271 ms                                                          | 149 ms: 1.81x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 201 ms: 1.81x faster                                                             |
| asyncio_tcp                | 662 ms                                                          | 368 ms: 1.80x faster                                                             |
| go                         | 137 ms                                                          | 76.8 ms: 1.79x faster                                                            |
| raytrace                   | 308 ms                                                          | 172 ms: 1.79x faster                                                             |
| async_tree_io              | 693 ms                                                          | 389 ms: 1.78x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 381 ms: 1.78x faster                                                             |
| pprint_pformat             | 1.50 sec                                                        | 851 ms: 1.76x faster                                                             |
| float                      | 76.7 ms                                                         | 43.6 ms: 1.76x faster                                                            |
| async_tree_none            | 298 ms                                                          | 170 ms: 1.75x faster                                                             |
| deepcopy_reduce            | 3.23 us                                                         | 1.85 us: 1.75x faster                                                            |
| pprint_safe_repr           | 721 ms                                                          | 417 ms: 1.73x faster                                                             |
| hexiom                     | 6.82 ms                                                         | 3.95 ms: 1.73x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 329 ms: 1.71x faster                                                             |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.27 ms: 1.70x faster                                                            |
| chaos                      | 69.4 ms                                                         | 41.1 ms: 1.69x faster                                                            |
| spectral_norm              | 104 ms                                                          | 61.5 ms: 1.69x faster                                                            |
| scimark_sor                | 130 ms                                                          | 77.1 ms: 1.68x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 208 ms: 1.68x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 166 ms: 1.67x faster                                                             |
| fannkuch                   | 354 ms                                                          | 212 ms: 1.66x faster                                                             |
| regex_compile              | 129 ms                                                          | 78.1 ms: 1.65x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 40.3 ms: 1.65x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 333 ms: 1.64x faster                                                             |
| logging_format             | 10.4 us                                                         | 6.44 us: 1.61x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 2.22 ms: 1.61x faster                                                            |
| logging_simple             | 9.75 us                                                         | 6.05 us: 1.61x faster                                                            |
| pyflate                    | 424 ms                                                          | 268 ms: 1.58x faster                                                             |
| nqueens                    | 93.7 ms                                                         | 59.7 ms: 1.57x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 59.7 ms: 1.56x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 44.6 ms: 1.55x faster                                                            |
| richards                   | 41.3 ms                                                         | 26.7 ms: 1.55x faster                                                            |
| richards_super             | 46.5 ms                                                         | 30.1 ms: 1.54x faster                                                            |
| django_template            | 36.9 ms                                                         | 24.1 ms: 1.53x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 35.4 ms: 1.51x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 39.1 ms: 1.50x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 14.0 ms: 1.49x faster                                                            |
| json_loads                 | 20.4 us                                                         | 13.9 us: 1.46x faster                                                            |
| telco                      | 5.51 ms                                                         | 3.82 ms: 1.44x faster                                                            |
| pycparser                  | 978 ms                                                          | 678 ms: 1.44x faster                                                             |
| sympy_sum                  | 123 ms                                                          | 85.5 ms: 1.44x faster                                                            |
| sympy_str                  | 240 ms                                                          | 167 ms: 1.43x faster                                                             |
| sympy_integrate            | 17.5 ms                                                         | 12.3 ms: 1.43x faster                                                            |
| pickle_pure_python         | 286 us                                                          | 201 us: 1.42x faster                                                             |
| xml_etree_generate         | 72.1 ms                                                         | 51.1 ms: 1.41x faster                                                            |
| json                       | 4.15 ms                                                         | 2.98 ms: 1.39x faster                                                            |
| sympy_expand               | 398 ms                                                          | 288 ms: 1.38x faster                                                             |
| pidigits                   | 199 ms                                                          | 145 ms: 1.38x faster                                                             |
| json_dumps                 | 7.40 ms                                                         | 5.38 ms: 1.37x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.52 us: 1.37x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 85.5 ms: 1.32x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 835 us: 1.32x faster                                                             |
| 2to3                       | 280 ms                                                          | 214 ms: 1.31x faster                                                             |
| regex_effbot               | 2.04 ms                                                         | 1.57 ms: 1.30x faster                                                            |
| async_generators           | 313 ms                                                          | 245 ms: 1.28x faster                                                             |
| xml_etree_iterparse        | 77.6 ms                                                         | 61.6 ms: 1.26x faster                                                            |
| typing_runtime_protocols   | 126 us                                                          | 101 us: 1.25x faster                                                             |
| docutils                   | 1.98 sec                                                        | 1.61 sec: 1.24x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 70.4 ms: 1.23x faster                                                            |
| regex_v8                   | 15.0 ms                                                         | 13.1 ms: 1.15x faster                                                            |
| unpickle                   | 9.71 us                                                         | 8.61 us: 1.13x faster                                                            |
| regex_dna                  | 127 ms                                                          | 116 ms: 1.10x faster                                                             |
| unpickle_list              | 2.95 us                                                         | 2.69 us: 1.09x faster                                                            |
| pickle_dict                | 19.9 us                                                         | 19.5 us: 1.02x faster                                                            |
| pickle_list                | 3.37 us                                                         | 3.33 us: 1.01x faster                                                            |
| pickle                     | 7.79 us                                                         | 7.72 us: 1.01x faster                                                            |
| coverage                   | 48.4 ms                                                         | 50.1 ms: 1.03x slower                                                            |
| python_startup             | 22.4 ms                                                         | 25.2 ms: 1.13x slower                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 92.0 ms: 1.22x slower                                                            |
| gc_traversal               | 1.44 ms                                                         | 2.12 ms: 1.47x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.26 ms: 1.93x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.53x faster                                                                     |

Benchmark hidden because not significant (1): python_startup_no_site
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250823-3.15.0a0-6fcac09-JIT/bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.526x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.54x
- 95% likely to have a speedup of 1.52x
- 99% likely to have a speedup of 1.48x

# Memory
- memory change: unknown