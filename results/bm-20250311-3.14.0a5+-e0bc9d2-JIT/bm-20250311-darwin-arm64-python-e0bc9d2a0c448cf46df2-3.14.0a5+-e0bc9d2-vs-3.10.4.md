# Results vs. 3.10.4

- fork: python
- ref: e0bc9d2a0c448cf46df2
- machine: darwin-arm64
- commit hash: e0bc9d2
- commit date: 2025-03-11
- overall geometric mean: 1.279x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250311-darwin-arm64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 176 ms: 1.14x faster                                                   |
| docutils       | 1.74 sec                                               | 1.54 sec: 1.13x faster                                                 |
| html5lib       | 43.5 ms                                                | 33.1 ms: 1.31x faster                                                  |
| sphinx         | 729 ms                                                 | 614 ms: 1.19x faster                                                   |
| Geometric mean | (ref)                                                  | 1.19x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250311-darwin-arm64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 67.9 ms: 5.77x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 150 ms: 3.23x faster                                                   |
| async_tree_eager_io           | 1.01 sec                                               | 389 ms: 2.61x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 403 ms: 2.53x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 212 ms: 2.27x faster                                                   |
| async_tree_none               | 391 ms                                                 | 175 ms: 2.24x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 372 ms: 1.80x faster                                                   |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 438 ms: 1.53x faster                                                   |
| coroutines                    | 20.5 ms                                                | 17.9 ms: 1.15x faster                                                  |
| asyncio_websockets            | 242 ms                                                 | 251 ms: 1.04x slower                                                   |
| async_generators              | 233 ms                                                 | 290 ms: 1.24x slower                                                   |
| Geometric mean                | (ref)                                                  | 1.95x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250311-darwin-arm64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 47.3 ms: 1.53x faster                                                  |
| nbody          | 92.5 ms                                                | 72.0 ms: 1.29x faster                                                  |
| pidigits       | 280 ms                                                 | 293 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                  | 1.24x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250311-darwin-arm64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 77.3 ms: 1.24x faster                                                  |
| regex_dna      | 175 ms                                                 | 145 ms: 1.20x faster                                                   |
| regex_v8       | 19.1 ms                                                | 16.5 ms: 1.16x faster                                                  |
| regex_effbot   | 2.34 ms                                                | 2.33 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.15x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250311-darwin-arm64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 148 us: 1.34x faster                                                   |
| tomli_loads          | 1.72 sec                                               | 1.31 sec: 1.32x faster                                                 |
| pickle_pure_python   | 285 us                                                 | 221 us: 1.29x faster                                                   |
| xml_etree_process    | 44.6 ms                                                | 37.8 ms: 1.18x faster                                                  |
| json_dumps           | 8.31 ms                                                | 7.47 ms: 1.11x faster                                                  |
| xml_etree_parse      | 109 ms                                                 | 102 ms: 1.07x faster                                                   |
| xml_etree_generate   | 53.9 ms                                                | 53.3 ms: 1.01x faster                                                  |
| xml_etree_iterparse  | 74.5 ms                                                | 73.9 ms: 1.01x faster                                                  |
| json_loads           | 16.6 us                                                | 18.2 us: 1.10x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250311-darwin-arm64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 17.9 ms: 1.10x faster                                                  |
| python_startup_no_site | 12.8 ms                                                | 13.5 ms: 1.06x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250311-darwin-arm64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 6.94 ms: 1.41x faster                                                  |
| genshi_text     | 17.7 ms                                                | 15.9 ms: 1.12x faster                                                  |
| genshi_xml      | 35.1 ms                                                | 32.8 ms: 1.07x faster                                                  |
| django_template | 24.4 ms                                                | 23.6 ms: 1.03x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.15x faster                                                           |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250311-darwin-arm64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 67.9 ms: 5.77x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 150 ms: 3.23x faster                                                   |
| typing_runtime_protocols      | 326 us                                                 | 101 us: 3.21x faster                                                   |
| subparsers                    | 39.8 ms                                                | 12.9 ms: 3.09x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 389 ms: 2.61x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 403 ms: 2.53x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 212 ms: 2.27x faster                                                   |
| async_tree_none               | 391 ms                                                 | 175 ms: 2.24x faster                                                   |
| deltablue                     | 4.99 ms                                                | 2.33 ms: 2.14x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 372 ms: 1.80x faster                                                   |
| richards_super                | 61.0 ms                                                | 36.9 ms: 1.65x faster                                                  |
| deepcopy                      | 276 us                                                 | 168 us: 1.64x faster                                                   |
| raytrace                      | 327 ms                                                 | 200 ms: 1.63x faster                                                   |
| deepcopy_memo                 | 34.7 us                                                | 21.4 us: 1.63x faster                                                  |
| logging_silent                | 117 ns                                                 | 74.5 ns: 1.57x faster                                                  |
| richards                      | 52.3 ms                                                | 33.6 ms: 1.56x faster                                                  |
| go                            | 163 ms                                                 | 105 ms: 1.56x faster                                                   |
| float                         | 72.4 ms                                                | 47.3 ms: 1.53x faster                                                  |
| scimark_sor                   | 140 ms                                                 | 91.7 ms: 1.53x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 438 ms: 1.53x faster                                                   |
| scimark_monte_carlo           | 72.4 ms                                                | 48.6 ms: 1.49x faster                                                  |
| chaos                         | 67.7 ms                                                | 45.5 ms: 1.49x faster                                                  |
| spectral_norm                 | 95.3 ms                                                | 66.6 ms: 1.43x faster                                                  |
| mako                          | 9.81 ms                                                | 6.94 ms: 1.41x faster                                                  |
| pyflate                       | 448 ms                                                 | 333 ms: 1.34x faster                                                   |
| unpickle_pure_python          | 198 us                                                 | 148 us: 1.34x faster                                                   |
| pylint                        | 231 ms                                                 | 173 ms: 1.33x faster                                                   |
| dulwich_log                   | 35.6 ms                                                | 26.7 ms: 1.33x faster                                                  |
| comprehensions                | 17.3 us                                                | 13.0 us: 1.33x faster                                                  |
| deepcopy_reduce               | 2.32 us                                                | 1.76 us: 1.32x faster                                                  |
| tomli_loads                   | 1.72 sec                                               | 1.31 sec: 1.32x faster                                                 |
| html5lib                      | 43.5 ms                                                | 33.1 ms: 1.31x faster                                                  |
| pickle_pure_python            | 285 us                                                 | 221 us: 1.29x faster                                                   |
| nbody                         | 92.5 ms                                                | 72.0 ms: 1.29x faster                                                  |
| k_core                        | 2.01 sec                                               | 1.58 sec: 1.27x faster                                                 |
| scimark_lu                    | 103 ms                                                 | 81.1 ms: 1.26x faster                                                  |
| sqlalchemy_imperative         | 9.07 ms                                                | 7.23 ms: 1.25x faster                                                  |
| logging_format                | 5.03 us                                                | 4.07 us: 1.24x faster                                                  |
| regex_compile                 | 95.6 ms                                                | 77.3 ms: 1.24x faster                                                  |
| logging_simple                | 4.59 us                                                | 3.73 us: 1.23x faster                                                  |
| generators                    | 31.7 ms                                                | 25.8 ms: 1.23x faster                                                  |
| regex_dna                     | 175 ms                                                 | 145 ms: 1.20x faster                                                   |
| hexiom                        | 6.25 ms                                                | 5.19 ms: 1.20x faster                                                  |
| pprint_pformat                | 1.33 sec                                               | 1.10 sec: 1.20x faster                                                 |
| sqlalchemy_declarative        | 75.7 ms                                                | 63.1 ms: 1.20x faster                                                  |
| pycparser                     | 887 ms                                                 | 741 ms: 1.20x faster                                                   |
| thrift                        | 562 us                                                 | 471 us: 1.19x faster                                                   |
| pprint_safe_repr              | 648 ms                                                 | 544 ms: 1.19x faster                                                   |
| sphinx                        | 729 ms                                                 | 614 ms: 1.19x faster                                                   |
| xml_etree_process             | 44.6 ms                                                | 37.8 ms: 1.18x faster                                                  |
| sympy_sum                     | 92.7 ms                                                | 79.0 ms: 1.17x faster                                                  |
| crypto_pyaes                  | 73.3 ms                                                | 62.7 ms: 1.17x faster                                                  |
| regex_v8                      | 19.1 ms                                                | 16.5 ms: 1.16x faster                                                  |
| coroutines                    | 20.5 ms                                                | 17.9 ms: 1.15x faster                                                  |
| 2to3                          | 201 ms                                                 | 176 ms: 1.14x faster                                                   |
| docutils                      | 1.74 sec                                               | 1.54 sec: 1.13x faster                                                 |
| scimark_fft                   | 225 ms                                                 | 201 ms: 1.12x faster                                                   |
| genshi_text                   | 17.7 ms                                                | 15.9 ms: 1.12x faster                                                  |
| json_dumps                    | 8.31 ms                                                | 7.47 ms: 1.11x faster                                                  |
| python_startup                | 19.6 ms                                                | 17.9 ms: 1.10x faster                                                  |
| sympy_str                     | 166 ms                                                 | 152 ms: 1.09x faster                                                   |
| pathlib                       | 25.7 ms                                                | 23.6 ms: 1.09x faster                                                  |
| bpe_tokeniser                 | 3.44 sec                                               | 3.17 sec: 1.08x faster                                                 |
| mdp                           | 1.65 sec                                               | 1.54 sec: 1.07x faster                                                 |
| genshi_xml                    | 35.1 ms                                                | 32.8 ms: 1.07x faster                                                  |
| xml_etree_parse               | 109 ms                                                 | 102 ms: 1.07x faster                                                   |
| sympy_integrate               | 13.2 ms                                                | 12.4 ms: 1.06x faster                                                  |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.23 ms: 1.06x faster                                                  |
| bench_thread_pool             | 545 us                                                 | 516 us: 1.06x faster                                                   |
| sympy_expand                  | 269 ms                                                 | 258 ms: 1.04x faster                                                   |
| django_template               | 24.4 ms                                                | 23.6 ms: 1.03x faster                                                  |
| dask                          | 789 ms                                                 | 768 ms: 1.03x faster                                                   |
| connected_components          | 318 ms                                                 | 310 ms: 1.03x faster                                                   |
| xml_etree_generate            | 53.9 ms                                                | 53.3 ms: 1.01x faster                                                  |
| xml_etree_iterparse           | 74.5 ms                                                | 73.9 ms: 1.01x faster                                                  |
| regex_effbot                  | 2.34 ms                                                | 2.33 ms: 1.00x faster                                                  |
| json                          | 3.10 ms                                                | 3.14 ms: 1.01x slower                                                  |
| fannkuch                      | 303 ms                                                 | 308 ms: 1.02x slower                                                   |
| meteor_contest                | 77.8 ms                                                | 79.4 ms: 1.02x slower                                                  |
| asyncio_websockets            | 242 ms                                                 | 251 ms: 1.04x slower                                                   |
| shortest_path                 | 328 ms                                                 | 340 ms: 1.04x slower                                                   |
| pidigits                      | 280 ms                                                 | 293 ms: 1.04x slower                                                   |
| python_startup_no_site        | 12.8 ms                                                | 13.5 ms: 1.06x slower                                                  |
| nqueens                       | 63.8 ms                                                | 68.8 ms: 1.08x slower                                                  |
| sqlite_synth                  | 1.48 us                                                | 1.61 us: 1.09x slower                                                  |
| json_loads                    | 16.6 us                                                | 18.2 us: 1.10x slower                                                  |
| bench_mp_pool                 | 56.0 ms                                                | 63.9 ms: 1.14x slower                                                  |
| create_gc_cycles              | 1.16 ms                                                | 1.33 ms: 1.15x slower                                                  |
| coverage                      | 41.2 ms                                                | 48.3 ms: 1.17x slower                                                  |
| gc_traversal                  | 2.71 ms                                                | 3.23 ms: 1.19x slower                                                  |
| async_generators              | 233 ms                                                 | 290 ms: 1.24x slower                                                   |
| telco                         | 3.49 ms                                                | 4.76 ms: 1.37x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.27x faster                                                           |

Benchmark hidden because not significant (1): many_optionals
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250311-3.14.0a5+-e0bc9d2-JIT/bm-20250311-darwin-arm64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.279x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: 1.15x