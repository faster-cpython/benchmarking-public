# Results vs. 3.13.0

- fork: diegorusso
- ref: remove_jumps_aarch64
- machine: linux-aarch64
- commit hash: 460d0d3
- commit date: 2025-03-10
- overall geometric mean: 1.053x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250310-arminc-aarch64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 300 ms: 1.04x faster                                                         |
| docutils       | 2.96 sec                                                 | 3.07 sec: 1.03x slower                                                       |
| html5lib       | 65.6 ms                                                  | 61.5 ms: 1.07x faster                                                        |
| sphinx         | 1.20 sec                                                 | 1.14 sec: 1.05x faster                                                       |
| Geometric mean | (ref)                                                    | 1.03x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250310-arminc-aarch64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|----------------------------|:--------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization     | 664 ms                                                   | 465 ms: 1.43x faster                                                         |
| async_tree_memoization_tg  | 663 ms                                                   | 471 ms: 1.41x faster                                                         |
| async_tree_none            | 504 ms                                                   | 380 ms: 1.33x faster                                                         |
| async_tree_io_tg           | 1.16 sec                                                 | 883 ms: 1.32x faster                                                         |
| async_tree_none_tg         | 484 ms                                                   | 369 ms: 1.31x faster                                                         |
| async_tree_io              | 1.14 sec                                                 | 870 ms: 1.31x faster                                                         |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 644 ms: 1.24x faster                                                         |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 652 ms: 1.21x faster                                                         |
| async_generators           | 500 ms                                                   | 458 ms: 1.09x faster                                                         |
| coroutines                 | 29.4 ms                                                  | 27.8 ms: 1.06x faster                                                        |
| Geometric mean             | (ref)                                                    | 1.24x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250310-arminc-aarch64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 82.7 ms: 1.16x faster                                                        |
| Geometric mean | (ref)                                                    | 1.06x faster                                                                 |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250310-arminc-aarch64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.92 ms: 1.30x faster                                                        |
| regex_v8       | 32.5 ms                                                  | 28.0 ms: 1.16x faster                                                        |
| regex_compile  | 134 ms                                                   | 122 ms: 1.10x faster                                                         |
| regex_dna      | 263 ms                                                   | 249 ms: 1.05x faster                                                         |
| Geometric mean | (ref)                                                    | 1.15x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250310-arminc-aarch64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|---------------------|:--------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads         | 2.67 sec                                                 | 2.31 sec: 1.16x faster                                                       |
| xml_etree_parse     | 203 ms                                                   | 175 ms: 1.15x faster                                                         |
| xml_etree_iterparse | 159 ms                                                   | 142 ms: 1.12x faster                                                         |
| xml_etree_generate  | 118 ms                                                   | 108 ms: 1.10x faster                                                         |
| xml_etree_process   | 82.1 ms                                                  | 76.3 ms: 1.08x faster                                                        |
| Geometric mean      | (ref)                                                    | 1.06x faster                                                                 |

Benchmark hidden because not significant (4): unpickle_pure_python, json_dumps, json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250310-arminc-aarch64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|------------------------|:--------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 10.1 ms: 1.15x slower                                                        |
| Geometric mean         | (ref)                                                    | 1.08x slower                                                                 |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250310-arminc-aarch64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|-----------------|:--------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.0 ms                                                  | 12.5 ms: 1.12x faster                                                        |
| genshi_text     | 28.6 ms                                                  | 26.5 ms: 1.08x faster                                                        |
| genshi_xml      | 61.6 ms                                                  | 60.0 ms: 1.03x faster                                                        |
| django_template | 39.4 ms                                                  | 38.5 ms: 1.02x faster                                                        |
| Geometric mean  | (ref)                                                    | 1.06x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250310-arminc-aarch64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|----------------------------|:--------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy                   | 479 us                                                   | 330 us: 1.45x faster                                                         |
| async_tree_memoization     | 664 ms                                                   | 465 ms: 1.43x faster                                                         |
| async_tree_memoization_tg  | 663 ms                                                   | 471 ms: 1.41x faster                                                         |
| deepcopy_memo              | 53.0 us                                                  | 37.6 us: 1.41x faster                                                        |
| async_tree_none            | 504 ms                                                   | 380 ms: 1.33x faster                                                         |
| async_tree_io_tg           | 1.16 sec                                                 | 883 ms: 1.32x faster                                                         |
| async_tree_none_tg         | 484 ms                                                   | 369 ms: 1.31x faster                                                         |
| async_tree_io              | 1.14 sec                                                 | 870 ms: 1.31x faster                                                         |
| regex_effbot               | 5.10 ms                                                  | 3.92 ms: 1.30x faster                                                        |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 644 ms: 1.24x faster                                                         |
| deepcopy_reduce            | 4.24 us                                                  | 3.42 us: 1.24x faster                                                        |
| spectral_norm              | 143 ms                                                   | 117 ms: 1.22x faster                                                         |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 652 ms: 1.21x faster                                                         |
| scimark_fft                | 463 ms                                                   | 385 ms: 1.20x faster                                                         |
| richards                   | 54.5 ms                                                  | 45.7 ms: 1.19x faster                                                        |
| richards_super             | 60.8 ms                                                  | 51.7 ms: 1.18x faster                                                        |
| regex_v8                   | 32.5 ms                                                  | 28.0 ms: 1.16x faster                                                        |
| float                      | 95.8 ms                                                  | 82.7 ms: 1.16x faster                                                        |
| tomli_loads                | 2.67 sec                                                 | 2.31 sec: 1.16x faster                                                       |
| xml_etree_parse            | 203 ms                                                   | 175 ms: 1.15x faster                                                         |
| telco                      | 10.5 ms                                                  | 9.24 ms: 1.13x faster                                                        |
| generators                 | 40.3 ms                                                  | 35.7 ms: 1.13x faster                                                        |
| sqlite_synth               | 4.08 us                                                  | 3.63 us: 1.12x faster                                                        |
| xml_etree_iterparse        | 159 ms                                                   | 142 ms: 1.12x faster                                                         |
| mako                       | 14.0 ms                                                  | 12.5 ms: 1.12x faster                                                        |
| thrift                     | 1.01 ms                                                  | 906 us: 1.12x faster                                                         |
| pylint                     | 345 ms                                                   | 313 ms: 1.10x faster                                                         |
| bpe_tokeniser              | 6.02 sec                                                 | 5.45 sec: 1.10x faster                                                       |
| regex_compile              | 134 ms                                                   | 122 ms: 1.10x faster                                                         |
| xml_etree_generate         | 118 ms                                                   | 108 ms: 1.10x faster                                                         |
| scimark_sor                | 164 ms                                                   | 150 ms: 1.09x faster                                                         |
| async_generators           | 500 ms                                                   | 458 ms: 1.09x faster                                                         |
| coverage                   | 106 ms                                                   | 97.5 ms: 1.08x faster                                                        |
| genshi_text                | 28.6 ms                                                  | 26.5 ms: 1.08x faster                                                        |
| pyflate                    | 582 ms                                                   | 540 ms: 1.08x faster                                                         |
| xml_etree_process          | 82.1 ms                                                  | 76.3 ms: 1.08x faster                                                        |
| logging_format             | 8.10 us                                                  | 7.57 us: 1.07x faster                                                        |
| pathlib                    | 24.3 ms                                                  | 22.7 ms: 1.07x faster                                                        |
| html5lib                   | 65.6 ms                                                  | 61.5 ms: 1.07x faster                                                        |
| sqlalchemy_declarative     | 154 ms                                                   | 145 ms: 1.06x faster                                                         |
| scimark_lu                 | 146 ms                                                   | 138 ms: 1.06x faster                                                         |
| coroutines                 | 29.4 ms                                                  | 27.8 ms: 1.06x faster                                                        |
| logging_simple             | 7.25 us                                                  | 6.86 us: 1.06x faster                                                        |
| regex_dna                  | 263 ms                                                   | 249 ms: 1.05x faster                                                         |
| sphinx                     | 1.20 sec                                                 | 1.14 sec: 1.05x faster                                                       |
| chaos                      | 70.7 ms                                                  | 67.4 ms: 1.05x faster                                                        |
| k_core                     | 2.99 sec                                                 | 2.85 sec: 1.05x faster                                                       |
| fannkuch                   | 478 ms                                                   | 457 ms: 1.05x faster                                                         |
| mdp                        | 3.45 sec                                                 | 3.30 sec: 1.04x faster                                                       |
| 2to3                       | 313 ms                                                   | 300 ms: 1.04x faster                                                         |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 6.41 ms: 1.04x faster                                                        |
| genshi_xml                 | 61.6 ms                                                  | 60.0 ms: 1.03x faster                                                        |
| django_template            | 39.4 ms                                                  | 38.5 ms: 1.02x faster                                                        |
| sympy_str                  | 265 ms                                                   | 268 ms: 1.01x slower                                                         |
| connected_components       | 547 ms                                                   | 559 ms: 1.02x slower                                                         |
| hexiom                     | 7.34 ms                                                  | 7.57 ms: 1.03x slower                                                        |
| shortest_path              | 565 ms                                                   | 583 ms: 1.03x slower                                                         |
| typing_runtime_protocols   | 197 us                                                   | 204 us: 1.03x slower                                                         |
| docutils                   | 2.96 sec                                                 | 3.07 sec: 1.03x slower                                                       |
| create_gc_cycles           | 3.39 ms                                                  | 3.73 ms: 1.10x slower                                                        |
| crypto_pyaes               | 84.9 ms                                                  | 93.5 ms: 1.10x slower                                                        |
| gc_traversal               | 5.92 ms                                                  | 6.57 ms: 1.11x slower                                                        |
| comprehensions             | 20.8 us                                                  | 23.4 us: 1.13x slower                                                        |
| python_startup_no_site     | 8.79 ms                                                  | 10.1 ms: 1.15x slower                                                        |
| pprint_safe_repr           | 962 ms                                                   | 1.11 sec: 1.15x slower                                                       |
| pprint_pformat             | 1.99 sec                                                 | 2.31 sec: 1.16x slower                                                       |
| subparsers                 | 20.3 ms                                                  | 25.4 ms: 1.25x slower                                                        |
| many_optionals             | 626 us                                                   | 837 us: 1.34x slower                                                         |
| bench_mp_pool              | 8.07 ms                                                  | 2.82 sec: 349.69x slower                                                     |
| Geometric mean             | (ref)                                                    | 1.00x slower                                                                 |

Benchmark hidden because not significant (22): scimark_monte_carlo, unpickle_pure_python, deltablue, sqlalchemy_imperative, sympy_sum, json, nqueens, logging_silent, asyncio_websockets, go, nbody, sympy_expand, pycparser, pidigits, sympy_integrate, json_dumps, python_startup, meteor_contest, bench_thread_pool, raytrace, json_loads, pickle_pure_python
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250310-3.14.0a5+-460d0d3-JIT/bm-20250310-arminc-aarch64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.053x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x