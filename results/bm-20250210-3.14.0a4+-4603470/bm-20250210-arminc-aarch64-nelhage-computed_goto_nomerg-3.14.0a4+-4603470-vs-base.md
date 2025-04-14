# Results vs. base

- fork: nelhage
- ref: computed_goto_nomerg
- machine: linux-aarch64
- commit hash: 4603470
- commit date: 2025-02-10
- overall geometric mean: 1.001x slower
- HPT reliability: 99.64%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250208-arminc-aarch64-python-c1f352bf0813803bb795-3.14.0a4+-c1f352b | bm-20250210-arminc-aarch64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| html5lib       | 61.6 ms                                                                  | 65.9 ms: 1.07x slower                                                     |
| Geometric mean | (ref)                                                                    | 1.02x slower                                                              |

Benchmark hidden because not significant (3): 2to3, docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (11): asyncio_websockets, async_tree_io_tg, coroutines, async_tree_cpu_io_mixed, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_memoization_tg, async_tree_io, async_generators, async_tree_memoization

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, nbody, pidigits

Benchmarks with tag 'regex':
============================

Benchmark hidden because not significant (4): regex_effbot, regex_dna, regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

Benchmark hidden because not significant (9): json_dumps, pickle_pure_python, xml_etree_process, unpickle_pure_python, xml_etree_parse, tomli_loads, json_loads, xml_etree_iterparse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_text, mako, genshi_xml, django_template

All benchmarks:
===============

| Benchmark      | bm-20250208-arminc-aarch64-python-c1f352bf0813803bb795-3.14.0a4+-c1f352b | bm-20250210-arminc-aarch64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| html5lib       | 61.6 ms                                                                  | 65.9 ms: 1.07x slower                                                     |
| pathlib        | 21.6 ms                                                                  | 23.1 ms: 1.07x slower                                                     |
| coverage       | 98.3 ms                                                                  | 105 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                                    | 1.00x slower                                                              |

Benchmark hidden because not significant (93): bench_mp_pool, sqlite_synth, create_gc_cycles, genshi_text, richards_super, deepcopy_reduce, json_dumps, thrift, mako, spectral_norm, subparsers, regex_effbot, pickle_pure_python, pyflate, xml_etree_process, crypto_pyaes, dulwich_log, unpickle_pure_python, regex_dna, json, chaos, comprehensions, telco, asyncio_websockets, raytrace, deltablue, deepcopy, logging_silent, hexiom, sqlglot_parse, scimark_fft, pylint, bpe_tokeniser, mdp, k_core, async_tree_io_tg, xml_etree_parse, tomli_loads, docutils, float, meteor_contest, sqlglot_optimize, python_startup_no_site, scimark_sparse_mat_mult, sphinx, coroutines, sympy_str, python_startup, regex_compile, logging_simple, async_tree_cpu_io_mixed, typing_runtime_protocols, bench_thread_pool, many_optionals, json_loads, pprint_pformat, async_tree_none, generators, sympy_sum, async_tree_cpu_io_mixed_tg, scimark_lu, 2to3, async_tree_none_tg, async_tree_memoization_tg, connected_components, nbody, scimark_monte_carlo, sqlglot_normalize, logging_format, fannkuch, sqlalchemy_imperative, sympy_integrate, sympy_expand, pycparser, async_tree_io, scimark_sor, async_generators, shortest_path, genshi_xml, pprint_safe_repr, async_tree_memoization, sqlglot_transpile, deepcopy_memo, go, gc_traversal, sqlalchemy_declarative, nqueens, xml_etree_iterparse, pidigits, regex_v8, django_template, xml_etree_generate, richards

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 99.64% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x