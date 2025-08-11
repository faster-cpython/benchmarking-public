# Results vs. 3.12.0

- fork: python
- ref: 046a4e39b3f8ac5cb13e
- machine: windows-amd64
- commit hash: 046a4e3
- commit date: 2025-08-09
- overall geometric mean: 1.497x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.44x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 224 ms: 1.25x faster                                                             |
| docutils       | 1.98 sec                                                        | 1.66 sec: 1.20x faster                                                           |
| Geometric mean | (ref)                                                           | 1.22x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization     | 364 ms                                                          | 205 ms: 1.77x faster                                                             |
| async_tree_io              | 693 ms                                                          | 393 ms: 1.76x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 385 ms: 1.76x faster                                                             |
| async_tree_none            | 298 ms                                                          | 174 ms: 1.71x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 330 ms: 1.71x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 167 ms: 1.66x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 211 ms: 1.66x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 340 ms: 1.60x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.70x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 54.9 ms: 2.31x faster                                                            |
| float          | 76.7 ms                                                         | 43.3 ms: 1.77x faster                                                            |
| pidigits       | 199 ms                                                          | 146 ms: 1.37x faster                                                             |
| Geometric mean | (ref)                                                           | 1.78x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 78.9 ms: 1.64x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.55 ms: 1.31x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 14.0 ms: 1.08x faster                                                            |
| regex_dna      | 127 ms                                                          | 119 ms: 1.06x faster                                                             |
| Geometric mean | (ref)                                                           | 1.25x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.10 sec: 1.99x faster                                                           |
| unpickle_pure_python | 210 us                                                          | 105 us: 1.99x faster                                                             |
| xml_etree_process    | 53.2 ms                                                         | 35.7 ms: 1.49x faster                                                            |
| json_loads           | 20.4 us                                                         | 14.3 us: 1.42x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 51.2 ms: 1.41x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 204 us: 1.40x faster                                                             |
| json_dumps           | 7.40 ms                                                         | 5.45 ms: 1.36x faster                                                            |
| xml_etree_parse      | 113 ms                                                          | 88.0 ms: 1.29x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 63.2 ms: 1.23x faster                                                            |
| unpickle             | 9.71 us                                                         | 8.60 us: 1.13x faster                                                            |
| unpickle_list        | 2.95 us                                                         | 2.77 us: 1.06x faster                                                            |
| pickle_dict          | 19.9 us                                                         | 19.4 us: 1.03x faster                                                            |
| pickle               | 7.79 us                                                         | 7.67 us: 1.02x faster                                                            |
| Geometric mean       | (ref)                                                           | 1.31x faster                                                                     |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.0 ms: 1.05x slower                                                            |
| python_startup         | 22.4 ms                                                         | 26.5 ms: 1.18x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.11x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.28 ms: 1.89x faster                                                            |
| django_template | 36.9 ms                                                         | 24.2 ms: 1.52x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.69x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 1.44 sec: 12.25x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 32.2 ms: 2.84x faster                                                            |
| mdp                        | 1.91 sec                                                        | 807 ms: 2.37x faster                                                             |
| nbody                      | 127 ms                                                          | 54.9 ms: 2.31x faster                                                            |
| deepcopy_memo              | 38.4 us                                                         | 18.3 us: 2.10x faster                                                            |
| deepcopy                   | 360 us                                                          | 174 us: 2.07x faster                                                             |
| tomli_loads                | 2.20 sec                                                        | 1.10 sec: 1.99x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 105 us: 1.99x faster                                                             |
| generators                 | 38.5 ms                                                         | 19.7 ms: 1.96x faster                                                            |
| mako                       | 9.96 ms                                                         | 5.28 ms: 1.89x faster                                                            |
| unpack_sequence            | 62.5 ns                                                         | 33.2 ns: 1.88x faster                                                            |
| scimark_fft                | 271 ms                                                          | 148 ms: 1.83x faster                                                             |
| comprehensions             | 19.2 us                                                         | 10.5 us: 1.82x faster                                                            |
| go                         | 137 ms                                                          | 75.6 ms: 1.82x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 205 ms: 1.77x faster                                                             |
| float                      | 76.7 ms                                                         | 43.3 ms: 1.77x faster                                                            |
| async_tree_io              | 693 ms                                                          | 393 ms: 1.76x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 385 ms: 1.76x faster                                                             |
| deepcopy_reduce            | 3.23 us                                                         | 1.84 us: 1.75x faster                                                            |
| raytrace                   | 308 ms                                                          | 178 ms: 1.73x faster                                                             |
| fannkuch                   | 354 ms                                                          | 206 ms: 1.72x faster                                                             |
| scimark_sor                | 130 ms                                                          | 75.8 ms: 1.71x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.25 ms: 1.71x faster                                                            |
| async_tree_none            | 298 ms                                                          | 174 ms: 1.71x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 330 ms: 1.71x faster                                                             |
| chaos                      | 69.4 ms                                                         | 41.0 ms: 1.69x faster                                                            |
| hexiom                     | 6.82 ms                                                         | 4.10 ms: 1.66x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 167 ms: 1.66x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 211 ms: 1.66x faster                                                             |
| scimark_monte_carlo        | 66.4 ms                                                         | 40.0 ms: 1.66x faster                                                            |
| pprint_pformat             | 1.50 sec                                                        | 907 ms: 1.65x faster                                                             |
| regex_compile              | 129 ms                                                          | 78.9 ms: 1.64x faster                                                            |
| logging_silent             | 101 ns                                                          | 61.9 ns: 1.63x faster                                                            |
| pprint_safe_repr           | 721 ms                                                          | 442 ms: 1.63x faster                                                             |
| logging_simple             | 9.75 us                                                         | 6.04 us: 1.61x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 340 ms: 1.60x faster                                                             |
| pyflate                    | 424 ms                                                          | 265 ms: 1.60x faster                                                             |
| logging_format             | 10.4 us                                                         | 6.52 us: 1.60x faster                                                            |
| spectral_norm              | 104 ms                                                          | 65.5 ms: 1.59x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 2.26 ms: 1.58x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 59.0 ms: 1.58x faster                                                            |
| richards                   | 41.3 ms                                                         | 26.4 ms: 1.56x faster                                                            |
| richards_super             | 46.5 ms                                                         | 30.2 ms: 1.54x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 61.3 ms: 1.53x faster                                                            |
| django_template            | 36.9 ms                                                         | 24.2 ms: 1.52x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 46.4 ms: 1.49x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 35.7 ms: 1.49x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 40.9 ms: 1.43x faster                                                            |
| json_loads                 | 20.4 us                                                         | 14.3 us: 1.42x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 14.7 ms: 1.42x faster                                                            |
| pycparser                  | 978 ms                                                          | 690 ms: 1.42x faster                                                             |
| sympy_str                  | 240 ms                                                          | 169 ms: 1.42x faster                                                             |
| sympy_sum                  | 123 ms                                                          | 87.0 ms: 1.41x faster                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 51.2 ms: 1.41x faster                                                            |
| pickle_pure_python         | 286 us                                                          | 204 us: 1.40x faster                                                             |
| sympy_integrate            | 17.5 ms                                                         | 12.7 ms: 1.38x faster                                                            |
| sympy_expand               | 398 ms                                                          | 290 ms: 1.37x faster                                                             |
| pidigits                   | 199 ms                                                          | 146 ms: 1.37x faster                                                             |
| json_dumps                 | 7.40 ms                                                         | 5.45 ms: 1.36x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.55 us: 1.34x faster                                                            |
| json                       | 4.15 ms                                                         | 3.10 ms: 1.34x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.55 ms: 1.31x faster                                                            |
| telco                      | 5.51 ms                                                         | 4.24 ms: 1.30x faster                                                            |
| asyncio_tcp                | 662 ms                                                          | 512 ms: 1.29x faster                                                             |
| xml_etree_parse            | 113 ms                                                          | 88.0 ms: 1.29x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 864 us: 1.28x faster                                                             |
| 2to3                       | 280 ms                                                          | 224 ms: 1.25x faster                                                             |
| async_generators           | 313 ms                                                          | 251 ms: 1.25x faster                                                             |
| xml_etree_iterparse        | 77.6 ms                                                         | 63.2 ms: 1.23x faster                                                            |
| typing_runtime_protocols   | 126 us                                                          | 105 us: 1.20x faster                                                             |
| meteor_contest             | 86.9 ms                                                         | 72.4 ms: 1.20x faster                                                            |
| docutils                   | 1.98 sec                                                        | 1.66 sec: 1.20x faster                                                           |
| unpickle                   | 9.71 us                                                         | 8.60 us: 1.13x faster                                                            |
| regex_v8                   | 15.0 ms                                                         | 14.0 ms: 1.08x faster                                                            |
| regex_dna                  | 127 ms                                                          | 119 ms: 1.06x faster                                                             |
| unpickle_list              | 2.95 us                                                         | 2.77 us: 1.06x faster                                                            |
| pickle_dict                | 19.9 us                                                         | 19.4 us: 1.03x faster                                                            |
| pickle                     | 7.79 us                                                         | 7.67 us: 1.02x faster                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 20.0 ms: 1.05x slower                                                            |
| coverage                   | 48.4 ms                                                         | 51.1 ms: 1.05x slower                                                            |
| python_startup             | 22.4 ms                                                         | 26.5 ms: 1.18x slower                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 96.2 ms: 1.28x slower                                                            |
| gc_traversal               | 1.44 ms                                                         | 2.21 ms: 1.53x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.32 ms: 2.03x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.49x faster                                                                     |

Benchmark hidden because not significant (1): pickle_list
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.497x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.52x
- 95% likely to have a speedup of 1.49x
- 99% likely to have a speedup of 1.44x

# Memory
- memory change: unknown