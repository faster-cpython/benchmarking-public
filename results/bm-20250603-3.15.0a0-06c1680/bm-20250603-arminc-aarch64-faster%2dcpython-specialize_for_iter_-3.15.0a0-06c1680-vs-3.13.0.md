# Results vs. 3.13.0

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: linux-aarch64
- commit hash: 06c1680
- commit date: 2025-06-03
- overall geometric mean: 1.022x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 2.92 sec: 1.01x faster                                                            |
| html5lib       | 65.6 ms                                                  | 61.2 ms: 1.07x faster                                                             |
| sphinx         | 1.20 sec                                                 | 1.14 sec: 1.06x faster                                                            |
| Geometric mean | (ref)                                                    | 1.04x faster                                                                      |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 462 ms: 1.43x faster                                                              |
| async_tree_memoization     | 664 ms                                                   | 463 ms: 1.43x faster                                                              |
| async_tree_none_tg         | 484 ms                                                   | 373 ms: 1.30x faster                                                              |
| async_tree_io              | 1.14 sec                                                 | 877 ms: 1.30x faster                                                              |
| async_tree_none            | 504 ms                                                   | 390 ms: 1.29x faster                                                              |
| async_tree_io_tg           | 1.16 sec                                                 | 910 ms: 1.28x faster                                                              |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 645 ms: 1.24x faster                                                              |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 659 ms: 1.20x faster                                                              |
| async_generators           | 500 ms                                                   | 455 ms: 1.10x faster                                                              |
| Geometric mean             | (ref)                                                    | 1.23x faster                                                                      |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 86.0 ms: 1.11x faster                                                             |
| Geometric mean | (ref)                                                    | 1.02x faster                                                                      |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.92 ms: 1.30x faster                                                             |
| regex_v8       | 32.5 ms                                                  | 27.8 ms: 1.17x faster                                                             |
| regex_dna      | 263 ms                                                   | 229 ms: 1.15x faster                                                              |
| regex_compile  | 134 ms                                                   | 123 ms: 1.09x faster                                                              |
| Geometric mean | (ref)                                                    | 1.17x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|---------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 180 ms: 1.13x faster                                                              |
| xml_etree_iterparse | 159 ms                                                   | 141 ms: 1.13x faster                                                              |
| tomli_loads         | 2.67 sec                                                 | 2.46 sec: 1.09x faster                                                            |
| Geometric mean      | (ref)                                                    | 1.04x faster                                                                      |

Benchmark hidden because not significant (6): json_dumps, xml_etree_process, xml_etree_generate, json_loads, unpickle_pure_python, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 15.0 ms: 1.07x faster                                                             |
| python_startup_no_site | 8.79 ms                                                  | 8.59 ms: 1.02x faster                                                             |
| Geometric mean         | (ref)                                                    | 1.05x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml     | 61.6 ms                                                  | 61.0 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                    | 1.01x faster                                                                      |

Benchmark hidden because not significant (3): genshi_text, mako, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.65 sec: 2.09x faster                                                            |
| deepcopy                   | 479 us                                                   | 328 us: 1.46x faster                                                              |
| async_tree_memoization_tg  | 663 ms                                                   | 462 ms: 1.43x faster                                                              |
| async_tree_memoization     | 664 ms                                                   | 463 ms: 1.43x faster                                                              |
| deepcopy_memo              | 53.0 us                                                  | 38.2 us: 1.39x faster                                                             |
| regex_effbot               | 5.10 ms                                                  | 3.92 ms: 1.30x faster                                                             |
| async_tree_none_tg         | 484 ms                                                   | 373 ms: 1.30x faster                                                              |
| async_tree_io              | 1.14 sec                                                 | 877 ms: 1.30x faster                                                              |
| go                         | 164 ms                                                   | 127 ms: 1.30x faster                                                              |
| async_tree_none            | 504 ms                                                   | 390 ms: 1.29x faster                                                              |
| async_tree_io_tg           | 1.16 sec                                                 | 910 ms: 1.28x faster                                                              |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 645 ms: 1.24x faster                                                              |
| deepcopy_reduce            | 4.24 us                                                  | 3.52 us: 1.20x faster                                                             |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 659 ms: 1.20x faster                                                              |
| regex_v8                   | 32.5 ms                                                  | 27.8 ms: 1.17x faster                                                             |
| regex_dna                  | 263 ms                                                   | 229 ms: 1.15x faster                                                              |
| xml_etree_parse            | 203 ms                                                   | 180 ms: 1.13x faster                                                              |
| xml_etree_iterparse        | 159 ms                                                   | 141 ms: 1.13x faster                                                              |
| generators                 | 40.3 ms                                                  | 35.8 ms: 1.13x faster                                                             |
| scimark_sor                | 164 ms                                                   | 146 ms: 1.13x faster                                                              |
| float                      | 95.8 ms                                                  | 86.0 ms: 1.11x faster                                                             |
| scimark_monte_carlo        | 87.8 ms                                                  | 79.0 ms: 1.11x faster                                                             |
| pyflate                    | 582 ms                                                   | 526 ms: 1.11x faster                                                              |
| pylint                     | 345 ms                                                   | 313 ms: 1.11x faster                                                              |
| telco                      | 10.5 ms                                                  | 9.47 ms: 1.10x faster                                                             |
| bpe_tokeniser              | 6.02 sec                                                 | 5.45 sec: 1.10x faster                                                            |
| async_generators           | 500 ms                                                   | 455 ms: 1.10x faster                                                              |
| pathlib                    | 24.3 ms                                                  | 22.3 ms: 1.09x faster                                                             |
| spectral_norm              | 143 ms                                                   | 132 ms: 1.09x faster                                                              |
| regex_compile              | 134 ms                                                   | 123 ms: 1.09x faster                                                              |
| tomli_loads                | 2.67 sec                                                 | 2.46 sec: 1.09x faster                                                            |
| pycparser                  | 1.34 sec                                                 | 1.24 sec: 1.09x faster                                                            |
| nqueens                    | 105 ms                                                   | 97.2 ms: 1.08x faster                                                             |
| hexiom                     | 7.34 ms                                                  | 6.84 ms: 1.07x faster                                                             |
| html5lib                   | 65.6 ms                                                  | 61.2 ms: 1.07x faster                                                             |
| python_startup             | 16.0 ms                                                  | 15.0 ms: 1.07x faster                                                             |
| sqlite_synth               | 4.08 us                                                  | 3.83 us: 1.07x faster                                                             |
| scimark_fft                | 463 ms                                                   | 435 ms: 1.06x faster                                                              |
| k_core                     | 2.99 sec                                                 | 2.82 sec: 1.06x faster                                                            |
| sympy_integrate            | 21.4 ms                                                  | 20.3 ms: 1.06x faster                                                             |
| sphinx                     | 1.20 sec                                                 | 1.14 sec: 1.06x faster                                                            |
| richards                   | 54.5 ms                                                  | 51.7 ms: 1.05x faster                                                             |
| meteor_contest             | 117 ms                                                   | 113 ms: 1.04x faster                                                              |
| python_startup_no_site     | 8.79 ms                                                  | 8.59 ms: 1.02x faster                                                             |
| docutils                   | 2.96 sec                                                 | 2.92 sec: 1.01x faster                                                            |
| genshi_xml                 | 61.6 ms                                                  | 61.0 ms: 1.01x faster                                                             |
| shortest_path              | 565 ms                                                   | 577 ms: 1.02x slower                                                              |
| pprint_safe_repr           | 962 ms                                                   | 983 ms: 1.02x slower                                                              |
| connected_components       | 547 ms                                                   | 559 ms: 1.02x slower                                                              |
| sympy_str                  | 265 ms                                                   | 277 ms: 1.04x slower                                                              |
| logging_simple             | 7.25 us                                                  | 7.59 us: 1.05x slower                                                             |
| raytrace                   | 310 ms                                                   | 327 ms: 1.05x slower                                                              |
| create_gc_cycles           | 3.39 ms                                                  | 3.74 ms: 1.10x slower                                                             |
| gc_traversal               | 5.92 ms                                                  | 6.84 ms: 1.16x slower                                                             |
| many_optionals             | 626 us                                                   | 894 us: 1.43x slower                                                              |
| subparsers                 | 20.3 ms                                                  | 29.1 ms: 1.43x slower                                                             |
| logging_silent             | 135 ns                                                   | 634 ns: 4.71x slower                                                              |
| coverage                   | 106 ms                                                   | 568 ms: 5.38x slower                                                              |
| thrift                     | 1.01 ms                                                  | 191 ms: 188.76x slower                                                            |
| Geometric mean             | (ref)                                                    | 1.03x slower                                                                      |

Benchmark hidden because not significant (28): sympy_sum, json_dumps, 2to3, genshi_text, xml_etree_process, json, crypto_pyaes, chaos, xml_etree_generate, richards_super, fannkuch, sympy_expand, asyncio_websockets, deltablue, comprehensions, json_loads, unpickle_pure_python, mako, pidigits, django_template, pprint_pformat, coroutines, logging_format, typing_runtime_protocols, scimark_lu, scimark_sparse_mat_mult, nbody, pickle_pure_python
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250603-3.15.0a0-06c1680/bm-20250603-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.022x slower

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.06x