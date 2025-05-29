# Results vs. 3.13.0

- fork: python
- ref: 718d234e4086a65d78c8
- machine: darwin-arm64
- commit hash: 718d234
- commit date: 2025-04-12
- overall geometric mean: 1.160x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7+-718d234 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 153 ms: 1.17x faster                                                   |
| docutils       | 1.44 sec                                               | 1.36 sec: 1.06x faster                                                 |
| html5lib       | 36.7 ms                                                | 29.0 ms: 1.26x faster                                                  |
| sphinx         | 602 ms                                                 | 547 ms: 1.10x faster                                                   |
| Geometric mean | (ref)                                                  | 1.15x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7+-718d234 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 179 ms: 1.61x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 334 ms: 1.52x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 177 ms: 1.52x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 339 ms: 1.51x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 336 ms: 1.49x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 148 ms: 1.43x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 141 ms: 1.40x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 345 ms: 1.39x faster                                                   |
| coroutines                       | 20.0 ms                                                | 15.1 ms: 1.32x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 130 ms: 1.29x faster                                                   |
| async_tree_eager                 | 69.9 ms                                                | 56.2 ms: 1.24x faster                                                  |
| async_generators                 | 294 ms                                                 | 252 ms: 1.16x faster                                                   |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 396 ms: 1.16x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 396 ms: 1.13x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 345 ms: 1.08x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 377 ms: 1.09x slower                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 160 ms: 1.16x slower                                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 121 ms: 2.55x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.18x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7+-718d234 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 42.8 ms: 1.31x faster                                                  |
| nbody          | 73.6 ms                                                | 70.2 ms: 1.05x faster                                                  |
| pidigits       | 284 ms                                                 | 279 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.12x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7+-718d234 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 78.3 ms                                                | 60.8 ms: 1.29x faster                                                  |
| regex_effbot   | 2.63 ms                                                | 2.31 ms: 1.14x faster                                                  |
| regex_dna      | 149 ms                                                 | 143 ms: 1.04x faster                                                   |
| regex_v8       | 17.0 ms                                                | 16.4 ms: 1.04x faster                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7+-718d234 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.15 sec: 1.36x faster                                                 |
| unpickle_pure_python | 165 us                                                 | 128 us: 1.29x faster                                                   |
| xml_etree_process    | 41.3 ms                                                | 34.6 ms: 1.19x faster                                                  |
| xml_etree_generate   | 57.1 ms                                                | 48.5 ms: 1.18x faster                                                  |
| pickle_pure_python   | 215 us                                                 | 186 us: 1.16x faster                                                   |
| xml_etree_iterparse  | 74.2 ms                                                | 70.3 ms: 1.06x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 105 ms: 1.03x faster                                                   |
| json_loads           | 17.0 us                                                | 17.7 us: 1.04x slower                                                  |
| json_dumps           | 6.47 ms                                                | 7.08 ms: 1.09x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7+-718d234 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 18.1 ms: 1.04x faster                                                  |
| python_startup_no_site | 13.7 ms                                                | 14.0 ms: 1.02x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7+-718d234 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 12.8 ms: 1.32x faster                                                  |
| genshi_xml      | 34.1 ms                                                | 26.8 ms: 1.27x faster                                                  |
| mako            | 7.75 ms                                                | 7.18 ms: 1.08x faster                                                  |
| django_template | 20.5 ms                                                | 19.3 ms: 1.06x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.18x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7+-718d234 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 686 ms: 2.19x faster                                                   |
| deepcopy_memo                    | 27.4 us                                                | 15.9 us: 1.72x faster                                                  |
| deepcopy                         | 236 us                                                 | 139 us: 1.70x faster                                                   |
| generators                       | 31.9 ms                                                | 19.2 ms: 1.67x faster                                                  |
| go                               | 117 ms                                                 | 70.7 ms: 1.65x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 179 ms: 1.61x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 334 ms: 1.52x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 177 ms: 1.52x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 339 ms: 1.51x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 336 ms: 1.49x faster                                                   |
| scimark_sor                      | 106 ms                                                 | 73.2 ms: 1.44x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 148 ms: 1.43x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 141 ms: 1.40x faster                                                   |
| deepcopy_reduce                  | 2.09 us                                                | 1.49 us: 1.40x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 345 ms: 1.39x faster                                                   |
| tomli_loads                      | 1.57 sec                                               | 1.15 sec: 1.36x faster                                                 |
| genshi_text                      | 16.9 ms                                                | 12.8 ms: 1.32x faster                                                  |
| coroutines                       | 20.0 ms                                                | 15.1 ms: 1.32x faster                                                  |
| float                            | 55.8 ms                                                | 42.8 ms: 1.31x faster                                                  |
| deltablue                        | 2.65 ms                                                | 2.04 ms: 1.30x faster                                                  |
| hexiom                           | 4.87 ms                                                | 3.76 ms: 1.29x faster                                                  |
| pyflate                          | 352 ms                                                 | 272 ms: 1.29x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 130 ms: 1.29x faster                                                   |
| regex_compile                    | 78.3 ms                                                | 60.8 ms: 1.29x faster                                                  |
| unpickle_pure_python             | 165 us                                                 | 128 us: 1.29x faster                                                   |
| scimark_monte_carlo              | 50.4 ms                                                | 39.4 ms: 1.28x faster                                                  |
| genshi_xml                       | 34.1 ms                                                | 26.8 ms: 1.27x faster                                                  |
| html5lib                         | 36.7 ms                                                | 29.0 ms: 1.26x faster                                                  |
| async_tree_eager                 | 69.9 ms                                                | 56.2 ms: 1.24x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 23.3 ms: 1.23x faster                                                  |
| logging_silent                   | 71.0 ns                                                | 57.8 ns: 1.23x faster                                                  |
| richards                         | 36.2 ms                                                | 29.6 ms: 1.22x faster                                                  |
| logging_simple                   | 3.56 us                                                | 2.97 us: 1.20x faster                                                  |
| pylint                           | 180 ms                                                 | 150 ms: 1.20x faster                                                   |
| xml_etree_process                | 41.3 ms                                                | 34.6 ms: 1.19x faster                                                  |
| comprehensions                   | 12.0 us                                                | 10.0 us: 1.19x faster                                                  |
| richards_super                   | 39.2 ms                                                | 33.1 ms: 1.19x faster                                                  |
| nqueens                          | 61.8 ms                                                | 52.2 ms: 1.19x faster                                                  |
| logging_format                   | 3.85 us                                                | 3.27 us: 1.18x faster                                                  |
| xml_etree_generate               | 57.1 ms                                                | 48.5 ms: 1.18x faster                                                  |
| pprint_pformat                   | 1.10 sec                                               | 935 ms: 1.18x faster                                                   |
| chaos                            | 41.1 ms                                                | 34.9 ms: 1.18x faster                                                  |
| pprint_safe_repr                 | 541 ms                                                 | 461 ms: 1.17x faster                                                   |
| 2to3                             | 179 ms                                                 | 153 ms: 1.17x faster                                                   |
| typing_runtime_protocols         | 101 us                                                 | 86.2 us: 1.17x faster                                                  |
| async_generators                 | 294 ms                                                 | 252 ms: 1.16x faster                                                   |
| raytrace                         | 181 ms                                                 | 156 ms: 1.16x faster                                                   |
| bpe_tokeniser                    | 3.26 sec                                               | 2.81 sec: 1.16x faster                                                 |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 396 ms: 1.16x faster                                                   |
| pickle_pure_python               | 215 us                                                 | 186 us: 1.16x faster                                                   |
| spectral_norm                    | 76.5 ms                                                | 66.5 ms: 1.15x faster                                                  |
| sympy_expand                     | 248 ms                                                 | 217 ms: 1.14x faster                                                   |
| regex_effbot                     | 2.63 ms                                                | 2.31 ms: 1.14x faster                                                  |
| pycparser                        | 701 ms                                                 | 619 ms: 1.13x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 396 ms: 1.13x faster                                                   |
| fannkuch                         | 279 ms                                                 | 247 ms: 1.13x faster                                                   |
| sympy_str                        | 146 ms                                                 | 129 ms: 1.13x faster                                                   |
| sympy_integrate                  | 11.3 ms                                                | 10.0 ms: 1.13x faster                                                  |
| crypto_pyaes                     | 55.3 ms                                                | 49.2 ms: 1.12x faster                                                  |
| sphinx                           | 602 ms                                                 | 547 ms: 1.10x faster                                                   |
| bench_thread_pool                | 503 us                                                 | 461 us: 1.09x faster                                                   |
| scimark_lu                       | 75.9 ms                                                | 69.5 ms: 1.09x faster                                                  |
| telco                            | 4.84 ms                                                | 4.43 ms: 1.09x faster                                                  |
| sympy_sum                        | 75.1 ms                                                | 69.1 ms: 1.09x faster                                                  |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.18 ms: 1.08x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 345 ms: 1.08x faster                                                   |
| mako                             | 7.75 ms                                                | 7.18 ms: 1.08x faster                                                  |
| k_core                           | 1.61 sec                                               | 1.49 sec: 1.08x faster                                                 |
| connected_components             | 319 ms                                                 | 299 ms: 1.07x faster                                                   |
| sqlalchemy_declarative           | 59.0 ms                                                | 55.3 ms: 1.07x faster                                                  |
| shortest_path                    | 345 ms                                                 | 324 ms: 1.06x faster                                                   |
| docutils                         | 1.44 sec                                               | 1.36 sec: 1.06x faster                                                 |
| django_template                  | 20.5 ms                                                | 19.3 ms: 1.06x faster                                                  |
| xml_etree_iterparse              | 74.2 ms                                                | 70.3 ms: 1.06x faster                                                  |
| meteor_contest                   | 74.0 ms                                                | 70.1 ms: 1.06x faster                                                  |
| nbody                            | 73.6 ms                                                | 70.2 ms: 1.05x faster                                                  |
| scimark_fft                      | 200 ms                                                 | 192 ms: 1.04x faster                                                   |
| regex_dna                        | 149 ms                                                 | 143 ms: 1.04x faster                                                   |
| python_startup                   | 18.8 ms                                                | 18.1 ms: 1.04x faster                                                  |
| regex_v8                         | 17.0 ms                                                | 16.4 ms: 1.04x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 105 ms: 1.03x faster                                                   |
| pathlib                          | 23.2 ms                                                | 22.7 ms: 1.02x faster                                                  |
| bench_mp_pool                    | 64.7 ms                                                | 63.4 ms: 1.02x faster                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.52 us: 1.02x faster                                                  |
| json                             | 3.04 ms                                                | 2.99 ms: 1.02x faster                                                  |
| pidigits                         | 284 ms                                                 | 279 ms: 1.01x faster                                                   |
| coverage                         | 46.2 ms                                                | 45.7 ms: 1.01x faster                                                  |
| python_startup_no_site           | 13.7 ms                                                | 14.0 ms: 1.02x slower                                                  |
| many_optionals                   | 409 us                                                 | 418 us: 1.02x slower                                                   |
| json_loads                       | 17.0 us                                                | 17.7 us: 1.04x slower                                                  |
| gc_traversal                     | 2.94 ms                                                | 3.09 ms: 1.05x slower                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 1.27 ms: 1.07x slower                                                  |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.18 ms: 1.07x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 377 ms: 1.09x slower                                                   |
| json_dumps                       | 6.47 ms                                                | 7.08 ms: 1.09x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 160 ms: 1.16x slower                                                   |
| subparsers                       | 9.44 ms                                                | 11.4 ms: 1.21x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 121 ms: 2.55x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.16x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250412-3.14.0a7+-718d234-CLANG/bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7+-718d234.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.160x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: 1.09x