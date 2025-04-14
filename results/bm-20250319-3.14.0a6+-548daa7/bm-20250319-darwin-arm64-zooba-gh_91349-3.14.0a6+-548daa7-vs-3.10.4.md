# Results vs. 3.10.4

- fork: zooba
- ref: gh_91349
- machine: darwin-arm64
- commit hash: 548daa7
- commit date: 2025-03-19
- overall geometric mean: 1.358x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250319-darwin-arm64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 162 ms: 1.24x faster                                      |
| docutils       | 1.74 sec                                               | 1.44 sec: 1.21x faster                                    |
| html5lib       | 43.5 ms                                                | 29.9 ms: 1.46x faster                                     |
| sphinx         | 729 ms                                                 | 582 ms: 1.25x faster                                      |
| Geometric mean | (ref)                                                  | 1.29x faster                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250319-darwin-arm64-zooba-gh_91349-3.14.0a6+-548daa7 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 61.4 ms: 6.38x faster                                     |
| async_tree_eager_memoization  | 483 ms                                                 | 142 ms: 3.41x faster                                      |
| async_tree_eager_io           | 1.01 sec                                               | 363 ms: 2.79x faster                                      |
| async_tree_io                 | 1.02 sec                                               | 377 ms: 2.70x faster                                      |
| async_tree_memoization        | 481 ms                                                 | 198 ms: 2.43x faster                                      |
| async_tree_none               | 391 ms                                                 | 162 ms: 2.42x faster                                      |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 357 ms: 1.87x faster                                      |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 411 ms: 1.62x faster                                      |
| coroutines                    | 20.5 ms                                                | 16.4 ms: 1.25x faster                                     |
| async_generators              | 233 ms                                                 | 258 ms: 1.11x slower                                      |
| Geometric mean                | (ref)                                                  | 2.09x faster                                              |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250319-darwin-arm64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| float          | 72.4 ms                                                | 47.7 ms: 1.52x faster                                     |
| nbody          | 92.5 ms                                                | 72.9 ms: 1.27x faster                                     |
| pidigits       | 280 ms                                                 | 283 ms: 1.01x slower                                      |
| Geometric mean | (ref)                                                  | 1.24x faster                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250319-darwin-arm64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 68.7 ms: 1.39x faster                                     |
| regex_dna      | 175 ms                                                 | 140 ms: 1.25x faster                                      |
| regex_v8       | 19.1 ms                                                | 15.7 ms: 1.22x faster                                     |
| regex_effbot   | 2.34 ms                                                | 2.24 ms: 1.04x faster                                     |
| Geometric mean | (ref)                                                  | 1.22x faster                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250319-darwin-arm64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| pickle_pure_python   | 285 us                                                 | 203 us: 1.40x faster                                      |
| tomli_loads          | 1.72 sec                                               | 1.24 sec: 1.39x faster                                    |
| unpickle_pure_python | 198 us                                                 | 149 us: 1.33x faster                                      |
| xml_etree_process    | 44.6 ms                                                | 39.1 ms: 1.14x faster                                     |
| json_dumps           | 8.31 ms                                                | 7.36 ms: 1.13x faster                                     |
| xml_etree_parse      | 109 ms                                                 | 103 ms: 1.06x faster                                      |
| xml_etree_iterparse  | 74.5 ms                                                | 71.8 ms: 1.04x faster                                     |
| json_loads           | 16.6 us                                                | 18.0 us: 1.09x slower                                     |
| Geometric mean       | (ref)                                                  | 1.14x faster                                              |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250319-darwin-arm64-zooba-gh_91349-3.14.0a6+-548daa7 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 17.0 ms: 1.16x faster                                     |
| python_startup_no_site | 12.8 ms                                                | 12.7 ms: 1.00x faster                                     |
| Geometric mean         | (ref)                                                  | 1.08x faster                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250319-darwin-arm64-zooba-gh_91349-3.14.0a6+-548daa7 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| mako            | 9.81 ms                                                | 7.61 ms: 1.29x faster                                     |
| genshi_text     | 17.7 ms                                                | 14.2 ms: 1.25x faster                                     |
| genshi_xml      | 35.1 ms                                                | 29.2 ms: 1.20x faster                                     |
| django_template | 24.4 ms                                                | 21.3 ms: 1.15x faster                                     |
| Geometric mean  | (ref)                                                  | 1.22x faster                                              |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250319-darwin-arm64-zooba-gh_91349-3.14.0a6+-548daa7 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 61.4 ms: 6.38x faster                                     |
| typing_runtime_protocols      | 326 us                                                 | 94.2 us: 3.46x faster                                     |
| async_tree_eager_memoization  | 483 ms                                                 | 142 ms: 3.41x faster                                      |
| subparsers                    | 39.8 ms                                                | 12.1 ms: 3.29x faster                                     |
| async_tree_eager_io           | 1.01 sec                                               | 363 ms: 2.79x faster                                      |
| async_tree_io                 | 1.02 sec                                               | 377 ms: 2.70x faster                                      |
| async_tree_memoization        | 481 ms                                                 | 198 ms: 2.43x faster                                      |
| async_tree_none               | 391 ms                                                 | 162 ms: 2.42x faster                                      |
| deltablue                     | 4.99 ms                                                | 2.40 ms: 2.07x faster                                     |
| go                            | 163 ms                                                 | 82.1 ms: 1.99x faster                                     |
| deepcopy_memo                 | 34.7 us                                                | 18.3 us: 1.89x faster                                     |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 357 ms: 1.87x faster                                      |
| deepcopy                      | 276 us                                                 | 151 us: 1.82x faster                                      |
| raytrace                      | 327 ms                                                 | 182 ms: 1.80x faster                                      |
| scimark_sor                   | 140 ms                                                 | 78.9 ms: 1.77x faster                                     |
| logging_silent                | 117 ns                                                 | 66.9 ns: 1.75x faster                                     |
| scimark_monte_carlo           | 72.4 ms                                                | 43.2 ms: 1.67x faster                                     |
| chaos                         | 67.7 ms                                                | 41.4 ms: 1.64x faster                                     |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 411 ms: 1.62x faster                                      |
| richards_super                | 61.0 ms                                                | 37.7 ms: 1.62x faster                                     |
| richards                      | 52.3 ms                                                | 33.3 ms: 1.57x faster                                     |
| float                         | 72.4 ms                                                | 47.7 ms: 1.52x faster                                     |
| comprehensions                | 17.3 us                                                | 11.6 us: 1.49x faster                                     |
| html5lib                      | 43.5 ms                                                | 29.9 ms: 1.46x faster                                     |
| dulwich_log                   | 35.6 ms                                                | 24.6 ms: 1.45x faster                                     |
| deepcopy_reduce               | 2.32 us                                                | 1.62 us: 1.43x faster                                     |
| pylint                        | 231 ms                                                 | 162 ms: 1.42x faster                                      |
| hexiom                        | 6.25 ms                                                | 4.44 ms: 1.41x faster                                     |
| pickle_pure_python            | 285 us                                                 | 203 us: 1.40x faster                                      |
| pyflate                       | 448 ms                                                 | 320 ms: 1.40x faster                                      |
| pprint_pformat                | 1.33 sec                                               | 948 ms: 1.40x faster                                      |
| regex_compile                 | 95.6 ms                                                | 68.7 ms: 1.39x faster                                     |
| tomli_loads                   | 1.72 sec                                               | 1.24 sec: 1.39x faster                                    |
| logging_format                | 5.03 us                                                | 3.62 us: 1.39x faster                                     |
| logging_simple                | 4.59 us                                                | 3.32 us: 1.38x faster                                     |
| pprint_safe_repr              | 648 ms                                                 | 469 ms: 1.38x faster                                      |
| scimark_lu                    | 103 ms                                                 | 74.4 ms: 1.38x faster                                     |
| sqlalchemy_imperative         | 9.07 ms                                                | 6.62 ms: 1.37x faster                                     |
| pycparser                     | 887 ms                                                 | 664 ms: 1.34x faster                                      |
| unpickle_pure_python          | 198 us                                                 | 149 us: 1.33x faster                                      |
| generators                    | 31.7 ms                                                | 24.2 ms: 1.31x faster                                     |
| k_core                        | 2.01 sec                                               | 1.55 sec: 1.30x faster                                    |
| mako                          | 9.81 ms                                                | 7.61 ms: 1.29x faster                                     |
| sqlalchemy_declarative        | 75.7 ms                                                | 59.0 ms: 1.28x faster                                     |
| thrift                        | 562 us                                                 | 442 us: 1.27x faster                                      |
| nbody                         | 92.5 ms                                                | 72.9 ms: 1.27x faster                                     |
| spectral_norm                 | 95.3 ms                                                | 75.7 ms: 1.26x faster                                     |
| crypto_pyaes                  | 73.3 ms                                                | 58.4 ms: 1.25x faster                                     |
| sphinx                        | 729 ms                                                 | 582 ms: 1.25x faster                                      |
| coroutines                    | 20.5 ms                                                | 16.4 ms: 1.25x faster                                     |
| genshi_text                   | 17.7 ms                                                | 14.2 ms: 1.25x faster                                     |
| regex_dna                     | 175 ms                                                 | 140 ms: 1.25x faster                                      |
| sympy_sum                     | 92.7 ms                                                | 74.6 ms: 1.24x faster                                     |
| 2to3                          | 201 ms                                                 | 162 ms: 1.24x faster                                      |
| scimark_fft                   | 225 ms                                                 | 183 ms: 1.23x faster                                      |
| regex_v8                      | 19.1 ms                                                | 15.7 ms: 1.22x faster                                     |
| docutils                      | 1.74 sec                                               | 1.44 sec: 1.21x faster                                    |
| genshi_xml                    | 35.1 ms                                                | 29.2 ms: 1.20x faster                                     |
| sympy_str                     | 166 ms                                                 | 141 ms: 1.17x faster                                      |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 2.95 ms: 1.16x faster                                     |
| python_startup                | 19.6 ms                                                | 17.0 ms: 1.16x faster                                     |
| django_template               | 24.4 ms                                                | 21.3 ms: 1.15x faster                                     |
| xml_etree_process             | 44.6 ms                                                | 39.1 ms: 1.14x faster                                     |
| sympy_expand                  | 269 ms                                                 | 237 ms: 1.14x faster                                      |
| sympy_integrate               | 13.2 ms                                                | 11.6 ms: 1.14x faster                                     |
| json_dumps                    | 8.31 ms                                                | 7.36 ms: 1.13x faster                                     |
| mdp                           | 1.65 sec                                               | 1.48 sec: 1.11x faster                                    |
| bench_thread_pool             | 545 us                                                 | 491 us: 1.11x faster                                      |
| many_optionals                | 486 us                                                 | 447 us: 1.09x faster                                      |
| pathlib                       | 25.7 ms                                                | 23.7 ms: 1.09x faster                                     |
| fannkuch                      | 303 ms                                                 | 279 ms: 1.08x faster                                      |
| bpe_tokeniser                 | 3.44 sec                                               | 3.20 sec: 1.08x faster                                    |
| xml_etree_parse               | 109 ms                                                 | 103 ms: 1.06x faster                                      |
| meteor_contest                | 77.8 ms                                                | 73.8 ms: 1.05x faster                                     |
| regex_effbot                  | 2.34 ms                                                | 2.24 ms: 1.04x faster                                     |
| xml_etree_iterparse           | 74.5 ms                                                | 71.8 ms: 1.04x faster                                     |
| connected_components          | 318 ms                                                 | 308 ms: 1.03x faster                                      |
| dask                          | 789 ms                                                 | 768 ms: 1.03x faster                                      |
| python_startup_no_site        | 12.8 ms                                                | 12.7 ms: 1.00x faster                                     |
| pidigits                      | 280 ms                                                 | 283 ms: 1.01x slower                                      |
| json                          | 3.10 ms                                                | 3.16 ms: 1.02x slower                                     |
| nqueens                       | 63.8 ms                                                | 65.0 ms: 1.02x slower                                     |
| shortest_path                 | 328 ms                                                 | 334 ms: 1.02x slower                                      |
| sqlite_synth                  | 1.48 us                                                | 1.54 us: 1.04x slower                                     |
| bench_mp_pool                 | 56.0 ms                                                | 60.1 ms: 1.07x slower                                     |
| json_loads                    | 16.6 us                                                | 18.0 us: 1.09x slower                                     |
| async_generators              | 233 ms                                                 | 258 ms: 1.11x slower                                      |
| create_gc_cycles              | 1.16 ms                                                | 1.29 ms: 1.11x slower                                     |
| coverage                      | 41.2 ms                                                | 45.8 ms: 1.11x slower                                     |
| gc_traversal                  | 2.71 ms                                                | 3.12 ms: 1.15x slower                                     |
| telco                         | 3.49 ms                                                | 4.57 ms: 1.31x slower                                     |
| Geometric mean                | (ref)                                                  | 1.35x faster                                              |

Benchmark hidden because not significant (2): asyncio_websockets, xml_etree_generate
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250319-3.14.0a6+-548daa7/bm-20250319-darwin-arm64-zooba-gh_91349-3.14.0a6+-548daa7.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.358x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.15x