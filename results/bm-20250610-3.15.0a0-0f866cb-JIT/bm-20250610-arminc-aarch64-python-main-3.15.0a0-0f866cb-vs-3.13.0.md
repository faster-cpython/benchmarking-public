# Results vs. 3.13.0

- fork: python
- ref: main
- machine: linux-aarch64
- commit hash: 0f866cb
- commit date: 2025-06-10
- overall geometric mean: 1.039x slower
- HPT reliability: 94.29%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-arminc-aarch64-python-main-3.15.0a0-0f866cb |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.09 sec: 1.04x slower                                  |
| html5lib       | 65.6 ms                                                  | 63.2 ms: 1.04x faster                                   |
| sphinx         | 1.20 sec                                                 | 1.15 sec: 1.05x faster                                  |
| Geometric mean | (ref)                                                    | 1.01x faster                                            |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-arminc-aarch64-python-main-3.15.0a0-0f866cb |
|----------------------------|:--------------------------------------------------------:|:-------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 476 ms: 1.39x faster                                    |
| async_tree_memoization     | 664 ms                                                   | 478 ms: 1.39x faster                                    |
| async_tree_io              | 1.14 sec                                                 | 897 ms: 1.27x faster                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 925 ms: 1.26x faster                                    |
| async_tree_none            | 504 ms                                                   | 400 ms: 1.26x faster                                    |
| async_tree_none_tg         | 484 ms                                                   | 385 ms: 1.26x faster                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 669 ms: 1.20x faster                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 666 ms: 1.19x faster                                    |
| async_generators           | 500 ms                                                   | 475 ms: 1.05x faster                                    |
| Geometric mean             | (ref)                                                    | 1.20x faster                                            |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-arminc-aarch64-python-main-3.15.0a0-0f866cb |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------:|
| float          | 95.8 ms                                                  | 82.8 ms: 1.16x faster                                   |
| Geometric mean | (ref)                                                    | 1.05x faster                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-arminc-aarch64-python-main-3.15.0a0-0f866cb |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.02 ms: 1.27x faster                                   |
| regex_v8       | 32.5 ms                                                  | 27.1 ms: 1.20x faster                                   |
| regex_dna      | 263 ms                                                   | 223 ms: 1.18x faster                                    |
| regex_compile  | 134 ms                                                   | 122 ms: 1.10x faster                                    |
| Geometric mean | (ref)                                                    | 1.18x faster                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-arminc-aarch64-python-main-3.15.0a0-0f866cb |
|----------------------|:--------------------------------------------------------:|:-------------------------------------------------------:|
| xml_etree_parse      | 203 ms                                                   | 179 ms: 1.13x faster                                    |
| tomli_loads          | 2.67 sec                                                 | 2.37 sec: 1.13x faster                                  |
| xml_etree_iterparse  | 159 ms                                                   | 143 ms: 1.11x faster                                    |
| xml_etree_generate   | 118 ms                                                   | 110 ms: 1.08x faster                                    |
| unpickle_pure_python | 265 us                                                   | 248 us: 1.07x faster                                    |
| Geometric mean       | (ref)                                                    | 1.06x faster                                            |

Benchmark hidden because not significant (4): xml_etree_process, json_dumps, json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-arminc-aarch64-python-main-3.15.0a0-0f866cb |
|------------------------|:--------------------------------------------------------:|:-------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 15.1 ms: 1.06x faster                                   |
| python_startup_no_site | 8.79 ms                                                  | 8.62 ms: 1.02x faster                                   |
| Geometric mean         | (ref)                                                    | 1.04x faster                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-arminc-aarch64-python-main-3.15.0a0-0f866cb |
|-----------------|:--------------------------------------------------------:|:-------------------------------------------------------:|
| genshi_xml      | 61.6 ms                                                  | 63.4 ms: 1.03x slower                                   |
| django_template | 39.4 ms                                                  | 41.7 ms: 1.06x slower                                   |
| Geometric mean  | (ref)                                                    | 1.01x slower                                            |

Benchmark hidden because not significant (2): genshi_text, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-arminc-aarch64-python-main-3.15.0a0-0f866cb |
|----------------------------|:--------------------------------------------------------:|:-------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.68 sec: 2.05x faster                                  |
| async_tree_memoization_tg  | 663 ms                                                   | 476 ms: 1.39x faster                                    |
| deepcopy                   | 479 us                                                   | 345 us: 1.39x faster                                    |
| async_tree_memoization     | 664 ms                                                   | 478 ms: 1.39x faster                                    |
| deepcopy_memo              | 53.0 us                                                  | 38.2 us: 1.39x faster                                   |
| async_tree_io              | 1.14 sec                                                 | 897 ms: 1.27x faster                                    |
| regex_effbot               | 5.10 ms                                                  | 4.02 ms: 1.27x faster                                   |
| async_tree_io_tg           | 1.16 sec                                                 | 925 ms: 1.26x faster                                    |
| async_tree_none            | 504 ms                                                   | 400 ms: 1.26x faster                                    |
| async_tree_none_tg         | 484 ms                                                   | 385 ms: 1.26x faster                                    |
| richards                   | 54.5 ms                                                  | 44.7 ms: 1.22x faster                                   |
| regex_v8                   | 32.5 ms                                                  | 27.1 ms: 1.20x faster                                   |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 669 ms: 1.20x faster                                    |
| richards_super             | 60.8 ms                                                  | 51.1 ms: 1.19x faster                                   |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 666 ms: 1.19x faster                                    |
| regex_dna                  | 263 ms                                                   | 223 ms: 1.18x faster                                    |
| deepcopy_reduce            | 4.24 us                                                  | 3.63 us: 1.17x faster                                   |
| float                      | 95.8 ms                                                  | 82.8 ms: 1.16x faster                                   |
| xml_etree_parse            | 203 ms                                                   | 179 ms: 1.13x faster                                    |
| scimark_sor                | 164 ms                                                   | 145 ms: 1.13x faster                                    |
| tomli_loads                | 2.67 sec                                                 | 2.37 sec: 1.13x faster                                  |
| generators                 | 40.3 ms                                                  | 35.9 ms: 1.12x faster                                   |
| xml_etree_iterparse        | 159 ms                                                   | 143 ms: 1.11x faster                                    |
| telco                      | 10.5 ms                                                  | 9.45 ms: 1.11x faster                                   |
| bpe_tokeniser              | 6.02 sec                                                 | 5.45 sec: 1.10x faster                                  |
| sqlite_synth               | 4.08 us                                                  | 3.71 us: 1.10x faster                                   |
| regex_compile              | 134 ms                                                   | 122 ms: 1.10x faster                                    |
| scimark_fft                | 463 ms                                                   | 424 ms: 1.09x faster                                    |
| xml_etree_generate         | 118 ms                                                   | 110 ms: 1.08x faster                                    |
| spectral_norm              | 143 ms                                                   | 134 ms: 1.07x faster                                    |
| pylint                     | 345 ms                                                   | 322 ms: 1.07x faster                                    |
| unpickle_pure_python       | 265 us                                                   | 248 us: 1.07x faster                                    |
| python_startup             | 16.0 ms                                                  | 15.1 ms: 1.06x faster                                   |
| pyflate                    | 582 ms                                                   | 549 ms: 1.06x faster                                    |
| k_core                     | 2.99 sec                                                 | 2.82 sec: 1.06x faster                                  |
| async_generators           | 500 ms                                                   | 475 ms: 1.05x faster                                    |
| sphinx                     | 1.20 sec                                                 | 1.15 sec: 1.05x faster                                  |
| html5lib                   | 65.6 ms                                                  | 63.2 ms: 1.04x faster                                   |
| go                         | 164 ms                                                   | 159 ms: 1.03x faster                                    |
| python_startup_no_site     | 8.79 ms                                                  | 8.62 ms: 1.02x faster                                   |
| connected_components       | 547 ms                                                   | 561 ms: 1.03x slower                                    |
| genshi_xml                 | 61.6 ms                                                  | 63.4 ms: 1.03x slower                                   |
| sympy_expand               | 472 ms                                                   | 490 ms: 1.04x slower                                    |
| shortest_path              | 565 ms                                                   | 587 ms: 1.04x slower                                    |
| pycparser                  | 1.34 sec                                                 | 1.40 sec: 1.04x slower                                  |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 6.93 ms: 1.04x slower                                   |
| docutils                   | 2.96 sec                                                 | 3.09 sec: 1.04x slower                                  |
| logging_simple             | 7.25 us                                                  | 7.57 us: 1.04x slower                                   |
| django_template            | 39.4 ms                                                  | 41.7 ms: 1.06x slower                                   |
| sympy_str                  | 265 ms                                                   | 284 ms: 1.07x slower                                    |
| raytrace                   | 310 ms                                                   | 336 ms: 1.08x slower                                    |
| comprehensions             | 20.8 us                                                  | 22.7 us: 1.09x slower                                   |
| crypto_pyaes               | 84.9 ms                                                  | 92.8 ms: 1.09x slower                                   |
| create_gc_cycles           | 3.39 ms                                                  | 3.76 ms: 1.11x slower                                   |
| gc_traversal               | 5.92 ms                                                  | 7.06 ms: 1.19x slower                                   |
| many_optionals             | 626 us                                                   | 803 us: 1.28x slower                                    |
| pprint_safe_repr           | 962 ms                                                   | 1.25 sec: 1.30x slower                                  |
| pprint_pformat             | 1.99 sec                                                 | 2.58 sec: 1.30x slower                                  |
| subparsers                 | 20.3 ms                                                  | 28.4 ms: 1.39x slower                                   |
| logging_silent             | 135 ns                                                   | 606 ns: 4.50x slower                                    |
| coverage                   | 106 ms                                                   | 554 ms: 5.24x slower                                    |
| thrift                     | 1.01 ms                                                  | 191 ms: 188.52x slower                                  |
| Geometric mean             | (ref)                                                    | 1.05x slower                                            |

Benchmark hidden because not significant (25): scimark_monte_carlo, json, xml_etree_process, nqueens, pathlib, genshi_text, mako, json_dumps, sympy_integrate, pidigits, asyncio_websockets, meteor_contest, 2to3, json_loads, chaos, coroutines, deltablue, nbody, fannkuch, sympy_sum, hexiom, logging_format, pickle_pure_python, typing_runtime_protocols, scimark_lu
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250610-3.15.0a0-0f866cb-JIT/bm-20250610-arminc-aarch64-python-main-3.15.0a0-0f866cb.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.039x slower

# HPT report

- Reliability score: 94.29% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x