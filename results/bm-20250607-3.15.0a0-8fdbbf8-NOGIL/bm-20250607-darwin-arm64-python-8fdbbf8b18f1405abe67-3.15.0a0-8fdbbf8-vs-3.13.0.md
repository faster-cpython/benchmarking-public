# Results vs. 3.13.0

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: darwin-arm64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.068x slower
- HPT reliability: 99.74%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 233 ms: 1.31x slower                                                  |
| docutils       | 1.44 sec                                               | 1.59 sec: 1.10x slower                                                |
| html5lib       | 36.7 ms                                                | 34.6 ms: 1.06x faster                                                 |
| sphinx         | 602 ms                                                 | 678 ms: 1.13x slower                                                  |
| Geometric mean | (ref)                                                  | 1.11x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 179 ms: 1.61x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 333 ms: 1.53x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 327 ms: 1.53x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 323 ms: 1.48x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 344 ms: 1.48x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 146 ms: 1.36x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 197 ms: 1.36x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 164 ms: 1.29x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 147 ms: 1.14x faster                                                  |
| coroutines                       | 20.0 ms                                                | 18.0 ms: 1.11x faster                                                 |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 417 ms: 1.07x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 437 ms: 1.05x faster                                                  |
| asyncio_websockets               | 242 ms                                                 | 238 ms: 1.02x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 395 ms: 1.06x slower                                                  |
| async_generators                 | 294 ms                                                 | 320 ms: 1.09x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 401 ms: 1.15x slower                                                  |
| async_tree_eager                 | 69.9 ms                                                | 81.8 ms: 1.17x slower                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 163 ms: 1.18x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 127 ms: 2.68x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 49.1 ms: 1.14x faster                                                 |
| pidigits       | 284 ms                                                 | 281 ms: 1.01x faster                                                  |
| nbody          | 73.6 ms                                                | 95.0 ms: 1.29x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.20 ms: 1.20x faster                                                 |
| regex_dna      | 149 ms                                                 | 145 ms: 1.03x faster                                                  |
| regex_compile  | 78.3 ms                                                | 83.6 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_iterparse  | 74.2 ms                                                | 69.0 ms: 1.07x faster                                                 |
| unpickle_pure_python | 165 us                                                 | 167 us: 1.01x slower                                                  |
| xml_etree_parse      | 108 ms                                                 | 111 ms: 1.02x slower                                                  |
| pickle_pure_python   | 215 us                                                 | 237 us: 1.10x slower                                                  |
| xml_etree_process    | 41.3 ms                                                | 49.8 ms: 1.20x slower                                                 |
| xml_etree_generate   | 57.1 ms                                                | 72.1 ms: 1.26x slower                                                 |
| json_dumps           | 6.47 ms                                                | 8.41 ms: 1.30x slower                                                 |
| json_loads           | 17.0 us                                                | 24.6 us: 1.44x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.13x slower                                                          |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 21.0 ms: 1.11x slower                                                 |
| python_startup_no_site | 13.7 ms                                                | 16.0 ms: 1.16x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.14x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 18.3 ms: 1.08x slower                                                 |
| genshi_xml      | 34.1 ms                                                | 39.4 ms: 1.16x slower                                                 |
| django_template | 20.5 ms                                                | 28.2 ms: 1.38x slower                                                 |
| mako            | 7.75 ms                                                | 11.0 ms: 1.42x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.25x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| gc_traversal                     | 2.94 ms                                                | 1.42 ms: 2.07x faster                                                 |
| async_tree_memoization_tg        | 288 ms                                                 | 179 ms: 1.61x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 333 ms: 1.53x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 327 ms: 1.53x faster                                                  |
| mdp                              | 1.50 sec                                               | 989 ms: 1.52x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 323 ms: 1.48x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 344 ms: 1.48x faster                                                  |
| go                               | 117 ms                                                 | 84.3 ms: 1.38x faster                                                 |
| create_gc_cycles                 | 1.19 ms                                                | 861 us: 1.38x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 146 ms: 1.36x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 197 ms: 1.36x faster                                                  |
| generators                       | 31.9 ms                                                | 23.9 ms: 1.34x faster                                                 |
| async_tree_none                  | 212 ms                                                 | 164 ms: 1.29x faster                                                  |
| deepcopy_memo                    | 27.4 us                                                | 22.2 us: 1.24x faster                                                 |
| regex_effbot                     | 2.63 ms                                                | 2.20 ms: 1.20x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 147 ms: 1.14x faster                                                  |
| float                            | 55.8 ms                                                | 49.1 ms: 1.14x faster                                                 |
| coroutines                       | 20.0 ms                                                | 18.0 ms: 1.11x faster                                                 |
| pyflate                          | 352 ms                                                 | 317 ms: 1.11x faster                                                  |
| deepcopy                         | 236 us                                                 | 214 us: 1.11x faster                                                  |
| scimark_sor                      | 106 ms                                                 | 96.6 ms: 1.09x faster                                                 |
| xml_etree_iterparse              | 74.2 ms                                                | 69.0 ms: 1.07x faster                                                 |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 417 ms: 1.07x faster                                                  |
| html5lib                         | 36.7 ms                                                | 34.6 ms: 1.06x faster                                                 |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 437 ms: 1.05x faster                                                  |
| regex_dna                        | 149 ms                                                 | 145 ms: 1.03x faster                                                  |
| asyncio_websockets               | 242 ms                                                 | 238 ms: 1.02x faster                                                  |
| pidigits                         | 284 ms                                                 | 281 ms: 1.01x faster                                                  |
| connected_components             | 319 ms                                                 | 322 ms: 1.01x slower                                                  |
| unpickle_pure_python             | 165 us                                                 | 167 us: 1.01x slower                                                  |
| k_core                           | 1.61 sec                                               | 1.64 sec: 1.02x slower                                                |
| deltablue                        | 2.65 ms                                                | 2.70 ms: 1.02x slower                                                 |
| hexiom                           | 4.87 ms                                                | 4.97 ms: 1.02x slower                                                 |
| xml_etree_parse                  | 108 ms                                                 | 111 ms: 1.02x slower                                                  |
| pycparser                        | 701 ms                                                 | 736 ms: 1.05x slower                                                  |
| pylint                           | 180 ms                                                 | 189 ms: 1.05x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 395 ms: 1.06x slower                                                  |
| pathlib                          | 23.2 ms                                                | 24.7 ms: 1.07x slower                                                 |
| regex_compile                    | 78.3 ms                                                | 83.6 ms: 1.07x slower                                                 |
| sqlite_synth                     | 1.55 us                                                | 1.67 us: 1.07x slower                                                 |
| genshi_text                      | 16.9 ms                                                | 18.3 ms: 1.08x slower                                                 |
| async_generators                 | 294 ms                                                 | 320 ms: 1.09x slower                                                  |
| deepcopy_reduce                  | 2.09 us                                                | 2.29 us: 1.09x slower                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 55.2 ms: 1.09x slower                                                 |
| docutils                         | 1.44 sec                                               | 1.59 sec: 1.10x slower                                                |
| pickle_pure_python               | 215 us                                                 | 237 us: 1.10x slower                                                  |
| python_startup                   | 18.8 ms                                                | 21.0 ms: 1.11x slower                                                 |
| bpe_tokeniser                    | 3.26 sec                                               | 3.64 sec: 1.12x slower                                                |
| meteor_contest                   | 74.0 ms                                                | 83.2 ms: 1.13x slower                                                 |
| sphinx                           | 602 ms                                                 | 678 ms: 1.13x slower                                                  |
| richards                         | 36.2 ms                                                | 40.7 ms: 1.13x slower                                                 |
| sympy_integrate                  | 11.3 ms                                                | 12.9 ms: 1.15x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 401 ms: 1.15x slower                                                  |
| genshi_xml                       | 34.1 ms                                                | 39.4 ms: 1.16x slower                                                 |
| python_startup_no_site           | 13.7 ms                                                | 16.0 ms: 1.16x slower                                                 |
| async_tree_eager                 | 69.9 ms                                                | 81.8 ms: 1.17x slower                                                 |
| nqueens                          | 61.8 ms                                                | 72.5 ms: 1.17x slower                                                 |
| spectral_norm                    | 76.5 ms                                                | 90.2 ms: 1.18x slower                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 163 ms: 1.18x slower                                                  |
| richards_super                   | 39.2 ms                                                | 46.7 ms: 1.19x slower                                                 |
| chaos                            | 41.1 ms                                                | 49.2 ms: 1.20x slower                                                 |
| xml_etree_process                | 41.3 ms                                                | 49.8 ms: 1.20x slower                                                 |
| bench_mp_pool                    | 64.7 ms                                                | 78.6 ms: 1.21x slower                                                 |
| logging_simple                   | 3.56 us                                                | 4.36 us: 1.23x slower                                                 |
| logging_format                   | 3.85 us                                                | 4.79 us: 1.24x slower                                                 |
| sympy_sum                        | 75.1 ms                                                | 93.9 ms: 1.25x slower                                                 |
| sympy_str                        | 146 ms                                                 | 183 ms: 1.26x slower                                                  |
| telco                            | 4.84 ms                                                | 6.11 ms: 1.26x slower                                                 |
| xml_etree_generate               | 57.1 ms                                                | 72.1 ms: 1.26x slower                                                 |
| fannkuch                         | 279 ms                                                 | 354 ms: 1.27x slower                                                  |
| pprint_safe_repr                 | 541 ms                                                 | 687 ms: 1.27x slower                                                  |
| pprint_pformat                   | 1.10 sec                                               | 1.40 sec: 1.27x slower                                                |
| comprehensions                   | 12.0 us                                                | 15.3 us: 1.28x slower                                                 |
| crypto_pyaes                     | 55.3 ms                                                | 70.7 ms: 1.28x slower                                                 |
| nbody                            | 73.6 ms                                                | 95.0 ms: 1.29x slower                                                 |
| raytrace                         | 181 ms                                                 | 235 ms: 1.30x slower                                                  |
| json_dumps                       | 6.47 ms                                                | 8.41 ms: 1.30x slower                                                 |
| 2to3                             | 179 ms                                                 | 233 ms: 1.31x slower                                                  |
| sympy_expand                     | 248 ms                                                 | 324 ms: 1.31x slower                                                  |
| scimark_lu                       | 75.9 ms                                                | 100 ms: 1.32x slower                                                  |
| json                             | 3.04 ms                                                | 4.08 ms: 1.34x slower                                                 |
| many_optionals                   | 409 us                                                 | 557 us: 1.36x slower                                                  |
| thrift                           | 466 us                                                 | 635 us: 1.36x slower                                                  |
| django_template                  | 20.5 ms                                                | 28.2 ms: 1.38x slower                                                 |
| typing_runtime_protocols         | 101 us                                                 | 140 us: 1.39x slower                                                  |
| mako                             | 7.75 ms                                                | 11.0 ms: 1.42x slower                                                 |
| scimark_fft                      | 200 ms                                                 | 287 ms: 1.44x slower                                                  |
| json_loads                       | 17.0 us                                                | 24.6 us: 1.44x slower                                                 |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 4.53 ms: 1.52x slower                                                 |
| bench_thread_pool                | 503 us                                                 | 777 us: 1.54x slower                                                  |
| coverage                         | 46.2 ms                                                | 75.7 ms: 1.64x slower                                                 |
| subparsers                       | 9.44 ms                                                | 16.9 ms: 1.79x slower                                                 |
| async_tree_eager_tg              | 47.4 ms                                                | 127 ms: 2.68x slower                                                  |
| logging_silent                   | 71.0 ns                                                | 444 ns: 6.25x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.09x slower                                                          |

Benchmark hidden because not significant (4): dulwich_log, tomli_loads, regex_v8, shortest_path
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250607-3.15.0a0-8fdbbf8-NOGIL/bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.068x slower

# HPT report

- Reliability score: 99.74% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.26x