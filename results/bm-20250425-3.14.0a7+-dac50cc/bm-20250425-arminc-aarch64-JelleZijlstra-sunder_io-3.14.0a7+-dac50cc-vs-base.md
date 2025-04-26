# Results vs. base

- fork: JelleZijlstra
- ref: sunder_io
- machine: linux-aarch64
- commit hash: dac50cc
- commit date: 2025-04-25
- overall geometric mean: 1.002x faster
- HPT reliability: 75.82%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250425-arminc-aarch64-python-17718b0503e5d1c98725-3.14.0a7+-17718b0 | bm-20250425-arminc-aarch64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none_tg         | 384 ms                                                                   | 373 ms: 1.03x faster                                                 |
| async_tree_cpu_io_mixed_tg | 660 ms                                                                   | 644 ms: 1.03x faster                                                 |
| async_tree_io_tg           | 901 ms                                                                   | 887 ms: 1.02x faster                                                 |
| async_tree_memoization_tg  | 470 ms                                                                   | 463 ms: 1.02x faster                                                 |
| async_tree_memoization     | 465 ms                                                                   | 461 ms: 1.01x faster                                                 |
| Geometric mean             | (ref)                                                                    | 1.02x faster                                                         |

Benchmark hidden because not significant (6): coroutines, async_tree_io, async_tree_cpu_io_mixed, async_generators, async_tree_none, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250425-arminc-aarch64-python-17718b0503e5d1c98725-3.14.0a7+-17718b0 | bm-20250425-arminc-aarch64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 84.0 ms                                                                  | 84.8 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                    | 1.00x slower                                                         |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250425-arminc-aarch64-python-17718b0503e5d1c98725-3.14.0a7+-17718b0 | bm-20250425-arminc-aarch64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_dna      | 241 ms                                                                   | 236 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                                    | 1.03x faster                                                         |

Benchmark hidden because not significant (3): regex_v8, regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250425-arminc-aarch64-python-17718b0503e5d1c98725-3.14.0a7+-17718b0 | bm-20250425-arminc-aarch64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|---------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_process   | 80.4 ms                                                                  | 79.5 ms: 1.01x faster                                                |
| tomli_loads         | 2.41 sec                                                                 | 2.44 sec: 1.01x slower                                               |
| xml_etree_iterparse | 141 ms                                                                   | 144 ms: 1.02x slower                                                 |
| Geometric mean      | (ref)                                                                    | 1.00x slower                                                         |

Benchmark hidden because not significant (6): pickle_pure_python, xml_etree_parse, xml_etree_generate, unpickle_pure_python, json_dumps, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250425-arminc-aarch64-python-17718b0503e5d1c98725-3.14.0a7+-17718b0 | bm-20250425-arminc-aarch64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|------------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 10.2 ms                                                                  | 8.59 ms: 1.18x faster                                                |
| python_startup         | 16.1 ms                                                                  | 16.2 ms: 1.01x slower                                                |
| Geometric mean         | (ref)                                                                    | 1.08x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250425-arminc-aarch64-python-17718b0503e5d1c98725-3.14.0a7+-17718b0 | bm-20250425-arminc-aarch64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako           | 13.8 ms                                                                  | 14.0 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                    | 1.01x faster                                                         |

Benchmark hidden because not significant (3): genshi_xml, genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | bm-20250425-arminc-aarch64-python-17718b0503e5d1c98725-3.14.0a7+-17718b0 | bm-20250425-arminc-aarch64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| bench_mp_pool              | 3.43 sec                                                                 | 2.22 sec: 1.54x faster                                               |
| python_startup_no_site     | 10.2 ms                                                                  | 8.59 ms: 1.18x faster                                                |
| sympy_str                  | 269 ms                                                                   | 259 ms: 1.04x faster                                                 |
| async_tree_none_tg         | 384 ms                                                                   | 373 ms: 1.03x faster                                                 |
| async_tree_cpu_io_mixed_tg | 660 ms                                                                   | 644 ms: 1.03x faster                                                 |
| regex_dna                  | 241 ms                                                                   | 236 ms: 1.02x faster                                                 |
| coverage                   | 102 ms                                                                   | 100 ms: 1.02x faster                                                 |
| async_tree_io_tg           | 901 ms                                                                   | 887 ms: 1.02x faster                                                 |
| async_tree_memoization_tg  | 470 ms                                                                   | 463 ms: 1.02x faster                                                 |
| xml_etree_process          | 80.4 ms                                                                  | 79.5 ms: 1.01x faster                                                |
| async_tree_memoization     | 465 ms                                                                   | 461 ms: 1.01x faster                                                 |
| pprint_pformat             | 1.86 sec                                                                 | 1.84 sec: 1.01x faster                                               |
| logging_simple             | 7.05 us                                                                  | 7.00 us: 1.01x faster                                                |
| bpe_tokeniser              | 5.33 sec                                                                 | 5.35 sec: 1.00x slower                                               |
| python_startup             | 16.1 ms                                                                  | 16.2 ms: 1.01x slower                                                |
| float                      | 84.0 ms                                                                  | 84.8 ms: 1.01x slower                                                |
| tomli_loads                | 2.41 sec                                                                 | 2.44 sec: 1.01x slower                                               |
| mako                       | 13.8 ms                                                                  | 14.0 ms: 1.01x slower                                                |
| shortest_path              | 575 ms                                                                   | 584 ms: 1.02x slower                                                 |
| xml_etree_iterparse        | 141 ms                                                                   | 144 ms: 1.02x slower                                                 |
| pyflate                    | 539 ms                                                                   | 548 ms: 1.02x slower                                                 |
| sqlglot_v2_normalize       | 125 ms                                                                   | 132 ms: 1.06x slower                                                 |
| Geometric mean             | (ref)                                                                    | 1.01x faster                                                         |

Benchmark hidden because not significant (73): coroutines, regex_v8, pickle_pure_python, richards, logging_format, regex_effbot, many_optionals, regex_compile, genshi_xml, hexiom, pylint, sqlglot_v2_transpile, genshi_text, telco, comprehensions, json, deepcopy_reduce, async_tree_io, scimark_lu, sympy_expand, sqlglot_v2_parse, crypto_pyaes, connected_components, create_gc_cycles, async_tree_cpu_io_mixed, scimark_monte_carlo, scimark_sor, async_generators, async_tree_none, html5lib, xml_etree_parse, pycparser, gc_traversal, sphinx, scimark_sparse_mat_mult, pidigits, asyncio_websockets, sqlite_synth, sqlalchemy_imperative, dulwich_log, k_core, scimark_fft, deepcopy, generators, django_template, nqueens, xml_etree_generate, richards_super, unpickle_pure_python, 2to3, docutils, raytrace, typing_runtime_protocols, logging_silent, nbody, sqlalchemy_declarative, meteor_contest, bench_thread_pool, pprint_safe_repr, deltablue, sqlglot_v2_optimize, mdp, pathlib, spectral_norm, json_dumps, deepcopy_memo, sympy_integrate, go, json_loads, sympy_sum, fannkuch, subparsers, chaos

- Geometric mean (including insignificant results): 1.002x faster

# HPT report

- Reliability score: 75.82% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x