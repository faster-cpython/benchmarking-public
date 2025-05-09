# Results vs. 3.13.0

- fork: faster-cpython
- ref: make_decref_a_call
- machine: darwin-arm64
- commit hash: bdf907f
- commit date: 2025-05-08
- overall geometric mean: 1.041x slower
- HPT reliability: 99.34%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 188 ms: 1.06x slower                                                          |
| docutils       | 1.44 sec                                               | 1.57 sec: 1.09x slower                                                        |
| html5lib       | 36.7 ms                                                | 35.0 ms: 1.05x faster                                                         |
| sphinx         | 602 ms                                                 | 637 ms: 1.06x slower                                                          |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 216 ms: 1.33x faster                                                          |
| async_tree_eager_io              | 511 ms                                                 | 409 ms: 1.25x faster                                                          |
| async_tree_memoization           | 268 ms                                                 | 222 ms: 1.21x faster                                                          |
| async_tree_io_tg                 | 500 ms                                                 | 419 ms: 1.20x faster                                                          |
| async_tree_io                    | 508 ms                                                 | 427 ms: 1.19x faster                                                          |
| async_tree_eager_io_tg           | 479 ms                                                 | 417 ms: 1.15x faster                                                          |
| async_tree_none                  | 212 ms                                                 | 186 ms: 1.14x faster                                                          |
| async_tree_none_tg               | 198 ms                                                 | 176 ms: 1.13x faster                                                          |
| async_tree_eager_memoization     | 168 ms                                                 | 154 ms: 1.09x faster                                                          |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 439 ms: 1.05x faster                                                          |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 429 ms: 1.04x faster                                                          |
| coroutines                       | 20.0 ms                                                | 20.3 ms: 1.01x slower                                                         |
| async_tree_eager                 | 69.9 ms                                                | 76.6 ms: 1.10x slower                                                         |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 405 ms: 1.17x slower                                                          |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 189 ms: 1.37x slower                                                          |
| async_tree_eager_tg              | 47.4 ms                                                | 146 ms: 3.08x slower                                                          |
| Geometric mean                   | (ref)                                                  | 1.00x slower                                                                  |

Benchmark hidden because not significant (3): async_generators, asyncio_websockets, async_tree_eager_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pidigits       | 284 ms                                                 | 284 ms: 1.00x slower                                                          |
| float          | 55.8 ms                                                | 58.8 ms: 1.05x slower                                                         |
| nbody          | 73.6 ms                                                | 91.0 ms: 1.24x slower                                                         |
| Geometric mean | (ref)                                                  | 1.09x slower                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.16 ms: 1.22x faster                                                         |
| regex_dna      | 149 ms                                                 | 137 ms: 1.08x faster                                                          |
| regex_v8       | 17.0 ms                                                | 16.3 ms: 1.05x faster                                                         |
| regex_compile  | 78.3 ms                                                | 84.4 ms: 1.08x slower                                                         |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.49 sec: 1.05x faster                                                        |
| xml_etree_parse      | 108 ms                                                 | 109 ms: 1.01x slower                                                          |
| xml_etree_iterparse  | 74.2 ms                                                | 76.8 ms: 1.03x slower                                                         |
| unpickle_pure_python | 165 us                                                 | 178 us: 1.08x slower                                                          |
| json_loads           | 17.0 us                                                | 18.6 us: 1.09x slower                                                         |
| xml_etree_generate   | 57.1 ms                                                | 62.8 ms: 1.10x slower                                                         |
| xml_etree_process    | 41.3 ms                                                | 46.3 ms: 1.12x slower                                                         |
| pickle_pure_python   | 215 us                                                 | 249 us: 1.16x slower                                                          |
| json_dumps           | 6.47 ms                                                | 8.43 ms: 1.30x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.09x slower                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 13.7 ms                                                | 11.9 ms: 1.16x faster                                                         |
| python_startup         | 18.8 ms                                                | 16.3 ms: 1.15x faster                                                         |
| Geometric mean         | (ref)                                                  | 1.15x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 18.5 ms: 1.09x slower                                                         |
| genshi_xml      | 34.1 ms                                                | 37.6 ms: 1.10x slower                                                         |
| mako            | 7.75 ms                                                | 8.70 ms: 1.12x slower                                                         |
| django_template | 20.5 ms                                                | 26.1 ms: 1.27x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.15x slower                                                                  |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 881 ms: 1.70x faster                                                          |
| async_tree_memoization_tg        | 288 ms                                                 | 216 ms: 1.33x faster                                                          |
| deepcopy                         | 236 us                                                 | 183 us: 1.29x faster                                                          |
| async_tree_eager_io              | 511 ms                                                 | 409 ms: 1.25x faster                                                          |
| deepcopy_memo                    | 27.4 us                                                | 22.5 us: 1.22x faster                                                         |
| regex_effbot                     | 2.63 ms                                                | 2.16 ms: 1.22x faster                                                         |
| async_tree_memoization           | 268 ms                                                 | 222 ms: 1.21x faster                                                          |
| async_tree_io_tg                 | 500 ms                                                 | 419 ms: 1.20x faster                                                          |
| async_tree_io                    | 508 ms                                                 | 427 ms: 1.19x faster                                                          |
| go                               | 117 ms                                                 | 100 ms: 1.17x faster                                                          |
| python_startup_no_site           | 13.7 ms                                                | 11.9 ms: 1.16x faster                                                         |
| python_startup                   | 18.8 ms                                                | 16.3 ms: 1.15x faster                                                         |
| scimark_sor                      | 106 ms                                                 | 91.8 ms: 1.15x faster                                                         |
| async_tree_eager_io_tg           | 479 ms                                                 | 417 ms: 1.15x faster                                                          |
| async_tree_none                  | 212 ms                                                 | 186 ms: 1.14x faster                                                          |
| async_tree_none_tg               | 198 ms                                                 | 176 ms: 1.13x faster                                                          |
| async_tree_eager_memoization     | 168 ms                                                 | 154 ms: 1.09x faster                                                          |
| regex_dna                        | 149 ms                                                 | 137 ms: 1.08x faster                                                          |
| dulwich_log                      | 28.7 ms                                                | 26.9 ms: 1.07x faster                                                         |
| deepcopy_reduce                  | 2.09 us                                                | 1.98 us: 1.06x faster                                                         |
| tomli_loads                      | 1.57 sec                                               | 1.49 sec: 1.05x faster                                                        |
| html5lib                         | 36.7 ms                                                | 35.0 ms: 1.05x faster                                                         |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 439 ms: 1.05x faster                                                          |
| regex_v8                         | 17.0 ms                                                | 16.3 ms: 1.05x faster                                                         |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 429 ms: 1.04x faster                                                          |
| k_core                           | 1.61 sec                                               | 1.57 sec: 1.03x faster                                                        |
| generators                       | 31.9 ms                                                | 31.6 ms: 1.01x faster                                                         |
| connected_components             | 319 ms                                                 | 315 ms: 1.01x faster                                                          |
| pidigits                         | 284 ms                                                 | 284 ms: 1.00x slower                                                          |
| xml_etree_parse                  | 108 ms                                                 | 109 ms: 1.01x slower                                                          |
| coroutines                       | 20.0 ms                                                | 20.3 ms: 1.01x slower                                                         |
| pathlib                          | 23.2 ms                                                | 23.6 ms: 1.02x slower                                                         |
| json                             | 3.04 ms                                                | 3.12 ms: 1.03x slower                                                         |
| sympy_integrate                  | 11.3 ms                                                | 11.7 ms: 1.03x slower                                                         |
| xml_etree_iterparse              | 74.2 ms                                                | 76.8 ms: 1.03x slower                                                         |
| richards                         | 36.2 ms                                                | 37.8 ms: 1.05x slower                                                         |
| pyflate                          | 352 ms                                                 | 369 ms: 1.05x slower                                                          |
| spectral_norm                    | 76.5 ms                                                | 80.1 ms: 1.05x slower                                                         |
| scimark_monte_carlo              | 50.4 ms                                                | 53.0 ms: 1.05x slower                                                         |
| deltablue                        | 2.65 ms                                                | 2.79 ms: 1.05x slower                                                         |
| float                            | 55.8 ms                                                | 58.8 ms: 1.05x slower                                                         |
| 2to3                             | 179 ms                                                 | 188 ms: 1.06x slower                                                          |
| sphinx                           | 602 ms                                                 | 637 ms: 1.06x slower                                                          |
| telco                            | 4.84 ms                                                | 5.12 ms: 1.06x slower                                                         |
| pprint_safe_repr                 | 541 ms                                                 | 573 ms: 1.06x slower                                                          |
| hexiom                           | 4.87 ms                                                | 5.17 ms: 1.06x slower                                                         |
| pprint_pformat                   | 1.10 sec                                               | 1.17 sec: 1.06x slower                                                        |
| bpe_tokeniser                    | 3.26 sec                                               | 3.47 sec: 1.06x slower                                                        |
| sqlite_synth                     | 1.55 us                                                | 1.66 us: 1.07x slower                                                         |
| logging_silent                   | 71.0 ns                                                | 76.2 ns: 1.07x slower                                                         |
| bench_thread_pool                | 503 us                                                 | 542 us: 1.08x slower                                                          |
| regex_compile                    | 78.3 ms                                                | 84.4 ms: 1.08x slower                                                         |
| unpickle_pure_python             | 165 us                                                 | 178 us: 1.08x slower                                                          |
| pycparser                        | 701 ms                                                 | 759 ms: 1.08x slower                                                          |
| docutils                         | 1.44 sec                                               | 1.57 sec: 1.09x slower                                                        |
| json_loads                       | 17.0 us                                                | 18.6 us: 1.09x slower                                                         |
| bench_mp_pool                    | 64.7 ms                                                | 70.6 ms: 1.09x slower                                                         |
| thrift                           | 466 us                                                 | 509 us: 1.09x slower                                                          |
| genshi_text                      | 16.9 ms                                                | 18.5 ms: 1.09x slower                                                         |
| gc_traversal                     | 2.94 ms                                                | 3.21 ms: 1.09x slower                                                         |
| richards_super                   | 39.2 ms                                                | 42.9 ms: 1.09x slower                                                         |
| async_tree_eager                 | 69.9 ms                                                | 76.6 ms: 1.10x slower                                                         |
| scimark_fft                      | 200 ms                                                 | 219 ms: 1.10x slower                                                          |
| xml_etree_generate               | 57.1 ms                                                | 62.8 ms: 1.10x slower                                                         |
| genshi_xml                       | 34.1 ms                                                | 37.6 ms: 1.10x slower                                                         |
| sympy_str                        | 146 ms                                                 | 162 ms: 1.11x slower                                                          |
| meteor_contest                   | 74.0 ms                                                | 82.5 ms: 1.12x slower                                                         |
| xml_etree_process                | 41.3 ms                                                | 46.3 ms: 1.12x slower                                                         |
| sympy_expand                     | 248 ms                                                 | 278 ms: 1.12x slower                                                          |
| mako                             | 7.75 ms                                                | 8.70 ms: 1.12x slower                                                         |
| sympy_sum                        | 75.1 ms                                                | 84.3 ms: 1.12x slower                                                         |
| logging_format                   | 3.85 us                                                | 4.33 us: 1.12x slower                                                         |
| logging_simple                   | 3.56 us                                                | 4.02 us: 1.13x slower                                                         |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.37 ms: 1.13x slower                                                         |
| crypto_pyaes                     | 55.3 ms                                                | 62.6 ms: 1.13x slower                                                         |
| create_gc_cycles                 | 1.19 ms                                                | 1.36 ms: 1.14x slower                                                         |
| typing_runtime_protocols         | 101 us                                                 | 115 us: 1.14x slower                                                          |
| chaos                            | 41.1 ms                                                | 47.1 ms: 1.15x slower                                                         |
| fannkuch                         | 279 ms                                                 | 320 ms: 1.15x slower                                                          |
| raytrace                         | 181 ms                                                 | 208 ms: 1.15x slower                                                          |
| coverage                         | 46.2 ms                                                | 53.5 ms: 1.16x slower                                                         |
| pickle_pure_python               | 215 us                                                 | 249 us: 1.16x slower                                                          |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 405 ms: 1.17x slower                                                          |
| nqueens                          | 61.8 ms                                                | 73.8 ms: 1.19x slower                                                         |
| comprehensions                   | 12.0 us                                                | 14.3 us: 1.19x slower                                                         |
| scimark_lu                       | 75.9 ms                                                | 91.2 ms: 1.20x slower                                                         |
| many_optionals                   | 409 us                                                 | 503 us: 1.23x slower                                                          |
| nbody                            | 73.6 ms                                                | 91.0 ms: 1.24x slower                                                         |
| django_template                  | 20.5 ms                                                | 26.1 ms: 1.27x slower                                                         |
| json_dumps                       | 6.47 ms                                                | 8.43 ms: 1.30x slower                                                         |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 189 ms: 1.37x slower                                                          |
| subparsers                       | 9.44 ms                                                | 14.8 ms: 1.56x slower                                                         |
| async_tree_eager_tg              | 47.4 ms                                                | 146 ms: 3.08x slower                                                          |
| Geometric mean                   | (ref)                                                  | 1.04x slower                                                                  |

Benchmark hidden because not significant (6): pylint, shortest_path, dask, async_generators, asyncio_websockets, async_tree_eager_cpu_io_mixed
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250508-3.15.0a0-bdf907f/bm-20250508-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.041x slower

# HPT report

- Reliability score: 99.34% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.10x