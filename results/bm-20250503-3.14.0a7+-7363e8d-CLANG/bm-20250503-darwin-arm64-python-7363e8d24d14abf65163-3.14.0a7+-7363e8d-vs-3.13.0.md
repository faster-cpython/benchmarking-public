# Results vs. 3.13.0

- fork: python
- ref: 7363e8d24d14abf65163
- machine: darwin-arm64
- commit hash: 7363e8d
- commit date: 2025-05-03
- overall geometric mean: 1.136x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-darwin-arm64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 155 ms: 1.16x faster                                                   |
| docutils       | 1.44 sec                                               | 1.39 sec: 1.04x faster                                                 |
| html5lib       | 36.7 ms                                                | 29.2 ms: 1.26x faster                                                  |
| sphinx         | 602 ms                                                 | 556 ms: 1.08x faster                                                   |
| Geometric mean | (ref)                                                  | 1.13x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-darwin-arm64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 184 ms: 1.56x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 339 ms: 1.50x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 347 ms: 1.47x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 184 ms: 1.46x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 349 ms: 1.43x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 153 ms: 1.38x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 346 ms: 1.38x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 145 ms: 1.37x faster                                                   |
| coroutines                       | 20.0 ms                                                | 15.2 ms: 1.32x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 132 ms: 1.28x faster                                                   |
| async_tree_eager                 | 69.9 ms                                                | 58.0 ms: 1.20x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 405 ms: 1.14x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 403 ms: 1.11x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 351 ms: 1.06x faster                                                   |
| async_generators                 | 294 ms                                                 | 279 ms: 1.05x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 380 ms: 1.09x slower                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 163 ms: 1.18x slower                                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 125 ms: 2.63x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.16x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-darwin-arm64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 43.8 ms: 1.27x faster                                                  |
| pidigits       | 284 ms                                                 | 280 ms: 1.01x faster                                                   |
| nbody          | 73.6 ms                                                | 73.4 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-darwin-arm64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 78.3 ms                                                | 61.7 ms: 1.27x faster                                                  |
| regex_effbot   | 2.63 ms                                                | 2.20 ms: 1.19x faster                                                  |
| regex_v8       | 17.0 ms                                                | 15.5 ms: 1.09x faster                                                  |
| regex_dna      | 149 ms                                                 | 141 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                  | 1.15x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-darwin-arm64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.19 sec: 1.32x faster                                                 |
| unpickle_pure_python | 165 us                                                 | 129 us: 1.28x faster                                                   |
| xml_etree_process    | 41.3 ms                                                | 35.2 ms: 1.17x faster                                                  |
| pickle_pure_python   | 215 us                                                 | 186 us: 1.15x faster                                                   |
| xml_etree_generate   | 57.1 ms                                                | 49.6 ms: 1.15x faster                                                  |
| xml_etree_iterparse  | 74.2 ms                                                | 70.8 ms: 1.05x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 105 ms: 1.03x faster                                                   |
| json_loads           | 17.0 us                                                | 18.5 us: 1.08x slower                                                  |
| json_dumps           | 6.47 ms                                                | 7.37 ms: 1.14x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-darwin-arm64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 19.6 ms: 1.04x slower                                                  |
| python_startup_no_site | 13.7 ms                                                | 14.7 ms: 1.07x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-darwin-arm64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 12.9 ms: 1.31x faster                                                  |
| genshi_xml      | 34.1 ms                                                | 27.2 ms: 1.25x faster                                                  |
| mako            | 7.75 ms                                                | 7.19 ms: 1.08x faster                                                  |
| django_template | 20.5 ms                                                | 19.7 ms: 1.04x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.17x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-darwin-arm64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 701 ms: 2.14x faster                                                   |
| generators                       | 31.9 ms                                                | 18.7 ms: 1.71x faster                                                  |
| deepcopy_memo                    | 27.4 us                                                | 16.6 us: 1.65x faster                                                  |
| go                               | 117 ms                                                 | 71.1 ms: 1.64x faster                                                  |
| deepcopy                         | 236 us                                                 | 145 us: 1.63x faster                                                   |
| async_tree_memoization_tg        | 288 ms                                                 | 184 ms: 1.56x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 339 ms: 1.50x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 347 ms: 1.47x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 184 ms: 1.46x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 349 ms: 1.43x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 153 ms: 1.38x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 346 ms: 1.38x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 145 ms: 1.37x faster                                                   |
| scimark_sor                      | 106 ms                                                 | 78.0 ms: 1.35x faster                                                  |
| deepcopy_reduce                  | 2.09 us                                                | 1.56 us: 1.34x faster                                                  |
| tomli_loads                      | 1.57 sec                                               | 1.19 sec: 1.32x faster                                                 |
| coroutines                       | 20.0 ms                                                | 15.2 ms: 1.32x faster                                                  |
| genshi_text                      | 16.9 ms                                                | 12.9 ms: 1.31x faster                                                  |
| deltablue                        | 2.65 ms                                                | 2.05 ms: 1.29x faster                                                  |
| hexiom                           | 4.87 ms                                                | 3.79 ms: 1.28x faster                                                  |
| unpickle_pure_python             | 165 us                                                 | 129 us: 1.28x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 132 ms: 1.28x faster                                                   |
| float                            | 55.8 ms                                                | 43.8 ms: 1.27x faster                                                  |
| pyflate                          | 352 ms                                                 | 276 ms: 1.27x faster                                                   |
| regex_compile                    | 78.3 ms                                                | 61.7 ms: 1.27x faster                                                  |
| html5lib                         | 36.7 ms                                                | 29.2 ms: 1.26x faster                                                  |
| genshi_xml                       | 34.1 ms                                                | 27.2 ms: 1.25x faster                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 40.6 ms: 1.24x faster                                                  |
| richards                         | 36.2 ms                                                | 29.4 ms: 1.23x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 23.7 ms: 1.21x faster                                                  |
| async_tree_eager                 | 69.9 ms                                                | 58.0 ms: 1.20x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.20 ms: 1.19x faster                                                  |
| richards_super                   | 39.2 ms                                                | 33.0 ms: 1.19x faster                                                  |
| logging_simple                   | 3.56 us                                                | 3.01 us: 1.18x faster                                                  |
| pylint                           | 180 ms                                                 | 152 ms: 1.18x faster                                                   |
| logging_silent                   | 71.0 ns                                                | 60.2 ns: 1.18x faster                                                  |
| xml_etree_process                | 41.3 ms                                                | 35.2 ms: 1.17x faster                                                  |
| pprint_pformat                   | 1.10 sec                                               | 940 ms: 1.17x faster                                                   |
| logging_format                   | 3.85 us                                                | 3.32 us: 1.16x faster                                                  |
| chaos                            | 41.1 ms                                                | 35.5 ms: 1.16x faster                                                  |
| 2to3                             | 179 ms                                                 | 155 ms: 1.16x faster                                                   |
| pickle_pure_python               | 215 us                                                 | 186 us: 1.15x faster                                                   |
| xml_etree_generate               | 57.1 ms                                                | 49.6 ms: 1.15x faster                                                  |
| pprint_safe_repr                 | 541 ms                                                 | 471 ms: 1.15x faster                                                   |
| comprehensions                   | 12.0 us                                                | 10.5 us: 1.14x faster                                                  |
| nqueens                          | 61.8 ms                                                | 54.4 ms: 1.14x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 405 ms: 1.14x faster                                                   |
| raytrace                         | 181 ms                                                 | 160 ms: 1.13x faster                                                   |
| bpe_tokeniser                    | 3.26 sec                                               | 2.91 sec: 1.12x faster                                                 |
| pycparser                        | 701 ms                                                 | 626 ms: 1.12x faster                                                   |
| typing_runtime_protocols         | 101 us                                                 | 90.0 us: 1.12x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 68.7 ms: 1.11x faster                                                  |
| sympy_expand                     | 248 ms                                                 | 223 ms: 1.11x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 403 ms: 1.11x faster                                                   |
| sympy_integrate                  | 11.3 ms                                                | 10.2 ms: 1.11x faster                                                  |
| crypto_pyaes                     | 55.3 ms                                                | 49.9 ms: 1.11x faster                                                  |
| sympy_str                        | 146 ms                                                 | 132 ms: 1.10x faster                                                   |
| regex_v8                         | 17.0 ms                                                | 15.5 ms: 1.09x faster                                                  |
| fannkuch                         | 279 ms                                                 | 257 ms: 1.09x faster                                                   |
| sphinx                           | 602 ms                                                 | 556 ms: 1.08x faster                                                   |
| scimark_lu                       | 75.9 ms                                                | 70.4 ms: 1.08x faster                                                  |
| mako                             | 7.75 ms                                                | 7.19 ms: 1.08x faster                                                  |
| sympy_sum                        | 75.1 ms                                                | 70.2 ms: 1.07x faster                                                  |
| bench_thread_pool                | 503 us                                                 | 471 us: 1.07x faster                                                   |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.28 ms: 1.07x faster                                                  |
| k_core                           | 1.61 sec                                               | 1.52 sec: 1.06x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 351 ms: 1.06x faster                                                   |
| shortest_path                    | 345 ms                                                 | 327 ms: 1.06x faster                                                   |
| connected_components             | 319 ms                                                 | 302 ms: 1.06x faster                                                   |
| regex_dna                        | 149 ms                                                 | 141 ms: 1.05x faster                                                   |
| async_generators                 | 294 ms                                                 | 279 ms: 1.05x faster                                                   |
| xml_etree_iterparse              | 74.2 ms                                                | 70.8 ms: 1.05x faster                                                  |
| sqlalchemy_declarative           | 59.0 ms                                                | 56.3 ms: 1.05x faster                                                  |
| django_template                  | 20.5 ms                                                | 19.7 ms: 1.04x faster                                                  |
| meteor_contest                   | 74.0 ms                                                | 71.2 ms: 1.04x faster                                                  |
| docutils                         | 1.44 sec                                               | 1.39 sec: 1.04x faster                                                 |
| telco                            | 4.84 ms                                                | 4.69 ms: 1.03x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 105 ms: 1.03x faster                                                   |
| pidigits                         | 284 ms                                                 | 280 ms: 1.01x faster                                                   |
| nbody                            | 73.6 ms                                                | 73.4 ms: 1.00x faster                                                  |
| pathlib                          | 23.2 ms                                                | 23.5 ms: 1.01x slower                                                  |
| bench_mp_pool                    | 64.7 ms                                                | 65.8 ms: 1.02x slower                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.58 us: 1.02x slower                                                  |
| scimark_fft                      | 200 ms                                                 | 204 ms: 1.02x slower                                                   |
| python_startup                   | 18.8 ms                                                | 19.6 ms: 1.04x slower                                                  |
| gc_traversal                     | 2.94 ms                                                | 3.09 ms: 1.05x slower                                                  |
| many_optionals                   | 409 us                                                 | 436 us: 1.07x slower                                                   |
| python_startup_no_site           | 13.7 ms                                                | 14.7 ms: 1.07x slower                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 1.28 ms: 1.07x slower                                                  |
| json_loads                       | 17.0 us                                                | 18.5 us: 1.08x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 380 ms: 1.09x slower                                                   |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.32 ms: 1.11x slower                                                  |
| json_dumps                       | 6.47 ms                                                | 7.37 ms: 1.14x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 163 ms: 1.18x slower                                                   |
| subparsers                       | 9.44 ms                                                | 12.6 ms: 1.34x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 125 ms: 2.63x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.14x faster                                                           |

Benchmark hidden because not significant (3): coverage, asyncio_websockets, json
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250503-3.14.0a7+-7363e8d-CLANG/bm-20250503-darwin-arm64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.136x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: 1.09x