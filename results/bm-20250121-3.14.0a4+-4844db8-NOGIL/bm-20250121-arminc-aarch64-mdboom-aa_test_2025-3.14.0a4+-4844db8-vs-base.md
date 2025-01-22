# Results vs. base

- fork: mdboom
- ref: aa_test_2025
- machine: linux-aarch64
- commit hash: 4844db8
- commit date: 2025-01-21
- overall geometric mean: 1.000x faster
- HPT reliability: 85.43%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250121-arminc-aarch64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------:|
| sphinx         | 1.39 sec                                                                 | 1.45 sec: 1.04x slower                                           |
| Geometric mean | (ref)                                                                    | 1.00x slower                                                     |

Benchmark hidden because not significant (3): 2to3, docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20250121-arminc-aarch64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|------------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_generators | 539 ms                                                                   | 566 ms: 1.05x slower                                             |
| Geometric mean   | (ref)                                                                    | 1.01x slower                                                     |

Benchmark hidden because not significant (10): async_tree_memoization, async_tree_io_tg, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_none, async_tree_io, coroutines, async_tree_cpu_io_mixed, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): pidigits, nbody, float

Benchmarks with tag 'regex':
============================

Benchmark hidden because not significant (4): regex_compile, regex_dna, regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

Benchmark hidden because not significant (9): xml_etree_parse, json_dumps, xml_etree_generate, pickle_pure_python, json_loads, unpickle_pure_python, xml_etree_iterparse, xml_etree_process, tomli_loads

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_text, genshi_xml, mako, django_template

All benchmarks:
===============

| Benchmark        | bm-20250121-arminc-aarch64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|------------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------:|
| dulwich_log      | 76.2 ms                                                                  | 70.1 ms: 1.09x faster                                            |
| pyflate          | 673 ms                                                                   | 654 ms: 1.03x faster                                             |
| json             | 6.43 ms                                                                  | 6.25 ms: 1.03x faster                                            |
| pprint_safe_repr | 1.19 sec                                                                 | 1.16 sec: 1.02x faster                                           |
| k_core           | 3.23 sec                                                                 | 3.19 sec: 1.01x faster                                           |
| bpe_tokeniser    | 7.43 sec                                                                 | 7.61 sec: 1.02x slower                                           |
| sphinx           | 1.39 sec                                                                 | 1.45 sec: 1.04x slower                                           |
| async_generators | 539 ms                                                                   | 566 ms: 1.05x slower                                             |
| Geometric mean   | (ref)                                                                    | 1.00x faster                                                     |

Benchmark hidden because not significant (88): comprehensions, scimark_sparse_mat_mult, bench_mp_pool, deepcopy_reduce, deepcopy_memo, richards, xml_etree_parse, genshi_text, json_dumps, crypto_pyaes, spectral_norm, pidigits, meteor_contest, nbody, genshi_xml, scimark_monte_carlo, scimark_lu, html5lib, deltablue, typing_runtime_protocols, fannkuch, gc_traversal, sympy_sum, async_tree_memoization, mako, xml_etree_generate, regex_compile, thrift, pickle_pure_python, pprint_pformat, logging_simple, json_loads, go, 2to3, unpickle_pure_python, sqlglot_parse, xml_etree_iterparse, pycparser, logging_format, sympy_str, async_tree_io_tg, docutils, sympy_integrate, xml_etree_process, sympy_expand, sqlglot_optimize, tomli_loads, pathlib, bench_thread_pool, asyncio_websockets, async_tree_cpu_io_mixed_tg, raytrace, pylint, chaos, async_tree_none_tg, generators, python_startup_no_site, connected_components, async_tree_none, sqlglot_transpile, sqlglot_normalize, async_tree_io, mdp, logging_silent, coverage, python_startup, django_template, many_optionals, scimark_fft, regex_dna, nqueens, richards_super, subparsers, shortest_path, deepcopy, hexiom, float, coroutines, sqlalchemy_imperative, scimark_sor, async_tree_cpu_io_mixed, create_gc_cycles, async_tree_memoization_tg, sqlalchemy_declarative, regex_effbot, telco, sqlite_synth, regex_v8

- Geometric mean (including insignificant results): 1.000x faster

# HPT report

- Reliability score: 85.43% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x