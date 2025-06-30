# Results vs. 3.12.0

- fork: python
- ref: 75f40595e555e7d016cf
- machine: windows-amd64
- commit hash: 75f4059
- commit date: 2025-06-30
- overall geometric mean: 1.466x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.41x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 220 ms: 1.27x faster                                                             |
| docutils       | 1.98 sec                                                        | 1.60 sec: 1.24x faster                                                           |
| Geometric mean | (ref)                                                           | 1.25x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_none            | 298 ms                                                          | 170 ms: 1.75x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 208 ms: 1.75x faster                                                             |
| async_tree_io              | 693 ms                                                          | 397 ms: 1.74x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 393 ms: 1.72x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 328 ms: 1.72x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 212 ms: 1.65x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 170 ms: 1.64x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 340 ms: 1.61x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.70x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 63.0 ms: 2.02x faster                                                            |
| float          | 76.7 ms                                                         | 43.1 ms: 1.78x faster                                                            |
| pidigits       | 199 ms                                                          | 146 ms: 1.36x faster                                                             |
| Geometric mean | (ref)                                                           | 1.70x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 79.4 ms: 1.63x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.50 ms: 1.36x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 13.3 ms: 1.13x faster                                                            |
| regex_dna      | 127 ms                                                          | 115 ms: 1.10x faster                                                             |
| Geometric mean | (ref)                                                           | 1.29x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.38 sec: 1.60x faster                                                           |
| unpickle_pure_python | 210 us                                                          | 135 us: 1.56x faster                                                             |
| json_loads           | 20.4 us                                                         | 14.3 us: 1.42x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 208 us: 1.38x faster                                                             |
| xml_etree_process    | 53.2 ms                                                         | 39.1 ms: 1.36x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 56.1 ms: 1.29x faster                                                            |
| xml_etree_parse      | 113 ms                                                          | 89.2 ms: 1.27x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 6.19 ms: 1.20x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 66.3 ms: 1.17x faster                                                            |
| unpickle             | 9.71 us                                                         | 8.57 us: 1.13x faster                                                            |
| unpickle_list        | 2.95 us                                                         | 2.78 us: 1.06x faster                                                            |
| pickle_dict          | 19.9 us                                                         | 19.7 us: 1.01x faster                                                            |
| pickle_list          | 3.37 us                                                         | 3.40 us: 1.01x slower                                                            |
| pickle               | 7.79 us                                                         | 7.96 us: 1.02x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.23x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.4 ms: 1.02x slower                                                            |
| python_startup         | 22.4 ms                                                         | 25.7 ms: 1.15x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.9 ms                                                         | 24.3 ms: 1.52x faster                                                            |
| mako            | 9.96 ms                                                         | 6.55 ms: 1.52x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.52x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 1.33 sec: 13.31x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 31.7 ms: 2.88x faster                                                            |
| mdp                        | 1.91 sec                                                        | 801 ms: 2.39x faster                                                             |
| deepcopy_memo              | 38.4 us                                                         | 17.6 us: 2.19x faster                                                            |
| deepcopy                   | 360 us                                                          | 168 us: 2.14x faster                                                             |
| nbody                      | 127 ms                                                          | 63.0 ms: 2.02x faster                                                            |
| generators                 | 38.5 ms                                                         | 19.4 ms: 1.98x faster                                                            |
| logging_silent             | 101 ns                                                          | 55.2 ns: 1.83x faster                                                            |
| go                         | 137 ms                                                          | 75.5 ms: 1.82x faster                                                            |
| float                      | 76.7 ms                                                         | 43.1 ms: 1.78x faster                                                            |
| comprehensions             | 19.2 us                                                         | 10.9 us: 1.76x faster                                                            |
| scimark_sor                | 130 ms                                                          | 74.0 ms: 1.76x faster                                                            |
| async_tree_none            | 298 ms                                                          | 170 ms: 1.75x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 208 ms: 1.75x faster                                                             |
| deepcopy_reduce            | 3.23 us                                                         | 1.84 us: 1.75x faster                                                            |
| async_tree_io              | 693 ms                                                          | 397 ms: 1.74x faster                                                             |
| unpack_sequence            | 62.5 ns                                                         | 36.2 ns: 1.72x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 393 ms: 1.72x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 328 ms: 1.72x faster                                                             |
| chaos                      | 69.4 ms                                                         | 40.6 ms: 1.71x faster                                                            |
| raytrace                   | 308 ms                                                          | 180 ms: 1.71x faster                                                             |
| hexiom                     | 6.82 ms                                                         | 4.03 ms: 1.69x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 2.15 ms: 1.67x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 40.1 ms: 1.66x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 212 ms: 1.65x faster                                                             |
| scimark_lu                 | 93.2 ms                                                         | 56.6 ms: 1.65x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 170 ms: 1.64x faster                                                             |
| logging_simple             | 9.75 us                                                         | 5.99 us: 1.63x faster                                                            |
| regex_compile              | 129 ms                                                          | 79.4 ms: 1.63x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 340 ms: 1.61x faster                                                             |
| spectral_norm              | 104 ms                                                          | 64.7 ms: 1.61x faster                                                            |
| logging_format             | 10.4 us                                                         | 6.49 us: 1.60x faster                                                            |
| tomli_loads                | 2.20 sec                                                        | 1.38 sec: 1.60x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 135 us: 1.56x faster                                                             |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.49 ms: 1.55x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 60.5 ms: 1.55x faster                                                            |
| scimark_fft                | 271 ms                                                          | 176 ms: 1.54x faster                                                             |
| richards                   | 41.3 ms                                                         | 27.0 ms: 1.53x faster                                                            |
| asyncio_tcp                | 662 ms                                                          | 433 ms: 1.53x faster                                                             |
| django_template            | 36.9 ms                                                         | 24.3 ms: 1.52x faster                                                            |
| richards_super             | 46.5 ms                                                         | 30.6 ms: 1.52x faster                                                            |
| mako                       | 9.96 ms                                                         | 6.55 ms: 1.52x faster                                                            |
| pyflate                    | 424 ms                                                          | 285 ms: 1.49x faster                                                             |
| pprint_pformat             | 1.50 sec                                                        | 1.01 sec: 1.48x faster                                                           |
| pprint_safe_repr           | 721 ms                                                          | 490 ms: 1.47x faster                                                             |
| crypto_pyaes               | 69.2 ms                                                         | 47.8 ms: 1.45x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 14.4 ms: 1.45x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 40.9 ms: 1.43x faster                                                            |
| json_loads                 | 20.4 us                                                         | 14.3 us: 1.42x faster                                                            |
| sympy_str                  | 240 ms                                                          | 170 ms: 1.41x faster                                                             |
| sympy_integrate            | 17.5 ms                                                         | 12.4 ms: 1.41x faster                                                            |
| sympy_sum                  | 123 ms                                                          | 87.3 ms: 1.41x faster                                                            |
| pycparser                  | 978 ms                                                          | 699 ms: 1.40x faster                                                             |
| fannkuch                   | 354 ms                                                          | 255 ms: 1.39x faster                                                             |
| sympy_expand               | 398 ms                                                          | 287 ms: 1.39x faster                                                             |
| pickle_pure_python         | 286 us                                                          | 208 us: 1.38x faster                                                             |
| json                       | 4.15 ms                                                         | 3.03 ms: 1.37x faster                                                            |
| pidigits                   | 199 ms                                                          | 146 ms: 1.36x faster                                                             |
| async_generators           | 313 ms                                                          | 230 ms: 1.36x faster                                                             |
| xml_etree_process          | 53.2 ms                                                         | 39.1 ms: 1.36x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.50 ms: 1.36x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 843 us: 1.31x faster                                                             |
| sqlite_synth               | 2.07 us                                                         | 1.59 us: 1.30x faster                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 56.1 ms: 1.29x faster                                                            |
| 2to3                       | 280 ms                                                          | 220 ms: 1.27x faster                                                             |
| xml_etree_parse            | 113 ms                                                          | 89.2 ms: 1.27x faster                                                            |
| typing_runtime_protocols   | 126 us                                                          | 101 us: 1.25x faster                                                             |
| docutils                   | 1.98 sec                                                        | 1.60 sec: 1.24x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 71.8 ms: 1.21x faster                                                            |
| telco                      | 5.51 ms                                                         | 4.60 ms: 1.20x faster                                                            |
| json_dumps                 | 7.40 ms                                                         | 6.19 ms: 1.20x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 66.3 ms: 1.17x faster                                                            |
| unpickle                   | 9.71 us                                                         | 8.57 us: 1.13x faster                                                            |
| regex_v8                   | 15.0 ms                                                         | 13.3 ms: 1.13x faster                                                            |
| regex_dna                  | 127 ms                                                          | 115 ms: 1.10x faster                                                             |
| unpickle_list              | 2.95 us                                                         | 2.78 us: 1.06x faster                                                            |
| coverage                   | 48.4 ms                                                         | 47.6 ms: 1.02x faster                                                            |
| pickle_dict                | 19.9 us                                                         | 19.7 us: 1.01x faster                                                            |
| pickle_list                | 3.37 us                                                         | 3.40 us: 1.01x slower                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 19.4 ms: 1.02x slower                                                            |
| pickle                     | 7.79 us                                                         | 7.96 us: 1.02x slower                                                            |
| python_startup             | 22.4 ms                                                         | 25.7 ms: 1.15x slower                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 95.7 ms: 1.27x slower                                                            |
| gc_traversal               | 1.44 ms                                                         | 2.14 ms: 1.49x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.33 ms: 2.04x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.47x faster                                                                     |
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250630-3.15.0a0-75f4059/bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.466x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.46x
- 95% likely to have a speedup of 1.45x
- 99% likely to have a speedup of 1.41x

# Memory
- memory change: unknown