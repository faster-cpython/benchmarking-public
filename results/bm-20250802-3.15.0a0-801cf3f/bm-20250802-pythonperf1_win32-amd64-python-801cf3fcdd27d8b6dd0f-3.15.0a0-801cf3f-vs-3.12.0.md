# Results vs. 3.12.0

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: windows-amd64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.431x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.40x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 227 ms: 1.23x faster                                                             |
| docutils       | 1.98 sec                                                        | 1.61 sec: 1.23x faster                                                           |
| Geometric mean | (ref)                                                           | 1.23x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io              | 693 ms                                                          | 398 ms: 1.74x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 218 ms: 1.67x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 406 ms: 1.67x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 339 ms: 1.67x faster                                                             |
| async_tree_none            | 298 ms                                                          | 183 ms: 1.63x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 218 ms: 1.61x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 173 ms: 1.60x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 348 ms: 1.57x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.64x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 65.3 ms: 1.94x faster                                                            |
| float          | 76.7 ms                                                         | 43.5 ms: 1.76x faster                                                            |
| pidigits       | 199 ms                                                          | 146 ms: 1.37x faster                                                             |
| Geometric mean | (ref)                                                           | 1.67x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 81.0 ms: 1.59x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.64 ms: 1.24x faster                                                            |
| regex_dna      | 127 ms                                                          | 121 ms: 1.05x faster                                                             |
| regex_v8       | 15.0 ms                                                         | 14.5 ms: 1.04x faster                                                            |
| Geometric mean | (ref)                                                           | 1.21x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 134 us: 1.57x faster                                                             |
| tomli_loads          | 2.20 sec                                                        | 1.42 sec: 1.55x faster                                                           |
| json_loads           | 20.4 us                                                         | 14.6 us: 1.40x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 212 us: 1.35x faster                                                             |
| xml_etree_process    | 53.2 ms                                                         | 40.0 ms: 1.33x faster                                                            |
| xml_etree_parse      | 113 ms                                                          | 90.8 ms: 1.25x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 58.0 ms: 1.24x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 66.1 ms: 1.17x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 6.35 ms: 1.16x faster                                                            |
| unpickle             | 9.71 us                                                         | 8.74 us: 1.11x faster                                                            |
| unpickle_list        | 2.95 us                                                         | 2.83 us: 1.04x faster                                                            |
| pickle_dict          | 19.9 us                                                         | 20.6 us: 1.03x slower                                                            |
| pickle               | 7.79 us                                                         | 8.36 us: 1.07x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.20x faster                                                                     |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.4 ms: 1.07x slower                                                            |
| python_startup         | 22.4 ms                                                         | 27.2 ms: 1.21x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.14x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.9 ms                                                         | 24.6 ms: 1.50x faster                                                            |
| mako            | 9.96 ms                                                         | 6.67 ms: 1.49x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.50x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 1.30 sec: 13.56x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 33.0 ms: 2.77x faster                                                            |
| mdp                        | 1.91 sec                                                        | 824 ms: 2.32x faster                                                             |
| deepcopy_memo              | 38.4 us                                                         | 18.4 us: 2.08x faster                                                            |
| deepcopy                   | 360 us                                                          | 175 us: 2.05x faster                                                             |
| generators                 | 38.5 ms                                                         | 19.4 ms: 1.98x faster                                                            |
| nbody                      | 127 ms                                                          | 65.3 ms: 1.94x faster                                                            |
| go                         | 137 ms                                                          | 77.1 ms: 1.78x faster                                                            |
| comprehensions             | 19.2 us                                                         | 10.8 us: 1.77x faster                                                            |
| float                      | 76.7 ms                                                         | 43.5 ms: 1.76x faster                                                            |
| async_tree_io              | 693 ms                                                          | 398 ms: 1.74x faster                                                             |
| logging_silent             | 101 ns                                                          | 58.6 ns: 1.72x faster                                                            |
| raytrace                   | 308 ms                                                          | 181 ms: 1.70x faster                                                             |
| deepcopy_reduce            | 3.23 us                                                         | 1.91 us: 1.69x faster                                                            |
| chaos                      | 69.4 ms                                                         | 41.3 ms: 1.68x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 218 ms: 1.67x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 406 ms: 1.67x faster                                                             |
| unpack_sequence            | 62.5 ns                                                         | 37.5 ns: 1.67x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 339 ms: 1.67x faster                                                             |
| scimark_sor                | 130 ms                                                          | 78.2 ms: 1.66x faster                                                            |
| hexiom                     | 6.82 ms                                                         | 4.19 ms: 1.63x faster                                                            |
| async_tree_none            | 298 ms                                                          | 183 ms: 1.63x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 218 ms: 1.61x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 173 ms: 1.60x faster                                                             |
| regex_compile              | 129 ms                                                          | 81.0 ms: 1.59x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 41.9 ms: 1.59x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 2.27 ms: 1.58x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 348 ms: 1.57x faster                                                             |
| unpickle_pure_python       | 210 us                                                          | 134 us: 1.57x faster                                                             |
| scimark_lu                 | 93.2 ms                                                         | 60.2 ms: 1.55x faster                                                            |
| tomli_loads                | 2.20 sec                                                        | 1.42 sec: 1.55x faster                                                           |
| spectral_norm              | 104 ms                                                          | 67.2 ms: 1.54x faster                                                            |
| logging_simple             | 9.75 us                                                         | 6.34 us: 1.54x faster                                                            |
| logging_format             | 10.4 us                                                         | 6.76 us: 1.54x faster                                                            |
| django_template            | 36.9 ms                                                         | 24.6 ms: 1.50x faster                                                            |
| mako                       | 9.96 ms                                                         | 6.67 ms: 1.49x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.60 ms: 1.48x faster                                                            |
| asyncio_tcp                | 662 ms                                                          | 448 ms: 1.48x faster                                                             |
| nqueens                    | 93.7 ms                                                         | 63.5 ms: 1.47x faster                                                            |
| scimark_fft                | 271 ms                                                          | 184 ms: 1.47x faster                                                             |
| pyflate                    | 424 ms                                                          | 289 ms: 1.46x faster                                                             |
| pprint_pformat             | 1.50 sec                                                        | 1.03 sec: 1.45x faster                                                           |
| richards_super             | 46.5 ms                                                         | 32.1 ms: 1.45x faster                                                            |
| richards                   | 41.3 ms                                                         | 29.0 ms: 1.43x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 41.1 ms: 1.42x faster                                                            |
| pprint_safe_repr           | 721 ms                                                          | 509 ms: 1.42x faster                                                             |
| crypto_pyaes               | 69.2 ms                                                         | 49.2 ms: 1.41x faster                                                            |
| sympy_str                  | 240 ms                                                          | 171 ms: 1.40x faster                                                             |
| coroutines                 | 20.9 ms                                                         | 14.9 ms: 1.40x faster                                                            |
| json_loads                 | 20.4 us                                                         | 14.6 us: 1.40x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 12.6 ms: 1.39x faster                                                            |
| fannkuch                   | 354 ms                                                          | 256 ms: 1.38x faster                                                             |
| sympy_expand               | 398 ms                                                          | 288 ms: 1.38x faster                                                             |
| sympy_sum                  | 123 ms                                                          | 89.5 ms: 1.37x faster                                                            |
| pidigits                   | 199 ms                                                          | 146 ms: 1.37x faster                                                             |
| pickle_pure_python         | 286 us                                                          | 212 us: 1.35x faster                                                             |
| json                       | 4.15 ms                                                         | 3.09 ms: 1.35x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 40.0 ms: 1.33x faster                                                            |
| pycparser                  | 978 ms                                                          | 739 ms: 1.32x faster                                                             |
| async_generators           | 313 ms                                                          | 237 ms: 1.32x faster                                                             |
| sqlite_synth               | 2.07 us                                                         | 1.58 us: 1.31x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 868 us: 1.27x faster                                                             |
| xml_etree_parse            | 113 ms                                                          | 90.8 ms: 1.25x faster                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 58.0 ms: 1.24x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.64 ms: 1.24x faster                                                            |
| typing_runtime_protocols   | 126 us                                                          | 102 us: 1.24x faster                                                             |
| 2to3                       | 280 ms                                                          | 227 ms: 1.23x faster                                                             |
| docutils                   | 1.98 sec                                                        | 1.61 sec: 1.23x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 72.2 ms: 1.20x faster                                                            |
| telco                      | 5.51 ms                                                         | 4.61 ms: 1.20x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 66.1 ms: 1.17x faster                                                            |
| json_dumps                 | 7.40 ms                                                         | 6.35 ms: 1.16x faster                                                            |
| unpickle                   | 9.71 us                                                         | 8.74 us: 1.11x faster                                                            |
| regex_dna                  | 127 ms                                                          | 121 ms: 1.05x faster                                                             |
| unpickle_list              | 2.95 us                                                         | 2.83 us: 1.04x faster                                                            |
| regex_v8                   | 15.0 ms                                                         | 14.5 ms: 1.04x faster                                                            |
| pickle_dict                | 19.9 us                                                         | 20.6 us: 1.03x slower                                                            |
| coverage                   | 48.4 ms                                                         | 51.3 ms: 1.06x slower                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 20.4 ms: 1.07x slower                                                            |
| pickle                     | 7.79 us                                                         | 8.36 us: 1.07x slower                                                            |
| python_startup             | 22.4 ms                                                         | 27.2 ms: 1.21x slower                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 96.9 ms: 1.28x slower                                                            |
| gc_traversal               | 1.44 ms                                                         | 2.10 ms: 1.45x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.33 ms: 2.04x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.43x faster                                                                     |

Benchmark hidden because not significant (1): pickle_list
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.431x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.43x
- 95% likely to have a speedup of 1.42x
- 99% likely to have a speedup of 1.40x

# Memory
- memory change: unknown