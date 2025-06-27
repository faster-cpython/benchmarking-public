# Results vs. 3.13.0

- fork: faster-cpython
- ref: never_inline_decref
- machine: darwin-arm64
- commit hash: 2ab3a06
- commit date: 2025-06-27
- overall geometric mean: 1.022x slower
- HPT reliability: 95.11%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-darwin-arm64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 191 ms: 1.07x slower                                                           |
| docutils       | 1.44 sec                                               | 1.53 sec: 1.06x slower                                                         |
| sphinx         | 602 ms                                                 | 617 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                   |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-darwin-arm64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 209 ms: 1.38x faster                                                           |
| async_tree_eager_io              | 511 ms                                                 | 393 ms: 1.30x faster                                                           |
| async_tree_io                    | 508 ms                                                 | 412 ms: 1.23x faster                                                           |
| async_tree_memoization           | 268 ms                                                 | 218 ms: 1.23x faster                                                           |
| async_tree_io_tg                 | 500 ms                                                 | 408 ms: 1.23x faster                                                           |
| async_tree_eager_io_tg           | 479 ms                                                 | 404 ms: 1.19x faster                                                           |
| async_tree_none                  | 212 ms                                                 | 180 ms: 1.18x faster                                                           |
| async_tree_none_tg               | 198 ms                                                 | 173 ms: 1.15x faster                                                           |
| async_tree_eager_memoization     | 168 ms                                                 | 152 ms: 1.11x faster                                                           |
| coroutines                       | 20.0 ms                                                | 19.0 ms: 1.06x faster                                                          |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 425 ms: 1.05x faster                                                           |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 438 ms: 1.05x faster                                                           |
| async_generators                 | 294 ms                                                 | 285 ms: 1.03x faster                                                           |
| async_tree_eager                 | 69.9 ms                                                | 73.7 ms: 1.05x slower                                                          |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 403 ms: 1.16x slower                                                           |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 183 ms: 1.32x slower                                                           |
| async_tree_eager_tg              | 47.4 ms                                                | 144 ms: 3.04x slower                                                           |
| Geometric mean                   | (ref)                                                  | 1.02x faster                                                                   |

Benchmark hidden because not significant (2): async_tree_eager_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-darwin-arm64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 58.2 ms: 1.04x slower                                                          |
| nbody          | 73.6 ms                                                | 85.4 ms: 1.16x slower                                                          |
| Geometric mean | (ref)                                                  | 1.07x slower                                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-darwin-arm64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.35 ms: 1.12x faster                                                          |
| regex_dna      | 149 ms                                                 | 139 ms: 1.07x faster                                                           |
| regex_v8       | 17.0 ms                                                | 15.9 ms: 1.07x faster                                                          |
| regex_compile  | 78.3 ms                                                | 81.8 ms: 1.04x slower                                                          |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-darwin-arm64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.45 sec: 1.08x faster                                                         |
| xml_etree_parse      | 108 ms                                                 | 110 ms: 1.02x slower                                                           |
| xml_etree_iterparse  | 74.2 ms                                                | 76.2 ms: 1.03x slower                                                          |
| unpickle_pure_python | 165 us                                                 | 177 us: 1.07x slower                                                           |
| xml_etree_generate   | 57.1 ms                                                | 62.1 ms: 1.09x slower                                                          |
| xml_etree_process    | 41.3 ms                                                | 45.3 ms: 1.10x slower                                                          |
| json_dumps           | 6.47 ms                                                | 7.12 ms: 1.10x slower                                                          |
| pickle_pure_python   | 215 us                                                 | 241 us: 1.12x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.05x slower                                                                   |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-darwin-arm64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 18.1 ms: 1.04x faster                                                          |
| python_startup_no_site | 13.7 ms                                                | 13.6 ms: 1.01x faster                                                          |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-darwin-arm64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 34.1 ms                                                | 37.5 ms: 1.10x slower                                                          |
| genshi_text     | 16.9 ms                                                | 18.8 ms: 1.11x slower                                                          |
| mako            | 7.75 ms                                                | 9.21 ms: 1.19x slower                                                          |
| django_template | 20.5 ms                                                | 25.0 ms: 1.22x slower                                                          |
| Geometric mean  | (ref)                                                  | 1.15x slower                                                                   |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-darwin-arm64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 848 ms: 1.77x faster                                                           |
| async_tree_memoization_tg        | 288 ms                                                 | 209 ms: 1.38x faster                                                           |
| async_tree_eager_io              | 511 ms                                                 | 393 ms: 1.30x faster                                                           |
| deepcopy                         | 236 us                                                 | 187 us: 1.27x faster                                                           |
| async_tree_io                    | 508 ms                                                 | 412 ms: 1.23x faster                                                           |
| async_tree_memoization           | 268 ms                                                 | 218 ms: 1.23x faster                                                           |
| async_tree_io_tg                 | 500 ms                                                 | 408 ms: 1.23x faster                                                           |
| deepcopy_memo                    | 27.4 us                                                | 22.8 us: 1.20x faster                                                          |
| async_tree_eager_io_tg           | 479 ms                                                 | 404 ms: 1.19x faster                                                           |
| async_tree_none                  | 212 ms                                                 | 180 ms: 1.18x faster                                                           |
| scimark_sor                      | 106 ms                                                 | 90.3 ms: 1.17x faster                                                          |
| async_tree_none_tg               | 198 ms                                                 | 173 ms: 1.15x faster                                                           |
| regex_effbot                     | 2.63 ms                                                | 2.35 ms: 1.12x faster                                                          |
| async_tree_eager_memoization     | 168 ms                                                 | 152 ms: 1.11x faster                                                           |
| go                               | 117 ms                                                 | 106 ms: 1.11x faster                                                           |
| deepcopy_reduce                  | 2.09 us                                                | 1.92 us: 1.09x faster                                                          |
| k_core                           | 1.61 sec                                               | 1.48 sec: 1.09x faster                                                         |
| tomli_loads                      | 1.57 sec                                               | 1.45 sec: 1.08x faster                                                         |
| dulwich_log                      | 28.7 ms                                                | 26.6 ms: 1.08x faster                                                          |
| regex_dna                        | 149 ms                                                 | 139 ms: 1.07x faster                                                           |
| regex_v8                         | 17.0 ms                                                | 15.9 ms: 1.07x faster                                                          |
| pylint                           | 180 ms                                                 | 168 ms: 1.07x faster                                                           |
| coroutines                       | 20.0 ms                                                | 19.0 ms: 1.06x faster                                                          |
| connected_components             | 319 ms                                                 | 302 ms: 1.06x faster                                                           |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 425 ms: 1.05x faster                                                           |
| spectral_norm                    | 76.5 ms                                                | 72.7 ms: 1.05x faster                                                          |
| shortest_path                    | 345 ms                                                 | 329 ms: 1.05x faster                                                           |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 438 ms: 1.05x faster                                                           |
| python_startup                   | 18.8 ms                                                | 18.1 ms: 1.04x faster                                                          |
| async_generators                 | 294 ms                                                 | 285 ms: 1.03x faster                                                           |
| json                             | 3.04 ms                                                | 2.99 ms: 1.02x faster                                                          |
| python_startup_no_site           | 13.7 ms                                                | 13.6 ms: 1.01x faster                                                          |
| generators                       | 31.9 ms                                                | 31.7 ms: 1.01x faster                                                          |
| dask                             | 771 ms                                                 | 768 ms: 1.00x faster                                                           |
| sympy_integrate                  | 11.3 ms                                                | 11.3 ms: 1.00x slower                                                          |
| thrift                           | 466 us                                                 | 470 us: 1.01x slower                                                           |
| scimark_fft                      | 200 ms                                                 | 202 ms: 1.01x slower                                                           |
| bpe_tokeniser                    | 3.26 sec                                               | 3.30 sec: 1.01x slower                                                         |
| pyflate                          | 352 ms                                                 | 357 ms: 1.01x slower                                                           |
| xml_etree_parse                  | 108 ms                                                 | 110 ms: 1.02x slower                                                           |
| sphinx                           | 602 ms                                                 | 617 ms: 1.03x slower                                                           |
| xml_etree_iterparse              | 74.2 ms                                                | 76.2 ms: 1.03x slower                                                          |
| richards                         | 36.2 ms                                                | 37.3 ms: 1.03x slower                                                          |
| pprint_safe_repr                 | 541 ms                                                 | 561 ms: 1.04x slower                                                           |
| pprint_pformat                   | 1.10 sec                                               | 1.14 sec: 1.04x slower                                                         |
| telco                            | 4.84 ms                                                | 5.04 ms: 1.04x slower                                                          |
| sqlite_synth                     | 1.55 us                                                | 1.62 us: 1.04x slower                                                          |
| float                            | 55.8 ms                                                | 58.2 ms: 1.04x slower                                                          |
| meteor_contest                   | 74.0 ms                                                | 77.2 ms: 1.04x slower                                                          |
| regex_compile                    | 78.3 ms                                                | 81.8 ms: 1.04x slower                                                          |
| typing_runtime_protocols         | 101 us                                                 | 105 us: 1.05x slower                                                           |
| scimark_monte_carlo              | 50.4 ms                                                | 53.0 ms: 1.05x slower                                                          |
| async_tree_eager                 | 69.9 ms                                                | 73.7 ms: 1.05x slower                                                          |
| hexiom                           | 4.87 ms                                                | 5.14 ms: 1.06x slower                                                          |
| pycparser                        | 701 ms                                                 | 743 ms: 1.06x slower                                                           |
| deltablue                        | 2.65 ms                                                | 2.81 ms: 1.06x slower                                                          |
| docutils                         | 1.44 sec                                               | 1.53 sec: 1.06x slower                                                         |
| pathlib                          | 23.2 ms                                                | 24.8 ms: 1.07x slower                                                          |
| 2to3                             | 179 ms                                                 | 191 ms: 1.07x slower                                                           |
| logging_format                   | 3.85 us                                                | 4.12 us: 1.07x slower                                                          |
| unpickle_pure_python             | 165 us                                                 | 177 us: 1.07x slower                                                           |
| richards_super                   | 39.2 ms                                                | 42.0 ms: 1.07x slower                                                          |
| logging_simple                   | 3.56 us                                                | 3.82 us: 1.07x slower                                                          |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.20 ms: 1.07x slower                                                          |
| sympy_expand                     | 248 ms                                                 | 266 ms: 1.07x slower                                                           |
| sympy_str                        | 146 ms                                                 | 157 ms: 1.08x slower                                                           |
| gc_traversal                     | 2.94 ms                                                | 3.19 ms: 1.09x slower                                                          |
| xml_etree_generate               | 57.1 ms                                                | 62.1 ms: 1.09x slower                                                          |
| sympy_sum                        | 75.1 ms                                                | 82.1 ms: 1.09x slower                                                          |
| xml_etree_process                | 41.3 ms                                                | 45.3 ms: 1.10x slower                                                          |
| json_dumps                       | 6.47 ms                                                | 7.12 ms: 1.10x slower                                                          |
| genshi_xml                       | 34.1 ms                                                | 37.5 ms: 1.10x slower                                                          |
| crypto_pyaes                     | 55.3 ms                                                | 60.9 ms: 1.10x slower                                                          |
| comprehensions                   | 12.0 us                                                | 13.2 us: 1.11x slower                                                          |
| logging_silent                   | 71.0 ns                                                | 78.7 ns: 1.11x slower                                                          |
| genshi_text                      | 16.9 ms                                                | 18.8 ms: 1.11x slower                                                          |
| chaos                            | 41.1 ms                                                | 45.7 ms: 1.11x slower                                                          |
| pickle_pure_python               | 215 us                                                 | 241 us: 1.12x slower                                                           |
| create_gc_cycles                 | 1.19 ms                                                | 1.35 ms: 1.13x slower                                                          |
| scimark_lu                       | 75.9 ms                                                | 86.5 ms: 1.14x slower                                                          |
| raytrace                         | 181 ms                                                 | 206 ms: 1.14x slower                                                           |
| coverage                         | 46.2 ms                                                | 53.2 ms: 1.15x slower                                                          |
| fannkuch                         | 279 ms                                                 | 321 ms: 1.15x slower                                                           |
| nbody                            | 73.6 ms                                                | 85.4 ms: 1.16x slower                                                          |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 403 ms: 1.16x slower                                                           |
| mako                             | 7.75 ms                                                | 9.21 ms: 1.19x slower                                                          |
| nqueens                          | 61.8 ms                                                | 74.3 ms: 1.20x slower                                                          |
| many_optionals                   | 409 us                                                 | 493 us: 1.21x slower                                                           |
| django_template                  | 20.5 ms                                                | 25.0 ms: 1.22x slower                                                          |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 183 ms: 1.32x slower                                                           |
| subparsers                       | 9.44 ms                                                | 14.8 ms: 1.57x slower                                                          |
| async_tree_eager_tg              | 47.4 ms                                                | 144 ms: 3.04x slower                                                           |
| Geometric mean                   | (ref)                                                  | 1.02x slower                                                                   |

Benchmark hidden because not significant (5): html5lib, async_tree_eager_cpu_io_mixed, asyncio_websockets, pidigits, json_loads
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250627-3.15.0a0-2ab3a06/bm-20250627-darwin-arm64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.022x slower

# HPT report

- Reliability score: 95.11% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.11x