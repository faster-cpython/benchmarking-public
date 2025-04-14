# Results vs. base

- fork: faster-cpython
- ref: immortal_stickiness
- machine: linux-aarch64
- commit hash: 490cf8d
- commit date: 2025-03-12
- overall geometric mean: 1.002x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250312-arminc-aarch64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 294 ms                                                                   | 300 ms: 1.02x slower                                                              |
| docutils       | 2.91 sec                                                                 | 2.95 sec: 1.01x slower                                                            |
| Geometric mean | (ref)                                                                    | 1.01x slower                                                                      |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250312-arminc-aarch64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 642 ms                                                                   | 646 ms: 1.01x slower                                                              |
| async_tree_none            | 379 ms                                                                   | 386 ms: 1.02x slower                                                              |
| async_generators           | 434 ms                                                                   | 449 ms: 1.03x slower                                                              |
| Geometric mean             | (ref)                                                                    | 1.01x slower                                                                      |

Benchmark hidden because not significant (8): coroutines, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_io_tg, asyncio_websockets, async_tree_none_tg, async_tree_memoization_tg, async_tree_io

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): pidigits, float, nbody

Benchmarks with tag 'regex':
============================

Benchmark hidden because not significant (4): regex_v8, regex_compile, regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250312-arminc-aarch64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|--------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_pure_python | 382 us                                                                   | 386 us: 1.01x slower                                                              |
| tomli_loads        | 2.44 sec                                                                 | 2.48 sec: 1.02x slower                                                            |
| Geometric mean     | (ref)                                                                    | 1.01x slower                                                                      |

Benchmark hidden because not significant (7): json_dumps, xml_etree_parse, xml_etree_generate, xml_etree_iterparse, xml_etree_process, json_loads, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250312-arminc-aarch64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup | 16.1 ms                                                                  | 16.0 ms: 1.00x faster                                                             |
| Geometric mean | (ref)                                                                    | 1.00x faster                                                                      |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): mako, genshi_xml, genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | bm-20250312-arminc-aarch64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| create_gc_cycles           | 3.66 ms                                                                  | 3.57 ms: 1.03x faster                                                             |
| mdp                        | 3.38 sec                                                                 | 3.32 sec: 1.02x faster                                                            |
| python_startup             | 16.1 ms                                                                  | 16.0 ms: 1.00x faster                                                             |
| async_tree_cpu_io_mixed_tg | 642 ms                                                                   | 646 ms: 1.01x slower                                                              |
| spectral_norm              | 121 ms                                                                   | 122 ms: 1.01x slower                                                              |
| logging_simple             | 6.97 us                                                                  | 7.02 us: 1.01x slower                                                             |
| meteor_contest             | 112 ms                                                                   | 113 ms: 1.01x slower                                                              |
| subparsers                 | 25.4 ms                                                                  | 25.7 ms: 1.01x slower                                                             |
| shortest_path              | 576 ms                                                                   | 581 ms: 1.01x slower                                                              |
| sqlglot_v2_normalize       | 125 ms                                                                   | 127 ms: 1.01x slower                                                              |
| pickle_pure_python         | 382 us                                                                   | 386 us: 1.01x slower                                                              |
| docutils                   | 2.91 sec                                                                 | 2.95 sec: 1.01x slower                                                            |
| tomli_loads                | 2.44 sec                                                                 | 2.48 sec: 1.02x slower                                                            |
| async_tree_none            | 379 ms                                                                   | 386 ms: 1.02x slower                                                              |
| 2to3                       | 294 ms                                                                   | 300 ms: 1.02x slower                                                              |
| nqueens                    | 99.7 ms                                                                  | 102 ms: 1.02x slower                                                              |
| go                         | 135 ms                                                                   | 139 ms: 1.03x slower                                                              |
| async_generators           | 434 ms                                                                   | 449 ms: 1.03x slower                                                              |
| pyflate                    | 547 ms                                                                   | 577 ms: 1.05x slower                                                              |
| Geometric mean             | (ref)                                                                    | 1.01x slower                                                                      |

Benchmark hidden because not significant (77): richards, coverage, regex_v8, scimark_lu, json_dumps, logging_silent, scimark_monte_carlo, gc_traversal, sqlglot_v2_optimize, sqlglot_v2_parse, sympy_str, coroutines, generators, bench_thread_pool, json, k_core, crypto_pyaes, mako, dulwich_log, telco, python_startup_no_site, scimark_sparse_mat_mult, async_tree_memoization, thrift, async_tree_cpu_io_mixed, pylint, async_tree_io_tg, sqlite_synth, sympy_expand, chaos, scimark_fft, deepcopy, asyncio_websockets, xml_etree_parse, pidigits, connected_components, async_tree_none_tg, scimark_sor, xml_etree_generate, xml_etree_iterparse, raytrace, async_tree_memoization_tg, xml_etree_process, bpe_tokeniser, genshi_xml, sphinx, float, pycparser, sqlalchemy_declarative, genshi_text, async_tree_io, html5lib, regex_compile, sqlalchemy_imperative, pprint_pformat, json_loads, regex_dna, pprint_safe_repr, comprehensions, sympy_sum, typing_runtime_protocols, many_optionals, logging_format, richards_super, deltablue, fannkuch, django_template, hexiom, sympy_integrate, sqlglot_v2_transpile, unpickle_pure_python, deepcopy_reduce, pathlib, nbody, regex_effbot, deepcopy_memo, bench_mp_pool

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x