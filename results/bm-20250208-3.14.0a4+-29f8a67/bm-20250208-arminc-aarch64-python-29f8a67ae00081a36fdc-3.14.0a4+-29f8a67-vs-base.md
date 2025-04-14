# Results vs. base

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: linux-aarch64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.000x slower
- HPT reliability: 99.52%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (11): asyncio_websockets, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_generators, async_tree_cpu_io_mixed, async_tree_none_tg, coroutines, async_tree_io, async_tree_memoization_tg, async_tree_none, async_tree_memoization

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, float, pidigits

Benchmarks with tag 'regex':
============================

Benchmark hidden because not significant (4): regex_dna, regex_effbot, regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

Benchmark hidden because not significant (9): pickle_pure_python, xml_etree_process, json_dumps, unpickle_pure_python, tomli_loads, xml_etree_parse, xml_etree_generate, json_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_text, mako, django_template, genshi_xml

All benchmarks:
===============

| Benchmark      | bm-20250208-arminc-aarch64-python-c1f352bf0813803bb795-3.14.0a4+-c1f352b | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pyflate        | 575 ms                                                                   | 552 ms: 1.04x faster                                                     |
| mdp            | 3.40 sec                                                                 | 3.35 sec: 1.01x faster                                                   |
| sympy_str      | 260 ms                                                                   | 261 ms: 1.01x slower                                                     |
| gc_traversal   | 6.54 ms                                                                  | 7.01 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                                    | 1.01x slower                                                             |

Benchmark hidden because not significant (92): create_gc_cycles, pickle_pure_python, sqlite_synth, deepcopy, sqlglot_optimize, telco, logging_silent, spectral_norm, genshi_text, richards_super, mako, xml_etree_process, typing_runtime_protocols, regex_dna, scimark_sparse_mat_mult, nbody, subparsers, sympy_sum, dulwich_log, json_dumps, asyncio_websockets, meteor_contest, k_core, float, unpickle_pure_python, sqlglot_parse, sphinx, connected_components, pprint_safe_repr, tomli_loads, docutils, comprehensions, crypto_pyaes, deltablue, pycparser, regex_effbot, pylint, regex_compile, raytrace, sympy_expand, logging_simple, python_startup_no_site, json, nqueens, go, pprint_pformat, bpe_tokeniser, async_tree_io_tg, python_startup, chaos, async_tree_cpu_io_mixed_tg, hexiom, richards, async_generators, async_tree_cpu_io_mixed, generators, async_tree_none_tg, fannkuch, xml_etree_parse, 2to3, bench_thread_pool, regex_v8, pathlib, deepcopy_reduce, sqlalchemy_declarative, deepcopy_memo, sympy_integrate, xml_etree_generate, coroutines, shortest_path, async_tree_io, thrift, json_loads, html5lib, xml_etree_iterparse, async_tree_memoization_tg, scimark_sor, django_template, async_tree_none, many_optionals, sqlglot_normalize, pidigits, scimark_lu, async_tree_memoization, sqlalchemy_imperative, logging_format, scimark_fft, genshi_xml, scimark_monte_carlo, sqlglot_transpile, coverage, bench_mp_pool
Ignored benchmarks (8) of results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.000x slower

# HPT report

- Reliability score: 99.52% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x