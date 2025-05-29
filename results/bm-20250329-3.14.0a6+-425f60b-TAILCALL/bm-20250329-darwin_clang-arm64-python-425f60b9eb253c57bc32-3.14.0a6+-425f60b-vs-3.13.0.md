# Results vs. 3.13.0

- fork: python
- ref: 425f60b9eb253c57bc32
- machine: darwin-arm64
- commit hash: 425f60b
- commit date: 2025-03-29
- overall geometric mean: 1.159x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-darwin-arm64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 151 ms: 1.18x faster                                                   |
| docutils       | 1.44 sec                                               | 1.38 sec: 1.05x faster                                                 |
| html5lib       | 36.7 ms                                                | 29.1 ms: 1.26x faster                                                  |
| sphinx         | 602 ms                                                 | 553 ms: 1.09x faster                                                   |
| Geometric mean | (ref)                                                  | 1.14x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-darwin-arm64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 181 ms: 1.59x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 339 ms: 1.51x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 339 ms: 1.50x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 179 ms: 1.49x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 335 ms: 1.49x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 150 ms: 1.41x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 346 ms: 1.38x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 144 ms: 1.37x faster                                                   |
| coroutines                       | 20.0 ms                                                | 14.7 ms: 1.36x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 131 ms: 1.28x faster                                                   |
| async_tree_eager                 | 69.9 ms                                                | 56.6 ms: 1.24x faster                                                  |
| async_generators                 | 294 ms                                                 | 239 ms: 1.23x faster                                                   |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 399 ms: 1.15x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 399 ms: 1.12x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 345 ms: 1.08x faster                                                   |
| asyncio_websockets               | 242 ms                                                 | 242 ms: 1.00x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 377 ms: 1.09x slower                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 161 ms: 1.17x slower                                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 122 ms: 2.57x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.18x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-darwin-arm64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 43.2 ms: 1.29x faster                                                  |
| nbody          | 73.6 ms                                                | 61.6 ms: 1.19x faster                                                  |
| pidigits       | 284 ms                                                 | 280 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.16x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-darwin-arm64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 78.3 ms                                                | 62.9 ms: 1.25x faster                                                  |
| regex_effbot   | 2.63 ms                                                | 2.37 ms: 1.11x faster                                                  |
| regex_v8       | 17.0 ms                                                | 16.6 ms: 1.02x faster                                                  |
| regex_dna      | 149 ms                                                 | 148 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-darwin-arm64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.17 sec: 1.33x faster                                                 |
| unpickle_pure_python | 165 us                                                 | 128 us: 1.29x faster                                                   |
| xml_etree_process    | 41.3 ms                                                | 34.8 ms: 1.19x faster                                                  |
| xml_etree_generate   | 57.1 ms                                                | 48.9 ms: 1.17x faster                                                  |
| pickle_pure_python   | 215 us                                                 | 186 us: 1.15x faster                                                   |
| xml_etree_parse      | 108 ms                                                 | 98.3 ms: 1.10x faster                                                  |
| xml_etree_iterparse  | 74.2 ms                                                | 69.9 ms: 1.06x faster                                                  |
| json_loads           | 17.0 us                                                | 17.8 us: 1.05x slower                                                  |
| json_dumps           | 6.47 ms                                                | 7.21 ms: 1.12x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-darwin-arm64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 19.3 ms: 1.03x slower                                                  |
| python_startup_no_site | 13.7 ms                                                | 14.9 ms: 1.09x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-darwin-arm64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 12.7 ms: 1.33x faster                                                  |
| genshi_xml      | 34.1 ms                                                | 27.2 ms: 1.25x faster                                                  |
| django_template | 20.5 ms                                                | 19.4 ms: 1.06x faster                                                  |
| mako            | 7.75 ms                                                | 7.35 ms: 1.05x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.17x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-darwin-arm64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 690 ms: 2.17x faster                                                   |
| generators                       | 31.9 ms                                                | 17.8 ms: 1.79x faster                                                  |
| deepcopy_memo                    | 27.4 us                                                | 16.4 us: 1.67x faster                                                  |
| deepcopy                         | 236 us                                                 | 142 us: 1.67x faster                                                   |
| go                               | 117 ms                                                 | 72.6 ms: 1.61x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 181 ms: 1.59x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 339 ms: 1.51x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 339 ms: 1.50x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 179 ms: 1.49x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 335 ms: 1.49x faster                                                   |
| scimark_sor                      | 106 ms                                                 | 71.8 ms: 1.47x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 150 ms: 1.41x faster                                                   |
| deepcopy_reduce                  | 2.09 us                                                | 1.50 us: 1.40x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 346 ms: 1.38x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 144 ms: 1.37x faster                                                   |
| coroutines                       | 20.0 ms                                                | 14.7 ms: 1.36x faster                                                  |
| tomli_loads                      | 1.57 sec                                               | 1.17 sec: 1.33x faster                                                 |
| genshi_text                      | 16.9 ms                                                | 12.7 ms: 1.33x faster                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 38.8 ms: 1.30x faster                                                  |
| float                            | 55.8 ms                                                | 43.2 ms: 1.29x faster                                                  |
| unpickle_pure_python             | 165 us                                                 | 128 us: 1.29x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 131 ms: 1.28x faster                                                   |
| hexiom                           | 4.87 ms                                                | 3.80 ms: 1.28x faster                                                  |
| pyflate                          | 352 ms                                                 | 276 ms: 1.28x faster                                                   |
| deltablue                        | 2.65 ms                                                | 2.08 ms: 1.27x faster                                                  |
| html5lib                         | 36.7 ms                                                | 29.1 ms: 1.26x faster                                                  |
| genshi_xml                       | 34.1 ms                                                | 27.2 ms: 1.25x faster                                                  |
| richards                         | 36.2 ms                                                | 29.0 ms: 1.25x faster                                                  |
| logging_silent                   | 71.0 ns                                                | 56.9 ns: 1.25x faster                                                  |
| regex_compile                    | 78.3 ms                                                | 62.9 ms: 1.25x faster                                                  |
| async_tree_eager                 | 69.9 ms                                                | 56.6 ms: 1.24x faster                                                  |
| async_generators                 | 294 ms                                                 | 239 ms: 1.23x faster                                                   |
| spectral_norm                    | 76.5 ms                                                | 62.6 ms: 1.22x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 23.5 ms: 1.22x faster                                                  |
| richards_super                   | 39.2 ms                                                | 32.6 ms: 1.20x faster                                                  |
| logging_simple                   | 3.56 us                                                | 2.96 us: 1.20x faster                                                  |
| nbody                            | 73.6 ms                                                | 61.6 ms: 1.19x faster                                                  |
| pylint                           | 180 ms                                                 | 151 ms: 1.19x faster                                                   |
| xml_etree_process                | 41.3 ms                                                | 34.8 ms: 1.19x faster                                                  |
| logging_format                   | 3.85 us                                                | 3.25 us: 1.18x faster                                                  |
| pprint_pformat                   | 1.10 sec                                               | 931 ms: 1.18x faster                                                   |
| nqueens                          | 61.8 ms                                                | 52.4 ms: 1.18x faster                                                  |
| 2to3                             | 179 ms                                                 | 151 ms: 1.18x faster                                                   |
| comprehensions                   | 12.0 us                                                | 10.2 us: 1.18x faster                                                  |
| raytrace                         | 181 ms                                                 | 155 ms: 1.17x faster                                                   |
| xml_etree_generate               | 57.1 ms                                                | 48.9 ms: 1.17x faster                                                  |
| chaos                            | 41.1 ms                                                | 35.3 ms: 1.16x faster                                                  |
| pprint_safe_repr                 | 541 ms                                                 | 466 ms: 1.16x faster                                                   |
| bpe_tokeniser                    | 3.26 sec                                               | 2.81 sec: 1.16x faster                                                 |
| typing_runtime_protocols         | 101 us                                                 | 87.0 us: 1.16x faster                                                  |
| pickle_pure_python               | 215 us                                                 | 186 us: 1.15x faster                                                   |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 399 ms: 1.15x faster                                                   |
| scimark_lu                       | 75.9 ms                                                | 66.1 ms: 1.15x faster                                                  |
| sympy_integrate                  | 11.3 ms                                                | 9.94 ms: 1.14x faster                                                  |
| sympy_expand                     | 248 ms                                                 | 220 ms: 1.12x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 399 ms: 1.12x faster                                                   |
| crypto_pyaes                     | 55.3 ms                                                | 49.3 ms: 1.12x faster                                                  |
| pycparser                        | 701 ms                                                 | 627 ms: 1.12x faster                                                   |
| sympy_str                        | 146 ms                                                 | 130 ms: 1.12x faster                                                   |
| scimark_fft                      | 200 ms                                                 | 180 ms: 1.11x faster                                                   |
| fannkuch                         | 279 ms                                                 | 251 ms: 1.11x faster                                                   |
| regex_effbot                     | 2.63 ms                                                | 2.37 ms: 1.11x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 98.3 ms: 1.10x faster                                                  |
| bench_thread_pool                | 503 us                                                 | 460 us: 1.09x faster                                                   |
| sphinx                           | 602 ms                                                 | 553 ms: 1.09x faster                                                   |
| telco                            | 4.84 ms                                                | 4.46 ms: 1.08x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 345 ms: 1.08x faster                                                   |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.22 ms: 1.08x faster                                                  |
| k_core                           | 1.61 sec                                               | 1.50 sec: 1.08x faster                                                 |
| sympy_sum                        | 75.1 ms                                                | 69.8 ms: 1.08x faster                                                  |
| sqlalchemy_declarative           | 59.0 ms                                                | 55.0 ms: 1.07x faster                                                  |
| bench_mp_pool                    | 64.7 ms                                                | 60.6 ms: 1.07x faster                                                  |
| connected_components             | 319 ms                                                 | 300 ms: 1.06x faster                                                   |
| xml_etree_iterparse              | 74.2 ms                                                | 69.9 ms: 1.06x faster                                                  |
| django_template                  | 20.5 ms                                                | 19.4 ms: 1.06x faster                                                  |
| shortest_path                    | 345 ms                                                 | 327 ms: 1.06x faster                                                   |
| mako                             | 7.75 ms                                                | 7.35 ms: 1.05x faster                                                  |
| meteor_contest                   | 74.0 ms                                                | 70.2 ms: 1.05x faster                                                  |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 2.84 ms: 1.05x faster                                                  |
| docutils                         | 1.44 sec                                               | 1.38 sec: 1.05x faster                                                 |
| coverage                         | 46.2 ms                                                | 44.7 ms: 1.04x faster                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.52 us: 1.03x faster                                                  |
| regex_v8                         | 17.0 ms                                                | 16.6 ms: 1.02x faster                                                  |
| pidigits                         | 284 ms                                                 | 280 ms: 1.01x faster                                                   |
| regex_dna                        | 149 ms                                                 | 148 ms: 1.01x faster                                                   |
| asyncio_websockets               | 242 ms                                                 | 242 ms: 1.00x faster                                                   |
| python_startup                   | 18.8 ms                                                | 19.3 ms: 1.03x slower                                                  |
| json_loads                       | 17.0 us                                                | 17.8 us: 1.05x slower                                                  |
| many_optionals                   | 409 us                                                 | 429 us: 1.05x slower                                                   |
| gc_traversal                     | 2.94 ms                                                | 3.10 ms: 1.06x slower                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 1.28 ms: 1.07x slower                                                  |
| python_startup_no_site           | 13.7 ms                                                | 14.9 ms: 1.09x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 377 ms: 1.09x slower                                                   |
| json_dumps                       | 6.47 ms                                                | 7.21 ms: 1.12x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 161 ms: 1.17x slower                                                   |
| subparsers                       | 9.44 ms                                                | 11.7 ms: 1.24x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 122 ms: 2.57x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.16x faster                                                           |

Benchmark hidden because not significant (2): json, pathlib
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250329-3.14.0a6+-425f60b-CLANG/bm-20250329-darwin-arm64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.159x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: 1.09x