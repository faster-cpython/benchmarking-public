# Results vs. base

- fork: kumaraditya303
- ref: future_iter
- machine: linux-aarch64
- commit hash: 82b905d
- commit date: 2025-01-05
- overall geometric mean: 1.004x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20250105-arminc-aarch64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250105-arminc-aarch64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|------------------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization | 508 ms                                                                   | 486 ms: 1.05x faster                                                    |
| async_tree_io          | 913 ms                                                                   | 875 ms: 1.04x faster                                                    |
| async_tree_io_tg       | 897 ms                                                                   | 862 ms: 1.04x faster                                                    |
| Geometric mean         | (ref)                                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed_tg, coroutines, async_tree_memoization_tg, async_tree_none, async_tree_cpu_io_mixed, async_tree_none_tg, asyncio_websockets, async_generators

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, float, pidigits

Benchmarks with tag 'regex':
============================

Benchmark hidden because not significant (4): regex_v8, regex_compile, regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

Benchmark hidden because not significant (9): json_loads, unpickle_pure_python, xml_etree_process, xml_etree_iterparse, pickle_pure_python, json_dumps, xml_etree_generate, xml_etree_parse, tomli_loads

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): mako, django_template, genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark               | bm-20250105-arminc-aarch64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250105-arminc-aarch64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|-------------------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| gc_traversal            | 7.24 ms                                                                  | 6.69 ms: 1.08x faster                                                   |
| pathlib                 | 23.3 ms                                                                  | 21.8 ms: 1.07x faster                                                   |
| scimark_sor             | 159 ms                                                                   | 151 ms: 1.06x faster                                                    |
| pylint                  | 325 ms                                                                   | 308 ms: 1.05x faster                                                    |
| async_tree_memoization  | 508 ms                                                                   | 486 ms: 1.05x faster                                                    |
| scimark_sparse_mat_mult | 6.51 ms                                                                  | 6.22 ms: 1.05x faster                                                   |
| shortest_path           | 591 ms                                                                   | 566 ms: 1.04x faster                                                    |
| async_tree_io           | 913 ms                                                                   | 875 ms: 1.04x faster                                                    |
| json                    | 5.74 ms                                                                  | 5.52 ms: 1.04x faster                                                   |
| async_tree_io_tg        | 897 ms                                                                   | 862 ms: 1.04x faster                                                    |
| mdp                     | 3.47 sec                                                                 | 3.42 sec: 1.02x faster                                                  |
| nqueens                 | 103 ms                                                                   | 104 ms: 1.01x slower                                                    |
| sympy_str               | 271 ms                                                                   | 286 ms: 1.06x slower                                                    |
| Geometric mean          | (ref)                                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (84): sqlite_synth, json_loads, create_gc_cycles, generators, regex_v8, unpickle_pure_python, logging_silent, xml_etree_process, sqlglot_transpile, many_optionals, async_tree_cpu_io_mixed_tg, sqlglot_parse, spectral_norm, coroutines, async_tree_memoization_tg, xml_etree_iterparse, scimark_lu, sympy_expand, sqlalchemy_imperative, async_tree_none, connected_components, typing_runtime_protocols, async_tree_cpu_io_mixed, fannkuch, python_startup_no_site, mako, django_template, thrift, deepcopy_memo, sqlglot_optimize, pprint_safe_repr, python_startup, pickle_pure_python, pprint_pformat, coverage, regex_compile, deepcopy_reduce, chaos, async_tree_none_tg, genshi_xml, 2to3, json_dumps, pycparser, regex_dna, mypy2, sphinx, nbody, bench_thread_pool, sympy_integrate, subparsers, richards, bpe_tokeniser, hexiom, k_core, pyflate, docutils, xml_etree_generate, xml_etree_parse, deltablue, scimark_fft, asyncio_websockets, tomli_loads, comprehensions, raytrace, regex_effbot, logging_format, sympy_sum, go, float, html5lib, meteor_contest, dulwich_log, sqlalchemy_declarative, logging_simple, genshi_text, pidigits, crypto_pyaes, async_generators, sqlglot_normalize, richards_super, scimark_monte_carlo, deepcopy, telco, bench_mp_pool

- Geometric mean (including insignificant results): 1.004x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x