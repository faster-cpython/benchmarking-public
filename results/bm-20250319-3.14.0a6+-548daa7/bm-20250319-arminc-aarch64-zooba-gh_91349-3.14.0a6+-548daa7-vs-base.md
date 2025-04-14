# Results vs. base

- fork: zooba
- ref: gh_91349
- machine: linux-aarch64
- commit hash: 548daa7
- commit date: 2025-03-19
- overall geometric mean: 1.000x faster
- HPT reliability: 95.84%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250318-arminc-aarch64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b | bm-20250319-arminc-aarch64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| docutils       | 2.97 sec                                                                 | 3.07 sec: 1.03x slower                                      |
| Geometric mean | (ref)                                                                    | 1.01x slower                                                |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (11): async_generators, async_tree_memoization_tg, async_tree_none, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_none_tg, asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, float, pidigits

Benchmarks with tag 'regex':
============================

Benchmark hidden because not significant (4): regex_effbot, regex_compile, regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark      | bm-20250318-arminc-aarch64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b | bm-20250319-arminc-aarch64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| tomli_loads    | 2.48 sec                                                                 | 2.45 sec: 1.01x faster                                      |
| Geometric mean | (ref)                                                                    | 1.01x faster                                                |

Benchmark hidden because not significant (8): xml_etree_process, pickle_pure_python, xml_etree_generate, xml_etree_iterparse, json_dumps, xml_etree_parse, unpickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_xml, mako, genshi_text, django_template

All benchmarks:
===============

| Benchmark               | bm-20250318-arminc-aarch64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b | bm-20250319-arminc-aarch64-zooba-gh_91349-3.14.0a6+-548daa7 |
|-------------------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| pylint                  | 334 ms                                                                   | 311 ms: 1.08x faster                                        |
| pprint_pformat          | 1.97 sec                                                                 | 1.92 sec: 1.03x faster                                      |
| pprint_safe_repr        | 959 ms                                                                   | 940 ms: 1.02x faster                                        |
| thrift                  | 949 us                                                                   | 936 us: 1.01x faster                                        |
| sqlite_synth            | 3.87 us                                                                  | 3.82 us: 1.01x faster                                       |
| tomli_loads             | 2.48 sec                                                                 | 2.45 sec: 1.01x faster                                      |
| nqueens                 | 104 ms                                                                   | 103 ms: 1.01x faster                                        |
| scimark_sparse_mat_mult | 6.59 ms                                                                  | 6.54 ms: 1.01x faster                                       |
| mdp                     | 3.31 sec                                                                 | 3.34 sec: 1.01x slower                                      |
| sqlglot_v2_transpile    | 1.77 ms                                                                  | 1.79 ms: 1.01x slower                                       |
| bench_thread_pool       | 1.34 ms                                                                  | 1.35 ms: 1.01x slower                                       |
| generators              | 35.7 ms                                                                  | 36.3 ms: 1.02x slower                                       |
| shortest_path           | 579 ms                                                                   | 591 ms: 1.02x slower                                        |
| pyflate                 | 548 ms                                                                   | 561 ms: 1.02x slower                                        |
| k_core                  | 2.78 sec                                                                 | 2.84 sec: 1.02x slower                                      |
| docutils                | 2.97 sec                                                                 | 3.07 sec: 1.03x slower                                      |
| json                    | 5.79 ms                                                                  | 5.97 ms: 1.03x slower                                       |
| sympy_str               | 267 ms                                                                   | 277 ms: 1.04x slower                                        |
| scimark_lu              | 149 ms                                                                   | 157 ms: 1.05x slower                                        |
| Geometric mean          | (ref)                                                                    | 1.00x slower                                                |

Benchmark hidden because not significant (77): xml_etree_process, pickle_pure_python, nbody, scimark_monte_carlo, async_generators, create_gc_cycles, chaos, pathlib, fannkuch, xml_etree_generate, comprehensions, dulwich_log, sqlglot_v2_normalize, genshi_xml, sqlglot_v2_optimize, raytrace, async_tree_memoization_tg, spectral_norm, typing_runtime_protocols, async_tree_none, async_tree_io, many_optionals, float, sympy_integrate, sqlalchemy_declarative, mako, subparsers, async_tree_cpu_io_mixed_tg, richards_super, xml_etree_iterparse, bpe_tokeniser, json_dumps, async_tree_memoization, async_tree_cpu_io_mixed, logging_format, python_startup, go, xml_etree_parse, python_startup_no_site, scimark_fft, meteor_contest, pidigits, genshi_text, richards, sqlglot_v2_parse, unpickle_pure_python, connected_components, telco, gc_traversal, async_tree_io_tg, logging_simple, html5lib, sphinx, async_tree_none_tg, sympy_expand, pycparser, django_template, regex_effbot, asyncio_websockets, logging_silent, coverage, regex_compile, regex_dna, 2to3, deepcopy_reduce, coroutines, scimark_sor, deltablue, json_loads, sqlalchemy_imperative, sympy_sum, deepcopy_memo, crypto_pyaes, deepcopy, regex_v8, hexiom, bench_mp_pool

- Geometric mean (including insignificant results): 1.000x faster

# HPT report

- Reliability score: 95.84% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x