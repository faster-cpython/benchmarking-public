# Results vs. 3.13.0

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-aarch64
- commit hash: efe4628
- commit date: 2025-08-22
- overall geometric mean: 1.023x faster
- HPT reliability: 99.71%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.08 sec: 1.04x slower                                                          |
| html5lib       | 65.6 ms                                                  | 61.7 ms: 1.06x faster                                                           |
| sphinx         | 1.20 sec                                                 | 1.15 sec: 1.04x faster                                                          |
| Geometric mean | (ref)                                                    | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 465 ms: 1.43x faster                                                            |
| async_tree_memoization     | 664 ms                                                   | 472 ms: 1.41x faster                                                            |
| async_tree_none            | 504 ms                                                   | 381 ms: 1.32x faster                                                            |
| async_tree_io_tg           | 1.16 sec                                                 | 889 ms: 1.31x faster                                                            |
| async_tree_none_tg         | 484 ms                                                   | 373 ms: 1.30x faster                                                            |
| async_tree_io              | 1.14 sec                                                 | 879 ms: 1.30x faster                                                            |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 644 ms: 1.24x faster                                                            |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 660 ms: 1.20x faster                                                            |
| Geometric mean             | (ref)                                                    | 1.21x faster                                                                    |

Benchmark hidden because not significant (3): async_generators, asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 76.3 ms: 1.26x faster                                                           |
| nbody          | 118 ms                                                   | 106 ms: 1.12x faster                                                            |
| Geometric mean | (ref)                                                    | 1.12x faster                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.91 ms: 1.30x faster                                                           |
| regex_v8       | 32.5 ms                                                  | 26.9 ms: 1.21x faster                                                           |
| regex_dna      | 263 ms                                                   | 226 ms: 1.16x faster                                                            |
| regex_compile  | 134 ms                                                   | 122 ms: 1.10x faster                                                            |
| Geometric mean | (ref)                                                    | 1.19x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|---------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps          | 14.2 ms                                                  | 11.9 ms: 1.19x faster                                                           |
| tomli_loads         | 2.67 sec                                                 | 2.24 sec: 1.19x faster                                                          |
| xml_etree_parse     | 203 ms                                                   | 183 ms: 1.11x faster                                                            |
| xml_etree_iterparse | 159 ms                                                   | 144 ms: 1.10x faster                                                            |
| xml_etree_generate  | 118 ms                                                   | 108 ms: 1.09x faster                                                            |
| xml_etree_process   | 82.1 ms                                                  | 76.3 ms: 1.08x faster                                                           |
| Geometric mean      | (ref)                                                    | 1.08x faster                                                                    |

Benchmark hidden because not significant (3): unpickle_pure_python, json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 15.1 ms: 1.06x faster                                                           |
| python_startup_no_site | 8.79 ms                                                  | 8.61 ms: 1.02x faster                                                           |
| Geometric mean         | (ref)                                                    | 1.04x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|-----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 14.0 ms                                                  | 12.8 ms: 1.09x faster                                                           |
| genshi_text     | 28.6 ms                                                  | 27.0 ms: 1.06x faster                                                           |
| django_template | 39.4 ms                                                  | 38.6 ms: 1.02x faster                                                           |
| genshi_xml      | 61.6 ms                                                  | 64.1 ms: 1.04x slower                                                           |
| Geometric mean  | (ref)                                                    | 1.03x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.66 sec: 2.07x faster                                                          |
| deepcopy_memo              | 53.0 us                                                  | 36.8 us: 1.44x faster                                                           |
| async_tree_memoization_tg  | 663 ms                                                   | 465 ms: 1.43x faster                                                            |
| deepcopy                   | 479 us                                                   | 338 us: 1.42x faster                                                            |
| async_tree_memoization     | 664 ms                                                   | 472 ms: 1.41x faster                                                            |
| async_tree_none            | 504 ms                                                   | 381 ms: 1.32x faster                                                            |
| async_tree_io_tg           | 1.16 sec                                                 | 889 ms: 1.31x faster                                                            |
| regex_effbot               | 5.10 ms                                                  | 3.91 ms: 1.30x faster                                                           |
| async_tree_none_tg         | 484 ms                                                   | 373 ms: 1.30x faster                                                            |
| spectral_norm              | 143 ms                                                   | 111 ms: 1.30x faster                                                            |
| async_tree_io              | 1.14 sec                                                 | 879 ms: 1.30x faster                                                            |
| float                      | 95.8 ms                                                  | 76.3 ms: 1.26x faster                                                           |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 644 ms: 1.24x faster                                                            |
| richards                   | 54.5 ms                                                  | 44.6 ms: 1.22x faster                                                           |
| richards_super             | 60.8 ms                                                  | 49.9 ms: 1.22x faster                                                           |
| scimark_fft                | 463 ms                                                   | 382 ms: 1.21x faster                                                            |
| regex_v8                   | 32.5 ms                                                  | 26.9 ms: 1.21x faster                                                           |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 660 ms: 1.20x faster                                                            |
| json_dumps                 | 14.2 ms                                                  | 11.9 ms: 1.19x faster                                                           |
| tomli_loads                | 2.67 sec                                                 | 2.24 sec: 1.19x faster                                                          |
| regex_dna                  | 263 ms                                                   | 226 ms: 1.16x faster                                                            |
| deepcopy_reduce            | 4.24 us                                                  | 3.70 us: 1.15x faster                                                           |
| scimark_sor                | 164 ms                                                   | 143 ms: 1.14x faster                                                            |
| bpe_tokeniser              | 6.02 sec                                                 | 5.28 sec: 1.14x faster                                                          |
| nbody                      | 118 ms                                                   | 106 ms: 1.12x faster                                                            |
| sqlite_synth               | 4.08 us                                                  | 3.65 us: 1.12x faster                                                           |
| generators                 | 40.3 ms                                                  | 36.2 ms: 1.12x faster                                                           |
| go                         | 164 ms                                                   | 147 ms: 1.11x faster                                                            |
| pyflate                    | 582 ms                                                   | 524 ms: 1.11x faster                                                            |
| xml_etree_parse            | 203 ms                                                   | 183 ms: 1.11x faster                                                            |
| logging_format             | 8.10 us                                                  | 7.32 us: 1.11x faster                                                           |
| xml_etree_iterparse        | 159 ms                                                   | 144 ms: 1.10x faster                                                            |
| regex_compile              | 134 ms                                                   | 122 ms: 1.10x faster                                                            |
| logging_simple             | 7.25 us                                                  | 6.63 us: 1.09x faster                                                           |
| xml_etree_generate         | 118 ms                                                   | 108 ms: 1.09x faster                                                            |
| mako                       | 14.0 ms                                                  | 12.8 ms: 1.09x faster                                                           |
| scimark_monte_carlo        | 87.8 ms                                                  | 81.4 ms: 1.08x faster                                                           |
| xml_etree_process          | 82.1 ms                                                  | 76.3 ms: 1.08x faster                                                           |
| k_core                     | 2.99 sec                                                 | 2.79 sec: 1.07x faster                                                          |
| html5lib                   | 65.6 ms                                                  | 61.7 ms: 1.06x faster                                                           |
| python_startup             | 16.0 ms                                                  | 15.1 ms: 1.06x faster                                                           |
| genshi_text                | 28.6 ms                                                  | 27.0 ms: 1.06x faster                                                           |
| hexiom                     | 7.34 ms                                                  | 7.03 ms: 1.04x faster                                                           |
| sphinx                     | 1.20 sec                                                 | 1.15 sec: 1.04x faster                                                          |
| python_startup_no_site     | 8.79 ms                                                  | 8.61 ms: 1.02x faster                                                           |
| django_template            | 39.4 ms                                                  | 38.6 ms: 1.02x faster                                                           |
| djangocms                  | 66.2 us                                                  | 65.0 us: 1.02x faster                                                           |
| connected_components       | 547 ms                                                   | 555 ms: 1.02x slower                                                            |
| shortest_path              | 565 ms                                                   | 579 ms: 1.02x slower                                                            |
| docutils                   | 2.96 sec                                                 | 3.08 sec: 1.04x slower                                                          |
| genshi_xml                 | 61.6 ms                                                  | 64.1 ms: 1.04x slower                                                           |
| sympy_str                  | 265 ms                                                   | 280 ms: 1.06x slower                                                            |
| comprehensions             | 20.8 us                                                  | 22.1 us: 1.06x slower                                                           |
| typing_runtime_protocols   | 197 us                                                   | 209 us: 1.06x slower                                                            |
| crypto_pyaes               | 84.9 ms                                                  | 90.3 ms: 1.06x slower                                                           |
| raytrace                   | 310 ms                                                   | 336 ms: 1.08x slower                                                            |
| create_gc_cycles           | 3.39 ms                                                  | 3.86 ms: 1.14x slower                                                           |
| pprint_pformat             | 1.99 sec                                                 | 2.30 sec: 1.16x slower                                                          |
| gc_traversal               | 5.92 ms                                                  | 6.96 ms: 1.17x slower                                                           |
| pprint_safe_repr           | 962 ms                                                   | 1.13 sec: 1.18x slower                                                          |
| many_optionals             | 626 us                                                   | 999 us: 1.59x slower                                                            |
| subparsers                 | 20.3 ms                                                  | 49.2 ms: 2.42x slower                                                           |
| telco                      | 10.5 ms                                                  | 166 ms: 15.83x slower                                                           |
| Geometric mean             | (ref)                                                    | 1.03x faster                                                                    |

Benchmark hidden because not significant (25): unpickle_pure_python, pylint, pathlib, nqueens, deltablue, meteor_contest, fannkuch, json, chaos, logging_silent, thrift, coverage, sympy_sum, async_generators, 2to3, asyncio_websockets, pidigits, pycparser, json_loads, sympy_integrate, scimark_lu, sympy_expand, pickle_pure_python, scimark_sparse_mat_mult, coroutines
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250822-3.15.0a0-efe4628-JIT/bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.023x faster

# HPT report

- Reliability score: 99.71% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.11x