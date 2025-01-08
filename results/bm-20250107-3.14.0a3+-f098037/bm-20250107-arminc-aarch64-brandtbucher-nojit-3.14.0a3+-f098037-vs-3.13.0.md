# Results vs. 3.13.0

- fork: brandtbucher
- ref: nojit
- machine: linux-aarch64
- commit hash: f098037
- commit date: 2025-01-07
- overall geometric mean: 1.037x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.03 sec: 1.02x slower                                          |
| Geometric mean | (ref)                                                    | 1.01x faster                                                    |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 478 ms: 1.38x faster                                            |
| async_tree_memoization     | 664 ms                                                   | 490 ms: 1.36x faster                                            |
| async_tree_none            | 504 ms                                                   | 375 ms: 1.34x faster                                            |
| async_tree_io_tg           | 1.16 sec                                                 | 901 ms: 1.29x faster                                            |
| async_tree_io              | 1.14 sec                                                 | 890 ms: 1.28x faster                                            |
| async_tree_none_tg         | 484 ms                                                   | 382 ms: 1.27x faster                                            |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 667 ms: 1.20x faster                                            |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 672 ms: 1.17x faster                                            |
| Geometric mean             | (ref)                                                    | 1.20x faster                                                    |

Benchmark hidden because not significant (3): async_generators, coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 90.7 ms: 1.06x faster                                           |
| Geometric mean | (ref)                                                    | 1.01x slower                                                    |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.06 ms: 1.26x faster                                           |
| regex_dna      | 263 ms                                                   | 245 ms: 1.07x faster                                            |
| Geometric mean | (ref)                                                    | 1.09x faster                                                    |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|---------------------|:--------------------------------------------------------:|:---------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 180 ms: 1.12x faster                                            |
| xml_etree_iterparse | 159 ms                                                   | 143 ms: 1.11x faster                                            |
| tomli_loads         | 2.67 sec                                                 | 2.61 sec: 1.02x faster                                          |
| pickle_pure_python  | 374 us                                                   | 400 us: 1.07x slower                                            |
| Geometric mean      | (ref)                                                    | 1.02x faster                                                    |

Benchmark hidden because not significant (5): xml_etree_generate, json_loads, unpickle_pure_python, json_dumps, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 9.01 ms: 1.02x slower                                           |
| Geometric mean         | (ref)                                                    | 1.02x slower                                                    |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|-----------------|:--------------------------------------------------------:|:---------------------------------------------------------------:|
| django_template | 39.4 ms                                                  | 42.3 ms: 1.07x slower                                           |
| Geometric mean  | (ref)                                                    | 1.02x slower                                                    |

Benchmark hidden because not significant (3): genshi_text, genshi_xml, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------:|
| deepcopy                   | 479 us                                                   | 342 us: 1.40x faster                                            |
| async_tree_memoization_tg  | 663 ms                                                   | 478 ms: 1.38x faster                                            |
| async_tree_memoization     | 664 ms                                                   | 490 ms: 1.36x faster                                            |
| async_tree_none            | 504 ms                                                   | 375 ms: 1.34x faster                                            |
| async_tree_io_tg           | 1.16 sec                                                 | 901 ms: 1.29x faster                                            |
| deepcopy_memo              | 53.0 us                                                  | 41.2 us: 1.28x faster                                           |
| async_tree_io              | 1.14 sec                                                 | 890 ms: 1.28x faster                                            |
| async_tree_none_tg         | 484 ms                                                   | 382 ms: 1.27x faster                                            |
| regex_effbot               | 5.10 ms                                                  | 4.06 ms: 1.26x faster                                           |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 667 ms: 1.20x faster                                            |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 672 ms: 1.17x faster                                            |
| deepcopy_reduce            | 4.24 us                                                  | 3.67 us: 1.16x faster                                           |
| go                         | 164 ms                                                   | 144 ms: 1.14x faster                                            |
| pylint                     | 345 ms                                                   | 307 ms: 1.13x faster                                            |
| xml_etree_parse            | 203 ms                                                   | 180 ms: 1.12x faster                                            |
| pathlib                    | 24.3 ms                                                  | 21.7 ms: 1.12x faster                                           |
| xml_etree_iterparse        | 159 ms                                                   | 143 ms: 1.11x faster                                            |
| spectral_norm              | 143 ms                                                   | 130 ms: 1.11x faster                                            |
| generators                 | 40.3 ms                                                  | 36.9 ms: 1.09x faster                                           |
| json                       | 5.94 ms                                                  | 5.49 ms: 1.08x faster                                           |
| regex_dna                  | 263 ms                                                   | 245 ms: 1.07x faster                                            |
| scimark_fft                | 463 ms                                                   | 435 ms: 1.06x faster                                            |
| scimark_lu                 | 146 ms                                                   | 138 ms: 1.06x faster                                            |
| richards                   | 54.5 ms                                                  | 51.6 ms: 1.06x faster                                           |
| float                      | 95.8 ms                                                  | 90.7 ms: 1.06x faster                                           |
| coverage                   | 106 ms                                                   | 100 ms: 1.05x faster                                            |
| richards_super             | 60.8 ms                                                  | 58.1 ms: 1.05x faster                                           |
| bpe_tokeniser              | 6.02 sec                                                 | 5.76 sec: 1.05x faster                                          |
| pycparser                  | 1.34 sec                                                 | 1.29 sec: 1.04x faster                                          |
| k_core                     | 2.99 sec                                                 | 2.90 sec: 1.03x faster                                          |
| tomli_loads                | 2.67 sec                                                 | 2.61 sec: 1.02x faster                                          |
| docutils                   | 2.96 sec                                                 | 3.03 sec: 1.02x slower                                          |
| python_startup_no_site     | 8.79 ms                                                  | 9.01 ms: 1.02x slower                                           |
| sympy_str                  | 265 ms                                                   | 272 ms: 1.03x slower                                            |
| raytrace                   | 310 ms                                                   | 329 ms: 1.06x slower                                            |
| pickle_pure_python         | 374 us                                                   | 400 us: 1.07x slower                                            |
| django_template            | 39.4 ms                                                  | 42.3 ms: 1.07x slower                                           |
| create_gc_cycles           | 3.39 ms                                                  | 3.71 ms: 1.09x slower                                           |
| many_optionals             | 626 us                                                   | 713 us: 1.14x slower                                            |
| gc_traversal               | 5.92 ms                                                  | 6.91 ms: 1.17x slower                                           |
| subparsers                 | 20.3 ms                                                  | 25.7 ms: 1.26x slower                                           |
| bench_mp_pool              | 8.07 ms                                                  | 3.47 sec: 430.05x slower                                        |
| Geometric mean             | (ref)                                                    | 1.03x slower                                                    |

Benchmark hidden because not significant (53): sympy_sum, telco, sqlglot_optimize, thrift, regex_compile, scimark_sor, scimark_monte_carlo, bench_thread_pool, xml_etree_generate, sqlglot_transpile, pyflate, sqlalchemy_declarative, sphinx, 2to3, genshi_text, async_generators, meteor_contest, mdp, sqlalchemy_imperative, html5lib, json_loads, logging_simple, coroutines, connected_components, pprint_safe_repr, deltablue, pprint_pformat, fannkuch, scimark_sparse_mat_mult, nqueens, sympy_expand, hexiom, sqlglot_normalize, asyncio_websockets, regex_v8, chaos, unpickle_pure_python, python_startup, shortest_path, logging_format, json_dumps, sqlglot_parse, crypto_pyaes, comprehensions, genshi_xml, mako, sympy_integrate, typing_runtime_protocols, pidigits, logging_silent, xml_etree_process, sqlite_synth, nbody
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (2) of results/bm-20250107-3.14.0a3+-f098037/bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037.json: dulwich_log, mypy2

- Geometric mean (including insignificant results): 1.037x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x