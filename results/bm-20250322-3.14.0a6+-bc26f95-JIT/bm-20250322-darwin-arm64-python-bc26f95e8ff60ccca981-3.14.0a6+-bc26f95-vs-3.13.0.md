# Results vs. 3.13.0

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: darwin-arm64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.043x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 170 ms: 1.05x faster                                                   |
| docutils       | 1.44 sec                                               | 1.48 sec: 1.03x slower                                                 |
| html5lib       | 36.7 ms                                                | 32.3 ms: 1.14x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 198 ms: 1.45x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 202 ms: 1.33x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 385 ms: 1.33x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 381 ms: 1.31x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 391 ms: 1.30x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 167 ms: 1.26x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 387 ms: 1.24x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 161 ms: 1.23x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 143 ms: 1.17x faster                                                   |
| coroutines                       | 20.0 ms                                                | 17.3 ms: 1.16x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 416 ms: 1.10x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 417 ms: 1.07x faster                                                   |
| async_tree_eager                 | 69.9 ms                                                | 65.4 ms: 1.07x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 360 ms: 1.04x faster                                                   |
| async_generators                 | 294 ms                                                 | 283 ms: 1.04x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 392 ms: 1.13x slower                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 177 ms: 1.28x slower                                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 134 ms: 2.83x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.07x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 45.7 ms: 1.22x faster                                                  |
| nbody          | 73.6 ms                                                | 69.6 ms: 1.06x faster                                                  |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.27 ms: 1.16x faster                                                  |
| regex_v8       | 17.0 ms                                                | 15.9 ms: 1.07x faster                                                  |
| regex_compile  | 78.3 ms                                                | 73.5 ms: 1.06x faster                                                  |
| regex_dna      | 149 ms                                                 | 140 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.25 sec: 1.25x faster                                                 |
| unpickle_pure_python | 165 us                                                 | 140 us: 1.18x faster                                                   |
| xml_etree_process    | 41.3 ms                                                | 36.5 ms: 1.13x faster                                                  |
| xml_etree_generate   | 57.1 ms                                                | 51.4 ms: 1.11x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 99.1 ms: 1.09x faster                                                  |
| xml_etree_iterparse  | 74.2 ms                                                | 72.5 ms: 1.02x faster                                                  |
| pickle_pure_python   | 215 us                                                 | 212 us: 1.01x faster                                                   |
| json_loads           | 17.0 us                                                | 17.8 us: 1.04x slower                                                  |
| json_dumps           | 6.47 ms                                                | 7.53 ms: 1.16x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 18.7 ms: 1.01x faster                                                  |
| python_startup_no_site | 13.7 ms                                                | 14.2 ms: 1.04x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 7.75 ms                                                | 6.69 ms: 1.16x faster                                                  |
| genshi_text     | 16.9 ms                                                | 15.4 ms: 1.10x faster                                                  |
| genshi_xml      | 34.1 ms                                                | 32.1 ms: 1.06x faster                                                  |
| django_template | 20.5 ms                                                | 22.7 ms: 1.11x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy                         | 236 us                                                 | 162 us: 1.46x faster                                                   |
| async_tree_memoization_tg        | 288 ms                                                 | 198 ms: 1.45x faster                                                   |
| deepcopy_memo                    | 27.4 us                                                | 20.3 us: 1.35x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 202 ms: 1.33x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 385 ms: 1.33x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 381 ms: 1.31x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 391 ms: 1.30x faster                                                   |
| generators                       | 31.9 ms                                                | 25.0 ms: 1.28x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 167 ms: 1.26x faster                                                   |
| tomli_loads                      | 1.57 sec                                               | 1.25 sec: 1.25x faster                                                 |
| async_tree_eager_io_tg           | 479 ms                                                 | 387 ms: 1.24x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 161 ms: 1.23x faster                                                   |
| float                            | 55.8 ms                                                | 45.7 ms: 1.22x faster                                                  |
| deepcopy_reduce                  | 2.09 us                                                | 1.74 us: 1.20x faster                                                  |
| scimark_sor                      | 106 ms                                                 | 87.8 ms: 1.20x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 64.3 ms: 1.19x faster                                                  |
| unpickle_pure_python             | 165 us                                                 | 140 us: 1.18x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 143 ms: 1.17x faster                                                   |
| go                               | 117 ms                                                 | 100 ms: 1.16x faster                                                   |
| mako                             | 7.75 ms                                                | 6.69 ms: 1.16x faster                                                  |
| coroutines                       | 20.0 ms                                                | 17.3 ms: 1.16x faster                                                  |
| deltablue                        | 2.65 ms                                                | 2.29 ms: 1.16x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.27 ms: 1.16x faster                                                  |
| richards                         | 36.2 ms                                                | 31.7 ms: 1.14x faster                                                  |
| html5lib                         | 36.7 ms                                                | 32.3 ms: 1.14x faster                                                  |
| xml_etree_process                | 41.3 ms                                                | 36.5 ms: 1.13x faster                                                  |
| richards_super                   | 39.2 ms                                                | 35.3 ms: 1.11x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 25.9 ms: 1.11x faster                                                  |
| xml_etree_generate               | 57.1 ms                                                | 51.4 ms: 1.11x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 416 ms: 1.10x faster                                                   |
| pyflate                          | 352 ms                                                 | 321 ms: 1.10x faster                                                   |
| genshi_text                      | 16.9 ms                                                | 15.4 ms: 1.10x faster                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 46.3 ms: 1.09x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 99.1 ms: 1.09x faster                                                  |
| bpe_tokeniser                    | 3.26 sec                                               | 3.02 sec: 1.08x faster                                                 |
| telco                            | 4.84 ms                                                | 4.49 ms: 1.08x faster                                                  |
| pylint                           | 180 ms                                                 | 167 ms: 1.08x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 417 ms: 1.07x faster                                                   |
| regex_v8                         | 17.0 ms                                                | 15.9 ms: 1.07x faster                                                  |
| async_tree_eager                 | 69.9 ms                                                | 65.4 ms: 1.07x faster                                                  |
| pprint_safe_repr                 | 541 ms                                                 | 507 ms: 1.07x faster                                                   |
| regex_compile                    | 78.3 ms                                                | 73.5 ms: 1.06x faster                                                  |
| pprint_pformat                   | 1.10 sec                                               | 1.04 sec: 1.06x faster                                                 |
| genshi_xml                       | 34.1 ms                                                | 32.1 ms: 1.06x faster                                                  |
| regex_dna                        | 149 ms                                                 | 140 ms: 1.06x faster                                                   |
| scimark_fft                      | 200 ms                                                 | 189 ms: 1.06x faster                                                   |
| nbody                            | 73.6 ms                                                | 69.6 ms: 1.06x faster                                                  |
| bench_mp_pool                    | 64.7 ms                                                | 61.4 ms: 1.05x faster                                                  |
| 2to3                             | 179 ms                                                 | 170 ms: 1.05x faster                                                   |
| connected_components             | 319 ms                                                 | 304 ms: 1.05x faster                                                   |
| k_core                           | 1.61 sec                                               | 1.55 sec: 1.04x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 360 ms: 1.04x faster                                                   |
| async_generators                 | 294 ms                                                 | 283 ms: 1.04x faster                                                   |
| shortest_path                    | 345 ms                                                 | 336 ms: 1.03x faster                                                   |
| typing_runtime_protocols         | 101 us                                                 | 98.3 us: 1.02x faster                                                  |
| xml_etree_iterparse              | 74.2 ms                                                | 72.5 ms: 1.02x faster                                                  |
| thrift                           | 466 us                                                 | 456 us: 1.02x faster                                                   |
| pickle_pure_python               | 215 us                                                 | 212 us: 1.01x faster                                                   |
| mdp                              | 1.50 sec                                               | 1.48 sec: 1.01x faster                                                 |
| python_startup                   | 18.8 ms                                                | 18.7 ms: 1.01x faster                                                  |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                                   |
| bench_thread_pool                | 503 us                                                 | 505 us: 1.00x slower                                                   |
| sympy_str                        | 146 ms                                                 | 146 ms: 1.00x slower                                                   |
| logging_silent                   | 71.0 ns                                                | 71.3 ns: 1.00x slower                                                  |
| sympy_expand                     | 248 ms                                                 | 250 ms: 1.01x slower                                                   |
| logging_simple                   | 3.56 us                                                | 3.60 us: 1.01x slower                                                  |
| sympy_sum                        | 75.1 ms                                                | 76.1 ms: 1.01x slower                                                  |
| pycparser                        | 701 ms                                                 | 713 ms: 1.02x slower                                                   |
| coverage                         | 46.2 ms                                                | 47.1 ms: 1.02x slower                                                  |
| logging_format                   | 3.85 us                                                | 3.92 us: 1.02x slower                                                  |
| meteor_contest                   | 74.0 ms                                                | 75.8 ms: 1.02x slower                                                  |
| fannkuch                         | 279 ms                                                 | 287 ms: 1.03x slower                                                   |
| docutils                         | 1.44 sec                                               | 1.48 sec: 1.03x slower                                                 |
| pathlib                          | 23.2 ms                                                | 23.9 ms: 1.03x slower                                                  |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.07 ms: 1.03x slower                                                  |
| sympy_integrate                  | 11.3 ms                                                | 11.7 ms: 1.04x slower                                                  |
| python_startup_no_site           | 13.7 ms                                                | 14.2 ms: 1.04x slower                                                  |
| hexiom                           | 4.87 ms                                                | 5.06 ms: 1.04x slower                                                  |
| comprehensions                   | 12.0 us                                                | 12.4 us: 1.04x slower                                                  |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.96 ms: 1.04x slower                                                  |
| sqlalchemy_declarative           | 59.0 ms                                                | 61.4 ms: 1.04x slower                                                  |
| json_loads                       | 17.0 us                                                | 17.8 us: 1.04x slower                                                  |
| scimark_lu                       | 75.9 ms                                                | 79.9 ms: 1.05x slower                                                  |
| raytrace                         | 181 ms                                                 | 192 ms: 1.06x slower                                                   |
| gc_traversal                     | 2.94 ms                                                | 3.13 ms: 1.07x slower                                                  |
| nqueens                          | 61.8 ms                                                | 66.0 ms: 1.07x slower                                                  |
| chaos                            | 41.1 ms                                                | 43.8 ms: 1.07x slower                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 1.29 ms: 1.08x slower                                                  |
| crypto_pyaes                     | 55.3 ms                                                | 60.6 ms: 1.10x slower                                                  |
| django_template                  | 20.5 ms                                                | 22.7 ms: 1.11x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 392 ms: 1.13x slower                                                   |
| many_optionals                   | 409 us                                                 | 473 us: 1.16x slower                                                   |
| json_dumps                       | 6.47 ms                                                | 7.53 ms: 1.16x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 177 ms: 1.28x slower                                                   |
| subparsers                       | 9.44 ms                                                | 12.8 ms: 1.35x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 134 ms: 2.83x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (5): sphinx, dask, asyncio_websockets, sqlite_synth, json
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.043x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.10x