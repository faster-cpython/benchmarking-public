# Results vs. base

- fork: brandtbucher
- ref: jit_nops
- machine: linux-aarch64
- commit hash: 75922b6
- commit date: 2025-06-27
- overall geometric mean: 1.000x faster
- HPT reliability: 88.01%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250627-arminc-aarch64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| docutils       | 3.13 sec                                                                | 3.07 sec: 1.02x faster                                            |
| sphinx         | 1.14 sec                                                                | 1.17 sec: 1.02x slower                                            |
| Geometric mean | (ref)                                                                   | 1.00x slower                                                      |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark      | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250627-arminc-aarch64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_io  | 918 ms                                                                  | 905 ms: 1.02x faster                                              |
| Geometric mean | (ref)                                                                   | 1.00x slower                                                      |

Benchmark hidden because not significant (10): coroutines, async_tree_io_tg, async_tree_none, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_none_tg, asyncio_websockets, async_generators

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250627-arminc-aarch64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_v8       | 26.5 ms                                                                 | 26.6 ms: 1.01x slower                                             |
| Geometric mean | (ref)                                                                   | 1.00x slower                                                      |

Benchmark hidden because not significant (3): regex_compile, regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250627-arminc-aarch64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|---------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| json_dumps          | 13.5 ms                                                                 | 13.3 ms: 1.01x faster                                             |
| xml_etree_parse     | 178 ms                                                                  | 179 ms: 1.01x slower                                              |
| xml_etree_iterparse | 143 ms                                                                  | 144 ms: 1.01x slower                                              |
| pickle_pure_python  | 396 us                                                                  | 401 us: 1.01x slower                                              |
| Geometric mean      | (ref)                                                                   | 1.01x faster                                                      |

Benchmark hidden because not significant (5): unpickle_pure_python, xml_etree_process, json_loads, xml_etree_generate, tomli_loads

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250627-arminc-aarch64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_text    | 28.3 ms                                                                 | 26.7 ms: 1.06x faster                                             |
| Geometric mean | (ref)                                                                   | 1.01x faster                                                      |

Benchmark hidden because not significant (3): genshi_xml, django_template, mako

All benchmarks:
===============

| Benchmark            | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250627-arminc-aarch64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_text          | 28.3 ms                                                                 | 26.7 ms: 1.06x faster                                             |
| sqlglot_v2_normalize | 132 ms                                                                  | 126 ms: 1.05x faster                                              |
| telco                | 9.38 ms                                                                 | 9.08 ms: 1.03x faster                                             |
| meteor_contest       | 115 ms                                                                  | 113 ms: 1.02x faster                                              |
| docutils             | 3.13 sec                                                                | 3.07 sec: 1.02x faster                                            |
| async_tree_io        | 918 ms                                                                  | 905 ms: 1.02x faster                                              |
| json                 | 5.77 ms                                                                 | 5.69 ms: 1.01x faster                                             |
| json_dumps           | 13.5 ms                                                                 | 13.3 ms: 1.01x faster                                             |
| scimark_monte_carlo  | 80.3 ms                                                                 | 79.7 ms: 1.01x faster                                             |
| xml_etree_parse      | 178 ms                                                                  | 179 ms: 1.01x slower                                              |
| regex_v8             | 26.5 ms                                                                 | 26.6 ms: 1.01x slower                                             |
| xml_etree_iterparse  | 143 ms                                                                  | 144 ms: 1.01x slower                                              |
| logging_format       | 7.76 us                                                                 | 7.82 us: 1.01x slower                                             |
| pickle_pure_python   | 396 us                                                                  | 401 us: 1.01x slower                                              |
| sqlite_synth         | 3.66 us                                                                 | 3.72 us: 1.01x slower                                             |
| pyflate              | 531 ms                                                                  | 539 ms: 1.01x slower                                              |
| mdp                  | 1.66 sec                                                                | 1.68 sec: 1.01x slower                                            |
| connected_components | 563 ms                                                                  | 572 ms: 1.02x slower                                              |
| shortest_path        | 585 ms                                                                  | 594 ms: 1.02x slower                                              |
| sphinx               | 1.14 sec                                                                | 1.17 sec: 1.02x slower                                            |
| pprint_pformat       | 2.34 sec                                                                | 2.39 sec: 1.02x slower                                            |
| pprint_safe_repr     | 1.14 sec                                                                | 1.16 sec: 1.02x slower                                            |
| sympy_expand         | 478 ms                                                                  | 493 ms: 1.03x slower                                              |
| Geometric mean       | (ref)                                                                   | 1.00x faster                                                      |

Benchmark hidden because not significant (70): nqueens, sqlglot_v2_optimize, sympy_sum, thrift, dulwich_log, comprehensions, nbody, unpickle_pure_python, coroutines, chaos, scimark_sor, xml_etree_process, json_loads, sqlglot_v2_parse, coverage, raytrace, fannkuch, gc_traversal, async_tree_io_tg, scimark_fft, sqlglot_v2_transpile, crypto_pyaes, xml_etree_generate, richards_super, logging_simple, tomli_loads, pylint, scimark_sparse_mat_mult, sympy_integrate, richards, regex_compile, go, genshi_xml, 2to3, deepcopy_memo, sympy_str, async_tree_none, float, djangocms, logging_silent, html5lib, bpe_tokeniser, python_startup_no_site, python_startup, async_tree_memoization, spectral_norm, django_template, pathlib, pycparser, async_tree_cpu_io_mixed_tg, hexiom, mako, async_tree_memoization_tg, regex_dna, k_core, deltablue, async_tree_cpu_io_mixed, regex_effbot, deepcopy_reduce, async_tree_none_tg, pidigits, asyncio_websockets, many_optionals, async_generators, subparsers, deepcopy, create_gc_cycles, scimark_lu, generators, typing_runtime_protocols

- Geometric mean (including insignificant results): 1.000x faster

# HPT report

- Reliability score: 88.01% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x