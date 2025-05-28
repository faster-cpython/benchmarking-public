# Results vs. 3.10.4

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: darwin-arm64
- commit hash: 6783662
- commit date: 2025-05-28
- overall geometric mean: 1.151x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250528-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-6783662 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 187 ms: 1.08x faster                                                            |
| docutils       | 1.74 sec                                               | 1.52 sec: 1.15x faster                                                          |
| html5lib       | 43.5 ms                                                | 34.1 ms: 1.28x faster                                                           |
| sphinx         | 729 ms                                                 | 614 ms: 1.19x faster                                                            |
| Geometric mean | (ref)                                                  | 1.17x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250528-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-6783662 |
|-------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 73.5 ms: 5.33x faster                                                           |
| async_tree_eager_memoization  | 483 ms                                                 | 152 ms: 3.19x faster                                                            |
| async_tree_eager_io           | 1.01 sec                                               | 397 ms: 2.56x faster                                                            |
| async_tree_io                 | 1.02 sec                                               | 417 ms: 2.44x faster                                                            |
| async_tree_memoization        | 481 ms                                                 | 216 ms: 2.23x faster                                                            |
| async_tree_none               | 391 ms                                                 | 186 ms: 2.11x faster                                                            |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 370 ms: 1.81x faster                                                            |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 438 ms: 1.53x faster                                                            |
| coroutines                    | 20.5 ms                                                | 19.3 ms: 1.06x faster                                                           |
| asyncio_websockets            | 242 ms                                                 | 243 ms: 1.00x slower                                                            |
| async_generators              | 233 ms                                                 | 276 ms: 1.18x slower                                                            |
| Geometric mean                | (ref)                                                  | 1.91x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250528-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-6783662 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 59.4 ms: 1.22x faster                                                           |
| nbody          | 92.5 ms                                                | 85.5 ms: 1.08x faster                                                           |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250528-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-6783662 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 175 ms                                                 | 143 ms: 1.22x faster                                                            |
| regex_v8       | 19.1 ms                                                | 16.2 ms: 1.18x faster                                                           |
| regex_compile  | 95.6 ms                                                | 81.5 ms: 1.17x faster                                                           |
| regex_effbot   | 2.34 ms                                                | 2.35 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                  | 1.14x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250528-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-6783662 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 8.31 ms                                                | 6.85 ms: 1.21x faster                                                           |
| tomli_loads          | 1.72 sec                                               | 1.43 sec: 1.20x faster                                                          |
| pickle_pure_python   | 285 us                                                 | 242 us: 1.17x faster                                                            |
| unpickle_pure_python | 198 us                                                 | 179 us: 1.11x faster                                                            |
| xml_etree_parse      | 109 ms                                                 | 105 ms: 1.04x faster                                                            |
| xml_etree_process    | 44.6 ms                                                | 43.5 ms: 1.03x faster                                                           |
| xml_etree_generate   | 53.9 ms                                                | 58.2 ms: 1.08x slower                                                           |
| json_loads           | 16.6 us                                                | 18.2 us: 1.10x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                                    |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250528-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-6783662 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 16.4 ms: 1.20x faster                                                           |
| python_startup_no_site | 12.8 ms                                                | 12.0 ms: 1.07x faster                                                           |
| Geometric mean         | (ref)                                                  | 1.13x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250528-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-6783662 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 8.96 ms: 1.09x faster                                                           |
| genshi_text     | 17.7 ms                                                | 17.5 ms: 1.01x faster                                                           |
| django_template | 24.4 ms                                                | 24.9 ms: 1.02x slower                                                           |
| genshi_xml      | 35.1 ms                                                | 36.1 ms: 1.03x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                                    |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250528-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-6783662 |
|-------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 73.5 ms: 5.33x faster                                                           |
| async_tree_eager_memoization  | 483 ms                                                 | 152 ms: 3.19x faster                                                            |
| typing_runtime_protocols      | 326 us                                                 | 108 us: 3.01x faster                                                            |
| subparsers                    | 39.8 ms                                                | 15.0 ms: 2.66x faster                                                           |
| async_tree_eager_io           | 1.01 sec                                               | 397 ms: 2.56x faster                                                            |
| async_tree_io                 | 1.02 sec                                               | 417 ms: 2.44x faster                                                            |
| async_tree_memoization        | 481 ms                                                 | 216 ms: 2.23x faster                                                            |
| async_tree_none               | 391 ms                                                 | 186 ms: 2.11x faster                                                            |
| mdp                           | 1.65 sec                                               | 828 ms: 1.99x faster                                                            |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 370 ms: 1.81x faster                                                            |
| deltablue                     | 4.99 ms                                                | 2.81 ms: 1.78x faster                                                           |
| go                            | 163 ms                                                 | 100 ms: 1.63x faster                                                            |
| deepcopy                      | 276 us                                                 | 174 us: 1.59x faster                                                            |
| deepcopy_memo                 | 34.7 us                                                | 22.0 us: 1.58x faster                                                           |
| raytrace                      | 327 ms                                                 | 212 ms: 1.54x faster                                                            |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 438 ms: 1.53x faster                                                            |
| scimark_sor                   | 140 ms                                                 | 91.8 ms: 1.52x faster                                                           |
| richards_super                | 61.0 ms                                                | 42.2 ms: 1.44x faster                                                           |
| chaos                         | 67.7 ms                                                | 47.7 ms: 1.42x faster                                                           |
| richards                      | 52.3 ms                                                | 37.8 ms: 1.38x faster                                                           |
| pylint                        | 231 ms                                                 | 169 ms: 1.37x faster                                                            |
| scimark_monte_carlo           | 72.4 ms                                                | 53.6 ms: 1.35x faster                                                           |
| dulwich_log                   | 35.6 ms                                                | 26.9 ms: 1.32x faster                                                           |
| pyflate                       | 448 ms                                                 | 339 ms: 1.32x faster                                                            |
| comprehensions                | 17.3 us                                                | 13.2 us: 1.31x faster                                                           |
| k_core                        | 2.01 sec                                               | 1.55 sec: 1.30x faster                                                          |
| html5lib                      | 43.5 ms                                                | 34.1 ms: 1.28x faster                                                           |
| spectral_norm                 | 95.3 ms                                                | 75.6 ms: 1.26x faster                                                           |
| deepcopy_reduce               | 2.32 us                                                | 1.90 us: 1.23x faster                                                           |
| regex_dna                     | 175 ms                                                 | 143 ms: 1.22x faster                                                            |
| float                         | 72.4 ms                                                | 59.4 ms: 1.22x faster                                                           |
| json_dumps                    | 8.31 ms                                                | 6.85 ms: 1.21x faster                                                           |
| hexiom                        | 6.25 ms                                                | 5.16 ms: 1.21x faster                                                           |
| scimark_lu                    | 103 ms                                                 | 85.3 ms: 1.20x faster                                                           |
| tomli_loads                   | 1.72 sec                                               | 1.43 sec: 1.20x faster                                                          |
| python_startup                | 19.6 ms                                                | 16.4 ms: 1.20x faster                                                           |
| crypto_pyaes                  | 73.3 ms                                                | 61.3 ms: 1.20x faster                                                           |
| pycparser                     | 887 ms                                                 | 744 ms: 1.19x faster                                                            |
| sphinx                        | 729 ms                                                 | 614 ms: 1.19x faster                                                            |
| regex_v8                      | 19.1 ms                                                | 16.2 ms: 1.18x faster                                                           |
| pickle_pure_python            | 285 us                                                 | 242 us: 1.17x faster                                                            |
| regex_compile                 | 95.6 ms                                                | 81.5 ms: 1.17x faster                                                           |
| sympy_integrate               | 13.2 ms                                                | 11.3 ms: 1.16x faster                                                           |
| logging_format                | 5.03 us                                                | 4.39 us: 1.15x faster                                                           |
| docutils                      | 1.74 sec                                               | 1.52 sec: 1.15x faster                                                          |
| sympy_sum                     | 92.7 ms                                                | 81.3 ms: 1.14x faster                                                           |
| logging_simple                | 4.59 us                                                | 4.09 us: 1.12x faster                                                           |
| unpickle_pure_python          | 198 us                                                 | 179 us: 1.11x faster                                                            |
| mako                          | 9.81 ms                                                | 8.96 ms: 1.09x faster                                                           |
| nbody                         | 92.5 ms                                                | 85.5 ms: 1.08x faster                                                           |
| 2to3                          | 201 ms                                                 | 187 ms: 1.08x faster                                                            |
| sympy_str                     | 166 ms                                                 | 154 ms: 1.08x faster                                                            |
| pathlib                       | 25.7 ms                                                | 23.9 ms: 1.08x faster                                                           |
| scimark_fft                   | 225 ms                                                 | 210 ms: 1.07x faster                                                            |
| python_startup_no_site        | 12.8 ms                                                | 12.0 ms: 1.07x faster                                                           |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.21 ms: 1.06x faster                                                           |
| coroutines                    | 20.5 ms                                                | 19.3 ms: 1.06x faster                                                           |
| bpe_tokeniser                 | 3.44 sec                                               | 3.26 sec: 1.05x faster                                                          |
| meteor_contest                | 77.8 ms                                                | 74.3 ms: 1.05x faster                                                           |
| pprint_pformat                | 1.33 sec                                               | 1.27 sec: 1.04x faster                                                          |
| xml_etree_parse               | 109 ms                                                 | 105 ms: 1.04x faster                                                            |
| pprint_safe_repr              | 648 ms                                                 | 625 ms: 1.04x faster                                                            |
| sympy_expand                  | 269 ms                                                 | 260 ms: 1.03x faster                                                            |
| xml_etree_process             | 44.6 ms                                                | 43.5 ms: 1.03x faster                                                           |
| bench_thread_pool             | 545 us                                                 | 536 us: 1.02x faster                                                            |
| json                          | 3.10 ms                                                | 3.05 ms: 1.02x faster                                                           |
| genshi_text                   | 17.7 ms                                                | 17.5 ms: 1.01x faster                                                           |
| connected_components          | 318 ms                                                 | 315 ms: 1.01x faster                                                            |
| asyncio_websockets            | 242 ms                                                 | 243 ms: 1.00x slower                                                            |
| regex_effbot                  | 2.34 ms                                                | 2.35 ms: 1.01x slower                                                           |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                                            |
| django_template               | 24.4 ms                                                | 24.9 ms: 1.02x slower                                                           |
| many_optionals                | 486 us                                                 | 498 us: 1.02x slower                                                            |
| fannkuch                      | 303 ms                                                 | 311 ms: 1.03x slower                                                            |
| genshi_xml                    | 35.1 ms                                                | 36.1 ms: 1.03x slower                                                           |
| shortest_path                 | 328 ms                                                 | 342 ms: 1.04x slower                                                            |
| dask                          | 789 ms                                                 | 852 ms: 1.08x slower                                                            |
| xml_etree_generate            | 53.9 ms                                                | 58.2 ms: 1.08x slower                                                           |
| sqlite_synth                  | 1.48 us                                                | 1.62 us: 1.10x slower                                                           |
| json_loads                    | 16.6 us                                                | 18.2 us: 1.10x slower                                                           |
| nqueens                       | 63.8 ms                                                | 71.3 ms: 1.12x slower                                                           |
| create_gc_cycles              | 1.16 ms                                                | 1.36 ms: 1.17x slower                                                           |
| async_generators              | 233 ms                                                 | 276 ms: 1.18x slower                                                            |
| gc_traversal                  | 2.71 ms                                                | 3.21 ms: 1.19x slower                                                           |
| bench_mp_pool                 | 56.0 ms                                                | 70.5 ms: 1.26x slower                                                           |
| telco                         | 3.49 ms                                                | 4.81 ms: 1.38x slower                                                           |
| logging_silent                | 117 ns                                                 | 340 ns: 2.90x slower                                                            |
| coverage                      | 41.2 ms                                                | 335 ms: 8.14x slower                                                            |
| thrift                        | 562 us                                                 | 44.0 ms: 78.19x slower                                                          |
| Geometric mean                | (ref)                                                  | 1.13x faster                                                                    |

Benchmark hidden because not significant (2): generators, xml_etree_iterparse
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250528-3.15.0a0-6783662/bm-20250528-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-6783662.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.151x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.17x