# Results vs. 3.12.0

- fork: python
- ref: 2f60b8f02fe7cb83dd58
- machine: windows-amd64
- commit hash: 2f60b8f
- commit date: 2025-11-01
- overall geometric mean: 1.490x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.44x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 216 ms: 1.30x faster                                                              |
| docutils       | 1.98 sec                                                        | 1.59 sec: 1.25x faster                                                            |
| Geometric mean | (ref)                                                           | 1.27x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_io              | 693 ms                                                          | 366 ms: 1.90x faster                                                              |
| async_tree_memoization     | 364 ms                                                          | 195 ms: 1.87x faster                                                              |
| async_tree_memoization_tg  | 350 ms                                                          | 189 ms: 1.85x faster                                                              |
| async_tree_io_tg           | 677 ms                                                          | 370 ms: 1.83x faster                                                              |
| async_tree_none            | 298 ms                                                          | 167 ms: 1.78x faster                                                              |
| async_tree_none_tg         | 278 ms                                                          | 157 ms: 1.77x faster                                                              |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 322 ms: 1.75x faster                                                              |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 335 ms: 1.63x faster                                                              |
| Geometric mean             | (ref)                                                           | 1.80x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 65.6 ms: 1.94x faster                                                             |
| float          | 76.7 ms                                                         | 43.3 ms: 1.77x faster                                                             |
| pidigits       | 199 ms                                                          | 145 ms: 1.37x faster                                                              |
| Geometric mean | (ref)                                                           | 1.68x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 79.9 ms: 1.62x faster                                                             |
| regex_effbot   | 2.04 ms                                                         | 1.46 ms: 1.40x faster                                                             |
| regex_v8       | 15.0 ms                                                         | 13.7 ms: 1.10x faster                                                             |
| regex_dna      | 127 ms                                                          | 116 ms: 1.10x faster                                                              |
| Geometric mean | (ref)                                                           | 1.28x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.37 sec: 1.61x faster                                                            |
| unpickle_pure_python | 210 us                                                          | 134 us: 1.56x faster                                                              |
| json_loads           | 20.4 us                                                         | 14.0 us: 1.46x faster                                                             |
| xml_etree_process    | 53.2 ms                                                         | 38.6 ms: 1.38x faster                                                             |
| json_dumps           | 7.40 ms                                                         | 5.43 ms: 1.36x faster                                                             |
| pickle_pure_python   | 286 us                                                          | 210 us: 1.36x faster                                                              |
| xml_etree_iterparse  | 77.6 ms                                                         | 58.6 ms: 1.33x faster                                                             |
| xml_etree_parse      | 113 ms                                                          | 86.6 ms: 1.31x faster                                                             |
| xml_etree_generate   | 72.1 ms                                                         | 55.3 ms: 1.31x faster                                                             |
| unpickle             | 9.71 us                                                         | 8.28 us: 1.17x faster                                                             |
| unpickle_list        | 2.95 us                                                         | 2.78 us: 1.06x faster                                                             |
| pickle_list          | 3.37 us                                                         | 3.20 us: 1.05x faster                                                             |
| pickle_dict          | 19.9 us                                                         | 19.4 us: 1.03x faster                                                             |
| Geometric mean       | (ref)                                                           | 1.27x faster                                                                      |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.4 ms: 1.01x slower                                                             |
| python_startup         | 22.4 ms                                                         | 25.3 ms: 1.13x slower                                                             |
| Geometric mean         | (ref)                                                           | 1.07x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| django_template | 36.9 ms                                                         | 23.4 ms: 1.58x faster                                                             |
| mako            | 9.96 ms                                                         | 6.72 ms: 1.48x faster                                                             |
| Geometric mean  | (ref)                                                           | 1.53x faster                                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 1.36 sec: 13.00x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 28.3 ms: 3.23x faster                                                             |
| mdp                        | 1.91 sec                                                        | 812 ms: 2.35x faster                                                              |
| deepcopy                   | 360 us                                                          | 165 us: 2.19x faster                                                              |
| deepcopy_memo              | 38.4 us                                                         | 17.8 us: 2.15x faster                                                             |
| generators                 | 38.5 ms                                                         | 19.2 ms: 2.01x faster                                                             |
| nbody                      | 127 ms                                                          | 65.6 ms: 1.94x faster                                                             |
| unpack_sequence            | 62.5 ns                                                         | 32.6 ns: 1.91x faster                                                             |
| async_tree_io              | 693 ms                                                          | 366 ms: 1.90x faster                                                              |
| async_tree_memoization     | 364 ms                                                          | 195 ms: 1.87x faster                                                              |
| async_tree_memoization_tg  | 350 ms                                                          | 189 ms: 1.85x faster                                                              |
| async_tree_io_tg           | 677 ms                                                          | 370 ms: 1.83x faster                                                              |
| logging_silent             | 101 ns                                                          | 55.2 ns: 1.83x faster                                                             |
| deepcopy_reduce            | 3.23 us                                                         | 1.77 us: 1.82x faster                                                             |
| go                         | 137 ms                                                          | 76.6 ms: 1.79x faster                                                             |
| async_tree_none            | 298 ms                                                          | 167 ms: 1.78x faster                                                              |
| float                      | 76.7 ms                                                         | 43.3 ms: 1.77x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 157 ms: 1.77x faster                                                              |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 322 ms: 1.75x faster                                                              |
| raytrace                   | 308 ms                                                          | 178 ms: 1.73x faster                                                              |
| comprehensions             | 19.2 us                                                         | 11.2 us: 1.71x faster                                                             |
| scimark_sor                | 130 ms                                                          | 76.6 ms: 1.70x faster                                                             |
| chaos                      | 69.4 ms                                                         | 41.1 ms: 1.69x faster                                                             |
| scimark_lu                 | 93.2 ms                                                         | 56.2 ms: 1.66x faster                                                             |
| hexiom                     | 6.82 ms                                                         | 4.12 ms: 1.66x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 335 ms: 1.63x faster                                                              |
| logging_format             | 10.4 us                                                         | 6.39 us: 1.63x faster                                                             |
| logging_simple             | 9.75 us                                                         | 6.01 us: 1.62x faster                                                             |
| scimark_monte_carlo        | 66.4 ms                                                         | 41.0 ms: 1.62x faster                                                             |
| regex_compile              | 129 ms                                                          | 79.9 ms: 1.62x faster                                                             |
| deltablue                  | 3.58 ms                                                         | 2.23 ms: 1.61x faster                                                             |
| tomli_loads                | 2.20 sec                                                        | 1.37 sec: 1.61x faster                                                            |
| scimark_fft                | 271 ms                                                          | 169 ms: 1.60x faster                                                              |
| spectral_norm              | 104 ms                                                          | 65.1 ms: 1.59x faster                                                             |
| django_template            | 36.9 ms                                                         | 23.4 ms: 1.58x faster                                                             |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.47 ms: 1.56x faster                                                             |
| unpickle_pure_python       | 210 us                                                          | 134 us: 1.56x faster                                                              |
| pyflate                    | 424 ms                                                          | 283 ms: 1.50x faster                                                              |
| pprint_pformat             | 1.50 sec                                                        | 1.00 sec: 1.50x faster                                                            |
| richards                   | 41.3 ms                                                         | 27.7 ms: 1.49x faster                                                             |
| dulwich_log                | 58.5 ms                                                         | 39.3 ms: 1.49x faster                                                             |
| coroutines                 | 20.9 ms                                                         | 14.1 ms: 1.48x faster                                                             |
| mako                       | 9.96 ms                                                         | 6.72 ms: 1.48x faster                                                             |
| nqueens                    | 93.7 ms                                                         | 63.3 ms: 1.48x faster                                                             |
| richards_super             | 46.5 ms                                                         | 31.4 ms: 1.48x faster                                                             |
| json                       | 4.15 ms                                                         | 2.83 ms: 1.47x faster                                                             |
| json_loads                 | 20.4 us                                                         | 14.0 us: 1.46x faster                                                             |
| pprint_safe_repr           | 721 ms                                                          | 497 ms: 1.45x faster                                                              |
| crypto_pyaes               | 69.2 ms                                                         | 47.9 ms: 1.44x faster                                                             |
| sympy_sum                  | 123 ms                                                          | 85.3 ms: 1.44x faster                                                             |
| sympy_integrate            | 17.5 ms                                                         | 12.2 ms: 1.43x faster                                                             |
| sympy_str                  | 240 ms                                                          | 167 ms: 1.43x faster                                                              |
| pycparser                  | 978 ms                                                          | 684 ms: 1.43x faster                                                              |
| sympy_expand               | 398 ms                                                          | 283 ms: 1.41x faster                                                              |
| regex_effbot               | 2.04 ms                                                         | 1.46 ms: 1.40x faster                                                             |
| xml_etree_process          | 53.2 ms                                                         | 38.6 ms: 1.38x faster                                                             |
| pidigits                   | 199 ms                                                          | 145 ms: 1.37x faster                                                              |
| async_generators           | 313 ms                                                          | 229 ms: 1.37x faster                                                              |
| json_dumps                 | 7.40 ms                                                         | 5.43 ms: 1.36x faster                                                             |
| pickle_pure_python         | 286 us                                                          | 210 us: 1.36x faster                                                              |
| xml_etree_iterparse        | 77.6 ms                                                         | 58.6 ms: 1.33x faster                                                             |
| bench_thread_pool          | 1.10 ms                                                         | 833 us: 1.32x faster                                                              |
| fannkuch                   | 354 ms                                                          | 267 ms: 1.32x faster                                                              |
| telco                      | 5.51 ms                                                         | 4.17 ms: 1.32x faster                                                             |
| sqlite_synth               | 2.07 us                                                         | 1.57 us: 1.32x faster                                                             |
| asyncio_tcp                | 662 ms                                                          | 504 ms: 1.31x faster                                                              |
| xml_etree_parse            | 113 ms                                                          | 86.6 ms: 1.31x faster                                                             |
| xml_etree_generate         | 72.1 ms                                                         | 55.3 ms: 1.31x faster                                                             |
| 2to3                       | 280 ms                                                          | 216 ms: 1.30x faster                                                              |
| docutils                   | 1.98 sec                                                        | 1.59 sec: 1.25x faster                                                            |
| typing_runtime_protocols   | 126 us                                                          | 103 us: 1.23x faster                                                              |
| meteor_contest             | 86.9 ms                                                         | 72.0 ms: 1.21x faster                                                             |
| unpickle                   | 9.71 us                                                         | 8.28 us: 1.17x faster                                                             |
| regex_v8                   | 15.0 ms                                                         | 13.7 ms: 1.10x faster                                                             |
| regex_dna                  | 127 ms                                                          | 116 ms: 1.10x faster                                                              |
| unpickle_list              | 2.95 us                                                         | 2.78 us: 1.06x faster                                                             |
| pickle_list                | 3.37 us                                                         | 3.20 us: 1.05x faster                                                             |
| pickle_dict                | 19.9 us                                                         | 19.4 us: 1.03x faster                                                             |
| coverage                   | 48.4 ms                                                         | 48.0 ms: 1.01x faster                                                             |
| python_startup_no_site     | 19.1 ms                                                         | 19.4 ms: 1.01x slower                                                             |
| python_startup             | 22.4 ms                                                         | 25.3 ms: 1.13x slower                                                             |
| bench_mp_pool              | 75.4 ms                                                         | 88.7 ms: 1.18x slower                                                             |
| gc_traversal               | 1.44 ms                                                         | 2.05 ms: 1.43x slower                                                             |
| create_gc_cycles           | 652 us                                                          | 1.28 ms: 1.97x slower                                                             |
| Geometric mean             | (ref)                                                           | 1.49x faster                                                                      |

Benchmark hidden because not significant (1): pickle
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20251101-3.15.0a1+-2f60b8f/bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.490x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.47x
- 95% likely to have a speedup of 1.46x
- 99% likely to have a speedup of 1.44x

# Memory
- memory change: unknown