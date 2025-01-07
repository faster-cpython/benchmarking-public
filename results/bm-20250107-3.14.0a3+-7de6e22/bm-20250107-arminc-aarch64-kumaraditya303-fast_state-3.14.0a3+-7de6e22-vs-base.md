# Results vs. base

- fork: kumaraditya303
- ref: fast_state
- machine: linux-aarch64
- commit hash: 7de6e22
- commit date: 2025-01-07
- overall geometric mean: 1.001x faster
- HPT reliability: 97.12%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark      | bm-20250105-arminc-aarch64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io  | 913 ms                                                                   | 888 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                                    | 1.01x faster                                                           |

Benchmark hidden because not significant (10): async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_none, async_tree_io_tg, async_tree_cpu_io_mixed, coroutines, async_tree_memoization_tg, asyncio_websockets, async_generators

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, pidigits, float

Benchmarks with tag 'regex':
============================

Benchmark hidden because not significant (4): regex_compile, regex_v8, regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

Benchmark hidden because not significant (9): json_dumps, xml_etree_process, json_loads, unpickle_pure_python, tomli_loads, xml_etree_generate, xml_etree_iterparse, xml_etree_parse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250105-arminc-aarch64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|-----------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 42.5 ms                                                                  | 40.5 ms: 1.05x faster                                                  |
| Geometric mean  | (ref)                                                                    | 1.02x faster                                                           |

Benchmark hidden because not significant (3): genshi_text, mako, genshi_xml

All benchmarks:
===============

| Benchmark       | bm-20250105-arminc-aarch64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|-----------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pylint          | 325 ms                                                                   | 307 ms: 1.06x faster                                                   |
| django_template | 42.5 ms                                                                  | 40.5 ms: 1.05x faster                                                  |
| shortest_path   | 591 ms                                                                   | 569 ms: 1.04x faster                                                   |
| async_tree_io   | 913 ms                                                                   | 888 ms: 1.03x faster                                                   |
| k_core          | 2.86 sec                                                                 | 2.94 sec: 1.03x slower                                                 |
| nqueens         | 103 ms                                                                   | 107 ms: 1.04x slower                                                   |
| bench_mp_pool   | 3.96 sec                                                                 | 5.70 sec: 1.44x slower                                                 |
| Geometric mean  | (ref)                                                                    | 1.00x faster                                                           |

Benchmark hidden because not significant (90): pathlib, nbody, gc_traversal, genshi_text, richards, sqlglot_optimize, json_dumps, async_tree_memoization, xml_etree_process, regex_compile, json_loads, python_startup_no_site, json, coverage, meteor_contest, async_tree_cpu_io_mixed_tg, chaos, connected_components, deepcopy, sqlite_synth, python_startup, async_tree_none_tg, create_gc_cycles, generators, unpickle_pure_python, sympy_integrate, deepcopy_reduce, sqlalchemy_imperative, deepcopy_memo, mako, async_tree_none, sympy_expand, async_tree_io_tg, logging_simple, scimark_sor, 2to3, scimark_lu, mdp, logging_silent, sqlalchemy_declarative, async_tree_cpu_io_mixed, sqlglot_parse, comprehensions, typing_runtime_protocols, pprint_pformat, pprint_safe_repr, coroutines, regex_v8, scimark_fft, deltablue, tomli_loads, sympy_str, sqlglot_transpile, xml_etree_generate, xml_etree_iterparse, sphinx, dulwich_log, async_tree_memoization_tg, mypy2, genshi_xml, spectral_norm, bpe_tokeniser, pycparser, sympy_sum, logging_format, fannkuch, telco, asyncio_websockets, scimark_sparse_mat_mult, pidigits, docutils, richards_super, xml_etree_parse, regex_effbot, float, bench_thread_pool, thrift, async_generators, raytrace, hexiom, many_optionals, pickle_pure_python, regex_dna, subparsers, crypto_pyaes, go, sqlglot_normalize, pyflate, scimark_monte_carlo, html5lib

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 97.12% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x