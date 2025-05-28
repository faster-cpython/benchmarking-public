# Results vs. 3.13.0

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: darwin-arm64
- commit hash: 6783662
- commit date: 2025-05-28
- overall geometric mean: 1.084x slower
- HPT reliability: 90.81%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250528-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-6783662 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 187 ms: 1.05x slower                                                            |
| docutils       | 1.44 sec                                               | 1.52 sec: 1.05x slower                                                          |
| html5lib       | 36.7 ms                                                | 34.1 ms: 1.08x faster                                                           |
| sphinx         | 602 ms                                                 | 614 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250528-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-6783662 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 209 ms: 1.38x faster                                                            |
| async_tree_eager_io              | 511 ms                                                 | 397 ms: 1.29x faster                                                            |
| async_tree_memoization           | 268 ms                                                 | 216 ms: 1.24x faster                                                            |
| async_tree_io_tg                 | 500 ms                                                 | 408 ms: 1.23x faster                                                            |
| async_tree_io                    | 508 ms                                                 | 417 ms: 1.22x faster                                                            |
| async_tree_eager_io_tg           | 479 ms                                                 | 405 ms: 1.18x faster                                                            |
| async_tree_none_tg               | 198 ms                                                 | 172 ms: 1.15x faster                                                            |
| async_tree_none                  | 212 ms                                                 | 186 ms: 1.14x faster                                                            |
| async_tree_eager_memoization     | 168 ms                                                 | 152 ms: 1.11x faster                                                            |
| async_generators                 | 294 ms                                                 | 276 ms: 1.06x faster                                                            |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 427 ms: 1.05x faster                                                            |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 438 ms: 1.05x faster                                                            |
| coroutines                       | 20.0 ms                                                | 19.3 ms: 1.04x faster                                                           |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 370 ms: 1.01x faster                                                            |
| async_tree_eager                 | 69.9 ms                                                | 73.5 ms: 1.05x slower                                                           |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 402 ms: 1.16x slower                                                            |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 184 ms: 1.33x slower                                                            |
| async_tree_eager_tg              | 47.4 ms                                                | 144 ms: 3.04x slower                                                            |
| Geometric mean                   | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250528-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-6783662 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 59.4 ms: 1.07x slower                                                           |
| nbody          | 73.6 ms                                                | 85.5 ms: 1.16x slower                                                           |
| Geometric mean | (ref)                                                  | 1.07x slower                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250528-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-6783662 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.35 ms: 1.12x faster                                                           |
| regex_v8       | 17.0 ms                                                | 16.2 ms: 1.05x faster                                                           |
| regex_dna      | 149 ms                                                 | 143 ms: 1.04x faster                                                            |
| regex_compile  | 78.3 ms                                                | 81.5 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250528-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-6783662 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.43 sec: 1.09x faster                                                          |
| xml_etree_parse      | 108 ms                                                 | 105 ms: 1.03x faster                                                            |
| xml_etree_iterparse  | 74.2 ms                                                | 74.9 ms: 1.01x slower                                                           |
| xml_etree_generate   | 57.1 ms                                                | 58.2 ms: 1.02x slower                                                           |
| xml_etree_process    | 41.3 ms                                                | 43.5 ms: 1.05x slower                                                           |
| json_dumps           | 6.47 ms                                                | 6.85 ms: 1.06x slower                                                           |
| json_loads           | 17.0 us                                                | 18.2 us: 1.07x slower                                                           |
| unpickle_pure_python | 165 us                                                 | 179 us: 1.08x slower                                                            |
| pickle_pure_python   | 215 us                                                 | 242 us: 1.13x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.03x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250528-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-6783662 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 16.4 ms: 1.14x faster                                                           |
| python_startup_no_site | 13.7 ms                                                | 12.0 ms: 1.14x faster                                                           |
| Geometric mean         | (ref)                                                  | 1.14x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250528-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-6783662 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 17.5 ms: 1.03x slower                                                           |
| genshi_xml      | 34.1 ms                                                | 36.1 ms: 1.06x slower                                                           |
| mako            | 7.75 ms                                                | 8.96 ms: 1.16x slower                                                           |
| django_template | 20.5 ms                                                | 24.9 ms: 1.21x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.11x slower                                                                    |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250528-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-6783662 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 828 ms: 1.81x faster                                                            |
| async_tree_memoization_tg        | 288 ms                                                 | 209 ms: 1.38x faster                                                            |
| deepcopy                         | 236 us                                                 | 174 us: 1.36x faster                                                            |
| async_tree_eager_io              | 511 ms                                                 | 397 ms: 1.29x faster                                                            |
| deepcopy_memo                    | 27.4 us                                                | 22.0 us: 1.25x faster                                                           |
| async_tree_memoization           | 268 ms                                                 | 216 ms: 1.24x faster                                                            |
| async_tree_io_tg                 | 500 ms                                                 | 408 ms: 1.23x faster                                                            |
| async_tree_io                    | 508 ms                                                 | 417 ms: 1.22x faster                                                            |
| async_tree_eager_io_tg           | 479 ms                                                 | 405 ms: 1.18x faster                                                            |
| go                               | 117 ms                                                 | 100 ms: 1.16x faster                                                            |
| async_tree_none_tg               | 198 ms                                                 | 172 ms: 1.15x faster                                                            |
| scimark_sor                      | 106 ms                                                 | 91.8 ms: 1.15x faster                                                           |
| python_startup                   | 18.8 ms                                                | 16.4 ms: 1.14x faster                                                           |
| python_startup_no_site           | 13.7 ms                                                | 12.0 ms: 1.14x faster                                                           |
| async_tree_none                  | 212 ms                                                 | 186 ms: 1.14x faster                                                            |
| regex_effbot                     | 2.63 ms                                                | 2.35 ms: 1.12x faster                                                           |
| async_tree_eager_memoization     | 168 ms                                                 | 152 ms: 1.11x faster                                                            |
| deepcopy_reduce                  | 2.09 us                                                | 1.90 us: 1.10x faster                                                           |
| tomli_loads                      | 1.57 sec                                               | 1.43 sec: 1.09x faster                                                          |
| html5lib                         | 36.7 ms                                                | 34.1 ms: 1.08x faster                                                           |
| dulwich_log                      | 28.7 ms                                                | 26.9 ms: 1.07x faster                                                           |
| pylint                           | 180 ms                                                 | 169 ms: 1.07x faster                                                            |
| async_generators                 | 294 ms                                                 | 276 ms: 1.06x faster                                                            |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 427 ms: 1.05x faster                                                            |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 438 ms: 1.05x faster                                                            |
| regex_v8                         | 17.0 ms                                                | 16.2 ms: 1.05x faster                                                           |
| regex_dna                        | 149 ms                                                 | 143 ms: 1.04x faster                                                            |
| k_core                           | 1.61 sec                                               | 1.55 sec: 1.04x faster                                                          |
| pyflate                          | 352 ms                                                 | 339 ms: 1.04x faster                                                            |
| coroutines                       | 20.0 ms                                                | 19.3 ms: 1.04x faster                                                           |
| xml_etree_parse                  | 108 ms                                                 | 105 ms: 1.03x faster                                                            |
| spectral_norm                    | 76.5 ms                                                | 75.6 ms: 1.01x faster                                                           |
| connected_components             | 319 ms                                                 | 315 ms: 1.01x faster                                                            |
| shortest_path                    | 345 ms                                                 | 342 ms: 1.01x faster                                                            |
| generators                       | 31.9 ms                                                | 31.6 ms: 1.01x faster                                                           |
| telco                            | 4.84 ms                                                | 4.81 ms: 1.01x faster                                                           |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 370 ms: 1.01x faster                                                            |
| meteor_contest                   | 74.0 ms                                                | 74.3 ms: 1.00x slower                                                           |
| xml_etree_iterparse              | 74.2 ms                                                | 74.9 ms: 1.01x slower                                                           |
| xml_etree_generate               | 57.1 ms                                                | 58.2 ms: 1.02x slower                                                           |
| sphinx                           | 602 ms                                                 | 614 ms: 1.02x slower                                                            |
| pathlib                          | 23.2 ms                                                | 23.9 ms: 1.03x slower                                                           |
| genshi_text                      | 16.9 ms                                                | 17.5 ms: 1.03x slower                                                           |
| regex_compile                    | 78.3 ms                                                | 81.5 ms: 1.04x slower                                                           |
| sqlite_synth                     | 1.55 us                                                | 1.62 us: 1.04x slower                                                           |
| richards                         | 36.2 ms                                                | 37.8 ms: 1.05x slower                                                           |
| 2to3                             | 179 ms                                                 | 187 ms: 1.05x slower                                                            |
| docutils                         | 1.44 sec                                               | 1.52 sec: 1.05x slower                                                          |
| sympy_expand                     | 248 ms                                                 | 260 ms: 1.05x slower                                                            |
| async_tree_eager                 | 69.9 ms                                                | 73.5 ms: 1.05x slower                                                           |
| scimark_fft                      | 200 ms                                                 | 210 ms: 1.05x slower                                                            |
| xml_etree_process                | 41.3 ms                                                | 43.5 ms: 1.05x slower                                                           |
| json_dumps                       | 6.47 ms                                                | 6.85 ms: 1.06x slower                                                           |
| sympy_str                        | 146 ms                                                 | 154 ms: 1.06x slower                                                            |
| genshi_xml                       | 34.1 ms                                                | 36.1 ms: 1.06x slower                                                           |
| hexiom                           | 4.87 ms                                                | 5.16 ms: 1.06x slower                                                           |
| deltablue                        | 2.65 ms                                                | 2.81 ms: 1.06x slower                                                           |
| pycparser                        | 701 ms                                                 | 744 ms: 1.06x slower                                                            |
| scimark_monte_carlo              | 50.4 ms                                                | 53.6 ms: 1.06x slower                                                           |
| bench_thread_pool                | 503 us                                                 | 536 us: 1.06x slower                                                            |
| float                            | 55.8 ms                                                | 59.4 ms: 1.07x slower                                                           |
| json_loads                       | 17.0 us                                                | 18.2 us: 1.07x slower                                                           |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.21 ms: 1.08x slower                                                           |
| richards_super                   | 39.2 ms                                                | 42.2 ms: 1.08x slower                                                           |
| typing_runtime_protocols         | 101 us                                                 | 108 us: 1.08x slower                                                            |
| unpickle_pure_python             | 165 us                                                 | 179 us: 1.08x slower                                                            |
| sympy_sum                        | 75.1 ms                                                | 81.3 ms: 1.08x slower                                                           |
| bench_mp_pool                    | 64.7 ms                                                | 70.5 ms: 1.09x slower                                                           |
| gc_traversal                     | 2.94 ms                                                | 3.21 ms: 1.09x slower                                                           |
| comprehensions                   | 12.0 us                                                | 13.2 us: 1.10x slower                                                           |
| dask                             | 771 ms                                                 | 852 ms: 1.10x slower                                                            |
| crypto_pyaes                     | 55.3 ms                                                | 61.3 ms: 1.11x slower                                                           |
| fannkuch                         | 279 ms                                                 | 311 ms: 1.11x slower                                                            |
| scimark_lu                       | 75.9 ms                                                | 85.3 ms: 1.12x slower                                                           |
| pickle_pure_python               | 215 us                                                 | 242 us: 1.13x slower                                                            |
| logging_format                   | 3.85 us                                                | 4.39 us: 1.14x slower                                                           |
| create_gc_cycles                 | 1.19 ms                                                | 1.36 ms: 1.14x slower                                                           |
| logging_simple                   | 3.56 us                                                | 4.09 us: 1.15x slower                                                           |
| nqueens                          | 61.8 ms                                                | 71.3 ms: 1.15x slower                                                           |
| pprint_pformat                   | 1.10 sec                                               | 1.27 sec: 1.16x slower                                                          |
| mako                             | 7.75 ms                                                | 8.96 ms: 1.16x slower                                                           |
| pprint_safe_repr                 | 541 ms                                                 | 625 ms: 1.16x slower                                                            |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 402 ms: 1.16x slower                                                            |
| chaos                            | 41.1 ms                                                | 47.7 ms: 1.16x slower                                                           |
| nbody                            | 73.6 ms                                                | 85.5 ms: 1.16x slower                                                           |
| raytrace                         | 181 ms                                                 | 212 ms: 1.17x slower                                                            |
| django_template                  | 20.5 ms                                                | 24.9 ms: 1.21x slower                                                           |
| many_optionals                   | 409 us                                                 | 498 us: 1.22x slower                                                            |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 184 ms: 1.33x slower                                                            |
| subparsers                       | 9.44 ms                                                | 15.0 ms: 1.59x slower                                                           |
| async_tree_eager_tg              | 47.4 ms                                                | 144 ms: 3.04x slower                                                            |
| logging_silent                   | 71.0 ns                                                | 340 ns: 4.79x slower                                                            |
| coverage                         | 46.2 ms                                                | 335 ms: 7.26x slower                                                            |
| thrift                           | 466 us                                                 | 44.0 ms: 94.35x slower                                                          |
| Geometric mean                   | (ref)                                                  | 1.11x slower                                                                    |

Benchmark hidden because not significant (5): pidigits, bpe_tokeniser, sympy_integrate, asyncio_websockets, json
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250528-3.15.0a0-6783662/bm-20250528-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-6783662.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.084x slower

# HPT report

- Reliability score: 90.81% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.11x