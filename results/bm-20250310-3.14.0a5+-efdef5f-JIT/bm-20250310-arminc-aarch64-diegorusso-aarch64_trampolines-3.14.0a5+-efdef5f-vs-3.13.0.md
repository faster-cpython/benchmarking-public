# Results vs. 3.13.0

- fork: diegorusso
- ref: aarch64_trampolines
- machine: linux-aarch64
- commit hash: efdef5f
- commit date: 2025-03-10
- overall geometric mean: 1.031x faster
- HPT reliability: 98.77%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250310-arminc-aarch64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 303 ms: 1.03x faster                                                        |
| docutils       | 2.96 sec                                                 | 3.10 sec: 1.04x slower                                                      |
| html5lib       | 65.6 ms                                                  | 61.9 ms: 1.06x faster                                                       |
| sphinx         | 1.20 sec                                                 | 1.15 sec: 1.04x faster                                                      |
| Geometric mean | (ref)                                                    | 1.02x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250310-arminc-aarch64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization     | 664 ms                                                   | 471 ms: 1.41x faster                                                        |
| async_tree_memoization_tg  | 663 ms                                                   | 475 ms: 1.40x faster                                                        |
| async_tree_none            | 504 ms                                                   | 381 ms: 1.32x faster                                                        |
| async_tree_none_tg         | 484 ms                                                   | 370 ms: 1.31x faster                                                        |
| async_tree_io_tg           | 1.16 sec                                                 | 893 ms: 1.30x faster                                                        |
| async_tree_io              | 1.14 sec                                                 | 885 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 649 ms: 1.23x faster                                                        |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 657 ms: 1.20x faster                                                        |
| async_generators           | 500 ms                                                   | 456 ms: 1.10x faster                                                        |
| Geometric mean             | (ref)                                                    | 1.23x faster                                                                |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250310-arminc-aarch64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 82.9 ms: 1.16x faster                                                       |
| Geometric mean | (ref)                                                    | 1.04x faster                                                                |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250310-arminc-aarch64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.89 ms: 1.31x faster                                                       |
| regex_v8       | 32.5 ms                                                  | 28.2 ms: 1.15x faster                                                       |
| regex_compile  | 134 ms                                                   | 123 ms: 1.08x faster                                                        |
| regex_dna      | 263 ms                                                   | 251 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                    | 1.15x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250310-arminc-aarch64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|----------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 203 ms                                                   | 177 ms: 1.15x faster                                                        |
| xml_etree_iterparse  | 159 ms                                                   | 141 ms: 1.12x faster                                                        |
| xml_etree_generate   | 118 ms                                                   | 107 ms: 1.10x faster                                                        |
| tomli_loads          | 2.67 sec                                                 | 2.45 sec: 1.09x faster                                                      |
| xml_etree_process    | 82.1 ms                                                  | 76.6 ms: 1.07x faster                                                       |
| pickle_pure_python   | 374 us                                                   | 398 us: 1.06x slower                                                        |
| unpickle_pure_python | 265 us                                                   | 282 us: 1.07x slower                                                        |
| Geometric mean       | (ref)                                                    | 1.04x faster                                                                |

Benchmark hidden because not significant (2): json_dumps, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250310-arminc-aarch64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 10.1 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                    | 1.07x slower                                                                |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250310-arminc-aarch64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|-----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 28.6 ms                                                  | 26.6 ms: 1.07x faster                                                       |
| django_template | 39.4 ms                                                  | 38.8 ms: 1.02x faster                                                       |
| genshi_xml      | 61.6 ms                                                  | 61.0 ms: 1.01x faster                                                       |
| Geometric mean  | (ref)                                                    | 1.03x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250310-arminc-aarch64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 479 us                                                   | 334 us: 1.43x faster                                                        |
| async_tree_memoization     | 664 ms                                                   | 471 ms: 1.41x faster                                                        |
| async_tree_memoization_tg  | 663 ms                                                   | 475 ms: 1.40x faster                                                        |
| deepcopy_memo              | 53.0 us                                                  | 38.5 us: 1.38x faster                                                       |
| async_tree_none            | 504 ms                                                   | 381 ms: 1.32x faster                                                        |
| regex_effbot               | 5.10 ms                                                  | 3.89 ms: 1.31x faster                                                       |
| async_tree_none_tg         | 484 ms                                                   | 370 ms: 1.31x faster                                                        |
| async_tree_io_tg           | 1.16 sec                                                 | 893 ms: 1.30x faster                                                        |
| async_tree_io              | 1.14 sec                                                 | 885 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 649 ms: 1.23x faster                                                        |
| deepcopy_reduce            | 4.24 us                                                  | 3.52 us: 1.20x faster                                                       |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 657 ms: 1.20x faster                                                        |
| float                      | 95.8 ms                                                  | 82.9 ms: 1.16x faster                                                       |
| regex_v8                   | 32.5 ms                                                  | 28.2 ms: 1.15x faster                                                       |
| xml_etree_parse            | 203 ms                                                   | 177 ms: 1.15x faster                                                        |
| richards_super             | 60.8 ms                                                  | 54.0 ms: 1.13x faster                                                       |
| xml_etree_iterparse        | 159 ms                                                   | 141 ms: 1.12x faster                                                        |
| richards                   | 54.5 ms                                                  | 49.0 ms: 1.11x faster                                                       |
| telco                      | 10.5 ms                                                  | 9.46 ms: 1.11x faster                                                       |
| pylint                     | 345 ms                                                   | 313 ms: 1.11x faster                                                        |
| generators                 | 40.3 ms                                                  | 36.6 ms: 1.10x faster                                                       |
| xml_etree_generate         | 118 ms                                                   | 107 ms: 1.10x faster                                                        |
| pathlib                    | 24.3 ms                                                  | 22.1 ms: 1.10x faster                                                       |
| async_generators           | 500 ms                                                   | 456 ms: 1.10x faster                                                        |
| scimark_sor                | 164 ms                                                   | 150 ms: 1.09x faster                                                        |
| tomli_loads                | 2.67 sec                                                 | 2.45 sec: 1.09x faster                                                      |
| sqlite_synth               | 4.08 us                                                  | 3.75 us: 1.09x faster                                                       |
| regex_compile              | 134 ms                                                   | 123 ms: 1.08x faster                                                        |
| thrift                     | 1.01 ms                                                  | 934 us: 1.08x faster                                                        |
| scimark_fft                | 463 ms                                                   | 428 ms: 1.08x faster                                                        |
| genshi_text                | 28.6 ms                                                  | 26.6 ms: 1.07x faster                                                       |
| xml_etree_process          | 82.1 ms                                                  | 76.6 ms: 1.07x faster                                                       |
| coverage                   | 106 ms                                                   | 98.7 ms: 1.07x faster                                                       |
| chaos                      | 70.7 ms                                                  | 66.5 ms: 1.06x faster                                                       |
| logging_format             | 8.10 us                                                  | 7.64 us: 1.06x faster                                                       |
| html5lib                   | 65.6 ms                                                  | 61.9 ms: 1.06x faster                                                       |
| sqlalchemy_declarative     | 154 ms                                                   | 146 ms: 1.05x faster                                                        |
| logging_simple             | 7.25 us                                                  | 6.90 us: 1.05x faster                                                       |
| bpe_tokeniser              | 6.02 sec                                                 | 5.73 sec: 1.05x faster                                                      |
| regex_dna                  | 263 ms                                                   | 251 ms: 1.05x faster                                                        |
| sphinx                     | 1.20 sec                                                 | 1.15 sec: 1.04x faster                                                      |
| mdp                        | 3.45 sec                                                 | 3.31 sec: 1.04x faster                                                      |
| 2to3                       | 313 ms                                                   | 303 ms: 1.03x faster                                                        |
| logging_silent             | 135 ns                                                   | 131 ns: 1.03x faster                                                        |
| pyflate                    | 582 ms                                                   | 566 ms: 1.03x faster                                                        |
| k_core                     | 2.99 sec                                                 | 2.93 sec: 1.02x faster                                                      |
| django_template            | 39.4 ms                                                  | 38.8 ms: 1.02x faster                                                       |
| genshi_xml                 | 61.6 ms                                                  | 61.0 ms: 1.01x faster                                                       |
| sympy_str                  | 265 ms                                                   | 270 ms: 1.02x slower                                                        |
| shortest_path              | 565 ms                                                   | 585 ms: 1.04x slower                                                        |
| meteor_contest             | 117 ms                                                   | 121 ms: 1.04x slower                                                        |
| typing_runtime_protocols   | 197 us                                                   | 205 us: 1.04x slower                                                        |
| docutils                   | 2.96 sec                                                 | 3.10 sec: 1.04x slower                                                      |
| create_gc_cycles           | 3.39 ms                                                  | 3.57 ms: 1.05x slower                                                       |
| go                         | 164 ms                                                   | 174 ms: 1.06x slower                                                        |
| pickle_pure_python         | 374 us                                                   | 398 us: 1.06x slower                                                        |
| unpickle_pure_python       | 265 us                                                   | 282 us: 1.07x slower                                                        |
| fannkuch                   | 478 ms                                                   | 521 ms: 1.09x slower                                                        |
| gc_traversal               | 5.92 ms                                                  | 6.57 ms: 1.11x slower                                                       |
| hexiom                     | 7.34 ms                                                  | 8.25 ms: 1.12x slower                                                       |
| crypto_pyaes               | 84.9 ms                                                  | 97.4 ms: 1.15x slower                                                       |
| python_startup_no_site     | 8.79 ms                                                  | 10.1 ms: 1.15x slower                                                       |
| comprehensions             | 20.8 us                                                  | 24.6 us: 1.18x slower                                                       |
| subparsers                 | 20.3 ms                                                  | 25.7 ms: 1.26x slower                                                       |
| pprint_safe_repr           | 962 ms                                                   | 1.23 sec: 1.28x slower                                                      |
| pprint_pformat             | 1.99 sec                                                 | 2.56 sec: 1.29x slower                                                      |
| many_optionals             | 626 us                                                   | 837 us: 1.34x slower                                                        |
| bench_mp_pool              | 8.07 ms                                                  | 2.79 sec: 345.88x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.02x slower                                                                |

Benchmark hidden because not significant (23): sympy_sum, scimark_lu, spectral_norm, json_dumps, sqlalchemy_imperative, coroutines, json, mako, asyncio_websockets, sympy_integrate, bench_thread_pool, sympy_expand, pidigits, deltablue, scimark_sparse_mat_mult, python_startup, connected_components, scimark_monte_carlo, pycparser, nbody, nqueens, raytrace, json_loads
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250310-3.14.0a5+-efdef5f-JIT/bm-20250310-arminc-aarch64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.031x faster

# HPT report

- Reliability score: 98.77% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x