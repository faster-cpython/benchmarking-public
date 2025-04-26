# Results vs. 3.13.0

- fork: mdboom
- ref: python_startup_time
- machine: darwin-arm64
- commit hash: 9fc1238
- commit date: 2025-04-25
- overall geometric mean: 1.045x slower
- HPT reliability: 98.20%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-darwin-arm64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 220 ms: 1.23x slower                                                  |
| docutils       | 1.44 sec                                               | 1.55 sec: 1.07x slower                                                |
| sphinx         | 602 ms                                                 | 627 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.08x slower                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-darwin-arm64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 215 ms: 1.34x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 410 ms: 1.25x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 410 ms: 1.22x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 223 ms: 1.20x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 435 ms: 1.17x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 413 ms: 1.16x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 176 ms: 1.13x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 189 ms: 1.12x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 156 ms: 1.08x faster                                                  |
| async_generators                 | 294 ms                                                 | 273 ms: 1.08x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 437 ms: 1.05x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 427 ms: 1.05x faster                                                  |
| coroutines                       | 20.0 ms                                                | 19.6 ms: 1.02x faster                                                 |
| asyncio_websockets               | 242 ms                                                 | 245 ms: 1.01x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 402 ms: 1.16x slower                                                  |
| async_tree_eager                 | 69.9 ms                                                | 81.3 ms: 1.16x slower                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 188 ms: 1.37x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 146 ms: 3.08x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (1): async_tree_eager_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-darwin-arm64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 57.9 ms: 1.04x slower                                                 |
| nbody          | 73.6 ms                                                | 97.4 ms: 1.32x slower                                                 |
| Geometric mean | (ref)                                                  | 1.11x slower                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-darwin-arm64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.28 ms: 1.15x faster                                                 |
| regex_v8       | 17.0 ms                                                | 15.9 ms: 1.07x faster                                                 |
| regex_dna      | 149 ms                                                 | 140 ms: 1.06x faster                                                  |
| regex_compile  | 78.3 ms                                                | 85.6 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-darwin-arm64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.52 sec: 1.03x faster                                                |
| xml_etree_parse      | 108 ms                                                 | 107 ms: 1.01x faster                                                  |
| xml_etree_iterparse  | 74.2 ms                                                | 76.4 ms: 1.03x slower                                                 |
| json_loads           | 17.0 us                                                | 17.7 us: 1.04x slower                                                 |
| xml_etree_generate   | 57.1 ms                                                | 61.5 ms: 1.08x slower                                                 |
| unpickle_pure_python | 165 us                                                 | 183 us: 1.11x slower                                                  |
| xml_etree_process    | 41.3 ms                                                | 45.8 ms: 1.11x slower                                                 |
| pickle_pure_python   | 215 us                                                 | 249 us: 1.16x slower                                                  |
| json_dumps           | 6.47 ms                                                | 7.88 ms: 1.22x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.08x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-darwin-arm64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 19.9 ms: 1.06x slower                                                 |
| python_startup_no_site | 13.7 ms                                                | 15.0 ms: 1.09x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-darwin-arm64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 34.1 ms                                                | 37.2 ms: 1.09x slower                                                 |
| genshi_text     | 16.9 ms                                                | 18.8 ms: 1.11x slower                                                 |
| mako            | 7.75 ms                                                | 9.07 ms: 1.17x slower                                                 |
| django_template | 20.5 ms                                                | 26.2 ms: 1.28x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.16x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-darwin-arm64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 877 ms: 1.71x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 215 ms: 1.34x faster                                                  |
| deepcopy                         | 236 us                                                 | 181 us: 1.30x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 410 ms: 1.25x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 410 ms: 1.22x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 223 ms: 1.20x faster                                                  |
| deepcopy_memo                    | 27.4 us                                                | 23.4 us: 1.17x faster                                                 |
| async_tree_io                    | 508 ms                                                 | 435 ms: 1.17x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 413 ms: 1.16x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.28 ms: 1.15x faster                                                 |
| async_tree_none_tg               | 198 ms                                                 | 176 ms: 1.13x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 189 ms: 1.12x faster                                                  |
| scimark_sor                      | 106 ms                                                 | 95.0 ms: 1.11x faster                                                 |
| go                               | 117 ms                                                 | 105 ms: 1.11x faster                                                  |
| deepcopy_reduce                  | 2.09 us                                                | 1.93 us: 1.09x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 156 ms: 1.08x faster                                                  |
| async_generators                 | 294 ms                                                 | 273 ms: 1.08x faster                                                  |
| regex_v8                         | 17.0 ms                                                | 15.9 ms: 1.07x faster                                                 |
| dulwich_log                      | 28.7 ms                                                | 26.9 ms: 1.07x faster                                                 |
| regex_dna                        | 149 ms                                                 | 140 ms: 1.06x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 437 ms: 1.05x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 427 ms: 1.05x faster                                                  |
| k_core                           | 1.61 sec                                               | 1.54 sec: 1.05x faster                                                |
| tomli_loads                      | 1.57 sec                                               | 1.52 sec: 1.03x faster                                                |
| connected_components             | 319 ms                                                 | 311 ms: 1.02x faster                                                  |
| coroutines                       | 20.0 ms                                                | 19.6 ms: 1.02x faster                                                 |
| shortest_path                    | 345 ms                                                 | 340 ms: 1.02x faster                                                  |
| pyflate                          | 352 ms                                                 | 347 ms: 1.01x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 107 ms: 1.01x faster                                                  |
| generators                       | 31.9 ms                                                | 31.7 ms: 1.01x faster                                                 |
| spectral_norm                    | 76.5 ms                                                | 77.0 ms: 1.01x slower                                                 |
| asyncio_websockets               | 242 ms                                                 | 245 ms: 1.01x slower                                                  |
| telco                            | 4.84 ms                                                | 4.91 ms: 1.01x slower                                                 |
| bpe_tokeniser                    | 3.26 sec                                               | 3.32 sec: 1.02x slower                                                |
| sympy_integrate                  | 11.3 ms                                                | 11.6 ms: 1.03x slower                                                 |
| xml_etree_iterparse              | 74.2 ms                                                | 76.4 ms: 1.03x slower                                                 |
| bench_mp_pool                    | 64.7 ms                                                | 66.7 ms: 1.03x slower                                                 |
| sqlite_synth                     | 1.55 us                                                | 1.60 us: 1.03x slower                                                 |
| scimark_fft                      | 200 ms                                                 | 206 ms: 1.03x slower                                                  |
| float                            | 55.8 ms                                                | 57.9 ms: 1.04x slower                                                 |
| json_loads                       | 17.0 us                                                | 17.7 us: 1.04x slower                                                 |
| sphinx                           | 602 ms                                                 | 627 ms: 1.04x slower                                                  |
| pathlib                          | 23.2 ms                                                | 24.2 ms: 1.04x slower                                                 |
| meteor_contest                   | 74.0 ms                                                | 77.5 ms: 1.05x slower                                                 |
| python_startup                   | 18.8 ms                                                | 19.9 ms: 1.06x slower                                                 |
| gc_traversal                     | 2.94 ms                                                | 3.11 ms: 1.06x slower                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 53.6 ms: 1.06x slower                                                 |
| docutils                         | 1.44 sec                                               | 1.55 sec: 1.07x slower                                                |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.20 ms: 1.07x slower                                                 |
| pycparser                        | 701 ms                                                 | 753 ms: 1.08x slower                                                  |
| xml_etree_generate               | 57.1 ms                                                | 61.5 ms: 1.08x slower                                                 |
| create_gc_cycles                 | 1.19 ms                                                | 1.29 ms: 1.08x slower                                                 |
| coverage                         | 46.2 ms                                                | 50.0 ms: 1.08x slower                                                 |
| sympy_expand                     | 248 ms                                                 | 268 ms: 1.08x slower                                                  |
| richards                         | 36.2 ms                                                | 39.3 ms: 1.09x slower                                                 |
| python_startup_no_site           | 13.7 ms                                                | 15.0 ms: 1.09x slower                                                 |
| genshi_xml                       | 34.1 ms                                                | 37.2 ms: 1.09x slower                                                 |
| sympy_str                        | 146 ms                                                 | 159 ms: 1.09x slower                                                  |
| regex_compile                    | 78.3 ms                                                | 85.6 ms: 1.09x slower                                                 |
| sympy_sum                        | 75.1 ms                                                | 82.4 ms: 1.10x slower                                                 |
| scimark_lu                       | 75.9 ms                                                | 83.7 ms: 1.10x slower                                                 |
| pprint_pformat                   | 1.10 sec                                               | 1.21 sec: 1.10x slower                                                |
| logging_silent                   | 71.0 ns                                                | 78.3 ns: 1.10x slower                                                 |
| crypto_pyaes                     | 55.3 ms                                                | 61.1 ms: 1.10x slower                                                 |
| deltablue                        | 2.65 ms                                                | 2.93 ms: 1.11x slower                                                 |
| pprint_safe_repr                 | 541 ms                                                 | 598 ms: 1.11x slower                                                  |
| unpickle_pure_python             | 165 us                                                 | 183 us: 1.11x slower                                                  |
| xml_etree_process                | 41.3 ms                                                | 45.8 ms: 1.11x slower                                                 |
| genshi_text                      | 16.9 ms                                                | 18.8 ms: 1.11x slower                                                 |
| sqlalchemy_imperative            | 6.69 ms                                                | 7.45 ms: 1.11x slower                                                 |
| bench_thread_pool                | 503 us                                                 | 561 us: 1.12x slower                                                  |
| richards_super                   | 39.2 ms                                                | 43.9 ms: 1.12x slower                                                 |
| hexiom                           | 4.87 ms                                                | 5.47 ms: 1.12x slower                                                 |
| chaos                            | 41.1 ms                                                | 46.5 ms: 1.13x slower                                                 |
| logging_format                   | 3.85 us                                                | 4.38 us: 1.14x slower                                                 |
| typing_runtime_protocols         | 101 us                                                 | 115 us: 1.14x slower                                                  |
| logging_simple                   | 3.56 us                                                | 4.06 us: 1.14x slower                                                 |
| sqlalchemy_declarative           | 59.0 ms                                                | 67.4 ms: 1.14x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 402 ms: 1.16x slower                                                  |
| pickle_pure_python               | 215 us                                                 | 249 us: 1.16x slower                                                  |
| async_tree_eager                 | 69.9 ms                                                | 81.3 ms: 1.16x slower                                                 |
| raytrace                         | 181 ms                                                 | 212 ms: 1.17x slower                                                  |
| mako                             | 7.75 ms                                                | 9.07 ms: 1.17x slower                                                 |
| comprehensions                   | 12.0 us                                                | 14.3 us: 1.20x slower                                                 |
| fannkuch                         | 279 ms                                                 | 333 ms: 1.20x slower                                                  |
| many_optionals                   | 409 us                                                 | 492 us: 1.20x slower                                                  |
| json_dumps                       | 6.47 ms                                                | 7.88 ms: 1.22x slower                                                 |
| 2to3                             | 179 ms                                                 | 220 ms: 1.23x slower                                                  |
| nqueens                          | 61.8 ms                                                | 78.5 ms: 1.27x slower                                                 |
| django_template                  | 20.5 ms                                                | 26.2 ms: 1.28x slower                                                 |
| nbody                            | 73.6 ms                                                | 97.4 ms: 1.32x slower                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 188 ms: 1.37x slower                                                  |
| subparsers                       | 9.44 ms                                                | 13.9 ms: 1.47x slower                                                 |
| async_tree_eager_tg              | 47.4 ms                                                | 146 ms: 3.08x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.05x slower                                                          |

Benchmark hidden because not significant (5): pylint, async_tree_eager_cpu_io_mixed, pidigits, html5lib, json
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250425-3.14.0a7+-9fc1238/bm-20250425-darwin-arm64-mdboom-python_startup_time-3.14.0a7+-9fc1238.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.045x slower

# HPT report

- Reliability score: 98.20% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.09x