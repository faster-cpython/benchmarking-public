# Results vs. 3.13.0

- fork: mdboom
- ref: python_startup_time
- machine: linux-aarch64
- commit hash: 9fc1238
- commit date: 2025-04-25
- overall geometric mean: 1.069x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-arminc-aarch64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 298 ms: 1.05x faster                                                    |
| html5lib       | 65.6 ms                                                  | 61.5 ms: 1.07x faster                                                   |
| sphinx         | 1.20 sec                                                 | 1.15 sec: 1.04x faster                                                  |
| Geometric mean | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-arminc-aarch64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 664 ms                                                   | 464 ms: 1.43x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 466 ms: 1.42x faster                                                    |
| async_tree_none            | 504 ms                                                   | 386 ms: 1.31x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 373 ms: 1.30x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 902 ms: 1.29x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 892 ms: 1.28x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 649 ms: 1.23x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 662 ms: 1.19x faster                                                    |
| async_generators           | 500 ms                                                   | 446 ms: 1.12x faster                                                    |
| Geometric mean             | (ref)                                                    | 1.22x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-arminc-aarch64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 83.3 ms: 1.15x faster                                                   |
| Geometric mean | (ref)                                                    | 1.05x faster                                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-arminc-aarch64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.84 ms: 1.33x faster                                                   |
| regex_v8       | 32.5 ms                                                  | 27.7 ms: 1.18x faster                                                   |
| regex_compile  | 134 ms                                                   | 120 ms: 1.11x faster                                                    |
| regex_dna      | 263 ms                                                   | 236 ms: 1.11x faster                                                    |
| Geometric mean | (ref)                                                    | 1.18x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-arminc-aarch64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 179 ms: 1.13x faster                                                    |
| xml_etree_iterparse | 159 ms                                                   | 141 ms: 1.13x faster                                                    |
| tomli_loads         | 2.67 sec                                                 | 2.44 sec: 1.09x faster                                                  |
| xml_etree_generate  | 118 ms                                                   | 112 ms: 1.06x faster                                                    |
| Geometric mean      | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (5): json_dumps, xml_etree_process, unpickle_pure_python, pickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-arminc-aarch64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 9.08 ms: 1.03x slower                                                   |
| Geometric mean         | (ref)                                                    | 1.03x slower                                                            |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-arminc-aarch64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text    | 28.6 ms                                                  | 26.0 ms: 1.10x faster                                                   |
| Geometric mean | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (3): mako, genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-arminc-aarch64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.62 sec: 2.12x faster                                                  |
| deepcopy                   | 479 us                                                   | 330 us: 1.45x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 464 ms: 1.43x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 466 ms: 1.42x faster                                                    |
| deepcopy_memo              | 53.0 us                                                  | 38.2 us: 1.39x faster                                                   |
| regex_effbot               | 5.10 ms                                                  | 3.84 ms: 1.33x faster                                                   |
| async_tree_none            | 504 ms                                                   | 386 ms: 1.31x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 373 ms: 1.30x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 902 ms: 1.29x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 892 ms: 1.28x faster                                                    |
| go                         | 164 ms                                                   | 131 ms: 1.25x faster                                                    |
| deepcopy_reduce            | 4.24 us                                                  | 3.40 us: 1.25x faster                                                   |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 649 ms: 1.23x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 662 ms: 1.19x faster                                                    |
| regex_v8                   | 32.5 ms                                                  | 27.7 ms: 1.18x faster                                                   |
| spectral_norm              | 143 ms                                                   | 123 ms: 1.17x faster                                                    |
| float                      | 95.8 ms                                                  | 83.3 ms: 1.15x faster                                                   |
| xml_etree_parse            | 203 ms                                                   | 179 ms: 1.13x faster                                                    |
| xml_etree_iterparse        | 159 ms                                                   | 141 ms: 1.13x faster                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 5.35 sec: 1.12x faster                                                  |
| async_generators           | 500 ms                                                   | 446 ms: 1.12x faster                                                    |
| telco                      | 10.5 ms                                                  | 9.32 ms: 1.12x faster                                                   |
| scimark_fft                | 463 ms                                                   | 413 ms: 1.12x faster                                                    |
| scimark_monte_carlo        | 87.8 ms                                                  | 78.5 ms: 1.12x faster                                                   |
| pyflate                    | 582 ms                                                   | 521 ms: 1.12x faster                                                    |
| regex_compile              | 134 ms                                                   | 120 ms: 1.11x faster                                                    |
| regex_dna                  | 263 ms                                                   | 236 ms: 1.11x faster                                                    |
| pylint                     | 345 ms                                                   | 312 ms: 1.11x faster                                                    |
| scimark_sor                | 164 ms                                                   | 148 ms: 1.11x faster                                                    |
| generators                 | 40.3 ms                                                  | 36.5 ms: 1.11x faster                                                   |
| genshi_text                | 28.6 ms                                                  | 26.0 ms: 1.10x faster                                                   |
| tomli_loads                | 2.67 sec                                                 | 2.44 sec: 1.09x faster                                                  |
| nqueens                    | 105 ms                                                   | 96.3 ms: 1.09x faster                                                   |
| pycparser                  | 1.34 sec                                                 | 1.24 sec: 1.08x faster                                                  |
| sqlite_synth               | 4.08 us                                                  | 3.80 us: 1.08x faster                                                   |
| k_core                     | 2.99 sec                                                 | 2.79 sec: 1.07x faster                                                  |
| pprint_safe_repr           | 962 ms                                                   | 898 ms: 1.07x faster                                                    |
| sympy_integrate            | 21.4 ms                                                  | 20.0 ms: 1.07x faster                                                   |
| pathlib                    | 24.3 ms                                                  | 22.8 ms: 1.07x faster                                                   |
| html5lib                   | 65.6 ms                                                  | 61.5 ms: 1.07x faster                                                   |
| pprint_pformat             | 1.99 sec                                                 | 1.87 sec: 1.06x faster                                                  |
| chaos                      | 70.7 ms                                                  | 66.5 ms: 1.06x faster                                                   |
| xml_etree_generate         | 118 ms                                                   | 112 ms: 1.06x faster                                                    |
| logging_format             | 8.10 us                                                  | 7.67 us: 1.06x faster                                                   |
| logging_simple             | 7.25 us                                                  | 6.90 us: 1.05x faster                                                   |
| 2to3                       | 313 ms                                                   | 298 ms: 1.05x faster                                                    |
| logging_silent             | 135 ns                                                   | 129 ns: 1.04x faster                                                    |
| sphinx                     | 1.20 sec                                                 | 1.15 sec: 1.04x faster                                                  |
| sympy_expand               | 472 ms                                                   | 454 ms: 1.04x faster                                                    |
| sympy_str                  | 265 ms                                                   | 258 ms: 1.03x faster                                                    |
| connected_components       | 547 ms                                                   | 559 ms: 1.02x slower                                                    |
| shortest_path              | 565 ms                                                   | 579 ms: 1.02x slower                                                    |
| python_startup_no_site     | 8.79 ms                                                  | 9.08 ms: 1.03x slower                                                   |
| raytrace                   | 310 ms                                                   | 325 ms: 1.05x slower                                                    |
| create_gc_cycles           | 3.39 ms                                                  | 3.58 ms: 1.06x slower                                                   |
| gc_traversal               | 5.92 ms                                                  | 6.59 ms: 1.11x slower                                                   |
| subparsers                 | 20.3 ms                                                  | 26.1 ms: 1.28x slower                                                   |
| many_optionals             | 626 us                                                   | 830 us: 1.32x slower                                                    |
| bench_mp_pool              | 8.07 ms                                                  | 4.67 sec: 579.20x slower                                                |
| Geometric mean             | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (31): sympy_sum, sqlalchemy_declarative, sqlalchemy_imperative, coverage, meteor_contest, richards_super, richards, json_dumps, crypto_pyaes, xml_etree_process, mako, pidigits, fannkuch, deltablue, asyncio_websockets, docutils, genshi_xml, unpickle_pure_python, hexiom, django_template, nbody, comprehensions, json, pickle_pure_python, scimark_sparse_mat_mult, typing_runtime_protocols, python_startup, scimark_lu, bench_thread_pool, coroutines, json_loads
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (5) of results/bm-20250425-3.14.0a7+-9fc1238/bm-20250425-arminc-aarch64-mdboom-python_startup_time-3.14.0a7+-9fc1238.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.069x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.04x