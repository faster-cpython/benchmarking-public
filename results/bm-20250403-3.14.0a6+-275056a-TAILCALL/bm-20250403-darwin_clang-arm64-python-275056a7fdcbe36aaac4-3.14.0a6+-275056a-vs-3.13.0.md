# Results vs. 3.13.0

- fork: python
- ref: 275056a7fdcbe36aaac4
- machine: darwin-arm64
- commit hash: 275056a
- commit date: 2025-04-03
- overall geometric mean: 1.151x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 186 ms: 1.04x slower                                                   |
| docutils       | 1.44 sec                                               | 1.37 sec: 1.05x faster                                                 |
| html5lib       | 36.7 ms                                                | 29.0 ms: 1.27x faster                                                  |
| sphinx         | 602 ms                                                 | 548 ms: 1.10x faster                                                   |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 181 ms: 1.59x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 338 ms: 1.51x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 179 ms: 1.50x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 339 ms: 1.50x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 339 ms: 1.48x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 143 ms: 1.39x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 348 ms: 1.38x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 155 ms: 1.37x faster                                                   |
| coroutines                       | 20.0 ms                                                | 14.8 ms: 1.36x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 130 ms: 1.29x faster                                                   |
| async_tree_eager                 | 69.9 ms                                                | 56.2 ms: 1.24x faster                                                  |
| async_generators                 | 294 ms                                                 | 239 ms: 1.23x faster                                                   |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 398 ms: 1.15x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 398 ms: 1.13x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 345 ms: 1.08x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 378 ms: 1.09x slower                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 160 ms: 1.16x slower                                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 124 ms: 2.61x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.18x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 42.9 ms: 1.30x faster                                                  |
| nbody          | 73.6 ms                                                | 71.6 ms: 1.03x faster                                                  |
| pidigits       | 284 ms                                                 | 280 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 78.3 ms                                                | 62.0 ms: 1.26x faster                                                  |
| regex_effbot   | 2.63 ms                                                | 2.39 ms: 1.10x faster                                                  |
| regex_v8       | 17.0 ms                                                | 16.7 ms: 1.02x faster                                                  |
| regex_dna      | 149 ms                                                 | 148 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.16 sec: 1.35x faster                                                 |
| unpickle_pure_python | 165 us                                                 | 129 us: 1.28x faster                                                   |
| xml_etree_process    | 41.3 ms                                                | 34.4 ms: 1.20x faster                                                  |
| xml_etree_generate   | 57.1 ms                                                | 48.5 ms: 1.18x faster                                                  |
| pickle_pure_python   | 215 us                                                 | 186 us: 1.16x faster                                                   |
| xml_etree_parse      | 108 ms                                                 | 98.8 ms: 1.09x faster                                                  |
| xml_etree_iterparse  | 74.2 ms                                                | 70.2 ms: 1.06x faster                                                  |
| json_loads           | 17.0 us                                                | 18.0 us: 1.06x slower                                                  |
| json_dumps           | 6.47 ms                                                | 7.20 ms: 1.11x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 19.2 ms: 1.02x slower                                                  |
| python_startup_no_site | 13.7 ms                                                | 14.9 ms: 1.08x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 12.7 ms: 1.33x faster                                                  |
| genshi_xml      | 34.1 ms                                                | 26.7 ms: 1.27x faster                                                  |
| django_template | 20.5 ms                                                | 19.3 ms: 1.06x faster                                                  |
| mako            | 7.75 ms                                                | 7.32 ms: 1.06x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.18x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 691 ms: 2.17x faster                                                   |
| deepcopy_memo                    | 27.4 us                                                | 16.0 us: 1.71x faster                                                  |
| generators                       | 31.9 ms                                                | 19.0 ms: 1.68x faster                                                  |
| deepcopy                         | 236 us                                                 | 141 us: 1.67x faster                                                   |
| go                               | 117 ms                                                 | 70.8 ms: 1.65x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 181 ms: 1.59x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 338 ms: 1.51x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 179 ms: 1.50x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 339 ms: 1.50x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 339 ms: 1.48x faster                                                   |
| scimark_sor                      | 106 ms                                                 | 75.2 ms: 1.41x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 143 ms: 1.39x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 348 ms: 1.38x faster                                                   |
| deepcopy_reduce                  | 2.09 us                                                | 1.53 us: 1.37x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 155 ms: 1.37x faster                                                   |
| coroutines                       | 20.0 ms                                                | 14.8 ms: 1.36x faster                                                  |
| tomli_loads                      | 1.57 sec                                               | 1.16 sec: 1.35x faster                                                 |
| genshi_text                      | 16.9 ms                                                | 12.7 ms: 1.33x faster                                                  |
| float                            | 55.8 ms                                                | 42.9 ms: 1.30x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 130 ms: 1.29x faster                                                   |
| pyflate                          | 352 ms                                                 | 273 ms: 1.29x faster                                                   |
| deltablue                        | 2.65 ms                                                | 2.06 ms: 1.28x faster                                                  |
| unpickle_pure_python             | 165 us                                                 | 129 us: 1.28x faster                                                   |
| scimark_monte_carlo              | 50.4 ms                                                | 39.4 ms: 1.28x faster                                                  |
| genshi_xml                       | 34.1 ms                                                | 26.7 ms: 1.27x faster                                                  |
| hexiom                           | 4.87 ms                                                | 3.83 ms: 1.27x faster                                                  |
| html5lib                         | 36.7 ms                                                | 29.0 ms: 1.27x faster                                                  |
| regex_compile                    | 78.3 ms                                                | 62.0 ms: 1.26x faster                                                  |
| async_tree_eager                 | 69.9 ms                                                | 56.2 ms: 1.24x faster                                                  |
| richards                         | 36.2 ms                                                | 29.4 ms: 1.23x faster                                                  |
| async_generators                 | 294 ms                                                 | 239 ms: 1.23x faster                                                   |
| dulwich_log                      | 28.7 ms                                                | 23.4 ms: 1.23x faster                                                  |
| logging_silent                   | 71.0 ns                                                | 57.9 ns: 1.23x faster                                                  |
| xml_etree_process                | 41.3 ms                                                | 34.4 ms: 1.20x faster                                                  |
| comprehensions                   | 12.0 us                                                | 10.1 us: 1.19x faster                                                  |
| pylint                           | 180 ms                                                 | 151 ms: 1.19x faster                                                   |
| richards_super                   | 39.2 ms                                                | 33.1 ms: 1.18x faster                                                  |
| pprint_pformat                   | 1.10 sec                                               | 929 ms: 1.18x faster                                                   |
| logging_simple                   | 3.56 us                                                | 3.01 us: 1.18x faster                                                  |
| xml_etree_generate               | 57.1 ms                                                | 48.5 ms: 1.18x faster                                                  |
| logging_format                   | 3.85 us                                                | 3.28 us: 1.17x faster                                                  |
| pprint_safe_repr                 | 541 ms                                                 | 461 ms: 1.17x faster                                                   |
| nqueens                          | 61.8 ms                                                | 52.8 ms: 1.17x faster                                                  |
| typing_runtime_protocols         | 101 us                                                 | 86.5 us: 1.16x faster                                                  |
| bpe_tokeniser                    | 3.26 sec                                               | 2.81 sec: 1.16x faster                                                 |
| chaos                            | 41.1 ms                                                | 35.5 ms: 1.16x faster                                                  |
| pickle_pure_python               | 215 us                                                 | 186 us: 1.16x faster                                                   |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 398 ms: 1.15x faster                                                   |
| raytrace                         | 181 ms                                                 | 157 ms: 1.15x faster                                                   |
| spectral_norm                    | 76.5 ms                                                | 66.8 ms: 1.15x faster                                                  |
| sympy_expand                     | 248 ms                                                 | 219 ms: 1.13x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 398 ms: 1.13x faster                                                   |
| pycparser                        | 701 ms                                                 | 626 ms: 1.12x faster                                                   |
| sympy_integrate                  | 11.3 ms                                                | 10.1 ms: 1.12x faster                                                  |
| crypto_pyaes                     | 55.3 ms                                                | 49.5 ms: 1.12x faster                                                  |
| sympy_str                        | 146 ms                                                 | 130 ms: 1.12x faster                                                   |
| fannkuch                         | 279 ms                                                 | 251 ms: 1.11x faster                                                   |
| regex_effbot                     | 2.63 ms                                                | 2.39 ms: 1.10x faster                                                  |
| sphinx                           | 602 ms                                                 | 548 ms: 1.10x faster                                                   |
| scimark_lu                       | 75.9 ms                                                | 69.4 ms: 1.09x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 98.8 ms: 1.09x faster                                                  |
| bench_thread_pool                | 503 us                                                 | 462 us: 1.09x faster                                                   |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.18 ms: 1.08x faster                                                  |
| k_core                           | 1.61 sec                                               | 1.49 sec: 1.08x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 345 ms: 1.08x faster                                                   |
| bench_mp_pool                    | 64.7 ms                                                | 60.0 ms: 1.08x faster                                                  |
| sympy_sum                        | 75.1 ms                                                | 69.9 ms: 1.07x faster                                                  |
| telco                            | 4.84 ms                                                | 4.51 ms: 1.07x faster                                                  |
| sqlalchemy_declarative           | 59.0 ms                                                | 55.2 ms: 1.07x faster                                                  |
| connected_components             | 319 ms                                                 | 299 ms: 1.07x faster                                                   |
| shortest_path                    | 345 ms                                                 | 324 ms: 1.06x faster                                                   |
| django_template                  | 20.5 ms                                                | 19.3 ms: 1.06x faster                                                  |
| mako                             | 7.75 ms                                                | 7.32 ms: 1.06x faster                                                  |
| xml_etree_iterparse              | 74.2 ms                                                | 70.2 ms: 1.06x faster                                                  |
| docutils                         | 1.44 sec                                               | 1.37 sec: 1.05x faster                                                 |
| meteor_contest                   | 74.0 ms                                                | 70.4 ms: 1.05x faster                                                  |
| scimark_fft                      | 200 ms                                                 | 194 ms: 1.03x faster                                                   |
| nbody                            | 73.6 ms                                                | 71.6 ms: 1.03x faster                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.52 us: 1.02x faster                                                  |
| coverage                         | 46.2 ms                                                | 45.3 ms: 1.02x faster                                                  |
| regex_v8                         | 17.0 ms                                                | 16.7 ms: 1.02x faster                                                  |
| pidigits                         | 284 ms                                                 | 280 ms: 1.01x faster                                                   |
| regex_dna                        | 149 ms                                                 | 148 ms: 1.01x faster                                                   |
| python_startup                   | 18.8 ms                                                | 19.2 ms: 1.02x slower                                                  |
| many_optionals                   | 409 us                                                 | 420 us: 1.03x slower                                                   |
| 2to3                             | 179 ms                                                 | 186 ms: 1.04x slower                                                   |
| gc_traversal                     | 2.94 ms                                                | 3.09 ms: 1.05x slower                                                  |
| json_loads                       | 17.0 us                                                | 18.0 us: 1.06x slower                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 1.27 ms: 1.06x slower                                                  |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.20 ms: 1.07x slower                                                  |
| python_startup_no_site           | 13.7 ms                                                | 14.9 ms: 1.08x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 378 ms: 1.09x slower                                                   |
| json_dumps                       | 6.47 ms                                                | 7.20 ms: 1.11x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 160 ms: 1.16x slower                                                   |
| subparsers                       | 9.44 ms                                                | 11.5 ms: 1.22x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 124 ms: 2.61x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.15x faster                                                           |

Benchmark hidden because not significant (3): json, asyncio_websockets, pathlib
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250403-3.14.0a6+-275056a-CLANG/bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.151x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: 1.08x