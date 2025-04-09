# Results vs. 3.13.0

- fork: faster-cpython
- ref: trashcan_in_dealloc
- machine: linux-aarch64
- commit hash: 8aa20f2
- commit date: 2025-04-09
- overall geometric mean: 1.058x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 297 ms: 1.05x faster                                                              |
| html5lib       | 65.6 ms                                                  | 63.0 ms: 1.04x faster                                                             |
| sphinx         | 1.20 sec                                                 | 1.16 sec: 1.04x faster                                                            |
| Geometric mean | (ref)                                                    | 1.04x faster                                                                      |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization     | 664 ms                                                   | 458 ms: 1.45x faster                                                              |
| async_tree_memoization_tg  | 663 ms                                                   | 459 ms: 1.44x faster                                                              |
| async_tree_io_tg           | 1.16 sec                                                 | 879 ms: 1.32x faster                                                              |
| async_tree_none_tg         | 484 ms                                                   | 371 ms: 1.31x faster                                                              |
| async_tree_io              | 1.14 sec                                                 | 873 ms: 1.30x faster                                                              |
| async_tree_none            | 504 ms                                                   | 386 ms: 1.30x faster                                                              |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 648 ms: 1.24x faster                                                              |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 658 ms: 1.20x faster                                                              |
| async_generators           | 500 ms                                                   | 462 ms: 1.08x faster                                                              |
| Geometric mean             | (ref)                                                    | 1.23x faster                                                                      |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 86.0 ms: 1.11x faster                                                             |
| Geometric mean | (ref)                                                    | 1.04x faster                                                                      |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.99 ms: 1.28x faster                                                             |
| regex_v8       | 32.5 ms                                                  | 27.8 ms: 1.17x faster                                                             |
| regex_dna      | 263 ms                                                   | 242 ms: 1.08x faster                                                              |
| regex_compile  | 134 ms                                                   | 124 ms: 1.08x faster                                                              |
| Geometric mean | (ref)                                                    | 1.15x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|---------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 175 ms: 1.16x faster                                                              |
| xml_etree_iterparse | 159 ms                                                   | 140 ms: 1.13x faster                                                              |
| tomli_loads         | 2.67 sec                                                 | 2.48 sec: 1.08x faster                                                            |
| xml_etree_generate  | 118 ms                                                   | 112 ms: 1.06x faster                                                              |
| xml_etree_process   | 82.1 ms                                                  | 79.2 ms: 1.04x faster                                                             |
| json_loads          | 32.8 us                                                  | 34.8 us: 1.06x slower                                                             |
| Geometric mean      | (ref)                                                    | 1.04x faster                                                                      |

Benchmark hidden because not significant (3): unpickle_pure_python, json_dumps, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 10.2 ms: 1.16x slower                                                             |
| Geometric mean         | (ref)                                                    | 1.08x slower                                                                      |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_text, genshi_xml, mako, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.64 sec: 2.10x faster                                                            |
| async_tree_memoization     | 664 ms                                                   | 458 ms: 1.45x faster                                                              |
| async_tree_memoization_tg  | 663 ms                                                   | 459 ms: 1.44x faster                                                              |
| deepcopy                   | 479 us                                                   | 333 us: 1.44x faster                                                              |
| deepcopy_memo              | 53.0 us                                                  | 37.9 us: 1.40x faster                                                             |
| async_tree_io_tg           | 1.16 sec                                                 | 879 ms: 1.32x faster                                                              |
| async_tree_none_tg         | 484 ms                                                   | 371 ms: 1.31x faster                                                              |
| async_tree_io              | 1.14 sec                                                 | 873 ms: 1.30x faster                                                              |
| async_tree_none            | 504 ms                                                   | 386 ms: 1.30x faster                                                              |
| regex_effbot               | 5.10 ms                                                  | 3.99 ms: 1.28x faster                                                             |
| go                         | 164 ms                                                   | 131 ms: 1.25x faster                                                              |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 648 ms: 1.24x faster                                                              |
| deepcopy_reduce            | 4.24 us                                                  | 3.50 us: 1.21x faster                                                             |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 658 ms: 1.20x faster                                                              |
| regex_v8                   | 32.5 ms                                                  | 27.8 ms: 1.17x faster                                                             |
| xml_etree_parse            | 203 ms                                                   | 175 ms: 1.16x faster                                                              |
| xml_etree_iterparse        | 159 ms                                                   | 140 ms: 1.13x faster                                                              |
| pylint                     | 345 ms                                                   | 309 ms: 1.12x faster                                                              |
| float                      | 95.8 ms                                                  | 86.0 ms: 1.11x faster                                                             |
| spectral_norm              | 143 ms                                                   | 129 ms: 1.11x faster                                                              |
| scimark_sor                | 164 ms                                                   | 148 ms: 1.11x faster                                                              |
| telco                      | 10.5 ms                                                  | 9.55 ms: 1.10x faster                                                             |
| pathlib                    | 24.3 ms                                                  | 22.3 ms: 1.09x faster                                                             |
| pycparser                  | 1.34 sec                                                 | 1.24 sec: 1.09x faster                                                            |
| regex_dna                  | 263 ms                                                   | 242 ms: 1.08x faster                                                              |
| async_generators           | 500 ms                                                   | 462 ms: 1.08x faster                                                              |
| regex_compile              | 134 ms                                                   | 124 ms: 1.08x faster                                                              |
| tomli_loads                | 2.67 sec                                                 | 2.48 sec: 1.08x faster                                                            |
| bpe_tokeniser              | 6.02 sec                                                 | 5.62 sec: 1.07x faster                                                            |
| pyflate                    | 582 ms                                                   | 546 ms: 1.06x faster                                                              |
| k_core                     | 2.99 sec                                                 | 2.82 sec: 1.06x faster                                                            |
| scimark_fft                | 463 ms                                                   | 437 ms: 1.06x faster                                                              |
| xml_etree_generate         | 118 ms                                                   | 112 ms: 1.06x faster                                                              |
| 2to3                       | 313 ms                                                   | 297 ms: 1.05x faster                                                              |
| sqlite_synth               | 4.08 us                                                  | 3.87 us: 1.05x faster                                                             |
| sympy_integrate            | 21.4 ms                                                  | 20.4 ms: 1.05x faster                                                             |
| meteor_contest             | 117 ms                                                   | 112 ms: 1.05x faster                                                              |
| richards_super             | 60.8 ms                                                  | 58.1 ms: 1.05x faster                                                             |
| richards                   | 54.5 ms                                                  | 52.2 ms: 1.04x faster                                                             |
| chaos                      | 70.7 ms                                                  | 67.8 ms: 1.04x faster                                                             |
| html5lib                   | 65.6 ms                                                  | 63.0 ms: 1.04x faster                                                             |
| sphinx                     | 1.20 sec                                                 | 1.16 sec: 1.04x faster                                                            |
| pprint_pformat             | 1.99 sec                                                 | 1.91 sec: 1.04x faster                                                            |
| xml_etree_process          | 82.1 ms                                                  | 79.2 ms: 1.04x faster                                                             |
| hexiom                     | 7.34 ms                                                  | 7.09 ms: 1.04x faster                                                             |
| pprint_safe_repr           | 962 ms                                                   | 931 ms: 1.03x faster                                                              |
| shortest_path              | 565 ms                                                   | 579 ms: 1.02x slower                                                              |
| connected_components       | 547 ms                                                   | 560 ms: 1.02x slower                                                              |
| create_gc_cycles           | 3.39 ms                                                  | 3.56 ms: 1.05x slower                                                             |
| raytrace                   | 310 ms                                                   | 327 ms: 1.05x slower                                                              |
| json_loads                 | 32.8 us                                                  | 34.8 us: 1.06x slower                                                             |
| gc_traversal               | 5.92 ms                                                  | 6.56 ms: 1.11x slower                                                             |
| python_startup_no_site     | 8.79 ms                                                  | 10.2 ms: 1.16x slower                                                             |
| subparsers                 | 20.3 ms                                                  | 25.8 ms: 1.27x slower                                                             |
| many_optionals             | 626 us                                                   | 847 us: 1.35x slower                                                              |
| bench_mp_pool              | 8.07 ms                                                  | 4.04 sec: 500.54x slower                                                          |
| Geometric mean             | (ref)                                                    | 1.01x slower                                                                      |

Benchmark hidden because not significant (34): generators, scimark_monte_carlo, sympy_sum, deltablue, sqlalchemy_declarative, logging_format, nqueens, sympy_expand, pidigits, scimark_lu, logging_silent, sqlalchemy_imperative, coverage, unpickle_pure_python, logging_simple, asyncio_websockets, genshi_text, docutils, json_dumps, sympy_str, genshi_xml, mako, bench_thread_pool, python_startup, json, scimark_sparse_mat_mult, nbody, coroutines, django_template, crypto_pyaes, fannkuch, pickle_pure_python, typing_runtime_protocols, comprehensions
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (5) of results/bm-20250409-3.14.0a7+-8aa20f2/bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.058x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.03x