# Results vs. base

- fork: faster-cpython
- ref: c_recursion_limit
- machine: linux-aarch64
- commit hash: 21366c3
- commit date: 2025-02-17
- overall geometric mean: 1.000x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20250214-arminc-aarch64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 | bm-20250217-arminc-aarch64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|------------------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization | 486 ms                                                                   | 504 ms: 1.04x slower                                                            |
| Geometric mean         | (ref)                                                                    | 1.01x slower                                                                    |

Benchmark hidden because not significant (10): coroutines, asyncio_websockets, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_generators, async_tree_none, async_tree_io_tg

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): pidigits, float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250214-arminc-aarch64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 | bm-20250217-arminc-aarch64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 248 ms                                                                   | 244 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                                    | 1.01x slower                                                                    |

Benchmark hidden because not significant (3): regex_compile, regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

Benchmark hidden because not significant (9): pickle_pure_python, unpickle_pure_python, json_loads, json_dumps, tomli_loads, xml_etree_parse, xml_etree_generate, xml_etree_process, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_text, mako, genshi_xml, django_template

All benchmarks:
===============

| Benchmark              | bm-20250214-arminc-aarch64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 | bm-20250217-arminc-aarch64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|------------------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna              | 248 ms                                                                   | 244 ms: 1.02x faster                                                            |
| bpe_tokeniser          | 5.60 sec                                                                 | 5.67 sec: 1.01x slower                                                          |
| async_tree_memoization | 486 ms                                                                   | 504 ms: 1.04x slower                                                            |
| pylint                 | 305 ms                                                                   | 329 ms: 1.08x slower                                                            |
| bench_mp_pool          | 5.29 sec                                                                 | 7.19 sec: 1.36x slower                                                          |
| Geometric mean         | (ref)                                                                    | 1.01x slower                                                                    |

Benchmark hidden because not significant (91): genshi_text, create_gc_cycles, pickle_pure_python, mako, pidigits, richards, generators, pyflate, bench_thread_pool, unpickle_pure_python, json_loads, coroutines, sqlalchemy_imperative, deepcopy_memo, json_dumps, float, logging_simple, logging_format, chaos, shortest_path, json, connected_components, sympy_str, mdp, deepcopy, deltablue, gc_traversal, meteor_contest, 2to3, asyncio_websockets, tomli_loads, xml_etree_parse, async_tree_io, sphinx, async_tree_cpu_io_mixed_tg, pprint_safe_repr, html5lib, async_tree_none_tg, scimark_sparse_mat_mult, subparsers, async_tree_memoization_tg, sqlalchemy_declarative, python_startup_no_site, regex_compile, xml_etree_generate, genshi_xml, regex_v8, nqueens, sqlglot_optimize, async_tree_cpu_io_mixed, richards_super, thrift, k_core, sqlglot_parse, comprehensions, deepcopy_reduce, nbody, dulwich_log, docutils, pycparser, pathlib, xml_etree_process, sympy_sum, scimark_lu, raytrace, async_generators, many_optionals, sympy_expand, async_tree_none, pprint_pformat, xml_etree_iterparse, python_startup, go, sqlite_synth, logging_silent, scimark_sor, async_tree_io_tg, fannkuch, sympy_integrate, coverage, scimark_fft, crypto_pyaes, typing_runtime_protocols, sqlglot_transpile, regex_effbot, spectral_norm, sqlglot_normalize, scimark_monte_carlo, hexiom, django_template, telco

- Geometric mean (including insignificant results): 1.000x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x