# Results vs. 3.10.4

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: darwin-arm64
- commit hash: c41d531
- commit date: 2025-06-16
- overall geometric mean: 1.244x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250616-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 170 ms: 1.19x faster                                                            |
| docutils       | 1.74 sec                                               | 1.45 sec: 1.20x faster                                                          |
| html5lib       | 43.5 ms                                                | 31.7 ms: 1.37x faster                                                           |
| sphinx         | 729 ms                                                 | 580 ms: 1.26x faster                                                            |
| Geometric mean | (ref)                                                  | 1.25x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250616-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|-------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 63.6 ms: 6.16x faster                                                           |
| async_tree_eager_memoization  | 483 ms                                                 | 140 ms: 3.45x faster                                                            |
| async_tree_eager_io           | 1.01 sec                                               | 363 ms: 2.79x faster                                                            |
| async_tree_io                 | 1.02 sec                                               | 379 ms: 2.69x faster                                                            |
| async_tree_memoization        | 481 ms                                                 | 195 ms: 2.47x faster                                                            |
| async_tree_none               | 391 ms                                                 | 163 ms: 2.39x faster                                                            |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 357 ms: 1.88x faster                                                            |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 414 ms: 1.61x faster                                                            |
| coroutines                    | 20.5 ms                                                | 16.9 ms: 1.21x faster                                                           |
| async_generators              | 233 ms                                                 | 261 ms: 1.12x slower                                                            |
| Geometric mean                | (ref)                                                  | 2.08x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250616-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 49.9 ms: 1.45x faster                                                           |
| nbody          | 92.5 ms                                                | 74.2 ms: 1.25x faster                                                           |
| pidigits       | 280 ms                                                 | 283 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                  | 1.21x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250616-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 71.8 ms: 1.33x faster                                                           |
| regex_dna      | 175 ms                                                 | 143 ms: 1.22x faster                                                            |
| regex_v8       | 19.1 ms                                                | 16.2 ms: 1.18x faster                                                           |
| regex_effbot   | 2.34 ms                                                | 2.37 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                  | 1.17x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250616-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 285 us                                                 | 217 us: 1.31x faster                                                            |
| tomli_loads          | 1.72 sec                                               | 1.36 sec: 1.27x faster                                                          |
| json_dumps           | 8.31 ms                                                | 6.61 ms: 1.26x faster                                                           |
| unpickle_pure_python | 198 us                                                 | 158 us: 1.25x faster                                                            |
| xml_etree_process    | 44.6 ms                                                | 38.6 ms: 1.15x faster                                                           |
| xml_etree_parse      | 109 ms                                                 | 100 ms: 1.09x faster                                                            |
| xml_etree_iterparse  | 74.5 ms                                                | 72.7 ms: 1.02x faster                                                           |
| xml_etree_generate   | 53.9 ms                                                | 53.3 ms: 1.01x faster                                                           |
| json_loads           | 16.6 us                                                | 16.4 us: 1.01x faster                                                           |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250616-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 17.7 ms: 1.11x faster                                                           |
| python_startup_no_site | 12.8 ms                                                | 13.3 ms: 1.04x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250616-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 7.74 ms: 1.27x faster                                                           |
| genshi_text     | 17.7 ms                                                | 14.6 ms: 1.21x faster                                                           |
| genshi_xml      | 35.1 ms                                                | 30.9 ms: 1.14x faster                                                           |
| django_template | 24.4 ms                                                | 21.9 ms: 1.11x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.18x faster                                                                    |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250616-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|-------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 63.6 ms: 6.16x faster                                                           |
| async_tree_eager_memoization  | 483 ms                                                 | 140 ms: 3.45x faster                                                            |
| typing_runtime_protocols      | 326 us                                                 | 100 us: 3.25x faster                                                            |
| subparsers                    | 39.8 ms                                                | 13.6 ms: 2.94x faster                                                           |
| async_tree_eager_io           | 1.01 sec                                               | 363 ms: 2.79x faster                                                            |
| async_tree_io                 | 1.02 sec                                               | 379 ms: 2.69x faster                                                            |
| async_tree_memoization        | 481 ms                                                 | 195 ms: 2.47x faster                                                            |
| async_tree_none               | 391 ms                                                 | 163 ms: 2.39x faster                                                            |
| mdp                           | 1.65 sec                                               | 759 ms: 2.17x faster                                                            |
| deltablue                     | 4.99 ms                                                | 2.59 ms: 1.93x faster                                                           |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 357 ms: 1.88x faster                                                            |
| go                            | 163 ms                                                 | 87.5 ms: 1.87x faster                                                           |
| raytrace                      | 327 ms                                                 | 180 ms: 1.81x faster                                                            |
| deepcopy_memo                 | 34.7 us                                                | 19.4 us: 1.79x faster                                                           |
| deepcopy                      | 276 us                                                 | 157 us: 1.76x faster                                                            |
| chaos                         | 67.7 ms                                                | 39.7 ms: 1.71x faster                                                           |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 414 ms: 1.61x faster                                                            |
| scimark_sor                   | 140 ms                                                 | 88.6 ms: 1.58x faster                                                           |
| scimark_monte_carlo           | 72.4 ms                                                | 46.4 ms: 1.56x faster                                                           |
| richards_super                | 61.0 ms                                                | 40.9 ms: 1.49x faster                                                           |
| float                         | 72.4 ms                                                | 49.9 ms: 1.45x faster                                                           |
| pylint                        | 231 ms                                                 | 161 ms: 1.43x faster                                                            |
| richards                      | 52.3 ms                                                | 36.5 ms: 1.43x faster                                                           |
| dulwich_log                   | 35.6 ms                                                | 25.0 ms: 1.42x faster                                                           |
| pyflate                       | 448 ms                                                 | 318 ms: 1.41x faster                                                            |
| comprehensions                | 17.3 us                                                | 12.4 us: 1.39x faster                                                           |
| deepcopy_reduce               | 2.32 us                                                | 1.69 us: 1.38x faster                                                           |
| html5lib                      | 43.5 ms                                                | 31.7 ms: 1.37x faster                                                           |
| k_core                        | 2.01 sec                                               | 1.47 sec: 1.37x faster                                                          |
| spectral_norm                 | 95.3 ms                                                | 71.0 ms: 1.34x faster                                                           |
| hexiom                        | 6.25 ms                                                | 4.66 ms: 1.34x faster                                                           |
| regex_compile                 | 95.6 ms                                                | 71.8 ms: 1.33x faster                                                           |
| generators                    | 31.7 ms                                                | 24.1 ms: 1.32x faster                                                           |
| pickle_pure_python            | 285 us                                                 | 217 us: 1.31x faster                                                            |
| pycparser                     | 887 ms                                                 | 679 ms: 1.31x faster                                                            |
| crypto_pyaes                  | 73.3 ms                                                | 56.5 ms: 1.30x faster                                                           |
| logging_format                | 5.03 us                                                | 3.97 us: 1.27x faster                                                           |
| mako                          | 9.81 ms                                                | 7.74 ms: 1.27x faster                                                           |
| tomli_loads                   | 1.72 sec                                               | 1.36 sec: 1.27x faster                                                          |
| sphinx                        | 729 ms                                                 | 580 ms: 1.26x faster                                                            |
| json_dumps                    | 8.31 ms                                                | 6.61 ms: 1.26x faster                                                           |
| logging_simple                | 4.59 us                                                | 3.67 us: 1.25x faster                                                           |
| unpickle_pure_python          | 198 us                                                 | 158 us: 1.25x faster                                                            |
| scimark_lu                    | 103 ms                                                 | 82.0 ms: 1.25x faster                                                           |
| nbody                         | 92.5 ms                                                | 74.2 ms: 1.25x faster                                                           |
| sympy_sum                     | 92.7 ms                                                | 74.8 ms: 1.24x faster                                                           |
| regex_dna                     | 175 ms                                                 | 143 ms: 1.22x faster                                                            |
| genshi_text                   | 17.7 ms                                                | 14.6 ms: 1.21x faster                                                           |
| coroutines                    | 20.5 ms                                                | 16.9 ms: 1.21x faster                                                           |
| sympy_integrate               | 13.2 ms                                                | 11.0 ms: 1.20x faster                                                           |
| docutils                      | 1.74 sec                                               | 1.45 sec: 1.20x faster                                                          |
| 2to3                          | 201 ms                                                 | 170 ms: 1.19x faster                                                            |
| regex_v8                      | 19.1 ms                                                | 16.2 ms: 1.18x faster                                                           |
| sympy_str                     | 166 ms                                                 | 142 ms: 1.17x faster                                                            |
| pprint_pformat                | 1.33 sec                                               | 1.14 sec: 1.17x faster                                                          |
| xml_etree_process             | 44.6 ms                                                | 38.6 ms: 1.15x faster                                                           |
| pprint_safe_repr              | 648 ms                                                 | 562 ms: 1.15x faster                                                            |
| scimark_fft                   | 225 ms                                                 | 196 ms: 1.15x faster                                                            |
| pathlib                       | 25.7 ms                                                | 22.4 ms: 1.15x faster                                                           |
| genshi_xml                    | 35.1 ms                                                | 30.9 ms: 1.14x faster                                                           |
| bpe_tokeniser                 | 3.44 sec                                               | 3.06 sec: 1.12x faster                                                          |
| sympy_expand                  | 269 ms                                                 | 239 ms: 1.12x faster                                                            |
| fannkuch                      | 303 ms                                                 | 270 ms: 1.12x faster                                                            |
| django_template               | 24.4 ms                                                | 21.9 ms: 1.11x faster                                                           |
| python_startup                | 19.6 ms                                                | 17.7 ms: 1.11x faster                                                           |
| xml_etree_parse               | 109 ms                                                 | 100 ms: 1.09x faster                                                            |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.16 ms: 1.08x faster                                                           |
| meteor_contest                | 77.8 ms                                                | 72.8 ms: 1.07x faster                                                           |
| json                          | 3.10 ms                                                | 2.92 ms: 1.06x faster                                                           |
| nqueens                       | 63.8 ms                                                | 60.7 ms: 1.05x faster                                                           |
| many_optionals                | 486 us                                                 | 467 us: 1.04x faster                                                            |
| dask                          | 789 ms                                                 | 769 ms: 1.03x faster                                                            |
| xml_etree_iterparse           | 74.5 ms                                                | 72.7 ms: 1.02x faster                                                           |
| connected_components          | 318 ms                                                 | 311 ms: 1.02x faster                                                            |
| xml_etree_generate            | 53.9 ms                                                | 53.3 ms: 1.01x faster                                                           |
| json_loads                    | 16.6 us                                                | 16.4 us: 1.01x faster                                                           |
| pidigits                      | 280 ms                                                 | 283 ms: 1.01x slower                                                            |
| shortest_path                 | 328 ms                                                 | 332 ms: 1.01x slower                                                            |
| regex_effbot                  | 2.34 ms                                                | 2.37 ms: 1.01x slower                                                           |
| python_startup_no_site        | 12.8 ms                                                | 13.3 ms: 1.04x slower                                                           |
| sqlite_synth                  | 1.48 us                                                | 1.60 us: 1.08x slower                                                           |
| async_generators              | 233 ms                                                 | 261 ms: 1.12x slower                                                            |
| create_gc_cycles              | 1.16 ms                                                | 1.35 ms: 1.16x slower                                                           |
| gc_traversal                  | 2.71 ms                                                | 3.18 ms: 1.18x slower                                                           |
| telco                         | 3.49 ms                                                | 4.54 ms: 1.30x slower                                                           |
| logging_silent                | 117 ns                                                 | 323 ns: 2.76x slower                                                            |
| coverage                      | 41.2 ms                                                | 290 ms: 7.03x slower                                                            |
| thrift                        | 562 us                                                 | 43.6 ms: 77.57x slower                                                          |
| Geometric mean                | (ref)                                                  | 1.23x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250616-3.15.0a0-c41d531/bm-20250616-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.244x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: 1.17x