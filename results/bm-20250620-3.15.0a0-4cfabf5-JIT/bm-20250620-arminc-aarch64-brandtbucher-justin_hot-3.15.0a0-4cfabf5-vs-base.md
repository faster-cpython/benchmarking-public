# Results vs. base

- fork: brandtbucher
- ref: justin_hot
- machine: linux-aarch64
- commit hash: 4cfabf5
- commit date: 2025-06-20
- overall geometric mean: 1.002x faster
- HPT reliability: 97.25%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250620-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|-------------------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_generators        | 500 ms                                                                  | 480 ms: 1.04x faster                                                |
| async_tree_none_tg      | 382 ms                                                                  | 378 ms: 1.01x faster                                                |
| async_tree_cpu_io_mixed | 667 ms                                                                  | 660 ms: 1.01x faster                                                |
| Geometric mean          | (ref)                                                                   | 1.01x faster                                                        |

Benchmark hidden because not significant (8): async_tree_memoization_tg, asyncio_websockets, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_none, async_tree_memoization, coroutines

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): pidigits, float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250620-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_dna      | 225 ms                                                                  | 220 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                                   | 1.02x faster                                                        |

Benchmark hidden because not significant (3): regex_effbot, regex_v8, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250620-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|--------------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_generate | 112 ms                                                                  | 108 ms: 1.04x faster                                                |
| tomli_loads        | 2.34 sec                                                                | 2.38 sec: 1.02x slower                                              |
| Geometric mean     | (ref)                                                                   | 1.01x slower                                                        |

Benchmark hidden because not significant (7): xml_etree_parse, pickle_pure_python, xml_etree_process, xml_etree_iterparse, json_loads, unpickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_text, mako, genshi_xml, django_template

All benchmarks:
===============

| Benchmark               | bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250620-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|-------------------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nqueens                 | 106 ms                                                                  | 100 ms: 1.06x faster                                                |
| dulwich_log             | 56.1 ms                                                                 | 53.3 ms: 1.05x faster                                               |
| xml_etree_generate      | 112 ms                                                                  | 108 ms: 1.04x faster                                                |
| async_generators        | 500 ms                                                                  | 480 ms: 1.04x faster                                                |
| shortest_path           | 600 ms                                                                  | 587 ms: 1.02x faster                                                |
| regex_dna               | 225 ms                                                                  | 220 ms: 1.02x faster                                                |
| pyflate                 | 539 ms                                                                  | 529 ms: 1.02x faster                                                |
| pprint_safe_repr        | 1.26 sec                                                                | 1.25 sec: 1.01x faster                                              |
| async_tree_none_tg      | 382 ms                                                                  | 378 ms: 1.01x faster                                                |
| async_tree_cpu_io_mixed | 667 ms                                                                  | 660 ms: 1.01x faster                                                |
| logging_format          | 8.29 us                                                                 | 8.36 us: 1.01x slower                                               |
| deltablue               | 3.87 ms                                                                 | 3.91 ms: 1.01x slower                                               |
| pprint_pformat          | 2.54 sec                                                                | 2.58 sec: 1.01x slower                                              |
| tomli_loads             | 2.34 sec                                                                | 2.38 sec: 1.02x slower                                              |
| Geometric mean          | (ref)                                                                   | 1.00x faster                                                        |

Benchmark hidden because not significant (79): sqlite_synth, regex_effbot, meteor_contest, thrift, deepcopy_memo, scimark_monte_carlo, telco, json, subparsers, chaos, scimark_lu, pylint, k_core, create_gc_cycles, scimark_fft, deepcopy_reduce, fannkuch, async_tree_memoization_tg, scimark_sor, regex_v8, pidigits, asyncio_websockets, async_tree_io_tg, mdp, python_startup_no_site, raytrace, xml_etree_parse, logging_silent, deepcopy, go, scimark_sparse_mat_mult, gc_traversal, async_tree_cpu_io_mixed_tg, float, bpe_tokeniser, async_tree_io, connected_components, 2to3, python_startup, djangocms, sphinx, pickle_pure_python, regex_compile, sympy_sum, genshi_text, mako, async_tree_none, async_tree_memoization, hexiom, xml_etree_process, xml_etree_iterparse, coroutines, json_loads, docutils, logging_simple, nbody, html5lib, sqlglot_v2_transpile, sqlglot_v2_parse, sympy_str, richards, sqlglot_v2_normalize, sympy_expand, pycparser, genshi_xml, coverage, generators, many_optionals, sympy_integrate, sqlglot_v2_optimize, comprehensions, spectral_norm, pathlib, unpickle_pure_python, typing_runtime_protocols, crypto_pyaes, richards_super, django_template, json_dumps

- Geometric mean (including insignificant results): 1.002x faster

# HPT report

- Reliability score: 97.25% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x