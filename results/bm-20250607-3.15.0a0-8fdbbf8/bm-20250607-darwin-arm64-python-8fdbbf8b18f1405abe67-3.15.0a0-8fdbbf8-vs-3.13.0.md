# Results vs. 3.13.0

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: darwin-arm64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.087x slower
- HPT reliability: 96.36%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 217 ms: 1.22x slower                                                  |
| docutils       | 1.44 sec                                               | 1.59 sec: 1.10x slower                                                |
| html5lib       | 36.7 ms                                                | 33.4 ms: 1.10x faster                                                 |
| sphinx         | 602 ms                                                 | 651 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.07x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 201 ms: 1.43x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 388 ms: 1.32x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 204 ms: 1.31x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 386 ms: 1.30x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 399 ms: 1.27x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 173 ms: 1.22x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 399 ms: 1.20x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 166 ms: 1.19x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 147 ms: 1.14x faster                                                  |
| coroutines                       | 20.0 ms                                                | 18.3 ms: 1.10x faster                                                 |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 455 ms: 1.01x faster                                                  |
| async_tree_eager                 | 69.9 ms                                                | 71.0 ms: 1.02x slower                                                 |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 391 ms: 1.05x slower                                                  |
| async_generators                 | 294 ms                                                 | 314 ms: 1.07x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 426 ms: 1.23x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 179 ms: 1.30x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 140 ms: 2.96x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 51.1 ms: 1.09x faster                                                 |
| pidigits       | 284 ms                                                 | 284 ms: 1.00x slower                                                  |
| nbody          | 73.6 ms                                                | 77.4 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.19 ms: 1.20x faster                                                 |
| regex_compile  | 78.3 ms                                                | 74.5 ms: 1.05x faster                                                 |
| regex_dna      | 149 ms                                                 | 145 ms: 1.03x faster                                                  |
| regex_v8       | 17.0 ms                                                | 17.3 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.39 sec: 1.13x faster                                                |
| unpickle_pure_python | 165 us                                                 | 158 us: 1.05x faster                                                  |
| xml_etree_iterparse  | 74.2 ms                                                | 76.5 ms: 1.03x slower                                                 |
| pickle_pure_python   | 215 us                                                 | 221 us: 1.03x slower                                                  |
| xml_etree_parse      | 108 ms                                                 | 112 ms: 1.04x slower                                                  |
| xml_etree_process    | 41.3 ms                                                | 43.9 ms: 1.06x slower                                                 |
| xml_etree_generate   | 57.1 ms                                                | 64.9 ms: 1.14x slower                                                 |
| json_dumps           | 6.47 ms                                                | 8.13 ms: 1.26x slower                                                 |
| json_loads           | 17.0 us                                                | 22.9 us: 1.35x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.07x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 19.3 ms: 1.03x slower                                                 |
| python_startup_no_site | 13.7 ms                                                | 14.4 ms: 1.05x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.04x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 15.6 ms: 1.09x faster                                                 |
| genshi_xml      | 34.1 ms                                                | 33.2 ms: 1.02x faster                                                 |
| mako            | 7.75 ms                                                | 8.27 ms: 1.07x slower                                                 |
| django_template | 20.5 ms                                                | 25.7 ms: 1.26x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 889 ms: 1.69x faster                                                  |
| go                               | 117 ms                                                 | 77.5 ms: 1.51x faster                                                 |
| async_tree_memoization_tg        | 288 ms                                                 | 201 ms: 1.43x faster                                                  |
| deepcopy_memo                    | 27.4 us                                                | 19.4 us: 1.41x faster                                                 |
| generators                       | 31.9 ms                                                | 23.2 ms: 1.38x faster                                                 |
| async_tree_eager_io              | 511 ms                                                 | 388 ms: 1.32x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 204 ms: 1.31x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 386 ms: 1.30x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 399 ms: 1.27x faster                                                  |
| deepcopy                         | 236 us                                                 | 187 us: 1.26x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 173 ms: 1.22x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.19 ms: 1.20x faster                                                 |
| async_tree_eager_io_tg           | 479 ms                                                 | 399 ms: 1.20x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 166 ms: 1.19x faster                                                  |
| scimark_sor                      | 106 ms                                                 | 89.8 ms: 1.18x faster                                                 |
| pyflate                          | 352 ms                                                 | 305 ms: 1.15x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 147 ms: 1.14x faster                                                  |
| tomli_loads                      | 1.57 sec                                               | 1.39 sec: 1.13x faster                                                |
| html5lib                         | 36.7 ms                                                | 33.4 ms: 1.10x faster                                                 |
| coroutines                       | 20.0 ms                                                | 18.3 ms: 1.10x faster                                                 |
| float                            | 55.8 ms                                                | 51.1 ms: 1.09x faster                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 46.3 ms: 1.09x faster                                                 |
| genshi_text                      | 16.9 ms                                                | 15.6 ms: 1.09x faster                                                 |
| hexiom                           | 4.87 ms                                                | 4.56 ms: 1.07x faster                                                 |
| dulwich_log                      | 28.7 ms                                                | 27.1 ms: 1.06x faster                                                 |
| connected_components             | 319 ms                                                 | 301 ms: 1.06x faster                                                  |
| regex_compile                    | 78.3 ms                                                | 74.5 ms: 1.05x faster                                                 |
| deepcopy_reduce                  | 2.09 us                                                | 1.99 us: 1.05x faster                                                 |
| unpickle_pure_python             | 165 us                                                 | 158 us: 1.05x faster                                                  |
| shortest_path                    | 345 ms                                                 | 329 ms: 1.05x faster                                                  |
| k_core                           | 1.61 sec                                               | 1.54 sec: 1.05x faster                                                |
| regex_dna                        | 149 ms                                                 | 145 ms: 1.03x faster                                                  |
| genshi_xml                       | 34.1 ms                                                | 33.2 ms: 1.02x faster                                                 |
| deltablue                        | 2.65 ms                                                | 2.61 ms: 1.01x faster                                                 |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 455 ms: 1.01x faster                                                  |
| pidigits                         | 284 ms                                                 | 284 ms: 1.00x slower                                                  |
| async_tree_eager                 | 69.9 ms                                                | 71.0 ms: 1.02x slower                                                 |
| regex_v8                         | 17.0 ms                                                | 17.3 ms: 1.02x slower                                                 |
| python_startup                   | 18.8 ms                                                | 19.3 ms: 1.03x slower                                                 |
| xml_etree_iterparse              | 74.2 ms                                                | 76.5 ms: 1.03x slower                                                 |
| pickle_pure_python               | 215 us                                                 | 221 us: 1.03x slower                                                  |
| meteor_contest                   | 74.0 ms                                                | 76.3 ms: 1.03x slower                                                 |
| richards_super                   | 39.2 ms                                                | 40.7 ms: 1.04x slower                                                 |
| xml_etree_parse                  | 108 ms                                                 | 112 ms: 1.04x slower                                                  |
| sympy_integrate                  | 11.3 ms                                                | 11.8 ms: 1.04x slower                                                 |
| pathlib                          | 23.2 ms                                                | 24.3 ms: 1.05x slower                                                 |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 391 ms: 1.05x slower                                                  |
| python_startup_no_site           | 13.7 ms                                                | 14.4 ms: 1.05x slower                                                 |
| nbody                            | 73.6 ms                                                | 77.4 ms: 1.05x slower                                                 |
| spectral_norm                    | 76.5 ms                                                | 81.0 ms: 1.06x slower                                                 |
| pycparser                        | 701 ms                                                 | 745 ms: 1.06x slower                                                  |
| xml_etree_process                | 41.3 ms                                                | 43.9 ms: 1.06x slower                                                 |
| mako                             | 7.75 ms                                                | 8.27 ms: 1.07x slower                                                 |
| async_generators                 | 294 ms                                                 | 314 ms: 1.07x slower                                                  |
| bench_thread_pool                | 503 us                                                 | 539 us: 1.07x slower                                                  |
| chaos                            | 41.1 ms                                                | 44.4 ms: 1.08x slower                                                 |
| sphinx                           | 602 ms                                                 | 651 ms: 1.08x slower                                                  |
| pprint_pformat                   | 1.10 sec                                               | 1.20 sec: 1.09x slower                                                |
| pprint_safe_repr                 | 541 ms                                                 | 589 ms: 1.09x slower                                                  |
| gc_traversal                     | 2.94 ms                                                | 3.21 ms: 1.09x slower                                                 |
| crypto_pyaes                     | 55.3 ms                                                | 60.7 ms: 1.10x slower                                                 |
| nqueens                          | 61.8 ms                                                | 67.9 ms: 1.10x slower                                                 |
| docutils                         | 1.44 sec                                               | 1.59 sec: 1.10x slower                                                |
| dask                             | 771 ms                                                 | 853 ms: 1.11x slower                                                  |
| logging_simple                   | 3.56 us                                                | 3.94 us: 1.11x slower                                                 |
| fannkuch                         | 279 ms                                                 | 310 ms: 1.11x slower                                                  |
| logging_format                   | 3.85 us                                                | 4.28 us: 1.11x slower                                                 |
| bpe_tokeniser                    | 3.26 sec                                               | 3.66 sec: 1.12x slower                                                |
| sympy_str                        | 146 ms                                                 | 165 ms: 1.13x slower                                                  |
| sympy_sum                        | 75.1 ms                                                | 85.2 ms: 1.14x slower                                                 |
| xml_etree_generate               | 57.1 ms                                                | 64.9 ms: 1.14x slower                                                 |
| telco                            | 4.84 ms                                                | 5.55 ms: 1.15x slower                                                 |
| scimark_lu                       | 75.9 ms                                                | 87.6 ms: 1.15x slower                                                 |
| sympy_expand                     | 248 ms                                                 | 286 ms: 1.16x slower                                                  |
| raytrace                         | 181 ms                                                 | 210 ms: 1.16x slower                                                  |
| bench_mp_pool                    | 64.7 ms                                                | 75.4 ms: 1.16x slower                                                 |
| create_gc_cycles                 | 1.19 ms                                                | 1.42 ms: 1.19x slower                                                 |
| typing_runtime_protocols         | 101 us                                                 | 121 us: 1.20x slower                                                  |
| 2to3                             | 179 ms                                                 | 217 ms: 1.22x slower                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.90 us: 1.22x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 426 ms: 1.23x slower                                                  |
| json_dumps                       | 6.47 ms                                                | 8.13 ms: 1.26x slower                                                 |
| django_template                  | 20.5 ms                                                | 25.7 ms: 1.26x slower                                                 |
| json                             | 3.04 ms                                                | 3.84 ms: 1.26x slower                                                 |
| many_optionals                   | 409 us                                                 | 524 us: 1.28x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 179 ms: 1.30x slower                                                  |
| scimark_fft                      | 200 ms                                                 | 262 ms: 1.31x slower                                                  |
| json_loads                       | 17.0 us                                                | 22.9 us: 1.35x slower                                                 |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 4.03 ms: 1.35x slower                                                 |
| subparsers                       | 9.44 ms                                                | 16.1 ms: 1.70x slower                                                 |
| async_tree_eager_tg              | 47.4 ms                                                | 140 ms: 2.96x slower                                                  |
| logging_silent                   | 71.0 ns                                                | 421 ns: 5.93x slower                                                  |
| coverage                         | 46.2 ms                                                | 306 ms: 6.62x slower                                                  |
| thrift                           | 466 us                                                 | 44.1 ms: 94.71x slower                                                |
| Geometric mean                   | (ref)                                                  | 1.11x slower                                                          |

Benchmark hidden because not significant (5): pylint, richards, comprehensions, asyncio_websockets, async_tree_cpu_io_mixed_tg
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.087x slower

# HPT report

- Reliability score: 96.36% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.08x