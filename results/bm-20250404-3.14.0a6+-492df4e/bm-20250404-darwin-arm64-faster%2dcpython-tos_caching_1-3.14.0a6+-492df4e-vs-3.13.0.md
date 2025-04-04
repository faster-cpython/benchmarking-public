# Results vs. 3.13.0

- fork: faster-cpython
- ref: tos_caching_1
- machine: darwin-arm64
- commit hash: 492df4e
- commit date: 2025-04-04
- overall geometric mean: 1.039x slower
- HPT reliability: 99.86%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250404-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 186 ms: 1.04x slower                                                      |
| docutils       | 1.44 sec                                               | 1.56 sec: 1.08x slower                                                    |
| html5lib       | 36.7 ms                                                | 35.4 ms: 1.04x faster                                                     |
| sphinx         | 602 ms                                                 | 634 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                  | 1.03x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250404-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 212 ms: 1.36x faster                                                      |
| async_tree_eager_io              | 511 ms                                                 | 413 ms: 1.24x faster                                                      |
| async_tree_io_tg                 | 500 ms                                                 | 405 ms: 1.23x faster                                                      |
| async_tree_memoization           | 268 ms                                                 | 222 ms: 1.21x faster                                                      |
| async_tree_io                    | 508 ms                                                 | 430 ms: 1.18x faster                                                      |
| async_tree_eager_io_tg           | 479 ms                                                 | 411 ms: 1.16x faster                                                      |
| async_tree_none_tg               | 198 ms                                                 | 173 ms: 1.14x faster                                                      |
| async_tree_none                  | 212 ms                                                 | 187 ms: 1.13x faster                                                      |
| async_tree_eager_memoization     | 168 ms                                                 | 152 ms: 1.10x faster                                                      |
| async_generators                 | 294 ms                                                 | 270 ms: 1.09x faster                                                      |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 434 ms: 1.06x faster                                                      |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 424 ms: 1.06x faster                                                      |
| coroutines                       | 20.0 ms                                                | 19.6 ms: 1.02x faster                                                     |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 370 ms: 1.01x faster                                                      |
| async_tree_eager                 | 69.9 ms                                                | 75.3 ms: 1.08x slower                                                     |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 402 ms: 1.16x slower                                                      |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 186 ms: 1.35x slower                                                      |
| async_tree_eager_tg              | 47.4 ms                                                | 143 ms: 3.03x slower                                                      |
| Geometric mean                   | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250404-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 73.6 ms                                                | 85.9 ms: 1.17x slower                                                     |
| Geometric mean | (ref)                                                  | 1.05x slower                                                              |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250404-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.24 ms: 1.17x faster                                                     |
| regex_v8       | 17.0 ms                                                | 15.7 ms: 1.08x faster                                                     |
| regex_dna      | 149 ms                                                 | 140 ms: 1.06x faster                                                      |
| regex_compile  | 78.3 ms                                                | 85.0 ms: 1.08x slower                                                     |
| Geometric mean | (ref)                                                  | 1.06x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250404-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 105 ms: 1.03x faster                                                      |
| json_loads           | 17.0 us                                                | 17.8 us: 1.05x slower                                                     |
| xml_etree_iterparse  | 74.2 ms                                                | 77.7 ms: 1.05x slower                                                     |
| xml_etree_generate   | 57.1 ms                                                | 61.4 ms: 1.08x slower                                                     |
| xml_etree_process    | 41.3 ms                                                | 45.2 ms: 1.09x slower                                                     |
| unpickle_pure_python | 165 us                                                 | 184 us: 1.11x slower                                                      |
| pickle_pure_python   | 215 us                                                 | 241 us: 1.12x slower                                                      |
| json_dumps           | 6.47 ms                                                | 7.70 ms: 1.19x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.07x slower                                                              |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250404-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 19.4 ms: 1.03x slower                                                     |
| python_startup_no_site | 13.7 ms                                                | 14.9 ms: 1.08x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250404-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_xml      | 34.1 ms                                                | 36.1 ms: 1.06x slower                                                     |
| mako            | 7.75 ms                                                | 8.23 ms: 1.06x slower                                                     |
| genshi_text     | 16.9 ms                                                | 18.0 ms: 1.07x slower                                                     |
| django_template | 20.5 ms                                                | 24.7 ms: 1.21x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.10x slower                                                              |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250404-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 896 ms: 1.67x faster                                                      |
| async_tree_memoization_tg        | 288 ms                                                 | 212 ms: 1.36x faster                                                      |
| deepcopy                         | 236 us                                                 | 181 us: 1.31x faster                                                      |
| generators                       | 31.9 ms                                                | 25.4 ms: 1.26x faster                                                     |
| async_tree_eager_io              | 511 ms                                                 | 413 ms: 1.24x faster                                                      |
| async_tree_io_tg                 | 500 ms                                                 | 405 ms: 1.23x faster                                                      |
| async_tree_memoization           | 268 ms                                                 | 222 ms: 1.21x faster                                                      |
| async_tree_io                    | 508 ms                                                 | 430 ms: 1.18x faster                                                      |
| regex_effbot                     | 2.63 ms                                                | 2.24 ms: 1.17x faster                                                     |
| async_tree_eager_io_tg           | 479 ms                                                 | 411 ms: 1.16x faster                                                      |
| async_tree_none_tg               | 198 ms                                                 | 173 ms: 1.14x faster                                                      |
| async_tree_none                  | 212 ms                                                 | 187 ms: 1.13x faster                                                      |
| deepcopy_memo                    | 27.4 us                                                | 24.4 us: 1.12x faster                                                     |
| deepcopy_reduce                  | 2.09 us                                                | 1.88 us: 1.12x faster                                                     |
| async_tree_eager_memoization     | 168 ms                                                 | 152 ms: 1.10x faster                                                      |
| go                               | 117 ms                                                 | 106 ms: 1.10x faster                                                      |
| async_generators                 | 294 ms                                                 | 270 ms: 1.09x faster                                                      |
| scimark_sor                      | 106 ms                                                 | 97.7 ms: 1.08x faster                                                     |
| regex_v8                         | 17.0 ms                                                | 15.7 ms: 1.08x faster                                                     |
| regex_dna                        | 149 ms                                                 | 140 ms: 1.06x faster                                                      |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 434 ms: 1.06x faster                                                      |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 424 ms: 1.06x faster                                                      |
| dulwich_log                      | 28.7 ms                                                | 27.3 ms: 1.05x faster                                                     |
| bench_mp_pool                    | 64.7 ms                                                | 61.7 ms: 1.05x faster                                                     |
| html5lib                         | 36.7 ms                                                | 35.4 ms: 1.04x faster                                                     |
| xml_etree_parse                  | 108 ms                                                 | 105 ms: 1.03x faster                                                      |
| coroutines                       | 20.0 ms                                                | 19.6 ms: 1.02x faster                                                     |
| telco                            | 4.84 ms                                                | 4.77 ms: 1.01x faster                                                     |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 370 ms: 1.01x faster                                                      |
| bpe_tokeniser                    | 3.26 sec                                               | 3.27 sec: 1.00x slower                                                    |
| sqlite_synth                     | 1.55 us                                                | 1.56 us: 1.01x slower                                                     |
| pyflate                          | 352 ms                                                 | 356 ms: 1.01x slower                                                      |
| python_startup                   | 18.8 ms                                                | 19.4 ms: 1.03x slower                                                     |
| 2to3                             | 179 ms                                                 | 186 ms: 1.04x slower                                                      |
| coverage                         | 46.2 ms                                                | 48.3 ms: 1.04x slower                                                     |
| json_loads                       | 17.0 us                                                | 17.8 us: 1.05x slower                                                     |
| xml_etree_iterparse              | 74.2 ms                                                | 77.7 ms: 1.05x slower                                                     |
| shortest_path                    | 345 ms                                                 | 363 ms: 1.05x slower                                                      |
| logging_silent                   | 71.0 ns                                                | 74.8 ns: 1.05x slower                                                     |
| sphinx                           | 602 ms                                                 | 634 ms: 1.05x slower                                                      |
| meteor_contest                   | 74.0 ms                                                | 78.0 ms: 1.05x slower                                                     |
| pathlib                          | 23.2 ms                                                | 24.5 ms: 1.06x slower                                                     |
| gc_traversal                     | 2.94 ms                                                | 3.11 ms: 1.06x slower                                                     |
| genshi_xml                       | 34.1 ms                                                | 36.1 ms: 1.06x slower                                                     |
| mako                             | 7.75 ms                                                | 8.23 ms: 1.06x slower                                                     |
| connected_components             | 319 ms                                                 | 339 ms: 1.06x slower                                                      |
| genshi_text                      | 16.9 ms                                                | 18.0 ms: 1.07x slower                                                     |
| sympy_integrate                  | 11.3 ms                                                | 12.1 ms: 1.07x slower                                                     |
| create_gc_cycles                 | 1.19 ms                                                | 1.28 ms: 1.07x slower                                                     |
| bench_thread_pool                | 503 us                                                 | 540 us: 1.07x slower                                                      |
| xml_etree_generate               | 57.1 ms                                                | 61.4 ms: 1.08x slower                                                     |
| async_tree_eager                 | 69.9 ms                                                | 75.3 ms: 1.08x slower                                                     |
| pprint_pformat                   | 1.10 sec                                               | 1.19 sec: 1.08x slower                                                    |
| pycparser                        | 701 ms                                                 | 755 ms: 1.08x slower                                                      |
| docutils                         | 1.44 sec                                               | 1.56 sec: 1.08x slower                                                    |
| scimark_fft                      | 200 ms                                                 | 216 ms: 1.08x slower                                                      |
| python_startup_no_site           | 13.7 ms                                                | 14.9 ms: 1.08x slower                                                     |
| regex_compile                    | 78.3 ms                                                | 85.0 ms: 1.08x slower                                                     |
| pprint_safe_repr                 | 541 ms                                                 | 587 ms: 1.09x slower                                                      |
| xml_etree_process                | 41.3 ms                                                | 45.2 ms: 1.09x slower                                                     |
| sympy_expand                     | 248 ms                                                 | 271 ms: 1.09x slower                                                      |
| deltablue                        | 2.65 ms                                                | 2.91 ms: 1.10x slower                                                     |
| typing_runtime_protocols         | 101 us                                                 | 111 us: 1.10x slower                                                      |
| spectral_norm                    | 76.5 ms                                                | 84.6 ms: 1.11x slower                                                     |
| crypto_pyaes                     | 55.3 ms                                                | 61.3 ms: 1.11x slower                                                     |
| sympy_str                        | 146 ms                                                 | 162 ms: 1.11x slower                                                      |
| unpickle_pure_python             | 165 us                                                 | 184 us: 1.11x slower                                                      |
| richards                         | 36.2 ms                                                | 40.5 ms: 1.12x slower                                                     |
| fannkuch                         | 279 ms                                                 | 312 ms: 1.12x slower                                                      |
| sqlalchemy_declarative           | 59.0 ms                                                | 66.1 ms: 1.12x slower                                                     |
| sympy_sum                        | 75.1 ms                                                | 84.2 ms: 1.12x slower                                                     |
| pickle_pure_python               | 215 us                                                 | 241 us: 1.12x slower                                                      |
| raytrace                         | 181 ms                                                 | 204 ms: 1.12x slower                                                      |
| logging_format                   | 3.85 us                                                | 4.36 us: 1.13x slower                                                     |
| logging_simple                   | 3.56 us                                                | 4.03 us: 1.13x slower                                                     |
| scimark_monte_carlo              | 50.4 ms                                                | 57.3 ms: 1.14x slower                                                     |
| richards_super                   | 39.2 ms                                                | 44.7 ms: 1.14x slower                                                     |
| hexiom                           | 4.87 ms                                                | 5.60 ms: 1.15x slower                                                     |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.45 ms: 1.16x slower                                                     |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 402 ms: 1.16x slower                                                      |
| sqlalchemy_imperative            | 6.69 ms                                                | 7.77 ms: 1.16x slower                                                     |
| nbody                            | 73.6 ms                                                | 85.9 ms: 1.17x slower                                                     |
| nqueens                          | 61.8 ms                                                | 72.5 ms: 1.17x slower                                                     |
| scimark_lu                       | 75.9 ms                                                | 89.5 ms: 1.18x slower                                                     |
| many_optionals                   | 409 us                                                 | 486 us: 1.19x slower                                                      |
| json_dumps                       | 6.47 ms                                                | 7.70 ms: 1.19x slower                                                     |
| django_template                  | 20.5 ms                                                | 24.7 ms: 1.21x slower                                                     |
| chaos                            | 41.1 ms                                                | 49.8 ms: 1.21x slower                                                     |
| comprehensions                   | 12.0 us                                                | 14.7 us: 1.23x slower                                                     |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 186 ms: 1.35x slower                                                      |
| subparsers                       | 9.44 ms                                                | 13.6 ms: 1.45x slower                                                     |
| async_tree_eager_tg              | 47.4 ms                                                | 143 ms: 3.03x slower                                                      |
| Geometric mean                   | (ref)                                                  | 1.04x slower                                                              |

Benchmark hidden because not significant (7): pylint, float, k_core, asyncio_websockets, pidigits, tomli_loads, json
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250404-3.14.0a6+-492df4e/bm-20250404-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.039x slower

# HPT report

- Reliability score: 99.86% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.09x