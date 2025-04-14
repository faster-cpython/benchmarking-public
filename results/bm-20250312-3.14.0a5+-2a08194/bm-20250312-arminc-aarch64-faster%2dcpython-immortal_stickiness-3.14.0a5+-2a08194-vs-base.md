# Results vs. base

- fork: faster-cpython
- ref: immortal_stickiness
- machine: linux-aarch64
- commit hash: 2a08194
- commit date: 2025-03-12
- overall geometric mean: 1.000x faster
- HPT reliability: 62.23%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250312-arminc-aarch64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 295 ms                                                                   | 297 ms: 1.01x slower                                                              |
| Geometric mean | (ref)                                                                    | 1.00x slower                                                                      |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20250312-arminc-aarch64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization | 471 ms                                                                   | 474 ms: 1.01x slower                                                              |
| async_tree_io          | 873 ms                                                                   | 881 ms: 1.01x slower                                                              |
| async_generators       | 436 ms                                                                   | 444 ms: 1.02x slower                                                              |
| async_tree_none        | 378 ms                                                                   | 386 ms: 1.02x slower                                                              |
| async_tree_none_tg     | 374 ms                                                                   | 384 ms: 1.03x slower                                                              |
| Geometric mean         | (ref)                                                                    | 1.01x slower                                                                      |

Benchmark hidden because not significant (6): coroutines, asyncio_websockets, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): pidigits, float, nbody

Benchmarks with tag 'regex':
============================

Benchmark hidden because not significant (4): regex_compile, regex_v8, regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250312-arminc-aarch64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|--------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_loads         | 34.8 us                                                                  | 33.9 us: 1.03x faster                                                             |
| xml_etree_generate | 113 ms                                                                   | 111 ms: 1.02x faster                                                              |
| tomli_loads        | 2.46 sec                                                                 | 2.42 sec: 1.01x faster                                                            |
| xml_etree_process  | 80.1 ms                                                                  | 79.2 ms: 1.01x faster                                                             |
| Geometric mean     | (ref)                                                                    | 1.01x faster                                                                      |

Benchmark hidden because not significant (5): xml_etree_iterparse, json_dumps, xml_etree_parse, unpickle_pure_python, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250312-arminc-aarch64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 10.2 ms                                                                  | 10.3 ms: 1.01x slower                                                             |
| python_startup         | 16.1 ms                                                                  | 16.2 ms: 1.01x slower                                                             |
| Geometric mean         | (ref)                                                                    | 1.01x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250312-arminc-aarch64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako           | 14.1 ms                                                                  | 14.0 ms: 1.01x faster                                                             |
| genshi_xml     | 59.8 ms                                                                  | 60.4 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                                    | 1.01x slower                                                                      |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark               | bm-20250312-arminc-aarch64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|-------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nqueens                 | 106 ms                                                                   | 101 ms: 1.06x faster                                                              |
| richards                | 54.2 ms                                                                  | 51.8 ms: 1.05x faster                                                             |
| thrift                  | 976 us                                                                   | 943 us: 1.04x faster                                                              |
| json_loads              | 34.8 us                                                                  | 33.9 us: 1.03x faster                                                             |
| fannkuch                | 504 ms                                                                   | 493 ms: 1.02x faster                                                              |
| xml_etree_generate      | 113 ms                                                                   | 111 ms: 1.02x faster                                                              |
| subparsers              | 25.9 ms                                                                  | 25.5 ms: 1.02x faster                                                             |
| tomli_loads             | 2.46 sec                                                                 | 2.42 sec: 1.01x faster                                                            |
| xml_etree_process       | 80.1 ms                                                                  | 79.2 ms: 1.01x faster                                                             |
| mako                    | 14.1 ms                                                                  | 14.0 ms: 1.01x faster                                                             |
| deepcopy_reduce         | 3.41 us                                                                  | 3.39 us: 1.01x faster                                                             |
| sqlite_synth            | 3.78 us                                                                  | 3.76 us: 1.01x faster                                                             |
| generators              | 35.7 ms                                                                  | 35.6 ms: 1.00x faster                                                             |
| logging_simple          | 6.98 us                                                                  | 6.96 us: 1.00x faster                                                             |
| meteor_contest          | 113 ms                                                                   | 113 ms: 1.00x slower                                                              |
| async_tree_memoization  | 471 ms                                                                   | 474 ms: 1.01x slower                                                              |
| sympy_str               | 264 ms                                                                   | 267 ms: 1.01x slower                                                              |
| scimark_sparse_mat_mult | 6.45 ms                                                                  | 6.51 ms: 1.01x slower                                                             |
| bench_thread_pool       | 1.34 ms                                                                  | 1.35 ms: 1.01x slower                                                             |
| logging_format          | 7.65 us                                                                  | 7.72 us: 1.01x slower                                                             |
| python_startup_no_site  | 10.2 ms                                                                  | 10.3 ms: 1.01x slower                                                             |
| 2to3                    | 295 ms                                                                   | 297 ms: 1.01x slower                                                              |
| async_tree_io           | 873 ms                                                                   | 881 ms: 1.01x slower                                                              |
| genshi_xml              | 59.8 ms                                                                  | 60.4 ms: 1.01x slower                                                             |
| python_startup          | 16.1 ms                                                                  | 16.2 ms: 1.01x slower                                                             |
| async_generators        | 436 ms                                                                   | 444 ms: 1.02x slower                                                              |
| async_tree_none         | 378 ms                                                                   | 386 ms: 1.02x slower                                                              |
| async_tree_none_tg      | 374 ms                                                                   | 384 ms: 1.03x slower                                                              |
| telco                   | 9.42 ms                                                                  | 10.0 ms: 1.06x slower                                                             |
| Geometric mean          | (ref)                                                                    | 1.00x slower                                                                      |

Benchmark hidden because not significant (67): bench_mp_pool, sympy_sum, go, pylint, typing_runtime_protocols, crypto_pyaes, deepcopy_memo, chaos, pprint_safe_repr, deepcopy, coverage, sympy_integrate, sqlalchemy_declarative, coroutines, pprint_pformat, hexiom, docutils, asyncio_websockets, async_tree_io_tg, sqlalchemy_imperative, xml_etree_iterparse, json_dumps, html5lib, regex_compile, bpe_tokeniser, sphinx, regex_v8, pycparser, xml_etree_parse, pyflate, async_tree_cpu_io_mixed_tg, raytrace, mdp, dulwich_log, pidigits, shortest_path, sqlglot_v2_parse, async_tree_cpu_io_mixed, float, logging_silent, k_core, many_optionals, genshi_text, unpickle_pure_python, pathlib, regex_dna, json, connected_components, comprehensions, sympy_expand, sqlglot_v2_normalize, async_tree_memoization_tg, sqlglot_v2_transpile, scimark_lu, sqlglot_v2_optimize, scimark_sor, gc_traversal, spectral_norm, pickle_pure_python, richards_super, create_gc_cycles, django_template, regex_effbot, scimark_fft, deltablue, scimark_monte_carlo, nbody

- Geometric mean (including insignificant results): 1.000x faster

# HPT report

- Reliability score: 62.23% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x