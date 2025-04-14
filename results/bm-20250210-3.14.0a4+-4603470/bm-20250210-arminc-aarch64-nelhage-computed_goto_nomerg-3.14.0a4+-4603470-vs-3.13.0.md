# Results vs. 3.13.0

- fork: nelhage
- ref: computed_goto_nomerg
- machine: linux-aarch64
- commit hash: 4603470
- commit date: 2025-02-10
- overall geometric mean: 1.037x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-arminc-aarch64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.02 sec: 1.02x slower                                                    |
| Geometric mean | (ref)                                                    | 1.01x faster                                                              |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-arminc-aarch64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 487 ms: 1.36x faster                                                      |
| async_tree_memoization     | 664 ms                                                   | 499 ms: 1.33x faster                                                      |
| async_tree_none            | 504 ms                                                   | 396 ms: 1.27x faster                                                      |
| async_tree_io_tg           | 1.16 sec                                                 | 922 ms: 1.26x faster                                                      |
| async_tree_none_tg         | 484 ms                                                   | 391 ms: 1.24x faster                                                      |
| async_tree_io              | 1.14 sec                                                 | 925 ms: 1.23x faster                                                      |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 679 ms: 1.18x faster                                                      |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 686 ms: 1.15x faster                                                      |
| async_generators           | 500 ms                                                   | 458 ms: 1.09x faster                                                      |
| Geometric mean             | (ref)                                                    | 1.19x faster                                                              |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-arminc-aarch64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 87.0 ms: 1.10x faster                                                     |
| Geometric mean | (ref)                                                    | 1.01x faster                                                              |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-arminc-aarch64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.05 ms: 1.26x faster                                                     |
| Geometric mean | (ref)                                                    | 1.07x faster                                                              |

Benchmark hidden because not significant (3): regex_compile, regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-arminc-aarch64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|-----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_parse | 203 ms                                                   | 183 ms: 1.11x faster                                                      |
| tomli_loads     | 2.67 sec                                                 | 2.53 sec: 1.05x faster                                                    |
| json_loads      | 32.8 us                                                  | 34.8 us: 1.06x slower                                                     |
| Geometric mean  | (ref)                                                    | 1.00x slower                                                              |

Benchmark hidden because not significant (6): xml_etree_generate, unpickle_pure_python, xml_etree_process, xml_etree_iterparse, json_dumps, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-arminc-aarch64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 9.05 ms: 1.03x slower                                                     |
| Geometric mean         | (ref)                                                    | 1.03x slower                                                              |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_text, mako, genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-arminc-aarch64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy                   | 479 us                                                   | 347 us: 1.38x faster                                                      |
| async_tree_memoization_tg  | 663 ms                                                   | 487 ms: 1.36x faster                                                      |
| async_tree_memoization     | 664 ms                                                   | 499 ms: 1.33x faster                                                      |
| deepcopy_memo              | 53.0 us                                                  | 41.0 us: 1.29x faster                                                     |
| async_tree_none            | 504 ms                                                   | 396 ms: 1.27x faster                                                      |
| async_tree_io_tg           | 1.16 sec                                                 | 922 ms: 1.26x faster                                                      |
| regex_effbot               | 5.10 ms                                                  | 4.05 ms: 1.26x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 391 ms: 1.24x faster                                                      |
| async_tree_io              | 1.14 sec                                                 | 925 ms: 1.23x faster                                                      |
| spectral_norm              | 143 ms                                                   | 119 ms: 1.20x faster                                                      |
| deepcopy_reduce            | 4.24 us                                                  | 3.56 us: 1.19x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 679 ms: 1.18x faster                                                      |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 686 ms: 1.15x faster                                                      |
| go                         | 164 ms                                                   | 144 ms: 1.14x faster                                                      |
| pylint                     | 345 ms                                                   | 303 ms: 1.14x faster                                                      |
| scimark_fft                | 463 ms                                                   | 415 ms: 1.11x faster                                                      |
| xml_etree_parse            | 203 ms                                                   | 183 ms: 1.11x faster                                                      |
| generators                 | 40.3 ms                                                  | 36.6 ms: 1.10x faster                                                     |
| float                      | 95.8 ms                                                  | 87.0 ms: 1.10x faster                                                     |
| async_generators           | 500 ms                                                   | 458 ms: 1.09x faster                                                      |
| bpe_tokeniser              | 6.02 sec                                                 | 5.54 sec: 1.09x faster                                                    |
| telco                      | 10.5 ms                                                  | 9.65 ms: 1.08x faster                                                     |
| thrift                     | 1.01 ms                                                  | 947 us: 1.07x faster                                                      |
| sqlalchemy_imperative      | 16.1 ms                                                  | 15.1 ms: 1.07x faster                                                     |
| scimark_sor                | 164 ms                                                   | 156 ms: 1.06x faster                                                      |
| tomli_loads                | 2.67 sec                                                 | 2.53 sec: 1.05x faster                                                    |
| k_core                     | 2.99 sec                                                 | 2.86 sec: 1.04x faster                                                    |
| pyflate                    | 582 ms                                                   | 562 ms: 1.04x faster                                                      |
| pycparser                  | 1.34 sec                                                 | 1.30 sec: 1.03x faster                                                    |
| sympy_str                  | 265 ms                                                   | 261 ms: 1.02x faster                                                      |
| mdp                        | 3.45 sec                                                 | 3.39 sec: 1.02x faster                                                    |
| docutils                   | 2.96 sec                                                 | 3.02 sec: 1.02x slower                                                    |
| python_startup_no_site     | 8.79 ms                                                  | 9.05 ms: 1.03x slower                                                     |
| create_gc_cycles           | 3.39 ms                                                  | 3.59 ms: 1.06x slower                                                     |
| json_loads                 | 32.8 us                                                  | 34.8 us: 1.06x slower                                                     |
| gc_traversal               | 5.92 ms                                                  | 6.76 ms: 1.14x slower                                                     |
| subparsers                 | 20.3 ms                                                  | 25.7 ms: 1.26x slower                                                     |
| many_optionals             | 626 us                                                   | 823 us: 1.31x slower                                                      |
| bench_mp_pool              | 8.07 ms                                                  | 3.99 sec: 494.85x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.03x slower                                                              |

Benchmark hidden because not significant (56): regex_compile, pathlib, scimark_monte_carlo, scimark_lu, genshi_text, sqlalchemy_declarative, sqlglot_optimize, sympy_sum, sqlglot_transpile, chaos, logging_format, sphinx, 2to3, scimark_sparse_mat_mult, coroutines, sqlglot_parse, bench_thread_pool, meteor_contest, sqlglot_normalize, deltablue, richards_super, asyncio_websockets, xml_etree_generate, pprint_pformat, nqueens, unpickle_pure_python, sympy_expand, regex_dna, coverage, connected_components, mako, hexiom, crypto_pyaes, sqlite_synth, html5lib, sympy_integrate, logging_simple, xml_etree_process, richards, shortest_path, pprint_safe_repr, fannkuch, regex_v8, xml_etree_iterparse, genshi_xml, typing_runtime_protocols, json, django_template, python_startup, comprehensions, raytrace, logging_silent, json_dumps, pidigits, nbody, pickle_pure_python
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20250210-3.14.0a4+-4603470/bm-20250210-arminc-aarch64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470.json: dulwich_log

- Geometric mean (including insignificant results): 1.037x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.03x