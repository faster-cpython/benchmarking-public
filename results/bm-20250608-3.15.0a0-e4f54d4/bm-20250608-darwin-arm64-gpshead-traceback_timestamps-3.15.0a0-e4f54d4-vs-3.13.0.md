# Results vs. 3.13.0

- fork: gpshead
- ref: traceback_timestamps
- machine: darwin-arm64
- commit hash: e4f54d4
- commit date: 2025-06-08
- overall geometric mean: 1.044x slower
- HPT reliability: 99.97%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-darwin-arm64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 262 ms: 1.47x slower                                                   |
| docutils       | 1.44 sec                                               | 1.52 sec: 1.05x slower                                                 |
| html5lib       | 36.7 ms                                                | 31.5 ms: 1.16x faster                                                  |
| sphinx         | 602 ms                                                 | 592 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.07x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-darwin-arm64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 192 ms: 1.50x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 363 ms: 1.41x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 195 ms: 1.37x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 377 ms: 1.35x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 374 ms: 1.34x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 164 ms: 1.29x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 373 ms: 1.28x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 157 ms: 1.26x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.20x faster                                                   |
| coroutines                       | 20.0 ms                                                | 17.0 ms: 1.18x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 415 ms: 1.11x faster                                                   |
| async_generators                 | 294 ms                                                 | 267 ms: 1.10x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 411 ms: 1.09x faster                                                   |
| async_tree_eager                 | 69.9 ms                                                | 64.3 ms: 1.09x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 357 ms: 1.04x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 390 ms: 1.12x slower                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 168 ms: 1.22x slower                                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 130 ms: 2.74x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.10x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-darwin-arm64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 49.7 ms: 1.12x faster                                                  |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                                   |
| nbody          | 73.6 ms                                                | 74.0 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-darwin-arm64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.38 ms: 1.11x faster                                                  |
| regex_compile  | 78.3 ms                                                | 71.8 ms: 1.09x faster                                                  |
| regex_dna      | 149 ms                                                 | 143 ms: 1.04x faster                                                   |
| regex_v8       | 17.0 ms                                                | 16.4 ms: 1.04x faster                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-darwin-arm64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.36 sec: 1.15x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 99.7 ms: 1.08x faster                                                  |
| xml_etree_iterparse  | 74.2 ms                                                | 69.6 ms: 1.07x faster                                                  |
| xml_etree_process    | 41.3 ms                                                | 38.9 ms: 1.06x faster                                                  |
| xml_etree_generate   | 57.1 ms                                                | 53.8 ms: 1.06x faster                                                  |
| json_loads           | 17.0 us                                                | 16.4 us: 1.04x faster                                                  |
| unpickle_pure_python | 165 us                                                 | 160 us: 1.03x faster                                                   |
| pickle_pure_python   | 215 us                                                 | 217 us: 1.01x slower                                                   |
| json_dumps           | 6.47 ms                                                | 6.56 ms: 1.01x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-darwin-arm64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 13.7 ms                                                | 18.7 ms: 1.36x slower                                                  |
| python_startup         | 18.8 ms                                                | 28.1 ms: 1.50x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.43x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-darwin-arm64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 14.7 ms: 1.15x faster                                                  |
| genshi_xml      | 34.1 ms                                                | 31.1 ms: 1.10x faster                                                  |
| mako            | 7.75 ms                                                | 7.87 ms: 1.01x slower                                                  |
| django_template | 20.5 ms                                                | 21.9 ms: 1.07x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-darwin-arm64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 761 ms: 1.97x faster                                                   |
| async_tree_memoization_tg        | 288 ms                                                 | 192 ms: 1.50x faster                                                   |
| deepcopy                         | 236 us                                                 | 159 us: 1.49x faster                                                   |
| deepcopy_memo                    | 27.4 us                                                | 19.3 us: 1.42x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 363 ms: 1.41x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 195 ms: 1.37x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 377 ms: 1.35x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 374 ms: 1.34x faster                                                   |
| go                               | 117 ms                                                 | 87.7 ms: 1.33x faster                                                  |
| generators                       | 31.9 ms                                                | 24.2 ms: 1.32x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 164 ms: 1.29x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 373 ms: 1.28x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 157 ms: 1.26x faster                                                   |
| deepcopy_reduce                  | 2.09 us                                                | 1.70 us: 1.23x faster                                                  |
| pathlib                          | 23.2 ms                                                | 19.3 ms: 1.20x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.20x faster                                                   |
| scimark_sor                      | 106 ms                                                 | 88.9 ms: 1.19x faster                                                  |
| coroutines                       | 20.0 ms                                                | 17.0 ms: 1.18x faster                                                  |
| html5lib                         | 36.7 ms                                                | 31.5 ms: 1.16x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 24.9 ms: 1.16x faster                                                  |
| genshi_text                      | 16.9 ms                                                | 14.7 ms: 1.15x faster                                                  |
| tomli_loads                      | 1.57 sec                                               | 1.36 sec: 1.15x faster                                                 |
| float                            | 55.8 ms                                                | 49.7 ms: 1.12x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 415 ms: 1.11x faster                                                   |
| regex_effbot                     | 2.63 ms                                                | 2.38 ms: 1.11x faster                                                  |
| pyflate                          | 352 ms                                                 | 318 ms: 1.11x faster                                                   |
| async_generators                 | 294 ms                                                 | 267 ms: 1.10x faster                                                   |
| pylint                           | 180 ms                                                 | 163 ms: 1.10x faster                                                   |
| genshi_xml                       | 34.1 ms                                                | 31.1 ms: 1.10x faster                                                  |
| k_core                           | 1.61 sec                                               | 1.47 sec: 1.09x faster                                                 |
| regex_compile                    | 78.3 ms                                                | 71.8 ms: 1.09x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 411 ms: 1.09x faster                                                   |
| async_tree_eager                 | 69.9 ms                                                | 64.3 ms: 1.09x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 99.7 ms: 1.08x faster                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 46.7 ms: 1.08x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 70.9 ms: 1.08x faster                                                  |
| telco                            | 4.84 ms                                                | 4.50 ms: 1.08x faster                                                  |
| xml_etree_iterparse              | 74.2 ms                                                | 69.6 ms: 1.07x faster                                                  |
| xml_etree_process                | 41.3 ms                                                | 38.9 ms: 1.06x faster                                                  |
| xml_etree_generate               | 57.1 ms                                                | 53.8 ms: 1.06x faster                                                  |
| json                             | 3.04 ms                                                | 2.87 ms: 1.06x faster                                                  |
| bpe_tokeniser                    | 3.26 sec                                               | 3.08 sec: 1.06x faster                                                 |
| shortest_path                    | 345 ms                                                 | 329 ms: 1.05x faster                                                   |
| hexiom                           | 4.87 ms                                                | 4.66 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 357 ms: 1.04x faster                                                   |
| json_loads                       | 17.0 us                                                | 16.4 us: 1.04x faster                                                  |
| regex_dna                        | 149 ms                                                 | 143 ms: 1.04x faster                                                   |
| fannkuch                         | 279 ms                                                 | 268 ms: 1.04x faster                                                   |
| connected_components             | 319 ms                                                 | 307 ms: 1.04x faster                                                   |
| typing_runtime_protocols         | 101 us                                                 | 97.1 us: 1.04x faster                                                  |
| regex_v8                         | 17.0 ms                                                | 16.4 ms: 1.04x faster                                                  |
| unpickle_pure_python             | 165 us                                                 | 160 us: 1.03x faster                                                   |
| pycparser                        | 701 ms                                                 | 681 ms: 1.03x faster                                                   |
| sympy_expand                     | 248 ms                                                 | 241 ms: 1.03x faster                                                   |
| sympy_integrate                  | 11.3 ms                                                | 11.1 ms: 1.02x faster                                                  |
| deltablue                        | 2.65 ms                                                | 2.59 ms: 1.02x faster                                                  |
| scimark_fft                      | 200 ms                                                 | 196 ms: 1.02x faster                                                   |
| chaos                            | 41.1 ms                                                | 40.4 ms: 1.02x faster                                                  |
| sphinx                           | 602 ms                                                 | 592 ms: 1.02x faster                                                   |
| sympy_str                        | 146 ms                                                 | 143 ms: 1.02x faster                                                   |
| richards                         | 36.2 ms                                                | 35.9 ms: 1.01x faster                                                  |
| raytrace                         | 181 ms                                                 | 180 ms: 1.01x faster                                                   |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                                   |
| nbody                            | 73.6 ms                                                | 74.0 ms: 1.01x slower                                                  |
| comprehensions                   | 12.0 us                                                | 12.0 us: 1.01x slower                                                  |
| sympy_sum                        | 75.1 ms                                                | 75.7 ms: 1.01x slower                                                  |
| pickle_pure_python               | 215 us                                                 | 217 us: 1.01x slower                                                   |
| json_dumps                       | 6.47 ms                                                | 6.56 ms: 1.01x slower                                                  |
| richards_super                   | 39.2 ms                                                | 39.8 ms: 1.01x slower                                                  |
| mako                             | 7.75 ms                                                | 7.87 ms: 1.01x slower                                                  |
| pprint_pformat                   | 1.10 sec                                               | 1.13 sec: 1.03x slower                                                 |
| pprint_safe_repr                 | 541 ms                                                 | 556 ms: 1.03x slower                                                   |
| sqlite_synth                     | 1.55 us                                                | 1.60 us: 1.03x slower                                                  |
| logging_simple                   | 3.56 us                                                | 3.67 us: 1.03x slower                                                  |
| logging_format                   | 3.85 us                                                | 3.98 us: 1.03x slower                                                  |
| crypto_pyaes                     | 55.3 ms                                                | 57.1 ms: 1.03x slower                                                  |
| docutils                         | 1.44 sec                                               | 1.52 sec: 1.05x slower                                                 |
| dask                             | 771 ms                                                 | 823 ms: 1.07x slower                                                   |
| django_template                  | 20.5 ms                                                | 21.9 ms: 1.07x slower                                                  |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.23 ms: 1.08x slower                                                  |
| gc_traversal                     | 2.94 ms                                                | 3.19 ms: 1.09x slower                                                  |
| scimark_lu                       | 75.9 ms                                                | 83.2 ms: 1.10x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 390 ms: 1.12x slower                                                   |
| create_gc_cycles                 | 1.19 ms                                                | 1.36 ms: 1.14x slower                                                  |
| many_optionals                   | 409 us                                                 | 467 us: 1.14x slower                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 168 ms: 1.22x slower                                                   |
| python_startup_no_site           | 13.7 ms                                                | 18.7 ms: 1.36x slower                                                  |
| subparsers                       | 9.44 ms                                                | 13.7 ms: 1.45x slower                                                  |
| 2to3                             | 179 ms                                                 | 262 ms: 1.47x slower                                                   |
| python_startup                   | 18.8 ms                                                | 28.1 ms: 1.50x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 130 ms: 2.74x slower                                                   |
| logging_silent                   | 71.0 ns                                                | 331 ns: 4.67x slower                                                   |
| coverage                         | 46.2 ms                                                | 291 ms: 6.30x slower                                                   |
| thrift                           | 466 us                                                 | 340 ms: 728.69x slower                                                 |
| Geometric mean                   | (ref)                                                  | 1.06x slower                                                           |

Benchmark hidden because not significant (3): asyncio_websockets, meteor_contest, nqueens
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250608-3.15.0a0-e4f54d4/bm-20250608-darwin-arm64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.044x slower

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.10x