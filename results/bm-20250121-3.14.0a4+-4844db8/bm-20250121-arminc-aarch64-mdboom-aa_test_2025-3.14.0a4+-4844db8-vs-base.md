# Results vs. base

- fork: mdboom
- ref: aa_test_2025
- machine: linux-aarch64
- commit hash: 4844db8
- commit date: 2025-01-21
- overall geometric mean: 1.001x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250121-arminc-aarch64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------:|
| docutils       | 3.08 sec                                                                 | 3.01 sec: 1.02x faster                                           |
| html5lib       | 66.3 ms                                                                  | 63.0 ms: 1.05x faster                                            |
| Geometric mean | (ref)                                                                    | 1.02x faster                                                     |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (11): async_tree_none, async_tree_memoization, coroutines, async_generators, async_tree_cpu_io_mixed, async_tree_io_tg, asyncio_websockets, async_tree_io, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, pidigits, float

Benchmarks with tag 'regex':
============================

Benchmark hidden because not significant (4): regex_dna, regex_compile, regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

Benchmark hidden because not significant (9): json_dumps, json_loads, tomli_loads, xml_etree_parse, xml_etree_generate, pickle_pure_python, xml_etree_iterparse, xml_etree_process, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_xml, django_template, mako, genshi_text

All benchmarks:
===============

| Benchmark      | bm-20250121-arminc-aarch64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------:|
| crypto_pyaes   | 90.9 ms                                                                  | 85.0 ms: 1.07x faster                                            |
| coverage       | 106 ms                                                                   | 99.6 ms: 1.06x faster                                            |
| html5lib       | 66.3 ms                                                                  | 63.0 ms: 1.05x faster                                            |
| subparsers     | 27.1 ms                                                                  | 25.9 ms: 1.05x faster                                            |
| docutils       | 3.08 sec                                                                 | 3.01 sec: 1.02x faster                                           |
| bpe_tokeniser  | 5.73 sec                                                                 | 5.68 sec: 1.01x faster                                           |
| sympy_str      | 265 ms                                                                   | 279 ms: 1.05x slower                                             |
| pathlib        | 21.3 ms                                                                  | 22.6 ms: 1.06x slower                                            |
| Geometric mean | (ref)                                                                    | 1.01x faster                                                     |

Benchmark hidden because not significant (88): json_dumps, logging_format, richards_super, comprehensions, sqlglot_normalize, create_gc_cycles, typing_runtime_protocols, deltablue, nbody, many_optionals, sympy_sum, meteor_contest, async_tree_none, richards, async_tree_memoization, deepcopy_reduce, pycparser, json_loads, regex_dna, genshi_xml, coroutines, generators, django_template, shortest_path, fannkuch, logging_simple, logging_silent, telco, sqlglot_transpile, mako, pidigits, tomli_loads, k_core, pprint_safe_repr, pprint_pformat, go, sphinx, deepcopy, 2to3, async_generators, scimark_fft, float, spectral_norm, python_startup, async_tree_cpu_io_mixed, async_tree_io_tg, dulwich_log, connected_components, mdp, raytrace, sympy_integrate, asyncio_websockets, sympy_expand, pyflate, deepcopy_memo, genshi_text, xml_etree_parse, xml_etree_generate, async_tree_io, hexiom, sqlalchemy_declarative, async_tree_none_tg, scimark_sor, async_tree_cpu_io_mixed_tg, regex_compile, json, gc_traversal, thrift, python_startup_no_site, sqlglot_optimize, pickle_pure_python, scimark_lu, chaos, xml_etree_iterparse, regex_v8, async_tree_memoization_tg, xml_etree_process, sqlite_synth, bench_thread_pool, sqlglot_parse, unpickle_pure_python, regex_effbot, scimark_monte_carlo, nqueens, scimark_sparse_mat_mult, pylint, sqlalchemy_imperative, bench_mp_pool

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x