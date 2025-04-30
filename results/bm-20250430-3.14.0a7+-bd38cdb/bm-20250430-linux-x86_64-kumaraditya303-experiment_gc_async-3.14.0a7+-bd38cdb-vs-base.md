# Results vs. base

- fork: kumaraditya303
- ref: experiment_gc_async
- machine: linux-x86_64
- commit hash: bd38cdb
- commit date: 2025-04-30
- overall geometric mean: 1.025x slower
- HPT reliability: 99.72%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| docutils       | 2.61 sec                                                               | 2.63 sec: 1.00x slower                                                        |
| html5lib       | 61.3 ms                                                                | 60.2 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                  |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|----------------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_eager                 | 105 ms                                                                 | 103 ms: 1.02x faster                                                          |
| coroutines                       | 26.1 ms                                                                | 26.3 ms: 1.01x slower                                                         |
| async_tree_eager_memoization     | 204 ms                                                                 | 209 ms: 1.03x slower                                                          |
| async_tree_eager_cpu_io_mixed    | 384 ms                                                                 | 399 ms: 1.04x slower                                                          |
| async_tree_eager_tg              | 220 ms                                                                 | 240 ms: 1.09x slower                                                          |
| async_tree_eager_cpu_io_mixed_tg | 461 ms                                                                 | 510 ms: 1.11x slower                                                          |
| async_tree_eager_memoization_tg  | 285 ms                                                                 | 318 ms: 1.12x slower                                                          |
| async_tree_cpu_io_mixed          | 493 ms                                                                 | 574 ms: 1.16x slower                                                          |
| async_tree_cpu_io_mixed_tg       | 488 ms                                                                 | 580 ms: 1.19x slower                                                          |
| async_tree_eager_io              | 626 ms                                                                 | 755 ms: 1.21x slower                                                          |
| async_tree_memoization           | 314 ms                                                                 | 384 ms: 1.22x slower                                                          |
| async_tree_none                  | 261 ms                                                                 | 320 ms: 1.23x slower                                                          |
| async_tree_eager_io_tg           | 624 ms                                                                 | 785 ms: 1.26x slower                                                          |
| async_tree_memoization_tg        | 309 ms                                                                 | 391 ms: 1.26x slower                                                          |
| async_tree_none_tg               | 254 ms                                                                 | 324 ms: 1.28x slower                                                          |
| async_tree_io                    | 596 ms                                                                 | 804 ms: 1.35x slower                                                          |
| async_tree_io_tg                 | 611 ms                                                                 | 832 ms: 1.36x slower                                                          |
| Geometric mean                   | (ref)                                                                  | 1.15x slower                                                                  |

Benchmark hidden because not significant (2): asyncio_websockets, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 102 ms                                                                 | 99.2 ms: 1.03x faster                                                         |
| pidigits       | 195 ms                                                                 | 191 ms: 1.02x faster                                                          |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                                  |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 3.20 ms                                                                | 3.11 ms: 1.03x faster                                                         |
| regex_dna      | 210 ms                                                                 | 207 ms: 1.01x faster                                                          |
| regex_compile  | 128 ms                                                                 | 127 ms: 1.00x faster                                                          |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                  |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|--------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| xml_etree_process  | 59.9 ms                                                                | 59.2 ms: 1.01x faster                                                         |
| xml_etree_generate | 85.7 ms                                                                | 84.9 ms: 1.01x faster                                                         |
| xml_etree_parse    | 143 ms                                                                 | 142 ms: 1.01x faster                                                          |
| json_loads         | 30.7 us                                                                | 30.5 us: 1.01x faster                                                         |
| tomli_loads        | 2.03 sec                                                               | 2.05 sec: 1.01x slower                                                        |
| json_dumps         | 11.8 ms                                                                | 12.2 ms: 1.03x slower                                                         |
| Geometric mean     | (ref)                                                                  | 1.00x faster                                                                  |

Benchmark hidden because not significant (3): unpickle_pure_python, xml_etree_iterparse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 6.95 ms                                                                | 6.93 ms: 1.00x faster                                                         |
| python_startup         | 13.2 ms                                                                | 13.1 ms: 1.00x faster                                                         |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|-----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_text     | 21.1 ms                                                                | 21.1 ms: 1.00x slower                                                         |
| genshi_xml      | 49.3 ms                                                                | 50.4 ms: 1.02x slower                                                         |
| django_template | 32.3 ms                                                                | 33.1 ms: 1.03x slower                                                         |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                                  |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                        | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|----------------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| gc_traversal                     | 4.99 ms                                                                | 4.78 ms: 1.04x faster                                                         |
| regex_effbot                     | 3.20 ms                                                                | 3.11 ms: 1.03x faster                                                         |
| scimark_fft                      | 380 ms                                                                 | 369 ms: 1.03x faster                                                          |
| nbody                            | 102 ms                                                                 | 99.2 ms: 1.03x faster                                                         |
| html5lib                         | 61.3 ms                                                                | 60.2 ms: 1.02x faster                                                         |
| async_tree_eager                 | 105 ms                                                                 | 103 ms: 1.02x faster                                                          |
| scimark_sor                      | 124 ms                                                                 | 121 ms: 1.02x faster                                                          |
| coverage                         | 93.2 ms                                                                | 91.5 ms: 1.02x faster                                                         |
| pidigits                         | 195 ms                                                                 | 191 ms: 1.02x faster                                                          |
| mdp                              | 1.24 sec                                                               | 1.22 sec: 1.02x faster                                                        |
| scimark_sparse_mat_mult          | 5.27 ms                                                                | 5.19 ms: 1.02x faster                                                         |
| json                             | 5.56 ms                                                                | 5.49 ms: 1.01x faster                                                         |
| regex_dna                        | 210 ms                                                                 | 207 ms: 1.01x faster                                                          |
| xml_etree_process                | 59.9 ms                                                                | 59.2 ms: 1.01x faster                                                         |
| logging_format                   | 6.32 us                                                                | 6.25 us: 1.01x faster                                                         |
| fannkuch                         | 425 ms                                                                 | 421 ms: 1.01x faster                                                          |
| create_gc_cycles                 | 2.49 ms                                                                | 2.47 ms: 1.01x faster                                                         |
| xml_etree_generate               | 85.7 ms                                                                | 84.9 ms: 1.01x faster                                                         |
| telco                            | 8.01 ms                                                                | 7.95 ms: 1.01x faster                                                         |
| xml_etree_parse                  | 143 ms                                                                 | 142 ms: 1.01x faster                                                          |
| hexiom                           | 6.29 ms                                                                | 6.25 ms: 1.01x faster                                                         |
| bpe_tokeniser                    | 4.60 sec                                                               | 4.57 sec: 1.01x faster                                                        |
| sympy_sum                        | 150 ms                                                                 | 149 ms: 1.01x faster                                                          |
| chaos                            | 60.0 ms                                                                | 59.6 ms: 1.01x faster                                                         |
| json_loads                       | 30.7 us                                                                | 30.5 us: 1.01x faster                                                         |
| many_optionals                   | 940 us                                                                 | 935 us: 1.00x faster                                                          |
| comprehensions                   | 17.1 us                                                                | 17.0 us: 1.00x faster                                                         |
| spectral_norm                    | 108 ms                                                                 | 108 ms: 1.00x faster                                                          |
| regex_compile                    | 128 ms                                                                 | 127 ms: 1.00x faster                                                          |
| python_startup_no_site           | 6.95 ms                                                                | 6.93 ms: 1.00x faster                                                         |
| meteor_contest                   | 107 ms                                                                 | 107 ms: 1.00x faster                                                          |
| python_startup                   | 13.2 ms                                                                | 13.1 ms: 1.00x faster                                                         |
| sqlalchemy_declarative           | 133 ms                                                                 | 133 ms: 1.00x slower                                                          |
| crypto_pyaes                     | 76.1 ms                                                                | 76.3 ms: 1.00x slower                                                         |
| sympy_str                        | 269 ms                                                                 | 270 ms: 1.00x slower                                                          |
| pprint_pformat                   | 1.49 sec                                                               | 1.50 sec: 1.00x slower                                                        |
| genshi_text                      | 21.1 ms                                                                | 21.1 ms: 1.00x slower                                                         |
| sympy_expand                     | 461 ms                                                                 | 463 ms: 1.00x slower                                                          |
| sympy_integrate                  | 19.1 ms                                                                | 19.2 ms: 1.00x slower                                                         |
| docutils                         | 2.61 sec                                                               | 2.63 sec: 1.00x slower                                                        |
| deltablue                        | 3.31 ms                                                                | 3.33 ms: 1.01x slower                                                         |
| coroutines                       | 26.1 ms                                                                | 26.3 ms: 1.01x slower                                                         |
| generators                       | 29.2 ms                                                                | 29.4 ms: 1.01x slower                                                         |
| connected_components             | 449 ms                                                                 | 453 ms: 1.01x slower                                                          |
| raytrace                         | 267 ms                                                                 | 269 ms: 1.01x slower                                                          |
| pprint_safe_repr                 | 733 ms                                                                 | 741 ms: 1.01x slower                                                          |
| tomli_loads                      | 2.03 sec                                                               | 2.05 sec: 1.01x slower                                                        |
| richards                         | 42.8 ms                                                                | 43.4 ms: 1.01x slower                                                         |
| shortest_path                    | 492 ms                                                                 | 499 ms: 1.01x slower                                                          |
| nqueens                          | 81.9 ms                                                                | 83.1 ms: 1.01x slower                                                         |
| sqlglot_v2_optimize              | 53.0 ms                                                                | 53.7 ms: 1.01x slower                                                         |
| deepcopy                         | 255 us                                                                 | 260 us: 1.02x slower                                                          |
| genshi_xml                       | 49.3 ms                                                                | 50.4 ms: 1.02x slower                                                         |
| sqlglot_v2_normalize             | 107 ms                                                                 | 110 ms: 1.03x slower                                                          |
| async_tree_eager_memoization     | 204 ms                                                                 | 209 ms: 1.03x slower                                                          |
| django_template                  | 32.3 ms                                                                | 33.1 ms: 1.03x slower                                                         |
| pathlib                          | 16.9 ms                                                                | 17.4 ms: 1.03x slower                                                         |
| json_dumps                       | 11.8 ms                                                                | 12.2 ms: 1.03x slower                                                         |
| logging_silent                   | 96.5 ns                                                                | 100 ns: 1.04x slower                                                          |
| async_tree_eager_cpu_io_mixed    | 384 ms                                                                 | 399 ms: 1.04x slower                                                          |
| async_tree_eager_tg              | 220 ms                                                                 | 240 ms: 1.09x slower                                                          |
| async_tree_eager_cpu_io_mixed_tg | 461 ms                                                                 | 510 ms: 1.11x slower                                                          |
| async_tree_eager_memoization_tg  | 285 ms                                                                 | 318 ms: 1.12x slower                                                          |
| async_tree_cpu_io_mixed          | 493 ms                                                                 | 574 ms: 1.16x slower                                                          |
| async_tree_cpu_io_mixed_tg       | 488 ms                                                                 | 580 ms: 1.19x slower                                                          |
| async_tree_eager_io              | 626 ms                                                                 | 755 ms: 1.21x slower                                                          |
| async_tree_memoization           | 314 ms                                                                 | 384 ms: 1.22x slower                                                          |
| async_tree_none                  | 261 ms                                                                 | 320 ms: 1.23x slower                                                          |
| async_tree_eager_io_tg           | 624 ms                                                                 | 785 ms: 1.26x slower                                                          |
| async_tree_memoization_tg        | 309 ms                                                                 | 391 ms: 1.26x slower                                                          |
| async_tree_none_tg               | 254 ms                                                                 | 324 ms: 1.28x slower                                                          |
| async_tree_io                    | 596 ms                                                                 | 804 ms: 1.35x slower                                                          |
| async_tree_io_tg                 | 611 ms                                                                 | 832 ms: 1.36x slower                                                          |
| Geometric mean                   | (ref)                                                                  | 1.02x slower                                                                  |

Benchmark hidden because not significant (30): unpickle_pure_python, float, xml_etree_iterparse, scimark_lu, scimark_monte_carlo, sqlglot_v2_parse, sqlite_synth, bench_mp_pool, bench_thread_pool, regex_v8, dulwich_log, pickle_pure_python, subparsers, mako, sqlalchemy_imperative, go, typing_runtime_protocols, asyncio_websockets, 2to3, sqlglot_v2_transpile, sphinx, pyflate, deepcopy_memo, k_core, async_generators, logging_simple, deepcopy_reduce, pycparser, pylint, richards_super

- Geometric mean (including insignificant results): 1.025x slower

# HPT report

- Reliability score: 99.72% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x