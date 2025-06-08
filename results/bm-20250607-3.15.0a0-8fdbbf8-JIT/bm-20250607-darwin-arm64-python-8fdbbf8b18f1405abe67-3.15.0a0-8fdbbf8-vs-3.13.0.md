# Results vs. 3.13.0

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: darwin-arm64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.098x slower
- HPT reliability: 98.05%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 192 ms: 1.08x slower                                                  |
| docutils       | 1.44 sec                                               | 1.63 sec: 1.13x slower                                                |
| html5lib       | 36.7 ms                                                | 33.3 ms: 1.10x faster                                                 |
| sphinx         | 602 ms                                                 | 658 ms: 1.09x slower                                                  |
| Geometric mean | (ref)                                                  | 1.05x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 202 ms: 1.42x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 388 ms: 1.32x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 206 ms: 1.30x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 389 ms: 1.29x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 402 ms: 1.26x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 173 ms: 1.22x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 398 ms: 1.20x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 167 ms: 1.19x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 150 ms: 1.12x faster                                                  |
| coroutines                       | 20.0 ms                                                | 18.3 ms: 1.10x faster                                                 |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 452 ms: 1.02x faster                                                  |
| async_tree_eager                 | 69.9 ms                                                | 72.6 ms: 1.04x slower                                                 |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 394 ms: 1.06x slower                                                  |
| async_generators                 | 294 ms                                                 | 326 ms: 1.11x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 430 ms: 1.24x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 180 ms: 1.31x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 141 ms: 2.97x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 51.1 ms: 1.09x faster                                                 |
| pidigits       | 284 ms                                                 | 284 ms: 1.00x slower                                                  |
| nbody          | 73.6 ms                                                | 77.6 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.22 ms: 1.19x faster                                                 |
| regex_compile  | 78.3 ms                                                | 76.2 ms: 1.03x faster                                                 |
| regex_dna      | 149 ms                                                 | 147 ms: 1.01x faster                                                  |
| regex_v8       | 17.0 ms                                                | 17.7 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 165 us                                                 | 150 us: 1.10x faster                                                  |
| tomli_loads          | 1.57 sec                                               | 1.44 sec: 1.09x faster                                                |
| xml_etree_parse      | 108 ms                                                 | 111 ms: 1.03x slower                                                  |
| pickle_pure_python   | 215 us                                                 | 221 us: 1.03x slower                                                  |
| xml_etree_iterparse  | 74.2 ms                                                | 76.9 ms: 1.04x slower                                                 |
| xml_etree_process    | 41.3 ms                                                | 43.1 ms: 1.04x slower                                                 |
| xml_etree_generate   | 57.1 ms                                                | 64.0 ms: 1.12x slower                                                 |
| json_dumps           | 6.47 ms                                                | 8.05 ms: 1.24x slower                                                 |
| json_loads           | 17.0 us                                                | 22.9 us: 1.34x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.07x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 19.4 ms: 1.03x slower                                                 |
| python_startup_no_site | 13.7 ms                                                | 14.5 ms: 1.06x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.04x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 15.8 ms: 1.07x faster                                                 |
| genshi_xml      | 34.1 ms                                                | 33.5 ms: 1.02x faster                                                 |
| mako            | 7.75 ms                                                | 8.15 ms: 1.05x slower                                                 |
| django_template | 20.5 ms                                                | 25.6 ms: 1.25x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 891 ms: 1.68x faster                                                  |
| go                               | 117 ms                                                 | 79.5 ms: 1.47x faster                                                 |
| deepcopy_memo                    | 27.4 us                                                | 19.3 us: 1.42x faster                                                 |
| async_tree_memoization_tg        | 288 ms                                                 | 202 ms: 1.42x faster                                                  |
| generators                       | 31.9 ms                                                | 23.1 ms: 1.38x faster                                                 |
| async_tree_eager_io              | 511 ms                                                 | 388 ms: 1.32x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 206 ms: 1.30x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 389 ms: 1.29x faster                                                  |
| deepcopy                         | 236 us                                                 | 186 us: 1.27x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 402 ms: 1.26x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 173 ms: 1.22x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 398 ms: 1.20x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 167 ms: 1.19x faster                                                  |
| scimark_sor                      | 106 ms                                                 | 89.0 ms: 1.19x faster                                                 |
| regex_effbot                     | 2.63 ms                                                | 2.22 ms: 1.19x faster                                                 |
| pyflate                          | 352 ms                                                 | 310 ms: 1.14x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 150 ms: 1.12x faster                                                  |
| unpickle_pure_python             | 165 us                                                 | 150 us: 1.10x faster                                                  |
| html5lib                         | 36.7 ms                                                | 33.3 ms: 1.10x faster                                                 |
| coroutines                       | 20.0 ms                                                | 18.3 ms: 1.10x faster                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 46.1 ms: 1.09x faster                                                 |
| tomli_loads                      | 1.57 sec                                               | 1.44 sec: 1.09x faster                                                |
| float                            | 55.8 ms                                                | 51.1 ms: 1.09x faster                                                 |
| genshi_text                      | 16.9 ms                                                | 15.8 ms: 1.07x faster                                                 |
| deepcopy_reduce                  | 2.09 us                                                | 1.98 us: 1.06x faster                                                 |
| dulwich_log                      | 28.7 ms                                                | 27.5 ms: 1.04x faster                                                 |
| hexiom                           | 4.87 ms                                                | 4.68 ms: 1.04x faster                                                 |
| regex_compile                    | 78.3 ms                                                | 76.2 ms: 1.03x faster                                                 |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 452 ms: 1.02x faster                                                  |
| k_core                           | 1.61 sec                                               | 1.59 sec: 1.02x faster                                                |
| genshi_xml                       | 34.1 ms                                                | 33.5 ms: 1.02x faster                                                 |
| shortest_path                    | 345 ms                                                 | 341 ms: 1.01x faster                                                  |
| regex_dna                        | 149 ms                                                 | 147 ms: 1.01x faster                                                  |
| connected_components             | 319 ms                                                 | 316 ms: 1.01x faster                                                  |
| pidigits                         | 284 ms                                                 | 284 ms: 1.00x slower                                                  |
| richards                         | 36.2 ms                                                | 36.3 ms: 1.01x slower                                                 |
| deltablue                        | 2.65 ms                                                | 2.69 ms: 1.02x slower                                                 |
| xml_etree_parse                  | 108 ms                                                 | 111 ms: 1.03x slower                                                  |
| pickle_pure_python               | 215 us                                                 | 221 us: 1.03x slower                                                  |
| python_startup                   | 18.8 ms                                                | 19.4 ms: 1.03x slower                                                 |
| xml_etree_iterparse              | 74.2 ms                                                | 76.9 ms: 1.04x slower                                                 |
| regex_v8                         | 17.0 ms                                                | 17.7 ms: 1.04x slower                                                 |
| async_tree_eager                 | 69.9 ms                                                | 72.6 ms: 1.04x slower                                                 |
| xml_etree_process                | 41.3 ms                                                | 43.1 ms: 1.04x slower                                                 |
| richards_super                   | 39.2 ms                                                | 41.0 ms: 1.05x slower                                                 |
| pathlib                          | 23.2 ms                                                | 24.3 ms: 1.05x slower                                                 |
| spectral_norm                    | 76.5 ms                                                | 80.3 ms: 1.05x slower                                                 |
| mako                             | 7.75 ms                                                | 8.15 ms: 1.05x slower                                                 |
| nbody                            | 73.6 ms                                                | 77.6 ms: 1.05x slower                                                 |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 394 ms: 1.06x slower                                                  |
| python_startup_no_site           | 13.7 ms                                                | 14.5 ms: 1.06x slower                                                 |
| sympy_integrate                  | 11.3 ms                                                | 12.1 ms: 1.07x slower                                                 |
| 2to3                             | 179 ms                                                 | 192 ms: 1.08x slower                                                  |
| bench_thread_pool                | 503 us                                                 | 543 us: 1.08x slower                                                  |
| gc_traversal                     | 2.94 ms                                                | 3.20 ms: 1.09x slower                                                 |
| sphinx                           | 602 ms                                                 | 658 ms: 1.09x slower                                                  |
| chaos                            | 41.1 ms                                                | 45.0 ms: 1.09x slower                                                 |
| crypto_pyaes                     | 55.3 ms                                                | 61.0 ms: 1.10x slower                                                 |
| nqueens                          | 61.8 ms                                                | 68.3 ms: 1.10x slower                                                 |
| dask                             | 771 ms                                                 | 854 ms: 1.11x slower                                                  |
| async_generators                 | 294 ms                                                 | 326 ms: 1.11x slower                                                  |
| meteor_contest                   | 74.0 ms                                                | 82.8 ms: 1.12x slower                                                 |
| comprehensions                   | 12.0 us                                                | 13.4 us: 1.12x slower                                                 |
| xml_etree_generate               | 57.1 ms                                                | 64.0 ms: 1.12x slower                                                 |
| docutils                         | 1.44 sec                                               | 1.63 sec: 1.13x slower                                                |
| pycparser                        | 701 ms                                                 | 797 ms: 1.14x slower                                                  |
| logging_format                   | 3.85 us                                                | 4.39 us: 1.14x slower                                                 |
| logging_simple                   | 3.56 us                                                | 4.06 us: 1.14x slower                                                 |
| sympy_sum                        | 75.1 ms                                                | 86.0 ms: 1.15x slower                                                 |
| sympy_str                        | 146 ms                                                 | 168 ms: 1.15x slower                                                  |
| bpe_tokeniser                    | 3.26 sec                                               | 3.76 sec: 1.15x slower                                                |
| scimark_lu                       | 75.9 ms                                                | 87.5 ms: 1.15x slower                                                 |
| bench_mp_pool                    | 64.7 ms                                                | 75.2 ms: 1.16x slower                                                 |
| telco                            | 4.84 ms                                                | 5.63 ms: 1.16x slower                                                 |
| create_gc_cycles                 | 1.19 ms                                                | 1.39 ms: 1.17x slower                                                 |
| raytrace                         | 181 ms                                                 | 212 ms: 1.17x slower                                                  |
| sympy_expand                     | 248 ms                                                 | 291 ms: 1.18x slower                                                  |
| typing_runtime_protocols         | 101 us                                                 | 123 us: 1.22x slower                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.92 us: 1.24x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 430 ms: 1.24x slower                                                  |
| scimark_fft                      | 200 ms                                                 | 248 ms: 1.24x slower                                                  |
| json_dumps                       | 6.47 ms                                                | 8.05 ms: 1.24x slower                                                 |
| django_template                  | 20.5 ms                                                | 25.6 ms: 1.25x slower                                                 |
| json                             | 3.04 ms                                                | 3.85 ms: 1.27x slower                                                 |
| pprint_safe_repr                 | 541 ms                                                 | 690 ms: 1.28x slower                                                  |
| fannkuch                         | 279 ms                                                 | 357 ms: 1.28x slower                                                  |
| pprint_pformat                   | 1.10 sec                                               | 1.42 sec: 1.29x slower                                                |
| many_optionals                   | 409 us                                                 | 533 us: 1.31x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 180 ms: 1.31x slower                                                  |
| json_loads                       | 17.0 us                                                | 22.9 us: 1.34x slower                                                 |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 4.20 ms: 1.41x slower                                                 |
| subparsers                       | 9.44 ms                                                | 16.1 ms: 1.70x slower                                                 |
| async_tree_eager_tg              | 47.4 ms                                                | 141 ms: 2.97x slower                                                  |
| logging_silent                   | 71.0 ns                                                | 414 ns: 5.83x slower                                                  |
| coverage                         | 46.2 ms                                                | 306 ms: 6.63x slower                                                  |
| thrift                           | 466 us                                                 | 44.1 ms: 94.71x slower                                                |
| Geometric mean                   | (ref)                                                  | 1.13x slower                                                          |

Benchmark hidden because not significant (3): pylint, asyncio_websockets, async_tree_cpu_io_mixed_tg
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.098x slower

# HPT report

- Reliability score: 98.05% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.10x