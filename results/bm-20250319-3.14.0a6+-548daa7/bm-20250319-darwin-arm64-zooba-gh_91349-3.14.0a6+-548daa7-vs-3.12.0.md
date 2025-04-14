# Results vs. 3.12.0

- fork: zooba
- ref: gh_91349
- machine: darwin-arm64
- commit hash: 548daa7
- commit date: 2025-03-19
- overall geometric mean: 1.070x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-darwin-arm64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 162 ms: 1.04x faster                                      |
| docutils       | 1.45 sec                                               | 1.44 sec: 1.01x faster                                    |
| html5lib       | 33.4 ms                                                | 29.9 ms: 1.12x faster                                     |
| sphinx         | 613 ms                                                 | 582 ms: 1.05x faster                                      |
| Geometric mean | (ref)                                                  | 1.05x faster                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-darwin-arm64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 363 ms: 1.83x faster                                      |
| async_tree_io_tg                 | 673 ms                                                 | 367 ms: 1.83x faster                                      |
| async_tree_io                    | 672 ms                                                 | 377 ms: 1.78x faster                                      |
| async_tree_eager_io_tg           | 617 ms                                                 | 376 ms: 1.64x faster                                      |
| async_tree_none_tg               | 255 ms                                                 | 156 ms: 1.63x faster                                      |
| async_tree_none                  | 263 ms                                                 | 162 ms: 1.63x faster                                      |
| async_tree_memoization_tg        | 318 ms                                                 | 196 ms: 1.62x faster                                      |
| async_tree_memoization           | 310 ms                                                 | 198 ms: 1.57x faster                                      |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 411 ms: 1.28x faster                                      |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 414 ms: 1.28x faster                                      |
| coroutines                       | 19.7 ms                                                | 16.4 ms: 1.20x faster                                     |
| async_tree_eager_memoization     | 168 ms                                                 | 142 ms: 1.18x faster                                      |
| async_generators                 | 299 ms                                                 | 258 ms: 1.16x faster                                      |
| async_tree_eager                 | 65.8 ms                                                | 61.4 ms: 1.07x faster                                     |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 357 ms: 1.05x faster                                      |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 393 ms: 1.13x slower                                      |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 175 ms: 1.23x slower                                      |
| async_tree_eager_tg              | 46.9 ms                                                | 130 ms: 2.78x slower                                      |
| Geometric mean                   | (ref)                                                  | 1.23x faster                                              |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-darwin-arm64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| float          | 54.1 ms                                                | 47.7 ms: 1.13x faster                                     |
| pidigits       | 283 ms                                                 | 283 ms: 1.00x slower                                      |
| nbody          | 67.6 ms                                                | 72.9 ms: 1.08x slower                                     |
| Geometric mean | (ref)                                                  | 1.02x faster                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-darwin-arm64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 68.7 ms: 1.10x faster                                     |
| regex_effbot   | 2.44 ms                                                | 2.24 ms: 1.09x faster                                     |
| regex_dna      | 143 ms                                                 | 140 ms: 1.02x faster                                      |
| regex_v8       | 15.1 ms                                                | 15.7 ms: 1.04x slower                                     |
| Geometric mean | (ref)                                                  | 1.04x faster                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-darwin-arm64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                               | 1.24 sec: 1.10x faster                                    |
| xml_etree_iterparse  | 75.5 ms                                                | 71.8 ms: 1.05x faster                                     |
| xml_etree_parse      | 108 ms                                                 | 103 ms: 1.04x faster                                      |
| xml_etree_generate   | 55.4 ms                                                | 54.0 ms: 1.03x faster                                     |
| xml_etree_process    | 38.9 ms                                                | 39.1 ms: 1.00x slower                                     |
| unpickle_pure_python | 145 us                                                 | 149 us: 1.02x slower                                      |
| pickle_pure_python   | 197 us                                                 | 203 us: 1.03x slower                                      |
| json_loads           | 17.0 us                                                | 18.0 us: 1.06x slower                                     |
| json_dumps           | 6.19 ms                                                | 7.36 ms: 1.19x slower                                     |
| Geometric mean       | (ref)                                                  | 1.01x slower                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-darwin-arm64-zooba-gh_91349-3.14.0a6+-548daa7 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 17.0 ms: 1.05x faster                                     |
| python_startup_no_site | 13.2 ms                                                | 12.7 ms: 1.03x faster                                     |
| Geometric mean         | (ref)                                                  | 1.04x faster                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-darwin-arm64-zooba-gh_91349-3.14.0a6+-548daa7 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| genshi_xml      | 30.5 ms                                                | 29.2 ms: 1.04x faster                                     |
| genshi_text     | 14.7 ms                                                | 14.2 ms: 1.03x faster                                     |
| mako            | 7.44 ms                                                | 7.61 ms: 1.02x slower                                     |
| django_template | 19.7 ms                                                | 21.3 ms: 1.08x slower                                     |
| Geometric mean  | (ref)                                                  | 1.01x slower                                              |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-darwin-arm64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 12.1 ms: 2.65x faster                                     |
| async_tree_eager_io              | 666 ms                                                 | 363 ms: 1.83x faster                                      |
| async_tree_io_tg                 | 673 ms                                                 | 367 ms: 1.83x faster                                      |
| async_tree_io                    | 672 ms                                                 | 377 ms: 1.78x faster                                      |
| async_tree_eager_io_tg           | 617 ms                                                 | 376 ms: 1.64x faster                                      |
| async_tree_none_tg               | 255 ms                                                 | 156 ms: 1.63x faster                                      |
| async_tree_none                  | 263 ms                                                 | 162 ms: 1.63x faster                                      |
| async_tree_memoization_tg        | 318 ms                                                 | 196 ms: 1.62x faster                                      |
| async_tree_memoization           | 310 ms                                                 | 198 ms: 1.57x faster                                      |
| deepcopy                         | 226 us                                                 | 151 us: 1.49x faster                                      |
| deepcopy_memo                    | 26.0 us                                                | 18.3 us: 1.42x faster                                     |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 411 ms: 1.28x faster                                      |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 414 ms: 1.28x faster                                      |
| deepcopy_reduce                  | 2.01 us                                                | 1.62 us: 1.24x faster                                     |
| generators                       | 29.4 ms                                                | 24.2 ms: 1.21x faster                                     |
| comprehensions                   | 14.0 us                                                | 11.6 us: 1.21x faster                                     |
| go                               | 98.5 ms                                                | 82.1 ms: 1.20x faster                                     |
| coroutines                       | 19.7 ms                                                | 16.4 ms: 1.20x faster                                     |
| dulwich_log                      | 29.2 ms                                                | 24.6 ms: 1.19x faster                                     |
| async_tree_eager_memoization     | 168 ms                                                 | 142 ms: 1.18x faster                                      |
| async_generators                 | 299 ms                                                 | 258 ms: 1.16x faster                                      |
| float                            | 54.1 ms                                                | 47.7 ms: 1.13x faster                                     |
| raytrace                         | 204 ms                                                 | 182 ms: 1.12x faster                                      |
| pylint                           | 182 ms                                                 | 162 ms: 1.12x faster                                      |
| html5lib                         | 33.4 ms                                                | 29.9 ms: 1.12x faster                                     |
| k_core                           | 1.72 sec                                               | 1.55 sec: 1.11x faster                                    |
| regex_compile                    | 75.9 ms                                                | 68.7 ms: 1.10x faster                                     |
| tomli_loads                      | 1.36 sec                                               | 1.24 sec: 1.10x faster                                    |
| bench_mp_pool                    | 65.5 ms                                                | 60.1 ms: 1.09x faster                                     |
| regex_effbot                     | 2.44 ms                                                | 2.24 ms: 1.09x faster                                     |
| scimark_sor                      | 85.8 ms                                                | 78.9 ms: 1.09x faster                                     |
| logging_simple                   | 3.60 us                                                | 3.32 us: 1.09x faster                                     |
| logging_silent                   | 72.5 ns                                                | 66.9 ns: 1.08x faster                                     |
| logging_format                   | 3.90 us                                                | 3.62 us: 1.08x faster                                     |
| async_tree_eager                 | 65.8 ms                                                | 61.4 ms: 1.07x faster                                     |
| deltablue                        | 2.57 ms                                                | 2.40 ms: 1.07x faster                                     |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 2.95 ms: 1.07x faster                                     |
| scimark_fft                      | 194 ms                                                 | 183 ms: 1.06x faster                                      |
| thrift                           | 468 us                                                 | 442 us: 1.06x faster                                      |
| sphinx                           | 613 ms                                                 | 582 ms: 1.05x faster                                      |
| xml_etree_iterparse              | 75.5 ms                                                | 71.8 ms: 1.05x faster                                     |
| sqlalchemy_declarative           | 61.9 ms                                                | 59.0 ms: 1.05x faster                                     |
| python_startup                   | 17.8 ms                                                | 17.0 ms: 1.05x faster                                     |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 357 ms: 1.05x faster                                      |
| genshi_xml                       | 30.5 ms                                                | 29.2 ms: 1.04x faster                                     |
| xml_etree_parse                  | 108 ms                                                 | 103 ms: 1.04x faster                                      |
| pathlib                          | 24.7 ms                                                | 23.7 ms: 1.04x faster                                     |
| pprint_pformat                   | 986 ms                                                 | 948 ms: 1.04x faster                                      |
| 2to3                             | 168 ms                                                 | 162 ms: 1.04x faster                                      |
| python_startup_no_site           | 13.2 ms                                                | 12.7 ms: 1.03x faster                                     |
| genshi_text                      | 14.7 ms                                                | 14.2 ms: 1.03x faster                                     |
| pprint_safe_repr                 | 483 ms                                                 | 469 ms: 1.03x faster                                      |
| scimark_monte_carlo              | 44.5 ms                                                | 43.2 ms: 1.03x faster                                     |
| bpe_tokeniser                    | 3.28 sec                                               | 3.20 sec: 1.03x faster                                    |
| xml_etree_generate               | 55.4 ms                                                | 54.0 ms: 1.03x faster                                     |
| sympy_sum                        | 76.2 ms                                                | 74.6 ms: 1.02x faster                                     |
| regex_dna                        | 143 ms                                                 | 140 ms: 1.02x faster                                      |
| sympy_str                        | 144 ms                                                 | 141 ms: 1.02x faster                                      |
| dask                             | 779 ms                                                 | 768 ms: 1.01x faster                                      |
| pycparser                        | 673 ms                                                 | 664 ms: 1.01x faster                                      |
| spectral_norm                    | 76.5 ms                                                | 75.7 ms: 1.01x faster                                     |
| docutils                         | 1.45 sec                                               | 1.44 sec: 1.01x faster                                    |
| mdp                              | 1.49 sec                                               | 1.48 sec: 1.01x faster                                    |
| chaos                            | 41.6 ms                                                | 41.4 ms: 1.01x faster                                     |
| sqlite_synth                     | 1.55 us                                                | 1.54 us: 1.01x faster                                     |
| pidigits                         | 283 ms                                                 | 283 ms: 1.00x slower                                      |
| sqlalchemy_imperative            | 6.60 ms                                                | 6.62 ms: 1.00x slower                                     |
| xml_etree_process                | 38.9 ms                                                | 39.1 ms: 1.00x slower                                     |
| shortest_path                    | 331 ms                                                 | 334 ms: 1.01x slower                                      |
| scimark_lu                       | 73.5 ms                                                | 74.4 ms: 1.01x slower                                     |
| sympy_expand                     | 233 ms                                                 | 237 ms: 1.01x slower                                      |
| hexiom                           | 4.38 ms                                                | 4.44 ms: 1.02x slower                                     |
| bench_thread_pool                | 483 us                                                 | 491 us: 1.02x slower                                      |
| mako                             | 7.44 ms                                                | 7.61 ms: 1.02x slower                                     |
| unpickle_pure_python             | 145 us                                                 | 149 us: 1.02x slower                                      |
| pyflate                          | 311 ms                                                 | 320 ms: 1.03x slower                                      |
| connected_components             | 300 ms                                                 | 308 ms: 1.03x slower                                      |
| typing_runtime_protocols         | 91.5 us                                                | 94.2 us: 1.03x slower                                     |
| pickle_pure_python               | 197 us                                                 | 203 us: 1.03x slower                                      |
| regex_v8                         | 15.1 ms                                                | 15.7 ms: 1.04x slower                                     |
| sympy_integrate                  | 11.1 ms                                                | 11.6 ms: 1.05x slower                                     |
| json                             | 3.00 ms                                                | 3.16 ms: 1.05x slower                                     |
| json_loads                       | 17.0 us                                                | 18.0 us: 1.06x slower                                     |
| gc_traversal                     | 2.95 ms                                                | 3.12 ms: 1.06x slower                                     |
| meteor_contest                   | 69.1 ms                                                | 73.8 ms: 1.07x slower                                     |
| django_template                  | 19.7 ms                                                | 21.3 ms: 1.08x slower                                     |
| nbody                            | 67.6 ms                                                | 72.9 ms: 1.08x slower                                     |
| richards_super                   | 34.6 ms                                                | 37.7 ms: 1.09x slower                                     |
| richards                         | 30.6 ms                                                | 33.3 ms: 1.09x slower                                     |
| nqueens                          | 59.5 ms                                                | 65.0 ms: 1.09x slower                                     |
| many_optionals                   | 403 us                                                 | 447 us: 1.11x slower                                      |
| fannkuch                         | 250 ms                                                 | 279 ms: 1.11x slower                                      |
| create_gc_cycles                 | 1.15 ms                                                | 1.29 ms: 1.12x slower                                     |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 393 ms: 1.13x slower                                      |
| crypto_pyaes                     | 51.4 ms                                                | 58.4 ms: 1.14x slower                                     |
| telco                            | 3.92 ms                                                | 4.57 ms: 1.17x slower                                     |
| json_dumps                       | 6.19 ms                                                | 7.36 ms: 1.19x slower                                     |
| coverage                         | 38.5 ms                                                | 45.8 ms: 1.19x slower                                     |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 175 ms: 1.23x slower                                      |
| async_tree_eager_tg              | 46.9 ms                                                | 130 ms: 2.78x slower                                      |
| Geometric mean                   | (ref)                                                  | 1.07x faster                                              |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (9) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250319-3.14.0a6+-548daa7/bm-20250319-darwin-arm64-zooba-gh_91349-3.14.0a6+-548daa7.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.070x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.11x