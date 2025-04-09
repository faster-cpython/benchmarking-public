# Results vs. 3.13.0

- fork: faster-cpython
- ref: trashcan_in_dealloc
- machine: darwin-arm64
- commit hash: 8aa20f2
- commit date: 2025-04-09
- overall geometric mean: 1.089x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 161 ms: 1.11x faster                                                            |
| docutils       | 1.44 sec                                               | 1.42 sec: 1.01x faster                                                          |
| html5lib       | 36.7 ms                                                | 29.8 ms: 1.23x faster                                                           |
| sphinx         | 602 ms                                                 | 578 ms: 1.04x faster                                                            |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 190 ms: 1.52x faster                                                            |
| async_tree_eager_io              | 511 ms                                                 | 362 ms: 1.41x faster                                                            |
| async_tree_memoization           | 268 ms                                                 | 191 ms: 1.40x faster                                                            |
| async_tree_io_tg                 | 500 ms                                                 | 360 ms: 1.39x faster                                                            |
| async_tree_io                    | 508 ms                                                 | 379 ms: 1.34x faster                                                            |
| async_tree_none                  | 212 ms                                                 | 162 ms: 1.30x faster                                                            |
| async_tree_none_tg               | 198 ms                                                 | 154 ms: 1.29x faster                                                            |
| async_tree_eager_io_tg           | 479 ms                                                 | 377 ms: 1.27x faster                                                            |
| async_tree_eager_memoization     | 168 ms                                                 | 139 ms: 1.21x faster                                                            |
| coroutines                       | 20.0 ms                                                | 16.6 ms: 1.21x faster                                                           |
| async_tree_eager                 | 69.9 ms                                                | 63.0 ms: 1.11x faster                                                           |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 414 ms: 1.11x faster                                                            |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 411 ms: 1.09x faster                                                            |
| async_generators                 | 294 ms                                                 | 270 ms: 1.09x faster                                                            |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 360 ms: 1.04x faster                                                            |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 392 ms: 1.13x slower                                                            |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 171 ms: 1.24x slower                                                            |
| async_tree_eager_tg              | 47.4 ms                                                | 133 ms: 2.81x slower                                                            |
| Geometric mean                   | (ref)                                                  | 1.11x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 47.1 ms: 1.19x faster                                                           |
| nbody          | 73.6 ms                                                | 71.6 ms: 1.03x faster                                                           |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.24 ms: 1.18x faster                                                           |
| regex_compile  | 78.3 ms                                                | 67.9 ms: 1.15x faster                                                           |
| regex_v8       | 17.0 ms                                                | 15.6 ms: 1.09x faster                                                           |
| regex_dna      | 149 ms                                                 | 141 ms: 1.06x faster                                                            |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.22 sec: 1.28x faster                                                          |
| unpickle_pure_python | 165 us                                                 | 149 us: 1.11x faster                                                            |
| xml_etree_process    | 41.3 ms                                                | 38.5 ms: 1.07x faster                                                           |
| pickle_pure_python   | 215 us                                                 | 206 us: 1.04x faster                                                            |
| xml_etree_generate   | 57.1 ms                                                | 54.8 ms: 1.04x faster                                                           |
| xml_etree_iterparse  | 74.2 ms                                                | 71.8 ms: 1.03x faster                                                           |
| xml_etree_parse      | 108 ms                                                 | 105 ms: 1.03x faster                                                            |
| json_loads           | 17.0 us                                                | 18.2 us: 1.07x slower                                                           |
| json_dumps           | 6.47 ms                                                | 7.65 ms: 1.18x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 16.4 ms: 1.15x faster                                                           |
| python_startup_no_site | 13.7 ms                                                | 12.3 ms: 1.12x faster                                                           |
| Geometric mean         | (ref)                                                  | 1.13x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 13.9 ms: 1.22x faster                                                           |
| genshi_xml      | 34.1 ms                                                | 28.8 ms: 1.18x faster                                                           |
| mako            | 7.75 ms                                                | 7.49 ms: 1.03x faster                                                           |
| django_template | 20.5 ms                                                | 21.1 ms: 1.03x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                                    |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 765 ms: 1.96x faster                                                            |
| deepcopy                         | 236 us                                                 | 155 us: 1.52x faster                                                            |
| async_tree_memoization_tg        | 288 ms                                                 | 190 ms: 1.52x faster                                                            |
| deepcopy_memo                    | 27.4 us                                                | 18.4 us: 1.49x faster                                                           |
| go                               | 117 ms                                                 | 80.1 ms: 1.46x faster                                                           |
| async_tree_eager_io              | 511 ms                                                 | 362 ms: 1.41x faster                                                            |
| async_tree_memoization           | 268 ms                                                 | 191 ms: 1.40x faster                                                            |
| async_tree_io_tg                 | 500 ms                                                 | 360 ms: 1.39x faster                                                            |
| generators                       | 31.9 ms                                                | 23.5 ms: 1.36x faster                                                           |
| async_tree_io                    | 508 ms                                                 | 379 ms: 1.34x faster                                                            |
| scimark_sor                      | 106 ms                                                 | 79.6 ms: 1.33x faster                                                           |
| async_tree_none                  | 212 ms                                                 | 162 ms: 1.30x faster                                                            |
| async_tree_none_tg               | 198 ms                                                 | 154 ms: 1.29x faster                                                            |
| deepcopy_reduce                  | 2.09 us                                                | 1.63 us: 1.28x faster                                                           |
| tomli_loads                      | 1.57 sec                                               | 1.22 sec: 1.28x faster                                                          |
| async_tree_eager_io_tg           | 479 ms                                                 | 377 ms: 1.27x faster                                                            |
| html5lib                         | 36.7 ms                                                | 29.8 ms: 1.23x faster                                                           |
| genshi_text                      | 16.9 ms                                                | 13.9 ms: 1.22x faster                                                           |
| async_tree_eager_memoization     | 168 ms                                                 | 139 ms: 1.21x faster                                                            |
| pyflate                          | 352 ms                                                 | 290 ms: 1.21x faster                                                            |
| coroutines                       | 20.0 ms                                                | 16.6 ms: 1.21x faster                                                           |
| float                            | 55.8 ms                                                | 47.1 ms: 1.19x faster                                                           |
| scimark_monte_carlo              | 50.4 ms                                                | 42.6 ms: 1.18x faster                                                           |
| genshi_xml                       | 34.1 ms                                                | 28.8 ms: 1.18x faster                                                           |
| regex_effbot                     | 2.63 ms                                                | 2.24 ms: 1.18x faster                                                           |
| dulwich_log                      | 28.7 ms                                                | 24.5 ms: 1.17x faster                                                           |
| regex_compile                    | 78.3 ms                                                | 67.9 ms: 1.15x faster                                                           |
| python_startup                   | 18.8 ms                                                | 16.4 ms: 1.15x faster                                                           |
| hexiom                           | 4.87 ms                                                | 4.33 ms: 1.12x faster                                                           |
| deltablue                        | 2.65 ms                                                | 2.36 ms: 1.12x faster                                                           |
| pprint_safe_repr                 | 541 ms                                                 | 482 ms: 1.12x faster                                                            |
| python_startup_no_site           | 13.7 ms                                                | 12.3 ms: 1.12x faster                                                           |
| pprint_pformat                   | 1.10 sec                                               | 987 ms: 1.12x faster                                                            |
| async_tree_eager                 | 69.9 ms                                                | 63.0 ms: 1.11x faster                                                           |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 414 ms: 1.11x faster                                                            |
| 2to3                             | 179 ms                                                 | 161 ms: 1.11x faster                                                            |
| spectral_norm                    | 76.5 ms                                                | 69.0 ms: 1.11x faster                                                           |
| unpickle_pure_python             | 165 us                                                 | 149 us: 1.11x faster                                                            |
| richards                         | 36.2 ms                                                | 32.7 ms: 1.11x faster                                                           |
| pylint                           | 180 ms                                                 | 162 ms: 1.11x faster                                                            |
| regex_v8                         | 17.0 ms                                                | 15.6 ms: 1.09x faster                                                           |
| logging_simple                   | 3.56 us                                                | 3.26 us: 1.09x faster                                                           |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 411 ms: 1.09x faster                                                            |
| bench_mp_pool                    | 64.7 ms                                                | 59.4 ms: 1.09x faster                                                           |
| async_generators                 | 294 ms                                                 | 270 ms: 1.09x faster                                                            |
| scimark_fft                      | 200 ms                                                 | 184 ms: 1.09x faster                                                            |
| richards_super                   | 39.2 ms                                                | 36.2 ms: 1.08x faster                                                           |
| logging_format                   | 3.85 us                                                | 3.58 us: 1.08x faster                                                           |
| chaos                            | 41.1 ms                                                | 38.2 ms: 1.08x faster                                                           |
| xml_etree_process                | 41.3 ms                                                | 38.5 ms: 1.07x faster                                                           |
| pycparser                        | 701 ms                                                 | 655 ms: 1.07x faster                                                            |
| bpe_tokeniser                    | 3.26 sec                                               | 3.05 sec: 1.07x faster                                                          |
| typing_runtime_protocols         | 101 us                                                 | 94.2 us: 1.07x faster                                                           |
| fannkuch                         | 279 ms                                                 | 263 ms: 1.06x faster                                                            |
| regex_dna                        | 149 ms                                                 | 141 ms: 1.06x faster                                                            |
| logging_silent                   | 71.0 ns                                                | 67.2 ns: 1.06x faster                                                           |
| k_core                           | 1.61 sec                                               | 1.53 sec: 1.05x faster                                                          |
| connected_components             | 319 ms                                                 | 303 ms: 1.05x faster                                                            |
| telco                            | 4.84 ms                                                | 4.62 ms: 1.05x faster                                                           |
| shortest_path                    | 345 ms                                                 | 330 ms: 1.05x faster                                                            |
| sympy_integrate                  | 11.3 ms                                                | 10.8 ms: 1.04x faster                                                           |
| pickle_pure_python               | 215 us                                                 | 206 us: 1.04x faster                                                            |
| xml_etree_generate               | 57.1 ms                                                | 54.8 ms: 1.04x faster                                                           |
| nqueens                          | 61.8 ms                                                | 59.4 ms: 1.04x faster                                                           |
| sympy_expand                     | 248 ms                                                 | 238 ms: 1.04x faster                                                            |
| sphinx                           | 602 ms                                                 | 578 ms: 1.04x faster                                                            |
| raytrace                         | 181 ms                                                 | 174 ms: 1.04x faster                                                            |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 360 ms: 1.04x faster                                                            |
| comprehensions                   | 12.0 us                                                | 11.5 us: 1.04x faster                                                           |
| mako                             | 7.75 ms                                                | 7.49 ms: 1.03x faster                                                           |
| xml_etree_iterparse              | 74.2 ms                                                | 71.8 ms: 1.03x faster                                                           |
| sympy_str                        | 146 ms                                                 | 141 ms: 1.03x faster                                                            |
| xml_etree_parse                  | 108 ms                                                 | 105 ms: 1.03x faster                                                            |
| nbody                            | 73.6 ms                                                | 71.6 ms: 1.03x faster                                                           |
| meteor_contest                   | 74.0 ms                                                | 72.2 ms: 1.02x faster                                                           |
| bench_thread_pool                | 503 us                                                 | 494 us: 1.02x faster                                                            |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.58 ms: 1.02x faster                                                           |
| scimark_lu                       | 75.9 ms                                                | 74.9 ms: 1.01x faster                                                           |
| docutils                         | 1.44 sec                                               | 1.42 sec: 1.01x faster                                                          |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                                            |
| sqlalchemy_declarative           | 59.0 ms                                                | 59.4 ms: 1.01x slower                                                           |
| sympy_sum                        | 75.1 ms                                                | 75.6 ms: 1.01x slower                                                           |
| json                             | 3.04 ms                                                | 3.08 ms: 1.01x slower                                                           |
| django_template                  | 20.5 ms                                                | 21.1 ms: 1.03x slower                                                           |
| pathlib                          | 23.2 ms                                                | 24.0 ms: 1.04x slower                                                           |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.14 ms: 1.05x slower                                                           |
| json_loads                       | 17.0 us                                                | 18.2 us: 1.07x slower                                                           |
| gc_traversal                     | 2.94 ms                                                | 3.13 ms: 1.07x slower                                                           |
| create_gc_cycles                 | 1.19 ms                                                | 1.29 ms: 1.08x slower                                                           |
| many_optionals                   | 409 us                                                 | 447 us: 1.09x slower                                                            |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 392 ms: 1.13x slower                                                            |
| json_dumps                       | 6.47 ms                                                | 7.65 ms: 1.18x slower                                                           |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 171 ms: 1.24x slower                                                            |
| subparsers                       | 9.44 ms                                                | 12.3 ms: 1.30x slower                                                           |
| async_tree_eager_tg              | 47.4 ms                                                | 133 ms: 2.81x slower                                                            |
| Geometric mean                   | (ref)                                                  | 1.09x faster                                                                    |

Benchmark hidden because not significant (4): asyncio_websockets, crypto_pyaes, sqlite_synth, coverage
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250409-3.14.0a7+-8aa20f2/bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.089x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.08x