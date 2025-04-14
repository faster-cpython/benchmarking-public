# Results vs. 3.13.0

- fork: faster-cpython
- ref: immortal_stickiness
- machine: linux-aarch64
- commit hash: 2a08194
- commit date: 2025-03-12
- overall geometric mean: 1.048x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 297 ms: 1.05x faster                                                              |
| html5lib       | 65.6 ms                                                  | 64.2 ms: 1.02x faster                                                             |
| sphinx         | 1.20 sec                                                 | 1.14 sec: 1.05x faster                                                            |
| Geometric mean | (ref)                                                    | 1.03x faster                                                                      |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization     | 664 ms                                                   | 474 ms: 1.40x faster                                                              |
| async_tree_memoization_tg  | 663 ms                                                   | 480 ms: 1.38x faster                                                              |
| async_tree_io_tg           | 1.16 sec                                                 | 891 ms: 1.31x faster                                                              |
| async_tree_none            | 504 ms                                                   | 386 ms: 1.31x faster                                                              |
| async_tree_io              | 1.14 sec                                                 | 881 ms: 1.29x faster                                                              |
| async_tree_none_tg         | 484 ms                                                   | 384 ms: 1.26x faster                                                              |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 650 ms: 1.23x faster                                                              |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 657 ms: 1.20x faster                                                              |
| async_generators           | 500 ms                                                   | 444 ms: 1.13x faster                                                              |
| asyncio_websockets         | 674 ms                                                   | 658 ms: 1.02x faster                                                              |
| Geometric mean             | (ref)                                                    | 1.22x faster                                                                      |

Benchmark hidden because not significant (1): coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 87.5 ms: 1.09x faster                                                             |
| nbody          | 118 ms                                                   | 126 ms: 1.06x slower                                                              |
| Geometric mean | (ref)                                                    | 1.01x faster                                                                      |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.98 ms: 1.28x faster                                                             |
| regex_v8       | 32.5 ms                                                  | 28.5 ms: 1.14x faster                                                             |
| regex_dna      | 263 ms                                                   | 241 ms: 1.09x faster                                                              |
| regex_compile  | 134 ms                                                   | 125 ms: 1.07x faster                                                              |
| Geometric mean | (ref)                                                    | 1.14x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|---------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 176 ms: 1.15x faster                                                              |
| xml_etree_iterparse | 159 ms                                                   | 141 ms: 1.13x faster                                                              |
| tomli_loads         | 2.67 sec                                                 | 2.42 sec: 1.10x faster                                                            |
| xml_etree_generate  | 118 ms                                                   | 111 ms: 1.06x faster                                                              |
| xml_etree_process   | 82.1 ms                                                  | 79.2 ms: 1.04x faster                                                             |
| Geometric mean      | (ref)                                                    | 1.05x faster                                                                      |

Benchmark hidden because not significant (4): json_dumps, unpickle_pure_python, json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 10.3 ms: 1.17x slower                                                             |
| Geometric mean         | (ref)                                                    | 1.09x slower                                                                      |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|-----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_text     | 28.6 ms                                                  | 26.8 ms: 1.07x faster                                                             |
| genshi_xml      | 61.6 ms                                                  | 60.4 ms: 1.02x faster                                                             |
| django_template | 39.4 ms                                                  | 41.5 ms: 1.05x slower                                                             |
| Geometric mean  | (ref)                                                    | 1.01x faster                                                                      |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| deepcopy                   | 479 us                                                   | 329 us: 1.45x faster                                                              |
| async_tree_memoization     | 664 ms                                                   | 474 ms: 1.40x faster                                                              |
| deepcopy_memo              | 53.0 us                                                  | 38.2 us: 1.39x faster                                                             |
| async_tree_memoization_tg  | 663 ms                                                   | 480 ms: 1.38x faster                                                              |
| async_tree_io_tg           | 1.16 sec                                                 | 891 ms: 1.31x faster                                                              |
| async_tree_none            | 504 ms                                                   | 386 ms: 1.31x faster                                                              |
| async_tree_io              | 1.14 sec                                                 | 881 ms: 1.29x faster                                                              |
| regex_effbot               | 5.10 ms                                                  | 3.98 ms: 1.28x faster                                                             |
| async_tree_none_tg         | 484 ms                                                   | 384 ms: 1.26x faster                                                              |
| deepcopy_reduce            | 4.24 us                                                  | 3.39 us: 1.25x faster                                                             |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 650 ms: 1.23x faster                                                              |
| go                         | 164 ms                                                   | 136 ms: 1.21x faster                                                              |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 657 ms: 1.20x faster                                                              |
| spectral_norm              | 143 ms                                                   | 124 ms: 1.15x faster                                                              |
| xml_etree_parse            | 203 ms                                                   | 176 ms: 1.15x faster                                                              |
| regex_v8                   | 32.5 ms                                                  | 28.5 ms: 1.14x faster                                                             |
| generators                 | 40.3 ms                                                  | 35.6 ms: 1.13x faster                                                             |
| async_generators           | 500 ms                                                   | 444 ms: 1.13x faster                                                              |
| xml_etree_iterparse        | 159 ms                                                   | 141 ms: 1.13x faster                                                              |
| pylint                     | 345 ms                                                   | 310 ms: 1.12x faster                                                              |
| tomli_loads                | 2.67 sec                                                 | 2.42 sec: 1.10x faster                                                            |
| float                      | 95.8 ms                                                  | 87.5 ms: 1.09x faster                                                             |
| regex_dna                  | 263 ms                                                   | 241 ms: 1.09x faster                                                              |
| sqlite_synth               | 4.08 us                                                  | 3.76 us: 1.08x faster                                                             |
| scimark_sor                | 164 ms                                                   | 152 ms: 1.08x faster                                                              |
| pathlib                    | 24.3 ms                                                  | 22.5 ms: 1.08x faster                                                             |
| coverage                   | 106 ms                                                   | 97.8 ms: 1.08x faster                                                             |
| bpe_tokeniser              | 6.02 sec                                                 | 5.59 sec: 1.08x faster                                                            |
| thrift                     | 1.01 ms                                                  | 943 us: 1.07x faster                                                              |
| scimark_fft                | 463 ms                                                   | 432 ms: 1.07x faster                                                              |
| regex_compile              | 134 ms                                                   | 125 ms: 1.07x faster                                                              |
| genshi_text                | 28.6 ms                                                  | 26.8 ms: 1.07x faster                                                             |
| sympy_sum                  | 151 ms                                                   | 142 ms: 1.06x faster                                                              |
| xml_etree_generate         | 118 ms                                                   | 111 ms: 1.06x faster                                                              |
| sqlalchemy_imperative      | 16.1 ms                                                  | 15.2 ms: 1.06x faster                                                             |
| pycparser                  | 1.34 sec                                                 | 1.27 sec: 1.06x faster                                                            |
| sphinx                     | 1.20 sec                                                 | 1.14 sec: 1.05x faster                                                            |
| 2to3                       | 313 ms                                                   | 297 ms: 1.05x faster                                                              |
| richards                   | 54.5 ms                                                  | 51.8 ms: 1.05x faster                                                             |
| logging_format             | 8.10 us                                                  | 7.72 us: 1.05x faster                                                             |
| nqueens                    | 105 ms                                                   | 101 ms: 1.04x faster                                                              |
| logging_simple             | 7.25 us                                                  | 6.96 us: 1.04x faster                                                             |
| k_core                     | 2.99 sec                                                 | 2.87 sec: 1.04x faster                                                            |
| logging_silent             | 135 ns                                                   | 130 ns: 1.04x faster                                                              |
| xml_etree_process          | 82.1 ms                                                  | 79.2 ms: 1.04x faster                                                             |
| mdp                        | 3.45 sec                                                 | 3.32 sec: 1.04x faster                                                            |
| pprint_pformat             | 1.99 sec                                                 | 1.92 sec: 1.04x faster                                                            |
| meteor_contest             | 117 ms                                                   | 113 ms: 1.04x faster                                                              |
| asyncio_websockets         | 674 ms                                                   | 658 ms: 1.02x faster                                                              |
| pprint_safe_repr           | 962 ms                                                   | 940 ms: 1.02x faster                                                              |
| html5lib                   | 65.6 ms                                                  | 64.2 ms: 1.02x faster                                                             |
| genshi_xml                 | 61.6 ms                                                  | 60.4 ms: 1.02x faster                                                             |
| connected_components       | 547 ms                                                   | 564 ms: 1.03x slower                                                              |
| raytrace                   | 310 ms                                                   | 322 ms: 1.04x slower                                                              |
| django_template            | 39.4 ms                                                  | 41.5 ms: 1.05x slower                                                             |
| nbody                      | 118 ms                                                   | 126 ms: 1.06x slower                                                              |
| create_gc_cycles           | 3.39 ms                                                  | 3.69 ms: 1.09x slower                                                             |
| gc_traversal               | 5.92 ms                                                  | 6.79 ms: 1.15x slower                                                             |
| python_startup_no_site     | 8.79 ms                                                  | 10.3 ms: 1.17x slower                                                             |
| subparsers                 | 20.3 ms                                                  | 25.5 ms: 1.25x slower                                                             |
| many_optionals             | 626 us                                                   | 822 us: 1.31x slower                                                              |
| bench_mp_pool              | 8.07 ms                                                  | 4.02 sec: 498.70x slower                                                          |
| Geometric mean             | (ref)                                                    | 1.01x slower                                                                      |

Benchmark hidden because not significant (29): sqlalchemy_declarative, telco, scimark_monte_carlo, json_dumps, chaos, scimark_sparse_mat_mult, richards_super, pyflate, sympy_expand, pidigits, json, unpickle_pure_python, typing_runtime_protocols, docutils, coroutines, hexiom, mako, sympy_str, sympy_integrate, bench_thread_pool, python_startup, shortest_path, deltablue, comprehensions, crypto_pyaes, scimark_lu, fannkuch, json_loads, pickle_pure_python
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250312-3.14.0a5+-2a08194/bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.048x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.03x