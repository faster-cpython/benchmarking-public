# Results vs. 3.13.0

- fork: python
- ref: 47b01da4ccedd9c00fad
- machine: windows-amd64
- commit hash: 47b01da
- commit date: 2025-07-12
- overall geometric mean: 1.284x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 221 ms: 1.13x faster                                                             |
| docutils       | 1.78 sec                                                        | 1.61 sec: 1.10x faster                                                           |
| html5lib       | 47.5 ms                                                         | 38.1 ms: 1.25x faster                                                            |
| sphinx         | 719 ms                                                          | 634 ms: 1.13x faster                                                             |
| Geometric mean | (ref)                                                           | 1.15x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 158 ms: 2.29x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 332 ms: 1.46x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 204 ms: 1.45x faster                                                             |
| async_tree_none            | 245 ms                                                          | 170 ms: 1.44x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 209 ms: 1.35x faster                                                             |
| async_tree_io              | 526 ms                                                          | 391 ms: 1.34x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 341 ms: 1.34x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 169 ms: 1.27x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 398 ms: 1.24x faster                                                             |
| async_generators           | 270 ms                                                          | 229 ms: 1.18x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.4 ms: 1.13x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.38x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 145 ms: 1.39x faster                                                             |
| float          | 54.6 ms                                                         | 43.5 ms: 1.25x faster                                                            |
| nbody          | 80.0 ms                                                         | 65.6 ms: 1.22x faster                                                            |
| Geometric mean | (ref)                                                           | 1.28x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 79.0 ms: 1.28x faster                                                            |
| regex_v8       | 16.8 ms                                                         | 13.2 ms: 1.28x faster                                                            |
| regex_effbot   | 1.80 ms                                                         | 1.49 ms: 1.21x faster                                                            |
| regex_dna      | 114 ms                                                          | 116 ms: 1.02x slower                                                             |
| Geometric mean | (ref)                                                           | 1.18x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 14.2 us: 1.52x faster                                                            |
| tomli_loads          | 1.71 sec                                                        | 1.35 sec: 1.27x faster                                                           |
| xml_etree_parse      | 107 ms                                                          | 86.6 ms: 1.24x faster                                                            |
| unpickle_pure_python | 160 us                                                          | 132 us: 1.21x faster                                                             |
| json_dumps           | 7.30 ms                                                         | 6.13 ms: 1.19x faster                                                            |
| xml_etree_process    | 44.2 ms                                                         | 38.8 ms: 1.14x faster                                                            |
| pickle_pure_python   | 231 us                                                          | 208 us: 1.11x faster                                                             |
| xml_etree_generate   | 61.4 ms                                                         | 55.2 ms: 1.11x faster                                                            |
| xml_etree_iterparse  | 62.6 ms                                                         | 63.6 ms: 1.02x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.19x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 26.1 ms: 1.08x faster                                                            |
| python_startup_no_site | 19.7 ms                                                         | 19.4 ms: 1.01x faster                                                            |
| Geometric mean         | (ref)                                                           | 1.05x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 34.4 ms: 1.46x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 15.6 ms: 1.38x faster                                                            |
| django_template | 29.8 ms                                                         | 25.1 ms: 1.19x faster                                                            |
| mako            | 7.09 ms                                                         | 6.52 ms: 1.09x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.27x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 495 us: 20.14x faster                                                            |
| coverage                   | 324 ms                                                          | 49.6 ms: 6.53x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 30.0 ms: 2.76x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 158 ms: 2.29x faster                                                             |
| mdp                        | 1.62 sec                                                        | 807 ms: 2.01x faster                                                             |
| deepcopy                   | 314 us                                                          | 167 us: 1.88x faster                                                             |
| deepcopy_reduce            | 2.92 us                                                         | 1.82 us: 1.60x faster                                                            |
| telco                      | 6.96 ms                                                         | 4.51 ms: 1.54x faster                                                            |
| json_loads                 | 21.6 us                                                         | 14.2 us: 1.52x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 17.2 us: 1.48x faster                                                            |
| genshi_xml                 | 50.1 ms                                                         | 34.4 ms: 1.46x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 332 ms: 1.46x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 204 ms: 1.45x faster                                                             |
| go                         | 109 ms                                                          | 74.8 ms: 1.45x faster                                                            |
| json                       | 4.27 ms                                                         | 2.97 ms: 1.44x faster                                                            |
| async_tree_none            | 245 ms                                                          | 170 ms: 1.44x faster                                                             |
| pidigits                   | 201 ms                                                          | 145 ms: 1.39x faster                                                             |
| genshi_text                | 21.5 ms                                                         | 15.6 ms: 1.38x faster                                                            |
| pprint_pformat             | 1.33 sec                                                        | 977 ms: 1.36x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 209 ms: 1.35x faster                                                             |
| typing_runtime_protocols   | 138 us                                                          | 102 us: 1.35x faster                                                             |
| async_tree_io              | 526 ms                                                          | 391 ms: 1.34x faster                                                             |
| pprint_safe_repr           | 648 ms                                                          | 485 ms: 1.34x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 341 ms: 1.34x faster                                                             |
| logging_format             | 8.72 us                                                         | 6.60 us: 1.32x faster                                                            |
| logging_simple             | 7.99 us                                                         | 6.16 us: 1.30x faster                                                            |
| sympy_expand               | 373 ms                                                          | 289 ms: 1.29x faster                                                             |
| regex_compile              | 101 ms                                                          | 79.0 ms: 1.28x faster                                                            |
| regex_v8                   | 16.8 ms                                                         | 13.2 ms: 1.28x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 169 ms: 1.27x faster                                                             |
| tomli_loads                | 1.71 sec                                                        | 1.35 sec: 1.27x faster                                                           |
| float                      | 54.6 ms                                                         | 43.5 ms: 1.25x faster                                                            |
| chaos                      | 50.2 ms                                                         | 40.2 ms: 1.25x faster                                                            |
| pycparser                  | 872 ms                                                          | 698 ms: 1.25x faster                                                             |
| sympy_str                  | 212 ms                                                          | 170 ms: 1.25x faster                                                             |
| html5lib                   | 47.5 ms                                                         | 38.1 ms: 1.25x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 398 ms: 1.24x faster                                                             |
| sqlite_synth               | 1.95 us                                                         | 1.57 us: 1.24x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 86.6 ms: 1.24x faster                                                            |
| richards                   | 32.7 ms                                                         | 26.6 ms: 1.23x faster                                                            |
| nbody                      | 80.0 ms                                                         | 65.6 ms: 1.22x faster                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 39.2 ms: 1.22x faster                                                            |
| richards_super             | 36.7 ms                                                         | 30.3 ms: 1.21x faster                                                            |
| unpickle_pure_python       | 160 us                                                          | 132 us: 1.21x faster                                                             |
| sympy_sum                  | 106 ms                                                          | 87.3 ms: 1.21x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.49 ms: 1.21x faster                                                            |
| sympy_integrate            | 15.0 ms                                                         | 12.4 ms: 1.21x faster                                                            |
| dulwich_log                | 48.8 ms                                                         | 40.7 ms: 1.20x faster                                                            |
| crypto_pyaes               | 56.9 ms                                                         | 47.6 ms: 1.20x faster                                                            |
| bpe_tokeniser              | 3.46 sec                                                        | 2.91 sec: 1.19x faster                                                           |
| json_dumps                 | 7.30 ms                                                         | 6.13 ms: 1.19x faster                                                            |
| django_template            | 29.8 ms                                                         | 25.1 ms: 1.19x faster                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 847 us: 1.18x faster                                                             |
| async_generators           | 270 ms                                                          | 229 ms: 1.18x faster                                                             |
| nqueens                    | 72.1 ms                                                         | 61.4 ms: 1.17x faster                                                            |
| scimark_sor                | 85.9 ms                                                         | 73.3 ms: 1.17x faster                                                            |
| comprehensions             | 12.5 us                                                         | 10.7 us: 1.17x faster                                                            |
| fannkuch                   | 299 ms                                                          | 257 ms: 1.16x faster                                                             |
| scimark_fft                | 205 ms                                                          | 176 ms: 1.16x faster                                                             |
| pylint                     | 227 ms                                                          | 196 ms: 1.16x faster                                                             |
| xml_etree_process          | 44.2 ms                                                         | 38.8 ms: 1.14x faster                                                            |
| sphinx                     | 719 ms                                                          | 634 ms: 1.13x faster                                                             |
| 2to3                       | 250 ms                                                          | 221 ms: 1.13x faster                                                             |
| spectral_norm              | 69.4 ms                                                         | 61.2 ms: 1.13x faster                                                            |
| generators                 | 21.8 ms                                                         | 19.3 ms: 1.13x faster                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.52 ms: 1.13x faster                                                            |
| coroutines                 | 16.2 ms                                                         | 14.4 ms: 1.13x faster                                                            |
| pyflate                    | 320 ms                                                          | 287 ms: 1.12x faster                                                             |
| raytrace                   | 201 ms                                                          | 181 ms: 1.11x faster                                                             |
| pickle_pure_python         | 231 us                                                          | 208 us: 1.11x faster                                                             |
| xml_etree_generate         | 61.4 ms                                                         | 55.2 ms: 1.11x faster                                                            |
| docutils                   | 1.78 sec                                                        | 1.61 sec: 1.10x faster                                                           |
| hexiom                     | 4.44 ms                                                         | 4.04 ms: 1.10x faster                                                            |
| logging_silent             | 60.3 ns                                                         | 55.2 ns: 1.09x faster                                                            |
| mako                       | 7.09 ms                                                         | 6.52 ms: 1.09x faster                                                            |
| python_startup             | 28.3 ms                                                         | 26.1 ms: 1.08x faster                                                            |
| deltablue                  | 2.33 ms                                                         | 2.16 ms: 1.08x faster                                                            |
| scimark_lu                 | 60.2 ms                                                         | 57.2 ms: 1.05x faster                                                            |
| meteor_contest             | 74.6 ms                                                         | 71.4 ms: 1.05x faster                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 19.4 ms: 1.01x faster                                                            |
| many_optionals             | 436 us                                                          | 440 us: 1.01x slower                                                             |
| xml_etree_iterparse        | 62.6 ms                                                         | 63.6 ms: 1.02x slower                                                            |
| regex_dna                  | 114 ms                                                          | 116 ms: 1.02x slower                                                             |
| bench_mp_pool              | 90.6 ms                                                         | 94.2 ms: 1.04x slower                                                            |
| subparsers                 | 14.8 ms                                                         | 17.6 ms: 1.19x slower                                                            |
| gc_traversal               | 1.75 ms                                                         | 2.17 ms: 1.24x slower                                                            |
| k_core                     | 1.38 sec                                                        | 1.71 sec: 1.24x slower                                                           |
| shortest_path              | 290 ms                                                          | 360 ms: 1.24x slower                                                             |
| connected_components       | 267 ms                                                          | 332 ms: 1.24x slower                                                             |
| create_gc_cycles           | 1.06 ms                                                         | 1.34 ms: 1.27x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.28x faster                                                                     |
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250712-3.15.0a0-47b01da/bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.284x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: unknown