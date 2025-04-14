# Results vs. 3.13.0

- fork: faster-cpython
- ref: trashcan_in_dealloc
- machine: linux-aarch64
- commit hash: 3514aa1
- commit date: 2025-04-09
- overall geometric mean: 1.057x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 298 ms: 1.05x faster                                                              |
| sphinx         | 1.20 sec                                                 | 1.14 sec: 1.05x faster                                                            |
| Geometric mean | (ref)                                                    | 1.03x faster                                                                      |

Benchmark hidden because not significant (2): docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization     | 664 ms                                                   | 460 ms: 1.44x faster                                                              |
| async_tree_memoization_tg  | 663 ms                                                   | 464 ms: 1.43x faster                                                              |
| async_tree_none            | 504 ms                                                   | 386 ms: 1.31x faster                                                              |
| async_tree_io_tg           | 1.16 sec                                                 | 892 ms: 1.31x faster                                                              |
| async_tree_io              | 1.14 sec                                                 | 877 ms: 1.30x faster                                                              |
| async_tree_none_tg         | 484 ms                                                   | 373 ms: 1.30x faster                                                              |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 648 ms: 1.24x faster                                                              |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 660 ms: 1.20x faster                                                              |
| async_generators           | 500 ms                                                   | 462 ms: 1.08x faster                                                              |
| Geometric mean             | (ref)                                                    | 1.22x faster                                                                      |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 85.8 ms: 1.12x faster                                                             |
| Geometric mean | (ref)                                                    | 1.02x faster                                                                      |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.00 ms: 1.28x faster                                                             |
| regex_v8       | 32.5 ms                                                  | 28.0 ms: 1.16x faster                                                             |
| regex_dna      | 263 ms                                                   | 242 ms: 1.08x faster                                                              |
| regex_compile  | 134 ms                                                   | 124 ms: 1.08x faster                                                              |
| Geometric mean | (ref)                                                    | 1.15x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|---------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 180 ms: 1.13x faster                                                              |
| xml_etree_iterparse | 159 ms                                                   | 142 ms: 1.12x faster                                                              |
| tomli_loads         | 2.67 sec                                                 | 2.50 sec: 1.07x faster                                                            |
| json_loads          | 32.8 us                                                  | 34.9 us: 1.06x slower                                                             |
| Geometric mean      | (ref)                                                    | 1.03x faster                                                                      |

Benchmark hidden because not significant (5): xml_etree_generate, xml_etree_process, json_dumps, unpickle_pure_python, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 10.2 ms: 1.16x slower                                                             |
| Geometric mean         | (ref)                                                    | 1.08x slower                                                                      |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|-----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml      | 61.6 ms                                                  | 60.9 ms: 1.01x faster                                                             |
| django_template | 39.4 ms                                                  | 41.2 ms: 1.05x slower                                                             |
| Geometric mean  | (ref)                                                    | 1.00x slower                                                                      |

Benchmark hidden because not significant (2): genshi_text, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.68 sec: 2.05x faster                                                            |
| deepcopy                   | 479 us                                                   | 331 us: 1.45x faster                                                              |
| async_tree_memoization     | 664 ms                                                   | 460 ms: 1.44x faster                                                              |
| async_tree_memoization_tg  | 663 ms                                                   | 464 ms: 1.43x faster                                                              |
| deepcopy_memo              | 53.0 us                                                  | 37.5 us: 1.41x faster                                                             |
| async_tree_none            | 504 ms                                                   | 386 ms: 1.31x faster                                                              |
| async_tree_io_tg           | 1.16 sec                                                 | 892 ms: 1.31x faster                                                              |
| async_tree_io              | 1.14 sec                                                 | 877 ms: 1.30x faster                                                              |
| async_tree_none_tg         | 484 ms                                                   | 373 ms: 1.30x faster                                                              |
| regex_effbot               | 5.10 ms                                                  | 4.00 ms: 1.28x faster                                                             |
| go                         | 164 ms                                                   | 132 ms: 1.24x faster                                                              |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 648 ms: 1.24x faster                                                              |
| deepcopy_reduce            | 4.24 us                                                  | 3.52 us: 1.21x faster                                                             |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 660 ms: 1.20x faster                                                              |
| regex_v8                   | 32.5 ms                                                  | 28.0 ms: 1.16x faster                                                             |
| spectral_norm              | 143 ms                                                   | 127 ms: 1.13x faster                                                              |
| xml_etree_parse            | 203 ms                                                   | 180 ms: 1.13x faster                                                              |
| scimark_sor                | 164 ms                                                   | 146 ms: 1.12x faster                                                              |
| xml_etree_iterparse        | 159 ms                                                   | 142 ms: 1.12x faster                                                              |
| float                      | 95.8 ms                                                  | 85.8 ms: 1.12x faster                                                             |
| telco                      | 10.5 ms                                                  | 9.48 ms: 1.10x faster                                                             |
| generators                 | 40.3 ms                                                  | 36.7 ms: 1.10x faster                                                             |
| pylint                     | 345 ms                                                   | 315 ms: 1.10x faster                                                              |
| pycparser                  | 1.34 sec                                                 | 1.24 sec: 1.09x faster                                                            |
| regex_dna                  | 263 ms                                                   | 242 ms: 1.08x faster                                                              |
| async_generators           | 500 ms                                                   | 462 ms: 1.08x faster                                                              |
| pathlib                    | 24.3 ms                                                  | 22.5 ms: 1.08x faster                                                             |
| regex_compile              | 134 ms                                                   | 124 ms: 1.08x faster                                                              |
| sympy_integrate            | 21.4 ms                                                  | 20.0 ms: 1.07x faster                                                             |
| pyflate                    | 582 ms                                                   | 543 ms: 1.07x faster                                                              |
| tomli_loads                | 2.67 sec                                                 | 2.50 sec: 1.07x faster                                                            |
| nqueens                    | 105 ms                                                   | 98.4 ms: 1.07x faster                                                             |
| bpe_tokeniser              | 6.02 sec                                                 | 5.65 sec: 1.07x faster                                                            |
| richards                   | 54.5 ms                                                  | 51.2 ms: 1.06x faster                                                             |
| scimark_fft                | 463 ms                                                   | 435 ms: 1.06x faster                                                              |
| k_core                     | 2.99 sec                                                 | 2.81 sec: 1.06x faster                                                            |
| sqlite_synth               | 4.08 us                                                  | 3.84 us: 1.06x faster                                                             |
| sphinx                     | 1.20 sec                                                 | 1.14 sec: 1.05x faster                                                            |
| chaos                      | 70.7 ms                                                  | 67.3 ms: 1.05x faster                                                             |
| logging_silent             | 135 ns                                                   | 128 ns: 1.05x faster                                                              |
| coverage                   | 106 ms                                                   | 101 ms: 1.05x faster                                                              |
| 2to3                       | 313 ms                                                   | 298 ms: 1.05x faster                                                              |
| meteor_contest             | 117 ms                                                   | 112 ms: 1.05x faster                                                              |
| hexiom                     | 7.34 ms                                                  | 7.02 ms: 1.05x faster                                                             |
| pprint_pformat             | 1.99 sec                                                 | 1.90 sec: 1.04x faster                                                            |
| richards_super             | 60.8 ms                                                  | 58.6 ms: 1.04x faster                                                             |
| pprint_safe_repr           | 962 ms                                                   | 936 ms: 1.03x faster                                                              |
| genshi_xml                 | 61.6 ms                                                  | 60.9 ms: 1.01x faster                                                             |
| connected_components       | 547 ms                                                   | 563 ms: 1.03x slower                                                              |
| shortest_path              | 565 ms                                                   | 583 ms: 1.03x slower                                                              |
| create_gc_cycles           | 3.39 ms                                                  | 3.54 ms: 1.04x slower                                                             |
| django_template            | 39.4 ms                                                  | 41.2 ms: 1.05x slower                                                             |
| raytrace                   | 310 ms                                                   | 325 ms: 1.05x slower                                                              |
| json_loads                 | 32.8 us                                                  | 34.9 us: 1.06x slower                                                             |
| gc_traversal               | 5.92 ms                                                  | 6.62 ms: 1.12x slower                                                             |
| python_startup_no_site     | 8.79 ms                                                  | 10.2 ms: 1.16x slower                                                             |
| subparsers                 | 20.3 ms                                                  | 26.6 ms: 1.31x slower                                                             |
| many_optionals             | 626 us                                                   | 837 us: 1.34x slower                                                              |
| bench_mp_pool              | 8.07 ms                                                  | 2.04 sec: 252.66x slower                                                          |
| Geometric mean             | (ref)                                                    | 1.00x faster                                                                      |

Benchmark hidden because not significant (31): scimark_monte_carlo, sympy_sum, xml_etree_generate, deltablue, sqlalchemy_declarative, genshi_text, xml_etree_process, scimark_lu, logging_format, html5lib, json_dumps, sympy_expand, docutils, asyncio_websockets, sympy_str, logging_simple, pidigits, python_startup, bench_thread_pool, unpickle_pure_python, mako, sqlalchemy_imperative, fannkuch, crypto_pyaes, coroutines, json, pickle_pure_python, scimark_sparse_mat_mult, typing_runtime_protocols, comprehensions, nbody
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (5) of results/bm-20250409-3.14.0a7+-3514aa1/bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.057x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.03x