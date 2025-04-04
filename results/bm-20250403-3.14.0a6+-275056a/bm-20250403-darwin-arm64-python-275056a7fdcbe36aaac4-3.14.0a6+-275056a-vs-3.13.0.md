# Results vs. 3.13.0

- fork: python
- ref: 275056a7fdcbe36aaac4
- machine: darwin-arm64
- commit hash: 275056a
- commit date: 2025-04-03
- overall geometric mean: 1.046x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 169 ms: 1.06x faster                                                   |
| docutils       | 1.44 sec                                               | 1.46 sec: 1.01x slower                                                 |
| html5lib       | 36.7 ms                                                | 31.5 ms: 1.16x faster                                                  |
| sphinx         | 602 ms                                                 | 591 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 194 ms: 1.48x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 373 ms: 1.37x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 198 ms: 1.35x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 375 ms: 1.34x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 390 ms: 1.30x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 167 ms: 1.26x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 381 ms: 1.26x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 159 ms: 1.25x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.20x faster                                                   |
| coroutines                       | 20.0 ms                                                | 17.3 ms: 1.16x faster                                                  |
| async_generators                 | 294 ms                                                 | 261 ms: 1.12x faster                                                   |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 412 ms: 1.11x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 410 ms: 1.09x faster                                                   |
| async_tree_eager                 | 69.9 ms                                                | 65.0 ms: 1.08x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 357 ms: 1.04x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 390 ms: 1.12x slower                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 173 ms: 1.25x slower                                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 134 ms: 2.83x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.09x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 49.5 ms: 1.13x faster                                                  |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                                   |
| nbody          | 73.6 ms                                                | 75.7 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.28 ms: 1.16x faster                                                  |
| regex_compile  | 78.3 ms                                                | 73.2 ms: 1.07x faster                                                  |
| regex_dna      | 149 ms                                                 | 141 ms: 1.06x faster                                                   |
| regex_v8       | 17.0 ms                                                | 16.1 ms: 1.05x faster                                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.34 sec: 1.16x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 104 ms: 1.04x faster                                                   |
| xml_etree_process    | 41.3 ms                                                | 39.9 ms: 1.04x faster                                                  |
| xml_etree_generate   | 57.1 ms                                                | 55.9 ms: 1.02x faster                                                  |
| unpickle_pure_python | 165 us                                                 | 162 us: 1.02x faster                                                   |
| xml_etree_iterparse  | 74.2 ms                                                | 73.6 ms: 1.01x faster                                                  |
| pickle_pure_python   | 215 us                                                 | 220 us: 1.02x slower                                                   |
| json_loads           | 17.0 us                                                | 17.7 us: 1.04x slower                                                  |
| json_dumps           | 6.47 ms                                                | 7.43 ms: 1.15x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 19.3 ms: 1.03x slower                                                  |
| python_startup_no_site | 13.7 ms                                                | 14.9 ms: 1.08x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 14.9 ms: 1.13x faster                                                  |
| genshi_xml      | 34.1 ms                                                | 30.8 ms: 1.11x faster                                                  |
| mako            | 7.75 ms                                                | 7.87 ms: 1.02x slower                                                  |
| django_template | 20.5 ms                                                | 22.2 ms: 1.08x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 785 ms: 1.91x faster                                                   |
| deepcopy                         | 236 us                                                 | 159 us: 1.48x faster                                                   |
| async_tree_memoization_tg        | 288 ms                                                 | 194 ms: 1.48x faster                                                   |
| deepcopy_memo                    | 27.4 us                                                | 19.3 us: 1.42x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 373 ms: 1.37x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 198 ms: 1.35x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 375 ms: 1.34x faster                                                   |
| go                               | 117 ms                                                 | 88.7 ms: 1.32x faster                                                  |
| generators                       | 31.9 ms                                                | 24.3 ms: 1.31x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 390 ms: 1.30x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 167 ms: 1.26x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 381 ms: 1.26x faster                                                   |
| deepcopy_reduce                  | 2.09 us                                                | 1.67 us: 1.25x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 159 ms: 1.25x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.20x faster                                                   |
| scimark_sor                      | 106 ms                                                 | 88.6 ms: 1.19x faster                                                  |
| tomli_loads                      | 1.57 sec                                               | 1.34 sec: 1.16x faster                                                 |
| html5lib                         | 36.7 ms                                                | 31.5 ms: 1.16x faster                                                  |
| coroutines                       | 20.0 ms                                                | 17.3 ms: 1.16x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.28 ms: 1.16x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 25.3 ms: 1.14x faster                                                  |
| genshi_text                      | 16.9 ms                                                | 14.9 ms: 1.13x faster                                                  |
| float                            | 55.8 ms                                                | 49.5 ms: 1.13x faster                                                  |
| async_generators                 | 294 ms                                                 | 261 ms: 1.12x faster                                                   |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 412 ms: 1.11x faster                                                   |
| pyflate                          | 352 ms                                                 | 318 ms: 1.11x faster                                                   |
| genshi_xml                       | 34.1 ms                                                | 30.8 ms: 1.11x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 410 ms: 1.09x faster                                                   |
| scimark_monte_carlo              | 50.4 ms                                                | 46.4 ms: 1.09x faster                                                  |
| pylint                           | 180 ms                                                 | 166 ms: 1.08x faster                                                   |
| async_tree_eager                 | 69.9 ms                                                | 65.0 ms: 1.08x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 71.5 ms: 1.07x faster                                                  |
| regex_compile                    | 78.3 ms                                                | 73.2 ms: 1.07x faster                                                  |
| pprint_pformat                   | 1.10 sec                                               | 1.04 sec: 1.06x faster                                                 |
| 2to3                             | 179 ms                                                 | 169 ms: 1.06x faster                                                   |
| bench_mp_pool                    | 64.7 ms                                                | 61.2 ms: 1.06x faster                                                  |
| regex_dna                        | 149 ms                                                 | 141 ms: 1.06x faster                                                   |
| regex_v8                         | 17.0 ms                                                | 16.1 ms: 1.05x faster                                                  |
| pprint_safe_repr                 | 541 ms                                                 | 514 ms: 1.05x faster                                                   |
| k_core                           | 1.61 sec                                               | 1.54 sec: 1.05x faster                                                 |
| bpe_tokeniser                    | 3.26 sec                                               | 3.12 sec: 1.04x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 357 ms: 1.04x faster                                                   |
| xml_etree_parse                  | 108 ms                                                 | 104 ms: 1.04x faster                                                   |
| xml_etree_process                | 41.3 ms                                                | 39.9 ms: 1.04x faster                                                  |
| deltablue                        | 2.65 ms                                                | 2.56 ms: 1.03x faster                                                  |
| telco                            | 4.84 ms                                                | 4.68 ms: 1.03x faster                                                  |
| logging_simple                   | 3.56 us                                                | 3.45 us: 1.03x faster                                                  |
| scimark_fft                      | 200 ms                                                 | 194 ms: 1.03x faster                                                   |
| logging_silent                   | 71.0 ns                                                | 69.0 ns: 1.03x faster                                                  |
| pycparser                        | 701 ms                                                 | 682 ms: 1.03x faster                                                   |
| typing_runtime_protocols         | 101 us                                                 | 98.3 us: 1.02x faster                                                  |
| logging_format                   | 3.85 us                                                | 3.77 us: 1.02x faster                                                  |
| xml_etree_generate               | 57.1 ms                                                | 55.9 ms: 1.02x faster                                                  |
| unpickle_pure_python             | 165 us                                                 | 162 us: 1.02x faster                                                   |
| sphinx                           | 602 ms                                                 | 591 ms: 1.02x faster                                                   |
| shortest_path                    | 345 ms                                                 | 341 ms: 1.01x faster                                                   |
| raytrace                         | 181 ms                                                 | 179 ms: 1.01x faster                                                   |
| xml_etree_iterparse              | 74.2 ms                                                | 73.6 ms: 1.01x faster                                                  |
| hexiom                           | 4.87 ms                                                | 4.84 ms: 1.01x faster                                                  |
| chaos                            | 41.1 ms                                                | 40.9 ms: 1.00x faster                                                  |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                                   |
| bench_thread_pool                | 503 us                                                 | 505 us: 1.00x slower                                                   |
| sympy_expand                     | 248 ms                                                 | 248 ms: 1.00x slower                                                   |
| connected_components             | 319 ms                                                 | 320 ms: 1.00x slower                                                   |
| coverage                         | 46.2 ms                                                | 46.4 ms: 1.00x slower                                                  |
| sympy_integrate                  | 11.3 ms                                                | 11.4 ms: 1.01x slower                                                  |
| richards                         | 36.2 ms                                                | 36.5 ms: 1.01x slower                                                  |
| docutils                         | 1.44 sec                                               | 1.46 sec: 1.01x slower                                                 |
| sympy_str                        | 146 ms                                                 | 148 ms: 1.01x slower                                                   |
| mako                             | 7.75 ms                                                | 7.87 ms: 1.02x slower                                                  |
| fannkuch                         | 279 ms                                                 | 284 ms: 1.02x slower                                                   |
| meteor_contest                   | 74.0 ms                                                | 75.7 ms: 1.02x slower                                                  |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.85 ms: 1.02x slower                                                  |
| pickle_pure_python               | 215 us                                                 | 220 us: 1.02x slower                                                   |
| pathlib                          | 23.2 ms                                                | 23.8 ms: 1.03x slower                                                  |
| python_startup                   | 18.8 ms                                                | 19.3 ms: 1.03x slower                                                  |
| nbody                            | 73.6 ms                                                | 75.7 ms: 1.03x slower                                                  |
| richards_super                   | 39.2 ms                                                | 40.5 ms: 1.03x slower                                                  |
| sympy_sum                        | 75.1 ms                                                | 77.6 ms: 1.03x slower                                                  |
| nqueens                          | 61.8 ms                                                | 64.0 ms: 1.04x slower                                                  |
| sqlalchemy_declarative           | 59.0 ms                                                | 61.2 ms: 1.04x slower                                                  |
| json_loads                       | 17.0 us                                                | 17.7 us: 1.04x slower                                                  |
| crypto_pyaes                     | 55.3 ms                                                | 57.5 ms: 1.04x slower                                                  |
| comprehensions                   | 12.0 us                                                | 12.6 us: 1.05x slower                                                  |
| gc_traversal                     | 2.94 ms                                                | 3.11 ms: 1.06x slower                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 1.27 ms: 1.07x slower                                                  |
| scimark_lu                       | 75.9 ms                                                | 81.4 ms: 1.07x slower                                                  |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.20 ms: 1.07x slower                                                  |
| django_template                  | 20.5 ms                                                | 22.2 ms: 1.08x slower                                                  |
| python_startup_no_site           | 13.7 ms                                                | 14.9 ms: 1.08x slower                                                  |
| many_optionals                   | 409 us                                                 | 456 us: 1.11x slower                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 390 ms: 1.12x slower                                                   |
| json_dumps                       | 6.47 ms                                                | 7.43 ms: 1.15x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 173 ms: 1.25x slower                                                   |
| subparsers                       | 9.44 ms                                                | 12.6 ms: 1.33x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 134 ms: 2.83x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (3): json, asyncio_websockets, sqlite_synth
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250403-3.14.0a6+-275056a/bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.046x faster

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.09x