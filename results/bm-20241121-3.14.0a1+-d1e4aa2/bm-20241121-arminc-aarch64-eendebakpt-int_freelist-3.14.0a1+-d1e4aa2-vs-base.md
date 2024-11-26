# Results vs. base

- fork: eendebakpt
- ref: int_freelist
- machine: linux-aarch64
- commit hash: d1e4aa2
- commit date: 2024-11-21
- overall geometric mean: 1.004x faster
- HPT reliability: 99.75%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (11): async_tree_none, coroutines, async_generators, asyncio_websockets, async_tree_io, async_tree_io_tg, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_memoization

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241116-arminc-aarch64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241121-arminc-aarch64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_dna      | 266 ms                                                                   | 255 ms: 1.04x faster                                                 |
| Geometric mean | (ref)                                                                    | 1.03x faster                                                         |

Benchmark hidden because not significant (3): regex_v8, regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark      | bm-20241116-arminc-aarch64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241121-arminc-aarch64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads    | 2.76 sec                                                                 | 2.66 sec: 1.04x faster                                               |
| Geometric mean | (ref)                                                                    | 1.00x slower                                                         |

Benchmark hidden because not significant (8): json_dumps, xml_etree_iterparse, json_loads, xml_etree_process, xml_etree_generate, xml_etree_parse, pickle_pure_python, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_xml, genshi_text, mako, django_template

All benchmarks:
===============

| Benchmark               | bm-20241116-arminc-aarch64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241121-arminc-aarch64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|-------------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| spectral_norm           | 149 ms                                                                   | 130 ms: 1.15x faster                                                 |
| scimark_fft             | 461 ms                                                                   | 422 ms: 1.09x faster                                                 |
| scimark_sparse_mat_mult | 6.76 ms                                                                  | 6.22 ms: 1.09x faster                                                |
| richards                | 56.0 ms                                                                  | 53.6 ms: 1.04x faster                                                |
| regex_dna               | 266 ms                                                                   | 255 ms: 1.04x faster                                                 |
| sympy_str               | 278 ms                                                                   | 266 ms: 1.04x faster                                                 |
| tomli_loads             | 2.76 sec                                                                 | 2.66 sec: 1.04x faster                                               |
| pyflate                 | 604 ms                                                                   | 582 ms: 1.04x faster                                                 |
| dulwich_log             | 58.6 ms                                                                  | 59.6 ms: 1.02x slower                                                |
| deepcopy_reduce         | 3.58 us                                                                  | 3.66 us: 1.02x slower                                                |
| create_gc_cycles        | 3.76 ms                                                                  | 3.93 ms: 1.05x slower                                                |
| sqlalchemy_imperative   | 15.3 ms                                                                  | 16.2 ms: 1.06x slower                                                |
| Geometric mean          | (ref)                                                                    | 1.00x faster                                                         |

Benchmark hidden because not significant (85): regex_v8, scimark_sor, chaos, raytrace, deltablue, crypto_pyaes, subparsers, sqlglot_parse, djangocms, pprint_safe_repr, pathlib, json, async_tree_none, coroutines, async_generators, html5lib, nbody, k_core, genshi_xml, regex_effbot, json_dumps, many_optionals, shortest_path, asyncio_websockets, xml_etree_iterparse, mdp, genshi_text, async_tree_io, hexiom, sphinx, gc_traversal, regex_compile, logging_silent, float, async_tree_io_tg, connected_components, json_loads, scimark_monte_carlo, sympy_sum, scimark_lu, sqlalchemy_declarative, pprint_pformat, deepcopy_memo, bpe_tokeniser, async_tree_none_tg, sympy_expand, xml_etree_process, docutils, python_startup_no_site, async_tree_cpu_io_mixed_tg, python_startup, pycparser, async_tree_memoization_tg, meteor_contest, sqlglot_optimize, 2to3, mako, nqueens, sqlite_synth, async_tree_cpu_io_mixed, comprehensions, fannkuch, pidigits, pylint, go, generators, bench_thread_pool, thrift, typing_runtime_protocols, xml_etree_generate, xml_etree_parse, sqlglot_normalize, logging_format, pickle_pure_python, logging_simple, sympy_integrate, async_tree_memoization, coverage, deepcopy, django_template, richards_super, sqlglot_transpile, telco, unpickle_pure_python, bench_mp_pool

- Geometric mean (including insignificant results): 1.004x faster
# HPT report

- Reliability score: 99.75% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x