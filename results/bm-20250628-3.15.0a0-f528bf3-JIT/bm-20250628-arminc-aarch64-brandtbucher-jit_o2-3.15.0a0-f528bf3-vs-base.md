# Results vs. base

- fork: brandtbucher
- ref: jit_o2
- machine: linux-aarch64
- commit hash: f528bf3
- commit date: 2025-06-28
- overall geometric mean: 1.002x faster
- HPT reliability: 70.34%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-arminc-aarch64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 310 ms                                                                  | 312 ms: 1.01x slower                                            |
| Geometric mean | (ref)                                                                   | 1.00x faster                                                    |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-arminc-aarch64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|------------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_none        | 407 ms                                                                  | 397 ms: 1.02x faster                                            |
| async_tree_memoization | 478 ms                                                                  | 470 ms: 1.02x faster                                            |
| async_tree_io_tg       | 937 ms                                                                  | 924 ms: 1.01x faster                                            |
| Geometric mean         | (ref)                                                                   | 1.00x faster                                                    |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, async_tree_io, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_memoization_tg, async_generators, async_tree_none_tg, coroutines

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-arminc-aarch64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_dna      | 219 ms                                                                  | 226 ms: 1.03x slower                                            |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                    |

Benchmark hidden because not significant (3): regex_v8, regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-arminc-aarch64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|--------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| pickle_pure_python | 403 us                                                                  | 390 us: 1.03x faster                                            |
| xml_etree_process  | 77.7 ms                                                                 | 77.2 ms: 1.01x faster                                           |
| Geometric mean     | (ref)                                                                   | 1.00x faster                                                    |

Benchmark hidden because not significant (7): xml_etree_generate, xml_etree_parse, xml_etree_iterparse, json_dumps, tomli_loads, json_loads, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-arminc-aarch64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| genshi_text    | 26.8 ms                                                                 | 27.7 ms: 1.04x slower                                           |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                    |

Benchmark hidden because not significant (3): mako, genshi_xml, django_template

All benchmarks:
===============

| Benchmark              | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-arminc-aarch64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|------------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| create_gc_cycles       | 3.89 ms                                                                 | 3.65 ms: 1.07x faster                                           |
| shortest_path          | 611 ms                                                                  | 585 ms: 1.05x faster                                            |
| subparsers             | 29.5 ms                                                                 | 28.5 ms: 1.04x faster                                           |
| pickle_pure_python     | 403 us                                                                  | 390 us: 1.03x faster                                            |
| pprint_pformat         | 2.38 sec                                                                | 2.30 sec: 1.03x faster                                          |
| async_tree_none        | 407 ms                                                                  | 397 ms: 1.02x faster                                            |
| pprint_safe_repr       | 1.16 sec                                                                | 1.13 sec: 1.02x faster                                          |
| mdp                    | 1.69 sec                                                                | 1.65 sec: 1.02x faster                                          |
| json                   | 5.75 ms                                                                 | 5.63 ms: 1.02x faster                                           |
| async_tree_memoization | 478 ms                                                                  | 470 ms: 1.02x faster                                            |
| gc_traversal           | 6.90 ms                                                                 | 6.80 ms: 1.01x faster                                           |
| async_tree_io_tg       | 937 ms                                                                  | 924 ms: 1.01x faster                                            |
| connected_components   | 572 ms                                                                  | 566 ms: 1.01x faster                                            |
| xml_etree_process      | 77.7 ms                                                                 | 77.2 ms: 1.01x faster                                           |
| bpe_tokeniser          | 5.42 sec                                                                | 5.39 sec: 1.01x faster                                          |
| 2to3                   | 310 ms                                                                  | 312 ms: 1.01x slower                                            |
| sqlglot_v2_transpile   | 1.84 ms                                                                 | 1.87 ms: 1.01x slower                                           |
| sqlglot_v2_parse       | 1.50 ms                                                                 | 1.52 ms: 1.01x slower                                           |
| logging_format         | 7.73 us                                                                 | 7.86 us: 1.02x slower                                           |
| sqlite_synth           | 3.75 us                                                                 | 3.83 us: 1.02x slower                                           |
| regex_dna              | 219 ms                                                                  | 226 ms: 1.03x slower                                            |
| genshi_text            | 26.8 ms                                                                 | 27.7 ms: 1.04x slower                                           |
| sqlglot_v2_optimize    | 62.8 ms                                                                 | 65.0 ms: 1.04x slower                                           |
| dulwich_log            | 54.5 ms                                                                 | 56.7 ms: 1.04x slower                                           |
| sqlglot_v2_normalize   | 127 ms                                                                  | 133 ms: 1.04x slower                                            |
| generators             | 35.1 ms                                                                 | 37.1 ms: 1.06x slower                                           |
| Geometric mean         | (ref)                                                                   | 1.00x slower                                                    |

Benchmark hidden because not significant (67): meteor_contest, regex_v8, sympy_sum, comprehensions, html5lib, logging_silent, thrift, scimark_monte_carlo, deltablue, xml_etree_generate, many_optionals, typing_runtime_protocols, go, async_tree_cpu_io_mixed, async_tree_io, raytrace, logging_simple, python_startup_no_site, async_tree_cpu_io_mixed_tg, mako, deepcopy_memo, sympy_integrate, telco, float, xml_etree_parse, asyncio_websockets, python_startup, djangocms, docutils, xml_etree_iterparse, sympy_str, async_tree_memoization_tg, async_generators, json_dumps, async_tree_none_tg, nbody, scimark_fft, nqueens, k_core, tomli_loads, coverage, pyflate, genshi_xml, sphinx, pidigits, richards_super, django_template, json_loads, fannkuch, sympy_expand, hexiom, pycparser, pylint, scimark_sor, scimark_sparse_mat_mult, unpickle_pure_python, pathlib, regex_compile, chaos, coroutines, deepcopy, crypto_pyaes, deepcopy_reduce, regex_effbot, spectral_norm, richards, scimark_lu

- Geometric mean (including insignificant results): 1.002x faster

# HPT report

- Reliability score: 70.34% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x