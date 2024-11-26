# Results vs. base

- fork: python
- ref: 9d08423b6e0fa89ce9cf
- machine: linux-aarch64
- commit hash: 9d08423
- commit date: 2024-11-09
- overall geometric mean: 1.082x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20241109-3.14.0a1+-9d08423/bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json | results/bm-20241109-3.14.0a1+-9d08423-JIT/bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 306 ms                                                                                                              | 398 ms: 1.30x slower                                                                                                    |
| docutils       | 3.13 sec                                                                                                            | 3.76 sec: 1.20x slower                                                                                                  |
| sphinx         | 1.24 sec                                                                                                            | 1.53 sec: 1.23x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                               | 1.19x slower                                                                                                            |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | results/bm-20241109-3.14.0a1+-9d08423/bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json | results/bm-20241109-3.14.0a1+-9d08423-JIT/bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json |
|------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| async_tree_none  | 458 ms                                                                                                              | 471 ms: 1.03x slower                                                                                                    |
| async_generators | 496 ms                                                                                                              | 532 ms: 1.07x slower                                                                                                    |
| Geometric mean   | (ref)                                                                                                               | 1.02x slower                                                                                                            |

Benchmark hidden because not significant (9): async_tree_memoization_tg, asyncio_websockets, async_tree_none_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_io, async_tree_cpu_io_mixed_tg, coroutines

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20241109-3.14.0a1+-9d08423/bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json | results/bm-20241109-3.14.0a1+-9d08423-JIT/bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 272 ms                                                                                                              | 257 ms: 1.06x faster                                                                                                    |
| regex_compile  | 130 ms                                                                                                              | 183 ms: 1.41x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.08x slower                                                                                                            |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark      | results/bm-20241109-3.14.0a1+-9d08423/bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json | results/bm-20241109-3.14.0a1+-9d08423-JIT/bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| tomli_loads    | 2.78 sec                                                                                                            | 2.63 sec: 1.06x faster                                                                                                  |
| Geometric mean | (ref)                                                                                                               | 1.00x faster                                                                                                            |

Benchmark hidden because not significant (8): json_dumps, xml_etree_process, json_loads, xml_etree_parse, xml_etree_generate, xml_etree_iterparse, unpickle_pure_python, pickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20241109-3.14.0a1+-9d08423/bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json | results/bm-20241109-3.14.0a1+-9d08423-JIT/bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json |
|-----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| django_template | 43.7 ms                                                                                                             | 51.2 ms: 1.17x slower                                                                                                   |
| genshi_text     | 28.8 ms                                                                                                             | 34.0 ms: 1.18x slower                                                                                                   |
| genshi_xml      | 61.7 ms                                                                                                             | 81.4 ms: 1.32x slower                                                                                                   |
| Geometric mean  | (ref)                                                                                                               | 1.14x slower                                                                                                            |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | results/bm-20241109-3.14.0a1+-9d08423/bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json | results/bm-20241109-3.14.0a1+-9d08423-JIT/bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json |
|--------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool            | 6.80 sec                                                                                                            | 1.91 sec: 3.56x faster                                                                                                  |
| regex_dna                | 272 ms                                                                                                              | 257 ms: 1.06x faster                                                                                                    |
| tomli_loads              | 2.78 sec                                                                                                            | 2.63 sec: 1.06x faster                                                                                                  |
| gc_traversal             | 6.75 ms                                                                                                             | 6.42 ms: 1.05x faster                                                                                                   |
| scimark_sor              | 165 ms                                                                                                              | 157 ms: 1.05x faster                                                                                                    |
| mdp                      | 3.51 sec                                                                                                            | 3.58 sec: 1.02x slower                                                                                                  |
| connected_components     | 545 ms                                                                                                              | 557 ms: 1.02x slower                                                                                                    |
| async_tree_none          | 458 ms                                                                                                              | 471 ms: 1.03x slower                                                                                                    |
| crypto_pyaes             | 84.3 ms                                                                                                             | 87.8 ms: 1.04x slower                                                                                                   |
| fannkuch                 | 491 ms                                                                                                              | 513 ms: 1.05x slower                                                                                                    |
| telco                    | 9.40 ms                                                                                                             | 9.88 ms: 1.05x slower                                                                                                   |
| logging_format           | 8.01 us                                                                                                             | 8.44 us: 1.05x slower                                                                                                   |
| bench_thread_pool        | 1.30 ms                                                                                                             | 1.40 ms: 1.07x slower                                                                                                   |
| async_generators         | 496 ms                                                                                                              | 532 ms: 1.07x slower                                                                                                    |
| scimark_sparse_mat_mult  | 6.82 ms                                                                                                             | 7.38 ms: 1.08x slower                                                                                                   |
| scimark_lu               | 140 ms                                                                                                              | 151 ms: 1.08x slower                                                                                                    |
| typing_runtime_protocols | 205 us                                                                                                              | 224 us: 1.10x slower                                                                                                    |
| richards_super           | 62.6 ms                                                                                                             | 69.9 ms: 1.12x slower                                                                                                   |
| sqlglot_parse            | 1.47 ms                                                                                                             | 1.66 ms: 1.13x slower                                                                                                   |
| raytrace                 | 320 ms                                                                                                              | 362 ms: 1.13x slower                                                                                                    |
| richards                 | 55.0 ms                                                                                                             | 63.3 ms: 1.15x slower                                                                                                   |
| deepcopy_reduce          | 3.59 us                                                                                                             | 4.16 us: 1.16x slower                                                                                                   |
| deepcopy                 | 355 us                                                                                                              | 412 us: 1.16x slower                                                                                                    |
| nqueens                  | 108 ms                                                                                                              | 127 ms: 1.17x slower                                                                                                    |
| pycparser                | 1.29 sec                                                                                                            | 1.50 sec: 1.17x slower                                                                                                  |
| comprehensions           | 21.2 us                                                                                                             | 24.8 us: 1.17x slower                                                                                                   |
| django_template          | 43.7 ms                                                                                                             | 51.2 ms: 1.17x slower                                                                                                   |
| chaos                    | 71.4 ms                                                                                                             | 83.8 ms: 1.17x slower                                                                                                   |
| genshi_text              | 28.8 ms                                                                                                             | 34.0 ms: 1.18x slower                                                                                                   |
| sqlglot_transpile        | 1.83 ms                                                                                                             | 2.18 ms: 1.19x slower                                                                                                   |
| docutils                 | 3.13 sec                                                                                                            | 3.76 sec: 1.20x slower                                                                                                  |
| sphinx                   | 1.24 sec                                                                                                            | 1.53 sec: 1.23x slower                                                                                                  |
| sqlglot_normalize        | 135 ms                                                                                                              | 167 ms: 1.24x slower                                                                                                    |
| go                       | 147 ms                                                                                                              | 187 ms: 1.27x slower                                                                                                    |
| sympy_str                | 283 ms                                                                                                              | 363 ms: 1.28x slower                                                                                                    |
| 2to3                     | 306 ms                                                                                                              | 398 ms: 1.30x slower                                                                                                    |
| pprint_safe_repr         | 966 ms                                                                                                              | 1.26 sec: 1.31x slower                                                                                                  |
| sqlglot_optimize         | 63.9 ms                                                                                                             | 83.6 ms: 1.31x slower                                                                                                   |
| sympy_expand             | 470 ms                                                                                                              | 616 ms: 1.31x slower                                                                                                    |
| genshi_xml               | 61.7 ms                                                                                                             | 81.4 ms: 1.32x slower                                                                                                   |
| pprint_pformat           | 1.99 sec                                                                                                            | 2.63 sec: 1.32x slower                                                                                                  |
| sqlalchemy_imperative    | 15.5 ms                                                                                                             | 20.6 ms: 1.33x slower                                                                                                   |
| hexiom                   | 7.56 ms                                                                                                             | 10.1 ms: 1.33x slower                                                                                                   |
| sympy_integrate          | 21.9 ms                                                                                                             | 29.3 ms: 1.34x slower                                                                                                   |
| sqlalchemy_declarative   | 148 ms                                                                                                              | 198 ms: 1.34x slower                                                                                                    |
| dulwich_log              | 60.8 ms                                                                                                             | 82.2 ms: 1.35x slower                                                                                                   |
| generators               | 35.8 ms                                                                                                             | 49.3 ms: 1.38x slower                                                                                                   |
| pylint                   | 365 ms                                                                                                              | 509 ms: 1.39x slower                                                                                                    |
| regex_compile            | 130 ms                                                                                                              | 183 ms: 1.41x slower                                                                                                    |
| sympy_sum                | 144 ms                                                                                                              | 212 ms: 1.47x slower                                                                                                    |
| Geometric mean           | (ref)                                                                                                               | 1.08x slower                                                                                                            |

Benchmark hidden because not significant (44): mako, logging_silent, nbody, sqlite_synth, json_dumps, float, xml_etree_process, create_gc_cycles, pathlib, json_loads, pyflate, scimark_fft, spectral_norm, bpe_tokeniser, k_core, xml_etree_parse, coverage, deepcopy_memo, async_tree_memoization_tg, asyncio_websockets, regex_effbot, python_startup, xml_etree_generate, async_tree_none_tg, shortest_path, xml_etree_iterparse, async_tree_memoization, async_tree_cpu_io_mixed, python_startup_no_site, async_tree_io_tg, unpickle_pure_python, json, async_tree_io, async_tree_cpu_io_mixed_tg, html5lib, thrift, coroutines, regex_v8, scimark_monte_carlo, pidigits, deltablue, pickle_pure_python, logging_simple, meteor_contest

- Geometric mean (including insignificant results): 1.082x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.06x