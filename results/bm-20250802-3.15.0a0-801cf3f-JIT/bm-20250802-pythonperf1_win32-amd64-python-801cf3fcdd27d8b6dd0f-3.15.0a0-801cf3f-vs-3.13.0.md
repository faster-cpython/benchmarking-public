# Results vs. 3.13.0

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: windows-amd64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.262x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 224 ms: 1.12x faster                                                             |
| docutils       | 1.78 sec                                                        | 1.67 sec: 1.06x faster                                                           |
| html5lib       | 47.5 ms                                                         | 41.9 ms: 1.13x faster                                                            |
| sphinx         | 719 ms                                                          | 653 ms: 1.10x faster                                                             |
| Geometric mean | (ref)                                                           | 1.10x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 166 ms: 2.19x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 340 ms: 1.42x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 210 ms: 1.41x faster                                                             |
| async_tree_none            | 245 ms                                                          | 181 ms: 1.35x faster                                                             |
| async_tree_io              | 526 ms                                                          | 401 ms: 1.31x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 216 ms: 1.31x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 353 ms: 1.29x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 171 ms: 1.25x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 396 ms: 1.25x faster                                                             |
| async_generators           | 270 ms                                                          | 244 ms: 1.10x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.8 ms: 1.10x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.34x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 80.0 ms                                                         | 55.3 ms: 1.45x faster                                                            |
| pidigits       | 201 ms                                                          | 149 ms: 1.35x faster                                                             |
| float          | 54.6 ms                                                         | 44.3 ms: 1.23x faster                                                            |
| Geometric mean | (ref)                                                           | 1.34x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 82.4 ms: 1.23x faster                                                            |
| regex_v8       | 16.8 ms                                                         | 14.4 ms: 1.17x faster                                                            |
| regex_effbot   | 1.80 ms                                                         | 1.70 ms: 1.06x faster                                                            |
| regex_dna      | 114 ms                                                          | 124 ms: 1.09x slower                                                             |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 1.71 sec                                                        | 1.14 sec: 1.50x faster                                                           |
| unpickle_pure_python | 160 us                                                          | 108 us: 1.49x faster                                                             |
| json_loads           | 21.6 us                                                         | 14.7 us: 1.47x faster                                                            |
| xml_etree_process    | 44.2 ms                                                         | 35.9 ms: 1.23x faster                                                            |
| xml_etree_generate   | 61.4 ms                                                         | 51.0 ms: 1.20x faster                                                            |
| xml_etree_parse      | 107 ms                                                          | 89.3 ms: 1.20x faster                                                            |
| json_dumps           | 7.30 ms                                                         | 6.38 ms: 1.14x faster                                                            |
| pickle_pure_python   | 231 us                                                          | 210 us: 1.10x faster                                                             |
| xml_etree_iterparse  | 62.6 ms                                                         | 63.4 ms: 1.01x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.25x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 26.5 ms: 1.07x faster                                                            |
| python_startup_no_site | 19.7 ms                                                         | 20.0 ms: 1.02x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.02x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 34.7 ms: 1.45x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 15.9 ms: 1.35x faster                                                            |
| mako            | 7.09 ms                                                         | 5.34 ms: 1.33x faster                                                            |
| django_template | 29.8 ms                                                         | 26.0 ms: 1.15x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.31x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 505 us: 19.77x faster                                                            |
| coverage                   | 324 ms                                                          | 51.5 ms: 6.29x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 33.5 ms: 2.47x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 166 ms: 2.19x faster                                                             |
| mdp                        | 1.62 sec                                                        | 807 ms: 2.01x faster                                                             |
| deepcopy                   | 314 us                                                          | 179 us: 1.76x faster                                                             |
| deepcopy_reduce            | 2.92 us                                                         | 1.92 us: 1.52x faster                                                            |
| tomli_loads                | 1.71 sec                                                        | 1.14 sec: 1.50x faster                                                           |
| telco                      | 6.96 ms                                                         | 4.68 ms: 1.49x faster                                                            |
| unpickle_pure_python       | 160 us                                                          | 108 us: 1.49x faster                                                             |
| json_loads                 | 21.6 us                                                         | 14.7 us: 1.47x faster                                                            |
| genshi_xml                 | 50.1 ms                                                         | 34.7 ms: 1.45x faster                                                            |
| nbody                      | 80.0 ms                                                         | 55.3 ms: 1.45x faster                                                            |
| pprint_pformat             | 1.33 sec                                                        | 919 ms: 1.45x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 340 ms: 1.42x faster                                                             |
| pprint_safe_repr           | 648 ms                                                          | 456 ms: 1.42x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 210 ms: 1.41x faster                                                             |
| fannkuch                   | 299 ms                                                          | 214 ms: 1.40x faster                                                             |
| scimark_fft                | 205 ms                                                          | 149 ms: 1.37x faster                                                             |
| bpe_tokeniser              | 3.46 sec                                                        | 2.53 sec: 1.37x faster                                                           |
| go                         | 109 ms                                                          | 79.5 ms: 1.37x faster                                                            |
| async_tree_none            | 245 ms                                                          | 181 ms: 1.35x faster                                                             |
| genshi_text                | 21.5 ms                                                         | 15.9 ms: 1.35x faster                                                            |
| pidigits                   | 201 ms                                                          | 149 ms: 1.35x faster                                                             |
| json                       | 4.27 ms                                                         | 3.17 ms: 1.35x faster                                                            |
| mako                       | 7.09 ms                                                         | 5.34 ms: 1.33x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 19.2 us: 1.33x faster                                                            |
| async_tree_io              | 526 ms                                                          | 401 ms: 1.31x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 216 ms: 1.31x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 353 ms: 1.29x faster                                                             |
| typing_runtime_protocols   | 138 us                                                          | 107 us: 1.29x faster                                                             |
| logging_format             | 8.72 us                                                         | 6.85 us: 1.27x faster                                                            |
| logging_simple             | 7.99 us                                                         | 6.32 us: 1.26x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 171 ms: 1.25x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 396 ms: 1.25x faster                                                             |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.28 ms: 1.25x faster                                                            |
| pycparser                  | 872 ms                                                          | 703 ms: 1.24x faster                                                             |
| sympy_expand               | 373 ms                                                          | 303 ms: 1.23x faster                                                             |
| float                      | 54.6 ms                                                         | 44.3 ms: 1.23x faster                                                            |
| xml_etree_process          | 44.2 ms                                                         | 35.9 ms: 1.23x faster                                                            |
| regex_compile              | 101 ms                                                          | 82.4 ms: 1.23x faster                                                            |
| sqlite_synth               | 1.95 us                                                         | 1.60 us: 1.22x faster                                                            |
| sympy_str                  | 212 ms                                                          | 175 ms: 1.21x faster                                                             |
| xml_etree_generate         | 61.4 ms                                                         | 51.0 ms: 1.20x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 89.3 ms: 1.20x faster                                                            |
| pyflate                    | 320 ms                                                          | 267 ms: 1.20x faster                                                             |
| chaos                      | 50.2 ms                                                         | 41.9 ms: 1.20x faster                                                            |
| crypto_pyaes               | 56.9 ms                                                         | 47.8 ms: 1.19x faster                                                            |
| sympy_sum                  | 106 ms                                                          | 89.8 ms: 1.18x faster                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 40.7 ms: 1.17x faster                                                            |
| richards                   | 32.7 ms                                                         | 27.9 ms: 1.17x faster                                                            |
| comprehensions             | 12.5 us                                                         | 10.7 us: 1.17x faster                                                            |
| richards_super             | 36.7 ms                                                         | 31.5 ms: 1.17x faster                                                            |
| regex_v8                   | 16.8 ms                                                         | 14.4 ms: 1.17x faster                                                            |
| nqueens                    | 72.1 ms                                                         | 62.1 ms: 1.16x faster                                                            |
| dulwich_log                | 48.8 ms                                                         | 42.2 ms: 1.15x faster                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 870 us: 1.15x faster                                                             |
| sympy_integrate            | 15.0 ms                                                         | 13.0 ms: 1.15x faster                                                            |
| django_template            | 29.8 ms                                                         | 26.0 ms: 1.15x faster                                                            |
| json_dumps                 | 7.30 ms                                                         | 6.38 ms: 1.14x faster                                                            |
| html5lib                   | 47.5 ms                                                         | 41.9 ms: 1.13x faster                                                            |
| 2to3                       | 250 ms                                                          | 224 ms: 1.12x faster                                                             |
| async_generators           | 270 ms                                                          | 244 ms: 1.10x faster                                                             |
| generators                 | 21.8 ms                                                         | 19.8 ms: 1.10x faster                                                            |
| sphinx                     | 719 ms                                                          | 653 ms: 1.10x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.8 ms: 1.10x faster                                                            |
| pylint                     | 227 ms                                                          | 206 ms: 1.10x faster                                                             |
| pickle_pure_python         | 231 us                                                          | 210 us: 1.10x faster                                                             |
| scimark_sor                | 85.9 ms                                                         | 78.5 ms: 1.09x faster                                                            |
| logging_silent             | 60.3 ns                                                         | 56.4 ns: 1.07x faster                                                            |
| spectral_norm              | 69.4 ms                                                         | 65.0 ms: 1.07x faster                                                            |
| python_startup             | 28.3 ms                                                         | 26.5 ms: 1.07x faster                                                            |
| docutils                   | 1.78 sec                                                        | 1.67 sec: 1.06x faster                                                           |
| raytrace                   | 201 ms                                                          | 189 ms: 1.06x faster                                                             |
| regex_effbot               | 1.80 ms                                                         | 1.70 ms: 1.06x faster                                                            |
| hexiom                     | 4.44 ms                                                         | 4.28 ms: 1.04x faster                                                            |
| meteor_contest             | 74.6 ms                                                         | 73.1 ms: 1.02x faster                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 63.4 ms: 1.01x slower                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 20.0 ms: 1.02x slower                                                            |
| bench_mp_pool              | 90.6 ms                                                         | 96.6 ms: 1.07x slower                                                            |
| regex_dna                  | 114 ms                                                          | 124 ms: 1.09x slower                                                             |
| k_core                     | 1.38 sec                                                        | 1.63 sec: 1.18x slower                                                           |
| connected_components       | 267 ms                                                          | 326 ms: 1.22x slower                                                             |
| shortest_path              | 290 ms                                                          | 357 ms: 1.23x slower                                                             |
| gc_traversal               | 1.75 ms                                                         | 2.21 ms: 1.26x slower                                                            |
| create_gc_cycles           | 1.06 ms                                                         | 1.36 ms: 1.28x slower                                                            |
| many_optionals             | 436 us                                                          | 581 us: 1.33x slower                                                             |
| subparsers                 | 14.8 ms                                                         | 30.7 ms: 2.08x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.25x faster                                                                     |

Benchmark hidden because not significant (2): scimark_lu, deltablue
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250802-3.15.0a0-801cf3f-JIT/bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.262x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: unknown