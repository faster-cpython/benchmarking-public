# Results vs. 3.13.0

- fork: python
- ref: 2fd09b011031f3c00c34
- machine: darwin-arm64
- commit hash: 2fd09b0
- commit date: 2025-05-24
- overall geometric mean: 1.068x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250524-darwin-arm64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 157 ms: 1.14x faster                                                  |
| docutils       | 1.44 sec                                               | 1.37 sec: 1.05x faster                                                |
| html5lib       | 36.7 ms                                                | 30.8 ms: 1.19x faster                                                 |
| sphinx         | 602 ms                                                 | 551 ms: 1.09x faster                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250524-darwin-arm64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 180 ms: 1.59x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 335 ms: 1.52x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 178 ms: 1.51x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 342 ms: 1.48x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 342 ms: 1.46x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 150 ms: 1.41x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 144 ms: 1.38x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 348 ms: 1.38x faster                                                  |
| coroutines                       | 20.0 ms                                                | 15.3 ms: 1.31x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 133 ms: 1.26x faster                                                  |
| async_tree_eager                 | 69.9 ms                                                | 57.2 ms: 1.22x faster                                                 |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 405 ms: 1.13x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 401 ms: 1.12x faster                                                  |
| async_generators                 | 294 ms                                                 | 263 ms: 1.11x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 351 ms: 1.06x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 383 ms: 1.10x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 160 ms: 1.16x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 120 ms: 2.53x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.17x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250524-darwin-arm64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 44.0 ms: 1.27x faster                                                 |
| pidigits       | 284 ms                                                 | 280 ms: 1.01x faster                                                  |
| nbody          | 73.6 ms                                                | 73.0 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250524-darwin-arm64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 78.3 ms                                                | 61.4 ms: 1.28x faster                                                 |
| regex_effbot   | 2.63 ms                                                | 2.13 ms: 1.24x faster                                                 |
| regex_v8       | 17.0 ms                                                | 15.3 ms: 1.11x faster                                                 |
| regex_dna      | 149 ms                                                 | 144 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.16x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250524-darwin-arm64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.18 sec: 1.32x faster                                                |
| unpickle_pure_python | 165 us                                                 | 130 us: 1.27x faster                                                  |
| xml_etree_process    | 41.3 ms                                                | 34.9 ms: 1.18x faster                                                 |
| xml_etree_generate   | 57.1 ms                                                | 49.2 ms: 1.16x faster                                                 |
| pickle_pure_python   | 215 us                                                 | 188 us: 1.14x faster                                                  |
| json_dumps           | 6.47 ms                                                | 6.08 ms: 1.06x faster                                                 |
| xml_etree_iterparse  | 74.2 ms                                                | 70.5 ms: 1.05x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 104 ms: 1.03x faster                                                  |
| json_loads           | 17.0 us                                                | 18.4 us: 1.08x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250524-darwin-arm64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 13.7 ms                                                | 14.6 ms: 1.06x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.04x slower                                                          |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250524-darwin-arm64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 12.8 ms: 1.32x faster                                                 |
| genshi_xml      | 34.1 ms                                                | 27.1 ms: 1.26x faster                                                 |
| mako            | 7.75 ms                                                | 7.20 ms: 1.08x faster                                                 |
| django_template | 20.5 ms                                                | 19.5 ms: 1.05x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.17x faster                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250524-darwin-arm64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 700 ms: 2.14x faster                                                  |
| generators                       | 31.9 ms                                                | 18.9 ms: 1.69x faster                                                 |
| deepcopy_memo                    | 27.4 us                                                | 16.5 us: 1.66x faster                                                 |
| go                               | 117 ms                                                 | 71.5 ms: 1.63x faster                                                 |
| deepcopy                         | 236 us                                                 | 145 us: 1.63x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 180 ms: 1.59x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 335 ms: 1.52x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 178 ms: 1.51x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 342 ms: 1.48x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 342 ms: 1.46x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 150 ms: 1.41x faster                                                  |
| scimark_sor                      | 106 ms                                                 | 75.9 ms: 1.39x faster                                                 |
| async_tree_none_tg               | 198 ms                                                 | 144 ms: 1.38x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 348 ms: 1.38x faster                                                  |
| deepcopy_reduce                  | 2.09 us                                                | 1.57 us: 1.33x faster                                                 |
| tomli_loads                      | 1.57 sec                                               | 1.18 sec: 1.32x faster                                                |
| genshi_text                      | 16.9 ms                                                | 12.8 ms: 1.32x faster                                                 |
| coroutines                       | 20.0 ms                                                | 15.3 ms: 1.31x faster                                                 |
| hexiom                           | 4.87 ms                                                | 3.75 ms: 1.30x faster                                                 |
| deltablue                        | 2.65 ms                                                | 2.07 ms: 1.28x faster                                                 |
| regex_compile                    | 78.3 ms                                                | 61.4 ms: 1.28x faster                                                 |
| pyflate                          | 352 ms                                                 | 276 ms: 1.28x faster                                                  |
| unpickle_pure_python             | 165 us                                                 | 130 us: 1.27x faster                                                  |
| float                            | 55.8 ms                                                | 44.0 ms: 1.27x faster                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 39.9 ms: 1.27x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 133 ms: 1.26x faster                                                  |
| genshi_xml                       | 34.1 ms                                                | 27.1 ms: 1.26x faster                                                 |
| richards                         | 36.2 ms                                                | 29.2 ms: 1.24x faster                                                 |
| regex_effbot                     | 2.63 ms                                                | 2.13 ms: 1.24x faster                                                 |
| async_tree_eager                 | 69.9 ms                                                | 57.2 ms: 1.22x faster                                                 |
| dulwich_log                      | 28.7 ms                                                | 23.7 ms: 1.21x faster                                                 |
| richards_super                   | 39.2 ms                                                | 32.9 ms: 1.19x faster                                                 |
| pylint                           | 180 ms                                                 | 151 ms: 1.19x faster                                                  |
| html5lib                         | 36.7 ms                                                | 30.8 ms: 1.19x faster                                                 |
| xml_etree_process                | 41.3 ms                                                | 34.9 ms: 1.18x faster                                                 |
| xml_etree_generate               | 57.1 ms                                                | 49.2 ms: 1.16x faster                                                 |
| comprehensions                   | 12.0 us                                                | 10.4 us: 1.15x faster                                                 |
| pickle_pure_python               | 215 us                                                 | 188 us: 1.14x faster                                                  |
| chaos                            | 41.1 ms                                                | 35.9 ms: 1.14x faster                                                 |
| 2to3                             | 179 ms                                                 | 157 ms: 1.14x faster                                                  |
| pprint_pformat                   | 1.10 sec                                               | 969 ms: 1.14x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 405 ms: 1.13x faster                                                  |
| typing_runtime_protocols         | 101 us                                                 | 88.9 us: 1.13x faster                                                 |
| raytrace                         | 181 ms                                                 | 160 ms: 1.13x faster                                                  |
| pprint_safe_repr                 | 541 ms                                                 | 479 ms: 1.13x faster                                                  |
| pycparser                        | 701 ms                                                 | 621 ms: 1.13x faster                                                  |
| sympy_integrate                  | 11.3 ms                                                | 10.0 ms: 1.13x faster                                                 |
| sympy_expand                     | 248 ms                                                 | 221 ms: 1.12x faster                                                  |
| sympy_str                        | 146 ms                                                 | 130 ms: 1.12x faster                                                  |
| nqueens                          | 61.8 ms                                                | 55.2 ms: 1.12x faster                                                 |
| spectral_norm                    | 76.5 ms                                                | 68.4 ms: 1.12x faster                                                 |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 401 ms: 1.12x faster                                                  |
| bpe_tokeniser                    | 3.26 sec                                               | 2.92 sec: 1.12x faster                                                |
| fannkuch                         | 279 ms                                                 | 250 ms: 1.11x faster                                                  |
| async_generators                 | 294 ms                                                 | 263 ms: 1.11x faster                                                  |
| regex_v8                         | 17.0 ms                                                | 15.3 ms: 1.11x faster                                                 |
| crypto_pyaes                     | 55.3 ms                                                | 49.8 ms: 1.11x faster                                                 |
| logging_simple                   | 3.56 us                                                | 3.26 us: 1.09x faster                                                 |
| sphinx                           | 602 ms                                                 | 551 ms: 1.09x faster                                                  |
| scimark_lu                       | 75.9 ms                                                | 69.7 ms: 1.09x faster                                                 |
| sympy_sum                        | 75.1 ms                                                | 69.1 ms: 1.09x faster                                                 |
| telco                            | 4.84 ms                                                | 4.45 ms: 1.09x faster                                                 |
| logging_format                   | 3.85 us                                                | 3.58 us: 1.08x faster                                                 |
| mako                             | 7.75 ms                                                | 7.20 ms: 1.08x faster                                                 |
| bench_thread_pool                | 503 us                                                 | 472 us: 1.07x faster                                                  |
| json_dumps                       | 6.47 ms                                                | 6.08 ms: 1.06x faster                                                 |
| k_core                           | 1.61 sec                                               | 1.52 sec: 1.06x faster                                                |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 351 ms: 1.06x faster                                                  |
| connected_components             | 319 ms                                                 | 301 ms: 1.06x faster                                                  |
| shortest_path                    | 345 ms                                                 | 327 ms: 1.06x faster                                                  |
| docutils                         | 1.44 sec                                               | 1.37 sec: 1.05x faster                                                |
| xml_etree_iterparse              | 74.2 ms                                                | 70.5 ms: 1.05x faster                                                 |
| django_template                  | 20.5 ms                                                | 19.5 ms: 1.05x faster                                                 |
| meteor_contest                   | 74.0 ms                                                | 70.8 ms: 1.05x faster                                                 |
| xml_etree_parse                  | 108 ms                                                 | 104 ms: 1.03x faster                                                  |
| regex_dna                        | 149 ms                                                 | 144 ms: 1.03x faster                                                  |
| pidigits                         | 284 ms                                                 | 280 ms: 1.01x faster                                                  |
| nbody                            | 73.6 ms                                                | 73.0 ms: 1.01x faster                                                 |
| scimark_fft                      | 200 ms                                                 | 201 ms: 1.01x slower                                                  |
| dask                             | 771 ms                                                 | 798 ms: 1.03x slower                                                  |
| pathlib                          | 23.2 ms                                                | 24.2 ms: 1.04x slower                                                 |
| python_startup_no_site           | 13.7 ms                                                | 14.6 ms: 1.06x slower                                                 |
| many_optionals                   | 409 us                                                 | 439 us: 1.07x slower                                                  |
| bench_mp_pool                    | 64.7 ms                                                | 69.6 ms: 1.08x slower                                                 |
| json_loads                       | 17.0 us                                                | 18.4 us: 1.08x slower                                                 |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.24 ms: 1.09x slower                                                 |
| gc_traversal                     | 2.94 ms                                                | 3.19 ms: 1.09x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 383 ms: 1.10x slower                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 1.34 ms: 1.12x slower                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 160 ms: 1.16x slower                                                  |
| subparsers                       | 9.44 ms                                                | 13.0 ms: 1.38x slower                                                 |
| async_tree_eager_tg              | 47.4 ms                                                | 120 ms: 2.53x slower                                                  |
| logging_silent                   | 71.0 ns                                                | 292 ns: 4.12x slower                                                  |
| coverage                         | 46.2 ms                                                | 235 ms: 5.09x slower                                                  |
| thrift                           | 466 us                                                 | 43.1 ms: 92.50x slower                                                |
| Geometric mean                   | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (4): sqlite_synth, asyncio_websockets, json, python_startup
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250524-3.15.0a0-2fd09b0-CLANG/bm-20250524-darwin-arm64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.068x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: 1.11x