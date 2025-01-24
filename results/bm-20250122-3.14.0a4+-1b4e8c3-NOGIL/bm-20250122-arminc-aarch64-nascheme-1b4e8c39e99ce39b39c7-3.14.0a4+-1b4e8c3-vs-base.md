# Results vs. base

- fork: nascheme
- ref: 1b4e8c39e99ce39b39c7
- machine: linux-aarch64
- commit hash: 1b4e8c3
- commit date: 2025-01-22
- overall geometric mean: 1.001x slower
- HPT reliability: 97.17%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250117-arminc-aarch64-python-3829104ab412a47bf3f3-3.14.0a4+-3829104 | bm-20250122-arminc-aarch64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 3.43 sec                                                                 | 3.38 sec: 1.01x faster                                                     |
| sphinx         | 1.41 sec                                                                 | 1.38 sec: 1.02x faster                                                     |
| Geometric mean | (ref)                                                                    | 1.02x faster                                                               |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (11): async_generators, async_tree_memoization_tg, async_tree_none, async_tree_io, async_tree_none_tg, asyncio_websockets, coroutines, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): pidigits, float, nbody

Benchmarks with tag 'regex':
============================

Benchmark hidden because not significant (4): regex_dna, regex_v8, regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark      | bm-20250117-arminc-aarch64-python-3829104ab412a47bf3f3-3.14.0a4+-3829104 | bm-20250122-arminc-aarch64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads    | 3.24 sec                                                                 | 3.18 sec: 1.02x faster                                                     |
| Geometric mean | (ref)                                                                    | 1.01x faster                                                               |

Benchmark hidden because not significant (4): json_dumps, pickle_pure_python, json_loads, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): django_template, genshi_xml, mako, genshi_text

All benchmarks:
===============

| Benchmark        | bm-20250117-arminc-aarch64-python-3829104ab412a47bf3f3-3.14.0a4+-3829104 | bm-20250122-arminc-aarch64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pprint_pformat   | 2.43 sec                                                                 | 2.38 sec: 1.02x faster                                                     |
| sphinx           | 1.41 sec                                                                 | 1.38 sec: 1.02x faster                                                     |
| tomli_loads      | 3.24 sec                                                                 | 3.18 sec: 1.02x faster                                                     |
| docutils         | 3.43 sec                                                                 | 3.38 sec: 1.01x faster                                                     |
| k_core           | 3.22 sec                                                                 | 3.29 sec: 1.02x slower                                                     |
| shortest_path    | 689 ms                                                                   | 710 ms: 1.03x slower                                                       |
| bench_mp_pool    | 57.3 ms                                                                  | 59.2 ms: 1.03x slower                                                      |
| create_gc_cycles | 2.16 ms                                                                  | 2.29 ms: 1.06x slower                                                      |
| dulwich_log      | 69.0 ms                                                                  | 73.2 ms: 1.06x slower                                                      |
| Geometric mean   | (ref)                                                                    | 1.00x faster                                                               |

Benchmark hidden because not significant (83): richards, comprehensions, pidigits, django_template, deepcopy, regex_dna, deltablue, coverage, sqlite_synth, sqlalchemy_declarative, logging_silent, 2to3, logging_format, regex_v8, html5lib, scimark_sor, pathlib, connected_components, deepcopy_reduce, json_dumps, float, pickle_pure_python, regex_compile, pprint_safe_repr, scimark_fft, telco, sqlglot_parse, sympy_expand, regex_effbot, sqlglot_transpile, async_generators, chaos, async_tree_memoization_tg, async_tree_none, raytrace, genshi_xml, crypto_pyaes, go, json_loads, mako, async_tree_io, logging_simple, bench_thread_pool, meteor_contest, sympy_str, async_tree_none_tg, bpe_tokeniser, scimark_monte_carlo, scimark_sparse_mat_mult, pylint, asyncio_websockets, coroutines, typing_runtime_protocols, sqlalchemy_imperative, python_startup_no_site, async_tree_io_tg, gc_traversal, sympy_integrate, mdp, json, fannkuch, unpickle_pure_python, many_optionals, genshi_text, async_tree_cpu_io_mixed, pyflate, async_tree_cpu_io_mixed_tg, generators, nqueens, pycparser, sqlglot_normalize, async_tree_memoization, richards_super, subparsers, hexiom, thrift, python_startup, deepcopy_memo, sqlglot_optimize, scimark_lu, nbody, spectral_norm, sympy_sum
Ignored benchmarks (4) of results/bm-20250117-3.14.0a4+-3829104-NOGIL/bm-20250117-arminc-aarch64-python-3829104ab412a47bf3f3-3.14.0a4+-3829104.json: xml_etree_generate, xml_etree_iterparse, xml_etree_parse, xml_etree_process

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 97.17% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x