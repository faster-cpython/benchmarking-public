# Results vs. 3.10.4

- fork: brandtbucher
- ref: macos_10_15
- machine: darwin-arm64
- commit hash: 0887346
- commit date: 2025-07-28
- overall geometric mean: 1.350x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250728-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-0887346 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 172 ms: 1.17x faster                                               |
| docutils       | 1.74 sec                                               | 1.46 sec: 1.19x faster                                             |
| html5lib       | 43.5 ms                                                | 33.5 ms: 1.30x faster                                              |
| sphinx         | 729 ms                                                 | 578 ms: 1.26x faster                                               |
| Geometric mean | (ref)                                                  | 1.23x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250728-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-0887346 |
|-------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 64.2 ms: 6.10x faster                                              |
| async_tree_eager_memoization  | 483 ms                                                 | 139 ms: 3.48x faster                                               |
| async_tree_eager_io           | 1.01 sec                                               | 364 ms: 2.79x faster                                               |
| async_tree_io                 | 1.02 sec                                               | 378 ms: 2.69x faster                                               |
| async_tree_memoization        | 481 ms                                                 | 196 ms: 2.45x faster                                               |
| async_tree_none               | 391 ms                                                 | 166 ms: 2.36x faster                                               |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 357 ms: 1.88x faster                                               |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 419 ms: 1.59x faster                                               |
| coroutines                    | 20.5 ms                                                | 16.5 ms: 1.24x faster                                              |
| async_generators              | 233 ms                                                 | 285 ms: 1.22x slower                                               |
| Geometric mean                | (ref)                                                  | 2.06x faster                                                       |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250728-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-0887346 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 51.4 ms: 1.41x faster                                              |
| nbody          | 92.5 ms                                                | 71.6 ms: 1.29x faster                                              |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                  | 1.22x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250728-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-0887346 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 72.9 ms: 1.31x faster                                              |
| regex_dna      | 175 ms                                                 | 138 ms: 1.27x faster                                               |
| regex_v8       | 19.1 ms                                                | 15.3 ms: 1.25x faster                                              |
| regex_effbot   | 2.34 ms                                                | 2.16 ms: 1.08x faster                                              |
| Geometric mean | (ref)                                                  | 1.22x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250728-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-0887346 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 129 us: 1.53x faster                                               |
| tomli_loads          | 1.72 sec                                               | 1.24 sec: 1.38x faster                                             |
| pickle_pure_python   | 285 us                                                 | 208 us: 1.37x faster                                               |
| xml_etree_process    | 44.6 ms                                                | 34.5 ms: 1.29x faster                                              |
| json_dumps           | 8.31 ms                                                | 6.62 ms: 1.26x faster                                              |
| xml_etree_parse      | 109 ms                                                 | 97.5 ms: 1.12x faster                                              |
| xml_etree_generate   | 53.9 ms                                                | 49.4 ms: 1.09x faster                                              |
| xml_etree_iterparse  | 74.5 ms                                                | 70.9 ms: 1.05x faster                                              |
| json_loads           | 16.6 us                                                | 17.4 us: 1.05x slower                                              |
| Geometric mean       | (ref)                                                  | 1.22x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250728-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-0887346 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 16.1 ms: 1.22x faster                                              |
| python_startup_no_site | 12.8 ms                                                | 11.7 ms: 1.10x faster                                              |
| Geometric mean         | (ref)                                                  | 1.16x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250728-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-0887346 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 6.47 ms: 1.52x faster                                              |
| genshi_text     | 17.7 ms                                                | 15.4 ms: 1.15x faster                                              |
| django_template | 24.4 ms                                                | 23.2 ms: 1.05x faster                                              |
| genshi_xml      | 35.1 ms                                                | 33.6 ms: 1.05x faster                                              |
| Geometric mean  | (ref)                                                  | 1.18x faster                                                       |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250728-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-0887346 |
|-------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 64.2 ms: 6.10x faster                                              |
| typing_runtime_protocols      | 326 us                                                 | 93.5 us: 3.49x faster                                              |
| async_tree_eager_memoization  | 483 ms                                                 | 139 ms: 3.48x faster                                               |
| async_tree_eager_io           | 1.01 sec                                               | 364 ms: 2.79x faster                                               |
| async_tree_io                 | 1.02 sec                                               | 378 ms: 2.69x faster                                               |
| async_tree_memoization        | 481 ms                                                 | 196 ms: 2.45x faster                                               |
| async_tree_none               | 391 ms                                                 | 166 ms: 2.36x faster                                               |
| mdp                           | 1.65 sec                                               | 776 ms: 2.13x faster                                               |
| deltablue                     | 4.99 ms                                                | 2.47 ms: 2.02x faster                                              |
| raytrace                      | 327 ms                                                 | 173 ms: 1.89x faster                                               |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 357 ms: 1.88x faster                                               |
| go                            | 163 ms                                                 | 87.5 ms: 1.87x faster                                              |
| chaos                         | 67.7 ms                                                | 39.1 ms: 1.73x faster                                              |
| scimark_sor                   | 140 ms                                                 | 85.3 ms: 1.64x faster                                              |
| richards_super                | 61.0 ms                                                | 37.6 ms: 1.62x faster                                              |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 419 ms: 1.59x faster                                               |
| scimark_monte_carlo           | 72.4 ms                                                | 45.7 ms: 1.58x faster                                              |
| deepcopy_memo                 | 34.7 us                                                | 21.9 us: 1.58x faster                                              |
| deepcopy                      | 276 us                                                 | 174 us: 1.58x faster                                               |
| pyflate                       | 448 ms                                                 | 285 ms: 1.57x faster                                               |
| subparsers                    | 39.8 ms                                                | 25.4 ms: 1.57x faster                                              |
| richards                      | 52.3 ms                                                | 33.8 ms: 1.55x faster                                              |
| unpickle_pure_python          | 198 us                                                 | 129 us: 1.53x faster                                               |
| comprehensions                | 17.3 us                                                | 11.4 us: 1.52x faster                                              |
| logging_silent                | 117 ns                                                 | 77.1 ns: 1.52x faster                                              |
| mako                          | 9.81 ms                                                | 6.47 ms: 1.52x faster                                              |
| spectral_norm                 | 95.3 ms                                                | 62.9 ms: 1.52x faster                                              |
| crypto_pyaes                  | 73.3 ms                                                | 49.7 ms: 1.47x faster                                              |
| pprint_pformat                | 1.33 sec                                               | 910 ms: 1.46x faster                                               |
| pprint_safe_repr              | 648 ms                                                 | 449 ms: 1.44x faster                                               |
| pylint                        | 231 ms                                                 | 161 ms: 1.43x faster                                               |
| float                         | 72.4 ms                                                | 51.4 ms: 1.41x faster                                              |
| dulwich_log                   | 35.6 ms                                                | 25.4 ms: 1.40x faster                                              |
| tomli_loads                   | 1.72 sec                                               | 1.24 sec: 1.38x faster                                             |
| pickle_pure_python            | 285 us                                                 | 208 us: 1.37x faster                                               |
| logging_format                | 5.03 us                                                | 3.68 us: 1.37x faster                                              |
| logging_simple                | 4.59 us                                                | 3.38 us: 1.36x faster                                              |
| hexiom                        | 6.25 ms                                                | 4.60 ms: 1.36x faster                                              |
| scimark_lu                    | 103 ms                                                 | 77.0 ms: 1.33x faster                                              |
| regex_compile                 | 95.6 ms                                                | 72.9 ms: 1.31x faster                                              |
| html5lib                      | 43.5 ms                                                | 33.5 ms: 1.30x faster                                              |
| xml_etree_process             | 44.6 ms                                                | 34.5 ms: 1.29x faster                                              |
| nbody                         | 92.5 ms                                                | 71.6 ms: 1.29x faster                                              |
| deepcopy_reduce               | 2.32 us                                                | 1.80 us: 1.29x faster                                              |
| generators                    | 31.7 ms                                                | 24.6 ms: 1.29x faster                                              |
| regex_dna                     | 175 ms                                                 | 138 ms: 1.27x faster                                               |
| pycparser                     | 887 ms                                                 | 701 ms: 1.26x faster                                               |
| k_core                        | 2.01 sec                                               | 1.59 sec: 1.26x faster                                             |
| sphinx                        | 729 ms                                                 | 578 ms: 1.26x faster                                               |
| json_dumps                    | 8.31 ms                                                | 6.62 ms: 1.26x faster                                              |
| regex_v8                      | 19.1 ms                                                | 15.3 ms: 1.25x faster                                              |
| coroutines                    | 20.5 ms                                                | 16.5 ms: 1.24x faster                                              |
| thrift                        | 562 us                                                 | 458 us: 1.23x faster                                               |
| python_startup                | 19.6 ms                                                | 16.1 ms: 1.22x faster                                              |
| sympy_integrate               | 13.2 ms                                                | 10.9 ms: 1.21x faster                                              |
| sympy_sum                     | 92.7 ms                                                | 76.9 ms: 1.21x faster                                              |
| fannkuch                      | 303 ms                                                 | 252 ms: 1.20x faster                                               |
| docutils                      | 1.74 sec                                               | 1.46 sec: 1.19x faster                                             |
| scimark_fft                   | 225 ms                                                 | 191 ms: 1.18x faster                                               |
| bpe_tokeniser                 | 3.44 sec                                               | 2.92 sec: 1.18x faster                                             |
| 2to3                          | 201 ms                                                 | 172 ms: 1.17x faster                                               |
| genshi_text                   | 17.7 ms                                                | 15.4 ms: 1.15x faster                                              |
| sympy_str                     | 166 ms                                                 | 147 ms: 1.13x faster                                               |
| xml_etree_parse               | 109 ms                                                 | 97.5 ms: 1.12x faster                                              |
| pathlib                       | 25.7 ms                                                | 23.4 ms: 1.10x faster                                              |
| python_startup_no_site        | 12.8 ms                                                | 11.7 ms: 1.10x faster                                              |
| xml_etree_generate            | 53.9 ms                                                | 49.4 ms: 1.09x faster                                              |
| sympy_expand                  | 269 ms                                                 | 249 ms: 1.08x faster                                               |
| regex_effbot                  | 2.34 ms                                                | 2.16 ms: 1.08x faster                                              |
| xml_etree_iterparse           | 74.5 ms                                                | 70.9 ms: 1.05x faster                                              |
| django_template               | 24.4 ms                                                | 23.2 ms: 1.05x faster                                              |
| meteor_contest                | 77.8 ms                                                | 74.3 ms: 1.05x faster                                              |
| genshi_xml                    | 35.1 ms                                                | 33.6 ms: 1.05x faster                                              |
| nqueens                       | 63.8 ms                                                | 62.0 ms: 1.03x faster                                              |
| json                          | 3.10 ms                                                | 3.04 ms: 1.02x faster                                              |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.38 ms: 1.01x faster                                              |
| dask                          | 789 ms                                                 | 796 ms: 1.01x slower                                               |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                               |
| connected_components          | 318 ms                                                 | 322 ms: 1.01x slower                                               |
| json_loads                    | 16.6 us                                                | 17.4 us: 1.05x slower                                              |
| shortest_path                 | 328 ms                                                 | 350 ms: 1.07x slower                                               |
| sqlite_synth                  | 1.48 us                                                | 1.59 us: 1.07x slower                                              |
| coverage                      | 41.2 ms                                                | 47.9 ms: 1.16x slower                                              |
| create_gc_cycles              | 1.16 ms                                                | 1.36 ms: 1.17x slower                                              |
| gc_traversal                  | 2.71 ms                                                | 3.19 ms: 1.18x slower                                              |
| async_generators              | 233 ms                                                 | 285 ms: 1.22x slower                                               |
| many_optionals                | 486 us                                                 | 598 us: 1.23x slower                                               |
| telco                         | 3.49 ms                                                | 4.41 ms: 1.26x slower                                              |
| Geometric mean                | (ref)                                                  | 1.35x faster                                                       |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250728-3.15.0a0-0887346-JIT/bm-20250728-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-0887346.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.350x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.19x