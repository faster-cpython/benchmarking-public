# Results vs. 3.13.0

- fork: python
- ref: 4f18916c5c28321f363e
- machine: darwin-arm64
- commit hash: 4f18916
- commit date: 2025-04-26
- overall geometric mean: 1.158x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 151 ms: 1.18x faster                                                   |
| docutils       | 1.44 sec                                               | 1.37 sec: 1.05x faster                                                 |
| html5lib       | 36.7 ms                                                | 29.0 ms: 1.26x faster                                                  |
| sphinx         | 602 ms                                                 | 548 ms: 1.10x faster                                                   |
| Geometric mean | (ref)                                                  | 1.15x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 177 ms: 1.63x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 334 ms: 1.53x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 334 ms: 1.52x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 336 ms: 1.49x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 181 ms: 1.48x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 150 ms: 1.41x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 343 ms: 1.40x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 143 ms: 1.39x faster                                                   |
| coroutines                       | 20.0 ms                                                | 14.7 ms: 1.36x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 130 ms: 1.29x faster                                                   |
| async_tree_eager                 | 69.9 ms                                                | 55.8 ms: 1.25x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 397 ms: 1.16x faster                                                   |
| async_generators                 | 294 ms                                                 | 256 ms: 1.15x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 396 ms: 1.13x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 344 ms: 1.08x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 373 ms: 1.08x slower                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 161 ms: 1.17x slower                                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 123 ms: 2.59x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.19x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 42.6 ms: 1.31x faster                                                  |
| nbody          | 73.6 ms                                                | 71.3 ms: 1.03x faster                                                  |
| pidigits       | 284 ms                                                 | 280 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 78.3 ms                                                | 60.4 ms: 1.30x faster                                                  |
| regex_effbot   | 2.63 ms                                                | 2.32 ms: 1.14x faster                                                  |
| regex_v8       | 17.0 ms                                                | 16.3 ms: 1.04x faster                                                  |
| regex_dna      | 149 ms                                                 | 147 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.12x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.17 sec: 1.34x faster                                                 |
| unpickle_pure_python | 165 us                                                 | 127 us: 1.30x faster                                                   |
| xml_etree_process    | 41.3 ms                                                | 34.5 ms: 1.20x faster                                                  |
| xml_etree_generate   | 57.1 ms                                                | 48.6 ms: 1.17x faster                                                  |
| pickle_pure_python   | 215 us                                                 | 185 us: 1.16x faster                                                   |
| xml_etree_iterparse  | 74.2 ms                                                | 70.4 ms: 1.05x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 105 ms: 1.03x faster                                                   |
| json_loads           | 17.0 us                                                | 17.8 us: 1.04x slower                                                  |
| json_dumps           | 6.47 ms                                                | 7.07 ms: 1.09x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 18.7 ms: 1.01x faster                                                  |
| python_startup_no_site | 13.7 ms                                                | 14.6 ms: 1.06x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 12.7 ms: 1.33x faster                                                  |
| genshi_xml      | 34.1 ms                                                | 26.7 ms: 1.27x faster                                                  |
| django_template | 20.5 ms                                                | 19.2 ms: 1.07x faster                                                  |
| mako            | 7.75 ms                                                | 7.28 ms: 1.06x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.18x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 684 ms: 2.19x faster                                                   |
| deepcopy                         | 236 us                                                 | 139 us: 1.70x faster                                                   |
| deepcopy_memo                    | 27.4 us                                                | 16.2 us: 1.69x faster                                                  |
| generators                       | 31.9 ms                                                | 19.1 ms: 1.67x faster                                                  |
| go                               | 117 ms                                                 | 70.7 ms: 1.65x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 177 ms: 1.63x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 334 ms: 1.53x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 334 ms: 1.52x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 336 ms: 1.49x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 181 ms: 1.48x faster                                                   |
| scimark_sor                      | 106 ms                                                 | 73.2 ms: 1.44x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 150 ms: 1.41x faster                                                   |
| deepcopy_reduce                  | 2.09 us                                                | 1.50 us: 1.40x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 343 ms: 1.40x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 143 ms: 1.39x faster                                                   |
| coroutines                       | 20.0 ms                                                | 14.7 ms: 1.36x faster                                                  |
| tomli_loads                      | 1.57 sec                                               | 1.17 sec: 1.34x faster                                                 |
| genshi_text                      | 16.9 ms                                                | 12.7 ms: 1.33x faster                                                  |
| float                            | 55.8 ms                                                | 42.6 ms: 1.31x faster                                                  |
| unpickle_pure_python             | 165 us                                                 | 127 us: 1.30x faster                                                   |
| hexiom                           | 4.87 ms                                                | 3.75 ms: 1.30x faster                                                  |
| deltablue                        | 2.65 ms                                                | 2.04 ms: 1.30x faster                                                  |
| regex_compile                    | 78.3 ms                                                | 60.4 ms: 1.30x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 130 ms: 1.29x faster                                                   |
| pyflate                          | 352 ms                                                 | 275 ms: 1.28x faster                                                   |
| genshi_xml                       | 34.1 ms                                                | 26.7 ms: 1.27x faster                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 39.6 ms: 1.27x faster                                                  |
| html5lib                         | 36.7 ms                                                | 29.0 ms: 1.26x faster                                                  |
| async_tree_eager                 | 69.9 ms                                                | 55.8 ms: 1.25x faster                                                  |
| richards                         | 36.2 ms                                                | 29.3 ms: 1.23x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 23.4 ms: 1.23x faster                                                  |
| logging_silent                   | 71.0 ns                                                | 57.9 ns: 1.23x faster                                                  |
| pylint                           | 180 ms                                                 | 149 ms: 1.21x faster                                                   |
| xml_etree_process                | 41.3 ms                                                | 34.5 ms: 1.20x faster                                                  |
| comprehensions                   | 12.0 us                                                | 10.0 us: 1.19x faster                                                  |
| logging_simple                   | 3.56 us                                                | 3.01 us: 1.18x faster                                                  |
| richards_super                   | 39.2 ms                                                | 33.1 ms: 1.18x faster                                                  |
| 2to3                             | 179 ms                                                 | 151 ms: 1.18x faster                                                   |
| logging_format                   | 3.85 us                                                | 3.27 us: 1.18x faster                                                  |
| pprint_pformat                   | 1.10 sec                                               | 936 ms: 1.18x faster                                                   |
| chaos                            | 41.1 ms                                                | 35.0 ms: 1.18x faster                                                  |
| nqueens                          | 61.8 ms                                                | 52.7 ms: 1.17x faster                                                  |
| xml_etree_generate               | 57.1 ms                                                | 48.6 ms: 1.17x faster                                                  |
| bpe_tokeniser                    | 3.26 sec                                               | 2.78 sec: 1.17x faster                                                 |
| pprint_safe_repr                 | 541 ms                                                 | 462 ms: 1.17x faster                                                   |
| raytrace                         | 181 ms                                                 | 156 ms: 1.16x faster                                                   |
| pickle_pure_python               | 215 us                                                 | 185 us: 1.16x faster                                                   |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 397 ms: 1.16x faster                                                   |
| typing_runtime_protocols         | 101 us                                                 | 87.0 us: 1.16x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 66.3 ms: 1.15x faster                                                  |
| async_generators                 | 294 ms                                                 | 256 ms: 1.15x faster                                                   |
| sympy_expand                     | 248 ms                                                 | 216 ms: 1.15x faster                                                   |
| regex_effbot                     | 2.63 ms                                                | 2.32 ms: 1.14x faster                                                  |
| sympy_integrate                  | 11.3 ms                                                | 9.99 ms: 1.13x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 396 ms: 1.13x faster                                                   |
| sympy_str                        | 146 ms                                                 | 129 ms: 1.13x faster                                                   |
| pycparser                        | 701 ms                                                 | 621 ms: 1.13x faster                                                   |
| crypto_pyaes                     | 55.3 ms                                                | 49.1 ms: 1.13x faster                                                  |
| fannkuch                         | 279 ms                                                 | 249 ms: 1.12x faster                                                   |
| sympy_sum                        | 75.1 ms                                                | 68.3 ms: 1.10x faster                                                  |
| sphinx                           | 602 ms                                                 | 548 ms: 1.10x faster                                                   |
| bench_thread_pool                | 503 us                                                 | 460 us: 1.09x faster                                                   |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.17 ms: 1.09x faster                                                  |
| scimark_lu                       | 75.9 ms                                                | 70.0 ms: 1.08x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 344 ms: 1.08x faster                                                   |
| django_template                  | 20.5 ms                                                | 19.2 ms: 1.07x faster                                                  |
| sqlalchemy_declarative           | 59.0 ms                                                | 55.3 ms: 1.07x faster                                                  |
| telco                            | 4.84 ms                                                | 4.53 ms: 1.07x faster                                                  |
| k_core                           | 1.61 sec                                               | 1.51 sec: 1.07x faster                                                 |
| mako                             | 7.75 ms                                                | 7.28 ms: 1.06x faster                                                  |
| connected_components             | 319 ms                                                 | 300 ms: 1.06x faster                                                   |
| shortest_path                    | 345 ms                                                 | 326 ms: 1.06x faster                                                   |
| xml_etree_iterparse              | 74.2 ms                                                | 70.4 ms: 1.05x faster                                                  |
| docutils                         | 1.44 sec                                               | 1.37 sec: 1.05x faster                                                 |
| meteor_contest                   | 74.0 ms                                                | 70.2 ms: 1.05x faster                                                  |
| regex_v8                         | 17.0 ms                                                | 16.3 ms: 1.04x faster                                                  |
| scimark_fft                      | 200 ms                                                 | 191 ms: 1.04x faster                                                   |
| nbody                            | 73.6 ms                                                | 71.3 ms: 1.03x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 105 ms: 1.03x faster                                                   |
| sqlite_synth                     | 1.55 us                                                | 1.53 us: 1.02x faster                                                  |
| pidigits                         | 284 ms                                                 | 280 ms: 1.01x faster                                                   |
| regex_dna                        | 149 ms                                                 | 147 ms: 1.01x faster                                                   |
| json                             | 3.04 ms                                                | 3.00 ms: 1.01x faster                                                  |
| coverage                         | 46.2 ms                                                | 45.7 ms: 1.01x faster                                                  |
| python_startup                   | 18.8 ms                                                | 18.7 ms: 1.01x faster                                                  |
| many_optionals                   | 409 us                                                 | 418 us: 1.02x slower                                                   |
| json_loads                       | 17.0 us                                                | 17.8 us: 1.04x slower                                                  |
| gc_traversal                     | 2.94 ms                                                | 3.08 ms: 1.05x slower                                                  |
| pathlib                          | 23.2 ms                                                | 24.6 ms: 1.06x slower                                                  |
| python_startup_no_site           | 13.7 ms                                                | 14.6 ms: 1.06x slower                                                  |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.17 ms: 1.06x slower                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 1.27 ms: 1.07x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 373 ms: 1.08x slower                                                   |
| json_dumps                       | 6.47 ms                                                | 7.07 ms: 1.09x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 161 ms: 1.17x slower                                                   |
| subparsers                       | 9.44 ms                                                | 11.4 ms: 1.21x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 123 ms: 2.59x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.16x faster                                                           |

Benchmark hidden because not significant (2): bench_mp_pool, asyncio_websockets
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250426-3.14.0a7+-4f18916-CLANG/bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.158x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: 1.08x