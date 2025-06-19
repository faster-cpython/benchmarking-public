# Results vs. 3.13.0

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-aarch64
- commit hash: 2850d72
- commit date: 2025-06-19
- overall geometric mean: 1.049x faster
- HPT reliability: 99.51%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.09 sec: 1.04x slower                                                          |
| html5lib       | 65.6 ms                                                  | 63.7 ms: 1.03x faster                                                           |
| sphinx         | 1.20 sec                                                 | 1.17 sec: 1.03x faster                                                          |
| Geometric mean | (ref)                                                    | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization     | 664 ms                                                   | 476 ms: 1.40x faster                                                            |
| async_tree_memoization_tg  | 663 ms                                                   | 479 ms: 1.38x faster                                                            |
| async_tree_none_tg         | 484 ms                                                   | 386 ms: 1.26x faster                                                            |
| async_tree_none            | 504 ms                                                   | 402 ms: 1.26x faster                                                            |
| async_tree_io              | 1.14 sec                                                 | 910 ms: 1.25x faster                                                            |
| async_tree_io_tg           | 1.16 sec                                                 | 933 ms: 1.25x faster                                                            |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 665 ms: 1.20x faster                                                            |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 668 ms: 1.18x faster                                                            |
| async_generators           | 500 ms                                                   | 480 ms: 1.04x faster                                                            |
| Geometric mean             | (ref)                                                    | 1.19x faster                                                                    |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 77.3 ms: 1.24x faster                                                           |
| nbody          | 118 ms                                                   | 105 ms: 1.12x faster                                                            |
| Geometric mean | (ref)                                                    | 1.12x faster                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.89 ms: 1.31x faster                                                           |
| regex_dna      | 263 ms                                                   | 216 ms: 1.21x faster                                                            |
| regex_v8       | 32.5 ms                                                  | 27.0 ms: 1.21x faster                                                           |
| regex_compile  | 134 ms                                                   | 122 ms: 1.09x faster                                                            |
| Geometric mean | (ref)                                                    | 1.20x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|---------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads         | 2.67 sec                                                 | 2.29 sec: 1.16x faster                                                          |
| xml_etree_parse     | 203 ms                                                   | 179 ms: 1.13x faster                                                            |
| xml_etree_iterparse | 159 ms                                                   | 142 ms: 1.12x faster                                                            |
| xml_etree_generate  | 118 ms                                                   | 110 ms: 1.07x faster                                                            |
| xml_etree_process   | 82.1 ms                                                  | 77.2 ms: 1.06x faster                                                           |
| Geometric mean      | (ref)                                                    | 1.06x faster                                                                    |

Benchmark hidden because not significant (4): unpickle_pure_python, json_loads, json_dumps, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 15.0 ms: 1.07x faster                                                           |
| python_startup_no_site | 8.79 ms                                                  | 8.58 ms: 1.02x faster                                                           |
| Geometric mean         | (ref)                                                    | 1.05x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|-----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 14.0 ms                                                  | 13.3 ms: 1.05x faster                                                           |
| genshi_text     | 28.6 ms                                                  | 27.3 ms: 1.05x faster                                                           |
| genshi_xml      | 61.6 ms                                                  | 64.3 ms: 1.04x slower                                                           |
| django_template | 39.4 ms                                                  | 41.4 ms: 1.05x slower                                                           |
| Geometric mean  | (ref)                                                    | 1.00x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.69 sec: 2.04x faster                                                          |
| deepcopy                   | 479 us                                                   | 339 us: 1.41x faster                                                            |
| async_tree_memoization     | 664 ms                                                   | 476 ms: 1.40x faster                                                            |
| deepcopy_memo              | 53.0 us                                                  | 38.2 us: 1.38x faster                                                           |
| async_tree_memoization_tg  | 663 ms                                                   | 479 ms: 1.38x faster                                                            |
| regex_effbot               | 5.10 ms                                                  | 3.89 ms: 1.31x faster                                                           |
| async_tree_none_tg         | 484 ms                                                   | 386 ms: 1.26x faster                                                            |
| async_tree_none            | 504 ms                                                   | 402 ms: 1.26x faster                                                            |
| async_tree_io              | 1.14 sec                                                 | 910 ms: 1.25x faster                                                            |
| async_tree_io_tg           | 1.16 sec                                                 | 933 ms: 1.25x faster                                                            |
| float                      | 95.8 ms                                                  | 77.3 ms: 1.24x faster                                                           |
| spectral_norm              | 143 ms                                                   | 118 ms: 1.22x faster                                                            |
| regex_dna                  | 263 ms                                                   | 216 ms: 1.21x faster                                                            |
| regex_v8                   | 32.5 ms                                                  | 27.0 ms: 1.21x faster                                                           |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 665 ms: 1.20x faster                                                            |
| richards                   | 54.5 ms                                                  | 45.6 ms: 1.20x faster                                                           |
| scimark_fft                | 463 ms                                                   | 391 ms: 1.18x faster                                                            |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 668 ms: 1.18x faster                                                            |
| tomli_loads                | 2.67 sec                                                 | 2.29 sec: 1.16x faster                                                          |
| scimark_sor                | 164 ms                                                   | 141 ms: 1.16x faster                                                            |
| richards_super             | 60.8 ms                                                  | 52.4 ms: 1.16x faster                                                           |
| deepcopy_reduce            | 4.24 us                                                  | 3.69 us: 1.15x faster                                                           |
| generators                 | 40.3 ms                                                  | 35.2 ms: 1.14x faster                                                           |
| xml_etree_parse            | 203 ms                                                   | 179 ms: 1.13x faster                                                            |
| bpe_tokeniser              | 6.02 sec                                                 | 5.31 sec: 1.13x faster                                                          |
| nbody                      | 118 ms                                                   | 105 ms: 1.12x faster                                                            |
| xml_etree_iterparse        | 159 ms                                                   | 142 ms: 1.12x faster                                                            |
| pyflate                    | 582 ms                                                   | 522 ms: 1.12x faster                                                            |
| regex_compile              | 134 ms                                                   | 122 ms: 1.09x faster                                                            |
| scimark_monte_carlo        | 87.8 ms                                                  | 80.3 ms: 1.09x faster                                                           |
| telco                      | 10.5 ms                                                  | 9.58 ms: 1.09x faster                                                           |
| sqlite_synth               | 4.08 us                                                  | 3.77 us: 1.08x faster                                                           |
| pathlib                    | 24.3 ms                                                  | 22.6 ms: 1.08x faster                                                           |
| xml_etree_generate         | 118 ms                                                   | 110 ms: 1.07x faster                                                            |
| python_startup             | 16.0 ms                                                  | 15.0 ms: 1.07x faster                                                           |
| xml_etree_process          | 82.1 ms                                                  | 77.2 ms: 1.06x faster                                                           |
| deltablue                  | 3.97 ms                                                  | 3.73 ms: 1.06x faster                                                           |
| pylint                     | 345 ms                                                   | 325 ms: 1.06x faster                                                            |
| k_core                     | 2.99 sec                                                 | 2.83 sec: 1.06x faster                                                          |
| json                       | 5.94 ms                                                  | 5.63 ms: 1.05x faster                                                           |
| mako                       | 14.0 ms                                                  | 13.3 ms: 1.05x faster                                                           |
| nqueens                    | 105 ms                                                   | 99.8 ms: 1.05x faster                                                           |
| genshi_text                | 28.6 ms                                                  | 27.3 ms: 1.05x faster                                                           |
| async_generators           | 500 ms                                                   | 480 ms: 1.04x faster                                                            |
| meteor_contest             | 117 ms                                                   | 113 ms: 1.04x faster                                                            |
| html5lib                   | 65.6 ms                                                  | 63.7 ms: 1.03x faster                                                           |
| sphinx                     | 1.20 sec                                                 | 1.17 sec: 1.03x faster                                                          |
| python_startup_no_site     | 8.79 ms                                                  | 8.58 ms: 1.02x faster                                                           |
| djangocms                  | 66.2 us                                                  | 65.0 us: 1.02x faster                                                           |
| shortest_path              | 565 ms                                                   | 575 ms: 1.02x slower                                                            |
| pycparser                  | 1.34 sec                                                 | 1.38 sec: 1.02x slower                                                          |
| docutils                   | 2.96 sec                                                 | 3.09 sec: 1.04x slower                                                          |
| sympy_expand               | 472 ms                                                   | 493 ms: 1.04x slower                                                            |
| genshi_xml                 | 61.6 ms                                                  | 64.3 ms: 1.04x slower                                                           |
| typing_runtime_protocols   | 197 us                                                   | 207 us: 1.05x slower                                                            |
| django_template            | 39.4 ms                                                  | 41.4 ms: 1.05x slower                                                           |
| sympy_str                  | 265 ms                                                   | 279 ms: 1.05x slower                                                            |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 7.02 ms: 1.05x slower                                                           |
| logging_format             | 8.10 us                                                  | 8.59 us: 1.06x slower                                                           |
| crypto_pyaes               | 84.9 ms                                                  | 90.0 ms: 1.06x slower                                                           |
| raytrace                   | 310 ms                                                   | 332 ms: 1.07x slower                                                            |
| scimark_lu                 | 146 ms                                                   | 156 ms: 1.07x slower                                                            |
| comprehensions             | 20.8 us                                                  | 22.3 us: 1.07x slower                                                           |
| logging_simple             | 7.25 us                                                  | 7.85 us: 1.08x slower                                                           |
| create_gc_cycles           | 3.39 ms                                                  | 3.69 ms: 1.09x slower                                                           |
| gc_traversal               | 5.92 ms                                                  | 6.98 ms: 1.18x slower                                                           |
| pprint_pformat             | 1.99 sec                                                 | 2.60 sec: 1.31x slower                                                          |
| pprint_safe_repr           | 962 ms                                                   | 1.26 sec: 1.31x slower                                                          |
| many_optionals             | 626 us                                                   | 846 us: 1.35x slower                                                            |
| subparsers                 | 20.3 ms                                                  | 29.9 ms: 1.47x slower                                                           |
| logging_silent             | 135 ns                                                   | 630 ns: 4.68x slower                                                            |
| Geometric mean             | (ref)                                                    | 1.04x faster                                                                    |

Benchmark hidden because not significant (17): unpickle_pure_python, go, sympy_integrate, coverage, json_loads, json_dumps, thrift, 2to3, sympy_sum, asyncio_websockets, chaos, pidigits, fannkuch, hexiom, connected_components, coroutines, pickle_pure_python
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250619-3.15.0a0-2850d72-JIT/bm-20250619-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.049x faster

# HPT report

- Reliability score: 99.51% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.10x