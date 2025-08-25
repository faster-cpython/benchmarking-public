# Results vs. 3.12.0

- fork: python
- ref: 6fcac09401e336b25833
- machine: windows-amd64
- commit hash: 6fcac09
- commit date: 2025-08-23
- overall geometric mean: 1.483x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.44x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 217 ms: 1.29x faster                                                             |
| docutils       | 1.98 sec                                                        | 1.59 sec: 1.25x faster                                                           |
| Geometric mean | (ref)                                                           | 1.27x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization     | 364 ms                                                          | 201 ms: 1.81x faster                                                             |
| async_tree_io              | 693 ms                                                          | 389 ms: 1.78x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 384 ms: 1.77x faster                                                             |
| async_tree_none            | 298 ms                                                          | 173 ms: 1.72x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 327 ms: 1.72x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 205 ms: 1.71x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 168 ms: 1.66x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 332 ms: 1.65x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.73x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 64.0 ms: 1.98x faster                                                            |
| float          | 76.7 ms                                                         | 43.5 ms: 1.76x faster                                                            |
| pidigits       | 199 ms                                                          | 143 ms: 1.39x faster                                                             |
| Geometric mean | (ref)                                                           | 1.69x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 78.7 ms: 1.64x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.57 ms: 1.29x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 13.8 ms: 1.09x faster                                                            |
| regex_dna      | 127 ms                                                          | 120 ms: 1.06x faster                                                             |
| Geometric mean | (ref)                                                           | 1.25x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.39 sec: 1.58x faster                                                           |
| unpickle_pure_python | 210 us                                                          | 134 us: 1.57x faster                                                             |
| json_loads           | 20.4 us                                                         | 14.3 us: 1.42x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 5.34 ms: 1.39x faster                                                            |
| xml_etree_process    | 53.2 ms                                                         | 38.7 ms: 1.37x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 211 us: 1.36x faster                                                             |
| xml_etree_parse      | 113 ms                                                          | 85.6 ms: 1.32x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 56.4 ms: 1.28x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 62.3 ms: 1.25x faster                                                            |
| unpickle             | 9.71 us                                                         | 8.53 us: 1.14x faster                                                            |
| unpickle_list        | 2.95 us                                                         | 2.83 us: 1.04x faster                                                            |
| pickle_dict          | 19.9 us                                                         | 19.2 us: 1.04x faster                                                            |
| pickle_list          | 3.37 us                                                         | 3.28 us: 1.03x faster                                                            |
| pickle               | 7.79 us                                                         | 7.87 us: 1.01x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.26x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup | 22.4 ms                                                         | 25.1 ms: 1.12x slower                                                            |
| Geometric mean | (ref)                                                           | 1.07x slower                                                                     |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 6.56 ms: 1.52x faster                                                            |
| django_template | 36.9 ms                                                         | 24.4 ms: 1.51x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.52x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 1.25 sec: 14.13x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 29.9 ms: 3.06x faster                                                            |
| mdp                        | 1.91 sec                                                        | 794 ms: 2.41x faster                                                             |
| deepcopy                   | 360 us                                                          | 169 us: 2.13x faster                                                             |
| generators                 | 38.5 ms                                                         | 18.8 ms: 2.05x faster                                                            |
| deepcopy_memo              | 38.4 us                                                         | 19.3 us: 1.99x faster                                                            |
| nbody                      | 127 ms                                                          | 64.0 ms: 1.98x faster                                                            |
| logging_silent             | 101 ns                                                          | 54.6 ns: 1.85x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 201 ms: 1.81x faster                                                             |
| go                         | 137 ms                                                          | 76.1 ms: 1.81x faster                                                            |
| async_tree_io              | 693 ms                                                          | 389 ms: 1.78x faster                                                             |
| comprehensions             | 19.2 us                                                         | 10.8 us: 1.77x faster                                                            |
| raytrace                   | 308 ms                                                          | 174 ms: 1.77x faster                                                             |
| chaos                      | 69.4 ms                                                         | 39.3 ms: 1.77x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 384 ms: 1.77x faster                                                             |
| float                      | 76.7 ms                                                         | 43.5 ms: 1.76x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 1.84 us: 1.75x faster                                                            |
| asyncio_tcp                | 662 ms                                                          | 379 ms: 1.75x faster                                                             |
| async_tree_none            | 298 ms                                                          | 173 ms: 1.72x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 327 ms: 1.72x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 205 ms: 1.71x faster                                                             |
| scimark_monte_carlo        | 66.4 ms                                                         | 39.0 ms: 1.71x faster                                                            |
| scimark_sor                | 130 ms                                                          | 76.3 ms: 1.70x faster                                                            |
| hexiom                     | 6.82 ms                                                         | 4.04 ms: 1.69x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 168 ms: 1.66x faster                                                             |
| scimark_lu                 | 93.2 ms                                                         | 56.4 ms: 1.65x faster                                                            |
| unpack_sequence            | 62.5 ns                                                         | 37.9 ns: 1.65x faster                                                            |
| spectral_norm              | 104 ms                                                          | 63.1 ms: 1.65x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 332 ms: 1.65x faster                                                             |
| regex_compile              | 129 ms                                                          | 78.7 ms: 1.64x faster                                                            |
| logging_simple             | 9.75 us                                                         | 5.97 us: 1.63x faster                                                            |
| logging_format             | 10.4 us                                                         | 6.48 us: 1.61x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 2.23 ms: 1.61x faster                                                            |
| tomli_loads                | 2.20 sec                                                        | 1.39 sec: 1.58x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 134 us: 1.57x faster                                                             |
| richards                   | 41.3 ms                                                         | 26.6 ms: 1.55x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 60.8 ms: 1.54x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.51 ms: 1.54x faster                                                            |
| richards_super             | 46.5 ms                                                         | 30.3 ms: 1.53x faster                                                            |
| pprint_pformat             | 1.50 sec                                                        | 981 ms: 1.53x faster                                                             |
| mako                       | 9.96 ms                                                         | 6.56 ms: 1.52x faster                                                            |
| django_template            | 36.9 ms                                                         | 24.4 ms: 1.51x faster                                                            |
| pprint_safe_repr           | 721 ms                                                          | 478 ms: 1.51x faster                                                             |
| scimark_fft                | 271 ms                                                          | 180 ms: 1.51x faster                                                             |
| dulwich_log                | 58.5 ms                                                         | 39.0 ms: 1.50x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 14.0 ms: 1.49x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 46.7 ms: 1.48x faster                                                            |
| pyflate                    | 424 ms                                                          | 288 ms: 1.47x faster                                                             |
| sympy_str                  | 240 ms                                                          | 165 ms: 1.45x faster                                                             |
| sympy_sum                  | 123 ms                                                          | 85.3 ms: 1.44x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 12.3 ms: 1.42x faster                                                            |
| json_loads                 | 20.4 us                                                         | 14.3 us: 1.42x faster                                                            |
| sympy_expand               | 398 ms                                                          | 281 ms: 1.42x faster                                                             |
| pycparser                  | 978 ms                                                          | 701 ms: 1.39x faster                                                             |
| async_generators           | 313 ms                                                          | 225 ms: 1.39x faster                                                             |
| pidigits                   | 199 ms                                                          | 143 ms: 1.39x faster                                                             |
| json_dumps                 | 7.40 ms                                                         | 5.34 ms: 1.39x faster                                                            |
| json                       | 4.15 ms                                                         | 3.00 ms: 1.38x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 38.7 ms: 1.37x faster                                                            |
| fannkuch                   | 354 ms                                                          | 260 ms: 1.36x faster                                                             |
| pickle_pure_python         | 286 us                                                          | 211 us: 1.36x faster                                                             |
| telco                      | 5.51 ms                                                         | 4.13 ms: 1.33x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.55 us: 1.33x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 85.6 ms: 1.32x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 839 us: 1.31x faster                                                             |
| regex_effbot               | 2.04 ms                                                         | 1.57 ms: 1.29x faster                                                            |
| 2to3                       | 280 ms                                                          | 217 ms: 1.29x faster                                                             |
| xml_etree_generate         | 72.1 ms                                                         | 56.4 ms: 1.28x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 62.3 ms: 1.25x faster                                                            |
| docutils                   | 1.98 sec                                                        | 1.59 sec: 1.25x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 71.5 ms: 1.22x faster                                                            |
| typing_runtime_protocols   | 126 us                                                          | 104 us: 1.21x faster                                                             |
| unpickle                   | 9.71 us                                                         | 8.53 us: 1.14x faster                                                            |
| regex_v8                   | 15.0 ms                                                         | 13.8 ms: 1.09x faster                                                            |
| regex_dna                  | 127 ms                                                          | 120 ms: 1.06x faster                                                             |
| unpickle_list              | 2.95 us                                                         | 2.83 us: 1.04x faster                                                            |
| pickle_dict                | 19.9 us                                                         | 19.2 us: 1.04x faster                                                            |
| pickle_list                | 3.37 us                                                         | 3.28 us: 1.03x faster                                                            |
| pickle                     | 7.79 us                                                         | 7.87 us: 1.01x slower                                                            |
| coverage                   | 48.4 ms                                                         | 48.9 ms: 1.01x slower                                                            |
| python_startup             | 22.4 ms                                                         | 25.1 ms: 1.12x slower                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 91.9 ms: 1.22x slower                                                            |
| gc_traversal               | 1.44 ms                                                         | 2.05 ms: 1.42x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.26 ms: 1.93x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.49x faster                                                                     |

Benchmark hidden because not significant (1): python_startup_no_site
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250823-3.15.0a0-6fcac09/bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.483x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.48x
- 95% likely to have a speedup of 1.46x
- 99% likely to have a speedup of 1.44x

# Memory
- memory change: unknown