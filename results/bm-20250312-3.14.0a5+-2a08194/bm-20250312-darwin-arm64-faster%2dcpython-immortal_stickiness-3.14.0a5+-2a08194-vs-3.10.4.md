# Results vs. 3.10.4

- fork: faster-cpython
- ref: immortal_stickiness
- machine: darwin-arm64
- commit hash: 2a08194
- commit date: 2025-03-12
- overall geometric mean: 1.290x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 170 ms: 1.18x faster                                                            |
| docutils       | 1.74 sec                                               | 1.49 sec: 1.17x faster                                                          |
| html5lib       | 43.5 ms                                                | 32.3 ms: 1.35x faster                                                           |
| sphinx         | 729 ms                                                 | 596 ms: 1.22x faster                                                            |
| Geometric mean | (ref)                                                  | 1.23x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|-------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 65.4 ms: 5.99x faster                                                           |
| async_tree_eager_memoization  | 483 ms                                                 | 147 ms: 3.29x faster                                                            |
| async_tree_eager_io           | 1.01 sec                                               | 386 ms: 2.63x faster                                                            |
| async_tree_io                 | 1.02 sec                                               | 399 ms: 2.55x faster                                                            |
| async_tree_memoization        | 481 ms                                                 | 208 ms: 2.31x faster                                                            |
| async_tree_none               | 391 ms                                                 | 172 ms: 2.28x faster                                                            |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 362 ms: 1.85x faster                                                            |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 422 ms: 1.58x faster                                                            |
| coroutines                    | 20.5 ms                                                | 17.3 ms: 1.18x faster                                                           |
| async_generators              | 233 ms                                                 | 264 ms: 1.13x slower                                                            |
| Geometric mean                | (ref)                                                  | 2.01x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 52.6 ms: 1.38x faster                                                           |
| nbody          | 92.5 ms                                                | 81.0 ms: 1.14x faster                                                           |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                  | 1.16x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 75.3 ms: 1.27x faster                                                           |
| regex_dna      | 175 ms                                                 | 141 ms: 1.24x faster                                                            |
| regex_v8       | 19.1 ms                                                | 15.9 ms: 1.20x faster                                                           |
| regex_effbot   | 2.34 ms                                                | 2.27 ms: 1.03x faster                                                           |
| Geometric mean | (ref)                                                  | 1.18x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 285 us                                                 | 221 us: 1.29x faster                                                            |
| tomli_loads          | 1.72 sec                                               | 1.40 sec: 1.23x faster                                                          |
| unpickle_pure_python | 198 us                                                 | 164 us: 1.21x faster                                                            |
| json_dumps           | 8.31 ms                                                | 7.50 ms: 1.11x faster                                                           |
| xml_etree_parse      | 109 ms                                                 | 99.8 ms: 1.10x faster                                                           |
| xml_etree_process    | 44.6 ms                                                | 40.9 ms: 1.09x faster                                                           |
| xml_etree_iterparse  | 74.5 ms                                                | 73.8 ms: 1.01x faster                                                           |
| xml_etree_generate   | 53.9 ms                                                | 56.0 ms: 1.04x slower                                                           |
| json_loads           | 16.6 us                                                | 18.0 us: 1.09x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 17.8 ms: 1.10x faster                                                           |
| python_startup_no_site | 12.8 ms                                                | 13.7 ms: 1.07x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 7.96 ms: 1.23x faster                                                           |
| genshi_text     | 17.7 ms                                                | 15.3 ms: 1.16x faster                                                           |
| genshi_xml      | 35.1 ms                                                | 31.7 ms: 1.11x faster                                                           |
| django_template | 24.4 ms                                                | 22.8 ms: 1.07x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.14x faster                                                                    |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|-------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 65.4 ms: 5.99x faster                                                           |
| async_tree_eager_memoization  | 483 ms                                                 | 147 ms: 3.29x faster                                                            |
| typing_runtime_protocols      | 326 us                                                 | 100.0 us: 3.26x faster                                                          |
| subparsers                    | 39.8 ms                                                | 12.7 ms: 3.14x faster                                                           |
| async_tree_eager_io           | 1.01 sec                                               | 386 ms: 2.63x faster                                                            |
| async_tree_io                 | 1.02 sec                                               | 399 ms: 2.55x faster                                                            |
| async_tree_memoization        | 481 ms                                                 | 208 ms: 2.31x faster                                                            |
| async_tree_none               | 391 ms                                                 | 172 ms: 2.28x faster                                                            |
| deltablue                     | 4.99 ms                                                | 2.65 ms: 1.88x faster                                                           |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 362 ms: 1.85x faster                                                            |
| go                            | 163 ms                                                 | 92.7 ms: 1.76x faster                                                           |
| raytrace                      | 327 ms                                                 | 192 ms: 1.70x faster                                                            |
| deepcopy_memo                 | 34.7 us                                                | 20.4 us: 1.70x faster                                                           |
| deepcopy                      | 276 us                                                 | 164 us: 1.68x faster                                                            |
| logging_silent                | 117 ns                                                 | 73.3 ns: 1.60x faster                                                           |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 422 ms: 1.58x faster                                                            |
| scimark_sor                   | 140 ms                                                 | 88.3 ms: 1.58x faster                                                           |
| scimark_monte_carlo           | 72.4 ms                                                | 47.1 ms: 1.54x faster                                                           |
| chaos                         | 67.7 ms                                                | 44.5 ms: 1.52x faster                                                           |
| richards_super                | 61.0 ms                                                | 41.7 ms: 1.46x faster                                                           |
| richards                      | 52.3 ms                                                | 37.2 ms: 1.40x faster                                                           |
| dulwich_log                   | 35.6 ms                                                | 25.6 ms: 1.39x faster                                                           |
| pylint                        | 231 ms                                                 | 168 ms: 1.38x faster                                                            |
| float                         | 72.4 ms                                                | 52.6 ms: 1.38x faster                                                           |
| deepcopy_reduce               | 2.32 us                                                | 1.70 us: 1.37x faster                                                           |
| html5lib                      | 43.5 ms                                                | 32.3 ms: 1.35x faster                                                           |
| comprehensions                | 17.3 us                                                | 12.9 us: 1.34x faster                                                           |
| sqlalchemy_imperative         | 9.07 ms                                                | 6.92 ms: 1.31x faster                                                           |
| scimark_lu                    | 103 ms                                                 | 79.2 ms: 1.29x faster                                                           |
| pprint_pformat                | 1.33 sec                                               | 1.03 sec: 1.29x faster                                                          |
| pickle_pure_python            | 285 us                                                 | 221 us: 1.29x faster                                                            |
| pprint_safe_repr              | 648 ms                                                 | 506 ms: 1.28x faster                                                            |
| logging_format                | 5.03 us                                                | 3.94 us: 1.28x faster                                                           |
| pycparser                     | 887 ms                                                 | 695 ms: 1.28x faster                                                            |
| pyflate                       | 448 ms                                                 | 351 ms: 1.28x faster                                                            |
| generators                    | 31.7 ms                                                | 24.9 ms: 1.27x faster                                                           |
| k_core                        | 2.01 sec                                               | 1.58 sec: 1.27x faster                                                          |
| regex_compile                 | 95.6 ms                                                | 75.3 ms: 1.27x faster                                                           |
| logging_simple                | 4.59 us                                                | 3.62 us: 1.27x faster                                                           |
| hexiom                        | 6.25 ms                                                | 4.96 ms: 1.26x faster                                                           |
| sqlalchemy_declarative        | 75.7 ms                                                | 61.0 ms: 1.24x faster                                                           |
| regex_dna                     | 175 ms                                                 | 141 ms: 1.24x faster                                                            |
| mako                          | 9.81 ms                                                | 7.96 ms: 1.23x faster                                                           |
| tomli_loads                   | 1.72 sec                                               | 1.40 sec: 1.23x faster                                                          |
| thrift                        | 562 us                                                 | 459 us: 1.22x faster                                                            |
| sphinx                        | 729 ms                                                 | 596 ms: 1.22x faster                                                            |
| unpickle_pure_python          | 198 us                                                 | 164 us: 1.21x faster                                                            |
| regex_v8                      | 19.1 ms                                                | 15.9 ms: 1.20x faster                                                           |
| crypto_pyaes                  | 73.3 ms                                                | 60.9 ms: 1.20x faster                                                           |
| sympy_sum                     | 92.7 ms                                                | 77.3 ms: 1.20x faster                                                           |
| spectral_norm                 | 95.3 ms                                                | 79.9 ms: 1.19x faster                                                           |
| coroutines                    | 20.5 ms                                                | 17.3 ms: 1.18x faster                                                           |
| 2to3                          | 201 ms                                                 | 170 ms: 1.18x faster                                                            |
| docutils                      | 1.74 sec                                               | 1.49 sec: 1.17x faster                                                          |
| scimark_fft                   | 225 ms                                                 | 193 ms: 1.17x faster                                                            |
| genshi_text                   | 17.7 ms                                                | 15.3 ms: 1.16x faster                                                           |
| nbody                         | 92.5 ms                                                | 81.0 ms: 1.14x faster                                                           |
| sympy_str                     | 166 ms                                                 | 148 ms: 1.12x faster                                                            |
| genshi_xml                    | 35.1 ms                                                | 31.7 ms: 1.11x faster                                                           |
| json_dumps                    | 8.31 ms                                                | 7.50 ms: 1.11x faster                                                           |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.09 ms: 1.11x faster                                                           |
| python_startup                | 19.6 ms                                                | 17.8 ms: 1.10x faster                                                           |
| xml_etree_parse               | 109 ms                                                 | 99.8 ms: 1.10x faster                                                           |
| pathlib                       | 25.7 ms                                                | 23.5 ms: 1.09x faster                                                           |
| sympy_integrate               | 13.2 ms                                                | 12.1 ms: 1.09x faster                                                           |
| xml_etree_process             | 44.6 ms                                                | 40.9 ms: 1.09x faster                                                           |
| sympy_expand                  | 269 ms                                                 | 248 ms: 1.09x faster                                                            |
| mdp                           | 1.65 sec                                               | 1.53 sec: 1.08x faster                                                          |
| bench_thread_pool             | 545 us                                                 | 504 us: 1.08x faster                                                            |
| django_template               | 24.4 ms                                                | 22.8 ms: 1.07x faster                                                           |
| many_optionals                | 486 us                                                 | 465 us: 1.04x faster                                                            |
| bpe_tokeniser                 | 3.44 sec                                               | 3.30 sec: 1.04x faster                                                          |
| regex_effbot                  | 2.34 ms                                                | 2.27 ms: 1.03x faster                                                           |
| dask                          | 789 ms                                                 | 772 ms: 1.02x faster                                                            |
| meteor_contest                | 77.8 ms                                                | 76.4 ms: 1.02x faster                                                           |
| xml_etree_iterparse           | 74.5 ms                                                | 73.8 ms: 1.01x faster                                                           |
| connected_components          | 318 ms                                                 | 317 ms: 1.00x faster                                                            |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                                            |
| fannkuch                      | 303 ms                                                 | 308 ms: 1.02x slower                                                            |
| json                          | 3.10 ms                                                | 3.19 ms: 1.03x slower                                                           |
| sqlite_synth                  | 1.48 us                                                | 1.53 us: 1.04x slower                                                           |
| xml_etree_generate            | 53.9 ms                                                | 56.0 ms: 1.04x slower                                                           |
| shortest_path                 | 328 ms                                                 | 343 ms: 1.04x slower                                                            |
| python_startup_no_site        | 12.8 ms                                                | 13.7 ms: 1.07x slower                                                           |
| nqueens                       | 63.8 ms                                                | 68.8 ms: 1.08x slower                                                           |
| bench_mp_pool                 | 56.0 ms                                                | 60.9 ms: 1.09x slower                                                           |
| json_loads                    | 16.6 us                                                | 18.0 us: 1.09x slower                                                           |
| create_gc_cycles              | 1.16 ms                                                | 1.29 ms: 1.11x slower                                                           |
| coverage                      | 41.2 ms                                                | 46.4 ms: 1.13x slower                                                           |
| async_generators              | 233 ms                                                 | 264 ms: 1.13x slower                                                            |
| gc_traversal                  | 2.71 ms                                                | 3.14 ms: 1.16x slower                                                           |
| telco                         | 3.49 ms                                                | 4.68 ms: 1.34x slower                                                           |
| Geometric mean                | (ref)                                                  | 1.29x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250312-3.14.0a5+-2a08194/bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.290x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: 1.14x