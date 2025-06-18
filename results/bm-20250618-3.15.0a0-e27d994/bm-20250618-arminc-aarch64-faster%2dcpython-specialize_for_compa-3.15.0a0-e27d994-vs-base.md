# Results vs. base

- fork: faster-cpython
- ref: specialize_for_compa
- machine: linux-aarch64
- commit hash: e27d994
- commit date: 2025-06-18
- overall geometric mean: 1.002x slower
- HPT reliability: 86.87%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250617-arminc-aarch64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250618-arminc-aarch64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 297 ms                                                                  | 301 ms: 1.01x slower                                                              |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                                      |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20250617-arminc-aarch64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250618-arminc-aarch64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|---------------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 482 ms                                                                  | 466 ms: 1.03x faster                                                              |
| async_tree_none_tg        | 388 ms                                                                  | 379 ms: 1.02x faster                                                              |
| async_tree_io             | 910 ms                                                                  | 893 ms: 1.02x faster                                                              |
| Geometric mean            | (ref)                                                                   | 1.01x faster                                                                      |

Benchmark hidden because not significant (8): async_tree_io_tg, coroutines, async_tree_none, asyncio_websockets, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_generators, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, nbody, pidigits

Benchmarks with tag 'regex':
============================

Benchmark hidden because not significant (4): regex_v8, regex_dna, regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250617-arminc-aarch64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250618-arminc-aarch64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|---------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_parse     | 179 ms                                                                  | 181 ms: 1.01x slower                                                              |
| xml_etree_iterparse | 141 ms                                                                  | 142 ms: 1.01x slower                                                              |
| Geometric mean      | (ref)                                                                   | 1.00x slower                                                                      |

Benchmark hidden because not significant (7): json_dumps, json_loads, xml_etree_generate, tomli_loads, xml_etree_process, pickle_pure_python, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250617-arminc-aarch64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250618-arminc-aarch64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|------------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 8.60 ms                                                                 | 8.63 ms: 1.00x slower                                                             |
| python_startup         | 15.0 ms                                                                 | 15.1 ms: 1.01x slower                                                             |
| Geometric mean         | (ref)                                                                   | 1.01x slower                                                                      |

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_xml, mako, genshi_text, django_template

All benchmarks:
===============

| Benchmark                 | bm-20250617-arminc-aarch64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250618-arminc-aarch64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|---------------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 482 ms                                                                  | 466 ms: 1.03x faster                                                              |
| fannkuch                  | 481 ms                                                                  | 468 ms: 1.03x faster                                                              |
| async_tree_none_tg        | 388 ms                                                                  | 379 ms: 1.02x faster                                                              |
| async_tree_io             | 910 ms                                                                  | 893 ms: 1.02x faster                                                              |
| pyflate                   | 525 ms                                                                  | 518 ms: 1.01x faster                                                              |
| generators                | 35.8 ms                                                                 | 35.4 ms: 1.01x faster                                                             |
| python_startup_no_site    | 8.60 ms                                                                 | 8.63 ms: 1.00x slower                                                             |
| xml_etree_parse           | 179 ms                                                                  | 181 ms: 1.01x slower                                                              |
| python_startup            | 15.0 ms                                                                 | 15.1 ms: 1.01x slower                                                             |
| xml_etree_iterparse       | 141 ms                                                                  | 142 ms: 1.01x slower                                                              |
| 2to3                      | 297 ms                                                                  | 301 ms: 1.01x slower                                                              |
| pprint_safe_repr          | 1.00 sec                                                                | 1.01 sec: 1.01x slower                                                            |
| pprint_pformat            | 2.05 sec                                                                | 2.08 sec: 1.02x slower                                                            |
| dulwich_log               | 50.8 ms                                                                 | 52.3 ms: 1.03x slower                                                             |
| shortest_path             | 587 ms                                                                  | 605 ms: 1.03x slower                                                              |
| djangocms                 | 65.0 us                                                                 | 67.1 us: 1.03x slower                                                             |
| scimark_monte_carlo       | 79.8 ms                                                                 | 82.4 ms: 1.03x slower                                                             |
| gc_traversal              | 6.71 ms                                                                 | 6.97 ms: 1.04x slower                                                             |
| many_optionals            | 740 us                                                                  | 770 us: 1.04x slower                                                              |
| telco                     | 9.29 ms                                                                 | 9.70 ms: 1.04x slower                                                             |
| sqlglot_v2_normalize      | 123 ms                                                                  | 129 ms: 1.05x slower                                                              |
| Geometric mean            | (ref)                                                                   | 1.00x slower                                                                      |

Benchmark hidden because not significant (72): thrift, sqlglot_v2_transpile, json_dumps, scimark_lu, meteor_contest, spectral_norm, deepcopy_memo, scimark_fft, richards_super, crypto_pyaes, logging_format, logging_simple, chaos, sympy_sum, regex_v8, genshi_xml, async_tree_io_tg, deltablue, nqueens, comprehensions, coverage, coroutines, pylint, regex_dna, async_tree_none, asyncio_websockets, sympy_expand, json_loads, scimark_sor, scimark_sparse_mat_mult, connected_components, typing_runtime_protocols, xml_etree_generate, regex_effbot, mako, pycparser, float, tomli_loads, bpe_tokeniser, subparsers, nbody, async_tree_memoization, genshi_text, sympy_str, async_tree_cpu_io_mixed_tg, json, html5lib, django_template, docutils, raytrace, async_generators, k_core, pidigits, create_gc_cycles, deepcopy, sphinx, xml_etree_process, pathlib, pickle_pure_python, mdp, async_tree_cpu_io_mixed, unpickle_pure_python, go, logging_silent, sqlglot_v2_parse, hexiom, sqlite_synth, regex_compile, sqlglot_v2_optimize, sympy_integrate, richards, deepcopy_reduce

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 86.87% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x