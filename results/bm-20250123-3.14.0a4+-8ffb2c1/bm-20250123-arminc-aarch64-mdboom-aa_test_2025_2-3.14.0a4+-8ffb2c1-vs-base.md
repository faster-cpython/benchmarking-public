# Results vs. base

- fork: mdboom
- ref: aa_test_2025_2
- machine: linux-aarch64
- commit hash: 8ffb2c1
- commit date: 2025-01-23
- overall geometric mean: 1.002x faster
- HPT reliability: 98.79%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (11): coroutines, async_tree_none, async_tree_memoization, async_generators, async_tree_io_tg, async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250121-arminc-aarch64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 125 ms                                                                   | 117 ms: 1.07x faster                                               |
| float          | 86.3 ms                                                                  | 85.0 ms: 1.02x faster                                              |
| Geometric mean | (ref)                                                                    | 1.04x faster                                                       |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

Benchmark hidden because not significant (4): regex_v8, regex_effbot, regex_compile, regex_dna

Benchmarks with tag 'serialize':
================================

Benchmark hidden because not significant (9): json_dumps, json_loads, xml_etree_parse, xml_etree_generate, tomli_loads, pickle_pure_python, xml_etree_iterparse, xml_etree_process, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): mako, genshi_xml, genshi_text, django_template

All benchmarks:
===============

| Benchmark             | bm-20250121-arminc-aarch64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|-----------------------|:------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| crypto_pyaes          | 90.9 ms                                                                  | 84.5 ms: 1.08x faster                                              |
| nbody                 | 125 ms                                                                   | 117 ms: 1.07x faster                                               |
| coverage              | 106 ms                                                                   | 99.5 ms: 1.06x faster                                              |
| many_optionals        | 756 us                                                                   | 713 us: 1.06x faster                                               |
| fannkuch              | 500 ms                                                                   | 480 ms: 1.04x faster                                               |
| float                 | 86.3 ms                                                                  | 85.0 ms: 1.02x faster                                              |
| sqlalchemy_imperative | 15.3 ms                                                                  | 16.1 ms: 1.05x slower                                              |
| pathlib               | 21.3 ms                                                                  | 22.4 ms: 1.05x slower                                              |
| bench_mp_pool         | 3.86 sec                                                                 | 6.60 sec: 1.71x slower                                             |
| Geometric mean        | (ref)                                                                    | 1.00x faster                                                       |

Benchmark hidden because not significant (87): richards_super, coroutines, json_dumps, logging_format, json_loads, meteor_contest, go, typing_runtime_protocols, sqlglot_transpile, richards, async_tree_none, spectral_norm, html5lib, deepcopy, sympy_sum, sympy_integrate, thrift, pidigits, pycparser, scimark_lu, telco, comprehensions, pprint_pformat, pylint, xml_etree_parse, scimark_sparse_mat_mult, deepcopy_memo, xml_etree_generate, docutils, pprint_safe_repr, dulwich_log, sympy_expand, raytrace, logging_silent, mako, create_gc_cycles, k_core, nqueens, tomli_loads, async_tree_memoization, async_generators, shortest_path, pickle_pure_python, json, deepcopy_reduce, bpe_tokeniser, scimark_monte_carlo, sqlglot_optimize, sphinx, scimark_fft, subparsers, hexiom, async_tree_io_tg, xml_etree_iterparse, chaos, async_tree_none_tg, async_tree_memoization_tg, sympy_str, python_startup_no_site, logging_simple, python_startup, async_tree_cpu_io_mixed_tg, xml_etree_process, async_tree_cpu_io_mixed, mdp, asyncio_websockets, genshi_xml, async_tree_io, regex_v8, sqlglot_parse, regex_effbot, genshi_text, 2to3, sqlalchemy_declarative, sqlglot_normalize, connected_components, deltablue, generators, regex_compile, bench_thread_pool, scimark_sor, regex_dna, sqlite_synth, pyflate, unpickle_pure_python, gc_traversal, django_template

- Geometric mean (including insignificant results): 1.002x faster

# HPT report

- Reliability score: 98.79% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x