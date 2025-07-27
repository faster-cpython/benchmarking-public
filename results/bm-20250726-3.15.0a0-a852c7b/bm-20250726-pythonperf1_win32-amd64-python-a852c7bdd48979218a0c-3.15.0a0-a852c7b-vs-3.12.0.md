# Results vs. 3.12.0

- fork: python
- ref: a852c7bdd48979218a0c
- machine: windows-amd64
- commit hash: a852c7b
- commit date: 2025-07-26
- overall geometric mean: 1.425x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.40x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 227 ms: 1.23x faster                                                             |
| docutils       | 1.98 sec                                                        | 1.64 sec: 1.21x faster                                                           |
| Geometric mean | (ref)                                                           | 1.22x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io              | 693 ms                                                          | 394 ms: 1.76x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 393 ms: 1.72x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 213 ms: 1.71x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 338 ms: 1.67x faster                                                             |
| async_tree_none            | 298 ms                                                          | 179 ms: 1.66x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 221 ms: 1.58x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 349 ms: 1.57x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 178 ms: 1.56x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.65x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 67.9 ms: 1.87x faster                                                            |
| float          | 76.7 ms                                                         | 44.9 ms: 1.71x faster                                                            |
| pidigits       | 199 ms                                                          | 150 ms: 1.33x faster                                                             |
| Geometric mean | (ref)                                                           | 1.62x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 81.5 ms: 1.58x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.55 ms: 1.32x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 14.6 ms: 1.03x faster                                                            |
| Geometric mean | (ref)                                                           | 1.21x faster                                                                     |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 136 us: 1.54x faster                                                             |
| tomli_loads          | 2.20 sec                                                        | 1.44 sec: 1.52x faster                                                           |
| json_loads           | 20.4 us                                                         | 15.0 us: 1.36x faster                                                            |
| xml_etree_process    | 53.2 ms                                                         | 40.2 ms: 1.32x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 223 us: 1.28x faster                                                             |
| xml_etree_parse      | 113 ms                                                          | 89.6 ms: 1.26x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 57.8 ms: 1.25x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 66.7 ms: 1.16x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 6.52 ms: 1.13x faster                                                            |
| unpickle             | 9.71 us                                                         | 8.80 us: 1.10x faster                                                            |
| pickle_dict          | 19.9 us                                                         | 20.3 us: 1.02x slower                                                            |
| pickle               | 7.79 us                                                         | 8.31 us: 1.07x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.19x faster                                                                     |

Benchmark hidden because not significant (2): unpickle_list, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.1 ms: 1.05x slower                                                            |
| python_startup         | 22.4 ms                                                         | 26.6 ms: 1.19x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.12x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 6.84 ms: 1.46x faster                                                            |
| django_template | 36.9 ms                                                         | 25.4 ms: 1.45x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.45x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 1.31 sec: 13.51x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 33.5 ms: 2.73x faster                                                            |
| mdp                        | 1.91 sec                                                        | 819 ms: 2.33x faster                                                             |
| deepcopy                   | 360 us                                                          | 173 us: 2.08x faster                                                             |
| deepcopy_memo              | 38.4 us                                                         | 19.0 us: 2.02x faster                                                            |
| generators                 | 38.5 ms                                                         | 19.7 ms: 1.95x faster                                                            |
| nbody                      | 127 ms                                                          | 67.9 ms: 1.87x faster                                                            |
| go                         | 137 ms                                                          | 77.6 ms: 1.77x faster                                                            |
| async_tree_io              | 693 ms                                                          | 394 ms: 1.76x faster                                                             |
| logging_silent             | 101 ns                                                          | 57.9 ns: 1.74x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 1.87 us: 1.73x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 393 ms: 1.72x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 213 ms: 1.71x faster                                                             |
| float                      | 76.7 ms                                                         | 44.9 ms: 1.71x faster                                                            |
| raytrace                   | 308 ms                                                          | 181 ms: 1.70x faster                                                             |
| asyncio_tcp                | 662 ms                                                          | 396 ms: 1.67x faster                                                             |
| comprehensions             | 19.2 us                                                         | 11.5 us: 1.67x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 338 ms: 1.67x faster                                                             |
| async_tree_none            | 298 ms                                                          | 179 ms: 1.66x faster                                                             |
| unpack_sequence            | 62.5 ns                                                         | 37.6 ns: 1.66x faster                                                            |
| scimark_sor                | 130 ms                                                          | 78.6 ms: 1.65x faster                                                            |
| hexiom                     | 6.82 ms                                                         | 4.13 ms: 1.65x faster                                                            |
| spectral_norm              | 104 ms                                                          | 63.9 ms: 1.62x faster                                                            |
| chaos                      | 69.4 ms                                                         | 42.7 ms: 1.62x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 41.2 ms: 1.61x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 221 ms: 1.58x faster                                                             |
| regex_compile              | 129 ms                                                          | 81.5 ms: 1.58x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 2.29 ms: 1.57x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 349 ms: 1.57x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 178 ms: 1.56x faster                                                             |
| logging_simple             | 9.75 us                                                         | 6.27 us: 1.56x faster                                                            |
| unpickle_pure_python       | 210 us                                                          | 136 us: 1.54x faster                                                             |
| logging_format             | 10.4 us                                                         | 6.79 us: 1.53x faster                                                            |
| tomli_loads                | 2.20 sec                                                        | 1.44 sec: 1.52x faster                                                           |
| richards                   | 41.3 ms                                                         | 27.8 ms: 1.49x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.59 ms: 1.49x faster                                                            |
| pprint_pformat             | 1.50 sec                                                        | 1.01 sec: 1.48x faster                                                           |
| pyflate                    | 424 ms                                                          | 286 ms: 1.48x faster                                                             |
| scimark_lu                 | 93.2 ms                                                         | 63.2 ms: 1.47x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 63.8 ms: 1.47x faster                                                            |
| richards_super             | 46.5 ms                                                         | 31.8 ms: 1.46x faster                                                            |
| mako                       | 9.96 ms                                                         | 6.84 ms: 1.46x faster                                                            |
| django_template            | 36.9 ms                                                         | 25.4 ms: 1.45x faster                                                            |
| pprint_safe_repr           | 721 ms                                                          | 496 ms: 1.45x faster                                                             |
| crypto_pyaes               | 69.2 ms                                                         | 47.8 ms: 1.45x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 40.8 ms: 1.43x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 14.6 ms: 1.43x faster                                                            |
| scimark_fft                | 271 ms                                                          | 190 ms: 1.43x faster                                                             |
| sympy_sum                  | 123 ms                                                          | 87.9 ms: 1.40x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 12.6 ms: 1.39x faster                                                            |
| sympy_expand               | 398 ms                                                          | 287 ms: 1.39x faster                                                             |
| sympy_str                  | 240 ms                                                          | 173 ms: 1.38x faster                                                             |
| pycparser                  | 978 ms                                                          | 717 ms: 1.36x faster                                                             |
| json_loads                 | 20.4 us                                                         | 15.0 us: 1.36x faster                                                            |
| fannkuch                   | 354 ms                                                          | 261 ms: 1.35x faster                                                             |
| json                       | 4.15 ms                                                         | 3.07 ms: 1.35x faster                                                            |
| pidigits                   | 199 ms                                                          | 150 ms: 1.33x faster                                                             |
| xml_etree_process          | 53.2 ms                                                         | 40.2 ms: 1.32x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.55 ms: 1.32x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.58 us: 1.31x faster                                                            |
| async_generators           | 313 ms                                                          | 241 ms: 1.30x faster                                                             |
| pickle_pure_python         | 286 us                                                          | 223 us: 1.28x faster                                                             |
| bench_thread_pool          | 1.10 ms                                                         | 861 us: 1.28x faster                                                             |
| xml_etree_parse            | 113 ms                                                          | 89.6 ms: 1.26x faster                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 57.8 ms: 1.25x faster                                                            |
| 2to3                       | 280 ms                                                          | 227 ms: 1.23x faster                                                             |
| typing_runtime_protocols   | 126 us                                                          | 104 us: 1.22x faster                                                             |
| docutils                   | 1.98 sec                                                        | 1.64 sec: 1.21x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 66.7 ms: 1.16x faster                                                            |
| telco                      | 5.51 ms                                                         | 4.78 ms: 1.15x faster                                                            |
| meteor_contest             | 86.9 ms                                                         | 75.5 ms: 1.15x faster                                                            |
| json_dumps                 | 7.40 ms                                                         | 6.52 ms: 1.13x faster                                                            |
| unpickle                   | 9.71 us                                                         | 8.80 us: 1.10x faster                                                            |
| regex_v8                   | 15.0 ms                                                         | 14.6 ms: 1.03x faster                                                            |
| pickle_dict                | 19.9 us                                                         | 20.3 us: 1.02x slower                                                            |
| coverage                   | 48.4 ms                                                         | 50.5 ms: 1.04x slower                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 20.1 ms: 1.05x slower                                                            |
| pickle                     | 7.79 us                                                         | 8.31 us: 1.07x slower                                                            |
| python_startup             | 22.4 ms                                                         | 26.6 ms: 1.19x slower                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 96.1 ms: 1.27x slower                                                            |
| gc_traversal               | 1.44 ms                                                         | 2.20 ms: 1.53x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.32 ms: 2.03x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.43x faster                                                                     |

Benchmark hidden because not significant (3): regex_dna, unpickle_list, pickle_list
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.425x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.44x
- 95% likely to have a speedup of 1.43x
- 99% likely to have a speedup of 1.40x

# Memory
- memory change: unknown