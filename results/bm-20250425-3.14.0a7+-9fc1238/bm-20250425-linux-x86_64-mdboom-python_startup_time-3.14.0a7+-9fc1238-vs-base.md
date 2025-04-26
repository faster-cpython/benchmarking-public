# Results vs. base

- fork: mdboom
- ref: python_startup_time
- machine: linux-x86_64
- commit hash: 9fc1238
- commit date: 2025-04-25
- overall geometric mean: 1.002x faster
- HPT reliability: 99.95%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250421-linux-x86_64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 | bm-20250425-linux-x86_64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 252 ms                                                                 | 251 ms: 1.00x faster                                                  |
| docutils       | 2.61 sec                                                               | 2.60 sec: 1.00x faster                                                |
| html5lib       | 60.2 ms                                                                | 62.1 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250421-linux-x86_64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 | bm-20250425-linux-x86_64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg               | 254 ms                                                                 | 250 ms: 1.02x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 483 ms                                                                 | 479 ms: 1.01x faster                                                  |
| async_tree_eager                 | 103 ms                                                                 | 102 ms: 1.01x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 453 ms                                                                 | 450 ms: 1.01x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 378 ms                                                                 | 375 ms: 1.01x faster                                                  |
| async_generators                 | 401 ms                                                                 | 398 ms: 1.01x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                                 | 614 ms: 1.01x faster                                                  |
| Geometric mean                   | (ref)                                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (12): async_tree_eager_io, async_tree_eager_tg, async_tree_eager_memoization, async_tree_memoization, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_eager_memoization_tg, async_tree_io, async_tree_io_tg, coroutines, asyncio_websockets, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250421-linux-x86_64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 | bm-20250425-linux-x86_64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 70.6 ms                                                                | 69.0 ms: 1.02x faster                                                 |
| nbody          | 96.1 ms                                                                | 98.7 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250421-linux-x86_64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 | bm-20250425-linux-x86_64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 126 ms                                                                 | 126 ms: 1.00x faster                                                  |
| regex_v8       | 22.3 ms                                                                | 22.5 ms: 1.01x slower                                                 |
| regex_dna      | 205 ms                                                                 | 208 ms: 1.01x slower                                                  |
| regex_effbot   | 3.13 ms                                                                | 3.19 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250421-linux-x86_64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 | bm-20250425-linux-x86_64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 11.7 ms                                                                | 11.6 ms: 1.00x faster                                                 |
| pickle_pure_python   | 314 us                                                                 | 313 us: 1.00x faster                                                  |
| json_loads           | 30.1 us                                                                | 30.2 us: 1.00x slower                                                 |
| unpickle_pure_python | 217 us                                                                 | 218 us: 1.00x slower                                                  |
| xml_etree_parse      | 140 ms                                                                 | 141 ms: 1.01x slower                                                  |
| tomli_loads          | 1.96 sec                                                               | 1.99 sec: 1.02x slower                                                |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (3): xml_etree_generate, xml_etree_process, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250421-linux-x86_64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 | bm-20250425-linux-x86_64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 8.20 ms                                                                | 7.31 ms: 1.12x faster                                                 |
| python_startup         | 13.2 ms                                                                | 13.3 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                                  | 1.06x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250421-linux-x86_64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 | bm-20250425-linux-x86_64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.8 ms                                                                | 11.4 ms: 1.03x faster                                                 |
| genshi_xml      | 49.6 ms                                                                | 49.0 ms: 1.01x faster                                                 |
| django_template | 31.6 ms                                                                | 31.4 ms: 1.01x faster                                                 |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                        | bm-20250421-linux-x86_64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 | bm-20250425-linux-x86_64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site           | 8.20 ms                                                                | 7.31 ms: 1.12x faster                                                 |
| richards_super                   | 50.0 ms                                                                | 48.5 ms: 1.03x faster                                                 |
| mako                             | 11.8 ms                                                                | 11.4 ms: 1.03x faster                                                 |
| richards                         | 43.7 ms                                                                | 42.7 ms: 1.02x faster                                                 |
| float                            | 70.6 ms                                                                | 69.0 ms: 1.02x faster                                                 |
| deltablue                        | 3.41 ms                                                                | 3.33 ms: 1.02x faster                                                 |
| telco                            | 7.91 ms                                                                | 7.76 ms: 1.02x faster                                                 |
| pyflate                          | 446 ms                                                                 | 439 ms: 1.02x faster                                                  |
| async_tree_none_tg               | 254 ms                                                                 | 250 ms: 1.02x faster                                                  |
| spectral_norm                    | 105 ms                                                                 | 104 ms: 1.01x faster                                                  |
| pprint_pformat                   | 1.46 sec                                                               | 1.44 sec: 1.01x faster                                                |
| typing_runtime_protocols         | 169 us                                                                 | 167 us: 1.01x faster                                                  |
| dulwich_log                      | 59.8 ms                                                                | 59.0 ms: 1.01x faster                                                 |
| pathlib                          | 16.8 ms                                                                | 16.6 ms: 1.01x faster                                                 |
| genshi_xml                       | 49.6 ms                                                                | 49.0 ms: 1.01x faster                                                 |
| scimark_lu                       | 119 ms                                                                 | 117 ms: 1.01x faster                                                  |
| subparsers                       | 21.3 ms                                                                | 21.0 ms: 1.01x faster                                                 |
| async_tree_cpu_io_mixed_tg       | 483 ms                                                                 | 479 ms: 1.01x faster                                                  |
| async_tree_eager                 | 103 ms                                                                 | 102 ms: 1.01x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 453 ms                                                                 | 450 ms: 1.01x faster                                                  |
| scimark_sor                      | 120 ms                                                                 | 119 ms: 1.01x faster                                                  |
| go                               | 112 ms                                                                 | 111 ms: 1.01x faster                                                  |
| sympy_expand                     | 455 ms                                                                 | 451 ms: 1.01x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 378 ms                                                                 | 375 ms: 1.01x faster                                                  |
| django_template                  | 31.6 ms                                                                | 31.4 ms: 1.01x faster                                                 |
| create_gc_cycles                 | 2.48 ms                                                                | 2.46 ms: 1.01x faster                                                 |
| async_generators                 | 401 ms                                                                 | 398 ms: 1.01x faster                                                  |
| pprint_safe_repr                 | 714 ms                                                                 | 709 ms: 1.01x faster                                                  |
| sympy_sum                        | 148 ms                                                                 | 147 ms: 1.01x faster                                                  |
| deepcopy_memo                    | 28.5 us                                                                | 28.3 us: 1.01x faster                                                 |
| sqlglot_v2_transpile             | 1.56 ms                                                                | 1.55 ms: 1.01x faster                                                 |
| raytrace                         | 263 ms                                                                 | 262 ms: 1.01x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                                 | 614 ms: 1.01x faster                                                  |
| sympy_str                        | 267 ms                                                                 | 265 ms: 1.00x faster                                                  |
| regex_compile                    | 126 ms                                                                 | 126 ms: 1.00x faster                                                  |
| json_dumps                       | 11.7 ms                                                                | 11.6 ms: 1.00x faster                                                 |
| sqlglot_v2_optimize              | 52.2 ms                                                                | 52.0 ms: 1.00x faster                                                 |
| docutils                         | 2.61 sec                                                               | 2.60 sec: 1.00x faster                                                |
| pickle_pure_python               | 314 us                                                                 | 313 us: 1.00x faster                                                  |
| sqlglot_v2_parse                 | 1.24 ms                                                                | 1.24 ms: 1.00x faster                                                 |
| 2to3                             | 252 ms                                                                 | 251 ms: 1.00x faster                                                  |
| json_loads                       | 30.1 us                                                                | 30.2 us: 1.00x slower                                                 |
| unpickle_pure_python             | 217 us                                                                 | 218 us: 1.00x slower                                                  |
| bpe_tokeniser                    | 4.50 sec                                                               | 4.52 sec: 1.01x slower                                                |
| python_startup                   | 13.2 ms                                                                | 13.3 ms: 1.01x slower                                                 |
| xml_etree_parse                  | 140 ms                                                                 | 141 ms: 1.01x slower                                                  |
| logging_simple                   | 5.52 us                                                                | 5.56 us: 1.01x slower                                                 |
| regex_v8                         | 22.3 ms                                                                | 22.5 ms: 1.01x slower                                                 |
| chaos                            | 56.7 ms                                                                | 57.1 ms: 1.01x slower                                                 |
| scimark_monte_carlo              | 66.2 ms                                                                | 66.8 ms: 1.01x slower                                                 |
| logging_format                   | 6.18 us                                                                | 6.23 us: 1.01x slower                                                 |
| generators                       | 29.1 ms                                                                | 29.4 ms: 1.01x slower                                                 |
| sqlite_synth                     | 2.81 us                                                                | 2.85 us: 1.01x slower                                                 |
| fannkuch                         | 420 ms                                                                 | 425 ms: 1.01x slower                                                  |
| regex_dna                        | 205 ms                                                                 | 208 ms: 1.01x slower                                                  |
| tomli_loads                      | 1.96 sec                                                               | 1.99 sec: 1.02x slower                                                |
| regex_effbot                     | 3.13 ms                                                                | 3.19 ms: 1.02x slower                                                 |
| hexiom                           | 6.23 ms                                                                | 6.34 ms: 1.02x slower                                                 |
| connected_components             | 450 ms                                                                 | 459 ms: 1.02x slower                                                  |
| nbody                            | 96.1 ms                                                                | 98.7 ms: 1.03x slower                                                 |
| html5lib                         | 60.2 ms                                                                | 62.1 ms: 1.03x slower                                                 |
| gc_traversal                     | 4.78 ms                                                                | 5.00 ms: 1.05x slower                                                 |
| shortest_path                    | 486 ms                                                                 | 509 ms: 1.05x slower                                                  |
| Geometric mean                   | (ref)                                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (40): async_tree_eager_io, async_tree_eager_tg, async_tree_eager_memoization, async_tree_memoization, async_tree_memoization_tg, async_tree_cpu_io_mixed, scimark_sparse_mat_mult, async_tree_eager_memoization_tg, async_tree_io, async_tree_io_tg, genshi_text, sqlglot_v2_normalize, coroutines, deepcopy, xml_etree_generate, comprehensions, many_optionals, pycparser, sqlalchemy_declarative, sqlalchemy_imperative, coverage, meteor_contest, bench_mp_pool, scimark_fft, pylint, xml_etree_process, pidigits, crypto_pyaes, sphinx, bench_thread_pool, asyncio_websockets, nqueens, sympy_integrate, mdp, async_tree_none, k_core, deepcopy_reduce, xml_etree_iterparse, json, logging_silent

- Geometric mean (including insignificant results): 1.002x faster

# HPT report

- Reliability score: 99.95% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x