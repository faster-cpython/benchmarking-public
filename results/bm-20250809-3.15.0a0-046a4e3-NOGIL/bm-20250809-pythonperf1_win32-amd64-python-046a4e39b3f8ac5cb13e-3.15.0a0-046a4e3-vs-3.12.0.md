# Results vs. 3.12.0

- fork: python
- ref: 046a4e39b3f8ac5cb13e
- machine: windows-amd64
- commit hash: 046a4e3
- commit date: 2025-08-09
- overall geometric mean: 1.306x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 229 ms: 1.22x faster                                                             |
| docutils       | 1.98 sec                                                        | 2.92 sec: 1.47x slower                                                           |
| Geometric mean | (ref)                                                           | 1.10x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 331 ms: 2.05x faster                                                             |
| async_tree_io              | 693 ms                                                          | 354 ms: 1.96x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 147 ms: 1.89x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 190 ms: 1.85x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 313 ms: 1.74x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 210 ms: 1.73x faster                                                             |
| async_tree_none            | 298 ms                                                          | 173 ms: 1.72x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 336 ms: 1.68x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.82x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 47.1 ms: 1.63x faster                                                            |
| nbody          | 127 ms                                                          | 86.2 ms: 1.47x faster                                                            |
| pidigits       | 199 ms                                                          | 137 ms: 1.45x faster                                                             |
| Geometric mean | (ref)                                                           | 1.51x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 95.1 ms: 1.36x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.53 ms: 1.33x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 12.8 ms: 1.17x faster                                                            |
| regex_dna      | 127 ms                                                          | 112 ms: 1.13x faster                                                             |
| Geometric mean | (ref)                                                           | 1.25x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 77.6 ms                                                         | 58.3 ms: 1.33x faster                                                            |
| unpickle_pure_python | 210 us                                                          | 160 us: 1.31x faster                                                             |
| json_loads           | 20.4 us                                                         | 15.7 us: 1.30x faster                                                            |
| xml_etree_parse      | 113 ms                                                          | 90.5 ms: 1.25x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 5.96 ms: 1.24x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 235 us: 1.22x faster                                                             |
| xml_etree_process    | 53.2 ms                                                         | 44.7 ms: 1.19x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 63.0 ms: 1.15x faster                                                            |
| pickle_list          | 3.37 us                                                         | 2.98 us: 1.13x faster                                                            |
| unpickle             | 9.71 us                                                         | 10.1 us: 1.04x slower                                                            |
| unpickle_list        | 2.95 us                                                         | 3.07 us: 1.04x slower                                                            |
| tomli_loads          | 2.20 sec                                                        | 2.75 sec: 1.25x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.12x faster                                                                     |

Benchmark hidden because not significant (2): pickle_dict, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.0 ms: 1.05x slower                                                            |
| python_startup         | 22.4 ms                                                         | 27.1 ms: 1.21x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.13x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.9 ms                                                         | 27.3 ms: 1.35x faster                                                            |
| mako            | 9.96 ms                                                         | 10.1 ms: 1.01x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.16x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 2.50 sec: 7.06x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 32.7 ms: 2.80x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 331 ms: 2.05x faster                                                             |
| async_tree_io              | 693 ms                                                          | 354 ms: 1.96x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 147 ms: 1.89x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 190 ms: 1.85x faster                                                             |
| deepcopy_memo              | 38.4 us                                                         | 21.8 us: 1.76x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 313 ms: 1.74x faster                                                             |
| deepcopy                   | 360 us                                                          | 207 us: 1.74x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 210 ms: 1.73x faster                                                             |
| async_tree_none            | 298 ms                                                          | 173 ms: 1.72x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 336 ms: 1.68x faster                                                             |
| unpack_sequence            | 62.5 ns                                                         | 37.7 ns: 1.66x faster                                                            |
| generators                 | 38.5 ms                                                         | 23.3 ms: 1.65x faster                                                            |
| float                      | 76.7 ms                                                         | 47.1 ms: 1.63x faster                                                            |
| mdp                        | 1.91 sec                                                        | 1.18 sec: 1.62x faster                                                           |
| logging_silent             | 101 ns                                                          | 62.9 ns: 1.61x faster                                                            |
| comprehensions             | 19.2 us                                                         | 12.3 us: 1.56x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.40 us: 1.48x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 2.18 us: 1.48x faster                                                            |
| scimark_sor                | 130 ms                                                          | 87.7 ms: 1.48x faster                                                            |
| nbody                      | 127 ms                                                          | 86.2 ms: 1.47x faster                                                            |
| chaos                      | 69.4 ms                                                         | 47.5 ms: 1.46x faster                                                            |
| raytrace                   | 308 ms                                                          | 211 ms: 1.46x faster                                                             |
| go                         | 137 ms                                                          | 94.6 ms: 1.45x faster                                                            |
| pidigits                   | 199 ms                                                          | 137 ms: 1.45x faster                                                             |
| hexiom                     | 6.82 ms                                                         | 4.74 ms: 1.44x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 2.50 ms: 1.43x faster                                                            |
| logging_format             | 10.4 us                                                         | 7.32 us: 1.42x faster                                                            |
| logging_simple             | 9.75 us                                                         | 6.92 us: 1.41x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 67.4 ms: 1.38x faster                                                            |
| spectral_norm              | 104 ms                                                          | 75.8 ms: 1.37x faster                                                            |
| json                       | 4.15 ms                                                         | 3.04 ms: 1.37x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 42.8 ms: 1.36x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 15.4 ms: 1.36x faster                                                            |
| regex_compile              | 129 ms                                                          | 95.1 ms: 1.36x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 49.0 ms: 1.36x faster                                                            |
| django_template            | 36.9 ms                                                         | 27.3 ms: 1.35x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.53 ms: 1.33x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 58.3 ms: 1.33x faster                                                            |
| pyflate                    | 424 ms                                                          | 320 ms: 1.32x faster                                                             |
| unpickle_pure_python       | 210 us                                                          | 160 us: 1.31x faster                                                             |
| pycparser                  | 978 ms                                                          | 752 ms: 1.30x faster                                                             |
| json_loads                 | 20.4 us                                                         | 15.7 us: 1.30x faster                                                            |
| pprint_safe_repr           | 721 ms                                                          | 565 ms: 1.28x faster                                                             |
| sympy_str                  | 240 ms                                                          | 191 ms: 1.25x faster                                                             |
| xml_etree_parse            | 113 ms                                                          | 90.5 ms: 1.25x faster                                                            |
| scimark_fft                | 271 ms                                                          | 217 ms: 1.25x faster                                                             |
| json_dumps                 | 7.40 ms                                                         | 5.96 ms: 1.24x faster                                                            |
| sympy_sum                  | 123 ms                                                          | 99.1 ms: 1.24x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 76.0 ms: 1.23x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 14.3 ms: 1.23x faster                                                            |
| 2to3                       | 280 ms                                                          | 229 ms: 1.22x faster                                                             |
| sympy_expand               | 398 ms                                                          | 326 ms: 1.22x faster                                                             |
| pickle_pure_python         | 286 us                                                          | 235 us: 1.22x faster                                                             |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.17 ms: 1.22x faster                                                            |
| richards                   | 41.3 ms                                                         | 34.3 ms: 1.21x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 58.0 ms: 1.19x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 44.7 ms: 1.19x faster                                                            |
| async_generators           | 313 ms                                                          | 266 ms: 1.18x faster                                                             |
| regex_v8                   | 15.0 ms                                                         | 12.8 ms: 1.17x faster                                                            |
| asyncio_tcp                | 662 ms                                                          | 565 ms: 1.17x faster                                                             |
| richards_super             | 46.5 ms                                                         | 39.8 ms: 1.17x faster                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 63.0 ms: 1.15x faster                                                            |
| fannkuch                   | 354 ms                                                          | 310 ms: 1.14x faster                                                             |
| gc_traversal               | 1.44 ms                                                         | 1.26 ms: 1.14x faster                                                            |
| pickle_list                | 3.37 us                                                         | 2.98 us: 1.13x faster                                                            |
| regex_dna                  | 127 ms                                                          | 112 ms: 1.13x faster                                                             |
| telco                      | 5.51 ms                                                         | 5.29 ms: 1.04x faster                                                            |
| mako                       | 9.96 ms                                                         | 10.1 ms: 1.01x slower                                                            |
| meteor_contest             | 86.9 ms                                                         | 88.2 ms: 1.02x slower                                                            |
| unpickle                   | 9.71 us                                                         | 10.1 us: 1.04x slower                                                            |
| unpickle_list              | 2.95 us                                                         | 3.07 us: 1.04x slower                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 20.0 ms: 1.05x slower                                                            |
| typing_runtime_protocols   | 126 us                                                          | 132 us: 1.05x slower                                                             |
| bench_mp_pool              | 75.4 ms                                                         | 80.9 ms: 1.07x slower                                                            |
| pprint_pformat             | 1.50 sec                                                        | 1.76 sec: 1.18x slower                                                           |
| python_startup             | 22.4 ms                                                         | 27.1 ms: 1.21x slower                                                            |
| tomli_loads                | 2.20 sec                                                        | 2.75 sec: 1.25x slower                                                           |
| coverage                   | 48.4 ms                                                         | 69.4 ms: 1.43x slower                                                            |
| docutils                   | 1.98 sec                                                        | 2.92 sec: 1.47x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.06 ms: 1.62x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.31x faster                                                                     |

Benchmark hidden because not significant (3): pickle_dict, bench_thread_pool, pickle
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250809-3.15.0a0-046a4e3-NOGIL/bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.306x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: unknown