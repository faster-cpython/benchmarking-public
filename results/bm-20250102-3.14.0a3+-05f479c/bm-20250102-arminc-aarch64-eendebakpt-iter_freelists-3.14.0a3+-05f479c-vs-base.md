# Results vs. base

- fork: eendebakpt
- ref: iter_freelists
- machine: linux-aarch64
- commit hash: 05f479c
- commit date: 2025-01-02
- overall geometric mean: 1.000x faster
- HPT reliability: 99.79%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark      | bm-20250102-arminc-aarch64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-arminc-aarch64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io  | 904 ms                                                                   | 873 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                                    | 1.01x faster                                                           |

Benchmark hidden because not significant (10): async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_generators, async_tree_cpu_io_mixed, async_tree_memoization_tg, coroutines, asyncio_websockets, async_tree_none_tg

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): pidigits, float, nbody

Benchmarks with tag 'regex':
============================

Benchmark hidden because not significant (4): regex_v8, regex_dna, regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250102-arminc-aarch64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-arminc-aarch64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|--------------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python | 382 us                                                                   | 399 us: 1.05x slower                                                   |
| Geometric mean     | (ref)                                                                    | 1.00x faster                                                           |

Benchmark hidden because not significant (8): xml_etree_generate, xml_etree_process, unpickle_pure_python, xml_etree_parse, json_loads, tomli_loads, xml_etree_iterparse, json_dumps

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_xml, django_template, mako, genshi_text

All benchmarks:
===============

| Benchmark            | bm-20250102-arminc-aarch64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-arminc-aarch64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| sqlglot_normalize    | 132 ms                                                                   | 124 ms: 1.07x faster                                                   |
| sympy_str            | 275 ms                                                                   | 262 ms: 1.05x faster                                                   |
| async_tree_io        | 904 ms                                                                   | 873 ms: 1.04x faster                                                   |
| bpe_tokeniser        | 5.80 sec                                                                 | 5.62 sec: 1.03x faster                                                 |
| deepcopy_reduce      | 3.59 us                                                                  | 3.65 us: 1.02x slower                                                  |
| shortest_path        | 574 ms                                                                   | 588 ms: 1.03x slower                                                   |
| connected_components | 548 ms                                                                   | 567 ms: 1.03x slower                                                   |
| pickle_pure_python   | 382 us                                                                   | 399 us: 1.05x slower                                                   |
| Geometric mean       | (ref)                                                                    | 1.00x faster                                                           |

Benchmark hidden because not significant (90): xml_etree_generate, generators, sqlglot_optimize, sympy_expand, xml_etree_process, scimark_fft, async_tree_memoization, sympy_integrate, async_tree_none, pidigits, nqueens, subparsers, comprehensions, unpickle_pure_python, float, k_core, sympy_sum, sqlite_synth, create_gc_cycles, sphinx, dulwich_log, xml_etree_parse, regex_v8, meteor_contest, hexiom, async_tree_cpu_io_mixed_tg, scimark_monte_carlo, async_tree_io_tg, 2to3, regex_dna, nbody, async_generators, async_tree_cpu_io_mixed, async_tree_memoization_tg, bench_thread_pool, crypto_pyaes, genshi_xml, coroutines, docutils, python_startup_no_site, mdp, django_template, deltablue, json_loads, richards_super, tomli_loads, fannkuch, sqlglot_transpile, logging_silent, thrift, sqlglot_parse, djangocms, asyncio_websockets, scimark_lu, logging_format, gc_traversal, regex_compile, richards, deepcopy_memo, async_tree_none_tg, pycparser, mako, coverage, spectral_norm, pprint_safe_repr, regex_effbot, pathlib, xml_etree_iterparse, bench_mp_pool, telco, json_dumps, chaos, logging_simple, pylint, json, pprint_pformat, scimark_sor, mypy2, go, python_startup, typing_runtime_protocols, raytrace, genshi_text, deepcopy, html5lib, many_optionals, pyflate, sqlalchemy_imperative, sqlalchemy_declarative, scimark_sparse_mat_mult

- Geometric mean (including insignificant results): 1.000x faster

# HPT report

- Reliability score: 99.79% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x