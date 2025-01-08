# Results vs. base

- fork: brandtbucher
- ref: nojit
- machine: linux-aarch64
- commit hash: f098037
- commit date: 2025-01-07
- overall geometric mean: 1.001x faster
- HPT reliability: 82.75%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (11): coroutines, async_tree_memoization, async_generators, async_tree_cpu_io_mixed, async_tree_none, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_memoization_tg, async_tree_io_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250106-arminc-aarch64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_dna      | 255 ms                                                                   | 245 ms: 1.04x faster                                            |
| Geometric mean | (ref)                                                                    | 1.01x faster                                                    |

Benchmark hidden because not significant (3): regex_compile, regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

Benchmark hidden because not significant (9): xml_etree_generate, json_dumps, pickle_pure_python, xml_etree_iterparse, xml_etree_parse, tomli_loads, json_loads, unpickle_pure_python, xml_etree_process

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): mako, genshi_xml, genshi_text, django_template

All benchmarks:
===============

| Benchmark              | bm-20250106-arminc-aarch64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------:|
| bench_mp_pool          | 5.02 sec                                                                 | 3.47 sec: 1.45x faster                                          |
| coverage               | 108 ms                                                                   | 100 ms: 1.08x faster                                            |
| logging_simple         | 7.66 us                                                                  | 7.19 us: 1.06x faster                                           |
| regex_dna              | 255 ms                                                                   | 245 ms: 1.04x faster                                            |
| fannkuch               | 496 ms                                                                   | 478 ms: 1.04x faster                                            |
| subparsers             | 25.2 ms                                                                  | 25.7 ms: 1.02x slower                                           |
| thrift                 | 936 us                                                                   | 972 us: 1.04x slower                                            |
| sqlalchemy_declarative | 144 ms                                                                   | 151 ms: 1.04x slower                                            |
| Geometric mean         | (ref)                                                                    | 1.00x faster                                                    |

Benchmark hidden because not significant (89): richards, richards_super, hexiom, pyflate, bench_thread_pool, meteor_contest, typing_runtime_protocols, xml_etree_generate, pprint_safe_repr, scimark_lu, logging_silent, regex_compile, nqueens, coroutines, sympy_sum, json_dumps, async_tree_memoization, deepcopy_memo, gc_traversal, pprint_pformat, async_generators, pickle_pure_python, spectral_norm, chaos, telco, pathlib, sympy_expand, sphinx, deltablue, json, mypy2, async_tree_cpu_io_mixed, deepcopy_reduce, pylint, sqlalchemy_imperative, python_startup_no_site, docutils, mako, sympy_str, python_startup, bpe_tokeniser, regex_effbot, scimark_monte_carlo, async_tree_none, sqlglot_optimize, mdp, deepcopy, sqlglot_parse, go, asyncio_websockets, 2to3, logging_format, generators, xml_etree_iterparse, sqlglot_normalize, xml_etree_parse, connected_components, comprehensions, async_tree_cpu_io_mixed_tg, genshi_xml, raytrace, async_tree_io, float, tomli_loads, nbody, sympy_integrate, shortest_path, create_gc_cycles, async_tree_memoization_tg, async_tree_io_tg, sqlglot_transpile, crypto_pyaes, json_loads, k_core, unpickle_pure_python, scimark_sor, pidigits, dulwich_log, genshi_text, regex_v8, pycparser, scimark_fft, html5lib, async_tree_none_tg, many_optionals, scimark_sparse_mat_mult, xml_etree_process, django_template, sqlite_synth

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 82.75% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x