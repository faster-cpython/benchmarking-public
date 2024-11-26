# Results vs. 3.13.0

- fork: nick-arm
- ref: codecache
- machine: linux-aarch64
- commit hash: 0be1ef3
- commit date: 2024-10-21
- overall geometric mean: 1.091x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-arminc-aarch64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 375 ms: 1.23x slower                                              |
| docutils       | 2.89 sec                                                 | 3.55 sec: 1.23x slower                                            |
| html5lib       | 66.4 ms                                                  | 72.7 ms: 1.10x slower                                             |
| sphinx         | 1.17 sec                                                 | 1.42 sec: 1.22x slower                                            |
| tornado_http   | 128 ms                                                   | 150 ms: 1.17x slower                                              |
| Geometric mean | (ref)                                                    | 1.19x slower                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-arminc-aarch64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 547 ms: 1.19x faster                                              |
| async_tree_memoization     | 651 ms                                                   | 607 ms: 1.07x faster                                              |
| async_tree_none            | 497 ms                                                   | 473 ms: 1.05x faster                                              |
| async_tree_none_tg         | 470 ms                                                   | 453 ms: 1.04x faster                                              |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 744 ms: 1.03x faster                                              |
| async_generators           | 489 ms                                                   | 511 ms: 1.05x slower                                              |
| async_tree_io              | 1.11 sec                                                 | 1.17 sec: 1.05x slower                                            |
| async_tree_io_tg           | 1.13 sec                                                 | 1.27 sec: 1.12x slower                                            |
| Geometric mean             | (ref)                                                    | 1.01x faster                                                      |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-arminc-aarch64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 93.3 ms                                                  | 97.7 ms: 1.05x slower                                             |
| Geometric mean | (ref)                                                    | 1.02x slower                                                      |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-arminc-aarch64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 31.2 ms: 1.02x faster                                             |
| regex_dna      | 253 ms                                                   | 249 ms: 1.02x faster                                              |
| regex_effbot   | 4.89 ms                                                  | 5.06 ms: 1.03x slower                                             |
| regex_compile  | 127 ms                                                   | 172 ms: 1.35x slower                                              |
| Geometric mean | (ref)                                                    | 1.08x slower                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-arminc-aarch64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------:|
| xml_etree_parse      | 197 ms                                                   | 189 ms: 1.04x faster                                              |
| tomli_loads          | 2.54 sec                                                 | 2.62 sec: 1.03x slower                                            |
| json_dumps           | 13.6 ms                                                  | 14.2 ms: 1.05x slower                                             |
| unpickle_pure_python | 251 us                                                   | 266 us: 1.06x slower                                              |
| pickle_pure_python   | 357 us                                                   | 389 us: 1.09x slower                                              |
| Geometric mean       | (ref)                                                    | 1.02x slower                                                      |

Benchmark hidden because not significant (4): xml_etree_generate, xml_etree_iterparse, json_loads, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-arminc-aarch64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 14.6 ms: 1.06x faster                                             |
| Geometric mean | (ref)                                                    | 1.02x faster                                                      |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-arminc-aarch64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 13.4 ms                                                  | 13.2 ms: 1.01x faster                                             |
| django_template | 41.6 ms                                                  | 52.3 ms: 1.25x slower                                             |
| genshi_text     | 27.7 ms                                                  | 34.9 ms: 1.26x slower                                             |
| genshi_xml      | 60.3 ms                                                  | 82.5 ms: 1.37x slower                                             |
| Geometric mean  | (ref)                                                    | 1.21x slower                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-arminc-aarch64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------:|
| deepcopy_memo              | 50.4 us                                                  | 39.2 us: 1.28x faster                                             |
| deepcopy                   | 447 us                                                   | 374 us: 1.20x faster                                              |
| async_tree_memoization_tg  | 649 ms                                                   | 547 ms: 1.19x faster                                              |
| async_tree_memoization     | 651 ms                                                   | 607 ms: 1.07x faster                                              |
| python_startup             | 15.4 ms                                                  | 14.6 ms: 1.06x faster                                             |
| deepcopy_reduce            | 4.07 us                                                  | 3.87 us: 1.05x faster                                             |
| async_tree_none            | 497 ms                                                   | 473 ms: 1.05x faster                                              |
| pathlib                    | 22.7 ms                                                  | 21.8 ms: 1.04x faster                                             |
| xml_etree_parse            | 197 ms                                                   | 189 ms: 1.04x faster                                              |
| async_tree_none_tg         | 470 ms                                                   | 453 ms: 1.04x faster                                              |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 744 ms: 1.03x faster                                              |
| regex_v8                   | 31.8 ms                                                  | 31.2 ms: 1.02x faster                                             |
| telco                      | 9.74 ms                                                  | 9.56 ms: 1.02x faster                                             |
| regex_dna                  | 253 ms                                                   | 249 ms: 1.02x faster                                              |
| mako                       | 13.4 ms                                                  | 13.2 ms: 1.01x faster                                             |
| scimark_fft                | 447 ms                                                   | 454 ms: 1.02x slower                                              |
| bpe_tokeniser              | 5.87 sec                                                 | 6.01 sec: 1.02x slower                                            |
| tomli_loads                | 2.54 sec                                                 | 2.62 sec: 1.03x slower                                            |
| regex_effbot               | 4.89 ms                                                  | 5.06 ms: 1.03x slower                                             |
| mdp                        | 3.34 sec                                                 | 3.48 sec: 1.04x slower                                            |
| async_generators           | 489 ms                                                   | 511 ms: 1.05x slower                                              |
| float                      | 93.3 ms                                                  | 97.7 ms: 1.05x slower                                             |
| json_dumps                 | 13.6 ms                                                  | 14.2 ms: 1.05x slower                                             |
| async_tree_io              | 1.11 sec                                                 | 1.17 sec: 1.05x slower                                            |
| logging_format             | 7.82 us                                                  | 8.26 us: 1.06x slower                                             |
| unpickle_pure_python       | 251 us                                                   | 266 us: 1.06x slower                                              |
| crypto_pyaes               | 83.7 ms                                                  | 89.3 ms: 1.07x slower                                             |
| spectral_norm              | 143 ms                                                   | 154 ms: 1.08x slower                                              |
| logging_simple             | 7.07 us                                                  | 7.65 us: 1.08x slower                                             |
| create_gc_cycles           | 3.35 ms                                                  | 3.62 ms: 1.08x slower                                             |
| bench_thread_pool          | 1.27 ms                                                  | 1.38 ms: 1.08x slower                                             |
| scimark_lu                 | 139 ms                                                   | 151 ms: 1.08x slower                                              |
| scimark_monte_carlo        | 83.6 ms                                                  | 90.6 ms: 1.08x slower                                             |
| meteor_contest             | 114 ms                                                   | 123 ms: 1.09x slower                                              |
| pickle_pure_python         | 357 us                                                   | 389 us: 1.09x slower                                              |
| scimark_sparse_mat_mult    | 6.51 ms                                                  | 7.13 ms: 1.09x slower                                             |
| html5lib                   | 66.4 ms                                                  | 72.7 ms: 1.10x slower                                             |
| typing_runtime_protocols   | 193 us                                                   | 212 us: 1.10x slower                                              |
| gc_traversal               | 5.77 ms                                                  | 6.37 ms: 1.10x slower                                             |
| pyflate                    | 556 ms                                                   | 616 ms: 1.11x slower                                              |
| fannkuch                   | 461 ms                                                   | 515 ms: 1.12x slower                                              |
| async_tree_io_tg           | 1.13 sec                                                 | 1.27 sec: 1.12x slower                                            |
| richards_super             | 60.1 ms                                                  | 67.5 ms: 1.12x slower                                             |
| richards                   | 53.6 ms                                                  | 61.1 ms: 1.14x slower                                             |
| tornado_http               | 128 ms                                                   | 150 ms: 1.17x slower                                              |
| pycparser                  | 1.27 sec                                                 | 1.49 sec: 1.17x slower                                            |
| go                         | 160 ms                                                   | 188 ms: 1.17x slower                                              |
| raytrace                   | 300 ms                                                   | 353 ms: 1.18x slower                                              |
| sqlglot_normalize          | 127 ms                                                   | 153 ms: 1.21x slower                                              |
| comprehensions             | 20.4 us                                                  | 24.7 us: 1.21x slower                                             |
| sphinx                     | 1.17 sec                                                 | 1.42 sec: 1.22x slower                                            |
| deltablue                  | 3.82 ms                                                  | 4.66 ms: 1.22x slower                                             |
| docutils                   | 2.89 sec                                                 | 3.55 sec: 1.23x slower                                            |
| 2to3                       | 304 ms                                                   | 375 ms: 1.23x slower                                              |
| sqlglot_transpile          | 1.73 ms                                                  | 2.16 ms: 1.25x slower                                             |
| django_template            | 41.6 ms                                                  | 52.3 ms: 1.25x slower                                             |
| genshi_text                | 27.7 ms                                                  | 34.9 ms: 1.26x slower                                             |
| sqlglot_parse              | 1.38 ms                                                  | 1.73 ms: 1.26x slower                                             |
| chaos                      | 68.0 ms                                                  | 86.8 ms: 1.28x slower                                             |
| nqueens                    | 100 ms                                                   | 128 ms: 1.28x slower                                              |
| sqlglot_optimize           | 62.2 ms                                                  | 79.9 ms: 1.28x slower                                             |
| sympy_expand               | 457 ms                                                   | 588 ms: 1.29x slower                                              |
| pprint_safe_repr           | 926 ms                                                   | 1.20 sec: 1.30x slower                                            |
| sympy_str                  | 264 ms                                                   | 353 ms: 1.33x slower                                              |
| pylint                     | 342 ms                                                   | 458 ms: 1.34x slower                                              |
| pprint_pformat             | 1.90 sec                                                 | 2.55 sec: 1.35x slower                                            |
| regex_compile              | 127 ms                                                   | 172 ms: 1.35x slower                                              |
| genshi_xml                 | 60.3 ms                                                  | 82.5 ms: 1.37x slower                                             |
| hexiom                     | 7.11 ms                                                  | 10.1 ms: 1.42x slower                                             |
| sympy_integrate            | 20.8 ms                                                  | 29.7 ms: 1.43x slower                                             |
| sympy_sum                  | 144 ms                                                   | 214 ms: 1.49x slower                                              |
| generators                 | 37.6 ms                                                  | 60.0 ms: 1.59x slower                                             |
| bench_mp_pool              | 7.68 ms                                                  | 2.50 sec: 324.83x slower                                          |
| Geometric mean             | (ref)                                                    | 1.17x slower                                                      |

Benchmark hidden because not significant (15): json, async_tree_cpu_io_mixed, xml_etree_generate, scimark_sor, logging_silent, xml_etree_iterparse, coverage, nbody, pidigits, json_loads, asyncio_websockets, python_startup_no_site, thrift, coroutines, xml_etree_process
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of results/bm-20241021-3.14.0a1+-0be1ef3-JIT/bm-20241021-arminc-aarch64-nick%2darm-codecache-3.14.0a1+-0be1ef3.json: dulwich_log

- Geometric mean (including insignificant results): 1.091x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 1.10x