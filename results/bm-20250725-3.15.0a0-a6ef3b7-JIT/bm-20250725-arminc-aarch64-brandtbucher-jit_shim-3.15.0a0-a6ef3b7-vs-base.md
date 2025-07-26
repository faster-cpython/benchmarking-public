# Results vs. base

- fork: brandtbucher
- ref: jit_shim
- machine: linux-aarch64
- commit hash: a6ef3b7
- commit date: 2025-07-25
- overall geometric mean: 1.003x faster
- HPT reliability: 99.25%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250725-arminc-aarch64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 | bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 311 ms                                                                  | 308 ms: 1.01x faster                                              |
| Geometric mean | (ref)                                                                   | 1.01x faster                                                      |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (11): coroutines, async_generators, async_tree_none_tg, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_none

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250725-arminc-aarch64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 | bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 125 ms                                                                  | 120 ms: 1.04x faster                                              |
| regex_dna      | 218 ms                                                                  | 221 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                      |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

Benchmark hidden because not significant (9): xml_etree_process, unpickle_pure_python, pickle_pure_python, json_loads, json_dumps, tomli_loads, xml_etree_iterparse, xml_etree_parse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250725-arminc-aarch64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 | bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|------------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup_no_site | 8.56 ms                                                                 | 8.62 ms: 1.01x slower                                             |
| Geometric mean         | (ref)                                                                   | 1.00x slower                                                      |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250725-arminc-aarch64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 | bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_xml     | 64.8 ms                                                                 | 62.0 ms: 1.05x faster                                             |
| genshi_text    | 27.3 ms                                                                 | 26.4 ms: 1.03x faster                                             |
| mako           | 13.0 ms                                                                 | 12.8 ms: 1.02x faster                                             |
| Geometric mean | (ref)                                                                   | 1.02x faster                                                      |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark              | bm-20250725-arminc-aarch64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 | bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|------------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_xml             | 64.8 ms                                                                 | 62.0 ms: 1.05x faster                                             |
| regex_compile          | 125 ms                                                                  | 120 ms: 1.04x faster                                              |
| richards               | 45.0 ms                                                                 | 43.3 ms: 1.04x faster                                             |
| mdp                    | 1.67 sec                                                                | 1.62 sec: 1.04x faster                                            |
| richards_super         | 51.5 ms                                                                 | 49.7 ms: 1.03x faster                                             |
| genshi_text            | 27.3 ms                                                                 | 26.4 ms: 1.03x faster                                             |
| pprint_pformat         | 2.30 sec                                                                | 2.24 sec: 1.03x faster                                            |
| pprint_safe_repr       | 1.14 sec                                                                | 1.11 sec: 1.03x faster                                            |
| sqlite_synth           | 3.71 us                                                                 | 3.61 us: 1.03x faster                                             |
| go                     | 154 ms                                                                  | 150 ms: 1.02x faster                                              |
| logging_format         | 7.68 us                                                                 | 7.55 us: 1.02x faster                                             |
| mako                   | 13.0 ms                                                                 | 12.8 ms: 1.02x faster                                             |
| hexiom                 | 7.52 ms                                                                 | 7.41 ms: 1.02x faster                                             |
| 2to3                   | 311 ms                                                                  | 308 ms: 1.01x faster                                              |
| python_startup_no_site | 8.56 ms                                                                 | 8.62 ms: 1.01x slower                                             |
| coverage               | 102 ms                                                                  | 103 ms: 1.01x slower                                              |
| pyflate                | 536 ms                                                                  | 541 ms: 1.01x slower                                              |
| connected_components   | 565 ms                                                                  | 570 ms: 1.01x slower                                              |
| regex_dna              | 218 ms                                                                  | 221 ms: 1.01x slower                                              |
| Geometric mean         | (ref)                                                                   | 1.01x faster                                                      |

Benchmark hidden because not significant (74): sqlglot_v2_normalize, html5lib, logging_silent, xml_etree_process, nbody, scimark_sor, deepcopy_memo, unpickle_pure_python, chaos, deepcopy_reduce, pickle_pure_python, coroutines, scimark_monte_carlo, comprehensions, scimark_lu, sqlglot_v2_parse, sympy_integrate, sqlglot_v2_optimize, json_loads, async_generators, spectral_norm, sympy_sum, pylint, scimark_sparse_mat_mult, gc_traversal, meteor_contest, pycparser, scimark_fft, raytrace, json_dumps, async_tree_none_tg, logging_simple, deltablue, shortest_path, async_tree_cpu_io_mixed_tg, asyncio_websockets, crypto_pyaes, docutils, python_startup, tomli_loads, async_tree_io, sqlglot_v2_transpile, dulwich_log, async_tree_io_tg, djangocms, xml_etree_iterparse, pidigits, bpe_tokeniser, async_tree_memoization, float, telco, pathlib, async_tree_cpu_io_mixed, generators, sympy_expand, xml_etree_parse, create_gc_cycles, many_optionals, k_core, subparsers, json, async_tree_memoization_tg, fannkuch, async_tree_none, sphinx, xml_etree_generate, deepcopy, nqueens, typing_runtime_protocols, sympy_str, regex_effbot, django_template, regex_v8, thrift

- Geometric mean (including insignificant results): 1.003x faster

# HPT report

- Reliability score: 99.25% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x