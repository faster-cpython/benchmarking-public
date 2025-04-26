# Results vs. base

- fork: mdboom
- ref: python_startup_time
- machine: linux-aarch64
- commit hash: 9fc1238
- commit date: 2025-04-25
- overall geometric mean: 1.005x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250421-arminc-aarch64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 | bm-20250425-arminc-aarch64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 2.97 sec                                                                 | 2.94 sec: 1.01x faster                                                  |
| html5lib       | 62.4 ms                                                                  | 61.5 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20250421-arminc-aarch64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 | bm-20250425-arminc-aarch64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|---------------------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization    | 481 ms                                                                   | 464 ms: 1.03x faster                                                    |
| async_tree_none_tg        | 383 ms                                                                   | 373 ms: 1.03x faster                                                    |
| async_tree_memoization_tg | 475 ms                                                                   | 466 ms: 1.02x faster                                                    |
| async_tree_none           | 390 ms                                                                   | 386 ms: 1.01x faster                                                    |
| async_tree_io             | 882 ms                                                                   | 892 ms: 1.01x slower                                                    |
| Geometric mean            | (ref)                                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (6): async_generators, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_cpu_io_mixed, async_tree_io_tg, coroutines

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): pidigits, float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250421-arminc-aarch64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 | bm-20250425-arminc-aarch64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 234 ms                                                                   | 236 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (3): regex_v8, regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250421-arminc-aarch64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 | bm-20250425-arminc-aarch64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|---------------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_dumps          | 14.2 ms                                                                  | 13.8 ms: 1.03x faster                                                   |
| xml_etree_iterparse | 143 ms                                                                   | 141 ms: 1.01x faster                                                    |
| json_loads          | 34.5 us                                                                  | 34.2 us: 1.01x faster                                                   |
| pickle_pure_python  | 381 us                                                                   | 379 us: 1.01x faster                                                    |
| xml_etree_generate  | 113 ms                                                                   | 112 ms: 1.01x faster                                                    |
| Geometric mean      | (ref)                                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (4): unpickle_pure_python, xml_etree_parse, tomli_loads, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250421-arminc-aarch64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 | bm-20250425-arminc-aarch64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|------------------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 10.2 ms                                                                  | 9.08 ms: 1.12x faster                                                   |
| python_startup         | 16.2 ms                                                                  | 16.3 ms: 1.01x slower                                                   |
| Geometric mean         | (ref)                                                                    | 1.05x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250421-arminc-aarch64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 | bm-20250425-arminc-aarch64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text    | 26.5 ms                                                                  | 26.0 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (3): mako, django_template, genshi_xml

All benchmarks:
===============

| Benchmark                 | bm-20250421-arminc-aarch64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 | bm-20250425-arminc-aarch64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|---------------------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site    | 10.2 ms                                                                  | 9.08 ms: 1.12x faster                                                   |
| sympy_str                 | 271 ms                                                                   | 258 ms: 1.05x faster                                                    |
| async_tree_memoization    | 481 ms                                                                   | 464 ms: 1.03x faster                                                    |
| mdp                       | 1.68 sec                                                                 | 1.62 sec: 1.03x faster                                                  |
| logging_silent            | 133 ns                                                                   | 129 ns: 1.03x faster                                                    |
| async_tree_none_tg        | 383 ms                                                                   | 373 ms: 1.03x faster                                                    |
| json_dumps                | 14.2 ms                                                                  | 13.8 ms: 1.03x faster                                                   |
| pycparser                 | 1.27 sec                                                                 | 1.24 sec: 1.02x faster                                                  |
| async_tree_memoization_tg | 475 ms                                                                   | 466 ms: 1.02x faster                                                    |
| genshi_text               | 26.5 ms                                                                  | 26.0 ms: 1.02x faster                                                   |
| pyflate                   | 531 ms                                                                   | 521 ms: 1.02x faster                                                    |
| logging_format            | 7.82 us                                                                  | 7.67 us: 1.02x faster                                                   |
| logging_simple            | 7.01 us                                                                  | 6.90 us: 1.02x faster                                                   |
| bpe_tokeniser             | 5.44 sec                                                                 | 5.35 sec: 1.02x faster                                                  |
| html5lib                  | 62.4 ms                                                                  | 61.5 ms: 1.01x faster                                                   |
| xml_etree_iterparse       | 143 ms                                                                   | 141 ms: 1.01x faster                                                    |
| docutils                  | 2.97 sec                                                                 | 2.94 sec: 1.01x faster                                                  |
| json_loads                | 34.5 us                                                                  | 34.2 us: 1.01x faster                                                   |
| async_tree_none           | 390 ms                                                                   | 386 ms: 1.01x faster                                                    |
| generators                | 36.8 ms                                                                  | 36.5 ms: 1.01x faster                                                   |
| pickle_pure_python        | 381 us                                                                   | 379 us: 1.01x faster                                                    |
| xml_etree_generate        | 113 ms                                                                   | 112 ms: 1.01x faster                                                    |
| regex_dna                 | 234 ms                                                                   | 236 ms: 1.01x slower                                                    |
| python_startup            | 16.2 ms                                                                  | 16.3 ms: 1.01x slower                                                   |
| async_tree_io             | 882 ms                                                                   | 892 ms: 1.01x slower                                                    |
| connected_components      | 552 ms                                                                   | 559 ms: 1.01x slower                                                    |
| pprint_pformat            | 1.83 sec                                                                 | 1.87 sec: 1.02x slower                                                  |
| Geometric mean            | (ref)                                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (68): regex_v8, chaos, regex_compile, mako, deepcopy_reduce, sqlglot_v2_normalize, telco, many_optionals, spectral_norm, typing_runtime_protocols, comprehensions, async_generators, scimark_monte_carlo, sqlite_synth, sqlalchemy_imperative, pidigits, scimark_lu, async_tree_cpu_io_mixed_tg, sympy_expand, json, sympy_integrate, richards, pylint, nqueens, deltablue, unpickle_pure_python, k_core, xml_etree_parse, sympy_sum, asyncio_websockets, shortest_path, subparsers, django_template, go, tomli_loads, async_tree_cpu_io_mixed, async_tree_io_tg, meteor_contest, sqlglot_v2_optimize, scimark_fft, float, coverage, sqlglot_v2_parse, coroutines, pathlib, sqlalchemy_declarative, xml_etree_process, deepcopy, raytrace, 2to3, crypto_pyaes, hexiom, richards_super, sphinx, scimark_sparse_mat_mult, scimark_sor, gc_traversal, bench_thread_pool, pprint_safe_repr, genshi_xml, sqlglot_v2_transpile, dulwich_log, create_gc_cycles, fannkuch, deepcopy_memo, bench_mp_pool, nbody, regex_effbot

- Geometric mean (including insignificant results): 1.005x faster

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x