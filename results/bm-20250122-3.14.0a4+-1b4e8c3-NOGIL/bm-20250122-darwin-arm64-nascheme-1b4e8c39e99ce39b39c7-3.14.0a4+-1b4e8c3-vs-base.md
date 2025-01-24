# Results vs. base

- fork: nascheme
- ref: 1b4e8c39e99ce39b39c7
- machine: darwin-arm64
- commit hash: 1b4e8c3
- commit date: 2025-01-22
- overall geometric mean: 1.007x slower
- HPT reliability: 83.54%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250117-darwin-arm64-python-3829104ab412a47bf3f3-3.14.0a4+-3829104 | bm-20250122-darwin-arm64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 182 ms                                                                 | 183 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                             |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250117-darwin-arm64-python-3829104ab412a47bf3f3-3.14.0a4+-3829104 | bm-20250122-darwin-arm64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_generators                 | 261 ms                                                                 | 259 ms: 1.01x faster                                                     |
| async_tree_eager_cpu_io_mixed_tg | 345 ms                                                                 | 344 ms: 1.00x faster                                                     |
| coroutines                       | 16.9 ms                                                                | 16.8 ms: 1.00x faster                                                    |
| async_tree_io_tg                 | 305 ms                                                                 | 306 ms: 1.00x slower                                                     |
| async_tree_eager                 | 81.9 ms                                                                | 82.1 ms: 1.00x slower                                                    |
| async_tree_memoization_tg        | 173 ms                                                                 | 173 ms: 1.00x slower                                                     |
| async_tree_eager_memoization_tg  | 130 ms                                                                 | 131 ms: 1.01x slower                                                     |
| async_tree_eager_memoization     | 151 ms                                                                 | 152 ms: 1.01x slower                                                     |
| async_tree_eager_tg              | 55.6 ms                                                                | 56.0 ms: 1.01x slower                                                    |
| Geometric mean                   | (ref)                                                                  | 1.00x slower                                                             |

Benchmark hidden because not significant (10): asyncio_websockets, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_eager_io, async_tree_none, async_tree_eager_io_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250117-darwin-arm64-python-3829104ab412a47bf3f3-3.14.0a4+-3829104 | bm-20250122-darwin-arm64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 15.6 ms                                                                | 15.4 ms: 1.01x faster                                                    |
| regex_effbot   | 2.08 ms                                                                | 2.08 ms: 1.00x faster                                                    |
| regex_dna      | 138 ms                                                                 | 137 ms: 1.00x faster                                                     |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250117-darwin-arm64-python-3829104ab412a47bf3f3-3.14.0a4+-3829104 | bm-20250122-darwin-arm64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps           | 7.69 ms                                                                | 7.65 ms: 1.01x faster                                                    |
| json_loads           | 17.7 us                                                                | 17.7 us: 1.00x faster                                                    |
| unpickle_pure_python | 154 us                                                                 | 153 us: 1.00x faster                                                     |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (2): tomli_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250117-darwin-arm64-python-3829104ab412a47bf3f3-3.14.0a4+-3829104 | bm-20250122-darwin-arm64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                                | 20.7 ms: 1.00x slower                                                    |
| python_startup_no_site | 16.0 ms                                                                | 16.1 ms: 1.01x slower                                                    |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250117-darwin-arm64-python-3829104ab412a47bf3f3-3.14.0a4+-3829104 | bm-20250122-darwin-arm64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|-----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 9.93 ms                                                                | 9.96 ms: 1.00x slower                                                    |
| django_template | 23.9 ms                                                                | 24.0 ms: 1.00x slower                                                    |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                             |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                        | bm-20250117-darwin-arm64-python-3829104ab412a47bf3f3-3.14.0a4+-3829104 | bm-20250122-darwin-arm64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| scimark_sparse_mat_mult          | 3.63 ms                                                                | 3.56 ms: 1.02x faster                                                    |
| regex_v8                         | 15.6 ms                                                                | 15.4 ms: 1.01x faster                                                    |
| scimark_fft                      | 212 ms                                                                 | 210 ms: 1.01x faster                                                     |
| connected_components             | 329 ms                                                                 | 326 ms: 1.01x faster                                                     |
| pyflate                          | 309 ms                                                                 | 307 ms: 1.01x faster                                                     |
| bpe_tokeniser                    | 3.03 sec                                                               | 3.01 sec: 1.01x faster                                                   |
| k_core                           | 1.62 sec                                                               | 1.62 sec: 1.01x faster                                                   |
| scimark_sor                      | 90.7 ms                                                                | 90.2 ms: 1.01x faster                                                    |
| fannkuch                         | 284 ms                                                                 | 283 ms: 1.01x faster                                                     |
| logging_silent                   | 79.8 ns                                                                | 79.3 ns: 1.01x faster                                                    |
| async_generators                 | 261 ms                                                                 | 259 ms: 1.01x faster                                                     |
| json_dumps                       | 7.69 ms                                                                | 7.65 ms: 1.01x faster                                                    |
| scimark_lu                       | 88.6 ms                                                                | 88.2 ms: 1.00x faster                                                    |
| pycparser                        | 635 ms                                                                 | 633 ms: 1.00x faster                                                     |
| json_loads                       | 17.7 us                                                                | 17.7 us: 1.00x faster                                                    |
| comprehensions                   | 13.3 us                                                                | 13.3 us: 1.00x faster                                                    |
| deepcopy_memo                    | 21.6 us                                                                | 21.5 us: 1.00x faster                                                    |
| regex_effbot                     | 2.08 ms                                                                | 2.08 ms: 1.00x faster                                                    |
| thrift                           | 497 us                                                                 | 496 us: 1.00x faster                                                     |
| async_tree_eager_cpu_io_mixed_tg | 345 ms                                                                 | 344 ms: 1.00x faster                                                     |
| regex_dna                        | 138 ms                                                                 | 137 ms: 1.00x faster                                                     |
| unpickle_pure_python             | 154 us                                                                 | 153 us: 1.00x faster                                                     |
| nqueens                          | 60.3 ms                                                                | 60.2 ms: 1.00x faster                                                    |
| coroutines                       | 16.9 ms                                                                | 16.8 ms: 1.00x faster                                                    |
| sqlglot_normalize                | 187 ms                                                                 | 188 ms: 1.00x slower                                                     |
| async_tree_io_tg                 | 305 ms                                                                 | 306 ms: 1.00x slower                                                     |
| raytrace                         | 211 ms                                                                 | 211 ms: 1.00x slower                                                     |
| mako                             | 9.93 ms                                                                | 9.96 ms: 1.00x slower                                                    |
| chaos                            | 43.0 ms                                                                | 43.1 ms: 1.00x slower                                                    |
| async_tree_eager                 | 81.9 ms                                                                | 82.1 ms: 1.00x slower                                                    |
| mdp                              | 1.57 sec                                                               | 1.57 sec: 1.00x slower                                                   |
| async_tree_memoization_tg        | 173 ms                                                                 | 173 ms: 1.00x slower                                                     |
| bench_mp_pool                    | 66.1 ms                                                                | 66.3 ms: 1.00x slower                                                    |
| python_startup                   | 20.6 ms                                                                | 20.7 ms: 1.00x slower                                                    |
| django_template                  | 23.9 ms                                                                | 24.0 ms: 1.00x slower                                                    |
| dulwich_log                      | 29.1 ms                                                                | 29.2 ms: 1.00x slower                                                    |
| async_tree_eager_memoization_tg  | 130 ms                                                                 | 131 ms: 1.01x slower                                                     |
| 2to3                             | 182 ms                                                                 | 183 ms: 1.01x slower                                                     |
| async_tree_eager_memoization     | 151 ms                                                                 | 152 ms: 1.01x slower                                                     |
| async_tree_eager_tg              | 55.6 ms                                                                | 56.0 ms: 1.01x slower                                                    |
| python_startup_no_site           | 16.0 ms                                                                | 16.1 ms: 1.01x slower                                                    |
| sqlite_synth                     | 1.30 us                                                                | 1.32 us: 1.01x slower                                                    |
| create_gc_cycles                 | 814 us                                                                 | 1.06 ms: 1.30x slower                                                    |
| gc_traversal                     | 2.31 ms                                                                | 3.74 ms: 1.62x slower                                                    |
| Geometric mean                   | (ref)                                                                  | 1.01x slower                                                             |

Benchmark hidden because not significant (56): sqlalchemy_declarative, tomli_loads, subparsers, sphinx, asyncio_websockets, sympy_str, generators, shortest_path, coverage, async_tree_cpu_io_mixed, richards, spectral_norm, async_tree_cpu_io_mixed_tg, go, crypto_pyaes, sympy_integrate, deepcopy, float, pprint_pformat, meteor_contest, genshi_xml, genshi_text, async_tree_eager_cpu_io_mixed, richards_super, sqlalchemy_imperative, logging_simple, hexiom, regex_compile, async_tree_io, pidigits, async_tree_memoization, docutils, logging_format, pprint_safe_repr, html5lib, sympy_expand, async_tree_eager_io, sympy_sum, json, pickle_pure_python, sqlglot_optimize, nbody, scimark_monte_carlo, typing_runtime_protocols, telco, async_tree_none, sqlglot_transpile, async_tree_eager_io_tg, async_tree_none_tg, sqlglot_parse, bench_thread_pool, pathlib, deepcopy_reduce, deltablue, many_optionals, pylint
Ignored benchmarks (4) of results/bm-20250117-3.14.0a4+-3829104-NOGIL/bm-20250117-darwin-arm64-python-3829104ab412a47bf3f3-3.14.0a4+-3829104.json: xml_etree_generate, xml_etree_iterparse, xml_etree_parse, xml_etree_process

- Geometric mean (including insignificant results): 1.007x slower

# HPT report

- Reliability score: 83.54% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x