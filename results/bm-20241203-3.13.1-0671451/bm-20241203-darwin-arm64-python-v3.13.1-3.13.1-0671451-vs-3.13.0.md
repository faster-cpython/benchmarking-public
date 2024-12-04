# Results vs. 3.13.0

- fork: python
- ref: v3.13.1
- machine: darwin-arm64
- commit hash: 0671451
- commit date: 2024-12-03
- overall geometric mean: 1.002x slower
- HPT reliability: 98.22%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241203-darwin-arm64-python-v3.13.1-3.13.1-0671451 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 181 ms: 1.04x faster                                   |
| chameleon      | 5.08 ms                                                | 5.06 ms: 1.00x faster                                  |
| docutils       | 1.44 sec                                               | 1.43 sec: 1.01x faster                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                           |

Benchmark hidden because not significant (3): html5lib, sphinx, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241203-darwin-arm64-python-v3.13.1-3.13.1-0671451 |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 278 ms: 1.03x faster                                   |
| async_generators                 | 295 ms                                                 | 292 ms: 1.01x faster                                   |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 461 ms: 1.00x slower                                   |
| async_tree_eager                 | 70.1 ms                                                | 70.3 ms: 1.00x slower                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 348 ms: 1.00x slower                                   |
| coroutines                       | 19.8 ms                                                | 19.9 ms: 1.01x slower                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 140 ms: 1.02x slower                                   |
| async_tree_eager_tg              | 47.8 ms                                                | 49.0 ms: 1.02x slower                                  |
| async_tree_io_tg                 | 497 ms                                                 | 520 ms: 1.05x slower                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 481 ms: 1.07x slower                                   |
| async_tree_eager_io_tg           | 477 ms                                                 | 517 ms: 1.08x slower                                   |
| Geometric mean                   | (ref)                                                  | 1.01x slower                                           |

Benchmark hidden because not significant (8): async_tree_none, asyncio_websockets, async_tree_eager_memoization, async_tree_eager_cpu_io_mixed, async_tree_eager_io, async_tree_none_tg, async_tree_memoization, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241203-darwin-arm64-python-v3.13.1-3.13.1-0671451 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 74.0 ms                                                | 73.3 ms: 1.01x faster                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                           |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241203-darwin-arm64-python-v3.13.1-3.13.1-0671451 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.25 ms: 1.17x faster                                  |
| regex_dna      | 149 ms                                                 | 141 ms: 1.06x faster                                   |
| regex_v8       | 17.0 ms                                                | 16.9 ms: 1.01x faster                                  |
| regex_compile  | 78.6 ms                                                | 80.8 ms: 1.03x slower                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241203-darwin-arm64-python-v3.13.1-3.13.1-0671451 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| xml_etree_generate   | 57.0 ms                                                | 56.7 ms: 1.00x faster                                  |
| json_dumps           | 6.52 ms                                                | 6.55 ms: 1.00x slower                                  |
| unpickle_pure_python | 164 us                                                 | 165 us: 1.01x slower                                   |
| pickle_pure_python   | 214 us                                                 | 221 us: 1.03x slower                                   |
| Geometric mean       | (ref)                                                  | 1.00x slower                                           |

Benchmark hidden because not significant (5): xml_etree_parse, tomli_loads, xml_etree_process, json_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241203-darwin-arm64-python-v3.13.1-3.13.1-0671451 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 14.5 ms                                                | 15.6 ms: 1.08x slower                                  |
| python_startup         | 18.9 ms                                                | 20.5 ms: 1.09x slower                                  |
| Geometric mean         | (ref)                                                  | 1.08x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241203-darwin-arm64-python-v3.13.1-3.13.1-0671451 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| django_template | 22.2 ms                                                | 21.0 ms: 1.06x faster                                  |
| genshi_text     | 16.9 ms                                                | 17.0 ms: 1.01x slower                                  |
| Geometric mean  | (ref)                                                  | 1.01x faster                                           |

Benchmark hidden because not significant (2): mako, genshi_xml

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241203-darwin-arm64-python-v3.13.1-3.13.1-0671451 |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot                     | 2.63 ms                                                | 2.25 ms: 1.17x faster                                  |
| django_template                  | 22.2 ms                                                | 21.0 ms: 1.06x faster                                  |
| regex_dna                        | 149 ms                                                 | 141 ms: 1.06x faster                                   |
| 2to3                             | 187 ms                                                 | 181 ms: 1.04x faster                                   |
| async_tree_memoization_tg        | 288 ms                                                 | 278 ms: 1.03x faster                                   |
| dask                             | 790 ms                                                 | 771 ms: 1.02x faster                                   |
| fannkuch                         | 284 ms                                                 | 280 ms: 1.01x faster                                   |
| logging_simple                   | 3.60 us                                                | 3.56 us: 1.01x faster                                  |
| deepcopy                         | 237 us                                                 | 234 us: 1.01x faster                                   |
| async_generators                 | 295 ms                                                 | 292 ms: 1.01x faster                                   |
| nbody                            | 74.0 ms                                                | 73.3 ms: 1.01x faster                                  |
| scimark_lu                       | 76.7 ms                                                | 75.9 ms: 1.01x faster                                  |
| logging_format                   | 3.89 us                                                | 3.86 us: 1.01x faster                                  |
| deltablue                        | 2.68 ms                                                | 2.66 ms: 1.01x faster                                  |
| regex_v8                         | 17.0 ms                                                | 16.9 ms: 1.01x faster                                  |
| docutils                         | 1.44 sec                                               | 1.43 sec: 1.01x faster                                 |
| pycparser                        | 705 ms                                                 | 701 ms: 1.01x faster                                   |
| chameleon                        | 5.08 ms                                                | 5.06 ms: 1.00x faster                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 50.2 ms: 1.00x faster                                  |
| xml_etree_generate               | 57.0 ms                                                | 56.7 ms: 1.00x faster                                  |
| gc_traversal                     | 2.91 ms                                                | 2.92 ms: 1.00x slower                                  |
| sqlalchemy_declarative           | 58.9 ms                                                | 59.0 ms: 1.00x slower                                  |
| richards                         | 35.2 ms                                                | 35.3 ms: 1.00x slower                                  |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 461 ms: 1.00x slower                                   |
| async_tree_eager                 | 70.1 ms                                                | 70.3 ms: 1.00x slower                                  |
| pprint_safe_repr                 | 533 ms                                                 | 535 ms: 1.00x slower                                   |
| deepcopy_memo                    | 27.4 us                                                | 27.5 us: 1.00x slower                                  |
| connected_components             | 319 ms                                                 | 320 ms: 1.00x slower                                   |
| json_dumps                       | 6.52 ms                                                | 6.55 ms: 1.00x slower                                  |
| sympy_str                        | 145 ms                                                 | 146 ms: 1.00x slower                                   |
| pprint_pformat                   | 1.08 sec                                               | 1.09 sec: 1.00x slower                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 348 ms: 1.00x slower                                   |
| unpickle_pure_python             | 164 us                                                 | 165 us: 1.01x slower                                   |
| raytrace                         | 181 ms                                                 | 182 ms: 1.01x slower                                   |
| scimark_sor                      | 105 ms                                                 | 106 ms: 1.01x slower                                   |
| sympy_integrate                  | 11.3 ms                                                | 11.4 ms: 1.01x slower                                  |
| logging_silent                   | 70.1 ns                                                | 70.5 ns: 1.01x slower                                  |
| sqlglot_transpile                | 1.02 ms                                                | 1.03 ms: 1.01x slower                                  |
| bench_thread_pool                | 505 us                                                 | 508 us: 1.01x slower                                   |
| crypto_pyaes                     | 54.2 ms                                                | 54.6 ms: 1.01x slower                                  |
| bpe_tokeniser                    | 3.25 sec                                               | 3.27 sec: 1.01x slower                                 |
| sympy_sum                        | 75.4 ms                                                | 75.9 ms: 1.01x slower                                  |
| meteor_contest                   | 74.0 ms                                                | 74.5 ms: 1.01x slower                                  |
| sqlglot_optimize                 | 34.9 ms                                                | 35.2 ms: 1.01x slower                                  |
| comprehensions                   | 12.3 us                                                | 12.4 us: 1.01x slower                                  |
| sqlglot_normalize                | 189 ms                                                 | 190 ms: 1.01x slower                                   |
| coroutines                       | 19.8 ms                                                | 19.9 ms: 1.01x slower                                  |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 3.01 ms: 1.01x slower                                  |
| genshi_text                      | 16.9 ms                                                | 17.0 ms: 1.01x slower                                  |
| create_gc_cycles                 | 1.17 ms                                                | 1.18 ms: 1.01x slower                                  |
| nqueens                          | 62.5 ms                                                | 63.2 ms: 1.01x slower                                  |
| json                             | 3.03 ms                                                | 3.06 ms: 1.01x slower                                  |
| chaos                            | 41.2 ms                                                | 41.7 ms: 1.01x slower                                  |
| sympy_expand                     | 246 ms                                                 | 249 ms: 1.01x slower                                   |
| hexiom                           | 4.86 ms                                                | 4.92 ms: 1.01x slower                                  |
| mdp                              | 1.49 sec                                               | 1.51 sec: 1.01x slower                                 |
| richards_super                   | 39.1 ms                                                | 39.7 ms: 1.01x slower                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 140 ms: 1.02x slower                                   |
| async_tree_eager_tg              | 47.8 ms                                                | 49.0 ms: 1.02x slower                                  |
| regex_compile                    | 78.6 ms                                                | 80.8 ms: 1.03x slower                                  |
| pickle_pure_python               | 214 us                                                 | 221 us: 1.03x slower                                   |
| bench_mp_pool                    | 62.5 ms                                                | 64.7 ms: 1.03x slower                                  |
| async_tree_io_tg                 | 497 ms                                                 | 520 ms: 1.05x slower                                   |
| spectral_norm                    | 76.3 ms                                                | 79.9 ms: 1.05x slower                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 481 ms: 1.07x slower                                   |
| python_startup_no_site           | 14.5 ms                                                | 15.6 ms: 1.08x slower                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 517 ms: 1.08x slower                                   |
| python_startup                   | 18.9 ms                                                | 20.5 ms: 1.09x slower                                  |
| Geometric mean                   | (ref)                                                  | 1.00x slower                                           |

Benchmark hidden because not significant (37): tornado_http, html5lib, sphinx, async_tree_none, typing_runtime_protocols, coverage, pylint, scimark_fft, deepcopy_reduce, xml_etree_parse, generators, mako, thrift, float, dulwich_log, sqlglot_parse, genshi_xml, gevent_hub, go, tomli_loads, pyflate, pidigits, xml_etree_process, asyncio_websockets, sqlalchemy_imperative, async_tree_eager_memoization, telco, pathlib, async_tree_eager_cpu_io_mixed, async_tree_eager_io, json_loads, shortest_path, async_tree_none_tg, xml_etree_iterparse, k_core, async_tree_memoization, async_tree_io
Ignored benchmarks (1) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: mypy2
Ignored benchmarks (6) of results/bm-20241203-3.13.1-0671451/bm-20241203-darwin-arm64-python-v3.13.1-3.13.1-0671451.json: djangocms, flaskblogging, gunicorn, many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 98.22% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x