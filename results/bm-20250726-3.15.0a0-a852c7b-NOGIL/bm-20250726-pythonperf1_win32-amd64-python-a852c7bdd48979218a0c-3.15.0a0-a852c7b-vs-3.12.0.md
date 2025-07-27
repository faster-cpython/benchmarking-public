# Results vs. 3.12.0

- fork: python
- ref: a852c7bdd48979218a0c
- machine: windows-amd64
- commit hash: a852c7b
- commit date: 2025-07-26
- overall geometric mean: 1.306x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 231 ms: 1.21x faster                                                             |
| docutils       | 1.98 sec                                                        | 3.03 sec: 1.53x slower                                                           |
| Geometric mean | (ref)                                                           | 1.12x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 331 ms: 2.04x faster                                                             |
| async_tree_io              | 693 ms                                                          | 365 ms: 1.90x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 148 ms: 1.88x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 197 ms: 1.78x faster                                                             |
| async_tree_none            | 298 ms                                                          | 176 ms: 1.69x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 323 ms: 1.69x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 334 ms: 1.69x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 218 ms: 1.67x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.79x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 46.9 ms: 1.63x faster                                                            |
| nbody          | 127 ms                                                          | 83.7 ms: 1.52x faster                                                            |
| pidigits       | 199 ms                                                          | 138 ms: 1.44x faster                                                             |
| Geometric mean | (ref)                                                           | 1.53x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 95.2 ms: 1.36x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.52 ms: 1.34x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 12.9 ms: 1.17x faster                                                            |
| regex_dna      | 127 ms                                                          | 112 ms: 1.13x faster                                                             |
| Geometric mean | (ref)                                                           | 1.24x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 158 us: 1.33x faster                                                             |
| xml_etree_iterparse  | 77.6 ms                                                         | 59.9 ms: 1.30x faster                                                            |
| json_loads           | 20.4 us                                                         | 15.8 us: 1.29x faster                                                            |
| xml_etree_parse      | 113 ms                                                          | 93.4 ms: 1.21x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 237 us: 1.21x faster                                                             |
| xml_etree_process    | 53.2 ms                                                         | 44.4 ms: 1.20x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 63.2 ms: 1.14x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 6.75 ms: 1.10x faster                                                            |
| pickle_list          | 3.37 us                                                         | 3.09 us: 1.09x faster                                                            |
| pickle_dict          | 19.9 us                                                         | 20.3 us: 1.02x slower                                                            |
| pickle               | 7.79 us                                                         | 8.18 us: 1.05x slower                                                            |
| unpickle_list        | 2.95 us                                                         | 3.12 us: 1.06x slower                                                            |
| unpickle             | 9.71 us                                                         | 11.0 us: 1.14x slower                                                            |
| tomli_loads          | 2.20 sec                                                        | 2.83 sec: 1.29x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.09x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.2 ms: 1.06x slower                                                            |
| python_startup         | 22.4 ms                                                         | 27.2 ms: 1.22x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.13x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.9 ms                                                         | 27.3 ms: 1.35x faster                                                            |
| mako            | 9.96 ms                                                         | 9.64 ms: 1.03x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.18x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 2.33 sec: 7.59x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 33.9 ms: 2.70x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 331 ms: 2.04x faster                                                             |
| async_tree_io              | 693 ms                                                          | 365 ms: 1.90x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 148 ms: 1.88x faster                                                             |
| deepcopy_memo              | 38.4 us                                                         | 21.2 us: 1.81x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 197 ms: 1.78x faster                                                             |
| deepcopy                   | 360 us                                                          | 204 us: 1.76x faster                                                             |
| generators                 | 38.5 ms                                                         | 22.7 ms: 1.69x faster                                                            |
| async_tree_none            | 298 ms                                                          | 176 ms: 1.69x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 323 ms: 1.69x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 334 ms: 1.69x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 218 ms: 1.67x faster                                                             |
| float                      | 76.7 ms                                                         | 46.9 ms: 1.63x faster                                                            |
| mdp                        | 1.91 sec                                                        | 1.22 sec: 1.57x faster                                                           |
| logging_silent             | 101 ns                                                          | 64.8 ns: 1.56x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.35 us: 1.54x faster                                                            |
| comprehensions             | 19.2 us                                                         | 12.5 us: 1.53x faster                                                            |
| nbody                      | 127 ms                                                          | 83.7 ms: 1.52x faster                                                            |
| unpack_sequence            | 62.5 ns                                                         | 41.4 ns: 1.51x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 2.18 us: 1.48x faster                                                            |
| go                         | 137 ms                                                          | 93.0 ms: 1.48x faster                                                            |
| scimark_sor                | 130 ms                                                          | 88.3 ms: 1.47x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 14.3 ms: 1.46x faster                                                            |
| hexiom                     | 6.82 ms                                                         | 4.68 ms: 1.46x faster                                                            |
| chaos                      | 69.4 ms                                                         | 47.6 ms: 1.46x faster                                                            |
| pidigits                   | 199 ms                                                          | 138 ms: 1.44x faster                                                             |
| scimark_lu                 | 93.2 ms                                                         | 65.3 ms: 1.43x faster                                                            |
| logging_simple             | 9.75 us                                                         | 6.85 us: 1.42x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 2.52 ms: 1.42x faster                                                            |
| raytrace                   | 308 ms                                                          | 218 ms: 1.41x faster                                                             |
| spectral_norm              | 104 ms                                                          | 73.7 ms: 1.41x faster                                                            |
| logging_format             | 10.4 us                                                         | 7.41 us: 1.40x faster                                                            |
| asyncio_tcp                | 662 ms                                                          | 475 ms: 1.39x faster                                                             |
| regex_compile              | 129 ms                                                          | 95.2 ms: 1.36x faster                                                            |
| pyflate                    | 424 ms                                                          | 313 ms: 1.35x faster                                                             |
| django_template            | 36.9 ms                                                         | 27.3 ms: 1.35x faster                                                            |
| json                       | 4.15 ms                                                         | 3.08 ms: 1.35x faster                                                            |
| pycparser                  | 978 ms                                                          | 729 ms: 1.34x faster                                                             |
| regex_effbot               | 2.04 ms                                                         | 1.52 ms: 1.34x faster                                                            |
| unpickle_pure_python       | 210 us                                                          | 158 us: 1.33x faster                                                             |
| nqueens                    | 93.7 ms                                                         | 71.4 ms: 1.31x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 59.9 ms: 1.30x faster                                                            |
| json_loads                 | 20.4 us                                                         | 15.8 us: 1.29x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 51.5 ms: 1.29x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 45.5 ms: 1.28x faster                                                            |
| scimark_fft                | 271 ms                                                          | 211 ms: 1.28x faster                                                             |
| pprint_safe_repr           | 721 ms                                                          | 566 ms: 1.27x faster                                                             |
| sympy_str                  | 240 ms                                                          | 189 ms: 1.27x faster                                                             |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.05 ms: 1.26x faster                                                            |
| sympy_sum                  | 123 ms                                                          | 98.2 ms: 1.25x faster                                                            |
| richards                   | 41.3 ms                                                         | 33.4 ms: 1.24x faster                                                            |
| sympy_expand               | 398 ms                                                          | 326 ms: 1.22x faster                                                             |
| sympy_integrate            | 17.5 ms                                                         | 14.4 ms: 1.22x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 56.9 ms: 1.22x faster                                                            |
| 2to3                       | 280 ms                                                          | 231 ms: 1.21x faster                                                             |
| xml_etree_parse            | 113 ms                                                          | 93.4 ms: 1.21x faster                                                            |
| pickle_pure_python         | 286 us                                                          | 237 us: 1.21x faster                                                             |
| xml_etree_process          | 53.2 ms                                                         | 44.4 ms: 1.20x faster                                                            |
| richards_super             | 46.5 ms                                                         | 39.4 ms: 1.18x faster                                                            |
| gc_traversal               | 1.44 ms                                                         | 1.23 ms: 1.17x faster                                                            |
| async_generators           | 313 ms                                                          | 268 ms: 1.17x faster                                                             |
| regex_v8                   | 15.0 ms                                                         | 12.9 ms: 1.17x faster                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 63.2 ms: 1.14x faster                                                            |
| regex_dna                  | 127 ms                                                          | 112 ms: 1.13x faster                                                             |
| fannkuch                   | 354 ms                                                          | 315 ms: 1.12x faster                                                             |
| json_dumps                 | 7.40 ms                                                         | 6.75 ms: 1.10x faster                                                            |
| pickle_list                | 3.37 us                                                         | 3.09 us: 1.09x faster                                                            |
| telco                      | 5.51 ms                                                         | 5.24 ms: 1.05x faster                                                            |
| mako                       | 9.96 ms                                                         | 9.64 ms: 1.03x faster                                                            |
| pickle_dict                | 19.9 us                                                         | 20.3 us: 1.02x slower                                                            |
| pickle                     | 7.79 us                                                         | 8.18 us: 1.05x slower                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 20.2 ms: 1.06x slower                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 79.9 ms: 1.06x slower                                                            |
| unpickle_list              | 2.95 us                                                         | 3.12 us: 1.06x slower                                                            |
| typing_runtime_protocols   | 126 us                                                          | 137 us: 1.09x slower                                                             |
| unpickle                   | 9.71 us                                                         | 11.0 us: 1.14x slower                                                            |
| pprint_pformat             | 1.50 sec                                                        | 1.80 sec: 1.20x slower                                                           |
| python_startup             | 22.4 ms                                                         | 27.2 ms: 1.22x slower                                                            |
| tomli_loads                | 2.20 sec                                                        | 2.83 sec: 1.29x slower                                                           |
| coverage                   | 48.4 ms                                                         | 68.4 ms: 1.41x slower                                                            |
| docutils                   | 1.98 sec                                                        | 3.03 sec: 1.53x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.04 ms: 1.60x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.30x faster                                                                     |

Benchmark hidden because not significant (2): meteor_contest, bench_thread_pool
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.306x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: unknown