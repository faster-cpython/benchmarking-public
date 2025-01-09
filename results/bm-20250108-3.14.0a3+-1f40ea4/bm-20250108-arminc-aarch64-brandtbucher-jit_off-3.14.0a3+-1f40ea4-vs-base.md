# Results vs. base

- fork: brandtbucher
- ref: jit_off
- machine: linux-aarch64
- commit hash: 1f40ea4
- commit date: 2025-01-08
- overall geometric mean: 1.000x faster
- HPT reliability: 59.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (11): async_tree_memoization, asyncio_websockets, coroutines, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_io_tg, async_tree_io, async_generators, async_tree_none, async_tree_none_tg

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250106-arminc-aarch64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250108-arminc-aarch64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_dna      | 255 ms                                                                   | 244 ms: 1.04x faster                                              |
| Geometric mean | (ref)                                                                    | 1.03x faster                                                      |

Benchmark hidden because not significant (3): regex_compile, regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

Benchmark hidden because not significant (9): pickle_pure_python, xml_etree_parse, tomli_loads, xml_etree_generate, unpickle_pure_python, json_loads, json_dumps, xml_etree_process, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250106-arminc-aarch64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250108-arminc-aarch64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|-----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| django_template | 40.0 ms                                                                  | 42.2 ms: 1.05x slower                                             |
| Geometric mean  | (ref)                                                                    | 1.01x slower                                                      |

Benchmark hidden because not significant (3): mako, genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark       | bm-20250106-arminc-aarch64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250108-arminc-aarch64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|-----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_dna       | 255 ms                                                                   | 244 ms: 1.04x faster                                              |
| pyflate         | 589 ms                                                                   | 566 ms: 1.04x faster                                              |
| bpe_tokeniser   | 5.77 sec                                                                 | 5.84 sec: 1.01x slower                                            |
| sympy_str       | 273 ms                                                                   | 287 ms: 1.05x slower                                              |
| many_optionals  | 692 us                                                                   | 729 us: 1.05x slower                                              |
| django_template | 40.0 ms                                                                  | 42.2 ms: 1.05x slower                                             |
| Geometric mean  | (ref)                                                                    | 1.00x slower                                                      |

Benchmark hidden because not significant (90): logging_silent, regex_compile, regex_effbot, logging_simple, telco, pprint_safe_repr, coverage, scimark_sparse_mat_mult, crypto_pyaes, pickle_pure_python, richards, xml_etree_parse, nqueens, hexiom, scimark_lu, fannkuch, docutils, create_gc_cycles, pprint_pformat, async_tree_memoization, tomli_loads, mako, sqlglot_normalize, dulwich_log, genshi_text, asyncio_websockets, gc_traversal, generators, richards_super, nbody, bench_thread_pool, raytrace, json, spectral_norm, scimark_monte_carlo, comprehensions, deepcopy_memo, sphinx, meteor_contest, deltablue, shortest_path, pidigits, float, sqlglot_transpile, coroutines, async_tree_cpu_io_mixed, xml_etree_generate, sympy_sum, scimark_sor, python_startup_no_site, typing_runtime_protocols, mdp, thrift, async_tree_cpu_io_mixed_tg, unpickle_pure_python, 2to3, async_tree_memoization_tg, json_loads, k_core, async_tree_io_tg, bench_mp_pool, html5lib, json_dumps, logging_format, regex_v8, pycparser, deepcopy_reduce, sqlglot_parse, sqlglot_optimize, python_startup, pylint, sqlite_synth, scimark_fft, sympy_integrate, async_tree_io, async_generators, async_tree_none, connected_components, sympy_expand, xml_etree_process, xml_etree_iterparse, go, genshi_xml, chaos, async_tree_none_tg, pathlib, subparsers, sqlalchemy_imperative, sqlalchemy_declarative, deepcopy
Ignored benchmarks (1) of results/bm-20250106-3.14.0a3+-7363476/bm-20250106-arminc-aarch64-python-7363476b6405e3d288a6-3.14.0a3+-7363476.json: mypy2

- Geometric mean (including insignificant results): 1.000x faster

# HPT report

- Reliability score: 59.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x