# Results vs. 3.13.0

- fork: python
- ref: fba5dded6df3c2b19435
- machine: darwin-arm64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.027x slower
- HPT reliability: 93.26%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 187 ms: 1.05x slower                                                  |
| docutils       | 1.44 sec                                               | 1.64 sec: 1.14x slower                                                |
| html5lib       | 36.7 ms                                                | 33.3 ms: 1.10x faster                                                 |
| sphinx         | 602 ms                                                 | 647 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 202 ms: 1.42x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 386 ms: 1.32x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 204 ms: 1.31x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 387 ms: 1.29x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 400 ms: 1.27x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 173 ms: 1.22x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 397 ms: 1.21x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 167 ms: 1.19x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 148 ms: 1.14x faster                                                  |
| coroutines                       | 20.0 ms                                                | 18.1 ms: 1.11x faster                                                 |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 450 ms: 1.02x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 446 ms: 1.00x faster                                                  |
| async_tree_eager                 | 69.9 ms                                                | 70.5 ms: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 389 ms: 1.04x slower                                                  |
| async_generators                 | 294 ms                                                 | 310 ms: 1.06x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 425 ms: 1.22x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 180 ms: 1.30x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 141 ms: 2.97x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 51.4 ms: 1.09x faster                                                 |
| pidigits       | 284 ms                                                 | 285 ms: 1.00x slower                                                  |
| nbody          | 73.6 ms                                                | 83.1 ms: 1.13x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.19 ms: 1.20x faster                                                 |
| regex_compile  | 78.3 ms                                                | 74.2 ms: 1.05x faster                                                 |
| regex_dna      | 149 ms                                                 | 145 ms: 1.03x faster                                                  |
| regex_v8       | 17.0 ms                                                | 17.4 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.39 sec: 1.13x faster                                                |
| unpickle_pure_python | 165 us                                                 | 155 us: 1.07x faster                                                  |
| xml_etree_iterparse  | 74.2 ms                                                | 76.0 ms: 1.02x slower                                                 |
| pickle_pure_python   | 215 us                                                 | 221 us: 1.03x slower                                                  |
| xml_etree_parse      | 108 ms                                                 | 112 ms: 1.04x slower                                                  |
| xml_etree_process    | 41.3 ms                                                | 43.9 ms: 1.06x slower                                                 |
| xml_etree_generate   | 57.1 ms                                                | 65.2 ms: 1.14x slower                                                 |
| json_dumps           | 6.47 ms                                                | 8.09 ms: 1.25x slower                                                 |
| json_loads           | 17.0 us                                                | 22.7 us: 1.33x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.07x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 20.2 ms: 1.07x slower                                                 |
| python_startup_no_site | 13.7 ms                                                | 15.3 ms: 1.11x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 15.7 ms: 1.08x faster                                                 |
| genshi_xml      | 34.1 ms                                                | 33.1 ms: 1.03x faster                                                 |
| mako            | 7.75 ms                                                | 8.21 ms: 1.06x slower                                                 |
| django_template | 20.5 ms                                                | 25.5 ms: 1.25x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 883 ms: 1.70x faster                                                  |
| go                               | 117 ms                                                 | 77.2 ms: 1.51x faster                                                 |
| async_tree_memoization_tg        | 288 ms                                                 | 202 ms: 1.42x faster                                                  |
| deepcopy_memo                    | 27.4 us                                                | 19.3 us: 1.42x faster                                                 |
| generators                       | 31.9 ms                                                | 22.8 ms: 1.40x faster                                                 |
| async_tree_eager_io              | 511 ms                                                 | 386 ms: 1.32x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 204 ms: 1.31x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 387 ms: 1.29x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 400 ms: 1.27x faster                                                  |
| deepcopy                         | 236 us                                                 | 186 us: 1.27x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 173 ms: 1.22x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 397 ms: 1.21x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.19 ms: 1.20x faster                                                 |
| async_tree_none_tg               | 198 ms                                                 | 167 ms: 1.19x faster                                                  |
| scimark_sor                      | 106 ms                                                 | 91.2 ms: 1.16x faster                                                 |
| pyflate                          | 352 ms                                                 | 303 ms: 1.16x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 148 ms: 1.14x faster                                                  |
| tomli_loads                      | 1.57 sec                                               | 1.39 sec: 1.13x faster                                                |
| coroutines                       | 20.0 ms                                                | 18.1 ms: 1.11x faster                                                 |
| html5lib                         | 36.7 ms                                                | 33.3 ms: 1.10x faster                                                 |
| float                            | 55.8 ms                                                | 51.4 ms: 1.09x faster                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 46.7 ms: 1.08x faster                                                 |
| genshi_text                      | 16.9 ms                                                | 15.7 ms: 1.08x faster                                                 |
| unpickle_pure_python             | 165 us                                                 | 155 us: 1.07x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 27.0 ms: 1.06x faster                                                 |
| hexiom                           | 4.87 ms                                                | 4.58 ms: 1.06x faster                                                 |
| deepcopy_reduce                  | 2.09 us                                                | 1.98 us: 1.06x faster                                                 |
| regex_compile                    | 78.3 ms                                                | 74.2 ms: 1.05x faster                                                 |
| k_core                           | 1.61 sec                                               | 1.54 sec: 1.05x faster                                                |
| genshi_xml                       | 34.1 ms                                                | 33.1 ms: 1.03x faster                                                 |
| regex_dna                        | 149 ms                                                 | 145 ms: 1.03x faster                                                  |
| connected_components             | 319 ms                                                 | 312 ms: 1.02x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 450 ms: 1.02x faster                                                  |
| shortest_path                    | 345 ms                                                 | 340 ms: 1.02x faster                                                  |
| deltablue                        | 2.65 ms                                                | 2.61 ms: 1.01x faster                                                 |
| richards                         | 36.2 ms                                                | 35.9 ms: 1.01x faster                                                 |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 446 ms: 1.00x faster                                                  |
| pidigits                         | 284 ms                                                 | 285 ms: 1.00x slower                                                  |
| async_tree_eager                 | 69.9 ms                                                | 70.5 ms: 1.01x slower                                                 |
| regex_v8                         | 17.0 ms                                                | 17.4 ms: 1.02x slower                                                 |
| xml_etree_iterparse              | 74.2 ms                                                | 76.0 ms: 1.02x slower                                                 |
| meteor_contest                   | 74.0 ms                                                | 75.8 ms: 1.02x slower                                                 |
| pickle_pure_python               | 215 us                                                 | 221 us: 1.03x slower                                                  |
| richards_super                   | 39.2 ms                                                | 40.4 ms: 1.03x slower                                                 |
| xml_etree_parse                  | 108 ms                                                 | 112 ms: 1.04x slower                                                  |
| sympy_integrate                  | 11.3 ms                                                | 11.8 ms: 1.04x slower                                                 |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 389 ms: 1.04x slower                                                  |
| spectral_norm                    | 76.5 ms                                                | 79.9 ms: 1.05x slower                                                 |
| 2to3                             | 179 ms                                                 | 187 ms: 1.05x slower                                                  |
| pathlib                          | 23.2 ms                                                | 24.3 ms: 1.05x slower                                                 |
| async_generators                 | 294 ms                                                 | 310 ms: 1.06x slower                                                  |
| pycparser                        | 701 ms                                                 | 741 ms: 1.06x slower                                                  |
| mako                             | 7.75 ms                                                | 8.21 ms: 1.06x slower                                                 |
| xml_etree_process                | 41.3 ms                                                | 43.9 ms: 1.06x slower                                                 |
| bench_thread_pool                | 503 us                                                 | 538 us: 1.07x slower                                                  |
| python_startup                   | 18.8 ms                                                | 20.2 ms: 1.07x slower                                                 |
| chaos                            | 41.1 ms                                                | 44.1 ms: 1.07x slower                                                 |
| sphinx                           | 602 ms                                                 | 647 ms: 1.08x slower                                                  |
| pprint_pformat                   | 1.10 sec                                               | 1.19 sec: 1.08x slower                                                |
| pprint_safe_repr                 | 541 ms                                                 | 586 ms: 1.08x slower                                                  |
| crypto_pyaes                     | 55.3 ms                                                | 60.1 ms: 1.09x slower                                                 |
| gc_traversal                     | 2.94 ms                                                | 3.20 ms: 1.09x slower                                                 |
| nqueens                          | 61.8 ms                                                | 67.5 ms: 1.09x slower                                                 |
| logging_simple                   | 3.56 us                                                | 3.96 us: 1.11x slower                                                 |
| logging_format                   | 3.85 us                                                | 4.29 us: 1.11x slower                                                 |
| python_startup_no_site           | 13.7 ms                                                | 15.3 ms: 1.11x slower                                                 |
| fannkuch                         | 279 ms                                                 | 311 ms: 1.12x slower                                                  |
| bpe_tokeniser                    | 3.26 sec                                               | 3.65 sec: 1.12x slower                                                |
| sympy_str                        | 146 ms                                                 | 164 ms: 1.13x slower                                                  |
| nbody                            | 73.6 ms                                                | 83.1 ms: 1.13x slower                                                 |
| sympy_sum                        | 75.1 ms                                                | 85.1 ms: 1.13x slower                                                 |
| docutils                         | 1.44 sec                                               | 1.64 sec: 1.14x slower                                                |
| telco                            | 4.84 ms                                                | 5.50 ms: 1.14x slower                                                 |
| scimark_lu                       | 75.9 ms                                                | 86.6 ms: 1.14x slower                                                 |
| xml_etree_generate               | 57.1 ms                                                | 65.2 ms: 1.14x slower                                                 |
| sympy_expand                     | 248 ms                                                 | 286 ms: 1.15x slower                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 1.39 ms: 1.16x slower                                                 |
| bench_mp_pool                    | 64.7 ms                                                | 75.5 ms: 1.17x slower                                                 |
| raytrace                         | 181 ms                                                 | 211 ms: 1.17x slower                                                  |
| typing_runtime_protocols         | 101 us                                                 | 120 us: 1.19x slower                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.89 us: 1.21x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 425 ms: 1.22x slower                                                  |
| thrift                           | 466 us                                                 | 571 us: 1.23x slower                                                  |
| django_template                  | 20.5 ms                                                | 25.5 ms: 1.25x slower                                                 |
| json_dumps                       | 6.47 ms                                                | 8.09 ms: 1.25x slower                                                 |
| json                             | 3.04 ms                                                | 3.83 ms: 1.26x slower                                                 |
| many_optionals                   | 409 us                                                 | 520 us: 1.27x slower                                                  |
| coverage                         | 46.2 ms                                                | 59.8 ms: 1.29x slower                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 180 ms: 1.30x slower                                                  |
| json_loads                       | 17.0 us                                                | 22.7 us: 1.33x slower                                                 |
| scimark_fft                      | 200 ms                                                 | 267 ms: 1.34x slower                                                  |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 4.19 ms: 1.40x slower                                                 |
| subparsers                       | 9.44 ms                                                | 15.9 ms: 1.69x slower                                                 |
| async_tree_eager_tg              | 47.4 ms                                                | 141 ms: 2.97x slower                                                  |
| logging_silent                   | 71.0 ns                                                | 413 ns: 5.82x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.05x slower                                                          |

Benchmark hidden because not significant (4): pylint, comprehensions, dask, asyncio_websockets
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.027x slower

# HPT report

- Reliability score: 93.26% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.07x