# Results vs. 3.13.0

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: darwin-arm64
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.082x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 181 ms                                                 | 169 ms: 1.07x faster                                                   |
| docutils       | 1.44 sec                                               | 1.42 sec: 1.02x faster                                                 |
| html5lib       | 36.6 ms                                                | 31.6 ms: 1.16x faster                                                  |
| sphinx         | 600 ms                                                 | 573 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 289 ms                                                 | 194 ms: 1.49x faster                                                   |
| async_tree_eager_io              | 514 ms                                                 | 377 ms: 1.36x faster                                                   |
| async_tree_io                    | 510 ms                                                 | 381 ms: 1.34x faster                                                   |
| async_tree_io_tg                 | 499 ms                                                 | 380 ms: 1.31x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 206 ms: 1.30x faster                                                   |
| async_tree_none_tg               | 199 ms                                                 | 157 ms: 1.26x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 170 ms: 1.25x faster                                                   |
| async_tree_eager_io_tg           | 481 ms                                                 | 388 ms: 1.24x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 145 ms: 1.16x faster                                                   |
| coroutines                       | 19.8 ms                                                | 17.4 ms: 1.14x faster                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 126 ms: 1.09x faster                                                   |
| async_tree_eager                 | 69.9 ms                                                | 64.2 ms: 1.09x faster                                                  |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 426 ms: 1.08x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 421 ms: 1.07x faster                                                   |
| async_tree_eager_tg              | 48.0 ms                                                | 45.7 ms: 1.05x faster                                                  |
| async_generators                 | 292 ms                                                 | 283 ms: 1.03x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 364 ms: 1.02x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 346 ms                                                 | 342 ms: 1.01x faster                                                   |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.01x faster                                                   |
| Geometric mean                   | (ref)                                                  | 1.17x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 56.3 ms                                                | 51.4 ms: 1.09x faster                                                  |
| nbody          | 73.9 ms                                                | 68.4 ms: 1.08x faster                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.62 ms                                                | 2.03 ms: 1.29x faster                                                  |
| regex_compile  | 78.6 ms                                                | 70.7 ms: 1.11x faster                                                  |
| regex_dna      | 148 ms                                                 | 136 ms: 1.09x faster                                                   |
| regex_v8       | 17.0 ms                                                | 15.7 ms: 1.08x faster                                                  |
| Geometric mean | (ref)                                                  | 1.14x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 164 us                                                 | 153 us: 1.07x faster                                                   |
| tomli_loads          | 1.56 sec                                               | 1.46 sec: 1.07x faster                                                 |
| xml_etree_generate   | 57.0 ms                                                | 53.5 ms: 1.07x faster                                                  |
| xml_etree_process    | 41.0 ms                                                | 39.3 ms: 1.04x faster                                                  |
| xml_etree_parse      | 107 ms                                                 | 103 ms: 1.04x faster                                                   |
| json_loads           | 17.0 us                                                | 16.6 us: 1.03x faster                                                  |
| pickle_pure_python   | 214 us                                                 | 208 us: 1.03x faster                                                   |
| xml_etree_iterparse  | 74.1 ms                                                | 72.7 ms: 1.02x faster                                                  |
| json_dumps           | 6.51 ms                                                | 7.35 ms: 1.13x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                | 21.4 ms: 1.04x slower                                                  |
| python_startup_no_site | 15.8 ms                                                | 16.5 ms: 1.05x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.04x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 14.8 ms: 1.15x faster                                                  |
| mako            | 7.70 ms                                                | 6.93 ms: 1.11x faster                                                  |
| genshi_xml      | 34.1 ms                                                | 31.5 ms: 1.08x faster                                                  |
| django_template | 20.5 ms                                                | 21.2 ms: 1.03x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy                         | 234 us                                                 | 151 us: 1.55x faster                                                   |
| deepcopy_memo                    | 27.3 us                                                | 18.1 us: 1.51x faster                                                  |
| async_tree_memoization_tg        | 289 ms                                                 | 194 ms: 1.49x faster                                                   |
| generators                       | 31.5 ms                                                | 22.8 ms: 1.38x faster                                                  |
| async_tree_eager_io              | 514 ms                                                 | 377 ms: 1.36x faster                                                   |
| async_tree_io                    | 510 ms                                                 | 381 ms: 1.34x faster                                                   |
| go                               | 115 ms                                                 | 86.9 ms: 1.32x faster                                                  |
| async_tree_io_tg                 | 499 ms                                                 | 380 ms: 1.31x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 206 ms: 1.30x faster                                                   |
| deepcopy_reduce                  | 2.08 us                                                | 1.61 us: 1.29x faster                                                  |
| regex_effbot                     | 2.62 ms                                                | 2.03 ms: 1.29x faster                                                  |
| async_tree_none_tg               | 199 ms                                                 | 157 ms: 1.26x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 170 ms: 1.25x faster                                                   |
| async_tree_eager_io_tg           | 481 ms                                                 | 388 ms: 1.24x faster                                                   |
| spectral_norm                    | 76.3 ms                                                | 61.8 ms: 1.23x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 145 ms: 1.16x faster                                                   |
| html5lib                         | 36.6 ms                                                | 31.6 ms: 1.16x faster                                                  |
| scimark_fft                      | 200 ms                                                 | 174 ms: 1.15x faster                                                   |
| genshi_text                      | 16.9 ms                                                | 14.8 ms: 1.15x faster                                                  |
| coroutines                       | 19.8 ms                                                | 17.4 ms: 1.14x faster                                                  |
| pprint_pformat                   | 1.10 sec                                               | 986 ms: 1.11x faster                                                   |
| regex_compile                    | 78.6 ms                                                | 70.7 ms: 1.11x faster                                                  |
| pylint                           | 179 ms                                                 | 161 ms: 1.11x faster                                                   |
| mako                             | 7.70 ms                                                | 6.93 ms: 1.11x faster                                                  |
| scimark_sor                      | 106 ms                                                 | 95.6 ms: 1.10x faster                                                  |
| pprint_safe_repr                 | 535 ms                                                 | 485 ms: 1.10x faster                                                   |
| scimark_sparse_mat_mult          | 3.00 ms                                                | 2.72 ms: 1.10x faster                                                  |
| logging_simple                   | 3.59 us                                                | 3.26 us: 1.10x faster                                                  |
| scimark_monte_carlo              | 50.6 ms                                                | 46.1 ms: 1.10x faster                                                  |
| float                            | 56.3 ms                                                | 51.4 ms: 1.09x faster                                                  |
| logging_format                   | 3.90 us                                                | 3.57 us: 1.09x faster                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 126 ms: 1.09x faster                                                   |
| regex_dna                        | 148 ms                                                 | 136 ms: 1.09x faster                                                   |
| async_tree_eager                 | 69.9 ms                                                | 64.2 ms: 1.09x faster                                                  |
| regex_v8                         | 17.0 ms                                                | 15.7 ms: 1.08x faster                                                  |
| pyflate                          | 355 ms                                                 | 327 ms: 1.08x faster                                                   |
| genshi_xml                       | 34.1 ms                                                | 31.5 ms: 1.08x faster                                                  |
| deltablue                        | 2.67 ms                                                | 2.47 ms: 1.08x faster                                                  |
| nbody                            | 73.9 ms                                                | 68.4 ms: 1.08x faster                                                  |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 426 ms: 1.08x faster                                                   |
| pycparser                        | 708 ms                                                 | 658 ms: 1.08x faster                                                   |
| sqlglot_parse                    | 859 us                                                 | 800 us: 1.07x faster                                                   |
| 2to3                             | 181 ms                                                 | 169 ms: 1.07x faster                                                   |
| fannkuch                         | 285 ms                                                 | 266 ms: 1.07x faster                                                   |
| unpickle_pure_python             | 164 us                                                 | 153 us: 1.07x faster                                                   |
| json                             | 3.06 ms                                                | 2.86 ms: 1.07x faster                                                  |
| tomli_loads                      | 1.56 sec                                               | 1.46 sec: 1.07x faster                                                 |
| thrift                           | 465 us                                                 | 436 us: 1.07x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 421 ms: 1.07x faster                                                   |
| xml_etree_generate               | 57.0 ms                                                | 53.5 ms: 1.07x faster                                                  |
| hexiom                           | 4.83 ms                                                | 4.54 ms: 1.07x faster                                                  |
| sqlglot_optimize                 | 34.8 ms                                                | 32.7 ms: 1.06x faster                                                  |
| raytrace                         | 181 ms                                                 | 170 ms: 1.06x faster                                                   |
| nqueens                          | 61.8 ms                                                | 58.2 ms: 1.06x faster                                                  |
| richards_super                   | 39.2 ms                                                | 36.9 ms: 1.06x faster                                                  |
| sqlglot_transpile                | 1.03 ms                                                | 971 us: 1.06x faster                                                   |
| chaos                            | 41.3 ms                                                | 39.0 ms: 1.06x faster                                                  |
| richards                         | 35.2 ms                                                | 33.4 ms: 1.05x faster                                                  |
| sqlglot_normalize                | 188 ms                                                 | 179 ms: 1.05x faster                                                   |
| async_tree_eager_tg              | 48.0 ms                                                | 45.7 ms: 1.05x faster                                                  |
| bench_thread_pool                | 508 us                                                 | 483 us: 1.05x faster                                                   |
| sphinx                           | 600 ms                                                 | 573 ms: 1.05x faster                                                   |
| k_core                           | 1.62 sec                                               | 1.55 sec: 1.04x faster                                                 |
| xml_etree_process                | 41.0 ms                                                | 39.3 ms: 1.04x faster                                                  |
| xml_etree_parse                  | 107 ms                                                 | 103 ms: 1.04x faster                                                   |
| telco                            | 4.79 ms                                                | 4.60 ms: 1.04x faster                                                  |
| scimark_lu                       | 76.7 ms                                                | 73.6 ms: 1.04x faster                                                  |
| bpe_tokeniser                    | 3.25 sec                                               | 3.12 sec: 1.04x faster                                                 |
| pathlib                          | 23.3 ms                                                | 22.4 ms: 1.04x faster                                                  |
| sympy_expand                     | 247 ms                                                 | 237 ms: 1.04x faster                                                   |
| typing_runtime_protocols         | 103 us                                                 | 98.6 us: 1.04x faster                                                  |
| meteor_contest                   | 75.1 ms                                                | 72.3 ms: 1.04x faster                                                  |
| async_generators                 | 292 ms                                                 | 283 ms: 1.03x faster                                                   |
| sqlalchemy_imperative            | 6.68 ms                                                | 6.49 ms: 1.03x faster                                                  |
| coverage                         | 45.5 ms                                                | 44.2 ms: 1.03x faster                                                  |
| dulwich_log                      | 28.6 ms                                                | 27.8 ms: 1.03x faster                                                  |
| json_loads                       | 17.0 us                                                | 16.6 us: 1.03x faster                                                  |
| pickle_pure_python               | 214 us                                                 | 208 us: 1.03x faster                                                   |
| sympy_str                        | 145 ms                                                 | 141 ms: 1.02x faster                                                   |
| bench_mp_pool                    | 64.9 ms                                                | 63.4 ms: 1.02x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 364 ms: 1.02x faster                                                   |
| docutils                         | 1.44 sec                                               | 1.42 sec: 1.02x faster                                                 |
| xml_etree_iterparse              | 74.1 ms                                                | 72.7 ms: 1.02x faster                                                  |
| sqlite_synth                     | 1.56 us                                                | 1.53 us: 1.02x faster                                                  |
| sympy_sum                        | 75.1 ms                                                | 73.9 ms: 1.02x faster                                                  |
| shortest_path                    | 349 ms                                                 | 344 ms: 1.01x faster                                                   |
| logging_silent                   | 70.1 ns                                                | 69.3 ns: 1.01x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 346 ms                                                 | 342 ms: 1.01x faster                                                   |
| sqlalchemy_declarative           | 59.1 ms                                                | 58.7 ms: 1.01x faster                                                  |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.01x faster                                                   |
| connected_components             | 320 ms                                                 | 319 ms: 1.00x faster                                                   |
| mdp                              | 1.50 sec                                               | 1.52 sec: 1.01x slower                                                 |
| sympy_integrate                  | 11.3 ms                                                | 11.5 ms: 1.02x slower                                                  |
| django_template                  | 20.5 ms                                                | 21.2 ms: 1.03x slower                                                  |
| python_startup                   | 20.6 ms                                                | 21.4 ms: 1.04x slower                                                  |
| comprehensions                   | 12.0 us                                                | 12.5 us: 1.04x slower                                                  |
| gc_traversal                     | 2.93 ms                                                | 3.07 ms: 1.05x slower                                                  |
| python_startup_no_site           | 15.8 ms                                                | 16.5 ms: 1.05x slower                                                  |
| create_gc_cycles                 | 1.20 ms                                                | 1.27 ms: 1.06x slower                                                  |
| many_optionals                   | 324 us                                                 | 360 us: 1.11x slower                                                   |
| json_dumps                       | 6.51 ms                                                | 7.35 ms: 1.13x slower                                                  |
| subparsers                       | 9.50 ms                                                | 12.2 ms: 1.29x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.08x faster                                                           |

Benchmark hidden because not significant (2): pidigits, crypto_pyaes
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json: mypy2

- Geometric mean (including insignificant results): 1.082x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.03x