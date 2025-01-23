# Results vs. base

- fork: mdboom
- ref: aa_test_2025_2
- machine: linux-aarch64
- commit hash: 8ffb2c1
- commit date: 2025-01-23
- overall geometric mean: 1.001x faster
- HPT reliability: 99.85%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (11): async_tree_none, async_tree_memoization, async_tree_none_tg, async_generators, async_tree_cpu_io_mixed_tg, coroutines, async_tree_io_tg, async_tree_io, asyncio_websockets, async_tree_memoization_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): pidigits, nbody, float

Benchmarks with tag 'regex':
============================

Benchmark hidden because not significant (4): regex_v8, regex_compile, regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

Benchmark hidden because not significant (9): json_loads, xml_etree_process, unpickle_pure_python, json_dumps, xml_etree_generate, pickle_pure_python, tomli_loads, xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_text, genshi_xml, mako, django_template

All benchmarks:
===============

| Benchmark       | bm-20250121-arminc-aarch64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|-----------------|:------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| dulwich_log     | 76.2 ms                                                                  | 70.5 ms: 1.08x faster                                              |
| sympy_sum       | 195 ms                                                                   | 190 ms: 1.03x faster                                               |
| k_core          | 3.23 sec                                                                 | 3.20 sec: 1.01x faster                                             |
| sympy_integrate | 27.8 ms                                                                  | 29.2 ms: 1.05x slower                                              |
| Geometric mean  | (ref)                                                                    | 1.00x faster                                                       |

Benchmark hidden because not significant (92): comprehensions, scimark_monte_carlo, deltablue, scimark_lu, html5lib, scimark_sparse_mat_mult, deepcopy_memo, crypto_pyaes, logging_simple, logging_format, json_loads, genshi_text, pidigits, thrift, xml_etree_process, meteor_contest, sqlglot_normalize, unpickle_pure_python, pprint_safe_repr, async_tree_none, logging_silent, json_dumps, 2to3, deepcopy, gc_traversal, xml_etree_generate, richards_super, pyflate, async_tree_memoization, fannkuch, sqlglot_parse, pprint_pformat, coverage, pycparser, nqueens, genshi_xml, deepcopy_reduce, sqlglot_optimize, regex_v8, async_tree_none_tg, pathlib, spectral_norm, connected_components, sphinx, go, sympy_expand, async_generators, chaos, pylint, many_optionals, subparsers, pickle_pure_python, sqlite_synth, async_tree_cpu_io_mixed_tg, python_startup_no_site, scimark_fft, bench_mp_pool, tomli_loads, coroutines, bpe_tokeniser, json, sympy_str, telco, regex_compile, docutils, async_tree_io_tg, async_tree_io, shortest_path, raytrace, asyncio_websockets, nbody, async_tree_memoization_tg, python_startup, mdp, async_tree_cpu_io_mixed, xml_etree_parse, scimark_sor, sqlalchemy_imperative, bench_thread_pool, hexiom, richards, xml_etree_iterparse, mako, sqlglot_transpile, generators, sqlalchemy_declarative, django_template, create_gc_cycles, regex_effbot, typing_runtime_protocols, float, regex_dna

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 99.85% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x