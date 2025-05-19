# Results vs. 3.13.0

- fork: faster-cpython
- ref: make_decref_a_call
- machine: darwin-arm64
- commit hash: 4fee8de
- commit date: 2025-05-19
- overall geometric mean: 1.044x slower
- HPT reliability: 99.42%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 190 ms: 1.06x slower                                                          |
| docutils       | 1.44 sec                                               | 1.57 sec: 1.09x slower                                                        |
| html5lib       | 36.7 ms                                                | 34.8 ms: 1.05x faster                                                         |
| sphinx         | 602 ms                                                 | 635 ms: 1.05x slower                                                          |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 217 ms: 1.33x faster                                                          |
| async_tree_eager_io              | 511 ms                                                 | 409 ms: 1.25x faster                                                          |
| async_tree_memoization           | 268 ms                                                 | 222 ms: 1.21x faster                                                          |
| async_tree_io                    | 508 ms                                                 | 426 ms: 1.19x faster                                                          |
| async_tree_io_tg                 | 500 ms                                                 | 421 ms: 1.19x faster                                                          |
| async_tree_eager_io_tg           | 479 ms                                                 | 416 ms: 1.15x faster                                                          |
| async_tree_none                  | 212 ms                                                 | 188 ms: 1.13x faster                                                          |
| async_tree_none_tg               | 198 ms                                                 | 176 ms: 1.12x faster                                                          |
| async_tree_eager_memoization     | 168 ms                                                 | 154 ms: 1.09x faster                                                          |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 429 ms: 1.04x faster                                                          |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 442 ms: 1.04x faster                                                          |
| async_generators                 | 294 ms                                                 | 292 ms: 1.01x faster                                                          |
| coroutines                       | 20.0 ms                                                | 20.3 ms: 1.01x slower                                                         |
| async_tree_eager                 | 69.9 ms                                                | 77.0 ms: 1.10x slower                                                         |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 405 ms: 1.17x slower                                                          |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 189 ms: 1.37x slower                                                          |
| async_tree_eager_tg              | 47.4 ms                                                | 146 ms: 3.09x slower                                                          |
| Geometric mean                   | (ref)                                                  | 1.01x slower                                                                  |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_eager_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pidigits       | 284 ms                                                 | 284 ms: 1.00x slower                                                          |
| float          | 55.8 ms                                                | 59.4 ms: 1.06x slower                                                         |
| nbody          | 73.6 ms                                                | 89.0 ms: 1.21x slower                                                         |
| Geometric mean | (ref)                                                  | 1.09x slower                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.18 ms: 1.21x faster                                                         |
| regex_dna      | 149 ms                                                 | 138 ms: 1.08x faster                                                          |
| regex_v8       | 17.0 ms                                                | 15.8 ms: 1.07x faster                                                         |
| regex_compile  | 78.3 ms                                                | 84.4 ms: 1.08x slower                                                         |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.49 sec: 1.05x faster                                                        |
| xml_etree_iterparse  | 74.2 ms                                                | 76.8 ms: 1.03x slower                                                         |
| unpickle_pure_python | 165 us                                                 | 179 us: 1.08x slower                                                          |
| json_loads           | 17.0 us                                                | 18.5 us: 1.09x slower                                                         |
| xml_etree_generate   | 57.1 ms                                                | 62.9 ms: 1.10x slower                                                         |
| xml_etree_process    | 41.3 ms                                                | 46.2 ms: 1.12x slower                                                         |
| pickle_pure_python   | 215 us                                                 | 244 us: 1.14x slower                                                          |
| json_dumps           | 6.47 ms                                                | 7.38 ms: 1.14x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.07x slower                                                                  |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 13.7 ms                                                | 14.3 ms: 1.04x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                  |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 18.4 ms: 1.09x slower                                                         |
| genshi_xml      | 34.1 ms                                                | 37.6 ms: 1.10x slower                                                         |
| mako            | 7.75 ms                                                | 8.74 ms: 1.13x slower                                                         |
| django_template | 20.5 ms                                                | 26.2 ms: 1.28x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.15x slower                                                                  |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 879 ms: 1.70x faster                                                          |
| async_tree_memoization_tg        | 288 ms                                                 | 217 ms: 1.33x faster                                                          |
| deepcopy                         | 236 us                                                 | 185 us: 1.27x faster                                                          |
| async_tree_eager_io              | 511 ms                                                 | 409 ms: 1.25x faster                                                          |
| deepcopy_memo                    | 27.4 us                                                | 22.5 us: 1.22x faster                                                         |
| regex_effbot                     | 2.63 ms                                                | 2.18 ms: 1.21x faster                                                         |
| async_tree_memoization           | 268 ms                                                 | 222 ms: 1.21x faster                                                          |
| async_tree_io                    | 508 ms                                                 | 426 ms: 1.19x faster                                                          |
| async_tree_io_tg                 | 500 ms                                                 | 421 ms: 1.19x faster                                                          |
| go                               | 117 ms                                                 | 100 ms: 1.17x faster                                                          |
| scimark_sor                      | 106 ms                                                 | 91.3 ms: 1.16x faster                                                         |
| async_tree_eager_io_tg           | 479 ms                                                 | 416 ms: 1.15x faster                                                          |
| async_tree_none                  | 212 ms                                                 | 188 ms: 1.13x faster                                                          |
| async_tree_none_tg               | 198 ms                                                 | 176 ms: 1.12x faster                                                          |
| async_tree_eager_memoization     | 168 ms                                                 | 154 ms: 1.09x faster                                                          |
| regex_dna                        | 149 ms                                                 | 138 ms: 1.08x faster                                                          |
| regex_v8                         | 17.0 ms                                                | 15.8 ms: 1.07x faster                                                         |
| dulwich_log                      | 28.7 ms                                                | 27.1 ms: 1.06x faster                                                         |
| deepcopy_reduce                  | 2.09 us                                                | 1.98 us: 1.06x faster                                                         |
| html5lib                         | 36.7 ms                                                | 34.8 ms: 1.05x faster                                                         |
| tomli_loads                      | 1.57 sec                                               | 1.49 sec: 1.05x faster                                                        |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 429 ms: 1.04x faster                                                          |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 442 ms: 1.04x faster                                                          |
| k_core                           | 1.61 sec                                               | 1.57 sec: 1.03x faster                                                        |
| generators                       | 31.9 ms                                                | 31.4 ms: 1.02x faster                                                         |
| connected_components             | 319 ms                                                 | 316 ms: 1.01x faster                                                          |
| async_generators                 | 294 ms                                                 | 292 ms: 1.01x faster                                                          |
| shortest_path                    | 345 ms                                                 | 344 ms: 1.00x faster                                                          |
| pidigits                         | 284 ms                                                 | 284 ms: 1.00x slower                                                          |
| coroutines                       | 20.0 ms                                                | 20.3 ms: 1.01x slower                                                         |
| json                             | 3.04 ms                                                | 3.11 ms: 1.02x slower                                                         |
| sympy_integrate                  | 11.3 ms                                                | 11.6 ms: 1.03x slower                                                         |
| richards                         | 36.2 ms                                                | 37.4 ms: 1.03x slower                                                         |
| xml_etree_iterparse              | 74.2 ms                                                | 76.8 ms: 1.03x slower                                                         |
| scimark_monte_carlo              | 50.4 ms                                                | 52.3 ms: 1.04x slower                                                         |
| spectral_norm                    | 76.5 ms                                                | 79.4 ms: 1.04x slower                                                         |
| python_startup_no_site           | 13.7 ms                                                | 14.3 ms: 1.04x slower                                                         |
| pyflate                          | 352 ms                                                 | 369 ms: 1.05x slower                                                          |
| pathlib                          | 23.2 ms                                                | 24.4 ms: 1.05x slower                                                         |
| sphinx                           | 602 ms                                                 | 635 ms: 1.05x slower                                                          |
| pprint_safe_repr                 | 541 ms                                                 | 570 ms: 1.05x slower                                                          |
| deltablue                        | 2.65 ms                                                | 2.79 ms: 1.06x slower                                                         |
| pprint_pformat                   | 1.10 sec                                               | 1.17 sec: 1.06x slower                                                        |
| 2to3                             | 179 ms                                                 | 190 ms: 1.06x slower                                                          |
| hexiom                           | 4.87 ms                                                | 5.18 ms: 1.06x slower                                                         |
| bpe_tokeniser                    | 3.26 sec                                               | 3.47 sec: 1.06x slower                                                        |
| float                            | 55.8 ms                                                | 59.4 ms: 1.06x slower                                                         |
| sqlite_synth                     | 1.55 us                                                | 1.66 us: 1.07x slower                                                         |
| bench_thread_pool                | 503 us                                                 | 539 us: 1.07x slower                                                          |
| telco                            | 4.84 ms                                                | 5.19 ms: 1.07x slower                                                         |
| pycparser                        | 701 ms                                                 | 752 ms: 1.07x slower                                                          |
| richards_super                   | 39.2 ms                                                | 42.2 ms: 1.08x slower                                                         |
| regex_compile                    | 78.3 ms                                                | 84.4 ms: 1.08x slower                                                         |
| unpickle_pure_python             | 165 us                                                 | 179 us: 1.08x slower                                                          |
| thrift                           | 466 us                                                 | 505 us: 1.08x slower                                                          |
| json_loads                       | 17.0 us                                                | 18.5 us: 1.09x slower                                                         |
| docutils                         | 1.44 sec                                               | 1.57 sec: 1.09x slower                                                        |
| genshi_text                      | 16.9 ms                                                | 18.4 ms: 1.09x slower                                                         |
| scimark_fft                      | 200 ms                                                 | 218 ms: 1.09x slower                                                          |
| gc_traversal                     | 2.94 ms                                                | 3.22 ms: 1.10x slower                                                         |
| async_tree_eager                 | 69.9 ms                                                | 77.0 ms: 1.10x slower                                                         |
| xml_etree_generate               | 57.1 ms                                                | 62.9 ms: 1.10x slower                                                         |
| genshi_xml                       | 34.1 ms                                                | 37.6 ms: 1.10x slower                                                         |
| bench_mp_pool                    | 64.7 ms                                                | 71.8 ms: 1.11x slower                                                         |
| sympy_str                        | 146 ms                                                 | 162 ms: 1.11x slower                                                          |
| xml_etree_process                | 41.3 ms                                                | 46.2 ms: 1.12x slower                                                         |
| sympy_expand                     | 248 ms                                                 | 277 ms: 1.12x slower                                                          |
| meteor_contest                   | 74.0 ms                                                | 82.8 ms: 1.12x slower                                                         |
| sympy_sum                        | 75.1 ms                                                | 84.2 ms: 1.12x slower                                                         |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.35 ms: 1.12x slower                                                         |
| mako                             | 7.75 ms                                                | 8.74 ms: 1.13x slower                                                         |
| typing_runtime_protocols         | 101 us                                                 | 114 us: 1.13x slower                                                          |
| crypto_pyaes                     | 55.3 ms                                                | 62.7 ms: 1.13x slower                                                         |
| pickle_pure_python               | 215 us                                                 | 244 us: 1.14x slower                                                          |
| create_gc_cycles                 | 1.19 ms                                                | 1.36 ms: 1.14x slower                                                         |
| json_dumps                       | 6.47 ms                                                | 7.38 ms: 1.14x slower                                                         |
| raytrace                         | 181 ms                                                 | 207 ms: 1.14x slower                                                          |
| fannkuch                         | 279 ms                                                 | 320 ms: 1.15x slower                                                          |
| chaos                            | 41.1 ms                                                | 47.1 ms: 1.15x slower                                                         |
| coverage                         | 46.2 ms                                                | 54.0 ms: 1.17x slower                                                         |
| scimark_lu                       | 75.9 ms                                                | 88.6 ms: 1.17x slower                                                         |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 405 ms: 1.17x slower                                                          |
| logging_format                   | 3.85 us                                                | 4.58 us: 1.19x slower                                                         |
| comprehensions                   | 12.0 us                                                | 14.2 us: 1.19x slower                                                         |
| nqueens                          | 61.8 ms                                                | 73.7 ms: 1.19x slower                                                         |
| logging_simple                   | 3.56 us                                                | 4.26 us: 1.20x slower                                                         |
| nbody                            | 73.6 ms                                                | 89.0 ms: 1.21x slower                                                         |
| many_optionals                   | 409 us                                                 | 508 us: 1.24x slower                                                          |
| django_template                  | 20.5 ms                                                | 26.2 ms: 1.28x slower                                                         |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 189 ms: 1.37x slower                                                          |
| subparsers                       | 9.44 ms                                                | 15.4 ms: 1.63x slower                                                         |
| async_tree_eager_tg              | 47.4 ms                                                | 146 ms: 3.09x slower                                                          |
| logging_silent                   | 71.0 ns                                                | 359 ns: 5.05x slower                                                          |
| Geometric mean                   | (ref)                                                  | 1.06x slower                                                                  |

Benchmark hidden because not significant (6): pylint, python_startup, dask, asyncio_websockets, async_tree_eager_cpu_io_mixed, xml_etree_parse
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250519-3.15.0a0-4fee8de/bm-20250519-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.044x slower

# HPT report

- Reliability score: 99.42% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.10x