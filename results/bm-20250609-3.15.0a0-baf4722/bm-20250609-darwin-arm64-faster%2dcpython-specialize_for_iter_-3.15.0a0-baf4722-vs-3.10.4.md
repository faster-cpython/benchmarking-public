# Results vs. 3.10.4

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: darwin-arm64
- commit hash: baf4722
- commit date: 2025-06-09
- overall geometric mean: 1.155x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250609-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 185 ms: 1.09x faster                                                            |
| docutils       | 1.74 sec                                               | 1.51 sec: 1.15x faster                                                          |
| html5lib       | 43.5 ms                                                | 34.5 ms: 1.26x faster                                                           |
| sphinx         | 729 ms                                                 | 610 ms: 1.19x faster                                                            |
| Geometric mean | (ref)                                                  | 1.17x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250609-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|-------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 73.6 ms: 5.33x faster                                                           |
| async_tree_eager_memoization  | 483 ms                                                 | 151 ms: 3.19x faster                                                            |
| async_tree_eager_io           | 1.01 sec                                               | 392 ms: 2.59x faster                                                            |
| async_tree_io                 | 1.02 sec                                               | 413 ms: 2.46x faster                                                            |
| async_tree_memoization        | 481 ms                                                 | 214 ms: 2.24x faster                                                            |
| async_tree_none               | 391 ms                                                 | 182 ms: 2.15x faster                                                            |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 369 ms: 1.82x faster                                                            |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 432 ms: 1.55x faster                                                            |
| coroutines                    | 20.5 ms                                                | 19.3 ms: 1.07x faster                                                           |
| async_generators              | 233 ms                                                 | 275 ms: 1.18x slower                                                            |
| Geometric mean                | (ref)                                                  | 1.92x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250609-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 58.5 ms: 1.24x faster                                                           |
| nbody          | 92.5 ms                                                | 86.7 ms: 1.07x faster                                                           |
| pidigits       | 280 ms                                                 | 283 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250609-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 175 ms                                                 | 144 ms: 1.22x faster                                                            |
| regex_compile  | 95.6 ms                                                | 81.1 ms: 1.18x faster                                                           |
| regex_v8       | 19.1 ms                                                | 16.3 ms: 1.17x faster                                                           |
| regex_effbot   | 2.34 ms                                                | 2.37 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                  | 1.13x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250609-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 8.31 ms                                                | 6.78 ms: 1.23x faster                                                           |
| tomli_loads          | 1.72 sec                                               | 1.44 sec: 1.20x faster                                                          |
| pickle_pure_python   | 285 us                                                 | 241 us: 1.18x faster                                                            |
| unpickle_pure_python | 198 us                                                 | 177 us: 1.12x faster                                                            |
| xml_etree_parse      | 109 ms                                                 | 105 ms: 1.05x faster                                                            |
| xml_etree_process    | 44.6 ms                                                | 43.0 ms: 1.04x faster                                                           |
| xml_etree_iterparse  | 74.5 ms                                                | 73.5 ms: 1.01x faster                                                           |
| json_loads           | 16.6 us                                                | 16.5 us: 1.00x faster                                                           |
| xml_etree_generate   | 53.9 ms                                                | 58.3 ms: 1.08x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250609-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 18.6 ms: 1.06x faster                                                           |
| python_startup_no_site | 12.8 ms                                                | 14.1 ms: 1.10x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250609-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 8.99 ms: 1.09x faster                                                           |
| genshi_text     | 17.7 ms                                                | 17.6 ms: 1.01x faster                                                           |
| django_template | 24.4 ms                                                | 25.0 ms: 1.03x slower                                                           |
| genshi_xml      | 35.1 ms                                                | 36.3 ms: 1.03x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                                    |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250609-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|-------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 73.6 ms: 5.33x faster                                                           |
| async_tree_eager_memoization  | 483 ms                                                 | 151 ms: 3.19x faster                                                            |
| typing_runtime_protocols      | 326 us                                                 | 109 us: 2.99x faster                                                            |
| subparsers                    | 39.8 ms                                                | 14.9 ms: 2.68x faster                                                           |
| async_tree_eager_io           | 1.01 sec                                               | 392 ms: 2.59x faster                                                            |
| async_tree_io                 | 1.02 sec                                               | 413 ms: 2.46x faster                                                            |
| async_tree_memoization        | 481 ms                                                 | 214 ms: 2.24x faster                                                            |
| async_tree_none               | 391 ms                                                 | 182 ms: 2.15x faster                                                            |
| mdp                           | 1.65 sec                                               | 826 ms: 2.00x faster                                                            |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 369 ms: 1.82x faster                                                            |
| deltablue                     | 4.99 ms                                                | 2.79 ms: 1.79x faster                                                           |
| go                            | 163 ms                                                 | 100 ms: 1.63x faster                                                            |
| deepcopy_memo                 | 34.7 us                                                | 22.0 us: 1.58x faster                                                           |
| deepcopy                      | 276 us                                                 | 175 us: 1.58x faster                                                            |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 432 ms: 1.55x faster                                                            |
| raytrace                      | 327 ms                                                 | 212 ms: 1.54x faster                                                            |
| scimark_sor                   | 140 ms                                                 | 91.2 ms: 1.54x faster                                                           |
| richards_super                | 61.0 ms                                                | 41.7 ms: 1.46x faster                                                           |
| chaos                         | 67.7 ms                                                | 47.6 ms: 1.42x faster                                                           |
| richards                      | 52.3 ms                                                | 37.3 ms: 1.40x faster                                                           |
| scimark_monte_carlo           | 72.4 ms                                                | 52.7 ms: 1.37x faster                                                           |
| pylint                        | 231 ms                                                 | 169 ms: 1.37x faster                                                            |
| k_core                        | 2.01 sec                                               | 1.47 sec: 1.37x faster                                                          |
| dulwich_log                   | 35.6 ms                                                | 26.5 ms: 1.34x faster                                                           |
| pyflate                       | 448 ms                                                 | 336 ms: 1.33x faster                                                            |
| comprehensions                | 17.3 us                                                | 13.2 us: 1.31x faster                                                           |
| spectral_norm                 | 95.3 ms                                                | 74.3 ms: 1.28x faster                                                           |
| html5lib                      | 43.5 ms                                                | 34.5 ms: 1.26x faster                                                           |
| float                         | 72.4 ms                                                | 58.5 ms: 1.24x faster                                                           |
| hexiom                        | 6.25 ms                                                | 5.09 ms: 1.23x faster                                                           |
| deepcopy_reduce               | 2.32 us                                                | 1.89 us: 1.23x faster                                                           |
| json_dumps                    | 8.31 ms                                                | 6.78 ms: 1.23x faster                                                           |
| scimark_lu                    | 103 ms                                                 | 84.2 ms: 1.22x faster                                                           |
| regex_dna                     | 175 ms                                                 | 144 ms: 1.22x faster                                                            |
| tomli_loads                   | 1.72 sec                                               | 1.44 sec: 1.20x faster                                                          |
| pycparser                     | 887 ms                                                 | 742 ms: 1.20x faster                                                            |
| sphinx                        | 729 ms                                                 | 610 ms: 1.19x faster                                                            |
| crypto_pyaes                  | 73.3 ms                                                | 61.9 ms: 1.19x faster                                                           |
| pickle_pure_python            | 285 us                                                 | 241 us: 1.18x faster                                                            |
| regex_compile                 | 95.6 ms                                                | 81.1 ms: 1.18x faster                                                           |
| regex_v8                      | 19.1 ms                                                | 16.3 ms: 1.17x faster                                                           |
| sympy_integrate               | 13.2 ms                                                | 11.4 ms: 1.16x faster                                                           |
| docutils                      | 1.74 sec                                               | 1.51 sec: 1.15x faster                                                          |
| logging_format                | 5.03 us                                                | 4.36 us: 1.15x faster                                                           |
| sympy_sum                     | 92.7 ms                                                | 80.6 ms: 1.15x faster                                                           |
| logging_simple                | 4.59 us                                                | 4.06 us: 1.13x faster                                                           |
| pathlib                       | 25.7 ms                                                | 23.0 ms: 1.12x faster                                                           |
| unpickle_pure_python          | 198 us                                                 | 177 us: 1.12x faster                                                            |
| mako                          | 9.81 ms                                                | 8.99 ms: 1.09x faster                                                           |
| scimark_fft                   | 225 ms                                                 | 207 ms: 1.09x faster                                                            |
| 2to3                          | 201 ms                                                 | 185 ms: 1.09x faster                                                            |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.16 ms: 1.08x faster                                                           |
| sympy_str                     | 166 ms                                                 | 154 ms: 1.08x faster                                                            |
| nbody                         | 92.5 ms                                                | 86.7 ms: 1.07x faster                                                           |
| coroutines                    | 20.5 ms                                                | 19.3 ms: 1.07x faster                                                           |
| python_startup                | 19.6 ms                                                | 18.6 ms: 1.06x faster                                                           |
| bpe_tokeniser                 | 3.44 sec                                               | 3.25 sec: 1.06x faster                                                          |
| json                          | 3.10 ms                                                | 2.95 ms: 1.05x faster                                                           |
| meteor_contest                | 77.8 ms                                                | 74.0 ms: 1.05x faster                                                           |
| connected_components          | 318 ms                                                 | 304 ms: 1.05x faster                                                            |
| xml_etree_parse               | 109 ms                                                 | 105 ms: 1.05x faster                                                            |
| pprint_pformat                | 1.33 sec                                               | 1.28 sec: 1.04x faster                                                          |
| xml_etree_process             | 44.6 ms                                                | 43.0 ms: 1.04x faster                                                           |
| pprint_safe_repr              | 648 ms                                                 | 629 ms: 1.03x faster                                                            |
| sympy_expand                  | 269 ms                                                 | 261 ms: 1.03x faster                                                            |
| xml_etree_iterparse           | 74.5 ms                                                | 73.5 ms: 1.01x faster                                                           |
| genshi_text                   | 17.7 ms                                                | 17.6 ms: 1.01x faster                                                           |
| json_loads                    | 16.6 us                                                | 16.5 us: 1.00x faster                                                           |
| shortest_path                 | 328 ms                                                 | 327 ms: 1.00x faster                                                            |
| pidigits                      | 280 ms                                                 | 283 ms: 1.01x slower                                                            |
| regex_effbot                  | 2.34 ms                                                | 2.37 ms: 1.01x slower                                                           |
| many_optionals                | 486 us                                                 | 493 us: 1.02x slower                                                            |
| django_template               | 24.4 ms                                                | 25.0 ms: 1.03x slower                                                           |
| fannkuch                      | 303 ms                                                 | 311 ms: 1.03x slower                                                            |
| genshi_xml                    | 35.1 ms                                                | 36.3 ms: 1.03x slower                                                           |
| xml_etree_generate            | 53.9 ms                                                | 58.3 ms: 1.08x slower                                                           |
| dask                          | 789 ms                                                 | 854 ms: 1.08x slower                                                            |
| sqlite_synth                  | 1.48 us                                                | 1.62 us: 1.09x slower                                                           |
| python_startup_no_site        | 12.8 ms                                                | 14.1 ms: 1.10x slower                                                           |
| nqueens                       | 63.8 ms                                                | 71.5 ms: 1.12x slower                                                           |
| create_gc_cycles              | 1.16 ms                                                | 1.35 ms: 1.16x slower                                                           |
| gc_traversal                  | 2.71 ms                                                | 3.19 ms: 1.18x slower                                                           |
| async_generators              | 233 ms                                                 | 275 ms: 1.18x slower                                                            |
| telco                         | 3.49 ms                                                | 4.77 ms: 1.37x slower                                                           |
| logging_silent                | 117 ns                                                 | 339 ns: 2.89x slower                                                            |
| coverage                      | 41.2 ms                                                | 338 ms: 8.21x slower                                                            |
| thrift                        | 562 us                                                 | 43.8 ms: 77.96x slower                                                          |
| Geometric mean                | (ref)                                                  | 1.14x faster                                                                    |

Benchmark hidden because not significant (2): generators, asyncio_websockets
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250609-3.15.0a0-baf4722/bm-20250609-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.155x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.17x