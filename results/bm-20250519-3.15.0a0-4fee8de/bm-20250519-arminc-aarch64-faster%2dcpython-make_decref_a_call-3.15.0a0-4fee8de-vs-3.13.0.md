# Results vs. 3.13.0

- fork: faster-cpython
- ref: make_decref_a_call
- machine: linux-aarch64
- commit hash: 4fee8de
- commit date: 2025-05-19
- overall geometric mean: 1.027x faster
- HPT reliability: 94.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.01 sec: 1.01x slower                                                          |
| html5lib       | 65.6 ms                                                  | 63.7 ms: 1.03x faster                                                           |
| Geometric mean | (ref)                                                    | 1.00x faster                                                                    |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 471 ms: 1.41x faster                                                            |
| async_tree_memoization     | 664 ms                                                   | 473 ms: 1.40x faster                                                            |
| async_tree_none_tg         | 484 ms                                                   | 383 ms: 1.26x faster                                                            |
| async_tree_none            | 504 ms                                                   | 399 ms: 1.26x faster                                                            |
| async_tree_io              | 1.14 sec                                                 | 907 ms: 1.26x faster                                                            |
| async_tree_io_tg           | 1.16 sec                                                 | 938 ms: 1.24x faster                                                            |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 661 ms: 1.21x faster                                                            |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 668 ms: 1.18x faster                                                            |
| async_generators           | 500 ms                                                   | 480 ms: 1.04x faster                                                            |
| Geometric mean             | (ref)                                                    | 1.19x faster                                                                    |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 88.0 ms: 1.09x faster                                                           |
| Geometric mean | (ref)                                                    | 1.02x faster                                                                    |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.81 ms: 1.34x faster                                                           |
| regex_v8       | 32.5 ms                                                  | 28.2 ms: 1.15x faster                                                           |
| regex_dna      | 263 ms                                                   | 232 ms: 1.13x faster                                                            |
| Geometric mean | (ref)                                                    | 1.16x faster                                                                    |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|---------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 191 ms: 1.06x faster                                                            |
| xml_etree_iterparse | 159 ms                                                   | 152 ms: 1.05x faster                                                            |
| tomli_loads         | 2.67 sec                                                 | 2.56 sec: 1.04x faster                                                          |
| json_loads          | 32.8 us                                                  | 36.0 us: 1.10x slower                                                           |
| pickle_pure_python  | 374 us                                                   | 418 us: 1.12x slower                                                            |
| Geometric mean      | (ref)                                                    | 1.00x slower                                                                    |

Benchmark hidden because not significant (4): json_dumps, xml_etree_generate, xml_etree_process, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup | 16.0 ms                                                  | 15.2 ms: 1.05x faster                                                           |
| Geometric mean | (ref)                                                    | 1.03x faster                                                                    |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|-----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 61.6 ms                                                  | 63.1 ms: 1.02x slower                                                           |
| mako            | 14.0 ms                                                  | 14.5 ms: 1.04x slower                                                           |
| django_template | 39.4 ms                                                  | 42.5 ms: 1.08x slower                                                           |
| Geometric mean  | (ref)                                                    | 1.03x slower                                                                    |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.73 sec: 2.00x faster                                                          |
| async_tree_memoization_tg  | 663 ms                                                   | 471 ms: 1.41x faster                                                            |
| async_tree_memoization     | 664 ms                                                   | 473 ms: 1.40x faster                                                            |
| deepcopy                   | 479 us                                                   | 342 us: 1.40x faster                                                            |
| deepcopy_memo              | 53.0 us                                                  | 39.1 us: 1.36x faster                                                           |
| regex_effbot               | 5.10 ms                                                  | 3.81 ms: 1.34x faster                                                           |
| async_tree_none_tg         | 484 ms                                                   | 383 ms: 1.26x faster                                                            |
| async_tree_none            | 504 ms                                                   | 399 ms: 1.26x faster                                                            |
| go                         | 164 ms                                                   | 130 ms: 1.26x faster                                                            |
| async_tree_io              | 1.14 sec                                                 | 907 ms: 1.26x faster                                                            |
| async_tree_io_tg           | 1.16 sec                                                 | 938 ms: 1.24x faster                                                            |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 661 ms: 1.21x faster                                                            |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 668 ms: 1.18x faster                                                            |
| regex_v8                   | 32.5 ms                                                  | 28.2 ms: 1.15x faster                                                           |
| deepcopy_reduce            | 4.24 us                                                  | 3.69 us: 1.15x faster                                                           |
| regex_dna                  | 263 ms                                                   | 232 ms: 1.13x faster                                                            |
| pylint                     | 345 ms                                                   | 315 ms: 1.10x faster                                                            |
| spectral_norm              | 143 ms                                                   | 131 ms: 1.09x faster                                                            |
| generators                 | 40.3 ms                                                  | 36.9 ms: 1.09x faster                                                           |
| float                      | 95.8 ms                                                  | 88.0 ms: 1.09x faster                                                           |
| scimark_sor                | 164 ms                                                   | 152 ms: 1.08x faster                                                            |
| xml_etree_parse            | 203 ms                                                   | 191 ms: 1.06x faster                                                            |
| pathlib                    | 24.3 ms                                                  | 23.0 ms: 1.06x faster                                                           |
| k_core                     | 2.99 sec                                                 | 2.83 sec: 1.06x faster                                                          |
| python_startup             | 16.0 ms                                                  | 15.2 ms: 1.05x faster                                                           |
| telco                      | 10.5 ms                                                  | 9.94 ms: 1.05x faster                                                           |
| richards                   | 54.5 ms                                                  | 51.9 ms: 1.05x faster                                                           |
| bpe_tokeniser              | 6.02 sec                                                 | 5.74 sec: 1.05x faster                                                          |
| xml_etree_iterparse        | 159 ms                                                   | 152 ms: 1.05x faster                                                            |
| async_generators           | 500 ms                                                   | 480 ms: 1.04x faster                                                            |
| pycparser                  | 1.34 sec                                                 | 1.29 sec: 1.04x faster                                                          |
| tomli_loads                | 2.67 sec                                                 | 2.56 sec: 1.04x faster                                                          |
| pyflate                    | 582 ms                                                   | 560 ms: 1.04x faster                                                            |
| scimark_fft                | 463 ms                                                   | 446 ms: 1.04x faster                                                            |
| sqlite_synth               | 4.08 us                                                  | 3.94 us: 1.04x faster                                                           |
| html5lib                   | 65.6 ms                                                  | 63.7 ms: 1.03x faster                                                           |
| pprint_pformat             | 1.99 sec                                                 | 1.93 sec: 1.03x faster                                                          |
| djangocms                  | 66.2 us                                                  | 65.0 us: 1.02x faster                                                           |
| docutils                   | 2.96 sec                                                 | 3.01 sec: 1.01x slower                                                          |
| genshi_xml                 | 61.6 ms                                                  | 63.1 ms: 1.02x slower                                                           |
| connected_components       | 547 ms                                                   | 561 ms: 1.03x slower                                                            |
| sympy_expand               | 472 ms                                                   | 489 ms: 1.04x slower                                                            |
| mako                       | 14.0 ms                                                  | 14.5 ms: 1.04x slower                                                           |
| crypto_pyaes               | 84.9 ms                                                  | 88.0 ms: 1.04x slower                                                           |
| sympy_str                  | 265 ms                                                   | 276 ms: 1.04x slower                                                            |
| shortest_path              | 565 ms                                                   | 590 ms: 1.04x slower                                                            |
| json                       | 5.94 ms                                                  | 6.22 ms: 1.05x slower                                                           |
| typing_runtime_protocols   | 197 us                                                   | 209 us: 1.06x slower                                                            |
| fannkuch                   | 478 ms                                                   | 510 ms: 1.07x slower                                                            |
| coverage                   | 106 ms                                                   | 113 ms: 1.07x slower                                                            |
| scimark_lu                 | 146 ms                                                   | 157 ms: 1.08x slower                                                            |
| django_template            | 39.4 ms                                                  | 42.5 ms: 1.08x slower                                                           |
| comprehensions             | 20.8 us                                                  | 22.5 us: 1.08x slower                                                           |
| logging_format             | 8.10 us                                                  | 8.79 us: 1.09x slower                                                           |
| logging_simple             | 7.25 us                                                  | 7.88 us: 1.09x slower                                                           |
| raytrace                   | 310 ms                                                   | 340 ms: 1.10x slower                                                            |
| json_loads                 | 32.8 us                                                  | 36.0 us: 1.10x slower                                                           |
| pickle_pure_python         | 374 us                                                   | 418 us: 1.12x slower                                                            |
| create_gc_cycles           | 3.39 ms                                                  | 3.80 ms: 1.12x slower                                                           |
| gc_traversal               | 5.92 ms                                                  | 6.92 ms: 1.17x slower                                                           |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 7.86 ms: 1.18x slower                                                           |
| many_optionals             | 626 us                                                   | 873 us: 1.39x slower                                                            |
| subparsers                 | 20.3 ms                                                  | 29.2 ms: 1.44x slower                                                           |
| logging_silent             | 135 ns                                                   | 629 ns: 4.67x slower                                                            |
| bench_mp_pool              | 8.07 ms                                                  | 4.80 sec: 595.31x slower                                                        |
| Geometric mean             | (ref)                                                    | 1.05x slower                                                                    |

Benchmark hidden because not significant (25): regex_compile, sympy_integrate, scimark_monte_carlo, deltablue, json_dumps, richards_super, hexiom, xml_etree_generate, pprint_safe_repr, sphinx, python_startup_no_site, asyncio_websockets, genshi_text, pidigits, nqueens, thrift, xml_etree_process, unpickle_pure_python, sympy_sum, chaos, 2to3, nbody, bench_thread_pool, meteor_contest, coroutines
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250519-3.15.0a0-4fee8de/bm-20250519-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.027x faster

# HPT report

- Reliability score: 94.98% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x