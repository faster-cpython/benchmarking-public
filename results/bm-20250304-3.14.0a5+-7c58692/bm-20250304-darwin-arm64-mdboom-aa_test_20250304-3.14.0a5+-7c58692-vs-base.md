# Results vs. base

- fork: mdboom
- ref: aa_test_20250304
- machine: darwin-arm64
- commit hash: 7c58692
- commit date: 2025-03-04
- overall geometric mean: 1.003x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250304-darwin-arm64-python-3dd3675492a3fc3b7996-3.14.0a5+-3dd3675 | bm-20250304-darwin-arm64-mdboom-aa_test_20250304-3.14.0a5+-7c58692 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| docutils       | 1.50 sec                                                               | 1.51 sec: 1.00x slower                                             |
| html5lib       | 33.0 ms                                                                | 34.9 ms: 1.06x slower                                              |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                       |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250304-darwin-arm64-python-3dd3675492a3fc3b7996-3.14.0a5+-3dd3675 | bm-20250304-darwin-arm64-mdboom-aa_test_20250304-3.14.0a5+-7c58692 |
|----------------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_eager_cpu_io_mixed    | 367 ms                                                                 | 368 ms: 1.00x slower                                               |
| async_tree_eager                 | 69.1 ms                                                                | 69.4 ms: 1.00x slower                                              |
| coroutines                       | 18.7 ms                                                                | 18.7 ms: 1.00x slower                                              |
| async_tree_eager_cpu_io_mixed_tg | 402 ms                                                                 | 404 ms: 1.00x slower                                               |
| async_tree_memoization           | 222 ms                                                                 | 223 ms: 1.00x slower                                               |
| async_tree_cpu_io_mixed          | 435 ms                                                                 | 438 ms: 1.01x slower                                               |
| async_tree_none                  | 178 ms                                                                 | 180 ms: 1.01x slower                                               |
| Geometric mean                   | (ref)                                                                  | 1.00x slower                                                       |

Benchmark hidden because not significant (12): async_tree_eager_memoization_tg, async_tree_memoization_tg, asyncio_websockets, async_tree_eager_memoization, async_tree_io, async_tree_eager_tg, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_generators, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250304-darwin-arm64-python-3dd3675492a3fc3b7996-3.14.0a5+-3dd3675 | bm-20250304-darwin-arm64-mdboom-aa_test_20250304-3.14.0a5+-7c58692 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 91.8 ms                                                                | 91.8 ms: 1.00x slower                                              |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                       |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250304-darwin-arm64-python-3dd3675492a3fc3b7996-3.14.0a5+-3dd3675 | bm-20250304-darwin-arm64-mdboom-aa_test_20250304-3.14.0a5+-7c58692 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 78.0 ms                                                                | 78.1 ms: 1.00x slower                                              |
| regex_v8       | 16.9 ms                                                                | 16.9 ms: 1.00x slower                                              |
| regex_dna      | 140 ms                                                                 | 144 ms: 1.03x slower                                               |
| regex_effbot   | 2.26 ms                                                                | 2.34 ms: 1.03x slower                                              |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250304-darwin-arm64-python-3dd3675492a3fc3b7996-3.14.0a5+-3dd3675 | bm-20250304-darwin-arm64-mdboom-aa_test_20250304-3.14.0a5+-7c58692 |
|----------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| xml_etree_iterparse  | 74.9 ms                                                                | 74.3 ms: 1.01x faster                                              |
| pickle_pure_python   | 231 us                                                                 | 230 us: 1.01x faster                                               |
| xml_etree_process    | 42.8 ms                                                                | 42.9 ms: 1.00x slower                                              |
| json_dumps           | 7.49 ms                                                                | 7.51 ms: 1.00x slower                                              |
| unpickle_pure_python | 169 us                                                                 | 170 us: 1.00x slower                                               |
| xml_etree_generate   | 58.1 ms                                                                | 58.3 ms: 1.00x slower                                              |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                       |

Benchmark hidden because not significant (3): json_loads, tomli_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250304-darwin-arm64-python-3dd3675492a3fc3b7996-3.14.0a5+-3dd3675 | bm-20250304-darwin-arm64-mdboom-aa_test_20250304-3.14.0a5+-7c58692 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 13.9 ms                                                                | 14.0 ms: 1.01x slower                                              |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                       |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250304-darwin-arm64-python-3dd3675492a3fc3b7996-3.14.0a5+-3dd3675 | bm-20250304-darwin-arm64-mdboom-aa_test_20250304-3.14.0a5+-7c58692 |
|-----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| django_template | 24.7 ms                                                                | 24.2 ms: 1.02x faster                                              |
| mako            | 8.15 ms                                                                | 8.44 ms: 1.04x slower                                              |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                       |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                        | bm-20250304-darwin-arm64-python-3dd3675492a3fc3b7996-3.14.0a5+-3dd3675 | bm-20250304-darwin-arm64-mdboom-aa_test_20250304-3.14.0a5+-7c58692 |
|----------------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| richards_super                   | 44.2 ms                                                                | 42.9 ms: 1.03x faster                                              |
| django_template                  | 24.7 ms                                                                | 24.2 ms: 1.02x faster                                              |
| deepcopy_memo                    | 21.4 us                                                                | 21.0 us: 1.02x faster                                              |
| coverage                         | 48.6 ms                                                                | 47.9 ms: 1.01x faster                                              |
| xml_etree_iterparse              | 74.9 ms                                                                | 74.3 ms: 1.01x faster                                              |
| comprehensions                   | 13.1 us                                                                | 13.1 us: 1.01x faster                                              |
| gc_traversal                     | 3.10 ms                                                                | 3.08 ms: 1.01x faster                                              |
| pickle_pure_python               | 231 us                                                                 | 230 us: 1.01x faster                                               |
| richards                         | 40.1 ms                                                                | 39.9 ms: 1.00x faster                                              |
| sqlite_synth                     | 1.54 us                                                                | 1.53 us: 1.00x faster                                              |
| sympy_expand                     | 256 ms                                                                 | 255 ms: 1.00x faster                                               |
| nbody                            | 91.8 ms                                                                | 91.8 ms: 1.00x slower                                              |
| regex_compile                    | 78.0 ms                                                                | 78.1 ms: 1.00x slower                                              |
| pyflate                          | 351 ms                                                                 | 352 ms: 1.00x slower                                               |
| bpe_tokeniser                    | 3.23 sec                                                               | 3.24 sec: 1.00x slower                                             |
| dask                             | 768 ms                                                                 | 770 ms: 1.00x slower                                               |
| generators                       | 28.9 ms                                                                | 29.0 ms: 1.00x slower                                              |
| sqlglot_parse                    | 888 us                                                                 | 890 us: 1.00x slower                                               |
| regex_v8                         | 16.9 ms                                                                | 16.9 ms: 1.00x slower                                              |
| async_tree_eager_cpu_io_mixed    | 367 ms                                                                 | 368 ms: 1.00x slower                                               |
| xml_etree_process                | 42.8 ms                                                                | 42.9 ms: 1.00x slower                                              |
| hexiom                           | 5.26 ms                                                                | 5.28 ms: 1.00x slower                                              |
| sqlalchemy_declarative           | 62.6 ms                                                                | 62.8 ms: 1.00x slower                                              |
| json_dumps                       | 7.49 ms                                                                | 7.51 ms: 1.00x slower                                              |
| async_tree_eager                 | 69.1 ms                                                                | 69.4 ms: 1.00x slower                                              |
| pprint_pformat                   | 1.10 sec                                                               | 1.11 sec: 1.00x slower                                             |
| fannkuch                         | 291 ms                                                                 | 293 ms: 1.00x slower                                               |
| coroutines                       | 18.7 ms                                                                | 18.7 ms: 1.00x slower                                              |
| unpickle_pure_python             | 169 us                                                                 | 170 us: 1.00x slower                                               |
| xml_etree_generate               | 58.1 ms                                                                | 58.3 ms: 1.00x slower                                              |
| create_gc_cycles                 | 1.26 ms                                                                | 1.27 ms: 1.00x slower                                              |
| docutils                         | 1.50 sec                                                               | 1.51 sec: 1.00x slower                                             |
| async_tree_eager_cpu_io_mixed_tg | 402 ms                                                                 | 404 ms: 1.00x slower                                               |
| async_tree_memoization           | 222 ms                                                                 | 223 ms: 1.00x slower                                               |
| spectral_norm                    | 78.1 ms                                                                | 78.5 ms: 1.01x slower                                              |
| sqlalchemy_imperative            | 7.06 ms                                                                | 7.10 ms: 1.01x slower                                              |
| bench_thread_pool                | 521 us                                                                 | 523 us: 1.01x slower                                               |
| many_optionals                   | 465 us                                                                 | 468 us: 1.01x slower                                               |
| async_tree_cpu_io_mixed          | 435 ms                                                                 | 438 ms: 1.01x slower                                               |
| telco                            | 4.73 ms                                                                | 4.76 ms: 1.01x slower                                              |
| sqlglot_transpile                | 1.07 ms                                                                | 1.08 ms: 1.01x slower                                              |
| python_startup_no_site           | 13.9 ms                                                                | 14.0 ms: 1.01x slower                                              |
| json                             | 3.01 ms                                                                | 3.04 ms: 1.01x slower                                              |
| typing_runtime_protocols         | 101 us                                                                 | 102 us: 1.01x slower                                               |
| async_tree_none                  | 178 ms                                                                 | 180 ms: 1.01x slower                                               |
| connected_components             | 314 ms                                                                 | 317 ms: 1.01x slower                                               |
| pathlib                          | 23.6 ms                                                                | 23.9 ms: 1.01x slower                                              |
| shortest_path                    | 339 ms                                                                 | 345 ms: 1.02x slower                                               |
| regex_dna                        | 140 ms                                                                 | 144 ms: 1.03x slower                                               |
| regex_effbot                     | 2.26 ms                                                                | 2.34 ms: 1.03x slower                                              |
| mako                             | 8.15 ms                                                                | 8.44 ms: 1.04x slower                                              |
| html5lib                         | 33.0 ms                                                                | 34.9 ms: 1.06x slower                                              |
| mdp                              | 1.56 sec                                                               | 1.71 sec: 1.10x slower                                             |
| Geometric mean                   | (ref)                                                                  | 1.00x slower                                                       |

Benchmark hidden because not significant (52): k_core, deltablue, pprint_safe_repr, async_tree_eager_memoization_tg, scimark_sor, meteor_contest, scimark_fft, json_loads, crypto_pyaes, genshi_text, sympy_integrate, bench_mp_pool, nqueens, chaos, thrift, float, go, sqlglot_optimize, scimark_monte_carlo, pidigits, scimark_lu, python_startup, async_tree_memoization_tg, genshi_xml, subparsers, logging_simple, dulwich_log, raytrace, scimark_sparse_mat_mult, sqlglot_normalize, asyncio_websockets, sympy_sum, tomli_loads, async_tree_eager_memoization, pylint, logging_silent, 2to3, logging_format, deepcopy_reduce, async_tree_io, deepcopy, sympy_str, async_tree_eager_tg, xml_etree_parse, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, pycparser, async_generators, async_tree_none_tg, sphinx

- Geometric mean (including insignificant results): 1.003x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x