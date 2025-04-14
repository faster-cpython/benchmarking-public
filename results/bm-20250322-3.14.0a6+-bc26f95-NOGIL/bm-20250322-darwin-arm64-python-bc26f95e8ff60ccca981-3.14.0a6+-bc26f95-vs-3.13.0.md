# Results vs. 3.13.0

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: darwin-arm64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.043x slower
- HPT reliability: 99.85%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 195 ms: 1.09x slower                                                   |
| docutils       | 1.44 sec                                               | 1.47 sec: 1.02x slower                                                 |
| sphinx         | 602 ms                                                 | 635 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                  | 1.04x slower                                                           |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 184 ms: 1.56x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 331 ms: 1.51x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 317 ms: 1.51x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 343 ms: 1.49x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 358 ms: 1.42x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 149 ms: 1.33x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 207 ms: 1.29x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 172 ms: 1.23x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 388 ms: 1.15x faster                                                   |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 413 ms: 1.11x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 152 ms: 1.11x faster                                                   |
| coroutines                       | 20.0 ms                                                | 18.7 ms: 1.07x faster                                                  |
| async_generators                 | 294 ms                                                 | 276 ms: 1.07x faster                                                   |
| asyncio_websockets               | 242 ms                                                 | 238 ms: 1.02x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 369 ms: 1.01x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 372 ms: 1.07x slower                                                   |
| async_tree_eager                 | 69.9 ms                                                | 83.9 ms: 1.20x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 167 ms: 1.21x slower                                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 127 ms: 2.67x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 54.8 ms: 1.02x faster                                                  |
| pidigits       | 284 ms                                                 | 281 ms: 1.01x faster                                                   |
| nbody          | 73.6 ms                                                | 105 ms: 1.42x slower                                                   |
| Geometric mean | (ref)                                                  | 1.11x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.08 ms: 1.27x faster                                                  |
| regex_v8       | 17.0 ms                                                | 14.9 ms: 1.14x faster                                                  |
| regex_dna      | 149 ms                                                 | 137 ms: 1.09x faster                                                   |
| regex_compile  | 78.3 ms                                                | 86.4 ms: 1.10x slower                                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_iterparse  | 74.2 ms                                                | 66.4 ms: 1.12x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 103 ms: 1.05x faster                                                   |
| tomli_loads          | 1.57 sec                                               | 1.60 sec: 1.02x slower                                                 |
| xml_etree_generate   | 57.1 ms                                                | 60.5 ms: 1.06x slower                                                  |
| xml_etree_process    | 41.3 ms                                                | 44.9 ms: 1.09x slower                                                  |
| json_loads           | 17.0 us                                                | 18.6 us: 1.09x slower                                                  |
| unpickle_pure_python | 165 us                                                 | 187 us: 1.13x slower                                                   |
| pickle_pure_python   | 215 us                                                 | 250 us: 1.17x slower                                                   |
| json_dumps           | 6.47 ms                                                | 7.95 ms: 1.23x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.07x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 19.2 ms: 1.02x slower                                                  |
| python_startup_no_site | 13.7 ms                                                | 15.6 ms: 1.14x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 18.3 ms: 1.08x slower                                                  |
| genshi_xml      | 34.1 ms                                                | 37.4 ms: 1.10x slower                                                  |
| django_template | 20.5 ms                                                | 26.9 ms: 1.31x slower                                                  |
| mako            | 7.75 ms                                                | 10.8 ms: 1.40x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.22x slower                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| gc_traversal                     | 2.94 ms                                                | 1.43 ms: 2.05x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 184 ms: 1.56x faster                                                   |
| create_gc_cycles                 | 1.19 ms                                                | 780 us: 1.53x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 331 ms: 1.51x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 317 ms: 1.51x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 343 ms: 1.49x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 358 ms: 1.42x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 149 ms: 1.33x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 207 ms: 1.29x faster                                                   |
| deepcopy                         | 236 us                                                 | 186 us: 1.27x faster                                                   |
| regex_effbot                     | 2.63 ms                                                | 2.08 ms: 1.27x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 172 ms: 1.23x faster                                                   |
| sqlite_synth                     | 1.55 us                                                | 1.33 us: 1.17x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 388 ms: 1.15x faster                                                   |
| regex_v8                         | 17.0 ms                                                | 14.9 ms: 1.14x faster                                                  |
| xml_etree_iterparse              | 74.2 ms                                                | 66.4 ms: 1.12x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 413 ms: 1.11x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 152 ms: 1.11x faster                                                   |
| deepcopy_memo                    | 27.4 us                                                | 24.8 us: 1.10x faster                                                  |
| regex_dna                        | 149 ms                                                 | 137 ms: 1.09x faster                                                   |
| go                               | 117 ms                                                 | 107 ms: 1.09x faster                                                   |
| generators                       | 31.9 ms                                                | 29.8 ms: 1.07x faster                                                  |
| coroutines                       | 20.0 ms                                                | 18.7 ms: 1.07x faster                                                  |
| deepcopy_reduce                  | 2.09 us                                                | 1.96 us: 1.07x faster                                                  |
| async_generators                 | 294 ms                                                 | 276 ms: 1.07x faster                                                   |
| xml_etree_parse                  | 108 ms                                                 | 103 ms: 1.05x faster                                                   |
| dulwich_log                      | 28.7 ms                                                | 27.7 ms: 1.04x faster                                                  |
| asyncio_websockets               | 242 ms                                                 | 238 ms: 1.02x faster                                                   |
| float                            | 55.8 ms                                                | 54.8 ms: 1.02x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 369 ms: 1.01x faster                                                   |
| pidigits                         | 284 ms                                                 | 281 ms: 1.01x faster                                                   |
| pycparser                        | 701 ms                                                 | 711 ms: 1.01x slower                                                   |
| docutils                         | 1.44 sec                                               | 1.47 sec: 1.02x slower                                                 |
| json                             | 3.04 ms                                                | 3.10 ms: 1.02x slower                                                  |
| tomli_loads                      | 1.57 sec                                               | 1.60 sec: 1.02x slower                                                 |
| python_startup                   | 18.8 ms                                                | 19.2 ms: 1.02x slower                                                  |
| bench_mp_pool                    | 64.7 ms                                                | 66.6 ms: 1.03x slower                                                  |
| bpe_tokeniser                    | 3.26 sec                                               | 3.38 sec: 1.04x slower                                                 |
| pyflate                          | 352 ms                                                 | 370 ms: 1.05x slower                                                   |
| sphinx                           | 602 ms                                                 | 635 ms: 1.05x slower                                                   |
| pathlib                          | 23.2 ms                                                | 24.5 ms: 1.06x slower                                                  |
| xml_etree_generate               | 57.1 ms                                                | 60.5 ms: 1.06x slower                                                  |
| k_core                           | 1.61 sec                                               | 1.72 sec: 1.07x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 372 ms: 1.07x slower                                                   |
| shortest_path                    | 345 ms                                                 | 370 ms: 1.07x slower                                                   |
| telco                            | 4.84 ms                                                | 5.24 ms: 1.08x slower                                                  |
| genshi_text                      | 16.9 ms                                                | 18.3 ms: 1.08x slower                                                  |
| xml_etree_process                | 41.3 ms                                                | 44.9 ms: 1.09x slower                                                  |
| 2to3                             | 179 ms                                                 | 195 ms: 1.09x slower                                                   |
| json_loads                       | 17.0 us                                                | 18.6 us: 1.09x slower                                                  |
| genshi_xml                       | 34.1 ms                                                | 37.4 ms: 1.10x slower                                                  |
| thrift                           | 466 us                                                 | 513 us: 1.10x slower                                                   |
| connected_components             | 319 ms                                                 | 352 ms: 1.10x slower                                                   |
| regex_compile                    | 78.3 ms                                                | 86.4 ms: 1.10x slower                                                  |
| mdp                              | 1.50 sec                                               | 1.67 sec: 1.11x slower                                                 |
| pprint_pformat                   | 1.10 sec                                               | 1.23 sec: 1.11x slower                                                 |
| pprint_safe_repr                 | 541 ms                                                 | 604 ms: 1.12x slower                                                   |
| unpickle_pure_python             | 165 us                                                 | 187 us: 1.13x slower                                                   |
| python_startup_no_site           | 13.7 ms                                                | 15.6 ms: 1.14x slower                                                  |
| sympy_sum                        | 75.1 ms                                                | 85.8 ms: 1.14x slower                                                  |
| sympy_integrate                  | 11.3 ms                                                | 13.0 ms: 1.15x slower                                                  |
| sympy_expand                     | 248 ms                                                 | 286 ms: 1.15x slower                                                   |
| sympy_str                        | 146 ms                                                 | 168 ms: 1.15x slower                                                   |
| typing_runtime_protocols         | 101 us                                                 | 116 us: 1.16x slower                                                   |
| logging_simple                   | 3.56 us                                                | 4.13 us: 1.16x slower                                                  |
| sqlalchemy_imperative            | 6.69 ms                                                | 7.77 ms: 1.16x slower                                                  |
| deltablue                        | 2.65 ms                                                | 3.08 ms: 1.16x slower                                                  |
| pickle_pure_python               | 215 us                                                 | 250 us: 1.17x slower                                                   |
| fannkuch                         | 279 ms                                                 | 327 ms: 1.17x slower                                                   |
| richards                         | 36.2 ms                                                | 42.4 ms: 1.17x slower                                                  |
| logging_format                   | 3.85 us                                                | 4.53 us: 1.18x slower                                                  |
| sqlalchemy_declarative           | 59.0 ms                                                | 69.6 ms: 1.18x slower                                                  |
| many_optionals                   | 409 us                                                 | 484 us: 1.18x slower                                                   |
| meteor_contest                   | 74.0 ms                                                | 87.6 ms: 1.18x slower                                                  |
| spectral_norm                    | 76.5 ms                                                | 90.6 ms: 1.19x slower                                                  |
| scimark_fft                      | 200 ms                                                 | 238 ms: 1.19x slower                                                   |
| async_tree_eager                 | 69.9 ms                                                | 83.9 ms: 1.20x slower                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 60.6 ms: 1.20x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 167 ms: 1.21x slower                                                   |
| chaos                            | 41.1 ms                                                | 49.7 ms: 1.21x slower                                                  |
| crypto_pyaes                     | 55.3 ms                                                | 67.0 ms: 1.21x slower                                                  |
| nqueens                          | 61.8 ms                                                | 75.0 ms: 1.21x slower                                                  |
| logging_silent                   | 71.0 ns                                                | 87.2 ns: 1.23x slower                                                  |
| json_dumps                       | 6.47 ms                                                | 7.95 ms: 1.23x slower                                                  |
| hexiom                           | 4.87 ms                                                | 6.02 ms: 1.24x slower                                                  |
| comprehensions                   | 12.0 us                                                | 14.8 us: 1.24x slower                                                  |
| richards_super                   | 39.2 ms                                                | 48.7 ms: 1.24x slower                                                  |
| scimark_lu                       | 75.9 ms                                                | 98.6 ms: 1.30x slower                                                  |
| django_template                  | 20.5 ms                                                | 26.9 ms: 1.31x slower                                                  |
| raytrace                         | 181 ms                                                 | 239 ms: 1.32x slower                                                   |
| coverage                         | 46.2 ms                                                | 61.1 ms: 1.32x slower                                                  |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 4.09 ms: 1.37x slower                                                  |
| mako                             | 7.75 ms                                                | 10.8 ms: 1.40x slower                                                  |
| nbody                            | 73.6 ms                                                | 105 ms: 1.42x slower                                                   |
| subparsers                       | 9.44 ms                                                | 13.6 ms: 1.44x slower                                                  |
| bench_thread_pool                | 503 us                                                 | 756 us: 1.50x slower                                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 127 ms: 2.67x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.05x slower                                                           |

Benchmark hidden because not significant (3): pylint, html5lib, scimark_sor
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250322-3.14.0a6+-bc26f95-NOGIL/bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.043x slower

# HPT report

- Reliability score: 99.85% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.23x