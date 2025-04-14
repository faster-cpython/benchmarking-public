# Results vs. 3.13.0

- fork: python
- ref: d7bb7c781771650a4edc
- machine: darwin-arm64
- commit hash: d7bb7c7
- commit date: 2025-03-05
- overall geometric mean: 1.009x slower
- HPT reliability: 68.17%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250305-darwin-arm64-python-d7bb7c781771650a4edc-3.14.0a5+-d7bb7c7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 175 ms: 1.02x faster                                                   |
| docutils       | 1.44 sec                                               | 1.50 sec: 1.04x slower                                                 |
| html5lib       | 36.7 ms                                                | 33.1 ms: 1.11x faster                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250305-darwin-arm64-python-d7bb7c781771650a4edc-3.14.0a5+-d7bb7c7 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 212 ms: 1.35x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 393 ms: 1.30x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 397 ms: 1.28x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 402 ms: 1.24x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 222 ms: 1.21x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 178 ms: 1.19x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 404 ms: 1.18x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 171 ms: 1.16x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 150 ms: 1.12x faster                                                   |
| async_generators                 | 294 ms                                                 | 269 ms: 1.09x faster                                                   |
| coroutines                       | 20.0 ms                                                | 18.5 ms: 1.08x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 437 ms: 1.05x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 428 ms: 1.05x faster                                                   |
| async_tree_eager                 | 69.9 ms                                                | 68.2 ms: 1.02x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 366 ms: 1.02x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 402 ms: 1.16x slower                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 189 ms: 1.37x slower                                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 142 ms: 2.99x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250305-darwin-arm64-python-d7bb7c781771650a4edc-3.14.0a5+-d7bb7c7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 54.3 ms: 1.03x faster                                                  |
| pidigits       | 284 ms                                                 | 284 ms: 1.00x slower                                                   |
| nbody          | 73.6 ms                                                | 92.5 ms: 1.26x slower                                                  |
| Geometric mean | (ref)                                                  | 1.07x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250305-darwin-arm64-python-d7bb7c781771650a4edc-3.14.0a5+-d7bb7c7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.24 ms: 1.17x faster                                                  |
| regex_dna      | 149 ms                                                 | 140 ms: 1.06x faster                                                   |
| regex_v8       | 17.0 ms                                                | 16.7 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250305-darwin-arm64-python-d7bb7c781771650a4edc-3.14.0a5+-d7bb7c7 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.44 sec: 1.09x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 104 ms: 1.04x faster                                                   |
| xml_etree_generate   | 57.1 ms                                                | 58.1 ms: 1.02x slower                                                  |
| unpickle_pure_python | 165 us                                                 | 170 us: 1.03x slower                                                   |
| xml_etree_process    | 41.3 ms                                                | 42.8 ms: 1.04x slower                                                  |
| json_loads           | 17.0 us                                                | 17.8 us: 1.04x slower                                                  |
| pickle_pure_python   | 215 us                                                 | 231 us: 1.08x slower                                                   |
| json_dumps           | 6.47 ms                                                | 7.52 ms: 1.16x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x slower                                                           |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250305-darwin-arm64-python-d7bb7c781771650a4edc-3.14.0a5+-d7bb7c7 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 19.1 ms: 1.01x slower                                                  |
| python_startup_no_site | 13.7 ms                                                | 14.1 ms: 1.03x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250305-darwin-arm64-python-d7bb7c781771650a4edc-3.14.0a5+-d7bb7c7 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 16.2 ms: 1.04x faster                                                  |
| genshi_xml      | 34.1 ms                                                | 33.6 ms: 1.01x faster                                                  |
| mako            | 7.75 ms                                                | 8.39 ms: 1.08x slower                                                  |
| django_template | 20.5 ms                                                | 24.3 ms: 1.19x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250305-darwin-arm64-python-d7bb7c781771650a4edc-3.14.0a5+-d7bb7c7 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy                         | 236 us                                                 | 168 us: 1.41x faster                                                   |
| async_tree_memoization_tg        | 288 ms                                                 | 212 ms: 1.35x faster                                                   |
| deepcopy_memo                    | 27.4 us                                                | 20.9 us: 1.31x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 393 ms: 1.30x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 397 ms: 1.28x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 402 ms: 1.24x faster                                                   |
| go                               | 117 ms                                                 | 95.1 ms: 1.23x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 222 ms: 1.21x faster                                                   |
| deepcopy_reduce                  | 2.09 us                                                | 1.76 us: 1.19x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 178 ms: 1.19x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 404 ms: 1.18x faster                                                   |
| regex_effbot                     | 2.63 ms                                                | 2.24 ms: 1.17x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 171 ms: 1.16x faster                                                   |
| scimark_sor                      | 106 ms                                                 | 92.7 ms: 1.14x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 150 ms: 1.12x faster                                                   |
| html5lib                         | 36.7 ms                                                | 33.1 ms: 1.11x faster                                                  |
| generators                       | 31.9 ms                                                | 29.0 ms: 1.10x faster                                                  |
| async_generators                 | 294 ms                                                 | 269 ms: 1.09x faster                                                   |
| tomli_loads                      | 1.57 sec                                               | 1.44 sec: 1.09x faster                                                 |
| coroutines                       | 20.0 ms                                                | 18.5 ms: 1.08x faster                                                  |
| regex_dna                        | 149 ms                                                 | 140 ms: 1.06x faster                                                   |
| bench_mp_pool                    | 64.7 ms                                                | 61.3 ms: 1.06x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 437 ms: 1.05x faster                                                   |
| k_core                           | 1.61 sec                                               | 1.54 sec: 1.05x faster                                                 |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 428 ms: 1.05x faster                                                   |
| genshi_text                      | 16.9 ms                                                | 16.2 ms: 1.04x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 104 ms: 1.04x faster                                                   |
| float                            | 55.8 ms                                                | 54.3 ms: 1.03x faster                                                  |
| async_tree_eager                 | 69.9 ms                                                | 68.2 ms: 1.02x faster                                                  |
| 2to3                             | 179 ms                                                 | 175 ms: 1.02x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 366 ms: 1.02x faster                                                   |
| regex_v8                         | 17.0 ms                                                | 16.7 ms: 1.02x faster                                                  |
| telco                            | 4.84 ms                                                | 4.76 ms: 1.02x faster                                                  |
| scimark_fft                      | 200 ms                                                 | 196 ms: 1.02x faster                                                   |
| shortest_path                    | 345 ms                                                 | 340 ms: 1.02x faster                                                   |
| genshi_xml                       | 34.1 ms                                                | 33.6 ms: 1.01x faster                                                  |
| connected_components             | 319 ms                                                 | 315 ms: 1.01x faster                                                   |
| scimark_monte_carlo              | 50.4 ms                                                | 49.8 ms: 1.01x faster                                                  |
| bpe_tokeniser                    | 3.26 sec                                               | 3.24 sec: 1.01x faster                                                 |
| thrift                           | 466 us                                                 | 463 us: 1.01x faster                                                   |
| sqlite_synth                     | 1.55 us                                                | 1.55 us: 1.00x faster                                                  |
| pyflate                          | 352 ms                                                 | 351 ms: 1.00x faster                                                   |
| pidigits                         | 284 ms                                                 | 284 ms: 1.00x slower                                                   |
| pprint_pformat                   | 1.10 sec                                               | 1.11 sec: 1.01x slower                                                 |
| pprint_safe_repr                 | 541 ms                                                 | 546 ms: 1.01x slower                                                   |
| python_startup                   | 18.8 ms                                                | 19.1 ms: 1.01x slower                                                  |
| spectral_norm                    | 76.5 ms                                                | 77.8 ms: 1.02x slower                                                  |
| xml_etree_generate               | 57.1 ms                                                | 58.1 ms: 1.02x slower                                                  |
| pathlib                          | 23.2 ms                                                | 23.7 ms: 1.02x slower                                                  |
| coverage                         | 46.2 ms                                                | 47.2 ms: 1.02x slower                                                  |
| python_startup_no_site           | 13.7 ms                                                | 14.1 ms: 1.03x slower                                                  |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.06 ms: 1.03x slower                                                  |
| unpickle_pure_python             | 165 us                                                 | 170 us: 1.03x slower                                                   |
| sympy_expand                     | 248 ms                                                 | 255 ms: 1.03x slower                                                   |
| sqlglot_optimize                 | 34.7 ms                                                | 35.7 ms: 1.03x slower                                                  |
| sqlglot_transpile                | 1.04 ms                                                | 1.07 ms: 1.03x slower                                                  |
| xml_etree_process                | 41.3 ms                                                | 42.8 ms: 1.04x slower                                                  |
| docutils                         | 1.44 sec                                               | 1.50 sec: 1.04x slower                                                 |
| mdp                              | 1.50 sec                                               | 1.55 sec: 1.04x slower                                                 |
| logging_silent                   | 71.0 ns                                                | 73.6 ns: 1.04x slower                                                  |
| bench_thread_pool                | 503 us                                                 | 523 us: 1.04x slower                                                   |
| sqlglot_normalize                | 188 ms                                                 | 196 ms: 1.04x slower                                                   |
| json_loads                       | 17.0 us                                                | 17.8 us: 1.04x slower                                                  |
| sqlglot_parse                    | 852 us                                                 | 888 us: 1.04x slower                                                   |
| dulwich_log                      | 28.7 ms                                                | 30.0 ms: 1.04x slower                                                  |
| logging_simple                   | 3.56 us                                                | 3.72 us: 1.05x slower                                                  |
| sympy_str                        | 146 ms                                                 | 152 ms: 1.05x slower                                                   |
| fannkuch                         | 279 ms                                                 | 292 ms: 1.05x slower                                                   |
| deltablue                        | 2.65 ms                                                | 2.78 ms: 1.05x slower                                                  |
| logging_format                   | 3.85 us                                                | 4.04 us: 1.05x slower                                                  |
| nqueens                          | 61.8 ms                                                | 65.0 ms: 1.05x slower                                                  |
| sqlalchemy_imperative            | 6.69 ms                                                | 7.07 ms: 1.06x slower                                                  |
| gc_traversal                     | 2.94 ms                                                | 3.10 ms: 1.06x slower                                                  |
| meteor_contest                   | 74.0 ms                                                | 78.3 ms: 1.06x slower                                                  |
| sqlalchemy_declarative           | 59.0 ms                                                | 62.7 ms: 1.06x slower                                                  |
| crypto_pyaes                     | 55.3 ms                                                | 59.0 ms: 1.07x slower                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 1.27 ms: 1.07x slower                                                  |
| sympy_sum                        | 75.1 ms                                                | 80.1 ms: 1.07x slower                                                  |
| chaos                            | 41.1 ms                                                | 44.1 ms: 1.07x slower                                                  |
| pickle_pure_python               | 215 us                                                 | 231 us: 1.08x slower                                                   |
| hexiom                           | 4.87 ms                                                | 5.26 ms: 1.08x slower                                                  |
| mako                             | 7.75 ms                                                | 8.39 ms: 1.08x slower                                                  |
| sympy_integrate                  | 11.3 ms                                                | 12.3 ms: 1.08x slower                                                  |
| richards_super                   | 39.2 ms                                                | 42.8 ms: 1.09x slower                                                  |
| comprehensions                   | 12.0 us                                                | 13.1 us: 1.09x slower                                                  |
| scimark_lu                       | 75.9 ms                                                | 83.2 ms: 1.10x slower                                                  |
| richards                         | 36.2 ms                                                | 39.9 ms: 1.10x slower                                                  |
| many_optionals                   | 409 us                                                 | 468 us: 1.14x slower                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 402 ms: 1.16x slower                                                   |
| json_dumps                       | 6.47 ms                                                | 7.52 ms: 1.16x slower                                                  |
| raytrace                         | 181 ms                                                 | 212 ms: 1.17x slower                                                   |
| django_template                  | 20.5 ms                                                | 24.3 ms: 1.19x slower                                                  |
| nbody                            | 73.6 ms                                                | 92.5 ms: 1.26x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 189 ms: 1.37x slower                                                   |
| subparsers                       | 9.44 ms                                                | 13.0 ms: 1.38x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 142 ms: 2.99x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (9): pylint, json, dask, regex_compile, asyncio_websockets, pycparser, xml_etree_iterparse, typing_runtime_protocols, sphinx
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.009x slower

# HPT report

- Reliability score: 68.17% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.07x