# Results vs. base

- fork: kumaraditya303
- ref: experiment_gc_async
- machine: linux-x86_64
- commit hash: a8a0e1d
- commit date: 2025-05-03
- overall geometric mean: 1.027x slower
- HPT reliability: 99.75%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250503-linux-x86_64-python-1550c30fd5f2f2902bbc-3.14.0a7+-1550c30 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| docutils       | 2.61 sec                                                               | 2.62 sec: 1.00x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                  |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250503-linux-x86_64-python-1550c30fd5f2f2902bbc-3.14.0a7+-1550c30 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|----------------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| coroutines                       | 25.5 ms                                                                | 25.8 ms: 1.01x slower                                                         |
| async_generators                 | 406 ms                                                                 | 413 ms: 1.02x slower                                                          |
| async_tree_eager_memoization     | 202 ms                                                                 | 209 ms: 1.03x slower                                                          |
| async_tree_eager_cpu_io_mixed_tg | 466 ms                                                                 | 488 ms: 1.05x slower                                                          |
| async_tree_eager_tg              | 218 ms                                                                 | 239 ms: 1.10x slower                                                          |
| async_tree_eager_memoization_tg  | 282 ms                                                                 | 316 ms: 1.12x slower                                                          |
| async_tree_cpu_io_mixed          | 499 ms                                                                 | 561 ms: 1.12x slower                                                          |
| async_tree_cpu_io_mixed_tg       | 492 ms                                                                 | 567 ms: 1.15x slower                                                          |
| async_tree_eager_io              | 624 ms                                                                 | 754 ms: 1.21x slower                                                          |
| async_tree_memoization           | 313 ms                                                                 | 383 ms: 1.23x slower                                                          |
| async_tree_none                  | 259 ms                                                                 | 321 ms: 1.24x slower                                                          |
| async_tree_memoization_tg        | 307 ms                                                                 | 386 ms: 1.26x slower                                                          |
| async_tree_eager_io_tg           | 615 ms                                                                 | 781 ms: 1.27x slower                                                          |
| async_tree_none_tg               | 250 ms                                                                 | 322 ms: 1.29x slower                                                          |
| async_tree_io                    | 596 ms                                                                 | 804 ms: 1.35x slower                                                          |
| async_tree_io_tg                 | 608 ms                                                                 | 824 ms: 1.36x slower                                                          |
| Geometric mean                   | (ref)                                                                  | 1.14x slower                                                                  |

Benchmark hidden because not significant (3): async_tree_eager_cpu_io_mixed, asyncio_websockets, async_tree_eager

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250503-linux-x86_64-python-1550c30fd5f2f2902bbc-3.14.0a7+-1550c30 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 103 ms                                                                 | 96.3 ms: 1.06x faster                                                         |
| pidigits       | 187 ms                                                                 | 187 ms: 1.00x faster                                                          |
| float          | 70.3 ms                                                                | 71.1 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250503-linux-x86_64-python-1550c30fd5f2f2902bbc-3.14.0a7+-1550c30 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_v8       | 22.8 ms                                                                | 22.8 ms: 1.00x faster                                                         |
| regex_dna      | 205 ms                                                                 | 207 ms: 1.01x slower                                                          |
| regex_compile  | 126 ms                                                                 | 127 ms: 1.01x slower                                                          |
| regex_effbot   | 3.30 ms                                                                | 3.33 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250503-linux-x86_64-python-1550c30fd5f2f2902bbc-3.14.0a7+-1550c30 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|---------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| json_dumps          | 12.0 ms                                                                | 11.8 ms: 1.01x faster                                                         |
| xml_etree_process   | 59.2 ms                                                                | 59.8 ms: 1.01x slower                                                         |
| xml_etree_generate  | 85.2 ms                                                                | 86.1 ms: 1.01x slower                                                         |
| xml_etree_iterparse | 98.8 ms                                                                | 99.8 ms: 1.01x slower                                                         |
| tomli_loads         | 1.97 sec                                                               | 2.02 sec: 1.03x slower                                                        |
| xml_etree_parse     | 142 ms                                                                 | 145 ms: 1.03x slower                                                          |
| Geometric mean      | (ref)                                                                  | 1.01x slower                                                                  |

Benchmark hidden because not significant (3): json_loads, unpickle_pure_python, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250503-linux-x86_64-python-1550c30fd5f2f2902bbc-3.14.0a7+-1550c30 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 13.1 ms                                                                | 13.2 ms: 1.01x slower                                                         |
| python_startup_no_site | 6.91 ms                                                                | 6.95 ms: 1.01x slower                                                         |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250503-linux-x86_64-python-1550c30fd5f2f2902bbc-3.14.0a7+-1550c30 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|-----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| django_template | 32.3 ms                                                                | 31.8 ms: 1.02x faster                                                         |
| mako            | 11.7 ms                                                                | 11.8 ms: 1.01x slower                                                         |
| genshi_text     | 21.0 ms                                                                | 21.2 ms: 1.01x slower                                                         |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                                  |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                        | bm-20250503-linux-x86_64-python-1550c30fd5f2f2902bbc-3.14.0a7+-1550c30 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|----------------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody                            | 103 ms                                                                 | 96.3 ms: 1.06x faster                                                         |
| deepcopy_reduce                  | 2.84 us                                                                | 2.76 us: 1.03x faster                                                         |
| pyflate                          | 438 ms                                                                 | 426 ms: 1.03x faster                                                          |
| shortest_path                    | 501 ms                                                                 | 488 ms: 1.02x faster                                                          |
| connected_components             | 464 ms                                                                 | 454 ms: 1.02x faster                                                          |
| spectral_norm                    | 110 ms                                                                 | 108 ms: 1.02x faster                                                          |
| django_template                  | 32.3 ms                                                                | 31.8 ms: 1.02x faster                                                         |
| pathlib                          | 17.1 ms                                                                | 16.9 ms: 1.01x faster                                                         |
| json_dumps                       | 12.0 ms                                                                | 11.8 ms: 1.01x faster                                                         |
| pprint_safe_repr                 | 738 ms                                                                 | 730 ms: 1.01x faster                                                          |
| pprint_pformat                   | 1.49 sec                                                               | 1.48 sec: 1.01x faster                                                        |
| sympy_expand                     | 456 ms                                                                 | 454 ms: 1.01x faster                                                          |
| sqlalchemy_declarative           | 133 ms                                                                 | 133 ms: 1.01x faster                                                          |
| mdp                              | 1.23 sec                                                               | 1.23 sec: 1.01x faster                                                        |
| sqlglot_v2_normalize             | 106 ms                                                                 | 106 ms: 1.00x faster                                                          |
| sympy_str                        | 267 ms                                                                 | 267 ms: 1.00x faster                                                          |
| regex_v8                         | 22.8 ms                                                                | 22.8 ms: 1.00x faster                                                         |
| pidigits                         | 187 ms                                                                 | 187 ms: 1.00x faster                                                          |
| docutils                         | 2.61 sec                                                               | 2.62 sec: 1.00x slower                                                        |
| meteor_contest                   | 107 ms                                                                 | 107 ms: 1.00x slower                                                          |
| scimark_fft                      | 368 ms                                                                 | 369 ms: 1.00x slower                                                          |
| sqlglot_v2_transpile             | 1.54 ms                                                                | 1.55 ms: 1.01x slower                                                         |
| mako                             | 11.7 ms                                                                | 11.8 ms: 1.01x slower                                                         |
| sqlglot_v2_parse                 | 1.24 ms                                                                | 1.25 ms: 1.01x slower                                                         |
| genshi_text                      | 21.0 ms                                                                | 21.2 ms: 1.01x slower                                                         |
| python_startup                   | 13.1 ms                                                                | 13.2 ms: 1.01x slower                                                         |
| deltablue                        | 3.36 ms                                                                | 3.38 ms: 1.01x slower                                                         |
| python_startup_no_site           | 6.91 ms                                                                | 6.95 ms: 1.01x slower                                                         |
| regex_dna                        | 205 ms                                                                 | 207 ms: 1.01x slower                                                          |
| scimark_monte_carlo              | 67.2 ms                                                                | 67.7 ms: 1.01x slower                                                         |
| logging_format                   | 6.22 us                                                                | 6.26 us: 1.01x slower                                                         |
| regex_compile                    | 126 ms                                                                 | 127 ms: 1.01x slower                                                          |
| chaos                            | 59.0 ms                                                                | 59.5 ms: 1.01x slower                                                         |
| regex_effbot                     | 3.30 ms                                                                | 3.33 ms: 1.01x slower                                                         |
| xml_etree_process                | 59.2 ms                                                                | 59.8 ms: 1.01x slower                                                         |
| sqlite_synth                     | 2.84 us                                                                | 2.87 us: 1.01x slower                                                         |
| dulwich_log                      | 59.3 ms                                                                | 59.9 ms: 1.01x slower                                                         |
| xml_etree_generate               | 85.2 ms                                                                | 86.1 ms: 1.01x slower                                                         |
| raytrace                         | 269 ms                                                                 | 272 ms: 1.01x slower                                                          |
| xml_etree_iterparse              | 98.8 ms                                                                | 99.8 ms: 1.01x slower                                                         |
| create_gc_cycles                 | 2.48 ms                                                                | 2.51 ms: 1.01x slower                                                         |
| typing_runtime_protocols         | 164 us                                                                 | 166 us: 1.01x slower                                                          |
| float                            | 70.3 ms                                                                | 71.1 ms: 1.01x slower                                                         |
| fannkuch                         | 405 ms                                                                 | 410 ms: 1.01x slower                                                          |
| deepcopy_memo                    | 29.2 us                                                                | 29.6 us: 1.01x slower                                                         |
| bench_mp_pool                    | 82.4 ms                                                                | 83.5 ms: 1.01x slower                                                         |
| scimark_sparse_mat_mult          | 5.07 ms                                                                | 5.14 ms: 1.01x slower                                                         |
| coroutines                       | 25.5 ms                                                                | 25.8 ms: 1.01x slower                                                         |
| comprehensions                   | 16.9 us                                                                | 17.2 us: 1.01x slower                                                         |
| go                               | 111 ms                                                                 | 113 ms: 1.02x slower                                                          |
| async_generators                 | 406 ms                                                                 | 413 ms: 1.02x slower                                                          |
| hexiom                           | 6.20 ms                                                                | 6.32 ms: 1.02x slower                                                         |
| tomli_loads                      | 1.97 sec                                                               | 2.02 sec: 1.03x slower                                                        |
| xml_etree_parse                  | 142 ms                                                                 | 145 ms: 1.03x slower                                                          |
| async_tree_eager_memoization     | 202 ms                                                                 | 209 ms: 1.03x slower                                                          |
| richards_super                   | 48.8 ms                                                                | 50.5 ms: 1.03x slower                                                         |
| logging_silent                   | 96.0 ns                                                                | 99.4 ns: 1.04x slower                                                         |
| richards                         | 42.9 ms                                                                | 44.4 ms: 1.04x slower                                                         |
| async_tree_eager_cpu_io_mixed_tg | 466 ms                                                                 | 488 ms: 1.05x slower                                                          |
| gc_traversal                     | 4.62 ms                                                                | 5.01 ms: 1.08x slower                                                         |
| async_tree_eager_tg              | 218 ms                                                                 | 239 ms: 1.10x slower                                                          |
| async_tree_eager_memoization_tg  | 282 ms                                                                 | 316 ms: 1.12x slower                                                          |
| async_tree_cpu_io_mixed          | 499 ms                                                                 | 561 ms: 1.12x slower                                                          |
| async_tree_cpu_io_mixed_tg       | 492 ms                                                                 | 567 ms: 1.15x slower                                                          |
| async_tree_eager_io              | 624 ms                                                                 | 754 ms: 1.21x slower                                                          |
| async_tree_memoization           | 313 ms                                                                 | 383 ms: 1.23x slower                                                          |
| async_tree_none                  | 259 ms                                                                 | 321 ms: 1.24x slower                                                          |
| async_tree_memoization_tg        | 307 ms                                                                 | 386 ms: 1.26x slower                                                          |
| async_tree_eager_io_tg           | 615 ms                                                                 | 781 ms: 1.27x slower                                                          |
| async_tree_none_tg               | 250 ms                                                                 | 322 ms: 1.29x slower                                                          |
| async_tree_io                    | 596 ms                                                                 | 804 ms: 1.35x slower                                                          |
| async_tree_io_tg                 | 608 ms                                                                 | 824 ms: 1.36x slower                                                          |
| Geometric mean                   | (ref)                                                                  | 1.03x slower                                                                  |

Benchmark hidden because not significant (31): json, json_loads, pycparser, scimark_lu, async_tree_eager_cpu_io_mixed, genshi_xml, k_core, telco, asyncio_websockets, crypto_pyaes, sqlglot_v2_optimize, subparsers, nqueens, 2to3, unpickle_pure_python, bench_thread_pool, sympy_integrate, logging_simple, pickle_pure_python, bpe_tokeniser, generators, many_optionals, sqlalchemy_imperative, sympy_sum, deepcopy, sphinx, async_tree_eager, html5lib, pylint, scimark_sor, coverage

- Geometric mean (including insignificant results): 1.027x slower

# HPT report

- Reliability score: 99.75% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x