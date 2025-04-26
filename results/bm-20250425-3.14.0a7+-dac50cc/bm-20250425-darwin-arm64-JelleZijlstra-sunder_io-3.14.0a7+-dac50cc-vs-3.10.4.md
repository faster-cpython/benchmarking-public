# Results vs. 3.10.4

- fork: JelleZijlstra
- ref: sunder_io
- machine: darwin-arm64
- commit hash: dac50cc
- commit date: 2025-04-25
- overall geometric mean: 1.404x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250425-darwin-arm64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 160 ms: 1.25x faster                                               |
| docutils       | 1.74 sec                                               | 1.42 sec: 1.23x faster                                             |
| html5lib       | 43.5 ms                                                | 29.2 ms: 1.49x faster                                              |
| sphinx         | 729 ms                                                 | 574 ms: 1.27x faster                                               |
| Geometric mean | (ref)                                                  | 1.31x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250425-darwin-arm64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|-------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 59.9 ms: 6.54x faster                                              |
| async_tree_eager_memoization  | 483 ms                                                 | 135 ms: 3.58x faster                                               |
| async_tree_io                 | 1.02 sec                                               | 354 ms: 2.88x faster                                               |
| async_tree_eager_io           | 1.01 sec                                               | 359 ms: 2.82x faster                                               |
| async_tree_memoization        | 481 ms                                                 | 190 ms: 2.54x faster                                               |
| async_tree_none               | 391 ms                                                 | 159 ms: 2.46x faster                                               |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 347 ms: 1.93x faster                                               |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 399 ms: 1.67x faster                                               |
| coroutines                    | 20.5 ms                                                | 16.3 ms: 1.26x faster                                              |
| async_generators              | 233 ms                                                 | 246 ms: 1.05x slower                                               |
| Geometric mean                | (ref)                                                  | 2.15x faster                                                       |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250425-darwin-arm64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 45.7 ms: 1.58x faster                                              |
| nbody          | 92.5 ms                                                | 70.7 ms: 1.31x faster                                              |
| pidigits       | 280 ms                                                 | 283 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                  | 1.27x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250425-darwin-arm64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 66.1 ms: 1.44x faster                                              |
| regex_dna      | 175 ms                                                 | 140 ms: 1.25x faster                                               |
| regex_v8       | 19.1 ms                                                | 15.7 ms: 1.22x faster                                              |
| regex_effbot   | 2.34 ms                                                | 2.26 ms: 1.03x faster                                              |
| Geometric mean | (ref)                                                  | 1.23x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250425-darwin-arm64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 1.72 sec                                               | 1.21 sec: 1.42x faster                                             |
| pickle_pure_python   | 285 us                                                 | 201 us: 1.42x faster                                               |
| unpickle_pure_python | 198 us                                                 | 143 us: 1.39x faster                                               |
| xml_etree_process    | 44.6 ms                                                | 38.1 ms: 1.17x faster                                              |
| json_dumps           | 8.31 ms                                                | 7.37 ms: 1.13x faster                                              |
| xml_etree_iterparse  | 74.5 ms                                                | 71.6 ms: 1.04x faster                                              |
| xml_etree_generate   | 53.9 ms                                                | 53.5 ms: 1.01x faster                                              |
| json_loads           | 16.6 us                                                | 17.6 us: 1.06x slower                                              |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                       |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250425-darwin-arm64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 19.9 ms: 1.01x slower                                              |
| python_startup_no_site | 12.8 ms                                                | 14.7 ms: 1.15x slower                                              |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250425-darwin-arm64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text     | 17.7 ms                                                | 13.6 ms: 1.30x faster                                              |
| mako            | 9.81 ms                                                | 7.62 ms: 1.29x faster                                              |
| genshi_xml      | 35.1 ms                                                | 28.4 ms: 1.24x faster                                              |
| django_template | 24.4 ms                                                | 20.5 ms: 1.19x faster                                              |
| Geometric mean  | (ref)                                                  | 1.25x faster                                                       |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250425-darwin-arm64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|-------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 59.9 ms: 6.54x faster                                              |
| async_tree_eager_memoization  | 483 ms                                                 | 135 ms: 3.58x faster                                               |
| typing_runtime_protocols      | 326 us                                                 | 93.1 us: 3.50x faster                                              |
| subparsers                    | 39.8 ms                                                | 12.0 ms: 3.32x faster                                              |
| async_tree_io                 | 1.02 sec                                               | 354 ms: 2.88x faster                                               |
| async_tree_eager_io           | 1.01 sec                                               | 359 ms: 2.82x faster                                               |
| async_tree_memoization        | 481 ms                                                 | 190 ms: 2.54x faster                                               |
| async_tree_none               | 391 ms                                                 | 159 ms: 2.46x faster                                               |
| mdp                           | 1.65 sec                                               | 742 ms: 2.23x faster                                               |
| deltablue                     | 4.99 ms                                                | 2.30 ms: 2.17x faster                                              |
| go                            | 163 ms                                                 | 78.6 ms: 2.08x faster                                              |
| raytrace                      | 327 ms                                                 | 168 ms: 1.95x faster                                               |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 347 ms: 1.93x faster                                               |
| deepcopy_memo                 | 34.7 us                                                | 18.1 us: 1.92x faster                                              |
| deepcopy                      | 276 us                                                 | 147 us: 1.87x faster                                               |
| chaos                         | 67.7 ms                                                | 37.3 ms: 1.82x faster                                              |
| logging_silent                | 117 ns                                                 | 64.8 ns: 1.81x faster                                              |
| scimark_sor                   | 140 ms                                                 | 77.6 ms: 1.80x faster                                              |
| scimark_monte_carlo           | 72.4 ms                                                | 42.0 ms: 1.72x faster                                              |
| richards_super                | 61.0 ms                                                | 36.3 ms: 1.68x faster                                              |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 399 ms: 1.67x faster                                               |
| richards                      | 52.3 ms                                                | 32.3 ms: 1.62x faster                                              |
| float                         | 72.4 ms                                                | 45.7 ms: 1.58x faster                                              |
| pyflate                       | 448 ms                                                 | 286 ms: 1.57x faster                                               |
| comprehensions                | 17.3 us                                                | 11.2 us: 1.55x faster                                              |
| html5lib                      | 43.5 ms                                                | 29.2 ms: 1.49x faster                                              |
| dulwich_log                   | 35.6 ms                                                | 24.0 ms: 1.48x faster                                              |
| hexiom                        | 6.25 ms                                                | 4.23 ms: 1.48x faster                                              |
| deepcopy_reduce               | 2.32 us                                                | 1.59 us: 1.46x faster                                              |
| pylint                        | 231 ms                                                 | 159 ms: 1.45x faster                                               |
| regex_compile                 | 95.6 ms                                                | 66.1 ms: 1.44x faster                                              |
| tomli_loads                   | 1.72 sec                                               | 1.21 sec: 1.42x faster                                             |
| pickle_pure_python            | 285 us                                                 | 201 us: 1.42x faster                                               |
| logging_format                | 5.03 us                                                | 3.58 us: 1.41x faster                                              |
| logging_simple                | 4.59 us                                                | 3.28 us: 1.40x faster                                              |
| spectral_norm                 | 95.3 ms                                                | 68.2 ms: 1.40x faster                                              |
| sqlalchemy_imperative         | 9.07 ms                                                | 6.52 ms: 1.39x faster                                              |
| unpickle_pure_python          | 198 us                                                 | 143 us: 1.39x faster                                               |
| scimark_lu                    | 103 ms                                                 | 74.1 ms: 1.39x faster                                              |
| pprint_pformat                | 1.33 sec                                               | 964 ms: 1.38x faster                                               |
| pycparser                     | 887 ms                                                 | 646 ms: 1.37x faster                                               |
| generators                    | 31.7 ms                                                | 23.2 ms: 1.36x faster                                              |
| pprint_safe_repr              | 648 ms                                                 | 477 ms: 1.36x faster                                               |
| crypto_pyaes                  | 73.3 ms                                                | 54.8 ms: 1.34x faster                                              |
| k_core                        | 2.01 sec                                               | 1.51 sec: 1.33x faster                                             |
| nbody                         | 92.5 ms                                                | 70.7 ms: 1.31x faster                                              |
| genshi_text                   | 17.7 ms                                                | 13.6 ms: 1.30x faster                                              |
| sqlalchemy_declarative        | 75.7 ms                                                | 58.4 ms: 1.30x faster                                              |
| mako                          | 9.81 ms                                                | 7.62 ms: 1.29x faster                                              |
| sympy_sum                     | 92.7 ms                                                | 72.8 ms: 1.27x faster                                              |
| sphinx                        | 729 ms                                                 | 574 ms: 1.27x faster                                               |
| coroutines                    | 20.5 ms                                                | 16.3 ms: 1.26x faster                                              |
| 2to3                          | 201 ms                                                 | 160 ms: 1.25x faster                                               |
| sympy_integrate               | 13.2 ms                                                | 10.5 ms: 1.25x faster                                              |
| regex_dna                     | 175 ms                                                 | 140 ms: 1.25x faster                                               |
| genshi_xml                    | 35.1 ms                                                | 28.4 ms: 1.24x faster                                              |
| scimark_fft                   | 225 ms                                                 | 183 ms: 1.23x faster                                               |
| docutils                      | 1.74 sec                                               | 1.42 sec: 1.23x faster                                             |
| regex_v8                      | 19.1 ms                                                | 15.7 ms: 1.22x faster                                              |
| sympy_str                     | 166 ms                                                 | 136 ms: 1.22x faster                                               |
| django_template               | 24.4 ms                                                | 20.5 ms: 1.19x faster                                              |
| bpe_tokeniser                 | 3.44 sec                                               | 2.93 sec: 1.17x faster                                             |
| xml_etree_process             | 44.6 ms                                                | 38.1 ms: 1.17x faster                                              |
| sympy_expand                  | 269 ms                                                 | 230 ms: 1.17x faster                                               |
| fannkuch                      | 303 ms                                                 | 260 ms: 1.17x faster                                               |
| json_dumps                    | 8.31 ms                                                | 7.37 ms: 1.13x faster                                              |
| nqueens                       | 63.8 ms                                                | 57.2 ms: 1.12x faster                                              |
| many_optionals                | 486 us                                                 | 439 us: 1.11x faster                                               |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.09 ms: 1.11x faster                                              |
| pathlib                       | 25.7 ms                                                | 23.3 ms: 1.10x faster                                              |
| bench_thread_pool             | 545 us                                                 | 497 us: 1.10x faster                                               |
| meteor_contest                | 77.8 ms                                                | 71.9 ms: 1.08x faster                                              |
| connected_components          | 318 ms                                                 | 303 ms: 1.05x faster                                               |
| xml_etree_iterparse           | 74.5 ms                                                | 71.6 ms: 1.04x faster                                              |
| regex_effbot                  | 2.34 ms                                                | 2.26 ms: 1.03x faster                                              |
| json                          | 3.10 ms                                                | 3.02 ms: 1.03x faster                                              |
| xml_etree_generate            | 53.9 ms                                                | 53.5 ms: 1.01x faster                                              |
| pidigits                      | 280 ms                                                 | 283 ms: 1.01x slower                                               |
| python_startup                | 19.6 ms                                                | 19.9 ms: 1.01x slower                                              |
| sqlite_synth                  | 1.48 us                                                | 1.55 us: 1.05x slower                                              |
| async_generators              | 233 ms                                                 | 246 ms: 1.05x slower                                               |
| json_loads                    | 16.6 us                                                | 17.6 us: 1.06x slower                                              |
| create_gc_cycles              | 1.16 ms                                                | 1.28 ms: 1.10x slower                                              |
| gc_traversal                  | 2.71 ms                                                | 3.10 ms: 1.15x slower                                              |
| python_startup_no_site        | 12.8 ms                                                | 14.7 ms: 1.15x slower                                              |
| coverage                      | 41.2 ms                                                | 47.6 ms: 1.16x slower                                              |
| bench_mp_pool                 | 56.0 ms                                                | 65.7 ms: 1.17x slower                                              |
| telco                         | 3.49 ms                                                | 4.54 ms: 1.30x slower                                              |
| Geometric mean                | (ref)                                                  | 1.40x faster                                                       |

Benchmark hidden because not significant (3): xml_etree_parse, asyncio_websockets, shortest_path
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, dask, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250425-3.14.0a7+-dac50cc/bm-20250425-darwin-arm64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.404x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.16x