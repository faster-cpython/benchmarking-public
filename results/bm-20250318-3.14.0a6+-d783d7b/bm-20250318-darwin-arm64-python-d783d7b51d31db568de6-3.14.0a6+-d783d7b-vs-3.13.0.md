# Results vs. 3.13.0

- fork: python
- ref: d783d7b51d31db568de6
- machine: darwin-arm64
- commit hash: d783d7b
- commit date: 2025-03-18
- overall geometric mean: 1.071x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-darwin-arm64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 162 ms: 1.10x faster                                                   |
| html5lib       | 36.7 ms                                                | 29.8 ms: 1.23x faster                                                  |
| sphinx         | 602 ms                                                 | 582 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-darwin-arm64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 196 ms: 1.47x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 363 ms: 1.41x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 366 ms: 1.37x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 197 ms: 1.36x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 377 ms: 1.35x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 161 ms: 1.31x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 375 ms: 1.28x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 156 ms: 1.27x faster                                                   |
| coroutines                       | 20.0 ms                                                | 16.4 ms: 1.22x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 142 ms: 1.19x faster                                                   |
| async_tree_eager                 | 69.9 ms                                                | 61.2 ms: 1.14x faster                                                  |
| async_generators                 | 294 ms                                                 | 257 ms: 1.14x faster                                                   |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 411 ms: 1.12x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 414 ms: 1.08x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 357 ms: 1.04x faster                                                   |
| asyncio_websockets               | 242 ms                                                 | 242 ms: 1.00x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 392 ms: 1.13x slower                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 175 ms: 1.27x slower                                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 130 ms: 2.75x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-darwin-arm64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 47.7 ms: 1.17x faster                                                  |
| nbody          | 73.6 ms                                                | 72.9 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-darwin-arm64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.27 ms: 1.16x faster                                                  |
| regex_compile  | 78.3 ms                                                | 68.8 ms: 1.14x faster                                                  |
| regex_v8       | 17.0 ms                                                | 15.9 ms: 1.07x faster                                                  |
| regex_dna      | 149 ms                                                 | 141 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-darwin-arm64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.24 sec: 1.26x faster                                                 |
| unpickle_pure_python | 165 us                                                 | 149 us: 1.11x faster                                                   |
| xml_etree_generate   | 57.1 ms                                                | 53.7 ms: 1.06x faster                                                  |
| xml_etree_process    | 41.3 ms                                                | 38.9 ms: 1.06x faster                                                  |
| pickle_pure_python   | 215 us                                                 | 205 us: 1.05x faster                                                   |
| xml_etree_parse      | 108 ms                                                 | 104 ms: 1.04x faster                                                   |
| xml_etree_iterparse  | 74.2 ms                                                | 71.7 ms: 1.04x faster                                                  |
| json_loads           | 17.0 us                                                | 17.9 us: 1.05x slower                                                  |
| json_dumps           | 6.47 ms                                                | 7.30 ms: 1.13x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-darwin-arm64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 17.4 ms: 1.08x faster                                                  |
| python_startup_no_site | 13.7 ms                                                | 13.2 ms: 1.04x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-darwin-arm64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 14.1 ms: 1.20x faster                                                  |
| genshi_xml      | 34.1 ms                                                | 28.9 ms: 1.18x faster                                                  |
| mako            | 7.75 ms                                                | 7.60 ms: 1.02x faster                                                  |
| django_template | 20.5 ms                                                | 21.2 ms: 1.04x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-darwin-arm64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy                         | 236 us                                                 | 151 us: 1.56x faster                                                   |
| deepcopy_memo                    | 27.4 us                                                | 18.4 us: 1.49x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 196 ms: 1.47x faster                                                   |
| go                               | 117 ms                                                 | 82.2 ms: 1.42x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 363 ms: 1.41x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 366 ms: 1.37x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 197 ms: 1.36x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 377 ms: 1.35x faster                                                   |
| scimark_sor                      | 106 ms                                                 | 79.1 ms: 1.34x faster                                                  |
| generators                       | 31.9 ms                                                | 24.2 ms: 1.32x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 161 ms: 1.31x faster                                                   |
| deepcopy_reduce                  | 2.09 us                                                | 1.62 us: 1.29x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 375 ms: 1.28x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 156 ms: 1.27x faster                                                   |
| tomli_loads                      | 1.57 sec                                               | 1.24 sec: 1.26x faster                                                 |
| html5lib                         | 36.7 ms                                                | 29.8 ms: 1.23x faster                                                  |
| coroutines                       | 20.0 ms                                                | 16.4 ms: 1.22x faster                                                  |
| genshi_text                      | 16.9 ms                                                | 14.1 ms: 1.20x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 142 ms: 1.19x faster                                                   |
| genshi_xml                       | 34.1 ms                                                | 28.9 ms: 1.18x faster                                                  |
| float                            | 55.8 ms                                                | 47.7 ms: 1.17x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 24.6 ms: 1.17x faster                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 43.3 ms: 1.16x faster                                                  |
| pprint_pformat                   | 1.10 sec                                               | 948 ms: 1.16x faster                                                   |
| regex_effbot                     | 2.63 ms                                                | 2.27 ms: 1.16x faster                                                  |
| pprint_safe_repr                 | 541 ms                                                 | 467 ms: 1.16x faster                                                   |
| async_tree_eager                 | 69.9 ms                                                | 61.2 ms: 1.14x faster                                                  |
| async_generators                 | 294 ms                                                 | 257 ms: 1.14x faster                                                   |
| regex_compile                    | 78.3 ms                                                | 68.8 ms: 1.14x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 411 ms: 1.12x faster                                                   |
| unpickle_pure_python             | 165 us                                                 | 149 us: 1.11x faster                                                   |
| deltablue                        | 2.65 ms                                                | 2.39 ms: 1.11x faster                                                  |
| 2to3                             | 179 ms                                                 | 162 ms: 1.10x faster                                                   |
| pylint                           | 180 ms                                                 | 163 ms: 1.10x faster                                                   |
| pyflate                          | 352 ms                                                 | 320 ms: 1.10x faster                                                   |
| hexiom                           | 4.87 ms                                                | 4.44 ms: 1.10x faster                                                  |
| scimark_fft                      | 200 ms                                                 | 184 ms: 1.09x faster                                                   |
| python_startup                   | 18.8 ms                                                | 17.4 ms: 1.08x faster                                                  |
| richards                         | 36.2 ms                                                | 33.4 ms: 1.08x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 414 ms: 1.08x faster                                                   |
| typing_runtime_protocols         | 101 us                                                 | 93.6 us: 1.08x faster                                                  |
| logging_silent                   | 71.0 ns                                                | 66.2 ns: 1.07x faster                                                  |
| logging_simple                   | 3.56 us                                                | 3.32 us: 1.07x faster                                                  |
| regex_v8                         | 17.0 ms                                                | 15.9 ms: 1.07x faster                                                  |
| bench_mp_pool                    | 64.7 ms                                                | 60.8 ms: 1.07x faster                                                  |
| logging_format                   | 3.85 us                                                | 3.62 us: 1.06x faster                                                  |
| xml_etree_generate               | 57.1 ms                                                | 53.7 ms: 1.06x faster                                                  |
| xml_etree_process                | 41.3 ms                                                | 38.9 ms: 1.06x faster                                                  |
| thrift                           | 466 us                                                 | 440 us: 1.06x faster                                                   |
| regex_dna                        | 149 ms                                                 | 141 ms: 1.06x faster                                                   |
| pycparser                        | 701 ms                                                 | 663 ms: 1.06x faster                                                   |
| telco                            | 4.84 ms                                                | 4.58 ms: 1.06x faster                                                  |
| sympy_expand                     | 248 ms                                                 | 236 ms: 1.05x faster                                                   |
| pickle_pure_python               | 215 us                                                 | 205 us: 1.05x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 357 ms: 1.04x faster                                                   |
| richards_super                   | 39.2 ms                                                | 37.6 ms: 1.04x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 104 ms: 1.04x faster                                                   |
| python_startup_no_site           | 13.7 ms                                                | 13.2 ms: 1.04x faster                                                  |
| k_core                           | 1.61 sec                                               | 1.55 sec: 1.04x faster                                                 |
| connected_components             | 319 ms                                                 | 308 ms: 1.04x faster                                                   |
| xml_etree_iterparse              | 74.2 ms                                                | 71.7 ms: 1.04x faster                                                  |
| comprehensions                   | 12.0 us                                                | 11.6 us: 1.03x faster                                                  |
| shortest_path                    | 345 ms                                                 | 334 ms: 1.03x faster                                                   |
| sphinx                           | 602 ms                                                 | 582 ms: 1.03x faster                                                   |
| bench_thread_pool                | 503 us                                                 | 490 us: 1.03x faster                                                   |
| sympy_str                        | 146 ms                                                 | 142 ms: 1.03x faster                                                   |
| mako                             | 7.75 ms                                                | 7.60 ms: 1.02x faster                                                  |
| bpe_tokeniser                    | 3.26 sec                                               | 3.20 sec: 1.02x faster                                                 |
| scimark_lu                       | 75.9 ms                                                | 74.6 ms: 1.02x faster                                                  |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.60 ms: 1.01x faster                                                  |
| meteor_contest                   | 74.0 ms                                                | 73.0 ms: 1.01x faster                                                  |
| coverage                         | 46.2 ms                                                | 45.7 ms: 1.01x faster                                                  |
| sympy_sum                        | 75.1 ms                                                | 74.3 ms: 1.01x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 75.7 ms: 1.01x faster                                                  |
| nbody                            | 73.6 ms                                                | 72.9 ms: 1.01x faster                                                  |
| mdp                              | 1.50 sec                                               | 1.49 sec: 1.01x faster                                                 |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 2.96 ms: 1.01x faster                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.55 us: 1.01x faster                                                  |
| dask                             | 771 ms                                                 | 767 ms: 1.01x faster                                                   |
| fannkuch                         | 279 ms                                                 | 277 ms: 1.01x faster                                                   |
| asyncio_websockets               | 242 ms                                                 | 242 ms: 1.00x faster                                                   |
| sqlalchemy_declarative           | 59.0 ms                                                | 58.9 ms: 1.00x faster                                                  |
| raytrace                         | 181 ms                                                 | 182 ms: 1.00x slower                                                   |
| chaos                            | 41.1 ms                                                | 41.4 ms: 1.01x slower                                                  |
| sympy_integrate                  | 11.3 ms                                                | 11.5 ms: 1.02x slower                                                  |
| pathlib                          | 23.2 ms                                                | 23.8 ms: 1.03x slower                                                  |
| json                             | 3.04 ms                                                | 3.13 ms: 1.03x slower                                                  |
| django_template                  | 20.5 ms                                                | 21.2 ms: 1.04x slower                                                  |
| json_loads                       | 17.0 us                                                | 17.9 us: 1.05x slower                                                  |
| crypto_pyaes                     | 55.3 ms                                                | 58.3 ms: 1.05x slower                                                  |
| nqueens                          | 61.8 ms                                                | 65.3 ms: 1.06x slower                                                  |
| gc_traversal                     | 2.94 ms                                                | 3.11 ms: 1.06x slower                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 1.29 ms: 1.08x slower                                                  |
| many_optionals                   | 409 us                                                 | 448 us: 1.10x slower                                                   |
| json_dumps                       | 6.47 ms                                                | 7.30 ms: 1.13x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 392 ms: 1.13x slower                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 175 ms: 1.27x slower                                                   |
| subparsers                       | 9.44 ms                                                | 12.2 ms: 1.29x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 130 ms: 2.75x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.07x faster                                                           |

Benchmark hidden because not significant (2): pidigits, docutils
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250318-3.14.0a6+-d783d7b/bm-20250318-darwin-arm64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.071x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.09x