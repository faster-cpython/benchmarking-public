# Results vs. base

- fork: brandtbucher
- ref: nojit
- machine: linux-aarch64
- commit hash: f098037
- commit date: 2025-01-07
- overall geometric mean: 1.000x faster
- HPT reliability: 95.01%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (11): async_tree_cpu_io_mixed, async_tree_none, async_tree_memoization_tg, asyncio_websockets, async_tree_io, async_tree_memoization, coroutines, async_tree_io_tg, async_generators, async_tree_cpu_io_mixed_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250106-arminc-aarch64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 122 ms                                                                   | 114 ms: 1.07x faster                                            |
| Geometric mean | (ref)                                                                    | 1.01x faster                                                    |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

Benchmark hidden because not significant (4): regex_dna, regex_effbot, regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

Benchmark hidden because not significant (9): xml_etree_iterparse, pickle_pure_python, json_dumps, xml_etree_parse, xml_etree_process, json_loads, unpickle_pure_python, tomli_loads, xml_etree_generate

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_xml, genshi_text, mako, django_template

All benchmarks:
===============

| Benchmark              | bm-20250106-arminc-aarch64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody                  | 122 ms                                                                   | 114 ms: 1.07x faster                                            |
| fannkuch               | 540 ms                                                                   | 507 ms: 1.07x faster                                            |
| bpe_tokeniser          | 5.81 sec                                                                 | 5.87 sec: 1.01x slower                                          |
| sqlglot_parse          | 1.52 ms                                                                  | 1.61 ms: 1.06x slower                                           |
| many_optionals         | 816 us                                                                   | 867 us: 1.06x slower                                            |
| sqlalchemy_declarative | 151 ms                                                                   | 164 ms: 1.09x slower                                            |
| Geometric mean         | (ref)                                                                    | 1.01x slower                                                    |

Benchmark hidden because not significant (91): xml_etree_iterparse, regex_dna, spectral_norm, regex_effbot, pickle_pure_python, bench_thread_pool, sympy_integrate, sqlglot_normalize, typing_runtime_protocols, create_gc_cycles, nqueens, chaos, json_dumps, k_core, xml_etree_parse, pycparser, xml_etree_process, pathlib, scimark_sor, raytrace, json_loads, connected_components, pyflate, thrift, regex_compile, logging_format, logging_simple, hexiom, docutils, generators, pprint_safe_repr, logging_silent, async_tree_cpu_io_mixed, mdp, regex_v8, sqlglot_transpile, json, pprint_pformat, 2to3, genshi_xml, crypto_pyaes, async_tree_none, unpickle_pure_python, gc_traversal, tomli_loads, async_tree_memoization_tg, deltablue, python_startup, telco, asyncio_websockets, scimark_fft, pylint, scimark_lu, deepcopy_memo, genshi_text, scimark_monte_carlo, mako, async_tree_io, async_tree_memoization, sphinx, subparsers, sqlite_synth, django_template, meteor_contest, mypy2, coroutines, pidigits, sympy_str, deepcopy_reduce, sqlglot_optimize, async_tree_io_tg, comprehensions, python_startup_no_site, sympy_expand, go, coverage, shortest_path, async_generators, async_tree_cpu_io_mixed_tg, sqlalchemy_imperative, sympy_sum, dulwich_log, deepcopy, async_tree_none_tg, scimark_sparse_mat_mult, richards, float, richards_super, html5lib, xml_etree_generate, bench_mp_pool

- Geometric mean (including insignificant results): 1.000x faster

# HPT report

- Reliability score: 95.01% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x