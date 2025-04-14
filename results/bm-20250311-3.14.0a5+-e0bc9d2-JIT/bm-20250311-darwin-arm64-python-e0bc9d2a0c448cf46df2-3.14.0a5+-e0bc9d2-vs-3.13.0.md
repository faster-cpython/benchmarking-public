# Results vs. 3.13.0

- fork: python
- ref: e0bc9d2a0c448cf46df2
- machine: darwin-arm64
- commit hash: e0bc9d2
- commit date: 2025-03-11
- overall geometric mean: 1.009x faster
- HPT reliability: 85.78%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250311-darwin-arm64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 176 ms: 1.01x faster                                                   |
| docutils       | 1.44 sec                                               | 1.54 sec: 1.07x slower                                                 |
| html5lib       | 36.7 ms                                                | 33.1 ms: 1.11x faster                                                  |
| sphinx         | 602 ms                                                 | 614 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250311-darwin-arm64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 207 ms: 1.39x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 389 ms: 1.31x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 391 ms: 1.28x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 212 ms: 1.27x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 403 ms: 1.26x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 175 ms: 1.21x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 399 ms: 1.20x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 167 ms: 1.19x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 150 ms: 1.12x faster                                                   |
| coroutines                       | 20.0 ms                                                | 17.9 ms: 1.12x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 438 ms: 1.05x faster                                                   |
| async_tree_eager                 | 69.9 ms                                                | 67.9 ms: 1.03x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 435 ms: 1.03x faster                                                   |
| async_generators                 | 294 ms                                                 | 290 ms: 1.01x faster                                                   |
| asyncio_websockets               | 242 ms                                                 | 251 ms: 1.03x slower                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 410 ms: 1.18x slower                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 186 ms: 1.35x slower                                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 138 ms: 2.91x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (1): async_tree_eager_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250311-darwin-arm64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 47.3 ms: 1.18x faster                                                  |
| nbody          | 73.6 ms                                                | 72.0 ms: 1.02x faster                                                  |
| pidigits       | 284 ms                                                 | 293 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250311-darwin-arm64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.33 ms: 1.13x faster                                                  |
| regex_v8       | 17.0 ms                                                | 16.5 ms: 1.03x faster                                                  |
| regex_dna      | 149 ms                                                 | 145 ms: 1.03x faster                                                   |
| regex_compile  | 78.3 ms                                                | 77.3 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250311-darwin-arm64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.31 sec: 1.20x faster                                                 |
| unpickle_pure_python | 165 us                                                 | 148 us: 1.12x faster                                                   |
| xml_etree_process    | 41.3 ms                                                | 37.8 ms: 1.09x faster                                                  |
| xml_etree_generate   | 57.1 ms                                                | 53.3 ms: 1.07x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 102 ms: 1.05x faster                                                   |
| pickle_pure_python   | 215 us                                                 | 221 us: 1.03x slower                                                   |
| json_loads           | 17.0 us                                                | 18.2 us: 1.07x slower                                                  |
| json_dumps           | 6.47 ms                                                | 7.47 ms: 1.16x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250311-darwin-arm64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 17.9 ms: 1.05x faster                                                  |
| python_startup_no_site | 13.7 ms                                                | 13.5 ms: 1.02x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250311-darwin-arm64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 7.75 ms                                                | 6.94 ms: 1.12x faster                                                  |
| genshi_text     | 16.9 ms                                                | 15.9 ms: 1.07x faster                                                  |
| genshi_xml      | 34.1 ms                                                | 32.8 ms: 1.04x faster                                                  |
| django_template | 20.5 ms                                                | 23.6 ms: 1.15x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250311-darwin-arm64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy                         | 236 us                                                 | 168 us: 1.40x faster                                                   |
| async_tree_memoization_tg        | 288 ms                                                 | 207 ms: 1.39x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 389 ms: 1.31x faster                                                   |
| deepcopy_memo                    | 27.4 us                                                | 21.4 us: 1.28x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 391 ms: 1.28x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 212 ms: 1.27x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 403 ms: 1.26x faster                                                   |
| generators                       | 31.9 ms                                                | 25.8 ms: 1.24x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 175 ms: 1.21x faster                                                   |
| tomli_loads                      | 1.57 sec                                               | 1.31 sec: 1.20x faster                                                 |
| async_tree_eager_io_tg           | 479 ms                                                 | 399 ms: 1.20x faster                                                   |
| deepcopy_reduce                  | 2.09 us                                                | 1.76 us: 1.19x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 167 ms: 1.19x faster                                                   |
| float                            | 55.8 ms                                                | 47.3 ms: 1.18x faster                                                  |
| scimark_sor                      | 106 ms                                                 | 91.7 ms: 1.15x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 66.6 ms: 1.15x faster                                                  |
| deltablue                        | 2.65 ms                                                | 2.33 ms: 1.14x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.33 ms: 1.13x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 150 ms: 1.12x faster                                                   |
| coroutines                       | 20.0 ms                                                | 17.9 ms: 1.12x faster                                                  |
| mako                             | 7.75 ms                                                | 6.94 ms: 1.12x faster                                                  |
| unpickle_pure_python             | 165 us                                                 | 148 us: 1.12x faster                                                   |
| go                               | 117 ms                                                 | 105 ms: 1.11x faster                                                   |
| html5lib                         | 36.7 ms                                                | 33.1 ms: 1.11x faster                                                  |
| xml_etree_process                | 41.3 ms                                                | 37.8 ms: 1.09x faster                                                  |
| richards                         | 36.2 ms                                                | 33.6 ms: 1.08x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 26.7 ms: 1.08x faster                                                  |
| xml_etree_generate               | 57.1 ms                                                | 53.3 ms: 1.07x faster                                                  |
| genshi_text                      | 16.9 ms                                                | 15.9 ms: 1.07x faster                                                  |
| richards_super                   | 39.2 ms                                                | 36.9 ms: 1.06x faster                                                  |
| pyflate                          | 352 ms                                                 | 333 ms: 1.06x faster                                                   |
| xml_etree_parse                  | 108 ms                                                 | 102 ms: 1.05x faster                                                   |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 438 ms: 1.05x faster                                                   |
| python_startup                   | 18.8 ms                                                | 17.9 ms: 1.05x faster                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 48.6 ms: 1.04x faster                                                  |
| genshi_xml                       | 34.1 ms                                                | 32.8 ms: 1.04x faster                                                  |
| regex_v8                         | 17.0 ms                                                | 16.5 ms: 1.03x faster                                                  |
| async_tree_eager                 | 69.9 ms                                                | 67.9 ms: 1.03x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 435 ms: 1.03x faster                                                   |
| connected_components             | 319 ms                                                 | 310 ms: 1.03x faster                                                   |
| bpe_tokeniser                    | 3.26 sec                                               | 3.17 sec: 1.03x faster                                                 |
| regex_dna                        | 149 ms                                                 | 145 ms: 1.03x faster                                                   |
| nbody                            | 73.6 ms                                                | 72.0 ms: 1.02x faster                                                  |
| k_core                           | 1.61 sec                                               | 1.58 sec: 1.02x faster                                                 |
| python_startup_no_site           | 13.7 ms                                                | 13.5 ms: 1.02x faster                                                  |
| shortest_path                    | 345 ms                                                 | 340 ms: 1.02x faster                                                   |
| telco                            | 4.84 ms                                                | 4.76 ms: 1.02x faster                                                  |
| 2to3                             | 179 ms                                                 | 176 ms: 1.01x faster                                                   |
| async_generators                 | 294 ms                                                 | 290 ms: 1.01x faster                                                   |
| regex_compile                    | 78.3 ms                                                | 77.3 ms: 1.01x faster                                                  |
| dask                             | 771 ms                                                 | 768 ms: 1.00x faster                                                   |
| pprint_safe_repr                 | 541 ms                                                 | 544 ms: 1.01x slower                                                   |
| scimark_fft                      | 200 ms                                                 | 201 ms: 1.01x slower                                                   |
| typing_runtime_protocols         | 101 us                                                 | 101 us: 1.01x slower                                                   |
| thrift                           | 466 us                                                 | 471 us: 1.01x slower                                                   |
| pathlib                          | 23.2 ms                                                | 23.6 ms: 1.02x slower                                                  |
| sphinx                           | 602 ms                                                 | 614 ms: 1.02x slower                                                   |
| bench_thread_pool                | 503 us                                                 | 516 us: 1.02x slower                                                   |
| mdp                              | 1.50 sec                                               | 1.54 sec: 1.03x slower                                                 |
| pickle_pure_python               | 215 us                                                 | 221 us: 1.03x slower                                                   |
| pidigits                         | 284 ms                                                 | 293 ms: 1.03x slower                                                   |
| json                             | 3.04 ms                                                | 3.14 ms: 1.03x slower                                                  |
| asyncio_websockets               | 242 ms                                                 | 251 ms: 1.03x slower                                                   |
| sqlite_synth                     | 1.55 us                                                | 1.61 us: 1.04x slower                                                  |
| sympy_expand                     | 248 ms                                                 | 258 ms: 1.04x slower                                                   |
| sympy_str                        | 146 ms                                                 | 152 ms: 1.04x slower                                                   |
| coverage                         | 46.2 ms                                                | 48.3 ms: 1.04x slower                                                  |
| logging_simple                   | 3.56 us                                                | 3.73 us: 1.05x slower                                                  |
| logging_silent                   | 71.0 ns                                                | 74.5 ns: 1.05x slower                                                  |
| sympy_sum                        | 75.1 ms                                                | 79.0 ms: 1.05x slower                                                  |
| logging_format                   | 3.85 us                                                | 4.07 us: 1.06x slower                                                  |
| pycparser                        | 701 ms                                                 | 741 ms: 1.06x slower                                                   |
| docutils                         | 1.44 sec                                               | 1.54 sec: 1.07x slower                                                 |
| hexiom                           | 4.87 ms                                                | 5.19 ms: 1.07x slower                                                  |
| scimark_lu                       | 75.9 ms                                                | 81.1 ms: 1.07x slower                                                  |
| sqlalchemy_declarative           | 59.0 ms                                                | 63.1 ms: 1.07x slower                                                  |
| json_loads                       | 17.0 us                                                | 18.2 us: 1.07x slower                                                  |
| meteor_contest                   | 74.0 ms                                                | 79.4 ms: 1.07x slower                                                  |
| sqlalchemy_imperative            | 6.69 ms                                                | 7.23 ms: 1.08x slower                                                  |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.23 ms: 1.08x slower                                                  |
| comprehensions                   | 12.0 us                                                | 13.0 us: 1.09x slower                                                  |
| sympy_integrate                  | 11.3 ms                                                | 12.4 ms: 1.09x slower                                                  |
| gc_traversal                     | 2.94 ms                                                | 3.23 ms: 1.10x slower                                                  |
| raytrace                         | 181 ms                                                 | 200 ms: 1.10x slower                                                   |
| fannkuch                         | 279 ms                                                 | 308 ms: 1.11x slower                                                   |
| chaos                            | 41.1 ms                                                | 45.5 ms: 1.11x slower                                                  |
| nqueens                          | 61.8 ms                                                | 68.8 ms: 1.11x slower                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 1.33 ms: 1.12x slower                                                  |
| crypto_pyaes                     | 55.3 ms                                                | 62.7 ms: 1.13x slower                                                  |
| django_template                  | 20.5 ms                                                | 23.6 ms: 1.15x slower                                                  |
| json_dumps                       | 6.47 ms                                                | 7.47 ms: 1.16x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 410 ms: 1.18x slower                                                   |
| many_optionals                   | 409 us                                                 | 488 us: 1.19x slower                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 186 ms: 1.35x slower                                                   |
| subparsers                       | 9.44 ms                                                | 12.9 ms: 1.37x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 138 ms: 2.91x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (5): pylint, bench_mp_pool, xml_etree_iterparse, async_tree_eager_cpu_io_mixed, pprint_pformat
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250311-3.14.0a5+-e0bc9d2-JIT/bm-20250311-darwin-arm64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.009x faster

# HPT report

- Reliability score: 85.78% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x