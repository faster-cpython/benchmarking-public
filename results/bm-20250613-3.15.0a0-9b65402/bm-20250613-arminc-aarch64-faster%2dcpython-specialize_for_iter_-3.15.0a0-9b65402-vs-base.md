# Results vs. base

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: linux-aarch64
- commit hash: 9b65402
- commit date: 2025-06-13
- overall geometric mean: 1.001x faster
- HPT reliability: 72.89%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark      | bm-20250613-arminc-aarch64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250613-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_io  | 898 ms                                                                  | 888 ms: 1.01x faster                                                              |
| Geometric mean | (ref)                                                                   | 1.00x faster                                                                      |

Benchmark hidden because not significant (10): async_tree_none_tg, async_tree_io_tg, async_tree_none, async_tree_memoization, async_tree_memoization_tg, async_tree_cpu_io_mixed, asyncio_websockets, async_generators, coroutines, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250613-arminc-aarch64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250613-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 89.8 ms                                                                 | 85.5 ms: 1.05x faster                                                             |
| Geometric mean | (ref)                                                                   | 1.02x faster                                                                      |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

Benchmark hidden because not significant (4): regex_dna, regex_v8, regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark         | bm-20250613-arminc-aarch64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250613-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|-------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_process | 79.1 ms                                                                 | 79.8 ms: 1.01x slower                                                             |
| tomli_loads       | 2.44 sec                                                                | 2.47 sec: 1.01x slower                                                            |
| Geometric mean    | (ref)                                                                   | 1.01x slower                                                                      |

Benchmark hidden because not significant (7): unpickle_pure_python, json_loads, xml_etree_iterparse, xml_etree_parse, xml_etree_generate, pickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250613-arminc-aarch64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250613-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_text    | 26.3 ms                                                                 | 26.6 ms: 1.01x slower                                                             |
| mako           | 13.7 ms                                                                 | 14.0 ms: 1.02x slower                                                             |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                                      |

Benchmark hidden because not significant (2): genshi_xml, django_template

All benchmarks:
===============

| Benchmark         | bm-20250613-arminc-aarch64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250613-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|-------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| chaos             | 69.8 ms                                                                 | 65.8 ms: 1.06x faster                                                             |
| float             | 89.8 ms                                                                 | 85.5 ms: 1.05x faster                                                             |
| sympy_integrate   | 20.4 ms                                                                 | 19.8 ms: 1.03x faster                                                             |
| pyflate           | 527 ms                                                                  | 516 ms: 1.02x faster                                                              |
| coverage          | 566 ms                                                                  | 556 ms: 1.02x faster                                                              |
| richards          | 52.3 ms                                                                 | 51.4 ms: 1.02x faster                                                             |
| logging_format    | 8.25 us                                                                 | 8.10 us: 1.02x faster                                                             |
| gc_traversal      | 6.84 ms                                                                 | 6.73 ms: 1.02x faster                                                             |
| bpe_tokeniser     | 5.52 sec                                                                | 5.44 sec: 1.01x faster                                                            |
| async_tree_io     | 898 ms                                                                  | 888 ms: 1.01x faster                                                              |
| logging_silent    | 615 ns                                                                  | 620 ns: 1.01x slower                                                              |
| xml_etree_process | 79.1 ms                                                                 | 79.8 ms: 1.01x slower                                                             |
| tomli_loads       | 2.44 sec                                                                | 2.47 sec: 1.01x slower                                                            |
| genshi_text       | 26.3 ms                                                                 | 26.6 ms: 1.01x slower                                                             |
| deepcopy_reduce   | 3.61 us                                                                 | 3.65 us: 1.01x slower                                                             |
| pycparser         | 1.24 sec                                                                | 1.26 sec: 1.02x slower                                                            |
| k_core            | 2.79 sec                                                                | 2.84 sec: 1.02x slower                                                            |
| mdp               | 1.65 sec                                                                | 1.68 sec: 1.02x slower                                                            |
| shortest_path     | 580 ms                                                                  | 592 ms: 1.02x slower                                                              |
| mako              | 13.7 ms                                                                 | 14.0 ms: 1.02x slower                                                             |
| Geometric mean    | (ref)                                                                   | 1.00x slower                                                                      |

Benchmark hidden because not significant (72): telco, hexiom, sqlglot_v2_transpile, create_gc_cycles, sympy_expand, pidigits, nqueens, async_tree_none_tg, scimark_sparse_mat_mult, deltablue, pathlib, unpickle_pure_python, async_tree_io_tg, comprehensions, crypto_pyaes, sqlglot_v2_parse, async_tree_none, scimark_monte_carlo, async_tree_memoization, json, typing_runtime_protocols, async_tree_memoization_tg, regex_dna, json_loads, python_startup, async_tree_cpu_io_mixed, asyncio_websockets, pylint, raytrace, genshi_xml, sqlglot_v2_optimize, scimark_fft, sympy_sum, django_template, regex_v8, sphinx, scimark_sor, regex_compile, sqlite_synth, python_startup_no_site, 2to3, html5lib, async_generators, coroutines, docutils, xml_etree_iterparse, async_tree_cpu_io_mixed_tg, xml_etree_parse, pprint_safe_repr, pprint_pformat, nbody, connected_components, meteor_contest, generators, fannkuch, richards_super, scimark_lu, regex_effbot, dulwich_log, go, deepcopy, thrift, spectral_norm, many_optionals, deepcopy_memo, logging_simple, sympy_str, subparsers, xml_etree_generate, sqlglot_v2_normalize, pickle_pure_python, json_dumps

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 72.89% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x