# Results vs. 3.13.0

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: linux-aarch64
- commit hash: 9b65402
- commit date: 2025-06-13
- overall geometric mean: 1.018x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 298 ms: 1.05x faster                                                              |
| html5lib       | 65.6 ms                                                  | 61.2 ms: 1.07x faster                                                             |
| sphinx         | 1.20 sec                                                 | 1.13 sec: 1.06x faster                                                            |
| Geometric mean | (ref)                                                    | 1.05x faster                                                                      |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 461 ms: 1.44x faster                                                              |
| async_tree_memoization     | 664 ms                                                   | 465 ms: 1.43x faster                                                              |
| async_tree_none_tg         | 484 ms                                                   | 374 ms: 1.30x faster                                                              |
| async_tree_io_tg           | 1.16 sec                                                 | 905 ms: 1.29x faster                                                              |
| async_tree_io              | 1.14 sec                                                 | 888 ms: 1.28x faster                                                              |
| async_tree_none            | 504 ms                                                   | 394 ms: 1.28x faster                                                              |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 654 ms: 1.23x faster                                                              |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 656 ms: 1.20x faster                                                              |
| async_generators           | 500 ms                                                   | 455 ms: 1.10x faster                                                              |
| Geometric mean             | (ref)                                                    | 1.22x faster                                                                      |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 85.5 ms: 1.12x faster                                                             |
| Geometric mean | (ref)                                                    | 1.03x faster                                                                      |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.93 ms: 1.30x faster                                                             |
| regex_dna      | 263 ms                                                   | 221 ms: 1.19x faster                                                              |
| regex_v8       | 32.5 ms                                                  | 27.4 ms: 1.19x faster                                                             |
| regex_compile  | 134 ms                                                   | 122 ms: 1.09x faster                                                              |
| Geometric mean | (ref)                                                    | 1.19x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|---------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 181 ms: 1.12x faster                                                              |
| xml_etree_iterparse | 159 ms                                                   | 143 ms: 1.11x faster                                                              |
| tomli_loads         | 2.67 sec                                                 | 2.47 sec: 1.08x faster                                                            |
| Geometric mean      | (ref)                                                    | 1.04x faster                                                                      |

Benchmark hidden because not significant (6): xml_etree_generate, xml_etree_process, unpickle_pure_python, json_loads, json_dumps, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup | 16.0 ms                                                  | 15.1 ms: 1.06x faster                                                             |
| Geometric mean | (ref)                                                    | 1.04x faster                                                                      |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_text    | 28.6 ms                                                  | 26.6 ms: 1.07x faster                                                             |
| Geometric mean | (ref)                                                    | 1.02x faster                                                                      |

Benchmark hidden because not significant (3): genshi_xml, django_template, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.68 sec: 2.05x faster                                                            |
| async_tree_memoization_tg  | 663 ms                                                   | 461 ms: 1.44x faster                                                              |
| deepcopy                   | 479 us                                                   | 334 us: 1.44x faster                                                              |
| async_tree_memoization     | 664 ms                                                   | 465 ms: 1.43x faster                                                              |
| deepcopy_memo              | 53.0 us                                                  | 38.6 us: 1.37x faster                                                             |
| regex_effbot               | 5.10 ms                                                  | 3.93 ms: 1.30x faster                                                             |
| async_tree_none_tg         | 484 ms                                                   | 374 ms: 1.30x faster                                                              |
| async_tree_io_tg           | 1.16 sec                                                 | 905 ms: 1.29x faster                                                              |
| async_tree_io              | 1.14 sec                                                 | 888 ms: 1.28x faster                                                              |
| async_tree_none            | 504 ms                                                   | 394 ms: 1.28x faster                                                              |
| go                         | 164 ms                                                   | 129 ms: 1.27x faster                                                              |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 654 ms: 1.23x faster                                                              |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 656 ms: 1.20x faster                                                              |
| regex_dna                  | 263 ms                                                   | 221 ms: 1.19x faster                                                              |
| regex_v8                   | 32.5 ms                                                  | 27.4 ms: 1.19x faster                                                             |
| deepcopy_reduce            | 4.24 us                                                  | 3.65 us: 1.16x faster                                                             |
| telco                      | 10.5 ms                                                  | 9.20 ms: 1.14x faster                                                             |
| scimark_sor                | 164 ms                                                   | 146 ms: 1.13x faster                                                              |
| pyflate                    | 582 ms                                                   | 516 ms: 1.13x faster                                                              |
| generators                 | 40.3 ms                                                  | 36.0 ms: 1.12x faster                                                             |
| float                      | 95.8 ms                                                  | 85.5 ms: 1.12x faster                                                             |
| xml_etree_parse            | 203 ms                                                   | 181 ms: 1.12x faster                                                              |
| xml_etree_iterparse        | 159 ms                                                   | 143 ms: 1.11x faster                                                              |
| pylint                     | 345 ms                                                   | 312 ms: 1.11x faster                                                              |
| bpe_tokeniser              | 6.02 sec                                                 | 5.44 sec: 1.11x faster                                                            |
| async_generators           | 500 ms                                                   | 455 ms: 1.10x faster                                                              |
| spectral_norm              | 143 ms                                                   | 130 ms: 1.10x faster                                                              |
| regex_compile              | 134 ms                                                   | 122 ms: 1.09x faster                                                              |
| scimark_monte_carlo        | 87.8 ms                                                  | 80.7 ms: 1.09x faster                                                             |
| hexiom                     | 7.34 ms                                                  | 6.76 ms: 1.09x faster                                                             |
| sympy_integrate            | 21.4 ms                                                  | 19.8 ms: 1.08x faster                                                             |
| tomli_loads                | 2.67 sec                                                 | 2.47 sec: 1.08x faster                                                            |
| chaos                      | 70.7 ms                                                  | 65.8 ms: 1.08x faster                                                             |
| pathlib                    | 24.3 ms                                                  | 22.6 ms: 1.08x faster                                                             |
| genshi_text                | 28.6 ms                                                  | 26.6 ms: 1.07x faster                                                             |
| html5lib                   | 65.6 ms                                                  | 61.2 ms: 1.07x faster                                                             |
| pycparser                  | 1.34 sec                                                 | 1.26 sec: 1.07x faster                                                            |
| nqueens                    | 105 ms                                                   | 98.1 ms: 1.07x faster                                                             |
| sqlite_synth               | 4.08 us                                                  | 3.82 us: 1.07x faster                                                             |
| sphinx                     | 1.20 sec                                                 | 1.13 sec: 1.06x faster                                                            |
| python_startup             | 16.0 ms                                                  | 15.1 ms: 1.06x faster                                                             |
| richards                   | 54.5 ms                                                  | 51.4 ms: 1.06x faster                                                             |
| meteor_contest             | 117 ms                                                   | 111 ms: 1.06x faster                                                              |
| scimark_fft                | 463 ms                                                   | 439 ms: 1.05x faster                                                              |
| k_core                     | 2.99 sec                                                 | 2.84 sec: 1.05x faster                                                            |
| 2to3                       | 313 ms                                                   | 298 ms: 1.05x faster                                                              |
| typing_runtime_protocols   | 197 us                                                   | 190 us: 1.04x faster                                                              |
| pprint_pformat             | 1.99 sec                                                 | 2.03 sec: 1.02x slower                                                            |
| connected_components       | 547 ms                                                   | 563 ms: 1.03x slower                                                              |
| pprint_safe_repr           | 962 ms                                                   | 994 ms: 1.03x slower                                                              |
| shortest_path              | 565 ms                                                   | 592 ms: 1.05x slower                                                              |
| raytrace                   | 310 ms                                                   | 326 ms: 1.05x slower                                                              |
| logging_simple             | 7.25 us                                                  | 7.71 us: 1.06x slower                                                             |
| create_gc_cycles           | 3.39 ms                                                  | 3.78 ms: 1.11x slower                                                             |
| gc_traversal               | 5.92 ms                                                  | 6.73 ms: 1.14x slower                                                             |
| many_optionals             | 626 us                                                   | 753 us: 1.20x slower                                                              |
| subparsers                 | 20.3 ms                                                  | 28.8 ms: 1.42x slower                                                             |
| logging_silent             | 135 ns                                                   | 620 ns: 4.61x slower                                                              |
| coverage                   | 106 ms                                                   | 556 ms: 5.26x slower                                                              |
| thrift                     | 1.01 ms                                                  | 197 ms: 194.94x slower                                                            |
| Geometric mean             | (ref)                                                    | 1.03x slower                                                                      |

Benchmark hidden because not significant (27): sympy_sum, xml_etree_generate, json, comprehensions, xml_etree_process, richards_super, sympy_expand, unpickle_pure_python, json_loads, pidigits, python_startup_no_site, crypto_pyaes, asyncio_websockets, docutils, genshi_xml, json_dumps, logging_format, django_template, mako, fannkuch, deltablue, sympy_str, coroutines, nbody, scimark_sparse_mat_mult, pickle_pure_python, scimark_lu
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250613-3.15.0a0-9b65402/bm-20250613-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.018x slower

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.07x