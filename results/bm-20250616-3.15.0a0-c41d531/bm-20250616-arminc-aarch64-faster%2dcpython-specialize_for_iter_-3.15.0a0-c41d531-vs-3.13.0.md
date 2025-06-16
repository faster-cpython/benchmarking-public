# Results vs. 3.13.0

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: linux-aarch64
- commit hash: c41d531
- commit date: 2025-06-16
- overall geometric mean: 1.018x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250616-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 303 ms: 1.03x faster                                                              |
| html5lib       | 65.6 ms                                                  | 61.2 ms: 1.07x faster                                                             |
| sphinx         | 1.20 sec                                                 | 1.14 sec: 1.05x faster                                                            |
| Geometric mean | (ref)                                                    | 1.04x faster                                                                      |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250616-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 457 ms: 1.45x faster                                                              |
| async_tree_memoization     | 664 ms                                                   | 460 ms: 1.44x faster                                                              |
| async_tree_none_tg         | 484 ms                                                   | 365 ms: 1.33x faster                                                              |
| async_tree_none            | 504 ms                                                   | 385 ms: 1.31x faster                                                              |
| async_tree_io              | 1.14 sec                                                 | 892 ms: 1.28x faster                                                              |
| async_tree_io_tg           | 1.16 sec                                                 | 918 ms: 1.27x faster                                                              |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 646 ms: 1.24x faster                                                              |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 649 ms: 1.22x faster                                                              |
| async_generators           | 500 ms                                                   | 447 ms: 1.12x faster                                                              |
| Geometric mean             | (ref)                                                    | 1.23x faster                                                                      |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250616-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 85.4 ms: 1.12x faster                                                             |
| Geometric mean | (ref)                                                    | 1.03x faster                                                                      |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250616-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.01 ms: 1.27x faster                                                             |
| regex_v8       | 32.5 ms                                                  | 27.4 ms: 1.19x faster                                                             |
| regex_dna      | 263 ms                                                   | 223 ms: 1.18x faster                                                              |
| regex_compile  | 134 ms                                                   | 124 ms: 1.08x faster                                                              |
| Geometric mean | (ref)                                                    | 1.18x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250616-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|---------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 183 ms: 1.11x faster                                                              |
| xml_etree_iterparse | 159 ms                                                   | 143 ms: 1.11x faster                                                              |
| tomli_loads         | 2.67 sec                                                 | 2.44 sec: 1.09x faster                                                            |
| Geometric mean      | (ref)                                                    | 1.05x faster                                                                      |

Benchmark hidden because not significant (6): json_dumps, xml_etree_generate, xml_etree_process, unpickle_pure_python, json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250616-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 15.1 ms: 1.06x faster                                                             |
| python_startup_no_site | 8.79 ms                                                  | 8.61 ms: 1.02x faster                                                             |
| Geometric mean         | (ref)                                                    | 1.04x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250616-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml     | 61.6 ms                                                  | 60.3 ms: 1.02x faster                                                             |
| Geometric mean | (ref)                                                    | 1.00x faster                                                                      |

Benchmark hidden because not significant (3): genshi_text, django_template, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250616-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.64 sec: 2.10x faster                                                            |
| deepcopy                   | 479 us                                                   | 324 us: 1.48x faster                                                              |
| deepcopy_memo              | 53.0 us                                                  | 36.2 us: 1.46x faster                                                             |
| async_tree_memoization_tg  | 663 ms                                                   | 457 ms: 1.45x faster                                                              |
| async_tree_memoization     | 664 ms                                                   | 460 ms: 1.44x faster                                                              |
| async_tree_none_tg         | 484 ms                                                   | 365 ms: 1.33x faster                                                              |
| async_tree_none            | 504 ms                                                   | 385 ms: 1.31x faster                                                              |
| go                         | 164 ms                                                   | 128 ms: 1.28x faster                                                              |
| async_tree_io              | 1.14 sec                                                 | 892 ms: 1.28x faster                                                              |
| regex_effbot               | 5.10 ms                                                  | 4.01 ms: 1.27x faster                                                             |
| async_tree_io_tg           | 1.16 sec                                                 | 918 ms: 1.27x faster                                                              |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 646 ms: 1.24x faster                                                              |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 649 ms: 1.22x faster                                                              |
| deepcopy_reduce            | 4.24 us                                                  | 3.54 us: 1.20x faster                                                             |
| regex_v8                   | 32.5 ms                                                  | 27.4 ms: 1.19x faster                                                             |
| regex_dna                  | 263 ms                                                   | 223 ms: 1.18x faster                                                              |
| telco                      | 10.5 ms                                                  | 9.20 ms: 1.14x faster                                                             |
| spectral_norm              | 143 ms                                                   | 128 ms: 1.12x faster                                                              |
| float                      | 95.8 ms                                                  | 85.4 ms: 1.12x faster                                                             |
| async_generators           | 500 ms                                                   | 447 ms: 1.12x faster                                                              |
| generators                 | 40.3 ms                                                  | 36.1 ms: 1.12x faster                                                             |
| pyflate                    | 582 ms                                                   | 523 ms: 1.11x faster                                                              |
| scimark_sor                | 164 ms                                                   | 148 ms: 1.11x faster                                                              |
| xml_etree_parse            | 203 ms                                                   | 183 ms: 1.11x faster                                                              |
| xml_etree_iterparse        | 159 ms                                                   | 143 ms: 1.11x faster                                                              |
| bpe_tokeniser              | 6.02 sec                                                 | 5.44 sec: 1.11x faster                                                            |
| tomli_loads                | 2.67 sec                                                 | 2.44 sec: 1.09x faster                                                            |
| hexiom                     | 7.34 ms                                                  | 6.72 ms: 1.09x faster                                                             |
| pylint                     | 345 ms                                                   | 317 ms: 1.09x faster                                                              |
| meteor_contest             | 117 ms                                                   | 108 ms: 1.08x faster                                                              |
| regex_compile              | 134 ms                                                   | 124 ms: 1.08x faster                                                              |
| sqlite_synth               | 4.08 us                                                  | 3.80 us: 1.07x faster                                                             |
| scimark_monte_carlo        | 87.8 ms                                                  | 81.8 ms: 1.07x faster                                                             |
| sympy_sum                  | 151 ms                                                   | 141 ms: 1.07x faster                                                              |
| pycparser                  | 1.34 sec                                                 | 1.25 sec: 1.07x faster                                                            |
| html5lib                   | 65.6 ms                                                  | 61.2 ms: 1.07x faster                                                             |
| nqueens                    | 105 ms                                                   | 98.2 ms: 1.07x faster                                                             |
| sympy_integrate            | 21.4 ms                                                  | 20.2 ms: 1.06x faster                                                             |
| python_startup             | 16.0 ms                                                  | 15.1 ms: 1.06x faster                                                             |
| json                       | 5.94 ms                                                  | 5.63 ms: 1.06x faster                                                             |
| scimark_fft                | 463 ms                                                   | 439 ms: 1.05x faster                                                              |
| sphinx                     | 1.20 sec                                                 | 1.14 sec: 1.05x faster                                                            |
| k_core                     | 2.99 sec                                                 | 2.84 sec: 1.05x faster                                                            |
| crypto_pyaes               | 84.9 ms                                                  | 81.2 ms: 1.05x faster                                                             |
| 2to3                       | 313 ms                                                   | 303 ms: 1.03x faster                                                              |
| richards_super             | 60.8 ms                                                  | 58.9 ms: 1.03x faster                                                             |
| typing_runtime_protocols   | 197 us                                                   | 191 us: 1.03x faster                                                              |
| genshi_xml                 | 61.6 ms                                                  | 60.3 ms: 1.02x faster                                                             |
| python_startup_no_site     | 8.79 ms                                                  | 8.61 ms: 1.02x faster                                                             |
| shortest_path              | 565 ms                                                   | 578 ms: 1.02x slower                                                              |
| pprint_safe_repr           | 962 ms                                                   | 988 ms: 1.03x slower                                                              |
| connected_components       | 547 ms                                                   | 564 ms: 1.03x slower                                                              |
| logging_simple             | 7.25 us                                                  | 7.62 us: 1.05x slower                                                             |
| raytrace                   | 310 ms                                                   | 330 ms: 1.07x slower                                                              |
| create_gc_cycles           | 3.39 ms                                                  | 3.83 ms: 1.13x slower                                                             |
| gc_traversal               | 5.92 ms                                                  | 6.96 ms: 1.17x slower                                                             |
| many_optionals             | 626 us                                                   | 740 us: 1.18x slower                                                              |
| subparsers                 | 20.3 ms                                                  | 28.0 ms: 1.38x slower                                                             |
| logging_silent             | 135 ns                                                   | 609 ns: 4.53x slower                                                              |
| coverage                   | 106 ms                                                   | 545 ms: 5.16x slower                                                              |
| thrift                     | 1.01 ms                                                  | 194 ms: 191.83x slower                                                            |
| Geometric mean             | (ref)                                                    | 1.02x slower                                                                      |

Benchmark hidden because not significant (26): json_dumps, pathlib, xml_etree_generate, richards, chaos, xml_etree_process, genshi_text, pidigits, sympy_expand, docutils, asyncio_websockets, coroutines, deltablue, unpickle_pure_python, sympy_str, json_loads, comprehensions, fannkuch, scimark_sparse_mat_mult, django_template, pprint_pformat, scimark_lu, mako, logging_format, pickle_pure_python, nbody
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250616-3.15.0a0-c41d531/bm-20250616-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.018x slower

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.08x