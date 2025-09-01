# Results vs. 3.12.0

- fork: python
- ref: d3d94e0ed715829d9bf9
- machine: windows-amd64
- commit hash: d3d94e0
- commit date: 2025-08-30
- overall geometric mean: 1.318x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 228 ms: 1.23x faster                                                             |
| docutils       | 1.98 sec                                                        | 2.88 sec: 1.45x slower                                                           |
| Geometric mean | (ref)                                                           | 1.09x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 330 ms: 2.05x faster                                                             |
| async_tree_io              | 693 ms                                                          | 355 ms: 1.95x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 147 ms: 1.89x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 188 ms: 1.86x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 308 ms: 1.77x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 211 ms: 1.73x faster                                                             |
| async_tree_none            | 298 ms                                                          | 173 ms: 1.72x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 334 ms: 1.69x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.83x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 45.7 ms: 1.68x faster                                                            |
| nbody          | 127 ms                                                          | 80.8 ms: 1.57x faster                                                            |
| pidigits       | 199 ms                                                          | 136 ms: 1.46x faster                                                             |
| Geometric mean | (ref)                                                           | 1.57x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 95.4 ms: 1.35x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.63 ms: 1.25x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 13.7 ms: 1.10x faster                                                            |
| regex_dna      | 127 ms                                                          | 116 ms: 1.09x faster                                                             |
| Geometric mean | (ref)                                                           | 1.19x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 163 us: 1.29x faster                                                             |
| json_loads           | 20.4 us                                                         | 16.0 us: 1.27x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 62.1 ms: 1.25x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 5.95 ms: 1.24x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 239 us: 1.20x faster                                                             |
| xml_etree_process    | 53.2 ms                                                         | 45.5 ms: 1.17x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 63.8 ms: 1.13x faster                                                            |
| pickle_list          | 3.37 us                                                         | 3.09 us: 1.09x faster                                                            |
| xml_etree_parse      | 113 ms                                                          | 105 ms: 1.07x faster                                                             |
| pickle_dict          | 19.9 us                                                         | 20.4 us: 1.02x slower                                                            |
| pickle               | 7.79 us                                                         | 8.00 us: 1.03x slower                                                            |
| unpickle             | 9.71 us                                                         | 10.2 us: 1.05x slower                                                            |
| unpickle_list        | 2.95 us                                                         | 3.12 us: 1.06x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.10x faster                                                                     |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.4 ms: 1.02x slower                                                            |
| python_startup         | 22.4 ms                                                         | 25.7 ms: 1.15x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.9 ms                                                         | 27.5 ms: 1.34x faster                                                            |
| mako            | 9.96 ms                                                         | 10.1 ms: 1.02x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.15x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 2.16 sec: 8.17x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 29.8 ms: 3.07x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 330 ms: 2.05x faster                                                             |
| async_tree_io              | 693 ms                                                          | 355 ms: 1.95x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 147 ms: 1.89x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 188 ms: 1.86x faster                                                             |
| deepcopy_memo              | 38.4 us                                                         | 21.3 us: 1.80x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 308 ms: 1.77x faster                                                             |
| deepcopy                   | 360 us                                                          | 205 us: 1.76x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 211 ms: 1.73x faster                                                             |
| async_tree_none            | 298 ms                                                          | 173 ms: 1.72x faster                                                             |
| mdp                        | 1.91 sec                                                        | 1.13 sec: 1.70x faster                                                           |
| generators                 | 38.5 ms                                                         | 22.8 ms: 1.69x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 334 ms: 1.69x faster                                                             |
| float                      | 76.7 ms                                                         | 45.7 ms: 1.68x faster                                                            |
| logging_silent             | 101 ns                                                          | 61.9 ns: 1.63x faster                                                            |
| unpack_sequence            | 62.5 ns                                                         | 38.6 ns: 1.62x faster                                                            |
| asyncio_tcp                | 662 ms                                                          | 412 ms: 1.61x faster                                                             |
| nbody                      | 127 ms                                                          | 80.8 ms: 1.57x faster                                                            |
| comprehensions             | 19.2 us                                                         | 12.2 us: 1.57x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.37 us: 1.52x faster                                                            |
| chaos                      | 69.4 ms                                                         | 46.0 ms: 1.51x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 2.39 ms: 1.50x faster                                                            |
| logging_simple             | 9.75 us                                                         | 6.60 us: 1.48x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 2.19 us: 1.48x faster                                                            |
| go                         | 137 ms                                                          | 93.5 ms: 1.47x faster                                                            |
| logging_format             | 10.4 us                                                         | 7.10 us: 1.47x faster                                                            |
| pidigits                   | 199 ms                                                          | 136 ms: 1.46x faster                                                             |
| raytrace                   | 308 ms                                                          | 211 ms: 1.46x faster                                                             |
| spectral_norm              | 104 ms                                                          | 71.7 ms: 1.45x faster                                                            |
| scimark_sor                | 130 ms                                                          | 90.5 ms: 1.44x faster                                                            |
| hexiom                     | 6.82 ms                                                         | 4.80 ms: 1.42x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 41.6 ms: 1.41x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 14.9 ms: 1.40x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 66.7 ms: 1.40x faster                                                            |
| pyflate                    | 424 ms                                                          | 311 ms: 1.36x faster                                                             |
| regex_compile              | 129 ms                                                          | 95.4 ms: 1.35x faster                                                            |
| django_template            | 36.9 ms                                                         | 27.5 ms: 1.34x faster                                                            |
| pycparser                  | 978 ms                                                          | 728 ms: 1.34x faster                                                             |
| json                       | 4.15 ms                                                         | 3.12 ms: 1.33x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 51.0 ms: 1.30x faster                                                            |
| unpickle_pure_python       | 210 us                                                          | 163 us: 1.29x faster                                                             |
| nqueens                    | 93.7 ms                                                         | 72.9 ms: 1.28x faster                                                            |
| json_loads                 | 20.4 us                                                         | 16.0 us: 1.27x faster                                                            |
| pprint_safe_repr           | 721 ms                                                          | 571 ms: 1.26x faster                                                             |
| sympy_str                  | 240 ms                                                          | 190 ms: 1.26x faster                                                             |
| sympy_sum                  | 123 ms                                                          | 97.5 ms: 1.26x faster                                                            |
| scimark_fft                | 271 ms                                                          | 215 ms: 1.26x faster                                                             |
| regex_effbot               | 2.04 ms                                                         | 1.63 ms: 1.25x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 62.1 ms: 1.25x faster                                                            |
| json_dumps                 | 7.40 ms                                                         | 5.95 ms: 1.24x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 56.1 ms: 1.23x faster                                                            |
| async_generators           | 313 ms                                                          | 254 ms: 1.23x faster                                                             |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.13 ms: 1.23x faster                                                            |
| richards                   | 41.3 ms                                                         | 33.6 ms: 1.23x faster                                                            |
| sympy_expand               | 398 ms                                                          | 324 ms: 1.23x faster                                                             |
| 2to3                       | 280 ms                                                          | 228 ms: 1.23x faster                                                             |
| sympy_integrate            | 17.5 ms                                                         | 14.4 ms: 1.22x faster                                                            |
| pickle_pure_python         | 286 us                                                          | 239 us: 1.20x faster                                                             |
| richards_super             | 46.5 ms                                                         | 39.5 ms: 1.18x faster                                                            |
| gc_traversal               | 1.44 ms                                                         | 1.23 ms: 1.18x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 45.5 ms: 1.17x faster                                                            |
| fannkuch                   | 354 ms                                                          | 309 ms: 1.14x faster                                                             |
| xml_etree_generate         | 72.1 ms                                                         | 63.8 ms: 1.13x faster                                                            |
| regex_v8                   | 15.0 ms                                                         | 13.7 ms: 1.10x faster                                                            |
| regex_dna                  | 127 ms                                                          | 116 ms: 1.09x faster                                                             |
| pickle_list                | 3.37 us                                                         | 3.09 us: 1.09x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 105 ms: 1.07x faster                                                             |
| telco                      | 5.51 ms                                                         | 5.27 ms: 1.05x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 1.08 ms: 1.02x faster                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 19.4 ms: 1.02x slower                                                            |
| mako                       | 9.96 ms                                                         | 10.1 ms: 1.02x slower                                                            |
| pickle_dict                | 19.9 us                                                         | 20.4 us: 1.02x slower                                                            |
| pickle                     | 7.79 us                                                         | 8.00 us: 1.03x slower                                                            |
| typing_runtime_protocols   | 126 us                                                          | 131 us: 1.03x slower                                                             |
| unpickle                   | 9.71 us                                                         | 10.2 us: 1.05x slower                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 79.2 ms: 1.05x slower                                                            |
| unpickle_list              | 2.95 us                                                         | 3.12 us: 1.06x slower                                                            |
| pprint_pformat             | 1.50 sec                                                        | 1.70 sec: 1.14x slower                                                           |
| python_startup             | 22.4 ms                                                         | 25.7 ms: 1.15x slower                                                            |
| coverage                   | 48.4 ms                                                         | 68.2 ms: 1.41x slower                                                            |
| docutils                   | 1.98 sec                                                        | 2.88 sec: 1.45x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.02 ms: 1.56x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.32x faster                                                                     |

Benchmark hidden because not significant (2): meteor_contest, tomli_loads
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250830-3.15.0a0-d3d94e0-NOGIL/bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.318x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: unknown