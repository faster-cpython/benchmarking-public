# Results vs. 3.12.0

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: windows-amd64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.298x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 234 ms: 1.20x faster                                                             |
| docutils       | 1.98 sec                                                        | 3.03 sec: 1.53x slower                                                           |
| Geometric mean | (ref)                                                           | 1.13x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 342 ms: 1.98x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 150 ms: 1.85x faster                                                             |
| async_tree_io              | 693 ms                                                          | 377 ms: 1.84x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 198 ms: 1.77x faster                                                             |
| async_tree_none            | 298 ms                                                          | 173 ms: 1.72x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 334 ms: 1.69x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 332 ms: 1.64x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 225 ms: 1.62x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.76x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 47.7 ms: 1.61x faster                                                            |
| nbody          | 127 ms                                                          | 82.8 ms: 1.53x faster                                                            |
| pidigits       | 199 ms                                                          | 138 ms: 1.44x faster                                                             |
| Geometric mean | (ref)                                                           | 1.53x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 99.5 ms: 1.30x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.63 ms: 1.25x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 13.4 ms: 1.12x faster                                                            |
| regex_dna      | 127 ms                                                          | 117 ms: 1.08x faster                                                             |
| Geometric mean | (ref)                                                           | 1.18x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 77.6 ms                                                         | 58.6 ms: 1.32x faster                                                            |
| unpickle_pure_python | 210 us                                                          | 160 us: 1.31x faster                                                             |
| json_loads           | 20.4 us                                                         | 15.8 us: 1.29x faster                                                            |
| xml_etree_parse      | 113 ms                                                          | 92.1 ms: 1.23x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 240 us: 1.19x faster                                                             |
| xml_etree_process    | 53.2 ms                                                         | 44.8 ms: 1.19x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 64.0 ms: 1.13x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 6.75 ms: 1.10x faster                                                            |
| pickle_list          | 3.37 us                                                         | 3.29 us: 1.02x faster                                                            |
| pickle               | 7.79 us                                                         | 8.23 us: 1.06x slower                                                            |
| pickle_dict          | 19.9 us                                                         | 21.2 us: 1.06x slower                                                            |
| unpickle_list        | 2.95 us                                                         | 3.19 us: 1.08x slower                                                            |
| unpickle             | 9.71 us                                                         | 10.6 us: 1.10x slower                                                            |
| tomli_loads          | 2.20 sec                                                        | 2.75 sec: 1.25x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.08x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.1 ms: 1.05x slower                                                            |
| python_startup         | 22.4 ms                                                         | 27.0 ms: 1.21x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.13x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.9 ms                                                         | 27.6 ms: 1.34x faster                                                            |
| mako            | 9.96 ms                                                         | 10.3 ms: 1.03x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.14x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 2.35 sec: 7.52x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 32.8 ms: 2.78x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 342 ms: 1.98x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 150 ms: 1.85x faster                                                             |
| async_tree_io              | 693 ms                                                          | 377 ms: 1.84x faster                                                             |
| deepcopy_memo              | 38.4 us                                                         | 21.1 us: 1.81x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 198 ms: 1.77x faster                                                             |
| deepcopy                   | 360 us                                                          | 205 us: 1.76x faster                                                             |
| async_tree_none            | 298 ms                                                          | 173 ms: 1.72x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 334 ms: 1.69x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 332 ms: 1.64x faster                                                             |
| generators                 | 38.5 ms                                                         | 23.7 ms: 1.62x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 225 ms: 1.62x faster                                                             |
| float                      | 76.7 ms                                                         | 47.7 ms: 1.61x faster                                                            |
| comprehensions             | 19.2 us                                                         | 12.1 us: 1.58x faster                                                            |
| unpack_sequence            | 62.5 ns                                                         | 40.3 ns: 1.55x faster                                                            |
| mdp                        | 1.91 sec                                                        | 1.24 sec: 1.55x faster                                                           |
| nbody                      | 127 ms                                                          | 82.8 ms: 1.53x faster                                                            |
| logging_silent             | 101 ns                                                          | 66.7 ns: 1.51x faster                                                            |
| chaos                      | 69.4 ms                                                         | 46.1 ms: 1.50x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 2.15 us: 1.50x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.39 us: 1.49x faster                                                            |
| scimark_sor                | 130 ms                                                          | 87.8 ms: 1.48x faster                                                            |
| go                         | 137 ms                                                          | 93.8 ms: 1.46x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 2.47 ms: 1.45x faster                                                            |
| pidigits                   | 199 ms                                                          | 138 ms: 1.44x faster                                                             |
| asyncio_tcp                | 662 ms                                                          | 463 ms: 1.43x faster                                                             |
| hexiom                     | 6.82 ms                                                         | 4.78 ms: 1.43x faster                                                            |
| logging_format             | 10.4 us                                                         | 7.30 us: 1.43x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 65.6 ms: 1.42x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 14.9 ms: 1.41x faster                                                            |
| raytrace                   | 308 ms                                                          | 220 ms: 1.40x faster                                                             |
| logging_simple             | 9.75 us                                                         | 7.08 us: 1.38x faster                                                            |
| spectral_norm              | 104 ms                                                          | 75.9 ms: 1.37x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 42.8 ms: 1.37x faster                                                            |
| json                       | 4.15 ms                                                         | 3.07 ms: 1.35x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 49.6 ms: 1.34x faster                                                            |
| pyflate                    | 424 ms                                                          | 316 ms: 1.34x faster                                                             |
| django_template            | 36.9 ms                                                         | 27.6 ms: 1.34x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 58.6 ms: 1.32x faster                                                            |
| unpickle_pure_python       | 210 us                                                          | 160 us: 1.31x faster                                                             |
| regex_compile              | 129 ms                                                          | 99.5 ms: 1.30x faster                                                            |
| json_loads                 | 20.4 us                                                         | 15.8 us: 1.29x faster                                                            |
| scimark_fft                | 271 ms                                                          | 213 ms: 1.27x faster                                                             |
| pprint_safe_repr           | 721 ms                                                          | 566 ms: 1.27x faster                                                             |
| nqueens                    | 93.7 ms                                                         | 74.5 ms: 1.26x faster                                                            |
| sympy_str                  | 240 ms                                                          | 192 ms: 1.25x faster                                                             |
| regex_effbot               | 2.04 ms                                                         | 1.63 ms: 1.25x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.09 ms: 1.25x faster                                                            |
| sympy_sum                  | 123 ms                                                          | 98.8 ms: 1.24x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 92.1 ms: 1.23x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 14.3 ms: 1.22x faster                                                            |
| richards                   | 41.3 ms                                                         | 33.8 ms: 1.22x faster                                                            |
| sympy_expand               | 398 ms                                                          | 328 ms: 1.21x faster                                                             |
| pycparser                  | 978 ms                                                          | 811 ms: 1.21x faster                                                             |
| crypto_pyaes               | 69.2 ms                                                         | 57.6 ms: 1.20x faster                                                            |
| 2to3                       | 280 ms                                                          | 234 ms: 1.20x faster                                                             |
| pickle_pure_python         | 286 us                                                          | 240 us: 1.19x faster                                                             |
| xml_etree_process          | 53.2 ms                                                         | 44.8 ms: 1.19x faster                                                            |
| gc_traversal               | 1.44 ms                                                         | 1.21 ms: 1.19x faster                                                            |
| richards_super             | 46.5 ms                                                         | 39.3 ms: 1.18x faster                                                            |
| async_generators           | 313 ms                                                          | 268 ms: 1.17x faster                                                             |
| fannkuch                   | 354 ms                                                          | 306 ms: 1.16x faster                                                             |
| xml_etree_generate         | 72.1 ms                                                         | 64.0 ms: 1.13x faster                                                            |
| regex_v8                   | 15.0 ms                                                         | 13.4 ms: 1.12x faster                                                            |
| json_dumps                 | 7.40 ms                                                         | 6.75 ms: 1.10x faster                                                            |
| regex_dna                  | 127 ms                                                          | 117 ms: 1.08x faster                                                             |
| telco                      | 5.51 ms                                                         | 5.25 ms: 1.05x faster                                                            |
| pickle_list                | 3.37 us                                                         | 3.29 us: 1.02x faster                                                            |
| typing_runtime_protocols   | 126 us                                                          | 129 us: 1.02x slower                                                             |
| mako                       | 9.96 ms                                                         | 10.3 ms: 1.03x slower                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 20.1 ms: 1.05x slower                                                            |
| pickle                     | 7.79 us                                                         | 8.23 us: 1.06x slower                                                            |
| pickle_dict                | 19.9 us                                                         | 21.2 us: 1.06x slower                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 80.3 ms: 1.07x slower                                                            |
| unpickle_list              | 2.95 us                                                         | 3.19 us: 1.08x slower                                                            |
| unpickle                   | 9.71 us                                                         | 10.6 us: 1.10x slower                                                            |
| pprint_pformat             | 1.50 sec                                                        | 1.76 sec: 1.17x slower                                                           |
| python_startup             | 22.4 ms                                                         | 27.0 ms: 1.21x slower                                                            |
| tomli_loads                | 2.20 sec                                                        | 2.75 sec: 1.25x slower                                                           |
| coverage                   | 48.4 ms                                                         | 67.7 ms: 1.40x slower                                                            |
| docutils                   | 1.98 sec                                                        | 3.03 sec: 1.53x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.01 ms: 1.55x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.30x faster                                                                     |

Benchmark hidden because not significant (2): meteor_contest, bench_thread_pool
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250802-3.15.0a0-801cf3f-NOGIL/bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.298x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: unknown