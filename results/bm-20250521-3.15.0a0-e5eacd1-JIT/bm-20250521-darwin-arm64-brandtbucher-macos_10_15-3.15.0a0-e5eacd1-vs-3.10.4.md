# Results vs. 3.10.4

- fork: brandtbucher
- ref: macos_10_15
- machine: darwin-arm64
- commit hash: e5eacd1
- commit date: 2025-05-21
- overall geometric mean: 1.273x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250521-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-e5eacd1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 169 ms: 1.19x faster                                               |
| docutils       | 1.74 sec                                               | 1.45 sec: 1.20x faster                                             |
| html5lib       | 43.5 ms                                                | 30.8 ms: 1.42x faster                                              |
| sphinx         | 729 ms                                                 | 581 ms: 1.25x faster                                               |
| Geometric mean | (ref)                                                  | 1.26x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250521-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-e5eacd1 |
|-------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 61.3 ms: 6.40x faster                                              |
| async_tree_eager_memoization  | 483 ms                                                 | 138 ms: 3.50x faster                                               |
| async_tree_eager_io           | 1.01 sec                                               | 352 ms: 2.88x faster                                               |
| async_tree_io                 | 1.02 sec                                               | 373 ms: 2.73x faster                                               |
| async_tree_memoization        | 481 ms                                                 | 186 ms: 2.59x faster                                               |
| async_tree_none               | 391 ms                                                 | 156 ms: 2.50x faster                                               |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 354 ms: 1.89x faster                                               |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 409 ms: 1.63x faster                                               |
| coroutines                    | 20.5 ms                                                | 16.2 ms: 1.27x faster                                              |
| async_generators              | 233 ms                                                 | 279 ms: 1.20x slower                                               |
| Geometric mean                | (ref)                                                  | 2.11x faster                                                       |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250521-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-e5eacd1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 43.1 ms: 1.68x faster                                              |
| nbody          | 92.5 ms                                                | 75.5 ms: 1.23x faster                                              |
| pidigits       | 280 ms                                                 | 283 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                  | 1.27x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250521-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-e5eacd1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 67.2 ms: 1.42x faster                                              |
| regex_dna      | 175 ms                                                 | 143 ms: 1.22x faster                                               |
| regex_v8       | 19.1 ms                                                | 15.8 ms: 1.21x faster                                              |
| regex_effbot   | 2.34 ms                                                | 2.26 ms: 1.03x faster                                              |
| Geometric mean | (ref)                                                  | 1.21x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250521-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-e5eacd1 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 135 us: 1.46x faster                                               |
| pickle_pure_python   | 285 us                                                 | 198 us: 1.43x faster                                               |
| tomli_loads          | 1.72 sec                                               | 1.21 sec: 1.42x faster                                             |
| json_dumps           | 8.31 ms                                                | 6.60 ms: 1.26x faster                                              |
| xml_etree_process    | 44.6 ms                                                | 35.5 ms: 1.26x faster                                              |
| xml_etree_parse      | 109 ms                                                 | 104 ms: 1.06x faster                                               |
| xml_etree_generate   | 53.9 ms                                                | 51.1 ms: 1.05x faster                                              |
| xml_etree_iterparse  | 74.5 ms                                                | 71.5 ms: 1.04x faster                                              |
| json_loads           | 16.6 us                                                | 18.2 us: 1.10x slower                                              |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250521-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-e5eacd1 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 19.1 ms: 1.03x faster                                              |
| python_startup_no_site | 12.8 ms                                                | 14.6 ms: 1.14x slower                                              |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250521-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-e5eacd1 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 6.77 ms: 1.45x faster                                              |
| genshi_text     | 17.7 ms                                                | 13.7 ms: 1.30x faster                                              |
| genshi_xml      | 35.1 ms                                                | 28.9 ms: 1.21x faster                                              |
| django_template | 24.4 ms                                                | 20.8 ms: 1.17x faster                                              |
| Geometric mean  | (ref)                                                  | 1.28x faster                                                       |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250521-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-e5eacd1 |
|-------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 61.3 ms: 6.40x faster                                              |
| async_tree_eager_memoization  | 483 ms                                                 | 138 ms: 3.50x faster                                               |
| typing_runtime_protocols      | 326 us                                                 | 99.5 us: 3.28x faster                                              |
| subparsers                    | 39.8 ms                                                | 13.3 ms: 2.98x faster                                              |
| async_tree_eager_io           | 1.01 sec                                               | 352 ms: 2.88x faster                                               |
| async_tree_io                 | 1.02 sec                                               | 373 ms: 2.73x faster                                               |
| async_tree_memoization        | 481 ms                                                 | 186 ms: 2.59x faster                                               |
| async_tree_none               | 391 ms                                                 | 156 ms: 2.50x faster                                               |
| mdp                           | 1.65 sec                                               | 757 ms: 2.18x faster                                               |
| go                            | 163 ms                                                 | 79.2 ms: 2.06x faster                                              |
| deltablue                     | 4.99 ms                                                | 2.43 ms: 2.05x faster                                              |
| deepcopy_memo                 | 34.7 us                                                | 17.5 us: 1.98x faster                                              |
| raytrace                      | 327 ms                                                 | 170 ms: 1.92x faster                                               |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 354 ms: 1.89x faster                                               |
| deepcopy                      | 276 us                                                 | 149 us: 1.85x faster                                               |
| scimark_sor                   | 140 ms                                                 | 77.5 ms: 1.81x faster                                              |
| chaos                         | 67.7 ms                                                | 37.7 ms: 1.80x faster                                              |
| scimark_monte_carlo           | 72.4 ms                                                | 42.3 ms: 1.71x faster                                              |
| richards_super                | 61.0 ms                                                | 35.9 ms: 1.70x faster                                              |
| float                         | 72.4 ms                                                | 43.1 ms: 1.68x faster                                              |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 409 ms: 1.63x faster                                               |
| richards                      | 52.3 ms                                                | 32.0 ms: 1.63x faster                                              |
| pyflate                       | 448 ms                                                 | 291 ms: 1.54x faster                                               |
| unpickle_pure_python          | 198 us                                                 | 135 us: 1.46x faster                                               |
| hexiom                        | 6.25 ms                                                | 4.28 ms: 1.46x faster                                              |
| mako                          | 9.81 ms                                                | 6.77 ms: 1.45x faster                                              |
| dulwich_log                   | 35.6 ms                                                | 24.6 ms: 1.45x faster                                              |
| deepcopy_reduce               | 2.32 us                                                | 1.61 us: 1.44x faster                                              |
| pickle_pure_python            | 285 us                                                 | 198 us: 1.43x faster                                               |
| regex_compile                 | 95.6 ms                                                | 67.2 ms: 1.42x faster                                              |
| pylint                        | 231 ms                                                 | 162 ms: 1.42x faster                                               |
| tomli_loads                   | 1.72 sec                                               | 1.21 sec: 1.42x faster                                             |
| html5lib                      | 43.5 ms                                                | 30.8 ms: 1.42x faster                                              |
| spectral_norm                 | 95.3 ms                                                | 69.1 ms: 1.38x faster                                              |
| scimark_lu                    | 103 ms                                                 | 74.4 ms: 1.38x faster                                              |
| comprehensions                | 17.3 us                                                | 12.6 us: 1.37x faster                                              |
| generators                    | 31.7 ms                                                | 23.1 ms: 1.37x faster                                              |
| logging_format                | 5.03 us                                                | 3.77 us: 1.33x faster                                              |
| logging_simple                | 4.59 us                                                | 3.46 us: 1.33x faster                                              |
| crypto_pyaes                  | 73.3 ms                                                | 55.6 ms: 1.32x faster                                              |
| genshi_text                   | 17.7 ms                                                | 13.7 ms: 1.30x faster                                              |
| pycparser                     | 887 ms                                                 | 685 ms: 1.29x faster                                               |
| coroutines                    | 20.5 ms                                                | 16.2 ms: 1.27x faster                                              |
| json_dumps                    | 8.31 ms                                                | 6.60 ms: 1.26x faster                                              |
| sympy_sum                     | 92.7 ms                                                | 73.6 ms: 1.26x faster                                              |
| k_core                        | 2.01 sec                                               | 1.60 sec: 1.26x faster                                             |
| xml_etree_process             | 44.6 ms                                                | 35.5 ms: 1.26x faster                                              |
| sphinx                        | 729 ms                                                 | 581 ms: 1.25x faster                                               |
| pprint_pformat                | 1.33 sec                                               | 1.08 sec: 1.23x faster                                             |
| nbody                         | 92.5 ms                                                | 75.5 ms: 1.23x faster                                              |
| sympy_integrate               | 13.2 ms                                                | 10.7 ms: 1.23x faster                                              |
| regex_dna                     | 175 ms                                                 | 143 ms: 1.22x faster                                               |
| pprint_safe_repr              | 648 ms                                                 | 533 ms: 1.22x faster                                               |
| genshi_xml                    | 35.1 ms                                                | 28.9 ms: 1.21x faster                                              |
| regex_v8                      | 19.1 ms                                                | 15.8 ms: 1.21x faster                                              |
| sympy_str                     | 166 ms                                                 | 139 ms: 1.20x faster                                               |
| docutils                      | 1.74 sec                                               | 1.45 sec: 1.20x faster                                             |
| 2to3                          | 201 ms                                                 | 169 ms: 1.19x faster                                               |
| django_template               | 24.4 ms                                                | 20.8 ms: 1.17x faster                                              |
| sympy_expand                  | 269 ms                                                 | 236 ms: 1.14x faster                                               |
| bench_thread_pool             | 545 us                                                 | 489 us: 1.12x faster                                               |
| bpe_tokeniser                 | 3.44 sec                                               | 3.09 sec: 1.11x faster                                             |
| pathlib                       | 25.7 ms                                                | 23.4 ms: 1.10x faster                                              |
| scimark_fft                   | 225 ms                                                 | 207 ms: 1.09x faster                                               |
| nqueens                       | 63.8 ms                                                | 59.4 ms: 1.08x faster                                              |
| xml_etree_parse               | 109 ms                                                 | 104 ms: 1.06x faster                                               |
| xml_etree_generate            | 53.9 ms                                                | 51.1 ms: 1.05x faster                                              |
| many_optionals                | 486 us                                                 | 463 us: 1.05x faster                                               |
| xml_etree_iterparse           | 74.5 ms                                                | 71.5 ms: 1.04x faster                                              |
| regex_effbot                  | 2.34 ms                                                | 2.26 ms: 1.03x faster                                              |
| python_startup                | 19.6 ms                                                | 19.1 ms: 1.03x faster                                              |
| json                          | 3.10 ms                                                | 3.03 ms: 1.02x faster                                              |
| meteor_contest                | 77.8 ms                                                | 78.2 ms: 1.01x slower                                              |
| pidigits                      | 280 ms                                                 | 283 ms: 1.01x slower                                               |
| fannkuch                      | 303 ms                                                 | 312 ms: 1.03x slower                                               |
| dask                          | 789 ms                                                 | 814 ms: 1.03x slower                                               |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.54 ms: 1.03x slower                                              |
| shortest_path                 | 328 ms                                                 | 350 ms: 1.07x slower                                               |
| sqlite_synth                  | 1.48 us                                                | 1.60 us: 1.08x slower                                              |
| json_loads                    | 16.6 us                                                | 18.2 us: 1.10x slower                                              |
| python_startup_no_site        | 12.8 ms                                                | 14.6 ms: 1.14x slower                                              |
| create_gc_cycles              | 1.16 ms                                                | 1.36 ms: 1.17x slower                                              |
| gc_traversal                  | 2.71 ms                                                | 3.21 ms: 1.19x slower                                              |
| async_generators              | 233 ms                                                 | 279 ms: 1.20x slower                                               |
| bench_mp_pool                 | 56.0 ms                                                | 71.0 ms: 1.27x slower                                              |
| telco                         | 3.49 ms                                                | 4.54 ms: 1.30x slower                                              |
| logging_silent                | 117 ns                                                 | 321 ns: 2.74x slower                                               |
| coverage                      | 41.2 ms                                                | 269 ms: 6.53x slower                                               |
| thrift                        | 562 us                                                 | 43.4 ms: 77.11x slower                                             |
| Geometric mean                | (ref)                                                  | 1.25x faster                                                       |

Benchmark hidden because not significant (2): asyncio_websockets, connected_components
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250521-3.15.0a0-e5eacd1-JIT/bm-20250521-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-e5eacd1.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.273x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: 1.19x