# Results vs. 3.13.0

- fork: faster-cpython
- ref: c_recursion_limit
- machine: linux-aarch64
- commit hash: 21366c3
- commit date: 2025-02-17
- overall geometric mean: 1.033x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250217-arminc-aarch64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.03 sec: 1.02x slower                                                          |
| Geometric mean | (ref)                                                    | 1.01x faster                                                                    |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250217-arminc-aarch64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 499 ms: 1.33x faster                                                            |
| async_tree_memoization     | 664 ms                                                   | 504 ms: 1.32x faster                                                            |
| async_tree_none            | 504 ms                                                   | 403 ms: 1.25x faster                                                            |
| async_tree_io_tg           | 1.16 sec                                                 | 948 ms: 1.23x faster                                                            |
| async_tree_io              | 1.14 sec                                                 | 936 ms: 1.22x faster                                                            |
| async_tree_none_tg         | 484 ms                                                   | 403 ms: 1.20x faster                                                            |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 682 ms: 1.17x faster                                                            |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 690 ms: 1.14x faster                                                            |
| async_generators           | 500 ms                                                   | 458 ms: 1.09x faster                                                            |
| Geometric mean             | (ref)                                                    | 1.17x faster                                                                    |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250217-arminc-aarch64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 86.2 ms: 1.11x faster                                                           |
| Geometric mean | (ref)                                                    | 1.03x faster                                                                    |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250217-arminc-aarch64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.09 ms: 1.25x faster                                                           |
| regex_dna      | 263 ms                                                   | 244 ms: 1.08x faster                                                            |
| regex_compile  | 134 ms                                                   | 125 ms: 1.07x faster                                                            |
| Geometric mean | (ref)                                                    | 1.10x faster                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250217-arminc-aarch64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|---------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 190 ms: 1.06x faster                                                            |
| xml_etree_iterparse | 159 ms                                                   | 149 ms: 1.06x faster                                                            |
| tomli_loads         | 2.67 sec                                                 | 2.58 sec: 1.03x faster                                                          |
| Geometric mean      | (ref)                                                    | 1.00x slower                                                                    |

Benchmark hidden because not significant (6): xml_etree_generate, xml_etree_process, unpickle_pure_python, pickle_pure_python, json_loads, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250217-arminc-aarch64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 9.12 ms: 1.04x slower                                                           |
| Geometric mean         | (ref)                                                    | 1.03x slower                                                                    |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250217-arminc-aarch64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text    | 28.6 ms                                                  | 26.9 ms: 1.06x faster                                                           |
| Geometric mean | (ref)                                                    | 1.00x slower                                                                    |

Benchmark hidden because not significant (3): mako, genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250217-arminc-aarch64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                   | 479 us                                                   | 346 us: 1.38x faster                                                            |
| async_tree_memoization_tg  | 663 ms                                                   | 499 ms: 1.33x faster                                                            |
| async_tree_memoization     | 664 ms                                                   | 504 ms: 1.32x faster                                                            |
| deepcopy_memo              | 53.0 us                                                  | 40.5 us: 1.31x faster                                                           |
| async_tree_none            | 504 ms                                                   | 403 ms: 1.25x faster                                                            |
| regex_effbot               | 5.10 ms                                                  | 4.09 ms: 1.25x faster                                                           |
| async_tree_io_tg           | 1.16 sec                                                 | 948 ms: 1.23x faster                                                            |
| async_tree_io              | 1.14 sec                                                 | 936 ms: 1.22x faster                                                            |
| async_tree_none_tg         | 484 ms                                                   | 403 ms: 1.20x faster                                                            |
| spectral_norm              | 143 ms                                                   | 121 ms: 1.19x faster                                                            |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 682 ms: 1.17x faster                                                            |
| deepcopy_reduce            | 4.24 us                                                  | 3.66 us: 1.16x faster                                                           |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 690 ms: 1.14x faster                                                            |
| go                         | 164 ms                                                   | 146 ms: 1.12x faster                                                            |
| float                      | 95.8 ms                                                  | 86.2 ms: 1.11x faster                                                           |
| generators                 | 40.3 ms                                                  | 36.3 ms: 1.11x faster                                                           |
| async_generators           | 500 ms                                                   | 458 ms: 1.09x faster                                                            |
| scimark_fft                | 463 ms                                                   | 426 ms: 1.09x faster                                                            |
| pathlib                    | 24.3 ms                                                  | 22.5 ms: 1.08x faster                                                           |
| regex_dna                  | 263 ms                                                   | 244 ms: 1.08x faster                                                            |
| regex_compile              | 134 ms                                                   | 125 ms: 1.07x faster                                                            |
| xml_etree_parse            | 203 ms                                                   | 190 ms: 1.06x faster                                                            |
| xml_etree_iterparse        | 159 ms                                                   | 149 ms: 1.06x faster                                                            |
| genshi_text                | 28.6 ms                                                  | 26.9 ms: 1.06x faster                                                           |
| bpe_tokeniser              | 6.02 sec                                                 | 5.67 sec: 1.06x faster                                                          |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 6.30 ms: 1.06x faster                                                           |
| tomli_loads                | 2.67 sec                                                 | 2.58 sec: 1.03x faster                                                          |
| pycparser                  | 1.34 sec                                                 | 1.30 sec: 1.03x faster                                                          |
| k_core                     | 2.99 sec                                                 | 2.91 sec: 1.03x faster                                                          |
| docutils                   | 2.96 sec                                                 | 3.03 sec: 1.02x slower                                                          |
| python_startup_no_site     | 8.79 ms                                                  | 9.12 ms: 1.04x slower                                                           |
| create_gc_cycles           | 3.39 ms                                                  | 3.57 ms: 1.05x slower                                                           |
| raytrace                   | 310 ms                                                   | 328 ms: 1.06x slower                                                            |
| sympy_str                  | 265 ms                                                   | 281 ms: 1.06x slower                                                            |
| gc_traversal               | 5.92 ms                                                  | 6.89 ms: 1.16x slower                                                           |
| subparsers                 | 20.3 ms                                                  | 26.0 ms: 1.28x slower                                                           |
| many_optionals             | 626 us                                                   | 861 us: 1.37x slower                                                            |
| bench_mp_pool              | 8.07 ms                                                  | 7.19 sec: 890.95x slower                                                        |
| Geometric mean             | (ref)                                                    | 1.04x slower                                                                    |

Benchmark hidden because not significant (57): pylint, scimark_sor, sqlalchemy_imperative, chaos, logging_format, telco, richards, bench_thread_pool, sympy_sum, pyflate, thrift, sqlalchemy_declarative, html5lib, sqlglot_optimize, scimark_monte_carlo, meteor_contest, sphinx, coverage, coroutines, regex_v8, connected_components, scimark_lu, mako, 2to3, shortest_path, nqueens, logging_simple, deltablue, richards_super, sqlglot_normalize, asyncio_websockets, sqlglot_transpile, xml_etree_generate, mdp, pidigits, sqlite_synth, sqlglot_parse, pprint_pformat, xml_etree_process, sympy_expand, nbody, pprint_safe_repr, unpickle_pure_python, json, sympy_integrate, genshi_xml, python_startup, typing_runtime_protocols, comprehensions, hexiom, fannkuch, pickle_pure_python, django_template, crypto_pyaes, json_loads, json_dumps, logging_silent
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20250217-3.14.0a5+-21366c3/bm-20250217-arminc-aarch64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3.json: dulwich_log

- Geometric mean (including insignificant results): 1.033x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.03x