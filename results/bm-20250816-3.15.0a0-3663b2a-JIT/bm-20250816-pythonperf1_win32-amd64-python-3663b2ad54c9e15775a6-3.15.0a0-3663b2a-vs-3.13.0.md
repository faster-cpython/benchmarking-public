# Results vs. 3.13.0

- fork: python
- ref: 3663b2ad54c9e15775a6
- machine: windows-amd64
- commit hash: 3663b2a
- commit date: 2025-08-16
- overall geometric mean: 1.313x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 216 ms: 1.16x faster                                                             |
| docutils       | 1.78 sec                                                        | 1.62 sec: 1.09x faster                                                           |
| html5lib       | 47.5 ms                                                         | 37.8 ms: 1.26x faster                                                            |
| sphinx         | 719 ms                                                          | 626 ms: 1.15x faster                                                             |
| Geometric mean | (ref)                                                           | 1.16x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 158 ms: 2.30x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 330 ms: 1.47x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 204 ms: 1.46x faster                                                             |
| async_tree_none            | 245 ms                                                          | 172 ms: 1.43x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 336 ms: 1.36x faster                                                             |
| async_tree_io              | 526 ms                                                          | 389 ms: 1.35x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 213 ms: 1.33x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 382 ms: 1.30x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 166 ms: 1.29x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 13.8 ms: 1.18x faster                                                            |
| async_generators           | 270 ms                                                          | 238 ms: 1.13x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.39x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 80.0 ms                                                         | 54.6 ms: 1.46x faster                                                            |
| pidigits       | 201 ms                                                          | 145 ms: 1.39x faster                                                             |
| float          | 54.6 ms                                                         | 43.9 ms: 1.24x faster                                                            |
| Geometric mean | (ref)                                                           | 1.36x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 78.0 ms: 1.29x faster                                                            |
| regex_v8       | 16.8 ms                                                         | 13.1 ms: 1.29x faster                                                            |
| regex_effbot   | 1.80 ms                                                         | 1.52 ms: 1.18x faster                                                            |
| Geometric mean | (ref)                                                           | 1.18x faster                                                                     |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 1.71 sec                                                        | 1.10 sec: 1.55x faster                                                           |
| unpickle_pure_python | 160 us                                                          | 105 us: 1.52x faster                                                             |
| json_loads           | 21.6 us                                                         | 14.2 us: 1.52x faster                                                            |
| json_dumps           | 7.30 ms                                                         | 5.39 ms: 1.35x faster                                                            |
| xml_etree_process    | 44.2 ms                                                         | 35.2 ms: 1.26x faster                                                            |
| xml_etree_parse      | 107 ms                                                          | 87.7 ms: 1.22x faster                                                            |
| xml_etree_generate   | 61.4 ms                                                         | 50.2 ms: 1.22x faster                                                            |
| pickle_pure_python   | 231 us                                                          | 199 us: 1.16x faster                                                             |
| xml_etree_iterparse  | 62.6 ms                                                         | 61.1 ms: 1.02x faster                                                            |
| Geometric mean       | (ref)                                                           | 1.30x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 25.3 ms: 1.12x faster                                                            |
| python_startup_no_site | 19.7 ms                                                         | 19.1 ms: 1.03x faster                                                            |
| Geometric mean         | (ref)                                                           | 1.07x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 34.9 ms: 1.44x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 15.7 ms: 1.37x faster                                                            |
| mako            | 7.09 ms                                                         | 5.20 ms: 1.36x faster                                                            |
| django_template | 29.8 ms                                                         | 23.9 ms: 1.25x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.35x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 495 us: 20.18x faster                                                            |
| coverage                   | 324 ms                                                          | 49.7 ms: 6.52x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 29.1 ms: 2.85x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 158 ms: 2.30x faster                                                             |
| mdp                        | 1.62 sec                                                        | 801 ms: 2.03x faster                                                             |
| deepcopy                   | 314 us                                                          | 168 us: 1.87x faster                                                             |
| telco                      | 6.96 ms                                                         | 3.94 ms: 1.77x faster                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 1.83 us: 1.59x faster                                                            |
| tomli_loads                | 1.71 sec                                                        | 1.10 sec: 1.55x faster                                                           |
| unpickle_pure_python       | 160 us                                                          | 105 us: 1.52x faster                                                             |
| json_loads                 | 21.6 us                                                         | 14.2 us: 1.52x faster                                                            |
| pprint_pformat             | 1.33 sec                                                        | 891 ms: 1.49x faster                                                             |
| pprint_safe_repr           | 648 ms                                                          | 436 ms: 1.49x faster                                                             |
| json                       | 4.27 ms                                                         | 2.89 ms: 1.48x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 330 ms: 1.47x faster                                                             |
| nbody                      | 80.0 ms                                                         | 54.6 ms: 1.46x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 204 ms: 1.46x faster                                                             |
| fannkuch                   | 299 ms                                                          | 207 ms: 1.44x faster                                                             |
| genshi_xml                 | 50.1 ms                                                         | 34.9 ms: 1.44x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 17.8 us: 1.43x faster                                                            |
| async_tree_none            | 245 ms                                                          | 172 ms: 1.43x faster                                                             |
| go                         | 109 ms                                                          | 77.2 ms: 1.41x faster                                                            |
| bpe_tokeniser              | 3.46 sec                                                        | 2.49 sec: 1.39x faster                                                           |
| pidigits                   | 201 ms                                                          | 145 ms: 1.39x faster                                                             |
| scimark_fft                | 205 ms                                                          | 149 ms: 1.38x faster                                                             |
| genshi_text                | 21.5 ms                                                         | 15.7 ms: 1.37x faster                                                            |
| mako                       | 7.09 ms                                                         | 5.20 ms: 1.36x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 336 ms: 1.36x faster                                                             |
| json_dumps                 | 7.30 ms                                                         | 5.39 ms: 1.35x faster                                                            |
| async_tree_io              | 526 ms                                                          | 389 ms: 1.35x faster                                                             |
| logging_format             | 8.72 us                                                         | 6.47 us: 1.35x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 213 ms: 1.33x faster                                                             |
| logging_simple             | 7.99 us                                                         | 6.04 us: 1.32x faster                                                            |
| typing_runtime_protocols   | 138 us                                                          | 104 us: 1.32x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 382 ms: 1.30x faster                                                             |
| regex_compile              | 101 ms                                                          | 78.0 ms: 1.29x faster                                                            |
| sqlite_synth               | 1.95 us                                                         | 1.51 us: 1.29x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 166 ms: 1.29x faster                                                             |
| regex_v8                   | 16.8 ms                                                         | 13.1 ms: 1.29x faster                                                            |
| sympy_expand               | 373 ms                                                          | 290 ms: 1.29x faster                                                             |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.21 ms: 1.28x faster                                                            |
| crypto_pyaes               | 56.9 ms                                                         | 44.8 ms: 1.27x faster                                                            |
| pycparser                  | 872 ms                                                          | 688 ms: 1.27x faster                                                             |
| dulwich_log                | 48.8 ms                                                         | 38.7 ms: 1.26x faster                                                            |
| html5lib                   | 47.5 ms                                                         | 37.8 ms: 1.26x faster                                                            |
| sympy_str                  | 212 ms                                                          | 168 ms: 1.26x faster                                                             |
| xml_etree_process          | 44.2 ms                                                         | 35.2 ms: 1.26x faster                                                            |
| chaos                      | 50.2 ms                                                         | 40.2 ms: 1.25x faster                                                            |
| django_template            | 29.8 ms                                                         | 23.9 ms: 1.25x faster                                                            |
| float                      | 54.6 ms                                                         | 43.9 ms: 1.24x faster                                                            |
| pyflate                    | 320 ms                                                          | 260 ms: 1.23x faster                                                             |
| sympy_sum                  | 106 ms                                                          | 85.7 ms: 1.23x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 87.7 ms: 1.22x faster                                                            |
| xml_etree_generate         | 61.4 ms                                                         | 50.2 ms: 1.22x faster                                                            |
| richards                   | 32.7 ms                                                         | 26.9 ms: 1.21x faster                                                            |
| sympy_integrate            | 15.0 ms                                                         | 12.4 ms: 1.21x faster                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 833 us: 1.20x faster                                                             |
| nqueens                    | 72.1 ms                                                         | 60.0 ms: 1.20x faster                                                            |
| richards_super             | 36.7 ms                                                         | 30.6 ms: 1.20x faster                                                            |
| comprehensions             | 12.5 us                                                         | 10.5 us: 1.19x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.52 ms: 1.18x faster                                                            |
| coroutines                 | 16.2 ms                                                         | 13.8 ms: 1.18x faster                                                            |
| pylint                     | 227 ms                                                          | 194 ms: 1.17x faster                                                             |
| pickle_pure_python         | 231 us                                                          | 199 us: 1.16x faster                                                             |
| 2to3                       | 250 ms                                                          | 216 ms: 1.16x faster                                                             |
| generators                 | 21.8 ms                                                         | 18.9 ms: 1.15x faster                                                            |
| sphinx                     | 719 ms                                                          | 626 ms: 1.15x faster                                                             |
| async_generators           | 270 ms                                                          | 238 ms: 1.13x faster                                                             |
| raytrace                   | 201 ms                                                          | 178 ms: 1.13x faster                                                             |
| scimark_monte_carlo        | 47.7 ms                                                         | 42.1 ms: 1.13x faster                                                            |
| python_startup             | 28.3 ms                                                         | 25.3 ms: 1.12x faster                                                            |
| hexiom                     | 4.44 ms                                                         | 3.99 ms: 1.11x faster                                                            |
| scimark_sor                | 85.9 ms                                                         | 78.2 ms: 1.10x faster                                                            |
| docutils                   | 1.78 sec                                                        | 1.62 sec: 1.09x faster                                                           |
| logging_silent             | 60.3 ns                                                         | 55.2 ns: 1.09x faster                                                            |
| meteor_contest             | 74.6 ms                                                         | 69.1 ms: 1.08x faster                                                            |
| spectral_norm              | 69.4 ms                                                         | 65.7 ms: 1.06x faster                                                            |
| deltablue                  | 2.33 ms                                                         | 2.22 ms: 1.05x faster                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 19.1 ms: 1.03x faster                                                            |
| scimark_lu                 | 60.2 ms                                                         | 58.6 ms: 1.03x faster                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 61.1 ms: 1.02x faster                                                            |
| bench_mp_pool              | 90.6 ms                                                         | 92.8 ms: 1.02x slower                                                            |
| k_core                     | 1.38 sec                                                        | 1.59 sec: 1.16x slower                                                           |
| connected_components       | 267 ms                                                          | 317 ms: 1.19x slower                                                             |
| shortest_path              | 290 ms                                                          | 350 ms: 1.21x slower                                                             |
| create_gc_cycles           | 1.06 ms                                                         | 1.31 ms: 1.24x slower                                                            |
| gc_traversal               | 1.75 ms                                                         | 2.20 ms: 1.26x slower                                                            |
| many_optionals             | 436 us                                                          | 561 us: 1.29x slower                                                             |
| subparsers                 | 14.8 ms                                                         | 29.8 ms: 2.02x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.31x faster                                                                     |

Benchmark hidden because not significant (1): regex_dna
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250816-3.15.0a0-3663b2a-JIT/bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.313x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: unknown