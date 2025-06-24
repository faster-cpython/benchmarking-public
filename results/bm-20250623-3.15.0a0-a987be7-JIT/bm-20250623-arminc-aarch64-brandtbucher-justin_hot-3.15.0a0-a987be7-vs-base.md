# Results vs. base

- fork: brandtbucher
- ref: justin_hot
- machine: linux-aarch64
- commit hash: a987be7
- commit date: 2025-06-23
- overall geometric mean: 1.000x faster
- HPT reliability: 65.97%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250623-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| docutils       | 3.13 sec                                                                | 3.09 sec: 1.01x faster                                              |
| Geometric mean | (ref)                                                                   | 1.01x faster                                                        |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250623-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|------------------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization | 474 ms                                                                  | 465 ms: 1.02x faster                                                |
| async_tree_io          | 904 ms                                                                  | 891 ms: 1.01x faster                                                |
| async_tree_io_tg       | 916 ms                                                                  | 906 ms: 1.01x faster                                                |
| Geometric mean         | (ref)                                                                   | 1.01x faster                                                        |

Benchmark hidden because not significant (8): coroutines, async_tree_none, async_tree_cpu_io_mixed, async_tree_none_tg, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_generators, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250623-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 27.2 ms                                                                 | 26.7 ms: 1.02x faster                                               |
| regex_dna      | 220 ms                                                                  | 218 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                                   | 1.00x slower                                                        |

Benchmark hidden because not significant (2): regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark      | bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250623-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps     | 13.5 ms                                                                 | 13.3 ms: 1.02x faster                                               |
| json_loads     | 32.3 us                                                                 | 32.7 us: 1.01x slower                                               |
| Geometric mean | (ref)                                                                   | 1.00x faster                                                        |

Benchmark hidden because not significant (7): pickle_pure_python, xml_etree_parse, xml_etree_process, xml_etree_iterparse, tomli_loads, unpickle_pure_python, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250623-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|------------------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 8.57 ms                                                                 | 8.63 ms: 1.01x slower                                               |
| python_startup         | 15.0 ms                                                                 | 15.2 ms: 1.01x slower                                               |
| Geometric mean         | (ref)                                                                   | 1.01x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250623-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako           | 13.1 ms                                                                 | 13.2 ms: 1.00x slower                                               |
| Geometric mean | (ref)                                                                   | 1.01x faster                                                        |

Benchmark hidden because not significant (3): genshi_xml, django_template, genshi_text

All benchmarks:
===============

| Benchmark              | bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250623-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|------------------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pyflate                | 549 ms                                                                  | 532 ms: 1.03x faster                                                |
| async_tree_memoization | 474 ms                                                                  | 465 ms: 1.02x faster                                                |
| json_dumps             | 13.5 ms                                                                 | 13.3 ms: 1.02x faster                                               |
| regex_v8               | 27.2 ms                                                                 | 26.7 ms: 1.02x faster                                               |
| connected_components   | 575 ms                                                                  | 566 ms: 1.02x faster                                                |
| logging_format         | 8.29 us                                                                 | 8.16 us: 1.02x faster                                               |
| coverage               | 102 ms                                                                  | 101 ms: 1.02x faster                                                |
| async_tree_io          | 904 ms                                                                  | 891 ms: 1.01x faster                                                |
| async_tree_io_tg       | 916 ms                                                                  | 906 ms: 1.01x faster                                                |
| docutils               | 3.13 sec                                                                | 3.09 sec: 1.01x faster                                              |
| logging_simple         | 7.54 us                                                                 | 7.46 us: 1.01x faster                                               |
| regex_dna              | 220 ms                                                                  | 218 ms: 1.01x faster                                                |
| sqlglot_v2_normalize   | 127 ms                                                                  | 126 ms: 1.01x faster                                                |
| mako                   | 13.1 ms                                                                 | 13.2 ms: 1.00x slower                                               |
| python_startup_no_site | 8.57 ms                                                                 | 8.63 ms: 1.01x slower                                               |
| deltablue              | 3.88 ms                                                                 | 3.91 ms: 1.01x slower                                               |
| python_startup         | 15.0 ms                                                                 | 15.2 ms: 1.01x slower                                               |
| json_loads             | 32.3 us                                                                 | 32.7 us: 1.01x slower                                               |
| thrift                 | 926 us                                                                  | 938 us: 1.01x slower                                                |
| meteor_contest         | 114 ms                                                                  | 116 ms: 1.02x slower                                                |
| gc_traversal           | 6.80 ms                                                                 | 6.95 ms: 1.02x slower                                               |
| k_core                 | 2.80 sec                                                                | 2.86 sec: 1.02x slower                                              |
| sympy_integrate        | 20.5 ms                                                                 | 21.1 ms: 1.03x slower                                               |
| create_gc_cycles       | 3.72 ms                                                                 | 3.87 ms: 1.04x slower                                               |
| crypto_pyaes           | 89.3 ms                                                                 | 93.9 ms: 1.05x slower                                               |
| Geometric mean         | (ref)                                                                   | 1.00x faster                                                        |

Benchmark hidden because not significant (68): nqueens, genshi_xml, comprehensions, pickle_pure_python, scimark_monte_carlo, html5lib, coroutines, django_template, subparsers, nbody, richards, go, richards_super, telco, pathlib, sqlglot_v2_optimize, xml_etree_parse, deepcopy_reduce, async_tree_none, mdp, pprint_safe_repr, logging_silent, async_tree_cpu_io_mixed, pidigits, scimark_sparse_mat_mult, async_tree_none_tg, sphinx, xml_etree_process, sqlglot_v2_transpile, chaos, sqlglot_v2_parse, asyncio_websockets, spectral_norm, raytrace, sympy_expand, hexiom, fannkuch, float, xml_etree_iterparse, bpe_tokeniser, deepcopy_memo, scimark_lu, pycparser, djangocms, async_tree_cpu_io_mixed_tg, async_generators, regex_compile, async_tree_memoization_tg, pprint_pformat, 2to3, tomli_loads, pylint, genshi_text, sqlite_synth, shortest_path, scimark_sor, unpickle_pure_python, many_optionals, json, sympy_str, scimark_fft, xml_etree_generate, dulwich_log, typing_runtime_protocols, deepcopy, generators, regex_effbot, sympy_sum

- Geometric mean (including insignificant results): 1.000x faster

# HPT report

- Reliability score: 65.97% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x