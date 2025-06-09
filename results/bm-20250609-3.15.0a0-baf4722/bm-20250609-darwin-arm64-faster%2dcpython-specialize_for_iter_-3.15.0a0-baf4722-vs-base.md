# Results vs. base

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: darwin-arm64
- commit hash: baf4722
- commit date: 2025-06-09
- overall geometric mean: 1.001x faster
- HPT reliability: 98.71%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250609-darwin-arm64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a | bm-20250609-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 186 ms                                                                | 185 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250609-darwin-arm64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a | bm-20250609-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|----------------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager_cpu_io_mixed_tg | 406 ms                                                                | 400 ms: 1.01x faster                                                            |
| async_tree_eager_cpu_io_mixed    | 372 ms                                                                | 369 ms: 1.01x faster                                                            |
| async_tree_eager                 | 74.2 ms                                                               | 73.6 ms: 1.01x faster                                                           |
| async_tree_cpu_io_mixed_tg       | 426 ms                                                                | 423 ms: 1.01x faster                                                            |
| coroutines                       | 19.3 ms                                                               | 19.3 ms: 1.00x faster                                                           |
| async_generators                 | 274 ms                                                                | 275 ms: 1.01x slower                                                            |
| Geometric mean                   | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (13): async_tree_eager_io, async_tree_none, async_tree_eager_memoization_tg, async_tree_none_tg, async_tree_io_tg, async_tree_eager_io_tg, async_tree_memoization, async_tree_io, async_tree_eager_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250609-darwin-arm64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a | bm-20250609-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 57.5 ms                                                               | 58.5 ms: 1.02x slower                                                           |
| nbody          | 84.9 ms                                                               | 86.7 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250609-darwin-arm64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a | bm-20250609-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 143 ms                                                                | 144 ms: 1.01x slower                                                            |
| regex_v8       | 16.2 ms                                                               | 16.3 ms: 1.01x slower                                                           |
| regex_effbot   | 2.34 ms                                                               | 2.37 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250609-darwin-arm64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a | bm-20250609-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|---------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_iterparse | 74.3 ms                                                               | 73.5 ms: 1.01x faster                                                           |
| json_loads          | 16.6 us                                                               | 16.5 us: 1.00x faster                                                           |
| xml_etree_process   | 43.1 ms                                                               | 43.0 ms: 1.00x faster                                                           |
| Geometric mean      | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (6): json_dumps, unpickle_pure_python, xml_etree_generate, pickle_pure_python, tomli_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250609-darwin-arm64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a | bm-20250609-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 14.0 ms                                                               | 14.1 ms: 1.00x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250609-darwin-arm64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a | bm-20250609-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 25.2 ms                                                               | 25.0 ms: 1.01x faster                                                           |
| mako            | 9.02 ms                                                               | 8.99 ms: 1.00x faster                                                           |
| genshi_text     | 17.6 ms                                                               | 17.6 ms: 1.00x faster                                                           |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                        | bm-20250609-darwin-arm64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a | bm-20250609-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|----------------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| gc_traversal                     | 3.34 ms                                                               | 3.19 ms: 1.05x faster                                                           |
| chaos                            | 48.3 ms                                                               | 47.6 ms: 1.02x faster                                                           |
| async_tree_eager_cpu_io_mixed_tg | 406 ms                                                                | 400 ms: 1.01x faster                                                            |
| logging_silent                   | 343 ns                                                                | 339 ns: 1.01x faster                                                            |
| deltablue                        | 2.82 ms                                                               | 2.79 ms: 1.01x faster                                                           |
| async_tree_eager_cpu_io_mixed    | 372 ms                                                                | 369 ms: 1.01x faster                                                            |
| scimark_sparse_mat_mult          | 3.19 ms                                                               | 3.16 ms: 1.01x faster                                                           |
| xml_etree_iterparse              | 74.3 ms                                                               | 73.5 ms: 1.01x faster                                                           |
| meteor_contest                   | 74.8 ms                                                               | 74.0 ms: 1.01x faster                                                           |
| dulwich_log                      | 26.8 ms                                                               | 26.5 ms: 1.01x faster                                                           |
| async_tree_eager                 | 74.2 ms                                                               | 73.6 ms: 1.01x faster                                                           |
| sympy_sum                        | 81.2 ms                                                               | 80.6 ms: 1.01x faster                                                           |
| typing_runtime_protocols         | 110 us                                                                | 109 us: 1.01x faster                                                            |
| sqlglot_v2_normalize             | 76.5 ms                                                               | 75.9 ms: 1.01x faster                                                           |
| 2to3                             | 186 ms                                                                | 185 ms: 1.01x faster                                                            |
| async_tree_cpu_io_mixed_tg       | 426 ms                                                                | 423 ms: 1.01x faster                                                            |
| django_template                  | 25.2 ms                                                               | 25.0 ms: 1.01x faster                                                           |
| scimark_monte_carlo              | 53.0 ms                                                               | 52.7 ms: 1.01x faster                                                           |
| bpe_tokeniser                    | 3.27 sec                                                              | 3.25 sec: 1.01x faster                                                          |
| create_gc_cycles                 | 1.36 ms                                                               | 1.35 ms: 1.00x faster                                                           |
| mako                             | 9.02 ms                                                               | 8.99 ms: 1.00x faster                                                           |
| json_loads                       | 16.6 us                                                               | 16.5 us: 1.00x faster                                                           |
| genshi_text                      | 17.6 ms                                                               | 17.6 ms: 1.00x faster                                                           |
| xml_etree_process                | 43.1 ms                                                               | 43.0 ms: 1.00x faster                                                           |
| sqlglot_v2_optimize              | 36.4 ms                                                               | 36.3 ms: 1.00x faster                                                           |
| logging_simple                   | 4.07 us                                                               | 4.06 us: 1.00x faster                                                           |
| mdp                              | 827 ms                                                                | 826 ms: 1.00x faster                                                            |
| coroutines                       | 19.3 ms                                                               | 19.3 ms: 1.00x faster                                                           |
| fannkuch                         | 310 ms                                                                | 311 ms: 1.00x slower                                                            |
| generators                       | 31.6 ms                                                               | 31.7 ms: 1.00x slower                                                           |
| python_startup_no_site           | 14.0 ms                                                               | 14.1 ms: 1.00x slower                                                           |
| sympy_integrate                  | 11.3 ms                                                               | 11.4 ms: 1.00x slower                                                           |
| comprehensions                   | 13.1 us                                                               | 13.2 us: 1.01x slower                                                           |
| async_generators                 | 274 ms                                                                | 275 ms: 1.01x slower                                                            |
| pprint_pformat                   | 1.27 sec                                                              | 1.28 sec: 1.01x slower                                                          |
| regex_dna                        | 143 ms                                                                | 144 ms: 1.01x slower                                                            |
| coverage                         | 336 ms                                                                | 338 ms: 1.01x slower                                                            |
| pprint_safe_repr                 | 624 ms                                                                | 629 ms: 1.01x slower                                                            |
| dask                             | 847 ms                                                                | 854 ms: 1.01x slower                                                            |
| regex_v8                         | 16.2 ms                                                               | 16.3 ms: 1.01x slower                                                           |
| deepcopy_memo                    | 21.8 us                                                               | 22.0 us: 1.01x slower                                                           |
| crypto_pyaes                     | 61.3 ms                                                               | 61.9 ms: 1.01x slower                                                           |
| regex_effbot                     | 2.34 ms                                                               | 2.37 ms: 1.01x slower                                                           |
| float                            | 57.5 ms                                                               | 58.5 ms: 1.02x slower                                                           |
| nbody                            | 84.9 ms                                                               | 86.7 ms: 1.02x slower                                                           |
| Geometric mean                   | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (56): async_tree_eager_io, sphinx, async_tree_none, async_tree_eager_memoization_tg, async_tree_none_tg, thrift, async_tree_io_tg, async_tree_eager_io_tg, async_tree_memoization, genshi_xml, async_tree_io, async_tree_eager_tg, async_tree_memoization_tg, docutils, hexiom, json_dumps, json, scimark_sor, python_startup, sqlglot_v2_parse, pycparser, sympy_expand, shortest_path, async_tree_cpu_io_mixed, deepcopy, pathlib, richards_super, logging_format, sqlglot_v2_transpile, deepcopy_reduce, subparsers, regex_compile, go, many_optionals, spectral_norm, sympy_str, richards, pyflate, unpickle_pure_python, asyncio_websockets, xml_etree_generate, pidigits, pickle_pure_python, scimark_lu, scimark_fft, nqueens, sqlite_synth, async_tree_eager_memoization, raytrace, connected_components, tomli_loads, telco, xml_etree_parse, k_core, pylint, html5lib

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 98.71% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x