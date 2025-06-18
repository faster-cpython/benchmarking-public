# Results vs. 3.13.0

- fork: python
- ref: fba5dded6df3c2b19435
- machine: darwin-arm64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.043x slower
- HPT reliability: 97.34%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 191 ms: 1.07x slower                                                  |
| docutils       | 1.44 sec                                               | 1.63 sec: 1.13x slower                                                |
| html5lib       | 36.7 ms                                                | 33.7 ms: 1.09x faster                                                 |
| sphinx         | 602 ms                                                 | 659 ms: 1.09x slower                                                  |
| Geometric mean | (ref)                                                  | 1.05x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 204 ms: 1.41x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 390 ms: 1.31x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 207 ms: 1.29x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 397 ms: 1.26x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 405 ms: 1.25x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 175 ms: 1.21x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 400 ms: 1.20x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 168 ms: 1.18x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 151 ms: 1.12x faster                                                  |
| coroutines                       | 20.0 ms                                                | 18.4 ms: 1.09x faster                                                 |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 452 ms: 1.02x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 393 ms: 1.05x slower                                                  |
| async_tree_eager                 | 69.9 ms                                                | 73.8 ms: 1.06x slower                                                 |
| async_generators                 | 294 ms                                                 | 329 ms: 1.12x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 426 ms: 1.23x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 182 ms: 1.32x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 142 ms: 2.99x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 51.6 ms: 1.08x faster                                                 |
| pidigits       | 284 ms                                                 | 285 ms: 1.00x slower                                                  |
| nbody          | 73.6 ms                                                | 80.0 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.22 ms: 1.19x faster                                                 |
| regex_compile  | 78.3 ms                                                | 76.4 ms: 1.02x faster                                                 |
| regex_dna      | 149 ms                                                 | 145 ms: 1.02x faster                                                  |
| regex_v8       | 17.0 ms                                                | 17.4 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.41 sec: 1.11x faster                                                |
| unpickle_pure_python | 165 us                                                 | 150 us: 1.10x faster                                                  |
| pickle_pure_python   | 215 us                                                 | 221 us: 1.03x slower                                                  |
| xml_etree_parse      | 108 ms                                                 | 112 ms: 1.04x slower                                                  |
| xml_etree_iterparse  | 74.2 ms                                                | 77.1 ms: 1.04x slower                                                 |
| xml_etree_process    | 41.3 ms                                                | 43.4 ms: 1.05x slower                                                 |
| xml_etree_generate   | 57.1 ms                                                | 64.3 ms: 1.13x slower                                                 |
| json_dumps           | 6.47 ms                                                | 8.11 ms: 1.25x slower                                                 |
| json_loads           | 17.0 us                                                | 22.8 us: 1.34x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.07x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 18.7 ms: 1.01x faster                                                 |
| python_startup_no_site | 13.7 ms                                                | 13.9 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 15.9 ms: 1.06x faster                                                 |
| genshi_xml      | 34.1 ms                                                | 33.8 ms: 1.01x faster                                                 |
| mako            | 7.75 ms                                                | 8.17 ms: 1.05x slower                                                 |
| django_template | 20.5 ms                                                | 25.8 ms: 1.26x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 895 ms: 1.67x faster                                                  |
| go                               | 117 ms                                                 | 79.8 ms: 1.46x faster                                                 |
| async_tree_memoization_tg        | 288 ms                                                 | 204 ms: 1.41x faster                                                  |
| deepcopy_memo                    | 27.4 us                                                | 19.6 us: 1.40x faster                                                 |
| generators                       | 31.9 ms                                                | 23.4 ms: 1.37x faster                                                 |
| async_tree_eager_io              | 511 ms                                                 | 390 ms: 1.31x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 207 ms: 1.29x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 397 ms: 1.26x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 405 ms: 1.25x faster                                                  |
| deepcopy                         | 236 us                                                 | 190 us: 1.24x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 175 ms: 1.21x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 400 ms: 1.20x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.22 ms: 1.19x faster                                                 |
| async_tree_none_tg               | 198 ms                                                 | 168 ms: 1.18x faster                                                  |
| scimark_sor                      | 106 ms                                                 | 91.1 ms: 1.16x faster                                                 |
| pyflate                          | 352 ms                                                 | 304 ms: 1.16x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 151 ms: 1.12x faster                                                  |
| tomli_loads                      | 1.57 sec                                               | 1.41 sec: 1.11x faster                                                |
| unpickle_pure_python             | 165 us                                                 | 150 us: 1.10x faster                                                  |
| html5lib                         | 36.7 ms                                                | 33.7 ms: 1.09x faster                                                 |
| coroutines                       | 20.0 ms                                                | 18.4 ms: 1.09x faster                                                 |
| float                            | 55.8 ms                                                | 51.6 ms: 1.08x faster                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 46.8 ms: 1.08x faster                                                 |
| genshi_text                      | 16.9 ms                                                | 15.9 ms: 1.06x faster                                                 |
| dulwich_log                      | 28.7 ms                                                | 27.3 ms: 1.05x faster                                                 |
| deepcopy_reduce                  | 2.09 us                                                | 2.04 us: 1.03x faster                                                 |
| regex_compile                    | 78.3 ms                                                | 76.4 ms: 1.02x faster                                                 |
| regex_dna                        | 149 ms                                                 | 145 ms: 1.02x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 452 ms: 1.02x faster                                                  |
| connected_components             | 319 ms                                                 | 315 ms: 1.01x faster                                                  |
| shortest_path                    | 345 ms                                                 | 342 ms: 1.01x faster                                                  |
| genshi_xml                       | 34.1 ms                                                | 33.8 ms: 1.01x faster                                                 |
| python_startup                   | 18.8 ms                                                | 18.7 ms: 1.01x faster                                                 |
| pidigits                         | 284 ms                                                 | 285 ms: 1.00x slower                                                  |
| richards                         | 36.2 ms                                                | 36.5 ms: 1.01x slower                                                 |
| python_startup_no_site           | 13.7 ms                                                | 13.9 ms: 1.01x slower                                                 |
| hexiom                           | 4.87 ms                                                | 4.96 ms: 1.02x slower                                                 |
| deltablue                        | 2.65 ms                                                | 2.70 ms: 1.02x slower                                                 |
| regex_v8                         | 17.0 ms                                                | 17.4 ms: 1.02x slower                                                 |
| pathlib                          | 23.2 ms                                                | 23.8 ms: 1.03x slower                                                 |
| pickle_pure_python               | 215 us                                                 | 221 us: 1.03x slower                                                  |
| xml_etree_parse                  | 108 ms                                                 | 112 ms: 1.04x slower                                                  |
| xml_etree_iterparse              | 74.2 ms                                                | 77.1 ms: 1.04x slower                                                 |
| richards_super                   | 39.2 ms                                                | 41.0 ms: 1.05x slower                                                 |
| xml_etree_process                | 41.3 ms                                                | 43.4 ms: 1.05x slower                                                 |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 393 ms: 1.05x slower                                                  |
| mako                             | 7.75 ms                                                | 8.17 ms: 1.05x slower                                                 |
| async_tree_eager                 | 69.9 ms                                                | 73.8 ms: 1.06x slower                                                 |
| 2to3                             | 179 ms                                                 | 191 ms: 1.07x slower                                                  |
| spectral_norm                    | 76.5 ms                                                | 81.9 ms: 1.07x slower                                                 |
| sympy_integrate                  | 11.3 ms                                                | 12.2 ms: 1.08x slower                                                 |
| bench_thread_pool                | 503 us                                                 | 546 us: 1.08x slower                                                  |
| nbody                            | 73.6 ms                                                | 80.0 ms: 1.09x slower                                                 |
| chaos                            | 41.1 ms                                                | 44.7 ms: 1.09x slower                                                 |
| gc_traversal                     | 2.94 ms                                                | 3.20 ms: 1.09x slower                                                 |
| crypto_pyaes                     | 55.3 ms                                                | 60.4 ms: 1.09x slower                                                 |
| sphinx                           | 602 ms                                                 | 659 ms: 1.09x slower                                                  |
| meteor_contest                   | 74.0 ms                                                | 81.4 ms: 1.10x slower                                                 |
| nqueens                          | 61.8 ms                                                | 68.3 ms: 1.11x slower                                                 |
| async_generators                 | 294 ms                                                 | 329 ms: 1.12x slower                                                  |
| xml_etree_generate               | 57.1 ms                                                | 64.3 ms: 1.13x slower                                                 |
| docutils                         | 1.44 sec                                               | 1.63 sec: 1.13x slower                                                |
| pycparser                        | 701 ms                                                 | 792 ms: 1.13x slower                                                  |
| bpe_tokeniser                    | 3.26 sec                                               | 3.71 sec: 1.14x slower                                                |
| comprehensions                   | 12.0 us                                                | 13.6 us: 1.14x slower                                                 |
| logging_format                   | 3.85 us                                                | 4.39 us: 1.14x slower                                                 |
| logging_simple                   | 3.56 us                                                | 4.07 us: 1.14x slower                                                 |
| sympy_sum                        | 75.1 ms                                                | 86.7 ms: 1.16x slower                                                 |
| sympy_str                        | 146 ms                                                 | 169 ms: 1.16x slower                                                  |
| bench_mp_pool                    | 64.7 ms                                                | 75.2 ms: 1.16x slower                                                 |
| telco                            | 4.84 ms                                                | 5.63 ms: 1.16x slower                                                 |
| scimark_lu                       | 75.9 ms                                                | 88.6 ms: 1.17x slower                                                 |
| create_gc_cycles                 | 1.19 ms                                                | 1.40 ms: 1.17x slower                                                 |
| raytrace                         | 181 ms                                                 | 214 ms: 1.18x slower                                                  |
| sympy_expand                     | 248 ms                                                 | 296 ms: 1.19x slower                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.90 us: 1.22x slower                                                 |
| scimark_fft                      | 200 ms                                                 | 245 ms: 1.23x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 426 ms: 1.23x slower                                                  |
| thrift                           | 466 us                                                 | 575 us: 1.23x slower                                                  |
| typing_runtime_protocols         | 101 us                                                 | 125 us: 1.24x slower                                                  |
| fannkuch                         | 279 ms                                                 | 349 ms: 1.25x slower                                                  |
| json_dumps                       | 6.47 ms                                                | 8.11 ms: 1.25x slower                                                 |
| django_template                  | 20.5 ms                                                | 25.8 ms: 1.26x slower                                                 |
| json                             | 3.04 ms                                                | 3.85 ms: 1.27x slower                                                 |
| pprint_pformat                   | 1.10 sec                                               | 1.40 sec: 1.27x slower                                                |
| pprint_safe_repr                 | 541 ms                                                 | 693 ms: 1.28x slower                                                  |
| many_optionals                   | 409 us                                                 | 536 us: 1.31x slower                                                  |
| coverage                         | 46.2 ms                                                | 60.8 ms: 1.32x slower                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 182 ms: 1.32x slower                                                  |
| json_loads                       | 17.0 us                                                | 22.8 us: 1.34x slower                                                 |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 4.32 ms: 1.45x slower                                                 |
| subparsers                       | 9.44 ms                                                | 16.2 ms: 1.72x slower                                                 |
| async_tree_eager_tg              | 47.4 ms                                                | 142 ms: 2.99x slower                                                  |
| logging_silent                   | 71.0 ns                                                | 417 ns: 5.88x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.06x slower                                                          |

Benchmark hidden because not significant (5): k_core, async_tree_cpu_io_mixed_tg, dask, asyncio_websockets, pylint
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.043x slower

# HPT report

- Reliability score: 97.34% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.09x