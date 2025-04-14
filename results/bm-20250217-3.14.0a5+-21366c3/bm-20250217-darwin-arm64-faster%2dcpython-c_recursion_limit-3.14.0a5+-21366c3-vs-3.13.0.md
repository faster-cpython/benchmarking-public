# Results vs. 3.13.0

- fork: faster-cpython
- ref: c_recursion_limit
- machine: darwin-arm64
- commit hash: 21366c3
- commit date: 2025-02-17
- overall geometric mean: 1.012x slower
- HPT reliability: 79.44%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250217-darwin-arm64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 205 ms: 1.15x slower                                                          |
| docutils       | 1.44 sec                                               | 1.51 sec: 1.04x slower                                                        |
| html5lib       | 36.7 ms                                                | 32.9 ms: 1.11x faster                                                         |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                  |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250217-darwin-arm64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 215 ms: 1.34x faster                                                          |
| async_tree_eager_io              | 511 ms                                                 | 409 ms: 1.25x faster                                                          |
| async_tree_io_tg                 | 500 ms                                                 | 404 ms: 1.24x faster                                                          |
| async_tree_memoization           | 268 ms                                                 | 221 ms: 1.21x faster                                                          |
| async_tree_io                    | 508 ms                                                 | 424 ms: 1.20x faster                                                          |
| async_tree_eager_io_tg           | 479 ms                                                 | 405 ms: 1.18x faster                                                          |
| async_tree_none                  | 212 ms                                                 | 184 ms: 1.15x faster                                                          |
| async_tree_none_tg               | 198 ms                                                 | 173 ms: 1.15x faster                                                          |
| async_tree_eager_memoization     | 168 ms                                                 | 152 ms: 1.11x faster                                                          |
| async_generators                 | 294 ms                                                 | 269 ms: 1.09x faster                                                          |
| coroutines                       | 20.0 ms                                                | 18.6 ms: 1.08x faster                                                         |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 437 ms: 1.05x faster                                                          |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 431 ms: 1.04x faster                                                          |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 370 ms: 1.01x faster                                                          |
| async_tree_eager                 | 69.9 ms                                                | 74.2 ms: 1.06x slower                                                         |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 404 ms: 1.16x slower                                                          |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 190 ms: 1.38x slower                                                          |
| async_tree_eager_tg              | 47.4 ms                                                | 143 ms: 3.02x slower                                                          |
| Geometric mean                   | (ref)                                                  | 1.01x faster                                                                  |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250217-darwin-arm64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 54.2 ms: 1.03x faster                                                         |
| pidigits       | 284 ms                                                 | 284 ms: 1.00x slower                                                          |
| nbody          | 73.6 ms                                                | 91.9 ms: 1.25x slower                                                         |
| Geometric mean | (ref)                                                  | 1.07x slower                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250217-darwin-arm64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.30 ms: 1.14x faster                                                         |
| regex_dna      | 149 ms                                                 | 141 ms: 1.06x faster                                                          |
| regex_compile  | 78.3 ms                                                | 77.5 ms: 1.01x faster                                                         |
| regex_v8       | 17.0 ms                                                | 16.9 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250217-darwin-arm64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.44 sec: 1.09x faster                                                        |
| xml_etree_parse      | 108 ms                                                 | 102 ms: 1.06x faster                                                          |
| xml_etree_generate   | 57.1 ms                                                | 58.4 ms: 1.02x slower                                                         |
| unpickle_pure_python | 165 us                                                 | 170 us: 1.03x slower                                                          |
| xml_etree_process    | 41.3 ms                                                | 43.0 ms: 1.04x slower                                                         |
| json_loads           | 17.0 us                                                | 17.8 us: 1.05x slower                                                         |
| pickle_pure_python   | 215 us                                                 | 232 us: 1.08x slower                                                          |
| json_dumps           | 6.47 ms                                                | 7.53 ms: 1.16x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.03x slower                                                                  |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250217-darwin-arm64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 18.1 ms: 1.04x faster                                                         |
| python_startup_no_site | 13.7 ms                                                | 13.4 ms: 1.03x faster                                                         |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250217-darwin-arm64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 16.3 ms: 1.04x faster                                                         |
| genshi_xml      | 34.1 ms                                                | 33.8 ms: 1.01x faster                                                         |
| mako            | 7.75 ms                                                | 8.18 ms: 1.06x slower                                                         |
| django_template | 20.5 ms                                                | 24.1 ms: 1.18x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                                  |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250217-darwin-arm64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| deepcopy                         | 236 us                                                 | 167 us: 1.42x faster                                                          |
| async_tree_memoization_tg        | 288 ms                                                 | 215 ms: 1.34x faster                                                          |
| deepcopy_memo                    | 27.4 us                                                | 20.9 us: 1.31x faster                                                         |
| async_tree_eager_io              | 511 ms                                                 | 409 ms: 1.25x faster                                                          |
| async_tree_io_tg                 | 500 ms                                                 | 404 ms: 1.24x faster                                                          |
| go                               | 117 ms                                                 | 94.6 ms: 1.23x faster                                                         |
| async_tree_memoization           | 268 ms                                                 | 221 ms: 1.21x faster                                                          |
| async_tree_io                    | 508 ms                                                 | 424 ms: 1.20x faster                                                          |
| deepcopy_reduce                  | 2.09 us                                                | 1.76 us: 1.19x faster                                                         |
| async_tree_eager_io_tg           | 479 ms                                                 | 405 ms: 1.18x faster                                                          |
| async_tree_none                  | 212 ms                                                 | 184 ms: 1.15x faster                                                          |
| async_tree_none_tg               | 198 ms                                                 | 173 ms: 1.15x faster                                                          |
| regex_effbot                     | 2.63 ms                                                | 2.30 ms: 1.14x faster                                                         |
| scimark_sor                      | 106 ms                                                 | 92.7 ms: 1.14x faster                                                         |
| html5lib                         | 36.7 ms                                                | 32.9 ms: 1.11x faster                                                         |
| async_tree_eager_memoization     | 168 ms                                                 | 152 ms: 1.11x faster                                                          |
| generators                       | 31.9 ms                                                | 29.1 ms: 1.10x faster                                                         |
| async_generators                 | 294 ms                                                 | 269 ms: 1.09x faster                                                          |
| tomli_loads                      | 1.57 sec                                               | 1.44 sec: 1.09x faster                                                        |
| bench_mp_pool                    | 64.7 ms                                                | 59.7 ms: 1.08x faster                                                         |
| coroutines                       | 20.0 ms                                                | 18.6 ms: 1.08x faster                                                         |
| xml_etree_parse                  | 108 ms                                                 | 102 ms: 1.06x faster                                                          |
| pylint                           | 180 ms                                                 | 170 ms: 1.06x faster                                                          |
| regex_dna                        | 149 ms                                                 | 141 ms: 1.06x faster                                                          |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 437 ms: 1.05x faster                                                          |
| k_core                           | 1.61 sec                                               | 1.54 sec: 1.04x faster                                                        |
| genshi_text                      | 16.9 ms                                                | 16.3 ms: 1.04x faster                                                         |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 431 ms: 1.04x faster                                                          |
| python_startup                   | 18.8 ms                                                | 18.1 ms: 1.04x faster                                                         |
| float                            | 55.8 ms                                                | 54.2 ms: 1.03x faster                                                         |
| python_startup_no_site           | 13.7 ms                                                | 13.4 ms: 1.03x faster                                                         |
| bpe_tokeniser                    | 3.26 sec                                               | 3.20 sec: 1.02x faster                                                        |
| json                             | 3.04 ms                                                | 3.00 ms: 1.01x faster                                                         |
| telco                            | 4.84 ms                                                | 4.78 ms: 1.01x faster                                                         |
| regex_compile                    | 78.3 ms                                                | 77.5 ms: 1.01x faster                                                         |
| shortest_path                    | 345 ms                                                 | 343 ms: 1.01x faster                                                          |
| genshi_xml                       | 34.1 ms                                                | 33.8 ms: 1.01x faster                                                         |
| scimark_fft                      | 200 ms                                                 | 198 ms: 1.01x faster                                                          |
| connected_components             | 319 ms                                                 | 316 ms: 1.01x faster                                                          |
| regex_v8                         | 17.0 ms                                                | 16.9 ms: 1.01x faster                                                         |
| sqlite_synth                     | 1.55 us                                                | 1.54 us: 1.01x faster                                                         |
| scimark_monte_carlo              | 50.4 ms                                                | 50.1 ms: 1.01x faster                                                         |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 370 ms: 1.01x faster                                                          |
| pidigits                         | 284 ms                                                 | 284 ms: 1.00x slower                                                          |
| pprint_safe_repr                 | 541 ms                                                 | 542 ms: 1.00x slower                                                          |
| spectral_norm                    | 76.5 ms                                                | 77.9 ms: 1.02x slower                                                         |
| xml_etree_generate               | 57.1 ms                                                | 58.4 ms: 1.02x slower                                                         |
| sqlglot_optimize                 | 34.7 ms                                                | 35.6 ms: 1.03x slower                                                         |
| sympy_expand                     | 248 ms                                                 | 255 ms: 1.03x slower                                                          |
| coverage                         | 46.2 ms                                                | 47.6 ms: 1.03x slower                                                         |
| unpickle_pure_python             | 165 us                                                 | 170 us: 1.03x slower                                                          |
| logging_silent                   | 71.0 ns                                                | 73.4 ns: 1.03x slower                                                         |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.08 ms: 1.03x slower                                                         |
| sqlglot_transpile                | 1.04 ms                                                | 1.08 ms: 1.04x slower                                                         |
| bench_thread_pool                | 503 us                                                 | 522 us: 1.04x slower                                                          |
| mdp                              | 1.50 sec                                               | 1.56 sec: 1.04x slower                                                        |
| xml_etree_process                | 41.3 ms                                                | 43.0 ms: 1.04x slower                                                         |
| sqlglot_parse                    | 852 us                                                 | 888 us: 1.04x slower                                                          |
| deltablue                        | 2.65 ms                                                | 2.76 ms: 1.04x slower                                                         |
| sqlglot_normalize                | 188 ms                                                 | 196 ms: 1.04x slower                                                          |
| docutils                         | 1.44 sec                                               | 1.51 sec: 1.04x slower                                                        |
| dulwich_log                      | 28.7 ms                                                | 30.0 ms: 1.04x slower                                                         |
| json_loads                       | 17.0 us                                                | 17.8 us: 1.05x slower                                                         |
| logging_simple                   | 3.56 us                                                | 3.75 us: 1.05x slower                                                         |
| meteor_contest                   | 74.0 ms                                                | 78.0 ms: 1.05x slower                                                         |
| fannkuch                         | 279 ms                                                 | 294 ms: 1.05x slower                                                          |
| logging_format                   | 3.85 us                                                | 4.07 us: 1.06x slower                                                         |
| mako                             | 7.75 ms                                                | 8.18 ms: 1.06x slower                                                         |
| gc_traversal                     | 2.94 ms                                                | 3.11 ms: 1.06x slower                                                         |
| sympy_str                        | 146 ms                                                 | 154 ms: 1.06x slower                                                          |
| sqlalchemy_declarative           | 59.0 ms                                                | 62.5 ms: 1.06x slower                                                         |
| crypto_pyaes                     | 55.3 ms                                                | 58.6 ms: 1.06x slower                                                         |
| sqlalchemy_imperative            | 6.69 ms                                                | 7.10 ms: 1.06x slower                                                         |
| async_tree_eager                 | 69.9 ms                                                | 74.2 ms: 1.06x slower                                                         |
| nqueens                          | 61.8 ms                                                | 65.7 ms: 1.06x slower                                                         |
| sympy_sum                        | 75.1 ms                                                | 80.1 ms: 1.07x slower                                                         |
| pickle_pure_python               | 215 us                                                 | 232 us: 1.08x slower                                                          |
| create_gc_cycles                 | 1.19 ms                                                | 1.29 ms: 1.08x slower                                                         |
| hexiom                           | 4.87 ms                                                | 5.26 ms: 1.08x slower                                                         |
| chaos                            | 41.1 ms                                                | 44.5 ms: 1.08x slower                                                         |
| sympy_integrate                  | 11.3 ms                                                | 12.3 ms: 1.08x slower                                                         |
| comprehensions                   | 12.0 us                                                | 13.0 us: 1.09x slower                                                         |
| richards_super                   | 39.2 ms                                                | 42.7 ms: 1.09x slower                                                         |
| scimark_lu                       | 75.9 ms                                                | 83.4 ms: 1.10x slower                                                         |
| richards                         | 36.2 ms                                                | 39.8 ms: 1.10x slower                                                         |
| 2to3                             | 179 ms                                                 | 205 ms: 1.15x slower                                                          |
| many_optionals                   | 409 us                                                 | 468 us: 1.15x slower                                                          |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 404 ms: 1.16x slower                                                          |
| json_dumps                       | 6.47 ms                                                | 7.53 ms: 1.16x slower                                                         |
| raytrace                         | 181 ms                                                 | 212 ms: 1.17x slower                                                          |
| django_template                  | 20.5 ms                                                | 24.1 ms: 1.18x slower                                                         |
| nbody                            | 73.6 ms                                                | 91.9 ms: 1.25x slower                                                         |
| subparsers                       | 9.44 ms                                                | 12.9 ms: 1.36x slower                                                         |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 190 ms: 1.38x slower                                                          |
| async_tree_eager_tg              | 47.4 ms                                                | 143 ms: 3.02x slower                                                          |
| Geometric mean                   | (ref)                                                  | 1.01x slower                                                                  |

Benchmark hidden because not significant (9): pyflate, asyncio_websockets, thrift, pathlib, pprint_pformat, pycparser, typing_runtime_protocols, xml_etree_iterparse, sphinx
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.012x slower

# HPT report

- Reliability score: 79.44% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.08x