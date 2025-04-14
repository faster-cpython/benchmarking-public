# Results vs. base

- fork: brandtbucher
- ref: justin_mcmodel_again
- machine: linux-aarch64
- commit hash: 86ef9a1
- commit date: 2025-02-12
- overall geometric mean: 1.000x faster
- HPT reliability: 99.46%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250209-arminc-aarch64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250212-arminc-aarch64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| docutils       | 3.31 sec                                                                 | 3.23 sec: 1.03x faster                                                         |
| Geometric mean | (ref)                                                                    | 1.01x faster                                                                   |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (11): async_tree_cpu_io_mixed, async_tree_memoization_tg, asyncio_websockets, async_tree_none, async_tree_io_tg, async_tree_io, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_generators, coroutines

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250209-arminc-aarch64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250212-arminc-aarch64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 270 ms                                                                   | 252 ms: 1.07x faster                                                           |
| Geometric mean | (ref)                                                                    | 1.02x faster                                                                   |

Benchmark hidden because not significant (3): regex_v8, regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark       | bm-20250209-arminc-aarch64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250212-arminc-aarch64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|-----------------|:------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_parse | 193 ms                                                                   | 180 ms: 1.07x faster                                                           |
| tomli_loads     | 2.49 sec                                                                 | 2.55 sec: 1.03x slower                                                         |
| Geometric mean  | (ref)                                                                    | 1.01x slower                                                                   |

Benchmark hidden because not significant (7): pickle_pure_python, json_dumps, xml_etree_iterparse, json_loads, xml_etree_process, unpickle_pure_python, xml_etree_generate

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_text, mako, genshi_xml, django_template

All benchmarks:
===============

| Benchmark             | bm-20250209-arminc-aarch64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250212-arminc-aarch64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|-----------------------|:------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| bench_mp_pool         | 3.09 sec                                                                 | 2.14 sec: 1.45x faster                                                         |
| xml_etree_parse       | 193 ms                                                                   | 180 ms: 1.07x faster                                                           |
| regex_dna             | 270 ms                                                                   | 252 ms: 1.07x faster                                                           |
| dulwich_log           | 67.1 ms                                                                  | 64.1 ms: 1.05x faster                                                          |
| docutils              | 3.31 sec                                                                 | 3.23 sec: 1.03x faster                                                         |
| thrift                | 928 us                                                                   | 919 us: 1.01x faster                                                           |
| bpe_tokeniser         | 5.72 sec                                                                 | 5.76 sec: 1.01x slower                                                         |
| tomli_loads           | 2.49 sec                                                                 | 2.55 sec: 1.03x slower                                                         |
| richards              | 51.1 ms                                                                  | 53.0 ms: 1.04x slower                                                          |
| pathlib               | 21.9 ms                                                                  | 23.3 ms: 1.06x slower                                                          |
| sqlalchemy_imperative | 15.9 ms                                                                  | 17.2 ms: 1.08x slower                                                          |
| Geometric mean        | (ref)                                                                    | 1.00x slower                                                                   |

Benchmark hidden because not significant (85): deepcopy, pylint, comprehensions, sympy_sum, scimark_monte_carlo, float, sqlite_synth, meteor_contest, chaos, regex_v8, pidigits, json, scimark_lu, deepcopy_memo, subparsers, sympy_expand, generators, telco, regex_effbot, k_core, many_optionals, deepcopy_reduce, sympy_str, pickle_pure_python, async_tree_cpu_io_mixed, genshi_text, 2to3, pycparser, mdp, sphinx, shortest_path, create_gc_cycles, hexiom, sympy_integrate, raytrace, async_tree_memoization_tg, asyncio_websockets, bench_thread_pool, sqlglot_normalize, pyflate, mako, logging_format, async_tree_none, json_dumps, fannkuch, gc_traversal, xml_etree_iterparse, async_tree_io_tg, async_tree_io, python_startup_no_site, deltablue, sqlglot_parse, genshi_xml, sqlalchemy_declarative, html5lib, async_tree_memoization, async_tree_cpu_io_mixed_tg, pprint_pformat, typing_runtime_protocols, connected_components, pprint_safe_repr, sqlglot_optimize, logging_silent, regex_compile, python_startup, json_loads, nqueens, async_tree_none_tg, async_generators, scimark_sparse_mat_mult, sqlglot_transpile, coverage, scimark_fft, coroutines, go, xml_etree_process, unpickle_pure_python, nbody, crypto_pyaes, scimark_sor, spectral_norm, xml_etree_generate, logging_simple, django_template, richards_super

- Geometric mean (including insignificant results): 1.000x faster

# HPT report

- Reliability score: 99.46% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x