# Results vs. 3.13.0

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: darwin-arm64
- commit hash: c41d531
- commit date: 2025-06-16
- overall geometric mean: 1.010x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250616-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 170 ms: 1.05x faster                                                            |
| docutils       | 1.44 sec                                               | 1.45 sec: 1.01x slower                                                          |
| html5lib       | 36.7 ms                                                | 31.7 ms: 1.16x faster                                                           |
| sphinx         | 602 ms                                                 | 580 ms: 1.04x faster                                                            |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250616-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 192 ms: 1.50x faster                                                            |
| async_tree_eager_io              | 511 ms                                                 | 363 ms: 1.41x faster                                                            |
| async_tree_memoization           | 268 ms                                                 | 195 ms: 1.38x faster                                                            |
| async_tree_io_tg                 | 500 ms                                                 | 367 ms: 1.36x faster                                                            |
| async_tree_io                    | 508 ms                                                 | 379 ms: 1.34x faster                                                            |
| async_tree_none                  | 212 ms                                                 | 163 ms: 1.29x faster                                                            |
| async_tree_eager_io_tg           | 479 ms                                                 | 373 ms: 1.28x faster                                                            |
| async_tree_none_tg               | 198 ms                                                 | 156 ms: 1.27x faster                                                            |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.20x faster                                                            |
| coroutines                       | 20.0 ms                                                | 16.9 ms: 1.18x faster                                                           |
| async_generators                 | 294 ms                                                 | 261 ms: 1.12x faster                                                            |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 414 ms: 1.11x faster                                                            |
| async_tree_eager                 | 69.9 ms                                                | 63.6 ms: 1.10x faster                                                           |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 410 ms: 1.09x faster                                                            |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 357 ms: 1.04x faster                                                            |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 388 ms: 1.12x slower                                                            |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 168 ms: 1.22x slower                                                            |
| async_tree_eager_tg              | 47.4 ms                                                | 129 ms: 2.72x slower                                                            |
| Geometric mean                   | (ref)                                                  | 1.11x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250616-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 49.9 ms: 1.12x faster                                                           |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                                            |
| nbody          | 73.6 ms                                                | 74.2 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250616-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.37 ms: 1.11x faster                                                           |
| regex_compile  | 78.3 ms                                                | 71.8 ms: 1.09x faster                                                           |
| regex_v8       | 17.0 ms                                                | 16.2 ms: 1.05x faster                                                           |
| regex_dna      | 149 ms                                                 | 143 ms: 1.04x faster                                                            |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250616-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.36 sec: 1.15x faster                                                          |
| xml_etree_parse      | 108 ms                                                 | 100 ms: 1.08x faster                                                            |
| xml_etree_generate   | 57.1 ms                                                | 53.3 ms: 1.07x faster                                                           |
| xml_etree_process    | 41.3 ms                                                | 38.6 ms: 1.07x faster                                                           |
| unpickle_pure_python | 165 us                                                 | 158 us: 1.04x faster                                                            |
| json_loads           | 17.0 us                                                | 16.4 us: 1.04x faster                                                           |
| xml_etree_iterparse  | 74.2 ms                                                | 72.7 ms: 1.02x faster                                                           |
| pickle_pure_python   | 215 us                                                 | 217 us: 1.01x slower                                                            |
| json_dumps           | 6.47 ms                                                | 6.61 ms: 1.02x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250616-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 17.7 ms: 1.06x faster                                                           |
| python_startup_no_site | 13.7 ms                                                | 13.3 ms: 1.04x faster                                                           |
| Geometric mean         | (ref)                                                  | 1.05x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250616-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 14.6 ms: 1.16x faster                                                           |
| genshi_xml      | 34.1 ms                                                | 30.9 ms: 1.10x faster                                                           |
| django_template | 20.5 ms                                                | 21.9 ms: 1.07x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                                    |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250616-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 759 ms: 1.97x faster                                                            |
| deepcopy                         | 236 us                                                 | 157 us: 1.51x faster                                                            |
| async_tree_memoization_tg        | 288 ms                                                 | 192 ms: 1.50x faster                                                            |
| deepcopy_memo                    | 27.4 us                                                | 19.4 us: 1.42x faster                                                           |
| async_tree_eager_io              | 511 ms                                                 | 363 ms: 1.41x faster                                                            |
| async_tree_memoization           | 268 ms                                                 | 195 ms: 1.38x faster                                                            |
| async_tree_io_tg                 | 500 ms                                                 | 367 ms: 1.36x faster                                                            |
| async_tree_io                    | 508 ms                                                 | 379 ms: 1.34x faster                                                            |
| go                               | 117 ms                                                 | 87.5 ms: 1.33x faster                                                           |
| generators                       | 31.9 ms                                                | 24.1 ms: 1.33x faster                                                           |
| async_tree_none                  | 212 ms                                                 | 163 ms: 1.29x faster                                                            |
| async_tree_eager_io_tg           | 479 ms                                                 | 373 ms: 1.28x faster                                                            |
| async_tree_none_tg               | 198 ms                                                 | 156 ms: 1.27x faster                                                            |
| deepcopy_reduce                  | 2.09 us                                                | 1.69 us: 1.24x faster                                                           |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.20x faster                                                            |
| scimark_sor                      | 106 ms                                                 | 88.6 ms: 1.19x faster                                                           |
| coroutines                       | 20.0 ms                                                | 16.9 ms: 1.18x faster                                                           |
| genshi_text                      | 16.9 ms                                                | 14.6 ms: 1.16x faster                                                           |
| html5lib                         | 36.7 ms                                                | 31.7 ms: 1.16x faster                                                           |
| tomli_loads                      | 1.57 sec                                               | 1.36 sec: 1.15x faster                                                          |
| dulwich_log                      | 28.7 ms                                                | 25.0 ms: 1.15x faster                                                           |
| async_generators                 | 294 ms                                                 | 261 ms: 1.12x faster                                                            |
| float                            | 55.8 ms                                                | 49.9 ms: 1.12x faster                                                           |
| pylint                           | 180 ms                                                 | 161 ms: 1.12x faster                                                            |
| regex_effbot                     | 2.63 ms                                                | 2.37 ms: 1.11x faster                                                           |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 414 ms: 1.11x faster                                                            |
| pyflate                          | 352 ms                                                 | 318 ms: 1.11x faster                                                            |
| genshi_xml                       | 34.1 ms                                                | 30.9 ms: 1.10x faster                                                           |
| async_tree_eager                 | 69.9 ms                                                | 63.6 ms: 1.10x faster                                                           |
| k_core                           | 1.61 sec                                               | 1.47 sec: 1.10x faster                                                          |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 410 ms: 1.09x faster                                                            |
| regex_compile                    | 78.3 ms                                                | 71.8 ms: 1.09x faster                                                           |
| scimark_monte_carlo              | 50.4 ms                                                | 46.4 ms: 1.09x faster                                                           |
| xml_etree_parse                  | 108 ms                                                 | 100 ms: 1.08x faster                                                            |
| spectral_norm                    | 76.5 ms                                                | 71.0 ms: 1.08x faster                                                           |
| xml_etree_generate               | 57.1 ms                                                | 53.3 ms: 1.07x faster                                                           |
| xml_etree_process                | 41.3 ms                                                | 38.6 ms: 1.07x faster                                                           |
| bpe_tokeniser                    | 3.26 sec                                               | 3.06 sec: 1.07x faster                                                          |
| telco                            | 4.84 ms                                                | 4.54 ms: 1.07x faster                                                           |
| python_startup                   | 18.8 ms                                                | 17.7 ms: 1.06x faster                                                           |
| 2to3                             | 179 ms                                                 | 170 ms: 1.05x faster                                                            |
| regex_v8                         | 17.0 ms                                                | 16.2 ms: 1.05x faster                                                           |
| hexiom                           | 4.87 ms                                                | 4.66 ms: 1.04x faster                                                           |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 357 ms: 1.04x faster                                                            |
| unpickle_pure_python             | 165 us                                                 | 158 us: 1.04x faster                                                            |
| json                             | 3.04 ms                                                | 2.92 ms: 1.04x faster                                                           |
| shortest_path                    | 345 ms                                                 | 332 ms: 1.04x faster                                                            |
| json_loads                       | 17.0 us                                                | 16.4 us: 1.04x faster                                                           |
| sphinx                           | 602 ms                                                 | 580 ms: 1.04x faster                                                            |
| regex_dna                        | 149 ms                                                 | 143 ms: 1.04x faster                                                            |
| chaos                            | 41.1 ms                                                | 39.7 ms: 1.04x faster                                                           |
| python_startup_no_site           | 13.7 ms                                                | 13.3 ms: 1.04x faster                                                           |
| sympy_expand                     | 248 ms                                                 | 239 ms: 1.03x faster                                                            |
| pathlib                          | 23.2 ms                                                | 22.4 ms: 1.03x faster                                                           |
| fannkuch                         | 279 ms                                                 | 270 ms: 1.03x faster                                                            |
| pycparser                        | 701 ms                                                 | 679 ms: 1.03x faster                                                            |
| sympy_integrate                  | 11.3 ms                                                | 11.0 ms: 1.03x faster                                                           |
| sympy_str                        | 146 ms                                                 | 142 ms: 1.03x faster                                                            |
| connected_components             | 319 ms                                                 | 311 ms: 1.02x faster                                                            |
| deltablue                        | 2.65 ms                                                | 2.59 ms: 1.02x faster                                                           |
| xml_etree_iterparse              | 74.2 ms                                                | 72.7 ms: 1.02x faster                                                           |
| nqueens                          | 61.8 ms                                                | 60.7 ms: 1.02x faster                                                           |
| scimark_fft                      | 200 ms                                                 | 196 ms: 1.02x faster                                                            |
| meteor_contest                   | 74.0 ms                                                | 72.8 ms: 1.02x faster                                                           |
| raytrace                         | 181 ms                                                 | 180 ms: 1.00x faster                                                            |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                                            |
| docutils                         | 1.44 sec                                               | 1.45 sec: 1.01x slower                                                          |
| nbody                            | 73.6 ms                                                | 74.2 ms: 1.01x slower                                                           |
| richards                         | 36.2 ms                                                | 36.5 ms: 1.01x slower                                                           |
| pickle_pure_python               | 215 us                                                 | 217 us: 1.01x slower                                                            |
| crypto_pyaes                     | 55.3 ms                                                | 56.5 ms: 1.02x slower                                                           |
| json_dumps                       | 6.47 ms                                                | 6.61 ms: 1.02x slower                                                           |
| logging_format                   | 3.85 us                                                | 3.97 us: 1.03x slower                                                           |
| logging_simple                   | 3.56 us                                                | 3.67 us: 1.03x slower                                                           |
| sqlite_synth                     | 1.55 us                                                | 1.60 us: 1.03x slower                                                           |
| pprint_pformat                   | 1.10 sec                                               | 1.14 sec: 1.04x slower                                                          |
| comprehensions                   | 12.0 us                                                | 12.4 us: 1.04x slower                                                           |
| pprint_safe_repr                 | 541 ms                                                 | 562 ms: 1.04x slower                                                            |
| richards_super                   | 39.2 ms                                                | 40.9 ms: 1.04x slower                                                           |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.16 ms: 1.06x slower                                                           |
| django_template                  | 20.5 ms                                                | 21.9 ms: 1.07x slower                                                           |
| scimark_lu                       | 75.9 ms                                                | 82.0 ms: 1.08x slower                                                           |
| gc_traversal                     | 2.94 ms                                                | 3.18 ms: 1.08x slower                                                           |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 388 ms: 1.12x slower                                                            |
| create_gc_cycles                 | 1.19 ms                                                | 1.35 ms: 1.14x slower                                                           |
| many_optionals                   | 409 us                                                 | 467 us: 1.14x slower                                                            |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 168 ms: 1.22x slower                                                            |
| subparsers                       | 9.44 ms                                                | 13.6 ms: 1.44x slower                                                           |
| async_tree_eager_tg              | 47.4 ms                                                | 129 ms: 2.72x slower                                                            |
| logging_silent                   | 71.0 ns                                                | 323 ns: 4.55x slower                                                            |
| coverage                         | 46.2 ms                                                | 290 ms: 6.27x slower                                                            |
| thrift                           | 466 us                                                 | 43.6 ms: 93.60x slower                                                          |
| Geometric mean                   | (ref)                                                  | 1.02x slower                                                                    |

Benchmark hidden because not significant (5): sympy_sum, dask, typing_runtime_protocols, asyncio_websockets, mako
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250616-3.15.0a0-c41d531/bm-20250616-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.010x slower

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.11x