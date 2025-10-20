# Results vs. 3.12.0

- fork: python
- ref: bedaea05987738c4c6b9
- machine: windows-amd64
- commit hash: bedaea0
- commit date: 2025-10-19
- overall geometric mean: 1.374x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 217 ms: 1.29x faster                                                              |
| docutils       | 1.98 sec                                                        | 2.80 sec: 1.41x slower                                                            |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 318 ms: 2.13x faster                                                              |
| async_tree_io              | 693 ms                                                          | 339 ms: 2.04x faster                                                              |
| async_tree_none_tg         | 278 ms                                                          | 142 ms: 1.95x faster                                                              |
| async_tree_memoization_tg  | 350 ms                                                          | 184 ms: 1.90x faster                                                              |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 306 ms: 1.79x faster                                                              |
| async_tree_none            | 298 ms                                                          | 168 ms: 1.77x faster                                                              |
| async_tree_memoization     | 364 ms                                                          | 206 ms: 1.77x faster                                                              |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 335 ms: 1.68x faster                                                              |
| Geometric mean             | (ref)                                                           | 1.87x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 45.1 ms: 1.70x faster                                                             |
| nbody          | 127 ms                                                          | 76.8 ms: 1.65x faster                                                             |
| pidigits       | 199 ms                                                          | 136 ms: 1.46x faster                                                              |
| Geometric mean | (ref)                                                           | 1.60x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 90.1 ms: 1.43x faster                                                             |
| regex_effbot   | 2.04 ms                                                         | 1.53 ms: 1.33x faster                                                             |
| regex_v8       | 15.0 ms                                                         | 12.8 ms: 1.17x faster                                                             |
| regex_dna      | 127 ms                                                          | 112 ms: 1.13x faster                                                              |
| Geometric mean | (ref)                                                           | 1.26x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 150 us: 1.40x faster                                                              |
| xml_etree_iterparse  | 77.6 ms                                                         | 58.7 ms: 1.32x faster                                                             |
| pickle_pure_python   | 286 us                                                          | 222 us: 1.29x faster                                                              |
| json_loads           | 20.4 us                                                         | 16.1 us: 1.26x faster                                                             |
| xml_etree_process    | 53.2 ms                                                         | 43.3 ms: 1.23x faster                                                             |
| xml_etree_parse      | 113 ms                                                          | 92.7 ms: 1.22x faster                                                             |
| json_dumps           | 7.40 ms                                                         | 6.16 ms: 1.20x faster                                                             |
| xml_etree_generate   | 72.1 ms                                                         | 61.3 ms: 1.18x faster                                                             |
| pickle_list          | 3.37 us                                                         | 3.11 us: 1.08x faster                                                             |
| pickle_dict          | 19.9 us                                                         | 20.3 us: 1.02x slower                                                             |
| unpickle             | 9.71 us                                                         | 9.98 us: 1.03x slower                                                             |
| pickle               | 7.79 us                                                         | 8.15 us: 1.05x slower                                                             |
| unpickle_list        | 2.95 us                                                         | 3.09 us: 1.05x slower                                                             |
| Geometric mean       | (ref)                                                           | 1.13x faster                                                                      |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.3 ms: 1.01x slower                                                             |
| python_startup         | 22.4 ms                                                         | 25.7 ms: 1.15x slower                                                             |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| django_template | 36.9 ms                                                         | 25.8 ms: 1.43x faster                                                             |
| mako            | 9.96 ms                                                         | 9.74 ms: 1.02x faster                                                             |
| Geometric mean  | (ref)                                                           | 1.21x faster                                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 2.19 sec: 8.08x faster                                                            |
| pathlib                    | 91.4 ms                                                         | 28.7 ms: 3.19x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 318 ms: 2.13x faster                                                              |
| deepcopy_memo              | 38.4 us                                                         | 18.7 us: 2.05x faster                                                             |
| async_tree_io              | 693 ms                                                          | 339 ms: 2.04x faster                                                              |
| async_tree_none_tg         | 278 ms                                                          | 142 ms: 1.95x faster                                                              |
| deepcopy                   | 360 us                                                          | 185 us: 1.95x faster                                                              |
| async_tree_memoization_tg  | 350 ms                                                          | 184 ms: 1.90x faster                                                              |
| generators                 | 38.5 ms                                                         | 20.3 ms: 1.89x faster                                                             |
| mdp                        | 1.91 sec                                                        | 1.02 sec: 1.88x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 306 ms: 1.79x faster                                                              |
| async_tree_none            | 298 ms                                                          | 168 ms: 1.77x faster                                                              |
| async_tree_memoization     | 364 ms                                                          | 206 ms: 1.77x faster                                                              |
| unpack_sequence            | 62.5 ns                                                         | 35.5 ns: 1.76x faster                                                             |
| float                      | 76.7 ms                                                         | 45.1 ms: 1.70x faster                                                             |
| comprehensions             | 19.2 us                                                         | 11.4 us: 1.68x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 335 ms: 1.68x faster                                                              |
| logging_silent             | 101 ns                                                          | 60.3 ns: 1.67x faster                                                             |
| nbody                      | 127 ms                                                          | 76.8 ms: 1.65x faster                                                             |
| deepcopy_reduce            | 3.23 us                                                         | 1.97 us: 1.63x faster                                                             |
| scimark_sor                | 130 ms                                                          | 82.0 ms: 1.58x faster                                                             |
| chaos                      | 69.4 ms                                                         | 44.4 ms: 1.56x faster                                                             |
| go                         | 137 ms                                                          | 87.9 ms: 1.56x faster                                                             |
| sqlite_synth               | 2.07 us                                                         | 1.34 us: 1.55x faster                                                             |
| deltablue                  | 3.58 ms                                                         | 2.32 ms: 1.55x faster                                                             |
| hexiom                     | 6.82 ms                                                         | 4.42 ms: 1.54x faster                                                             |
| asyncio_tcp                | 662 ms                                                          | 432 ms: 1.53x faster                                                              |
| coroutines                 | 20.9 ms                                                         | 13.6 ms: 1.53x faster                                                             |
| logging_simple             | 9.75 us                                                         | 6.44 us: 1.51x faster                                                             |
| raytrace                   | 308 ms                                                          | 204 ms: 1.51x faster                                                              |
| spectral_norm              | 104 ms                                                          | 68.8 ms: 1.51x faster                                                             |
| scimark_lu                 | 93.2 ms                                                         | 63.2 ms: 1.48x faster                                                             |
| pidigits                   | 199 ms                                                          | 136 ms: 1.46x faster                                                              |
| logging_format             | 10.4 us                                                         | 7.21 us: 1.44x faster                                                             |
| scimark_fft                | 271 ms                                                          | 188 ms: 1.44x faster                                                              |
| regex_compile              | 129 ms                                                          | 90.1 ms: 1.43x faster                                                             |
| django_template            | 36.9 ms                                                         | 25.8 ms: 1.43x faster                                                             |
| dulwich_log                | 58.5 ms                                                         | 41.3 ms: 1.42x faster                                                             |
| pycparser                  | 978 ms                                                          | 691 ms: 1.41x faster                                                              |
| unpickle_pure_python       | 210 us                                                          | 150 us: 1.40x faster                                                              |
| pyflate                    | 424 ms                                                          | 304 ms: 1.39x faster                                                              |
| scimark_monte_carlo        | 66.4 ms                                                         | 48.0 ms: 1.38x faster                                                             |
| regex_effbot               | 2.04 ms                                                         | 1.53 ms: 1.33x faster                                                             |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.90 ms: 1.33x faster                                                             |
| pprint_safe_repr           | 721 ms                                                          | 543 ms: 1.33x faster                                                              |
| json                       | 4.15 ms                                                         | 3.14 ms: 1.32x faster                                                             |
| xml_etree_iterparse        | 77.6 ms                                                         | 58.7 ms: 1.32x faster                                                             |
| nqueens                    | 93.7 ms                                                         | 70.9 ms: 1.32x faster                                                             |
| richards                   | 41.3 ms                                                         | 31.4 ms: 1.32x faster                                                             |
| sympy_sum                  | 123 ms                                                          | 93.4 ms: 1.32x faster                                                             |
| sympy_str                  | 240 ms                                                          | 183 ms: 1.31x faster                                                              |
| sympy_expand               | 398 ms                                                          | 307 ms: 1.30x faster                                                              |
| 2to3                       | 280 ms                                                          | 217 ms: 1.29x faster                                                              |
| sympy_integrate            | 17.5 ms                                                         | 13.6 ms: 1.29x faster                                                             |
| pickle_pure_python         | 286 us                                                          | 222 us: 1.29x faster                                                              |
| richards_super             | 46.5 ms                                                         | 36.6 ms: 1.27x faster                                                             |
| json_loads                 | 20.4 us                                                         | 16.1 us: 1.26x faster                                                             |
| crypto_pyaes               | 69.2 ms                                                         | 55.1 ms: 1.26x faster                                                             |
| xml_etree_process          | 53.2 ms                                                         | 43.3 ms: 1.23x faster                                                             |
| async_generators           | 313 ms                                                          | 256 ms: 1.22x faster                                                              |
| xml_etree_parse            | 113 ms                                                          | 92.7 ms: 1.22x faster                                                             |
| json_dumps                 | 7.40 ms                                                         | 6.16 ms: 1.20x faster                                                             |
| fannkuch                   | 354 ms                                                          | 299 ms: 1.18x faster                                                              |
| xml_etree_generate         | 72.1 ms                                                         | 61.3 ms: 1.18x faster                                                             |
| regex_v8                   | 15.0 ms                                                         | 12.8 ms: 1.17x faster                                                             |
| gc_traversal               | 1.44 ms                                                         | 1.25 ms: 1.16x faster                                                             |
| regex_dna                  | 127 ms                                                          | 112 ms: 1.13x faster                                                              |
| telco                      | 5.51 ms                                                         | 5.07 ms: 1.09x faster                                                             |
| pickle_list                | 3.37 us                                                         | 3.11 us: 1.08x faster                                                             |
| bench_thread_pool          | 1.10 ms                                                         | 1.04 ms: 1.06x faster                                                             |
| mako                       | 9.96 ms                                                         | 9.74 ms: 1.02x faster                                                             |
| bench_mp_pool              | 75.4 ms                                                         | 73.9 ms: 1.02x faster                                                             |
| meteor_contest             | 86.9 ms                                                         | 85.2 ms: 1.02x faster                                                             |
| python_startup_no_site     | 19.1 ms                                                         | 19.3 ms: 1.01x slower                                                             |
| pickle_dict                | 19.9 us                                                         | 20.3 us: 1.02x slower                                                             |
| unpickle                   | 9.71 us                                                         | 9.98 us: 1.03x slower                                                             |
| pickle                     | 7.79 us                                                         | 8.15 us: 1.05x slower                                                             |
| unpickle_list              | 2.95 us                                                         | 3.09 us: 1.05x slower                                                             |
| python_startup             | 22.4 ms                                                         | 25.7 ms: 1.15x slower                                                             |
| coverage                   | 48.4 ms                                                         | 67.2 ms: 1.39x slower                                                             |
| docutils                   | 1.98 sec                                                        | 2.80 sec: 1.41x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.01 ms: 1.56x slower                                                             |
| Geometric mean             | (ref)                                                           | 1.38x faster                                                                      |

Benchmark hidden because not significant (3): typing_runtime_protocols, tomli_loads, pprint_pformat
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20251019-3.15.0a1+-bedaea0-NOGIL/bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.374x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: unknown