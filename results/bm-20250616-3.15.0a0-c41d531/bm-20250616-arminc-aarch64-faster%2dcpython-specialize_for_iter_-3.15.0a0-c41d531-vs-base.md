# Results vs. base

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: linux-aarch64
- commit hash: c41d531
- commit date: 2025-06-16
- overall geometric mean: 1.001x slower
- HPT reliability: 92.54%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20250613-arminc-aarch64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250616-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|--------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_none_tg | 380 ms                                                                  | 365 ms: 1.04x faster                                                              |
| Geometric mean     | (ref)                                                                   | 1.01x faster                                                                      |

Benchmark hidden because not significant (10): coroutines, async_generators, async_tree_none, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_cpu_io_mixed_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, pidigits, nbody

Benchmarks with tag 'regex':
============================

Benchmark hidden because not significant (4): regex_dna, regex_compile, regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250613-arminc-aarch64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250616-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|--------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| tomli_loads        | 2.48 sec                                                                | 2.44 sec: 1.02x faster                                                            |
| xml_etree_parse    | 181 ms                                                                  | 183 ms: 1.01x slower                                                              |
| pickle_pure_python | 380 us                                                                  | 387 us: 1.02x slower                                                              |
| Geometric mean     | (ref)                                                                   | 1.00x faster                                                                      |

Benchmark hidden because not significant (6): json_dumps, xml_etree_process, json_loads, unpickle_pure_python, xml_etree_iterparse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250613-arminc-aarch64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250616-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|------------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 8.51 ms                                                                 | 8.61 ms: 1.01x slower                                                             |
| python_startup         | 14.9 ms                                                                 | 15.1 ms: 1.01x slower                                                             |
| Geometric mean         | (ref)                                                                   | 1.01x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250613-arminc-aarch64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250616-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako           | 13.9 ms                                                                 | 14.2 ms: 1.02x slower                                                             |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                                      |

Benchmark hidden because not significant (3): genshi_xml, django_template, genshi_text

All benchmarks:
===============

| Benchmark               | bm-20250613-arminc-aarch64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250616-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|-------------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| scimark_sparse_mat_mult | 7.03 ms                                                                 | 6.69 ms: 1.05x faster                                                             |
| meteor_contest          | 113 ms                                                                  | 108 ms: 1.05x faster                                                              |
| async_tree_none_tg      | 380 ms                                                                  | 365 ms: 1.04x faster                                                              |
| deepcopy_memo           | 37.1 us                                                                 | 36.2 us: 1.02x faster                                                             |
| mdp                     | 1.68 sec                                                                | 1.64 sec: 1.02x faster                                                            |
| tomli_loads             | 2.48 sec                                                                | 2.44 sec: 1.02x faster                                                            |
| sqlite_synth            | 3.86 us                                                                 | 3.80 us: 1.01x faster                                                             |
| bpe_tokeniser           | 5.49 sec                                                                | 5.44 sec: 1.01x faster                                                            |
| hexiom                  | 6.78 ms                                                                 | 6.72 ms: 1.01x faster                                                             |
| sympy_sum               | 142 ms                                                                  | 141 ms: 1.01x faster                                                              |
| logging_simple          | 7.54 us                                                                 | 7.62 us: 1.01x slower                                                             |
| python_startup_no_site  | 8.51 ms                                                                 | 8.61 ms: 1.01x slower                                                             |
| subparsers              | 27.7 ms                                                                 | 28.0 ms: 1.01x slower                                                             |
| xml_etree_parse         | 181 ms                                                                  | 183 ms: 1.01x slower                                                              |
| python_startup          | 14.9 ms                                                                 | 15.1 ms: 1.01x slower                                                             |
| sympy_str               | 260 ms                                                                  | 264 ms: 1.01x slower                                                              |
| pickle_pure_python      | 380 us                                                                  | 387 us: 1.02x slower                                                              |
| mako                    | 13.9 ms                                                                 | 14.2 ms: 1.02x slower                                                             |
| connected_components    | 554 ms                                                                  | 564 ms: 1.02x slower                                                              |
| k_core                  | 2.78 sec                                                                | 2.84 sec: 1.02x slower                                                            |
| gc_traversal            | 6.76 ms                                                                 | 6.96 ms: 1.03x slower                                                             |
| create_gc_cycles        | 3.71 ms                                                                 | 3.83 ms: 1.03x slower                                                             |
| dulwich_log             | 51.0 ms                                                                 | 54.0 ms: 1.06x slower                                                             |
| Geometric mean          | (ref)                                                                   | 1.00x slower                                                                      |

Benchmark hidden because not significant (69): crypto_pyaes, json_dumps, deepcopy_reduce, scimark_lu, typing_runtime_protocols, coroutines, deepcopy, async_generators, richards, many_optionals, thrift, chaos, logging_silent, async_tree_none, spectral_norm, async_tree_cpu_io_mixed, async_tree_memoization_tg, json, sympy_integrate, richards_super, coverage, xml_etree_process, async_tree_io, shortest_path, async_tree_io_tg, pyflate, pprint_safe_repr, go, telco, genshi_xml, async_tree_memoization, async_tree_cpu_io_mixed_tg, sqlglot_v2_transpile, json_loads, scimark_sor, logging_format, float, regex_dna, html5lib, pprint_pformat, pidigits, fannkuch, nqueens, deltablue, sympy_expand, sqlglot_v2_normalize, unpickle_pure_python, xml_etree_iterparse, docutils, sqlglot_v2_parse, generators, asyncio_websockets, pycparser, django_template, scimark_fft, raytrace, xml_etree_generate, sphinx, 2to3, regex_compile, pathlib, sqlglot_v2_optimize, pylint, genshi_text, regex_effbot, regex_v8, nbody, scimark_monte_carlo, comprehensions

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 92.54% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x