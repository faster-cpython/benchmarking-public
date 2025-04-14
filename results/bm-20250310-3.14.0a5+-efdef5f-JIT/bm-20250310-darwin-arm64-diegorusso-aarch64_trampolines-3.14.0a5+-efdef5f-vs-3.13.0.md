# Results vs. 3.13.0

- fork: diegorusso
- ref: aarch64_trampolines
- machine: darwin-arm64
- commit hash: efdef5f
- commit date: 2025-03-10
- overall geometric mean: 1.094x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250310-darwin-arm64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 163 ms: 1.09x faster                                                      |
| html5lib       | 36.7 ms                                                | 29.3 ms: 1.25x faster                                                     |
| sphinx         | 602 ms                                                 | 574 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                  | 1.09x faster                                                              |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250310-darwin-arm64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 195 ms: 1.47x faster                                                      |
| async_tree_eager_io              | 511 ms                                                 | 364 ms: 1.40x faster                                                      |
| async_tree_io_tg                 | 500 ms                                                 | 359 ms: 1.39x faster                                                      |
| async_tree_memoization           | 268 ms                                                 | 195 ms: 1.37x faster                                                      |
| async_tree_io                    | 508 ms                                                 | 371 ms: 1.37x faster                                                      |
| async_tree_none                  | 212 ms                                                 | 161 ms: 1.32x faster                                                      |
| async_tree_eager_io_tg           | 479 ms                                                 | 369 ms: 1.30x faster                                                      |
| async_tree_none_tg               | 198 ms                                                 | 154 ms: 1.29x faster                                                      |
| coroutines                       | 20.0 ms                                                | 16.5 ms: 1.21x faster                                                     |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.20x faster                                                      |
| async_tree_eager                 | 69.9 ms                                                | 61.1 ms: 1.14x faster                                                     |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 415 ms: 1.11x faster                                                      |
| async_generators                 | 294 ms                                                 | 271 ms: 1.08x faster                                                      |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 416 ms: 1.08x faster                                                      |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 358 ms: 1.04x faster                                                      |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 389 ms: 1.12x slower                                                      |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 172 ms: 1.24x slower                                                      |
| async_tree_eager_tg              | 47.4 ms                                                | 127 ms: 2.69x slower                                                      |
| Geometric mean                   | (ref)                                                  | 1.11x faster                                                              |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250310-darwin-arm64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 44.5 ms: 1.25x faster                                                     |
| nbody          | 73.6 ms                                                | 64.0 ms: 1.15x faster                                                     |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                  | 1.13x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250310-darwin-arm64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.27 ms: 1.16x faster                                                     |
| regex_compile  | 78.3 ms                                                | 68.2 ms: 1.15x faster                                                     |
| regex_v8       | 17.0 ms                                                | 15.7 ms: 1.09x faster                                                     |
| regex_dna      | 149 ms                                                 | 141 ms: 1.06x faster                                                      |
| Geometric mean | (ref)                                                  | 1.11x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250310-darwin-arm64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.18 sec: 1.33x faster                                                    |
| unpickle_pure_python | 165 us                                                 | 132 us: 1.25x faster                                                      |
| xml_etree_process    | 41.3 ms                                                | 35.6 ms: 1.16x faster                                                     |
| xml_etree_generate   | 57.1 ms                                                | 50.4 ms: 1.13x faster                                                     |
| pickle_pure_python   | 215 us                                                 | 196 us: 1.10x faster                                                      |
| xml_etree_parse      | 108 ms                                                 | 103 ms: 1.05x faster                                                      |
| xml_etree_iterparse  | 74.2 ms                                                | 71.0 ms: 1.05x faster                                                     |
| json_loads           | 17.0 us                                                | 17.6 us: 1.03x slower                                                     |
| json_dumps           | 6.47 ms                                                | 7.29 ms: 1.13x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250310-darwin-arm64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 16.5 ms: 1.14x faster                                                     |
| python_startup_no_site | 13.7 ms                                                | 12.4 ms: 1.11x faster                                                     |
| Geometric mean         | (ref)                                                  | 1.13x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250310-darwin-arm64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 13.7 ms: 1.23x faster                                                     |
| mako            | 7.75 ms                                                | 6.47 ms: 1.20x faster                                                     |
| genshi_xml      | 34.1 ms                                                | 29.1 ms: 1.17x faster                                                     |
| django_template | 20.5 ms                                                | 20.9 ms: 1.02x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.14x faster                                                              |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250310-darwin-arm64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy                         | 236 us                                                 | 151 us: 1.57x faster                                                      |
| deepcopy_memo                    | 27.4 us                                                | 18.3 us: 1.49x faster                                                     |
| async_tree_memoization_tg        | 288 ms                                                 | 195 ms: 1.47x faster                                                      |
| async_tree_eager_io              | 511 ms                                                 | 364 ms: 1.40x faster                                                      |
| async_tree_io_tg                 | 500 ms                                                 | 359 ms: 1.39x faster                                                      |
| async_tree_memoization           | 268 ms                                                 | 195 ms: 1.37x faster                                                      |
| async_tree_io                    | 508 ms                                                 | 371 ms: 1.37x faster                                                      |
| generators                       | 31.9 ms                                                | 23.4 ms: 1.37x faster                                                     |
| scimark_sor                      | 106 ms                                                 | 79.4 ms: 1.33x faster                                                     |
| tomli_loads                      | 1.57 sec                                               | 1.18 sec: 1.33x faster                                                    |
| deepcopy_reduce                  | 2.09 us                                                | 1.58 us: 1.33x faster                                                     |
| async_tree_none                  | 212 ms                                                 | 161 ms: 1.32x faster                                                      |
| async_tree_eager_io_tg           | 479 ms                                                 | 369 ms: 1.30x faster                                                      |
| async_tree_none_tg               | 198 ms                                                 | 154 ms: 1.29x faster                                                      |
| go                               | 117 ms                                                 | 92.6 ms: 1.26x faster                                                     |
| float                            | 55.8 ms                                                | 44.5 ms: 1.25x faster                                                     |
| deltablue                        | 2.65 ms                                                | 2.11 ms: 1.25x faster                                                     |
| html5lib                         | 36.7 ms                                                | 29.3 ms: 1.25x faster                                                     |
| unpickle_pure_python             | 165 us                                                 | 132 us: 1.25x faster                                                      |
| richards                         | 36.2 ms                                                | 29.1 ms: 1.24x faster                                                     |
| genshi_text                      | 16.9 ms                                                | 13.7 ms: 1.23x faster                                                     |
| spectral_norm                    | 76.5 ms                                                | 62.2 ms: 1.23x faster                                                     |
| richards_super                   | 39.2 ms                                                | 32.3 ms: 1.22x faster                                                     |
| coroutines                       | 20.0 ms                                                | 16.5 ms: 1.21x faster                                                     |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.20x faster                                                      |
| mako                             | 7.75 ms                                                | 6.47 ms: 1.20x faster                                                     |
| dulwich_log                      | 28.7 ms                                                | 24.4 ms: 1.18x faster                                                     |
| genshi_xml                       | 34.1 ms                                                | 29.1 ms: 1.17x faster                                                     |
| regex_effbot                     | 2.63 ms                                                | 2.27 ms: 1.16x faster                                                     |
| xml_etree_process                | 41.3 ms                                                | 35.6 ms: 1.16x faster                                                     |
| scimark_monte_carlo              | 50.4 ms                                                | 43.6 ms: 1.16x faster                                                     |
| pyflate                          | 352 ms                                                 | 306 ms: 1.15x faster                                                      |
| nbody                            | 73.6 ms                                                | 64.0 ms: 1.15x faster                                                     |
| regex_compile                    | 78.3 ms                                                | 68.2 ms: 1.15x faster                                                     |
| async_tree_eager                 | 69.9 ms                                                | 61.1 ms: 1.14x faster                                                     |
| python_startup                   | 18.8 ms                                                | 16.5 ms: 1.14x faster                                                     |
| xml_etree_generate               | 57.1 ms                                                | 50.4 ms: 1.13x faster                                                     |
| scimark_fft                      | 200 ms                                                 | 177 ms: 1.13x faster                                                      |
| bpe_tokeniser                    | 3.26 sec                                               | 2.91 sec: 1.12x faster                                                    |
| logging_simple                   | 3.56 us                                                | 3.19 us: 1.11x faster                                                     |
| python_startup_no_site           | 13.7 ms                                                | 12.4 ms: 1.11x faster                                                     |
| pylint                           | 180 ms                                                 | 162 ms: 1.11x faster                                                      |
| pprint_pformat                   | 1.10 sec                                               | 993 ms: 1.11x faster                                                      |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 415 ms: 1.11x faster                                                      |
| pprint_safe_repr                 | 541 ms                                                 | 488 ms: 1.11x faster                                                      |
| logging_format                   | 3.85 us                                                | 3.51 us: 1.10x faster                                                     |
| logging_silent                   | 71.0 ns                                                | 64.7 ns: 1.10x faster                                                     |
| pickle_pure_python               | 215 us                                                 | 196 us: 1.10x faster                                                      |
| 2to3                             | 179 ms                                                 | 163 ms: 1.09x faster                                                      |
| typing_runtime_protocols         | 101 us                                                 | 92.5 us: 1.09x faster                                                     |
| regex_v8                         | 17.0 ms                                                | 15.7 ms: 1.09x faster                                                     |
| bench_mp_pool                    | 64.7 ms                                                | 59.7 ms: 1.08x faster                                                     |
| telco                            | 4.84 ms                                                | 4.46 ms: 1.08x faster                                                     |
| async_generators                 | 294 ms                                                 | 271 ms: 1.08x faster                                                      |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 416 ms: 1.08x faster                                                      |
| connected_components             | 319 ms                                                 | 297 ms: 1.07x faster                                                      |
| thrift                           | 466 us                                                 | 436 us: 1.07x faster                                                      |
| k_core                           | 1.61 sec                                               | 1.52 sec: 1.06x faster                                                    |
| regex_dna                        | 149 ms                                                 | 141 ms: 1.06x faster                                                      |
| hexiom                           | 4.87 ms                                                | 4.60 ms: 1.06x faster                                                     |
| nqueens                          | 61.8 ms                                                | 58.7 ms: 1.05x faster                                                     |
| xml_etree_parse                  | 108 ms                                                 | 103 ms: 1.05x faster                                                      |
| shortest_path                    | 345 ms                                                 | 328 ms: 1.05x faster                                                      |
| pycparser                        | 701 ms                                                 | 668 ms: 1.05x faster                                                      |
| sphinx                           | 602 ms                                                 | 574 ms: 1.05x faster                                                      |
| xml_etree_iterparse              | 74.2 ms                                                | 71.0 ms: 1.05x faster                                                     |
| sympy_expand                     | 248 ms                                                 | 237 ms: 1.04x faster                                                      |
| chaos                            | 41.1 ms                                                | 39.4 ms: 1.04x faster                                                     |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 358 ms: 1.04x faster                                                      |
| sympy_str                        | 146 ms                                                 | 140 ms: 1.04x faster                                                      |
| scimark_lu                       | 75.9 ms                                                | 73.3 ms: 1.04x faster                                                     |
| bench_thread_pool                | 503 us                                                 | 487 us: 1.03x faster                                                      |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 2.89 ms: 1.03x faster                                                     |
| mdp                              | 1.50 sec                                               | 1.47 sec: 1.02x faster                                                    |
| sympy_sum                        | 75.1 ms                                                | 73.8 ms: 1.02x faster                                                     |
| raytrace                         | 181 ms                                                 | 178 ms: 1.02x faster                                                      |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.61 ms: 1.01x faster                                                     |
| sqlalchemy_declarative           | 59.0 ms                                                | 58.4 ms: 1.01x faster                                                     |
| crypto_pyaes                     | 55.3 ms                                                | 54.8 ms: 1.01x faster                                                     |
| sqlite_synth                     | 1.55 us                                                | 1.54 us: 1.01x faster                                                     |
| dask                             | 771 ms                                                 | 768 ms: 1.00x faster                                                      |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                                      |
| sympy_integrate                  | 11.3 ms                                                | 11.3 ms: 1.00x slower                                                     |
| comprehensions                   | 12.0 us                                                | 12.1 us: 1.01x slower                                                     |
| meteor_contest                   | 74.0 ms                                                | 74.6 ms: 1.01x slower                                                     |
| django_template                  | 20.5 ms                                                | 20.9 ms: 1.02x slower                                                     |
| json_loads                       | 17.0 us                                                | 17.6 us: 1.03x slower                                                     |
| gc_traversal                     | 2.94 ms                                                | 3.12 ms: 1.06x slower                                                     |
| create_gc_cycles                 | 1.19 ms                                                | 1.29 ms: 1.08x slower                                                     |
| many_optionals                   | 409 us                                                 | 447 us: 1.09x slower                                                      |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 389 ms: 1.12x slower                                                      |
| json_dumps                       | 6.47 ms                                                | 7.29 ms: 1.13x slower                                                     |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 172 ms: 1.24x slower                                                      |
| subparsers                       | 9.44 ms                                                | 11.9 ms: 1.26x slower                                                     |
| async_tree_eager_tg              | 47.4 ms                                                | 127 ms: 2.69x slower                                                      |
| Geometric mean                   | (ref)                                                  | 1.10x faster                                                              |

Benchmark hidden because not significant (6): coverage, asyncio_websockets, fannkuch, docutils, pathlib, json
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250310-3.14.0a5+-efdef5f-JIT/bm-20250310-darwin-arm64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.094x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.10x