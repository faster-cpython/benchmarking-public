# Results vs. 3.13.0

- fork: JelleZijlstra
- ref: sunder_io
- machine: darwin-arm64
- commit hash: dac50cc
- commit date: 2025-04-25
- overall geometric mean: 1.105x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-darwin-arm64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 160 ms: 1.11x faster                                               |
| docutils       | 1.44 sec                                               | 1.42 sec: 1.02x faster                                             |
| html5lib       | 36.7 ms                                                | 29.2 ms: 1.25x faster                                              |
| sphinx         | 602 ms                                                 | 574 ms: 1.05x faster                                               |
| Geometric mean | (ref)                                                  | 1.11x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-darwin-arm64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 184 ms: 1.56x faster                                               |
| async_tree_io                    | 508 ms                                                 | 354 ms: 1.44x faster                                               |
| async_tree_io_tg                 | 500 ms                                                 | 351 ms: 1.43x faster                                               |
| async_tree_eager_io              | 511 ms                                                 | 359 ms: 1.42x faster                                               |
| async_tree_memoization           | 268 ms                                                 | 190 ms: 1.41x faster                                               |
| async_tree_eager_io_tg           | 479 ms                                                 | 360 ms: 1.33x faster                                               |
| async_tree_none                  | 212 ms                                                 | 159 ms: 1.33x faster                                               |
| async_tree_none_tg               | 198 ms                                                 | 151 ms: 1.31x faster                                               |
| async_tree_eager_memoization     | 168 ms                                                 | 135 ms: 1.25x faster                                               |
| coroutines                       | 20.0 ms                                                | 16.3 ms: 1.23x faster                                              |
| async_generators                 | 294 ms                                                 | 246 ms: 1.20x faster                                               |
| async_tree_eager                 | 69.9 ms                                                | 59.9 ms: 1.17x faster                                              |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 399 ms: 1.15x faster                                               |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 402 ms: 1.11x faster                                               |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 347 ms: 1.07x faster                                               |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 378 ms: 1.09x slower                                               |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 167 ms: 1.21x slower                                               |
| async_tree_eager_tg              | 47.4 ms                                                | 130 ms: 2.74x slower                                               |
| Geometric mean                   | (ref)                                                  | 1.14x faster                                                       |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-darwin-arm64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 45.7 ms: 1.22x faster                                              |
| nbody          | 73.6 ms                                                | 70.7 ms: 1.04x faster                                              |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                               |
| Geometric mean | (ref)                                                  | 1.08x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-darwin-arm64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 78.3 ms                                                | 66.1 ms: 1.18x faster                                              |
| regex_effbot   | 2.63 ms                                                | 2.26 ms: 1.16x faster                                              |
| regex_v8       | 17.0 ms                                                | 15.7 ms: 1.09x faster                                              |
| regex_dna      | 149 ms                                                 | 140 ms: 1.06x faster                                               |
| Geometric mean | (ref)                                                  | 1.12x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-darwin-arm64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.21 sec: 1.29x faster                                             |
| unpickle_pure_python | 165 us                                                 | 143 us: 1.16x faster                                               |
| xml_etree_process    | 41.3 ms                                                | 38.1 ms: 1.09x faster                                              |
| pickle_pure_python   | 215 us                                                 | 201 us: 1.07x faster                                               |
| xml_etree_generate   | 57.1 ms                                                | 53.5 ms: 1.07x faster                                              |
| xml_etree_iterparse  | 74.2 ms                                                | 71.6 ms: 1.04x faster                                              |
| xml_etree_parse      | 108 ms                                                 | 109 ms: 1.01x slower                                               |
| json_loads           | 17.0 us                                                | 17.6 us: 1.03x slower                                              |
| json_dumps           | 6.47 ms                                                | 7.37 ms: 1.14x slower                                              |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-darwin-arm64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 19.9 ms: 1.06x slower                                              |
| python_startup_no_site | 13.7 ms                                                | 14.7 ms: 1.07x slower                                              |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-darwin-arm64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text    | 16.9 ms                                                | 13.6 ms: 1.24x faster                                              |
| genshi_xml     | 34.1 ms                                                | 28.4 ms: 1.20x faster                                              |
| mako           | 7.75 ms                                                | 7.62 ms: 1.02x faster                                              |
| Geometric mean | (ref)                                                  | 1.11x faster                                                       |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-darwin-arm64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 742 ms: 2.02x faster                                               |
| deepcopy                         | 236 us                                                 | 147 us: 1.60x faster                                               |
| async_tree_memoization_tg        | 288 ms                                                 | 184 ms: 1.56x faster                                               |
| deepcopy_memo                    | 27.4 us                                                | 18.1 us: 1.52x faster                                              |
| go                               | 117 ms                                                 | 78.6 ms: 1.48x faster                                              |
| async_tree_io                    | 508 ms                                                 | 354 ms: 1.44x faster                                               |
| async_tree_io_tg                 | 500 ms                                                 | 351 ms: 1.43x faster                                               |
| async_tree_eager_io              | 511 ms                                                 | 359 ms: 1.42x faster                                               |
| async_tree_memoization           | 268 ms                                                 | 190 ms: 1.41x faster                                               |
| generators                       | 31.9 ms                                                | 23.2 ms: 1.37x faster                                              |
| scimark_sor                      | 106 ms                                                 | 77.6 ms: 1.36x faster                                              |
| async_tree_eager_io_tg           | 479 ms                                                 | 360 ms: 1.33x faster                                               |
| async_tree_none                  | 212 ms                                                 | 159 ms: 1.33x faster                                               |
| deepcopy_reduce                  | 2.09 us                                                | 1.59 us: 1.32x faster                                              |
| async_tree_none_tg               | 198 ms                                                 | 151 ms: 1.31x faster                                               |
| tomli_loads                      | 1.57 sec                                               | 1.21 sec: 1.29x faster                                             |
| html5lib                         | 36.7 ms                                                | 29.2 ms: 1.25x faster                                              |
| async_tree_eager_memoization     | 168 ms                                                 | 135 ms: 1.25x faster                                               |
| genshi_text                      | 16.9 ms                                                | 13.6 ms: 1.24x faster                                              |
| pyflate                          | 352 ms                                                 | 286 ms: 1.23x faster                                               |
| coroutines                       | 20.0 ms                                                | 16.3 ms: 1.23x faster                                              |
| float                            | 55.8 ms                                                | 45.7 ms: 1.22x faster                                              |
| genshi_xml                       | 34.1 ms                                                | 28.4 ms: 1.20x faster                                              |
| scimark_monte_carlo              | 50.4 ms                                                | 42.0 ms: 1.20x faster                                              |
| dulwich_log                      | 28.7 ms                                                | 24.0 ms: 1.20x faster                                              |
| async_generators                 | 294 ms                                                 | 246 ms: 1.20x faster                                               |
| regex_compile                    | 78.3 ms                                                | 66.1 ms: 1.18x faster                                              |
| async_tree_eager                 | 69.9 ms                                                | 59.9 ms: 1.17x faster                                              |
| regex_effbot                     | 2.63 ms                                                | 2.26 ms: 1.16x faster                                              |
| unpickle_pure_python             | 165 us                                                 | 143 us: 1.16x faster                                               |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 399 ms: 1.15x faster                                               |
| hexiom                           | 4.87 ms                                                | 4.23 ms: 1.15x faster                                              |
| deltablue                        | 2.65 ms                                                | 2.30 ms: 1.15x faster                                              |
| pprint_pformat                   | 1.10 sec                                               | 964 ms: 1.14x faster                                               |
| pprint_safe_repr                 | 541 ms                                                 | 477 ms: 1.13x faster                                               |
| pylint                           | 180 ms                                                 | 159 ms: 1.13x faster                                               |
| spectral_norm                    | 76.5 ms                                                | 68.2 ms: 1.12x faster                                              |
| richards                         | 36.2 ms                                                | 32.3 ms: 1.12x faster                                              |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 402 ms: 1.11x faster                                               |
| 2to3                             | 179 ms                                                 | 160 ms: 1.11x faster                                               |
| bpe_tokeniser                    | 3.26 sec                                               | 2.93 sec: 1.11x faster                                             |
| chaos                            | 41.1 ms                                                | 37.3 ms: 1.10x faster                                              |
| logging_silent                   | 71.0 ns                                                | 64.8 ns: 1.09x faster                                              |
| scimark_fft                      | 200 ms                                                 | 183 ms: 1.09x faster                                               |
| logging_simple                   | 3.56 us                                                | 3.28 us: 1.09x faster                                              |
| regex_v8                         | 17.0 ms                                                | 15.7 ms: 1.09x faster                                              |
| xml_etree_process                | 41.3 ms                                                | 38.1 ms: 1.09x faster                                              |
| pycparser                        | 701 ms                                                 | 646 ms: 1.09x faster                                               |
| typing_runtime_protocols         | 101 us                                                 | 93.1 us: 1.08x faster                                              |
| nqueens                          | 61.8 ms                                                | 57.2 ms: 1.08x faster                                              |
| raytrace                         | 181 ms                                                 | 168 ms: 1.08x faster                                               |
| richards_super                   | 39.2 ms                                                | 36.3 ms: 1.08x faster                                              |
| logging_format                   | 3.85 us                                                | 3.58 us: 1.08x faster                                              |
| sympy_expand                     | 248 ms                                                 | 230 ms: 1.08x faster                                               |
| sympy_integrate                  | 11.3 ms                                                | 10.5 ms: 1.08x faster                                              |
| fannkuch                         | 279 ms                                                 | 260 ms: 1.07x faster                                               |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 347 ms: 1.07x faster                                               |
| comprehensions                   | 12.0 us                                                | 11.2 us: 1.07x faster                                              |
| sympy_str                        | 146 ms                                                 | 136 ms: 1.07x faster                                               |
| pickle_pure_python               | 215 us                                                 | 201 us: 1.07x faster                                               |
| xml_etree_generate               | 57.1 ms                                                | 53.5 ms: 1.07x faster                                              |
| telco                            | 4.84 ms                                                | 4.54 ms: 1.07x faster                                              |
| k_core                           | 1.61 sec                                               | 1.51 sec: 1.06x faster                                             |
| regex_dna                        | 149 ms                                                 | 140 ms: 1.06x faster                                               |
| connected_components             | 319 ms                                                 | 303 ms: 1.05x faster                                               |
| sphinx                           | 602 ms                                                 | 574 ms: 1.05x faster                                               |
| shortest_path                    | 345 ms                                                 | 330 ms: 1.05x faster                                               |
| nbody                            | 73.6 ms                                                | 70.7 ms: 1.04x faster                                              |
| xml_etree_iterparse              | 74.2 ms                                                | 71.6 ms: 1.04x faster                                              |
| sympy_sum                        | 75.1 ms                                                | 72.8 ms: 1.03x faster                                              |
| meteor_contest                   | 74.0 ms                                                | 71.9 ms: 1.03x faster                                              |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.52 ms: 1.03x faster                                              |
| scimark_lu                       | 75.9 ms                                                | 74.1 ms: 1.03x faster                                              |
| docutils                         | 1.44 sec                                               | 1.42 sec: 1.02x faster                                             |
| mako                             | 7.75 ms                                                | 7.62 ms: 1.02x faster                                              |
| bench_thread_pool                | 503 us                                                 | 497 us: 1.01x faster                                               |
| sqlalchemy_declarative           | 59.0 ms                                                | 58.4 ms: 1.01x faster                                              |
| crypto_pyaes                     | 55.3 ms                                                | 54.8 ms: 1.01x faster                                              |
| sqlite_synth                     | 1.55 us                                                | 1.55 us: 1.00x faster                                              |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                               |
| xml_etree_parse                  | 108 ms                                                 | 109 ms: 1.01x slower                                               |
| bench_mp_pool                    | 64.7 ms                                                | 65.7 ms: 1.02x slower                                              |
| coverage                         | 46.2 ms                                                | 47.6 ms: 1.03x slower                                              |
| json_loads                       | 17.0 us                                                | 17.6 us: 1.03x slower                                              |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.09 ms: 1.04x slower                                              |
| gc_traversal                     | 2.94 ms                                                | 3.10 ms: 1.06x slower                                              |
| python_startup                   | 18.8 ms                                                | 19.9 ms: 1.06x slower                                              |
| create_gc_cycles                 | 1.19 ms                                                | 1.28 ms: 1.07x slower                                              |
| python_startup_no_site           | 13.7 ms                                                | 14.7 ms: 1.07x slower                                              |
| many_optionals                   | 409 us                                                 | 439 us: 1.07x slower                                               |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 378 ms: 1.09x slower                                               |
| json_dumps                       | 6.47 ms                                                | 7.37 ms: 1.14x slower                                              |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 167 ms: 1.21x slower                                               |
| subparsers                       | 9.44 ms                                                | 12.0 ms: 1.27x slower                                              |
| async_tree_eager_tg              | 47.4 ms                                                | 130 ms: 2.74x slower                                               |
| Geometric mean                   | (ref)                                                  | 1.10x faster                                                       |

Benchmark hidden because not significant (4): json, asyncio_websockets, django_template, pathlib
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250425-3.14.0a7+-dac50cc/bm-20250425-darwin-arm64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.105x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.10x