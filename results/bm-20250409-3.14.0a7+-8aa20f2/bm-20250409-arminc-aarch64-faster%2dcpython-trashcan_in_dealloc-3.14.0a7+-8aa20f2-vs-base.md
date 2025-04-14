# Results vs. base

- fork: faster-cpython
- ref: trashcan_in_dealloc
- machine: linux-aarch64
- commit hash: 8aa20f2
- commit date: 2025-04-09
- overall geometric mean: 1.006x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250408-arminc-aarch64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                                   | 297 ms: 1.02x slower                                                              |
| sphinx         | 1.14 sec                                                                 | 1.16 sec: 1.02x slower                                                            |
| Geometric mean | (ref)                                                                    | 1.01x slower                                                                      |

Benchmark hidden because not significant (2): docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20250408-arminc-aarch64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_generators | 450 ms                                                                   | 462 ms: 1.03x slower                                                              |
| Geometric mean   | (ref)                                                                    | 1.01x slower                                                                      |

Benchmark hidden because not significant (10): async_tree_io, coroutines, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none, asyncio_websockets, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250408-arminc-aarch64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 83.8 ms                                                                  | 86.0 ms: 1.03x slower                                                             |
| Geometric mean | (ref)                                                                    | 1.01x slower                                                                      |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250408-arminc-aarch64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_dna      | 251 ms                                                                   | 242 ms: 1.03x faster                                                              |
| Geometric mean | (ref)                                                                    | 1.00x faster                                                                      |

Benchmark hidden because not significant (3): regex_v8, regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250408-arminc-aarch64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|--------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_parse    | 173 ms                                                                   | 175 ms: 1.01x slower                                                              |
| xml_etree_generate | 110 ms                                                                   | 112 ms: 1.01x slower                                                              |
| json_dumps         | 13.9 ms                                                                  | 14.1 ms: 1.02x slower                                                             |
| tomli_loads        | 2.43 sec                                                                 | 2.48 sec: 1.02x slower                                                            |
| json_loads         | 33.9 us                                                                  | 34.8 us: 1.03x slower                                                             |
| Geometric mean     | (ref)                                                                    | 1.01x slower                                                                      |

Benchmark hidden because not significant (4): unpickle_pure_python, pickle_pure_python, xml_etree_process, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250408-arminc-aarch64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml     | 59.6 ms                                                                  | 61.6 ms: 1.03x slower                                                             |
| genshi_text    | 26.2 ms                                                                  | 28.3 ms: 1.08x slower                                                             |
| Geometric mean | (ref)                                                                    | 1.03x slower                                                                      |

Benchmark hidden because not significant (2): mako, django_template

All benchmarks:
===============

| Benchmark               | bm-20250408-arminc-aarch64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|-------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| scimark_lu              | 152 ms                                                                   | 143 ms: 1.06x faster                                                              |
| regex_dna               | 251 ms                                                                   | 242 ms: 1.03x faster                                                              |
| gc_traversal            | 6.73 ms                                                                  | 6.56 ms: 1.03x faster                                                             |
| shortest_path           | 587 ms                                                                   | 579 ms: 1.01x faster                                                              |
| deltablue               | 3.79 ms                                                                  | 3.82 ms: 1.01x slower                                                             |
| xml_etree_parse         | 173 ms                                                                   | 175 ms: 1.01x slower                                                              |
| xml_etree_generate      | 110 ms                                                                   | 112 ms: 1.01x slower                                                              |
| logging_simple          | 7.07 us                                                                  | 7.17 us: 1.01x slower                                                             |
| hexiom                  | 6.99 ms                                                                  | 7.09 ms: 1.01x slower                                                             |
| bpe_tokeniser           | 5.53 sec                                                                 | 5.62 sec: 1.02x slower                                                            |
| json_dumps              | 13.9 ms                                                                  | 14.1 ms: 1.02x slower                                                             |
| mdp                     | 1.61 sec                                                                 | 1.64 sec: 1.02x slower                                                            |
| sphinx                  | 1.14 sec                                                                 | 1.16 sec: 1.02x slower                                                            |
| go                      | 129 ms                                                                   | 131 ms: 1.02x slower                                                              |
| 2to3                    | 291 ms                                                                   | 297 ms: 1.02x slower                                                              |
| tomli_loads             | 2.43 sec                                                                 | 2.48 sec: 1.02x slower                                                            |
| connected_components    | 549 ms                                                                   | 560 ms: 1.02x slower                                                              |
| create_gc_cycles        | 3.49 ms                                                                  | 3.56 ms: 1.02x slower                                                             |
| pprint_safe_repr        | 910 ms                                                                   | 931 ms: 1.02x slower                                                              |
| scimark_sparse_mat_mult | 6.65 ms                                                                  | 6.82 ms: 1.03x slower                                                             |
| async_generators        | 450 ms                                                                   | 462 ms: 1.03x slower                                                              |
| json_loads              | 33.9 us                                                                  | 34.8 us: 1.03x slower                                                             |
| float                   | 83.8 ms                                                                  | 86.0 ms: 1.03x slower                                                             |
| json                    | 5.87 ms                                                                  | 6.03 ms: 1.03x slower                                                             |
| pathlib                 | 21.6 ms                                                                  | 22.3 ms: 1.03x slower                                                             |
| genshi_xml              | 59.6 ms                                                                  | 61.6 ms: 1.03x slower                                                             |
| deepcopy_reduce         | 3.38 us                                                                  | 3.50 us: 1.03x slower                                                             |
| pprint_pformat          | 1.85 sec                                                                 | 1.91 sec: 1.03x slower                                                            |
| raytrace                | 315 ms                                                                   | 327 ms: 1.04x slower                                                              |
| fannkuch                | 475 ms                                                                   | 494 ms: 1.04x slower                                                              |
| telco                   | 9.08 ms                                                                  | 9.55 ms: 1.05x slower                                                             |
| crypto_pyaes            | 83.3 ms                                                                  | 87.8 ms: 1.05x slower                                                             |
| scimark_fft             | 412 ms                                                                   | 437 ms: 1.06x slower                                                              |
| genshi_text             | 26.2 ms                                                                  | 28.3 ms: 1.08x slower                                                             |
| bench_mp_pool           | 2.07 sec                                                                 | 4.04 sec: 1.95x slower                                                            |
| Geometric mean          | (ref)                                                                    | 1.02x slower                                                                      |

Benchmark hidden because not significant (60): sqlglot_v2_parse, sqlglot_v2_normalize, pidigits, sqlglot_v2_optimize, scimark_sor, sqlglot_v2_transpile, pycparser, sqlite_synth, richards_super, regex_v8, subparsers, sympy_sum, unpickle_pure_python, sympy_expand, async_tree_io, sympy_integrate, coroutines, pyflate, python_startup_no_site, meteor_contest, async_tree_memoization_tg, async_tree_cpu_io_mixed, pickle_pure_python, html5lib, async_tree_memoization, richards, docutils, xml_etree_process, mako, async_tree_none, xml_etree_iterparse, asyncio_websockets, logging_format, async_tree_io_tg, dulwich_log, python_startup, pylint, regex_effbot, async_tree_cpu_io_mixed_tg, comprehensions, sqlalchemy_declarative, nbody, bench_thread_pool, sympy_str, deepcopy_memo, k_core, many_optionals, sqlalchemy_imperative, chaos, async_tree_none_tg, django_template, regex_compile, nqueens, logging_silent, coverage, generators, spectral_norm, deepcopy, typing_runtime_protocols, scimark_monte_carlo

- Geometric mean (including insignificant results): 1.006x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.99x