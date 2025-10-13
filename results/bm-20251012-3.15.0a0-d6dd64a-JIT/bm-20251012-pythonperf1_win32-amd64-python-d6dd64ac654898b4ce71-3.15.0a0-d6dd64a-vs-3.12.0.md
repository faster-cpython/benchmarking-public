# Results vs. 3.12.0

- fork: python
- ref: d6dd64ac654898b4ce71
- machine: windows-amd64
- commit hash: d6dd64a
- commit date: 2025-10-12
- overall geometric mean: 1.543x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.49x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 218 ms: 1.28x faster                                                             |
| docutils       | 1.98 sec                                                        | 1.61 sec: 1.24x faster                                                           |
| Geometric mean | (ref)                                                           | 1.26x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization     | 364 ms                                                          | 203 ms: 1.79x faster                                                             |
| async_tree_io              | 693 ms                                                          | 393 ms: 1.76x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 387 ms: 1.75x faster                                                             |
| async_tree_none            | 298 ms                                                          | 171 ms: 1.74x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 331 ms: 1.70x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 210 ms: 1.67x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 167 ms: 1.66x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 333 ms: 1.64x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.71x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 55.9 ms: 2.27x faster                                                            |
| float          | 76.7 ms                                                         | 43.8 ms: 1.75x faster                                                            |
| pidigits       | 199 ms                                                          | 147 ms: 1.36x faster                                                             |
| Geometric mean | (ref)                                                           | 1.75x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 77.7 ms: 1.66x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.55 ms: 1.32x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 13.2 ms: 1.14x faster                                                            |
| regex_dna      | 127 ms                                                          | 114 ms: 1.12x faster                                                             |
| Geometric mean | (ref)                                                           | 1.29x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.09 sec: 2.02x faster                                                           |
| unpickle_pure_python | 210 us                                                          | 105 us: 2.00x faster                                                             |
| xml_etree_process    | 53.2 ms                                                         | 35.3 ms: 1.51x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 49.0 ms: 1.47x faster                                                            |
| json_loads           | 20.4 us                                                         | 13.9 us: 1.46x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 202 us: 1.41x faster                                                             |
| json_dumps           | 7.40 ms                                                         | 5.42 ms: 1.37x faster                                                            |
| xml_etree_parse      | 113 ms                                                          | 86.3 ms: 1.31x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 62.7 ms: 1.24x faster                                                            |
| unpickle             | 9.71 us                                                         | 8.45 us: 1.15x faster                                                            |
| unpickle_list        | 2.95 us                                                         | 2.71 us: 1.08x faster                                                            |
| pickle               | 7.79 us                                                         | 7.32 us: 1.06x faster                                                            |
| pickle_list          | 3.37 us                                                         | 3.18 us: 1.06x faster                                                            |
| pickle_dict          | 19.9 us                                                         | 19.0 us: 1.05x faster                                                            |
| Geometric mean       | (ref)                                                           | 1.34x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup | 22.4 ms                                                         | 25.1 ms: 1.12x slower                                                            |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                     |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.27 ms: 1.89x faster                                                            |
| django_template | 36.9 ms                                                         | 24.4 ms: 1.52x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.69x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 1.26 sec: 14.00x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 29.2 ms: 3.14x faster                                                            |
| deepcopy_memo              | 38.4 us                                                         | 13.8 us: 2.78x faster                                                            |
| mdp                        | 1.91 sec                                                        | 786 ms: 2.43x faster                                                             |
| spectral_norm              | 104 ms                                                          | 43.6 ms: 2.38x faster                                                            |
| nbody                      | 127 ms                                                          | 55.9 ms: 2.27x faster                                                            |
| deepcopy                   | 360 us                                                          | 159 us: 2.27x faster                                                             |
| tomli_loads                | 2.20 sec                                                        | 1.09 sec: 2.02x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 105 us: 2.00x faster                                                             |
| scimark_fft                | 271 ms                                                          | 136 ms: 1.99x faster                                                             |
| generators                 | 38.5 ms                                                         | 19.6 ms: 1.97x faster                                                            |
| unpack_sequence            | 62.5 ns                                                         | 32.7 ns: 1.91x faster                                                            |
| mako                       | 9.96 ms                                                         | 5.27 ms: 1.89x faster                                                            |
| logging_silent             | 101 ns                                                          | 54.1 ns: 1.87x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 1.75 us: 1.84x faster                                                            |
| comprehensions             | 19.2 us                                                         | 10.7 us: 1.79x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 203 ms: 1.79x faster                                                             |
| go                         | 137 ms                                                          | 76.9 ms: 1.79x faster                                                            |
| asyncio_tcp                | 662 ms                                                          | 374 ms: 1.77x faster                                                             |
| raytrace                   | 308 ms                                                          | 174 ms: 1.77x faster                                                             |
| async_tree_io              | 693 ms                                                          | 393 ms: 1.76x faster                                                             |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.20 ms: 1.75x faster                                                            |
| float                      | 76.7 ms                                                         | 43.8 ms: 1.75x faster                                                            |
| pprint_pformat             | 1.50 sec                                                        | 857 ms: 1.75x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 387 ms: 1.75x faster                                                             |
| async_tree_none            | 298 ms                                                          | 171 ms: 1.74x faster                                                             |
| chaos                      | 69.4 ms                                                         | 40.6 ms: 1.71x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 331 ms: 1.70x faster                                                             |
| pprint_safe_repr           | 721 ms                                                          | 426 ms: 1.69x faster                                                             |
| pyflate                    | 424 ms                                                          | 252 ms: 1.68x faster                                                             |
| fannkuch                   | 354 ms                                                          | 211 ms: 1.68x faster                                                             |
| logging_simple             | 9.75 us                                                         | 5.82 us: 1.68x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 210 ms: 1.67x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 167 ms: 1.66x faster                                                             |
| regex_compile              | 129 ms                                                          | 77.7 ms: 1.66x faster                                                            |
| hexiom                     | 6.82 ms                                                         | 4.11 ms: 1.66x faster                                                            |
| scimark_sor                | 130 ms                                                          | 79.1 ms: 1.64x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 333 ms: 1.64x faster                                                             |
| logging_format             | 10.4 us                                                         | 6.37 us: 1.63x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 40.7 ms: 1.63x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 2.21 ms: 1.62x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 58.3 ms: 1.60x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 44.1 ms: 1.57x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 60.3 ms: 1.55x faster                                                            |
| django_template            | 36.9 ms                                                         | 24.4 ms: 1.52x faster                                                            |
| richards_super             | 46.5 ms                                                         | 30.7 ms: 1.51x faster                                                            |
| richards                   | 41.3 ms                                                         | 27.3 ms: 1.51x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 35.3 ms: 1.51x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 38.9 ms: 1.50x faster                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 49.0 ms: 1.47x faster                                                            |
| json_loads                 | 20.4 us                                                         | 13.9 us: 1.46x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 14.3 ms: 1.46x faster                                                            |
| sympy_sum                  | 123 ms                                                          | 84.3 ms: 1.46x faster                                                            |
| sympy_str                  | 240 ms                                                          | 166 ms: 1.44x faster                                                             |
| pycparser                  | 978 ms                                                          | 682 ms: 1.43x faster                                                             |
| telco                      | 5.51 ms                                                         | 3.86 ms: 1.43x faster                                                            |
| json                       | 4.15 ms                                                         | 2.92 ms: 1.42x faster                                                            |
| pickle_pure_python         | 286 us                                                          | 202 us: 1.41x faster                                                             |
| sympy_integrate            | 17.5 ms                                                         | 12.4 ms: 1.41x faster                                                            |
| sympy_expand               | 398 ms                                                          | 288 ms: 1.38x faster                                                             |
| json_dumps                 | 7.40 ms                                                         | 5.42 ms: 1.37x faster                                                            |
| pidigits                   | 199 ms                                                          | 147 ms: 1.36x faster                                                             |
| sqlite_synth               | 2.07 us                                                         | 1.53 us: 1.35x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 829 us: 1.33x faster                                                             |
| regex_effbot               | 2.04 ms                                                         | 1.55 ms: 1.32x faster                                                            |
| async_generators           | 313 ms                                                          | 239 ms: 1.31x faster                                                             |
| xml_etree_parse            | 113 ms                                                          | 86.3 ms: 1.31x faster                                                            |
| 2to3                       | 280 ms                                                          | 218 ms: 1.28x faster                                                             |
| xml_etree_iterparse        | 77.6 ms                                                         | 62.7 ms: 1.24x faster                                                            |
| docutils                   | 1.98 sec                                                        | 1.61 sec: 1.24x faster                                                           |
| typing_runtime_protocols   | 126 us                                                          | 103 us: 1.23x faster                                                             |
| meteor_contest             | 86.9 ms                                                         | 71.1 ms: 1.22x faster                                                            |
| unpickle                   | 9.71 us                                                         | 8.45 us: 1.15x faster                                                            |
| regex_v8                   | 15.0 ms                                                         | 13.2 ms: 1.14x faster                                                            |
| regex_dna                  | 127 ms                                                          | 114 ms: 1.12x faster                                                             |
| unpickle_list              | 2.95 us                                                         | 2.71 us: 1.08x faster                                                            |
| pickle                     | 7.79 us                                                         | 7.32 us: 1.06x faster                                                            |
| pickle_list                | 3.37 us                                                         | 3.18 us: 1.06x faster                                                            |
| pickle_dict                | 19.9 us                                                         | 19.0 us: 1.05x faster                                                            |
| coverage                   | 48.4 ms                                                         | 49.4 ms: 1.02x slower                                                            |
| python_startup             | 22.4 ms                                                         | 25.1 ms: 1.12x slower                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 88.8 ms: 1.18x slower                                                            |
| gc_traversal               | 1.44 ms                                                         | 2.14 ms: 1.48x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.27 ms: 1.95x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.55x faster                                                                     |

Benchmark hidden because not significant (1): python_startup_no_site
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20251012-3.15.0a0-d6dd64a-JIT/bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.543x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.54x
- 95% likely to have a speedup of 1.52x
- 99% likely to have a speedup of 1.49x

# Memory
- memory change: unknown