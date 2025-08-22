# Results vs. 3.13.0

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-aarch64
- commit hash: dc660a2
- commit date: 2025-08-22
- overall geometric mean: 1.032x faster
- HPT reliability: 99.92%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.04 sec: 1.03x slower                                                          |
| html5lib       | 65.6 ms                                                  | 61.7 ms: 1.06x faster                                                           |
| sphinx         | 1.20 sec                                                 | 1.16 sec: 1.04x faster                                                          |
| Geometric mean | (ref)                                                    | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 469 ms: 1.41x faster                                                            |
| async_tree_memoization     | 664 ms                                                   | 476 ms: 1.40x faster                                                            |
| async_tree_none            | 504 ms                                                   | 380 ms: 1.33x faster                                                            |
| async_tree_io              | 1.14 sec                                                 | 874 ms: 1.30x faster                                                            |
| async_tree_io_tg           | 1.16 sec                                                 | 905 ms: 1.29x faster                                                            |
| async_tree_none_tg         | 484 ms                                                   | 381 ms: 1.27x faster                                                            |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 654 ms: 1.22x faster                                                            |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 661 ms: 1.19x faster                                                            |
| async_generators           | 500 ms                                                   | 481 ms: 1.04x faster                                                            |
| Geometric mean             | (ref)                                                    | 1.21x faster                                                                    |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 75.9 ms: 1.26x faster                                                           |
| nbody          | 118 ms                                                   | 106 ms: 1.12x faster                                                            |
| Geometric mean | (ref)                                                    | 1.13x faster                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.80 ms: 1.34x faster                                                           |
| regex_v8       | 32.5 ms                                                  | 26.7 ms: 1.22x faster                                                           |
| regex_dna      | 263 ms                                                   | 218 ms: 1.21x faster                                                            |
| regex_compile  | 134 ms                                                   | 121 ms: 1.10x faster                                                            |
| Geometric mean | (ref)                                                    | 1.21x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.67 sec                                                 | 2.22 sec: 1.20x faster                                                          |
| json_dumps           | 14.2 ms                                                  | 11.9 ms: 1.19x faster                                                           |
| xml_etree_parse      | 203 ms                                                   | 183 ms: 1.11x faster                                                            |
| xml_etree_generate   | 118 ms                                                   | 108 ms: 1.09x faster                                                            |
| xml_etree_iterparse  | 159 ms                                                   | 146 ms: 1.09x faster                                                            |
| xml_etree_process    | 82.1 ms                                                  | 75.8 ms: 1.08x faster                                                           |
| unpickle_pure_python | 265 us                                                   | 247 us: 1.07x faster                                                            |
| Geometric mean       | (ref)                                                    | 1.09x faster                                                                    |

Benchmark hidden because not significant (2): json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 15.0 ms: 1.07x faster                                                           |
| python_startup_no_site | 8.79 ms                                                  | 8.62 ms: 1.02x faster                                                           |
| Geometric mean         | (ref)                                                    | 1.05x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako           | 14.0 ms                                                  | 12.9 ms: 1.09x faster                                                           |
| genshi_xml     | 61.6 ms                                                  | 62.8 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                    | 1.02x faster                                                                    |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.63 sec: 2.11x faster                                                          |
| deepcopy                   | 479 us                                                   | 331 us: 1.45x faster                                                            |
| deepcopy_memo              | 53.0 us                                                  | 36.6 us: 1.45x faster                                                           |
| async_tree_memoization_tg  | 663 ms                                                   | 469 ms: 1.41x faster                                                            |
| async_tree_memoization     | 664 ms                                                   | 476 ms: 1.40x faster                                                            |
| regex_effbot               | 5.10 ms                                                  | 3.80 ms: 1.34x faster                                                           |
| async_tree_none            | 504 ms                                                   | 380 ms: 1.33x faster                                                            |
| richards                   | 54.5 ms                                                  | 41.7 ms: 1.31x faster                                                           |
| async_tree_io              | 1.14 sec                                                 | 874 ms: 1.30x faster                                                            |
| async_tree_io_tg           | 1.16 sec                                                 | 905 ms: 1.29x faster                                                            |
| async_tree_none_tg         | 484 ms                                                   | 381 ms: 1.27x faster                                                            |
| spectral_norm              | 143 ms                                                   | 113 ms: 1.27x faster                                                            |
| float                      | 95.8 ms                                                  | 75.9 ms: 1.26x faster                                                           |
| richards_super             | 60.8 ms                                                  | 49.3 ms: 1.23x faster                                                           |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 654 ms: 1.22x faster                                                            |
| regex_v8                   | 32.5 ms                                                  | 26.7 ms: 1.22x faster                                                           |
| regex_dna                  | 263 ms                                                   | 218 ms: 1.21x faster                                                            |
| tomli_loads                | 2.67 sec                                                 | 2.22 sec: 1.20x faster                                                          |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 661 ms: 1.19x faster                                                            |
| json_dumps                 | 14.2 ms                                                  | 11.9 ms: 1.19x faster                                                           |
| scimark_fft                | 463 ms                                                   | 390 ms: 1.19x faster                                                            |
| scimark_sor                | 164 ms                                                   | 139 ms: 1.18x faster                                                            |
| deepcopy_reduce            | 4.24 us                                                  | 3.59 us: 1.18x faster                                                           |
| pyflate                    | 582 ms                                                   | 506 ms: 1.15x faster                                                            |
| bpe_tokeniser              | 6.02 sec                                                 | 5.24 sec: 1.15x faster                                                          |
| generators                 | 40.3 ms                                                  | 35.8 ms: 1.13x faster                                                           |
| nbody                      | 118 ms                                                   | 106 ms: 1.12x faster                                                            |
| logging_format             | 8.10 us                                                  | 7.26 us: 1.12x faster                                                           |
| go                         | 164 ms                                                   | 148 ms: 1.11x faster                                                            |
| pathlib                    | 24.3 ms                                                  | 22.0 ms: 1.11x faster                                                           |
| xml_etree_parse            | 203 ms                                                   | 183 ms: 1.11x faster                                                            |
| scimark_monte_carlo        | 87.8 ms                                                  | 79.4 ms: 1.11x faster                                                           |
| regex_compile              | 134 ms                                                   | 121 ms: 1.10x faster                                                            |
| xml_etree_generate         | 118 ms                                                   | 108 ms: 1.09x faster                                                            |
| xml_etree_iterparse        | 159 ms                                                   | 146 ms: 1.09x faster                                                            |
| mako                       | 14.0 ms                                                  | 12.9 ms: 1.09x faster                                                           |
| sqlite_synth               | 4.08 us                                                  | 3.76 us: 1.09x faster                                                           |
| xml_etree_process          | 82.1 ms                                                  | 75.8 ms: 1.08x faster                                                           |
| deltablue                  | 3.97 ms                                                  | 3.68 ms: 1.08x faster                                                           |
| unpickle_pure_python       | 265 us                                                   | 247 us: 1.07x faster                                                            |
| python_startup             | 16.0 ms                                                  | 15.0 ms: 1.07x faster                                                           |
| logging_simple             | 7.25 us                                                  | 6.78 us: 1.07x faster                                                           |
| pylint                     | 345 ms                                                   | 324 ms: 1.07x faster                                                            |
| html5lib                   | 65.6 ms                                                  | 61.7 ms: 1.06x faster                                                           |
| chaos                      | 70.7 ms                                                  | 66.5 ms: 1.06x faster                                                           |
| k_core                     | 2.99 sec                                                 | 2.83 sec: 1.06x faster                                                          |
| json                       | 5.94 ms                                                  | 5.63 ms: 1.05x faster                                                           |
| logging_silent             | 135 ns                                                   | 129 ns: 1.04x faster                                                            |
| async_generators           | 500 ms                                                   | 481 ms: 1.04x faster                                                            |
| nqueens                    | 105 ms                                                   | 101 ms: 1.04x faster                                                            |
| sphinx                     | 1.20 sec                                                 | 1.16 sec: 1.04x faster                                                          |
| python_startup_no_site     | 8.79 ms                                                  | 8.62 ms: 1.02x faster                                                           |
| djangocms                  | 66.2 us                                                  | 65.0 us: 1.02x faster                                                           |
| genshi_xml                 | 61.6 ms                                                  | 62.8 ms: 1.02x slower                                                           |
| connected_components       | 547 ms                                                   | 559 ms: 1.02x slower                                                            |
| sympy_str                  | 265 ms                                                   | 272 ms: 1.03x slower                                                            |
| docutils                   | 2.96 sec                                                 | 3.04 sec: 1.03x slower                                                          |
| shortest_path              | 565 ms                                                   | 580 ms: 1.03x slower                                                            |
| raytrace                   | 310 ms                                                   | 322 ms: 1.04x slower                                                            |
| comprehensions             | 20.8 us                                                  | 22.2 us: 1.07x slower                                                           |
| typing_runtime_protocols   | 197 us                                                   | 216 us: 1.09x slower                                                            |
| create_gc_cycles           | 3.39 ms                                                  | 3.73 ms: 1.10x slower                                                           |
| pprint_pformat             | 1.99 sec                                                 | 2.25 sec: 1.14x slower                                                          |
| pprint_safe_repr           | 962 ms                                                   | 1.10 sec: 1.15x slower                                                          |
| gc_traversal               | 5.92 ms                                                  | 6.82 ms: 1.15x slower                                                           |
| many_optionals             | 626 us                                                   | 991 us: 1.58x slower                                                            |
| subparsers                 | 20.3 ms                                                  | 47.8 ms: 2.35x slower                                                           |
| telco                      | 10.5 ms                                                  | 165 ms: 15.78x slower                                                           |
| Geometric mean             | (ref)                                                    | 1.04x faster                                                                    |

Benchmark hidden because not significant (20): genshi_text, fannkuch, meteor_contest, scimark_lu, thrift, hexiom, coverage, sympy_integrate, 2to3, sympy_sum, pidigits, json_loads, asyncio_websockets, pycparser, coroutines, django_template, sympy_expand, crypto_pyaes, scimark_sparse_mat_mult, pickle_pure_python
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250822-3.15.0a0-dc660a2-JIT/bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.032x faster

# HPT report

- Reliability score: 99.92% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.10x