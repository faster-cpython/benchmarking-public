# Results vs. 3.13.0

- fork: python
- ref: 44e4c479fbf2c28605bd
- machine: darwin-arm64
- commit hash: 44e4c47
- commit date: 2025-04-30
- overall geometric mean: 1.045x slower
- HPT reliability: 98.40%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-darwin-arm64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 190 ms: 1.06x slower                                                   |
| docutils       | 1.44 sec                                               | 1.55 sec: 1.08x slower                                                 |
| html5lib       | 36.7 ms                                                | 35.1 ms: 1.05x faster                                                  |
| sphinx         | 602 ms                                                 | 632 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                  | 1.03x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-darwin-arm64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 210 ms: 1.37x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 410 ms: 1.25x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 424 ms: 1.20x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 418 ms: 1.20x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 229 ms: 1.17x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 409 ms: 1.17x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 176 ms: 1.13x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 191 ms: 1.10x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 154 ms: 1.09x faster                                                   |
| async_generators                 | 294 ms                                                 | 279 ms: 1.05x faster                                                   |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 441 ms: 1.04x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 430 ms: 1.04x faster                                                   |
| coroutines                       | 20.0 ms                                                | 19.7 ms: 1.02x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 375 ms: 1.01x slower                                                   |
| async_tree_eager                 | 69.9 ms                                                | 78.1 ms: 1.12x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 402 ms: 1.16x slower                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 189 ms: 1.37x slower                                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 149 ms: 3.14x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-darwin-arm64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 284 ms                                                 | 284 ms: 1.00x slower                                                   |
| float          | 55.8 ms                                                | 58.5 ms: 1.05x slower                                                  |
| nbody          | 73.6 ms                                                | 93.6 ms: 1.27x slower                                                  |
| Geometric mean | (ref)                                                  | 1.10x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-darwin-arm64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.27 ms: 1.16x faster                                                  |
| regex_v8       | 17.0 ms                                                | 15.9 ms: 1.07x faster                                                  |
| regex_dna      | 149 ms                                                 | 141 ms: 1.06x faster                                                   |
| regex_compile  | 78.3 ms                                                | 86.5 ms: 1.11x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-darwin-arm64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.52 sec: 1.03x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 106 ms: 1.02x faster                                                   |
| xml_etree_iterparse  | 74.2 ms                                                | 76.1 ms: 1.03x slower                                                  |
| xml_etree_generate   | 57.1 ms                                                | 62.0 ms: 1.09x slower                                                  |
| json_loads           | 17.0 us                                                | 18.6 us: 1.09x slower                                                  |
| xml_etree_process    | 41.3 ms                                                | 45.7 ms: 1.11x slower                                                  |
| unpickle_pure_python | 165 us                                                 | 186 us: 1.13x slower                                                   |
| pickle_pure_python   | 215 us                                                 | 253 us: 1.18x slower                                                   |
| json_dumps           | 6.47 ms                                                | 8.13 ms: 1.26x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.09x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-darwin-arm64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 19.7 ms: 1.05x slower                                                  |
| python_startup_no_site | 13.7 ms                                                | 14.6 ms: 1.07x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-darwin-arm64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 18.5 ms: 1.09x slower                                                  |
| genshi_xml      | 34.1 ms                                                | 37.5 ms: 1.10x slower                                                  |
| mako            | 7.75 ms                                                | 9.16 ms: 1.18x slower                                                  |
| django_template | 20.5 ms                                                | 26.2 ms: 1.28x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.16x slower                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-darwin-arm64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 872 ms: 1.72x faster                                                   |
| async_tree_memoization_tg        | 288 ms                                                 | 210 ms: 1.37x faster                                                   |
| deepcopy                         | 236 us                                                 | 188 us: 1.26x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 410 ms: 1.25x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 424 ms: 1.20x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 418 ms: 1.20x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 229 ms: 1.17x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 409 ms: 1.17x faster                                                   |
| regex_effbot                     | 2.63 ms                                                | 2.27 ms: 1.16x faster                                                  |
| deepcopy_memo                    | 27.4 us                                                | 24.0 us: 1.14x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 176 ms: 1.13x faster                                                   |
| scimark_sor                      | 106 ms                                                 | 95.0 ms: 1.11x faster                                                  |
| go                               | 117 ms                                                 | 105 ms: 1.11x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 191 ms: 1.10x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 154 ms: 1.09x faster                                                   |
| regex_v8                         | 17.0 ms                                                | 15.9 ms: 1.07x faster                                                  |
| deepcopy_reduce                  | 2.09 us                                                | 1.97 us: 1.07x faster                                                  |
| regex_dna                        | 149 ms                                                 | 141 ms: 1.06x faster                                                   |
| dulwich_log                      | 28.7 ms                                                | 27.3 ms: 1.05x faster                                                  |
| async_generators                 | 294 ms                                                 | 279 ms: 1.05x faster                                                   |
| html5lib                         | 36.7 ms                                                | 35.1 ms: 1.05x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 441 ms: 1.04x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 430 ms: 1.04x faster                                                   |
| k_core                           | 1.61 sec                                               | 1.55 sec: 1.04x faster                                                 |
| tomli_loads                      | 1.57 sec                                               | 1.52 sec: 1.03x faster                                                 |
| connected_components             | 319 ms                                                 | 311 ms: 1.02x faster                                                   |
| shortest_path                    | 345 ms                                                 | 339 ms: 1.02x faster                                                   |
| generators                       | 31.9 ms                                                | 31.4 ms: 1.02x faster                                                  |
| coroutines                       | 20.0 ms                                                | 19.7 ms: 1.02x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 106 ms: 1.02x faster                                                   |
| pidigits                         | 284 ms                                                 | 284 ms: 1.00x slower                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 375 ms: 1.01x slower                                                   |
| spectral_norm                    | 76.5 ms                                                | 78.2 ms: 1.02x slower                                                  |
| xml_etree_iterparse              | 74.2 ms                                                | 76.1 ms: 1.03x slower                                                  |
| telco                            | 4.84 ms                                                | 4.97 ms: 1.03x slower                                                  |
| bpe_tokeniser                    | 3.26 sec                                               | 3.36 sec: 1.03x slower                                                 |
| sympy_integrate                  | 11.3 ms                                                | 11.7 ms: 1.03x slower                                                  |
| bench_mp_pool                    | 64.7 ms                                                | 66.9 ms: 1.03x slower                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.61 us: 1.04x slower                                                  |
| json                             | 3.04 ms                                                | 3.18 ms: 1.05x slower                                                  |
| python_startup                   | 18.8 ms                                                | 19.7 ms: 1.05x slower                                                  |
| float                            | 55.8 ms                                                | 58.5 ms: 1.05x slower                                                  |
| sphinx                           | 602 ms                                                 | 632 ms: 1.05x slower                                                   |
| scimark_fft                      | 200 ms                                                 | 210 ms: 1.05x slower                                                   |
| meteor_contest                   | 74.0 ms                                                | 77.9 ms: 1.05x slower                                                  |
| 2to3                             | 179 ms                                                 | 190 ms: 1.06x slower                                                   |
| gc_traversal                     | 2.94 ms                                                | 3.12 ms: 1.06x slower                                                  |
| python_startup_no_site           | 13.7 ms                                                | 14.6 ms: 1.07x slower                                                  |
| pprint_pformat                   | 1.10 sec                                               | 1.17 sec: 1.07x slower                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 54.0 ms: 1.07x slower                                                  |
| pprint_safe_repr                 | 541 ms                                                 | 579 ms: 1.07x slower                                                   |
| create_gc_cycles                 | 1.19 ms                                                | 1.28 ms: 1.08x slower                                                  |
| docutils                         | 1.44 sec                                               | 1.55 sec: 1.08x slower                                                 |
| pycparser                        | 701 ms                                                 | 758 ms: 1.08x slower                                                   |
| deltablue                        | 2.65 ms                                                | 2.86 ms: 1.08x slower                                                  |
| xml_etree_generate               | 57.1 ms                                                | 62.0 ms: 1.09x slower                                                  |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.25 ms: 1.09x slower                                                  |
| json_loads                       | 17.0 us                                                | 18.6 us: 1.09x slower                                                  |
| coverage                         | 46.2 ms                                                | 50.4 ms: 1.09x slower                                                  |
| richards                         | 36.2 ms                                                | 39.5 ms: 1.09x slower                                                  |
| genshi_text                      | 16.9 ms                                                | 18.5 ms: 1.09x slower                                                  |
| scimark_lu                       | 75.9 ms                                                | 83.0 ms: 1.09x slower                                                  |
| sympy_expand                     | 248 ms                                                 | 271 ms: 1.10x slower                                                   |
| bench_thread_pool                | 503 us                                                 | 553 us: 1.10x slower                                                   |
| pathlib                          | 23.2 ms                                                | 25.5 ms: 1.10x slower                                                  |
| genshi_xml                       | 34.1 ms                                                | 37.5 ms: 1.10x slower                                                  |
| sympy_str                        | 146 ms                                                 | 160 ms: 1.10x slower                                                   |
| regex_compile                    | 78.3 ms                                                | 86.5 ms: 1.11x slower                                                  |
| xml_etree_process                | 41.3 ms                                                | 45.7 ms: 1.11x slower                                                  |
| sympy_sum                        | 75.1 ms                                                | 83.2 ms: 1.11x slower                                                  |
| typing_runtime_protocols         | 101 us                                                 | 112 us: 1.11x slower                                                   |
| sqlalchemy_imperative            | 6.69 ms                                                | 7.46 ms: 1.11x slower                                                  |
| async_tree_eager                 | 69.9 ms                                                | 78.1 ms: 1.12x slower                                                  |
| logging_simple                   | 3.56 us                                                | 3.98 us: 1.12x slower                                                  |
| logging_format                   | 3.85 us                                                | 4.30 us: 1.12x slower                                                  |
| crypto_pyaes                     | 55.3 ms                                                | 62.0 ms: 1.12x slower                                                  |
| richards_super                   | 39.2 ms                                                | 44.0 ms: 1.12x slower                                                  |
| hexiom                           | 4.87 ms                                                | 5.46 ms: 1.12x slower                                                  |
| logging_silent                   | 71.0 ns                                                | 79.9 ns: 1.13x slower                                                  |
| unpickle_pure_python             | 165 us                                                 | 186 us: 1.13x slower                                                   |
| sqlalchemy_declarative           | 59.0 ms                                                | 66.5 ms: 1.13x slower                                                  |
| raytrace                         | 181 ms                                                 | 206 ms: 1.14x slower                                                   |
| chaos                            | 41.1 ms                                                | 46.7 ms: 1.14x slower                                                  |
| fannkuch                         | 279 ms                                                 | 318 ms: 1.14x slower                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 402 ms: 1.16x slower                                                   |
| pickle_pure_python               | 215 us                                                 | 253 us: 1.18x slower                                                   |
| mako                             | 7.75 ms                                                | 9.16 ms: 1.18x slower                                                  |
| comprehensions                   | 12.0 us                                                | 14.5 us: 1.21x slower                                                  |
| many_optionals                   | 409 us                                                 | 497 us: 1.22x slower                                                   |
| nqueens                          | 61.8 ms                                                | 75.3 ms: 1.22x slower                                                  |
| json_dumps                       | 6.47 ms                                                | 8.13 ms: 1.26x slower                                                  |
| nbody                            | 73.6 ms                                                | 93.6 ms: 1.27x slower                                                  |
| django_template                  | 20.5 ms                                                | 26.2 ms: 1.28x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 189 ms: 1.37x slower                                                   |
| subparsers                       | 9.44 ms                                                | 13.7 ms: 1.45x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 149 ms: 3.14x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.05x slower                                                           |

Benchmark hidden because not significant (3): pylint, pyflate, asyncio_websockets
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250430-3.14.0a7+-44e4c47/bm-20250430-darwin-arm64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.045x slower

# HPT report

- Reliability score: 98.40% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.09x