# Results vs. 3.13.0

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: darwin-arm64
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.109x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 181 ms                                                 | 214 ms: 1.18x slower                                                   |
| docutils       | 1.44 sec                                               | 1.50 sec: 1.04x slower                                                 |
| html5lib       | 36.6 ms                                                | 44.3 ms: 1.21x slower                                                  |
| sphinx         | 600 ms                                                 | 629 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                  | 1.12x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager_io              | 514 ms                                                 | 412 ms: 1.25x faster                                                   |
| async_tree_memoization_tg        | 289 ms                                                 | 237 ms: 1.22x faster                                                   |
| async_tree_eager_io_tg           | 481 ms                                                 | 399 ms: 1.20x faster                                                   |
| async_tree_io_tg                 | 499 ms                                                 | 429 ms: 1.16x faster                                                   |
| async_tree_io                    | 510 ms                                                 | 449 ms: 1.14x faster                                                   |
| coroutines                       | 19.8 ms                                                | 17.5 ms: 1.13x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 255 ms: 1.05x faster                                                   |
| async_tree_none_tg               | 199 ms                                                 | 189 ms: 1.05x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 206 ms: 1.03x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 164 ms: 1.02x faster                                                   |
| asyncio_websockets               | 243 ms                                                 | 238 ms: 1.02x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 441 ms: 1.02x faster                                                   |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 458 ms: 1.00x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 380 ms: 1.02x slower                                                   |
| async_generators                 | 292 ms                                                 | 300 ms: 1.03x slower                                                   |
| async_tree_eager_cpu_io_mixed_tg | 346 ms                                                 | 362 ms: 1.05x slower                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 149 ms: 1.08x slower                                                   |
| async_tree_eager                 | 69.9 ms                                                | 89.8 ms: 1.28x slower                                                  |
| async_tree_eager_tg              | 48.0 ms                                                | 69.5 ms: 1.45x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 284 ms                                                 | 281 ms: 1.01x faster                                                   |
| nbody          | 73.9 ms                                                | 86.2 ms: 1.17x slower                                                  |
| float          | 56.3 ms                                                | 82.9 ms: 1.47x slower                                                  |
| Geometric mean | (ref)                                                  | 1.19x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.62 ms                                                | 2.03 ms: 1.29x faster                                                  |
| regex_dna      | 148 ms                                                 | 134 ms: 1.10x faster                                                   |
| regex_v8       | 17.0 ms                                                | 15.5 ms: 1.09x faster                                                  |
| regex_compile  | 78.6 ms                                                | 89.4 ms: 1.14x slower                                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_iterparse  | 74.1 ms                                                | 66.4 ms: 1.12x faster                                                  |
| xml_etree_parse      | 107 ms                                                 | 103 ms: 1.04x faster                                                   |
| xml_etree_generate   | 57.0 ms                                                | 57.4 ms: 1.01x slower                                                  |
| tomli_loads          | 1.56 sec                                               | 1.58 sec: 1.01x slower                                                 |
| json_loads           | 17.0 us                                                | 17.4 us: 1.02x slower                                                  |
| xml_etree_process    | 41.0 ms                                                | 45.8 ms: 1.12x slower                                                  |
| json_dumps           | 6.51 ms                                                | 8.26 ms: 1.27x slower                                                  |
| unpickle_pure_python | 164 us                                                 | 209 us: 1.27x slower                                                   |
| pickle_pure_python   | 214 us                                                 | 296 us: 1.39x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.09x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                | 22.8 ms: 1.11x slower                                                  |
| python_startup_no_site | 15.8 ms                                                | 18.1 ms: 1.15x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 17.8 ms: 1.05x slower                                                  |
| genshi_xml      | 34.1 ms                                                | 36.4 ms: 1.07x slower                                                  |
| django_template | 20.5 ms                                                | 27.0 ms: 1.32x slower                                                  |
| mako            | 7.70 ms                                                | 11.1 ms: 1.44x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.21x slower                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy                         | 234 us                                                 | 178 us: 1.31x faster                                                   |
| regex_effbot                     | 2.62 ms                                                | 2.03 ms: 1.29x faster                                                  |
| async_tree_eager_io              | 514 ms                                                 | 412 ms: 1.25x faster                                                   |
| async_tree_memoization_tg        | 289 ms                                                 | 237 ms: 1.22x faster                                                   |
| async_tree_eager_io_tg           | 481 ms                                                 | 399 ms: 1.20x faster                                                   |
| async_tree_io_tg                 | 499 ms                                                 | 429 ms: 1.16x faster                                                   |
| deepcopy_memo                    | 27.3 us                                                | 23.7 us: 1.15x faster                                                  |
| generators                       | 31.5 ms                                                | 27.4 ms: 1.15x faster                                                  |
| async_tree_io                    | 510 ms                                                 | 449 ms: 1.14x faster                                                   |
| coroutines                       | 19.8 ms                                                | 17.5 ms: 1.13x faster                                                  |
| sqlite_synth                     | 1.56 us                                                | 1.38 us: 1.13x faster                                                  |
| xml_etree_iterparse              | 74.1 ms                                                | 66.4 ms: 1.12x faster                                                  |
| gc_traversal                     | 2.93 ms                                                | 2.63 ms: 1.11x faster                                                  |
| deepcopy_reduce                  | 2.08 us                                                | 1.88 us: 1.11x faster                                                  |
| regex_dna                        | 148 ms                                                 | 134 ms: 1.10x faster                                                   |
| regex_v8                         | 17.0 ms                                                | 15.5 ms: 1.09x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 255 ms: 1.05x faster                                                   |
| async_tree_none_tg               | 199 ms                                                 | 189 ms: 1.05x faster                                                   |
| create_gc_cycles                 | 1.20 ms                                                | 1.14 ms: 1.05x faster                                                  |
| nqueens                          | 61.8 ms                                                | 59.2 ms: 1.04x faster                                                  |
| xml_etree_parse                  | 107 ms                                                 | 103 ms: 1.04x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 206 ms: 1.03x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 164 ms: 1.02x faster                                                   |
| asyncio_websockets               | 243 ms                                                 | 238 ms: 1.02x faster                                                   |
| spectral_norm                    | 76.3 ms                                                | 74.6 ms: 1.02x faster                                                  |
| json                             | 3.06 ms                                                | 3.00 ms: 1.02x faster                                                  |
| pathlib                          | 23.3 ms                                                | 22.8 ms: 1.02x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 441 ms: 1.02x faster                                                   |
| pidigits                         | 284 ms                                                 | 281 ms: 1.01x faster                                                   |
| bpe_tokeniser                    | 3.25 sec                                               | 3.22 sec: 1.01x faster                                                 |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 458 ms: 1.00x faster                                                   |
| xml_etree_generate               | 57.0 ms                                                | 57.4 ms: 1.01x slower                                                  |
| tomli_loads                      | 1.56 sec                                               | 1.58 sec: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 380 ms: 1.02x slower                                                   |
| json_loads                       | 17.0 us                                                | 17.4 us: 1.02x slower                                                  |
| async_generators                 | 292 ms                                                 | 300 ms: 1.03x slower                                                   |
| fannkuch                         | 285 ms                                                 | 294 ms: 1.03x slower                                                   |
| docutils                         | 1.44 sec                                               | 1.50 sec: 1.04x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 346 ms                                                 | 362 ms: 1.05x slower                                                   |
| sphinx                           | 600 ms                                                 | 629 ms: 1.05x slower                                                   |
| genshi_text                      | 16.9 ms                                                | 17.8 ms: 1.05x slower                                                  |
| k_core                           | 1.62 sec                                               | 1.70 sec: 1.05x slower                                                 |
| shortest_path                    | 349 ms                                                 | 369 ms: 1.06x slower                                                   |
| telco                            | 4.79 ms                                                | 5.07 ms: 1.06x slower                                                  |
| genshi_xml                       | 34.1 ms                                                | 36.4 ms: 1.07x slower                                                  |
| sqlglot_optimize                 | 34.8 ms                                                | 37.4 ms: 1.08x slower                                                  |
| meteor_contest                   | 75.1 ms                                                | 80.9 ms: 1.08x slower                                                  |
| mdp                              | 1.50 sec                                               | 1.62 sec: 1.08x slower                                                 |
| connected_components             | 320 ms                                                 | 346 ms: 1.08x slower                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 149 ms: 1.08x slower                                                   |
| scimark_fft                      | 200 ms                                                 | 217 ms: 1.09x slower                                                   |
| sqlglot_normalize                | 188 ms                                                 | 204 ms: 1.09x slower                                                   |
| python_startup                   | 20.6 ms                                                | 22.8 ms: 1.11x slower                                                  |
| pycparser                        | 708 ms                                                 | 786 ms: 1.11x slower                                                   |
| xml_etree_process                | 41.0 ms                                                | 45.8 ms: 1.12x slower                                                  |
| coverage                         | 45.5 ms                                                | 51.7 ms: 1.14x slower                                                  |
| regex_compile                    | 78.6 ms                                                | 89.4 ms: 1.14x slower                                                  |
| bench_mp_pool                    | 64.9 ms                                                | 74.0 ms: 1.14x slower                                                  |
| python_startup_no_site           | 15.8 ms                                                | 18.1 ms: 1.15x slower                                                  |
| crypto_pyaes                     | 54.4 ms                                                | 63.1 ms: 1.16x slower                                                  |
| pyflate                          | 355 ms                                                 | 413 ms: 1.16x slower                                                   |
| typing_runtime_protocols         | 103 us                                                 | 120 us: 1.17x slower                                                   |
| nbody                            | 73.9 ms                                                | 86.2 ms: 1.17x slower                                                  |
| 2to3                             | 181 ms                                                 | 214 ms: 1.18x slower                                                   |
| html5lib                         | 36.6 ms                                                | 44.3 ms: 1.21x slower                                                  |
| scimark_sparse_mat_mult          | 3.00 ms                                                | 3.64 ms: 1.21x slower                                                  |
| scimark_sor                      | 106 ms                                                 | 129 ms: 1.22x slower                                                   |
| pprint_pformat                   | 1.10 sec                                               | 1.34 sec: 1.22x slower                                                 |
| pprint_safe_repr                 | 535 ms                                                 | 655 ms: 1.22x slower                                                   |
| dulwich_log                      | 28.6 ms                                                | 35.3 ms: 1.23x slower                                                  |
| many_optionals                   | 324 us                                                 | 402 us: 1.24x slower                                                   |
| sympy_integrate                  | 11.3 ms                                                | 14.1 ms: 1.25x slower                                                  |
| thrift                           | 465 us                                                 | 580 us: 1.25x slower                                                   |
| hexiom                           | 4.83 ms                                                | 6.10 ms: 1.26x slower                                                  |
| json_dumps                       | 6.51 ms                                                | 8.26 ms: 1.27x slower                                                  |
| unpickle_pure_python             | 164 us                                                 | 209 us: 1.27x slower                                                   |
| async_tree_eager                 | 69.9 ms                                                | 89.8 ms: 1.28x slower                                                  |
| logging_format                   | 3.90 us                                                | 5.10 us: 1.31x slower                                                  |
| sqlalchemy_imperative            | 6.68 ms                                                | 8.73 ms: 1.31x slower                                                  |
| logging_simple                   | 3.59 us                                                | 4.70 us: 1.31x slower                                                  |
| django_template                  | 20.5 ms                                                | 27.0 ms: 1.32x slower                                                  |
| go                               | 115 ms                                                 | 154 ms: 1.34x slower                                                   |
| sympy_str                        | 145 ms                                                 | 196 ms: 1.35x slower                                                   |
| sqlalchemy_declarative           | 59.1 ms                                                | 80.9 ms: 1.37x slower                                                  |
| richards_super                   | 39.2 ms                                                | 53.8 ms: 1.37x slower                                                  |
| richards                         | 35.2 ms                                                | 48.6 ms: 1.38x slower                                                  |
| pickle_pure_python               | 214 us                                                 | 296 us: 1.39x slower                                                   |
| scimark_monte_carlo              | 50.6 ms                                                | 70.2 ms: 1.39x slower                                                  |
| comprehensions                   | 12.0 us                                                | 17.1 us: 1.42x slower                                                  |
| chaos                            | 41.3 ms                                                | 59.2 ms: 1.43x slower                                                  |
| mako                             | 7.70 ms                                                | 11.1 ms: 1.44x slower                                                  |
| async_tree_eager_tg              | 48.0 ms                                                | 69.5 ms: 1.45x slower                                                  |
| scimark_lu                       | 76.7 ms                                                | 112 ms: 1.46x slower                                                   |
| float                            | 56.3 ms                                                | 82.9 ms: 1.47x slower                                                  |
| sympy_expand                     | 247 ms                                                 | 372 ms: 1.51x slower                                                   |
| bench_thread_pool                | 508 us                                                 | 802 us: 1.58x slower                                                   |
| sqlglot_transpile                | 1.03 ms                                                | 1.63 ms: 1.58x slower                                                  |
| subparsers                       | 9.50 ms                                                | 15.1 ms: 1.59x slower                                                  |
| sympy_sum                        | 75.1 ms                                                | 121 ms: 1.61x slower                                                   |
| raytrace                         | 181 ms                                                 | 297 ms: 1.64x slower                                                   |
| logging_silent                   | 70.1 ns                                                | 117 ns: 1.67x slower                                                   |
| sqlglot_parse                    | 859 us                                                 | 1.44 ms: 1.68x slower                                                  |
| deltablue                        | 2.67 ms                                                | 4.89 ms: 1.83x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.13x slower                                                           |

Benchmark hidden because not significant (1): pylint
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20241214-3.14.0a2+-0ac40ac-NOGIL/bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json: mypy2

- Geometric mean (including insignificant results): 1.109x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.16x