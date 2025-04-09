# Results vs. 3.13.0

- fork: python
- ref: c5e856a5dc8eed4813ec
- machine: darwin-arm64
- commit hash: c5e856a
- commit date: 2025-04-08
- overall geometric mean: 1.103x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-darwin-arm64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 159 ms: 1.12x faster                                                   |
| docutils       | 1.44 sec                                               | 1.41 sec: 1.02x faster                                                 |
| html5lib       | 36.7 ms                                                | 29.4 ms: 1.25x faster                                                  |
| sphinx         | 602 ms                                                 | 574 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-darwin-arm64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 189 ms: 1.52x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 356 ms: 1.43x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 188 ms: 1.42x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 361 ms: 1.38x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 370 ms: 1.37x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 160 ms: 1.33x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 152 ms: 1.31x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 369 ms: 1.30x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 136 ms: 1.23x faster                                                   |
| coroutines                       | 20.0 ms                                                | 16.3 ms: 1.23x faster                                                  |
| async_generators                 | 294 ms                                                 | 257 ms: 1.14x faster                                                   |
| async_tree_eager                 | 69.9 ms                                                | 61.3 ms: 1.14x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 405 ms: 1.13x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 406 ms: 1.10x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 353 ms: 1.05x faster                                                   |
| asyncio_websockets               | 242 ms                                                 | 242 ms: 1.00x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 387 ms: 1.12x slower                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 168 ms: 1.22x slower                                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 130 ms: 2.74x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.12x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-darwin-arm64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 45.8 ms: 1.22x faster                                                  |
| nbody          | 73.6 ms                                                | 70.1 ms: 1.05x faster                                                  |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-darwin-arm64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 78.3 ms                                                | 66.7 ms: 1.17x faster                                                  |
| regex_effbot   | 2.63 ms                                                | 2.27 ms: 1.16x faster                                                  |
| regex_v8       | 17.0 ms                                                | 15.6 ms: 1.09x faster                                                  |
| regex_dna      | 149 ms                                                 | 140 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                  | 1.12x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-darwin-arm64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.20 sec: 1.30x faster                                                 |
| unpickle_pure_python | 165 us                                                 | 148 us: 1.12x faster                                                   |
| xml_etree_process    | 41.3 ms                                                | 38.1 ms: 1.08x faster                                                  |
| xml_etree_generate   | 57.1 ms                                                | 53.4 ms: 1.07x faster                                                  |
| pickle_pure_python   | 215 us                                                 | 201 us: 1.07x faster                                                   |
| xml_etree_parse      | 108 ms                                                 | 103 ms: 1.04x faster                                                   |
| xml_etree_iterparse  | 74.2 ms                                                | 72.1 ms: 1.03x faster                                                  |
| json_loads           | 17.0 us                                                | 17.7 us: 1.04x slower                                                  |
| json_dumps           | 6.47 ms                                                | 7.36 ms: 1.14x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-darwin-arm64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 16.8 ms: 1.12x faster                                                  |
| python_startup_no_site | 13.7 ms                                                | 12.7 ms: 1.08x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-darwin-arm64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 13.7 ms: 1.23x faster                                                  |
| genshi_xml      | 34.1 ms                                                | 28.6 ms: 1.19x faster                                                  |
| mako            | 7.75 ms                                                | 7.56 ms: 1.02x faster                                                  |
| django_template | 20.5 ms                                                | 20.8 ms: 1.02x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-darwin-arm64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 753 ms: 1.99x faster                                                   |
| deepcopy                         | 236 us                                                 | 148 us: 1.59x faster                                                   |
| deepcopy_memo                    | 27.4 us                                                | 17.8 us: 1.54x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 189 ms: 1.52x faster                                                   |
| go                               | 117 ms                                                 | 78.8 ms: 1.48x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 356 ms: 1.43x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 188 ms: 1.42x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 361 ms: 1.38x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 370 ms: 1.37x faster                                                   |
| generators                       | 31.9 ms                                                | 23.4 ms: 1.37x faster                                                  |
| scimark_sor                      | 106 ms                                                 | 77.8 ms: 1.36x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 160 ms: 1.33x faster                                                   |
| deepcopy_reduce                  | 2.09 us                                                | 1.58 us: 1.32x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 152 ms: 1.31x faster                                                   |
| tomli_loads                      | 1.57 sec                                               | 1.20 sec: 1.30x faster                                                 |
| async_tree_eager_io_tg           | 479 ms                                                 | 369 ms: 1.30x faster                                                   |
| html5lib                         | 36.7 ms                                                | 29.4 ms: 1.25x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 136 ms: 1.23x faster                                                   |
| genshi_text                      | 16.9 ms                                                | 13.7 ms: 1.23x faster                                                  |
| pyflate                          | 352 ms                                                 | 286 ms: 1.23x faster                                                   |
| coroutines                       | 20.0 ms                                                | 16.3 ms: 1.23x faster                                                  |
| float                            | 55.8 ms                                                | 45.8 ms: 1.22x faster                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 41.8 ms: 1.21x faster                                                  |
| genshi_xml                       | 34.1 ms                                                | 28.6 ms: 1.19x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 24.4 ms: 1.18x faster                                                  |
| regex_compile                    | 78.3 ms                                                | 66.7 ms: 1.17x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.27 ms: 1.16x faster                                                  |
| deltablue                        | 2.65 ms                                                | 2.31 ms: 1.15x faster                                                  |
| pprint_pformat                   | 1.10 sec                                               | 961 ms: 1.15x faster                                                   |
| hexiom                           | 4.87 ms                                                | 4.26 ms: 1.14x faster                                                  |
| async_generators                 | 294 ms                                                 | 257 ms: 1.14x faster                                                   |
| async_tree_eager                 | 69.9 ms                                                | 61.3 ms: 1.14x faster                                                  |
| pprint_safe_repr                 | 541 ms                                                 | 475 ms: 1.14x faster                                                   |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 405 ms: 1.13x faster                                                   |
| 2to3                             | 179 ms                                                 | 159 ms: 1.12x faster                                                   |
| richards                         | 36.2 ms                                                | 32.2 ms: 1.12x faster                                                  |
| python_startup                   | 18.8 ms                                                | 16.8 ms: 1.12x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 68.4 ms: 1.12x faster                                                  |
| unpickle_pure_python             | 165 us                                                 | 148 us: 1.12x faster                                                   |
| pylint                           | 180 ms                                                 | 161 ms: 1.11x faster                                                   |
| logging_simple                   | 3.56 us                                                | 3.21 us: 1.11x faster                                                  |
| scimark_fft                      | 200 ms                                                 | 181 ms: 1.10x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 406 ms: 1.10x faster                                                   |
| logging_silent                   | 71.0 ns                                                | 64.5 ns: 1.10x faster                                                  |
| logging_format                   | 3.85 us                                                | 3.51 us: 1.10x faster                                                  |
| chaos                            | 41.1 ms                                                | 37.6 ms: 1.09x faster                                                  |
| bpe_tokeniser                    | 3.26 sec                                               | 2.98 sec: 1.09x faster                                                 |
| richards_super                   | 39.2 ms                                                | 35.9 ms: 1.09x faster                                                  |
| regex_v8                         | 17.0 ms                                                | 15.6 ms: 1.09x faster                                                  |
| xml_etree_process                | 41.3 ms                                                | 38.1 ms: 1.08x faster                                                  |
| bench_mp_pool                    | 64.7 ms                                                | 59.8 ms: 1.08x faster                                                  |
| python_startup_no_site           | 13.7 ms                                                | 12.7 ms: 1.08x faster                                                  |
| pycparser                        | 701 ms                                                 | 651 ms: 1.08x faster                                                   |
| fannkuch                         | 279 ms                                                 | 259 ms: 1.08x faster                                                   |
| typing_runtime_protocols         | 101 us                                                 | 93.7 us: 1.07x faster                                                  |
| raytrace                         | 181 ms                                                 | 169 ms: 1.07x faster                                                   |
| xml_etree_generate               | 57.1 ms                                                | 53.4 ms: 1.07x faster                                                  |
| pickle_pure_python               | 215 us                                                 | 201 us: 1.07x faster                                                   |
| telco                            | 4.84 ms                                                | 4.55 ms: 1.06x faster                                                  |
| sympy_expand                     | 248 ms                                                 | 233 ms: 1.06x faster                                                   |
| regex_dna                        | 149 ms                                                 | 140 ms: 1.06x faster                                                   |
| sympy_integrate                  | 11.3 ms                                                | 10.7 ms: 1.06x faster                                                  |
| k_core                           | 1.61 sec                                               | 1.53 sec: 1.06x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 353 ms: 1.05x faster                                                   |
| comprehensions                   | 12.0 us                                                | 11.3 us: 1.05x faster                                                  |
| nqueens                          | 61.8 ms                                                | 58.7 ms: 1.05x faster                                                  |
| nbody                            | 73.6 ms                                                | 70.1 ms: 1.05x faster                                                  |
| connected_components             | 319 ms                                                 | 304 ms: 1.05x faster                                                   |
| sphinx                           | 602 ms                                                 | 574 ms: 1.05x faster                                                   |
| sympy_str                        | 146 ms                                                 | 139 ms: 1.04x faster                                                   |
| shortest_path                    | 345 ms                                                 | 331 ms: 1.04x faster                                                   |
| xml_etree_parse                  | 108 ms                                                 | 103 ms: 1.04x faster                                                   |
| scimark_lu                       | 75.9 ms                                                | 73.3 ms: 1.04x faster                                                  |
| bench_thread_pool                | 503 us                                                 | 489 us: 1.03x faster                                                   |
| xml_etree_iterparse              | 74.2 ms                                                | 72.1 ms: 1.03x faster                                                  |
| mako                             | 7.75 ms                                                | 7.56 ms: 1.02x faster                                                  |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.54 ms: 1.02x faster                                                  |
| meteor_contest                   | 74.0 ms                                                | 72.3 ms: 1.02x faster                                                  |
| docutils                         | 1.44 sec                                               | 1.41 sec: 1.02x faster                                                 |
| sqlite_synth                     | 1.55 us                                                | 1.53 us: 1.02x faster                                                  |
| sympy_sum                        | 75.1 ms                                                | 74.1 ms: 1.01x faster                                                  |
| coverage                         | 46.2 ms                                                | 45.7 ms: 1.01x faster                                                  |
| crypto_pyaes                     | 55.3 ms                                                | 54.8 ms: 1.01x faster                                                  |
| asyncio_websockets               | 242 ms                                                 | 242 ms: 1.00x faster                                                   |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                                   |
| django_template                  | 20.5 ms                                                | 20.8 ms: 1.02x slower                                                  |
| pathlib                          | 23.2 ms                                                | 23.7 ms: 1.02x slower                                                  |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.09 ms: 1.03x slower                                                  |
| json_loads                       | 17.0 us                                                | 17.7 us: 1.04x slower                                                  |
| gc_traversal                     | 2.94 ms                                                | 3.12 ms: 1.06x slower                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 1.28 ms: 1.08x slower                                                  |
| many_optionals                   | 409 us                                                 | 445 us: 1.09x slower                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 387 ms: 1.12x slower                                                   |
| json_dumps                       | 6.47 ms                                                | 7.36 ms: 1.14x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 168 ms: 1.22x slower                                                   |
| subparsers                       | 9.44 ms                                                | 12.1 ms: 1.28x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 130 ms: 2.74x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.10x faster                                                           |

Benchmark hidden because not significant (2): json, sqlalchemy_declarative
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250408-3.14.0a7+-c5e856a/bm-20250408-darwin-arm64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.103x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.09x