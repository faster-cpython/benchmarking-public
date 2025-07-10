# Results vs. 3.12.0

- fork: python
- ref: c419af9e277bea7dd78f
- machine: windows-amd64
- commit hash: c419af9
- commit date: 2025-06-28
- overall geometric mean: 1.501x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.45x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf1_win32-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 219 ms: 1.28x faster                                                             |
| docutils       | 1.98 sec                                                        | 1.65 sec: 1.20x faster                                                           |
| Geometric mean | (ref)                                                           | 1.24x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf1_win32-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization     | 364 ms                                                          | 204 ms: 1.78x faster                                                             |
| async_tree_io              | 693 ms                                                          | 390 ms: 1.77x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 383 ms: 1.77x faster                                                             |
| async_tree_none            | 298 ms                                                          | 170 ms: 1.75x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 331 ms: 1.70x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 166 ms: 1.67x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 210 ms: 1.67x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 341 ms: 1.60x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.71x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf1_win32-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 53.3 ms: 2.38x faster                                                            |
| float          | 76.7 ms                                                         | 44.5 ms: 1.72x faster                                                            |
| pidigits       | 199 ms                                                          | 146 ms: 1.36x faster                                                             |
| Geometric mean | (ref)                                                           | 1.77x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf1_win32-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 78.9 ms: 1.64x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.57 ms: 1.29x faster                                                            |
| regex_dna      | 127 ms                                                          | 120 ms: 1.06x faster                                                             |
| regex_v8       | 15.0 ms                                                         | 14.4 ms: 1.04x faster                                                            |
| Geometric mean | (ref)                                                           | 1.24x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf1_win32-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.12 sec: 1.96x faster                                                           |
| unpickle_pure_python | 210 us                                                          | 109 us: 1.92x faster                                                             |
| xml_etree_process    | 53.2 ms                                                         | 35.7 ms: 1.49x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 50.9 ms: 1.42x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 203 us: 1.41x faster                                                             |
| json_loads           | 20.4 us                                                         | 14.6 us: 1.40x faster                                                            |
| xml_etree_parse      | 113 ms                                                          | 87.1 ms: 1.30x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 62.4 ms: 1.24x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 6.15 ms: 1.20x faster                                                            |
| Geometric mean       | (ref)                                                           | 1.46x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf1_win32-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup | 22.4 ms                                                         | 25.4 ms: 1.14x slower                                                            |
| Geometric mean | (ref)                                                           | 1.07x slower                                                                     |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf1_win32-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.45 ms: 1.83x faster                                                            |
| django_template | 36.9 ms                                                         | 24.2 ms: 1.53x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.67x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf1_win32-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pathlib                    | 91.4 ms                                                         | 28.7 ms: 3.18x faster                                                            |
| nbody                      | 127 ms                                                          | 53.3 ms: 2.38x faster                                                            |
| mdp                        | 1.91 sec                                                        | 810 ms: 2.36x faster                                                             |
| deepcopy_memo              | 38.4 us                                                         | 17.5 us: 2.20x faster                                                            |
| deepcopy                   | 360 us                                                          | 169 us: 2.13x faster                                                             |
| generators                 | 38.5 ms                                                         | 19.4 ms: 1.98x faster                                                            |
| tomli_loads                | 2.20 sec                                                        | 1.12 sec: 1.96x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 109 us: 1.92x faster                                                             |
| logging_silent             | 101 ns                                                          | 54.3 ns: 1.86x faster                                                            |
| mako                       | 9.96 ms                                                         | 5.45 ms: 1.83x faster                                                            |
| go                         | 137 ms                                                          | 75.9 ms: 1.81x faster                                                            |
| scimark_fft                | 271 ms                                                          | 150 ms: 1.80x faster                                                             |
| comprehensions             | 19.2 us                                                         | 10.7 us: 1.79x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 204 ms: 1.78x faster                                                             |
| async_tree_io              | 693 ms                                                          | 390 ms: 1.77x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 383 ms: 1.77x faster                                                             |
| async_tree_none            | 298 ms                                                          | 170 ms: 1.75x faster                                                             |
| deepcopy_reduce            | 3.23 us                                                         | 1.85 us: 1.74x faster                                                            |
| float                      | 76.7 ms                                                         | 44.5 ms: 1.72x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.26 ms: 1.71x faster                                                            |
| raytrace                   | 308 ms                                                          | 181 ms: 1.70x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 331 ms: 1.70x faster                                                             |
| chaos                      | 69.4 ms                                                         | 40.9 ms: 1.70x faster                                                            |
| scimark_sor                | 130 ms                                                          | 76.6 ms: 1.70x faster                                                            |
| pyflate                    | 424 ms                                                          | 253 ms: 1.67x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 166 ms: 1.67x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 210 ms: 1.67x faster                                                             |
| hexiom                     | 6.82 ms                                                         | 4.11 ms: 1.66x faster                                                            |
| regex_compile              | 129 ms                                                          | 78.9 ms: 1.64x faster                                                            |
| pprint_pformat             | 1.50 sec                                                        | 922 ms: 1.63x faster                                                             |
| deltablue                  | 3.58 ms                                                         | 2.21 ms: 1.62x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 41.5 ms: 1.60x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 341 ms: 1.60x faster                                                             |
| pprint_safe_repr           | 721 ms                                                          | 450 ms: 1.60x faster                                                             |
| spectral_norm              | 104 ms                                                          | 64.9 ms: 1.60x faster                                                            |
| logging_simple             | 9.75 us                                                         | 6.18 us: 1.58x faster                                                            |
| fannkuch                   | 354 ms                                                          | 224 ms: 1.58x faster                                                             |
| logging_format             | 10.4 us                                                         | 6.64 us: 1.57x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 59.5 ms: 1.57x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 59.9 ms: 1.56x faster                                                            |
| richards                   | 41.3 ms                                                         | 26.7 ms: 1.55x faster                                                            |
| django_template            | 36.9 ms                                                         | 24.2 ms: 1.53x faster                                                            |
| richards_super             | 46.5 ms                                                         | 30.6 ms: 1.52x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 45.7 ms: 1.52x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 35.7 ms: 1.49x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 14.2 ms: 1.47x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 40.7 ms: 1.44x faster                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 50.9 ms: 1.42x faster                                                            |
| sympy_str                  | 240 ms                                                          | 170 ms: 1.41x faster                                                             |
| pickle_pure_python         | 286 us                                                          | 203 us: 1.41x faster                                                             |
| pycparser                  | 978 ms                                                          | 697 ms: 1.40x faster                                                             |
| sympy_sum                  | 123 ms                                                          | 87.7 ms: 1.40x faster                                                            |
| json_loads                 | 20.4 us                                                         | 14.6 us: 1.40x faster                                                            |
| json                       | 4.15 ms                                                         | 3.02 ms: 1.37x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 12.8 ms: 1.37x faster                                                            |
| pidigits                   | 199 ms                                                          | 146 ms: 1.36x faster                                                             |
| sympy_expand               | 398 ms                                                          | 293 ms: 1.36x faster                                                             |
| sqlite_synth               | 2.07 us                                                         | 1.56 us: 1.32x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 87.1 ms: 1.30x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.57 ms: 1.29x faster                                                            |
| 2to3                       | 280 ms                                                          | 219 ms: 1.28x faster                                                             |
| telco                      | 5.51 ms                                                         | 4.32 ms: 1.27x faster                                                            |
| async_generators           | 313 ms                                                          | 250 ms: 1.25x faster                                                             |
| xml_etree_iterparse        | 77.6 ms                                                         | 62.4 ms: 1.24x faster                                                            |
| meteor_contest             | 86.9 ms                                                         | 70.3 ms: 1.24x faster                                                            |
| typing_runtime_protocols   | 126 us                                                          | 104 us: 1.21x faster                                                             |
| docutils                   | 1.98 sec                                                        | 1.65 sec: 1.20x faster                                                           |
| json_dumps                 | 7.40 ms                                                         | 6.15 ms: 1.20x faster                                                            |
| regex_dna                  | 127 ms                                                          | 120 ms: 1.06x faster                                                             |
| regex_v8                   | 15.0 ms                                                         | 14.4 ms: 1.04x faster                                                            |
| coverage                   | 48.4 ms                                                         | 49.6 ms: 1.02x slower                                                            |
| python_startup             | 22.4 ms                                                         | 25.4 ms: 1.14x slower                                                            |
| gc_traversal               | 1.44 ms                                                         | 2.11 ms: 1.46x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.32 ms: 2.03x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.50x faster                                                                     |

Benchmark hidden because not significant (1): python_startup_no_site
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250628-3.15.0a0-c419af9-JIT/bm-20250628-pythonperf1_win32-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.501x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.52x
- 95% likely to have a speedup of 1.49x
- 99% likely to have a speedup of 1.45x

# Memory
- memory change: unknown