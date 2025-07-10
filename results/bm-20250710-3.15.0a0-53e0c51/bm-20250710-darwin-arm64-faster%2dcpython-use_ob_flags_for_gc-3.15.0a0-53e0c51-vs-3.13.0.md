# Results vs. 3.13.0

- fork: faster-cpython
- ref: use_ob_flags_for_gc
- machine: darwin-arm64
- commit hash: 53e0c51
- commit date: 2025-07-10
- overall geometric mean: 1.015x slower
- HPT reliability: 79.50%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250710-darwin-arm64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-53e0c51 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 188 ms: 1.05x slower                                                           |
| docutils       | 1.44 sec                                               | 1.52 sec: 1.05x slower                                                         |
| html5lib       | 36.7 ms                                                | 34.4 ms: 1.06x faster                                                          |
| sphinx         | 602 ms                                                 | 620 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250710-darwin-arm64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-53e0c51 |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 205 ms: 1.40x faster                                                           |
| async_tree_eager_io              | 511 ms                                                 | 389 ms: 1.31x faster                                                           |
| async_tree_io                    | 508 ms                                                 | 404 ms: 1.26x faster                                                           |
| async_tree_memoization           | 268 ms                                                 | 214 ms: 1.25x faster                                                           |
| async_tree_io_tg                 | 500 ms                                                 | 407 ms: 1.23x faster                                                           |
| async_tree_eager_io_tg           | 479 ms                                                 | 394 ms: 1.21x faster                                                           |
| async_tree_none                  | 212 ms                                                 | 180 ms: 1.17x faster                                                           |
| async_tree_none_tg               | 198 ms                                                 | 172 ms: 1.16x faster                                                           |
| async_tree_eager_memoization     | 168 ms                                                 | 150 ms: 1.12x faster                                                           |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 421 ms: 1.06x faster                                                           |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 432 ms: 1.06x faster                                                           |
| async_generators                 | 294 ms                                                 | 278 ms: 1.05x faster                                                           |
| coroutines                       | 20.0 ms                                                | 19.1 ms: 1.05x faster                                                          |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 368 ms: 1.01x faster                                                           |
| async_tree_eager                 | 69.9 ms                                                | 73.5 ms: 1.05x slower                                                          |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 398 ms: 1.15x slower                                                           |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 181 ms: 1.31x slower                                                           |
| async_tree_eager_tg              | 47.4 ms                                                | 142 ms: 3.01x slower                                                           |
| Geometric mean                   | (ref)                                                  | 1.03x faster                                                                   |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250710-darwin-arm64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-53e0c51 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 284 ms                                                 | 286 ms: 1.01x slower                                                           |
| float          | 55.8 ms                                                | 59.9 ms: 1.07x slower                                                          |
| nbody          | 73.6 ms                                                | 86.6 ms: 1.18x slower                                                          |
| Geometric mean | (ref)                                                  | 1.08x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250710-darwin-arm64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-53e0c51 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.36 ms: 1.11x faster                                                          |
| regex_v8       | 17.0 ms                                                | 16.3 ms: 1.04x faster                                                          |
| regex_dna      | 149 ms                                                 | 144 ms: 1.03x faster                                                           |
| regex_compile  | 78.3 ms                                                | 82.2 ms: 1.05x slower                                                          |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250710-darwin-arm64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-53e0c51 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 98.7 ms: 1.09x faster                                                          |
| tomli_loads          | 1.57 sec                                               | 1.45 sec: 1.08x faster                                                         |
| json_loads           | 17.0 us                                                | 16.7 us: 1.02x faster                                                          |
| xml_etree_iterparse  | 74.2 ms                                                | 73.5 ms: 1.01x faster                                                          |
| xml_etree_generate   | 57.1 ms                                                | 58.9 ms: 1.03x slower                                                          |
| xml_etree_process    | 41.3 ms                                                | 43.9 ms: 1.06x slower                                                          |
| json_dumps           | 6.47 ms                                                | 6.94 ms: 1.07x slower                                                          |
| unpickle_pure_python | 165 us                                                 | 182 us: 1.10x slower                                                           |
| pickle_pure_python   | 215 us                                                 | 243 us: 1.13x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250710-darwin-arm64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-53e0c51 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 16.7 ms: 1.12x faster                                                          |
| python_startup_no_site | 13.7 ms                                                | 12.4 ms: 1.10x faster                                                          |
| Geometric mean         | (ref)                                                  | 1.11x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250710-darwin-arm64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-53e0c51 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 17.9 ms: 1.06x slower                                                          |
| genshi_xml      | 34.1 ms                                                | 36.7 ms: 1.08x slower                                                          |
| mako            | 7.75 ms                                                | 9.16 ms: 1.18x slower                                                          |
| django_template | 20.5 ms                                                | 25.1 ms: 1.23x slower                                                          |
| Geometric mean  | (ref)                                                  | 1.13x slower                                                                   |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250710-darwin-arm64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-53e0c51 |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 836 ms: 1.79x faster                                                           |
| async_tree_memoization_tg        | 288 ms                                                 | 205 ms: 1.40x faster                                                           |
| deepcopy                         | 236 us                                                 | 177 us: 1.34x faster                                                           |
| async_tree_eager_io              | 511 ms                                                 | 389 ms: 1.31x faster                                                           |
| async_tree_io                    | 508 ms                                                 | 404 ms: 1.26x faster                                                           |
| async_tree_memoization           | 268 ms                                                 | 214 ms: 1.25x faster                                                           |
| deepcopy_memo                    | 27.4 us                                                | 22.0 us: 1.24x faster                                                          |
| async_tree_io_tg                 | 500 ms                                                 | 407 ms: 1.23x faster                                                           |
| async_tree_eager_io_tg           | 479 ms                                                 | 394 ms: 1.21x faster                                                           |
| async_tree_none                  | 212 ms                                                 | 180 ms: 1.17x faster                                                           |
| go                               | 117 ms                                                 | 100 ms: 1.17x faster                                                           |
| async_tree_none_tg               | 198 ms                                                 | 172 ms: 1.16x faster                                                           |
| scimark_sor                      | 106 ms                                                 | 92.2 ms: 1.15x faster                                                          |
| python_startup                   | 18.8 ms                                                | 16.7 ms: 1.12x faster                                                          |
| async_tree_eager_memoization     | 168 ms                                                 | 150 ms: 1.12x faster                                                           |
| regex_effbot                     | 2.63 ms                                                | 2.36 ms: 1.11x faster                                                          |
| python_startup_no_site           | 13.7 ms                                                | 12.4 ms: 1.10x faster                                                          |
| deepcopy_reduce                  | 2.09 us                                                | 1.90 us: 1.10x faster                                                          |
| k_core                           | 1.61 sec                                               | 1.47 sec: 1.09x faster                                                         |
| xml_etree_parse                  | 108 ms                                                 | 98.7 ms: 1.09x faster                                                          |
| tomli_loads                      | 1.57 sec                                               | 1.45 sec: 1.08x faster                                                         |
| pylint                           | 180 ms                                                 | 169 ms: 1.07x faster                                                           |
| html5lib                         | 36.7 ms                                                | 34.4 ms: 1.06x faster                                                          |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 421 ms: 1.06x faster                                                           |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 432 ms: 1.06x faster                                                           |
| async_generators                 | 294 ms                                                 | 278 ms: 1.05x faster                                                           |
| coroutines                       | 20.0 ms                                                | 19.1 ms: 1.05x faster                                                          |
| shortest_path                    | 345 ms                                                 | 331 ms: 1.04x faster                                                           |
| spectral_norm                    | 76.5 ms                                                | 73.3 ms: 1.04x faster                                                          |
| regex_v8                         | 17.0 ms                                                | 16.3 ms: 1.04x faster                                                          |
| pyflate                          | 352 ms                                                 | 338 ms: 1.04x faster                                                           |
| connected_components             | 319 ms                                                 | 307 ms: 1.04x faster                                                           |
| regex_dna                        | 149 ms                                                 | 144 ms: 1.03x faster                                                           |
| json                             | 3.04 ms                                                | 2.98 ms: 1.02x faster                                                          |
| json_loads                       | 17.0 us                                                | 16.7 us: 1.02x faster                                                          |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 368 ms: 1.01x faster                                                           |
| xml_etree_iterparse              | 74.2 ms                                                | 73.5 ms: 1.01x faster                                                          |
| bpe_tokeniser                    | 3.26 sec                                               | 3.28 sec: 1.01x slower                                                         |
| pidigits                         | 284 ms                                                 | 286 ms: 1.01x slower                                                           |
| telco                            | 4.84 ms                                                | 4.89 ms: 1.01x slower                                                          |
| meteor_contest                   | 74.0 ms                                                | 74.9 ms: 1.01x slower                                                          |
| sympy_integrate                  | 11.3 ms                                                | 11.5 ms: 1.02x slower                                                          |
| thrift                           | 466 us                                                 | 478 us: 1.03x slower                                                           |
| scimark_fft                      | 200 ms                                                 | 205 ms: 1.03x slower                                                           |
| sphinx                           | 602 ms                                                 | 620 ms: 1.03x slower                                                           |
| xml_etree_generate               | 57.1 ms                                                | 58.9 ms: 1.03x slower                                                          |
| dulwich_log                      | 28.7 ms                                                | 29.7 ms: 1.03x slower                                                          |
| richards                         | 36.2 ms                                                | 37.8 ms: 1.04x slower                                                          |
| hexiom                           | 4.87 ms                                                | 5.10 ms: 1.05x slower                                                          |
| regex_compile                    | 78.3 ms                                                | 82.2 ms: 1.05x slower                                                          |
| docutils                         | 1.44 sec                                               | 1.52 sec: 1.05x slower                                                         |
| async_tree_eager                 | 69.9 ms                                                | 73.5 ms: 1.05x slower                                                          |
| 2to3                             | 179 ms                                                 | 188 ms: 1.05x slower                                                           |
| genshi_text                      | 16.9 ms                                                | 17.9 ms: 1.06x slower                                                          |
| gc_traversal                     | 2.94 ms                                                | 3.11 ms: 1.06x slower                                                          |
| scimark_monte_carlo              | 50.4 ms                                                | 53.5 ms: 1.06x slower                                                          |
| xml_etree_process                | 41.3 ms                                                | 43.9 ms: 1.06x slower                                                          |
| deltablue                        | 2.65 ms                                                | 2.81 ms: 1.06x slower                                                          |
| create_gc_cycles                 | 1.19 ms                                                | 1.27 ms: 1.06x slower                                                          |
| sqlite_synth                     | 1.55 us                                                | 1.65 us: 1.06x slower                                                          |
| typing_runtime_protocols         | 101 us                                                 | 107 us: 1.07x slower                                                           |
| pycparser                        | 701 ms                                                 | 748 ms: 1.07x slower                                                           |
| json_dumps                       | 6.47 ms                                                | 6.94 ms: 1.07x slower                                                          |
| float                            | 55.8 ms                                                | 59.9 ms: 1.07x slower                                                          |
| coverage                         | 46.2 ms                                                | 49.6 ms: 1.07x slower                                                          |
| logging_format                   | 3.85 us                                                | 4.14 us: 1.07x slower                                                          |
| genshi_xml                       | 34.1 ms                                                | 36.7 ms: 1.08x slower                                                          |
| logging_simple                   | 3.56 us                                                | 3.84 us: 1.08x slower                                                          |
| sympy_expand                     | 248 ms                                                 | 267 ms: 1.08x slower                                                           |
| sympy_str                        | 146 ms                                                 | 158 ms: 1.09x slower                                                           |
| logging_silent                   | 71.0 ns                                                | 77.7 ns: 1.09x slower                                                          |
| sympy_sum                        | 75.1 ms                                                | 82.3 ms: 1.10x slower                                                          |
| pprint_pformat                   | 1.10 sec                                               | 1.21 sec: 1.10x slower                                                         |
| pprint_safe_repr                 | 541 ms                                                 | 594 ms: 1.10x slower                                                           |
| crypto_pyaes                     | 55.3 ms                                                | 60.8 ms: 1.10x slower                                                          |
| unpickle_pure_python             | 165 us                                                 | 182 us: 1.10x slower                                                           |
| richards_super                   | 39.2 ms                                                | 43.4 ms: 1.11x slower                                                          |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.31 ms: 1.11x slower                                                          |
| comprehensions                   | 12.0 us                                                | 13.3 us: 1.11x slower                                                          |
| scimark_lu                       | 75.9 ms                                                | 85.3 ms: 1.12x slower                                                          |
| pickle_pure_python               | 215 us                                                 | 243 us: 1.13x slower                                                           |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 398 ms: 1.15x slower                                                           |
| chaos                            | 41.1 ms                                                | 47.6 ms: 1.16x slower                                                          |
| nqueens                          | 61.8 ms                                                | 71.6 ms: 1.16x slower                                                          |
| fannkuch                         | 279 ms                                                 | 327 ms: 1.17x slower                                                           |
| nbody                            | 73.6 ms                                                | 86.6 ms: 1.18x slower                                                          |
| mako                             | 7.75 ms                                                | 9.16 ms: 1.18x slower                                                          |
| raytrace                         | 181 ms                                                 | 215 ms: 1.19x slower                                                           |
| many_optionals                   | 409 us                                                 | 500 us: 1.22x slower                                                           |
| django_template                  | 20.5 ms                                                | 25.1 ms: 1.23x slower                                                          |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 181 ms: 1.31x slower                                                           |
| subparsers                       | 9.44 ms                                                | 14.9 ms: 1.57x slower                                                          |
| async_tree_eager_tg              | 47.4 ms                                                | 142 ms: 3.01x slower                                                           |
| Geometric mean                   | (ref)                                                  | 1.02x slower                                                                   |

Benchmark hidden because not significant (4): dask, generators, asyncio_websockets, pathlib
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250710-3.15.0a0-53e0c51/bm-20250710-darwin-arm64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-53e0c51.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.015x slower

# HPT report

- Reliability score: 79.50% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.11x