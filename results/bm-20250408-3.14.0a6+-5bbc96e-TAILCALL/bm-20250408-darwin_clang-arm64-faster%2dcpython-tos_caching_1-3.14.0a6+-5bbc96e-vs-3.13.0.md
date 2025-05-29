# Results vs. 3.13.0

- fork: faster-cpython
- ref: tos_caching_1
- machine: darwin-arm64
- commit hash: 5bbc96e
- commit date: 2025-04-08
- overall geometric mean: 1.166x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 149 ms: 1.19x faster                                                      |
| docutils       | 1.44 sec                                               | 1.36 sec: 1.06x faster                                                    |
| html5lib       | 36.7 ms                                                | 28.1 ms: 1.30x faster                                                     |
| sphinx         | 602 ms                                                 | 548 ms: 1.10x faster                                                      |
| Geometric mean | (ref)                                                  | 1.16x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 181 ms: 1.59x faster                                                      |
| async_tree_io                    | 508 ms                                                 | 336 ms: 1.51x faster                                                      |
| async_tree_memoization           | 268 ms                                                 | 178 ms: 1.50x faster                                                      |
| async_tree_eager_io              | 511 ms                                                 | 342 ms: 1.49x faster                                                      |
| async_tree_io_tg                 | 500 ms                                                 | 339 ms: 1.47x faster                                                      |
| async_tree_none                  | 212 ms                                                 | 150 ms: 1.41x faster                                                      |
| coroutines                       | 20.0 ms                                                | 14.2 ms: 1.41x faster                                                     |
| async_tree_none_tg               | 198 ms                                                 | 143 ms: 1.39x faster                                                      |
| async_tree_eager_io_tg           | 479 ms                                                 | 346 ms: 1.38x faster                                                      |
| async_tree_eager_memoization     | 168 ms                                                 | 130 ms: 1.30x faster                                                      |
| async_tree_eager                 | 69.9 ms                                                | 55.3 ms: 1.27x faster                                                     |
| async_generators                 | 294 ms                                                 | 249 ms: 1.18x faster                                                      |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 398 ms: 1.15x faster                                                      |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 397 ms: 1.13x faster                                                      |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 343 ms: 1.09x faster                                                      |
| asyncio_websockets               | 242 ms                                                 | 242 ms: 1.00x faster                                                      |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 379 ms: 1.09x slower                                                      |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 160 ms: 1.16x slower                                                      |
| async_tree_eager_tg              | 47.4 ms                                                | 121 ms: 2.55x slower                                                      |
| Geometric mean                   | (ref)                                                  | 1.19x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 41.0 ms: 1.36x faster                                                     |
| nbody          | 73.6 ms                                                | 69.0 ms: 1.07x faster                                                     |
| pidigits       | 284 ms                                                 | 280 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.14x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 78.3 ms                                                | 63.9 ms: 1.23x faster                                                     |
| regex_effbot   | 2.63 ms                                                | 2.39 ms: 1.10x faster                                                     |
| regex_v8       | 17.0 ms                                                | 16.7 ms: 1.02x faster                                                     |
| regex_dna      | 149 ms                                                 | 148 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.08x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.14 sec: 1.38x faster                                                    |
| unpickle_pure_python | 165 us                                                 | 128 us: 1.29x faster                                                      |
| pickle_pure_python   | 215 us                                                 | 180 us: 1.19x faster                                                      |
| xml_etree_process    | 41.3 ms                                                | 35.4 ms: 1.17x faster                                                     |
| xml_etree_generate   | 57.1 ms                                                | 50.9 ms: 1.12x faster                                                     |
| xml_etree_iterparse  | 74.2 ms                                                | 68.8 ms: 1.08x faster                                                     |
| xml_etree_parse      | 108 ms                                                 | 104 ms: 1.04x faster                                                      |
| json_loads           | 17.0 us                                                | 17.9 us: 1.05x slower                                                     |
| json_dumps           | 6.47 ms                                                | 7.15 ms: 1.10x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 19.2 ms: 1.02x slower                                                     |
| python_startup_no_site | 13.7 ms                                                | 14.9 ms: 1.08x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 12.7 ms: 1.34x faster                                                     |
| genshi_xml      | 34.1 ms                                                | 26.8 ms: 1.27x faster                                                     |
| django_template | 20.5 ms                                                | 18.8 ms: 1.09x faster                                                     |
| mako            | 7.75 ms                                                | 8.36 ms: 1.08x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.14x faster                                                              |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 675 ms: 2.22x faster                                                      |
| generators                       | 31.9 ms                                                | 17.9 ms: 1.78x faster                                                     |
| go                               | 117 ms                                                 | 66.0 ms: 1.77x faster                                                     |
| deepcopy                         | 236 us                                                 | 144 us: 1.64x faster                                                      |
| async_tree_memoization_tg        | 288 ms                                                 | 181 ms: 1.59x faster                                                      |
| async_tree_io                    | 508 ms                                                 | 336 ms: 1.51x faster                                                      |
| async_tree_memoization           | 268 ms                                                 | 178 ms: 1.50x faster                                                      |
| async_tree_eager_io              | 511 ms                                                 | 342 ms: 1.49x faster                                                      |
| deepcopy_memo                    | 27.4 us                                                | 18.5 us: 1.48x faster                                                     |
| async_tree_io_tg                 | 500 ms                                                 | 339 ms: 1.47x faster                                                      |
| scimark_sor                      | 106 ms                                                 | 72.7 ms: 1.45x faster                                                     |
| async_tree_none                  | 212 ms                                                 | 150 ms: 1.41x faster                                                      |
| coroutines                       | 20.0 ms                                                | 14.2 ms: 1.41x faster                                                     |
| async_tree_none_tg               | 198 ms                                                 | 143 ms: 1.39x faster                                                      |
| async_tree_eager_io_tg           | 479 ms                                                 | 346 ms: 1.38x faster                                                      |
| tomli_loads                      | 1.57 sec                                               | 1.14 sec: 1.38x faster                                                    |
| deltablue                        | 2.65 ms                                                | 1.92 ms: 1.38x faster                                                     |
| pyflate                          | 352 ms                                                 | 257 ms: 1.37x faster                                                      |
| scimark_monte_carlo              | 50.4 ms                                                | 36.9 ms: 1.37x faster                                                     |
| deepcopy_reduce                  | 2.09 us                                                | 1.53 us: 1.37x faster                                                     |
| float                            | 55.8 ms                                                | 41.0 ms: 1.36x faster                                                     |
| genshi_text                      | 16.9 ms                                                | 12.7 ms: 1.34x faster                                                     |
| hexiom                           | 4.87 ms                                                | 3.68 ms: 1.32x faster                                                     |
| logging_silent                   | 71.0 ns                                                | 54.4 ns: 1.31x faster                                                     |
| html5lib                         | 36.7 ms                                                | 28.1 ms: 1.30x faster                                                     |
| async_tree_eager_memoization     | 168 ms                                                 | 130 ms: 1.30x faster                                                      |
| unpickle_pure_python             | 165 us                                                 | 128 us: 1.29x faster                                                      |
| genshi_xml                       | 34.1 ms                                                | 26.8 ms: 1.27x faster                                                     |
| async_tree_eager                 | 69.9 ms                                                | 55.3 ms: 1.27x faster                                                     |
| richards                         | 36.2 ms                                                | 28.7 ms: 1.26x faster                                                     |
| dulwich_log                      | 28.7 ms                                                | 23.1 ms: 1.25x faster                                                     |
| chaos                            | 41.1 ms                                                | 33.1 ms: 1.24x faster                                                     |
| crypto_pyaes                     | 55.3 ms                                                | 44.8 ms: 1.24x faster                                                     |
| richards_super                   | 39.2 ms                                                | 31.9 ms: 1.23x faster                                                     |
| nqueens                          | 61.8 ms                                                | 50.4 ms: 1.23x faster                                                     |
| regex_compile                    | 78.3 ms                                                | 63.9 ms: 1.23x faster                                                     |
| comprehensions                   | 12.0 us                                                | 9.78 us: 1.22x faster                                                     |
| spectral_norm                    | 76.5 ms                                                | 63.0 ms: 1.21x faster                                                     |
| raytrace                         | 181 ms                                                 | 150 ms: 1.21x faster                                                      |
| pylint                           | 180 ms                                                 | 149 ms: 1.21x faster                                                      |
| logging_simple                   | 3.56 us                                                | 2.96 us: 1.20x faster                                                     |
| bpe_tokeniser                    | 3.26 sec                                               | 2.72 sec: 1.20x faster                                                    |
| 2to3                             | 179 ms                                                 | 149 ms: 1.19x faster                                                      |
| pickle_pure_python               | 215 us                                                 | 180 us: 1.19x faster                                                      |
| logging_format                   | 3.85 us                                                | 3.24 us: 1.19x faster                                                     |
| async_generators                 | 294 ms                                                 | 249 ms: 1.18x faster                                                      |
| sympy_integrate                  | 11.3 ms                                                | 9.67 ms: 1.17x faster                                                     |
| xml_etree_process                | 41.3 ms                                                | 35.4 ms: 1.17x faster                                                     |
| pprint_pformat                   | 1.10 sec                                               | 946 ms: 1.16x faster                                                      |
| fannkuch                         | 279 ms                                                 | 240 ms: 1.16x faster                                                      |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 398 ms: 1.15x faster                                                      |
| typing_runtime_protocols         | 101 us                                                 | 87.3 us: 1.15x faster                                                     |
| pprint_safe_repr                 | 541 ms                                                 | 469 ms: 1.15x faster                                                      |
| pycparser                        | 701 ms                                                 | 613 ms: 1.14x faster                                                      |
| sympy_expand                     | 248 ms                                                 | 217 ms: 1.14x faster                                                      |
| sympy_str                        | 146 ms                                                 | 128 ms: 1.14x faster                                                      |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 397 ms: 1.13x faster                                                      |
| xml_etree_generate               | 57.1 ms                                                | 50.9 ms: 1.12x faster                                                     |
| regex_effbot                     | 2.63 ms                                                | 2.39 ms: 1.10x faster                                                     |
| sphinx                           | 602 ms                                                 | 548 ms: 1.10x faster                                                      |
| scimark_lu                       | 75.9 ms                                                | 69.2 ms: 1.10x faster                                                     |
| scimark_fft                      | 200 ms                                                 | 183 ms: 1.09x faster                                                      |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.13 ms: 1.09x faster                                                     |
| django_template                  | 20.5 ms                                                | 18.8 ms: 1.09x faster                                                     |
| k_core                           | 1.61 sec                                               | 1.48 sec: 1.09x faster                                                    |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 343 ms: 1.09x faster                                                      |
| bench_thread_pool                | 503 us                                                 | 464 us: 1.08x faster                                                      |
| sqlalchemy_declarative           | 59.0 ms                                                | 54.4 ms: 1.08x faster                                                     |
| bench_mp_pool                    | 64.7 ms                                                | 59.8 ms: 1.08x faster                                                     |
| xml_etree_iterparse              | 74.2 ms                                                | 68.8 ms: 1.08x faster                                                     |
| sympy_sum                        | 75.1 ms                                                | 69.8 ms: 1.08x faster                                                     |
| meteor_contest                   | 74.0 ms                                                | 68.8 ms: 1.07x faster                                                     |
| telco                            | 4.84 ms                                                | 4.53 ms: 1.07x faster                                                     |
| nbody                            | 73.6 ms                                                | 69.0 ms: 1.07x faster                                                     |
| docutils                         | 1.44 sec                                               | 1.36 sec: 1.06x faster                                                    |
| connected_components             | 319 ms                                                 | 302 ms: 1.06x faster                                                      |
| shortest_path                    | 345 ms                                                 | 328 ms: 1.05x faster                                                      |
| xml_etree_parse                  | 108 ms                                                 | 104 ms: 1.04x faster                                                      |
| coverage                         | 46.2 ms                                                | 44.6 ms: 1.04x faster                                                     |
| sqlite_synth                     | 1.55 us                                                | 1.51 us: 1.03x faster                                                     |
| regex_v8                         | 17.0 ms                                                | 16.7 ms: 1.02x faster                                                     |
| pidigits                         | 284 ms                                                 | 280 ms: 1.01x faster                                                      |
| regex_dna                        | 149 ms                                                 | 148 ms: 1.01x faster                                                      |
| asyncio_websockets               | 242 ms                                                 | 242 ms: 1.00x faster                                                      |
| many_optionals                   | 409 us                                                 | 417 us: 1.02x slower                                                      |
| python_startup                   | 18.8 ms                                                | 19.2 ms: 1.02x slower                                                     |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.05 ms: 1.02x slower                                                     |
| json_loads                       | 17.0 us                                                | 17.9 us: 1.05x slower                                                     |
| gc_traversal                     | 2.94 ms                                                | 3.10 ms: 1.06x slower                                                     |
| create_gc_cycles                 | 1.19 ms                                                | 1.27 ms: 1.07x slower                                                     |
| mako                             | 7.75 ms                                                | 8.36 ms: 1.08x slower                                                     |
| python_startup_no_site           | 13.7 ms                                                | 14.9 ms: 1.08x slower                                                     |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 379 ms: 1.09x slower                                                      |
| json_dumps                       | 6.47 ms                                                | 7.15 ms: 1.10x slower                                                     |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 160 ms: 1.16x slower                                                      |
| subparsers                       | 9.44 ms                                                | 11.4 ms: 1.21x slower                                                     |
| async_tree_eager_tg              | 47.4 ms                                                | 121 ms: 2.55x slower                                                      |
| Geometric mean                   | (ref)                                                  | 1.17x faster                                                              |

Benchmark hidden because not significant (2): json, pathlib
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250408-3.14.0a6+-5bbc96e-CLANG/bm-20250408-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.166x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: 1.08x