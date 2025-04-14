# Results vs. 3.10.4

- fork: faster-cpython
- ref: immortal_stickiness
- machine: darwin-arm64
- commit hash: 490cf8d
- commit date: 2025-03-12
- overall geometric mean: 1.290x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 173 ms: 1.17x faster                                                            |
| docutils       | 1.74 sec                                               | 1.49 sec: 1.16x faster                                                          |
| html5lib       | 43.5 ms                                                | 31.7 ms: 1.38x faster                                                           |
| sphinx         | 729 ms                                                 | 601 ms: 1.21x faster                                                            |
| Geometric mean | (ref)                                                  | 1.23x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|-------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 67.3 ms: 5.82x faster                                                           |
| async_tree_eager_memoization  | 483 ms                                                 | 149 ms: 3.24x faster                                                            |
| async_tree_eager_io           | 1.01 sec                                               | 389 ms: 2.61x faster                                                            |
| async_tree_io                 | 1.02 sec                                               | 401 ms: 2.53x faster                                                            |
| async_tree_memoization        | 481 ms                                                 | 212 ms: 2.27x faster                                                            |
| async_tree_none               | 391 ms                                                 | 175 ms: 2.24x faster                                                            |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 365 ms: 1.83x faster                                                            |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 426 ms: 1.57x faster                                                            |
| coroutines                    | 20.5 ms                                                | 17.6 ms: 1.17x faster                                                           |
| async_generators              | 233 ms                                                 | 265 ms: 1.14x slower                                                            |
| Geometric mean                | (ref)                                                  | 1.98x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 52.1 ms: 1.39x faster                                                           |
| nbody          | 92.5 ms                                                | 80.1 ms: 1.15x faster                                                           |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                  | 1.17x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 75.9 ms: 1.26x faster                                                           |
| regex_dna      | 175 ms                                                 | 141 ms: 1.24x faster                                                            |
| regex_v8       | 19.1 ms                                                | 15.9 ms: 1.21x faster                                                           |
| regex_effbot   | 2.34 ms                                                | 2.27 ms: 1.03x faster                                                           |
| Geometric mean | (ref)                                                  | 1.18x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.72 sec                                               | 1.32 sec: 1.30x faster                                                          |
| pickle_pure_python   | 285 us                                                 | 229 us: 1.24x faster                                                            |
| unpickle_pure_python | 198 us                                                 | 166 us: 1.19x faster                                                            |
| json_dumps           | 8.31 ms                                                | 7.50 ms: 1.11x faster                                                           |
| xml_etree_process    | 44.6 ms                                                | 41.3 ms: 1.08x faster                                                           |
| xml_etree_parse      | 109 ms                                                 | 104 ms: 1.05x faster                                                            |
| xml_etree_generate   | 53.9 ms                                                | 56.9 ms: 1.05x slower                                                           |
| json_loads           | 16.6 us                                                | 18.0 us: 1.09x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                                    |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 17.7 ms: 1.11x faster                                                           |
| python_startup_no_site | 12.8 ms                                                | 13.4 ms: 1.05x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 8.11 ms: 1.21x faster                                                           |
| genshi_text     | 17.7 ms                                                | 15.9 ms: 1.11x faster                                                           |
| genshi_xml      | 35.1 ms                                                | 32.5 ms: 1.08x faster                                                           |
| django_template | 24.4 ms                                                | 23.0 ms: 1.06x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.12x faster                                                                    |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|-------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 67.3 ms: 5.82x faster                                                           |
| async_tree_eager_memoization  | 483 ms                                                 | 149 ms: 3.24x faster                                                            |
| typing_runtime_protocols      | 326 us                                                 | 101 us: 3.24x faster                                                            |
| subparsers                    | 39.8 ms                                                | 12.8 ms: 3.11x faster                                                           |
| async_tree_eager_io           | 1.01 sec                                               | 389 ms: 2.61x faster                                                            |
| async_tree_io                 | 1.02 sec                                               | 401 ms: 2.53x faster                                                            |
| async_tree_memoization        | 481 ms                                                 | 212 ms: 2.27x faster                                                            |
| async_tree_none               | 391 ms                                                 | 175 ms: 2.24x faster                                                            |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 365 ms: 1.83x faster                                                            |
| deltablue                     | 4.99 ms                                                | 2.76 ms: 1.81x faster                                                           |
| go                            | 163 ms                                                 | 94.2 ms: 1.73x faster                                                           |
| raytrace                      | 327 ms                                                 | 189 ms: 1.73x faster                                                            |
| deepcopy                      | 276 us                                                 | 166 us: 1.66x faster                                                            |
| deepcopy_memo                 | 34.7 us                                                | 21.4 us: 1.62x faster                                                           |
| logging_silent                | 117 ns                                                 | 73.0 ns: 1.60x faster                                                           |
| scimark_sor                   | 140 ms                                                 | 87.5 ms: 1.60x faster                                                           |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 426 ms: 1.57x faster                                                            |
| chaos                         | 67.7 ms                                                | 43.7 ms: 1.55x faster                                                           |
| richards_super                | 61.0 ms                                                | 40.2 ms: 1.51x faster                                                           |
| scimark_monte_carlo           | 72.4 ms                                                | 47.8 ms: 1.51x faster                                                           |
| richards                      | 52.3 ms                                                | 34.9 ms: 1.50x faster                                                           |
| dulwich_log                   | 35.6 ms                                                | 25.6 ms: 1.39x faster                                                           |
| float                         | 72.4 ms                                                | 52.1 ms: 1.39x faster                                                           |
| html5lib                      | 43.5 ms                                                | 31.7 ms: 1.38x faster                                                           |
| pyflate                       | 448 ms                                                 | 327 ms: 1.37x faster                                                            |
| pylint                        | 231 ms                                                 | 170 ms: 1.36x faster                                                            |
| spectral_norm                 | 95.3 ms                                                | 70.2 ms: 1.36x faster                                                           |
| deepcopy_reduce               | 2.32 us                                                | 1.72 us: 1.35x faster                                                           |
| comprehensions                | 17.3 us                                                | 13.0 us: 1.33x faster                                                           |
| sqlalchemy_imperative         | 9.07 ms                                                | 6.87 ms: 1.32x faster                                                           |
| scimark_lu                    | 103 ms                                                 | 77.9 ms: 1.32x faster                                                           |
| tomli_loads                   | 1.72 sec                                               | 1.32 sec: 1.30x faster                                                          |
| k_core                        | 2.01 sec                                               | 1.56 sec: 1.29x faster                                                          |
| logging_format                | 5.03 us                                                | 3.90 us: 1.29x faster                                                           |
| pprint_pformat                | 1.33 sec                                               | 1.04 sec: 1.28x faster                                                          |
| logging_simple                | 4.59 us                                                | 3.59 us: 1.28x faster                                                           |
| pycparser                     | 887 ms                                                 | 698 ms: 1.27x faster                                                            |
| pprint_safe_repr              | 648 ms                                                 | 513 ms: 1.26x faster                                                            |
| regex_compile                 | 95.6 ms                                                | 75.9 ms: 1.26x faster                                                           |
| pickle_pure_python            | 285 us                                                 | 229 us: 1.24x faster                                                            |
| regex_dna                     | 175 ms                                                 | 141 ms: 1.24x faster                                                            |
| crypto_pyaes                  | 73.3 ms                                                | 59.2 ms: 1.24x faster                                                           |
| hexiom                        | 6.25 ms                                                | 5.05 ms: 1.24x faster                                                           |
| sqlalchemy_declarative        | 75.7 ms                                                | 61.5 ms: 1.23x faster                                                           |
| thrift                        | 562 us                                                 | 460 us: 1.22x faster                                                            |
| sphinx                        | 729 ms                                                 | 601 ms: 1.21x faster                                                            |
| mako                          | 9.81 ms                                                | 8.11 ms: 1.21x faster                                                           |
| regex_v8                      | 19.1 ms                                                | 15.9 ms: 1.21x faster                                                           |
| unpickle_pure_python          | 198 us                                                 | 166 us: 1.19x faster                                                            |
| sympy_sum                     | 92.7 ms                                                | 78.2 ms: 1.19x faster                                                           |
| scimark_fft                   | 225 ms                                                 | 193 ms: 1.17x faster                                                            |
| 2to3                          | 201 ms                                                 | 173 ms: 1.17x faster                                                            |
| coroutines                    | 20.5 ms                                                | 17.6 ms: 1.17x faster                                                           |
| docutils                      | 1.74 sec                                               | 1.49 sec: 1.16x faster                                                          |
| nbody                         | 92.5 ms                                                | 80.1 ms: 1.15x faster                                                           |
| generators                    | 31.7 ms                                                | 27.8 ms: 1.14x faster                                                           |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.05 ms: 1.12x faster                                                           |
| genshi_text                   | 17.7 ms                                                | 15.9 ms: 1.11x faster                                                           |
| python_startup                | 19.6 ms                                                | 17.7 ms: 1.11x faster                                                           |
| json_dumps                    | 8.31 ms                                                | 7.50 ms: 1.11x faster                                                           |
| sympy_str                     | 166 ms                                                 | 150 ms: 1.10x faster                                                            |
| sympy_integrate               | 13.2 ms                                                | 12.1 ms: 1.09x faster                                                           |
| pathlib                       | 25.7 ms                                                | 23.7 ms: 1.09x faster                                                           |
| xml_etree_process             | 44.6 ms                                                | 41.3 ms: 1.08x faster                                                           |
| genshi_xml                    | 35.1 ms                                                | 32.5 ms: 1.08x faster                                                           |
| bpe_tokeniser                 | 3.44 sec                                               | 3.19 sec: 1.08x faster                                                          |
| sympy_expand                  | 269 ms                                                 | 251 ms: 1.07x faster                                                            |
| mdp                           | 1.65 sec                                               | 1.54 sec: 1.07x faster                                                          |
| django_template               | 24.4 ms                                                | 23.0 ms: 1.06x faster                                                           |
| bench_thread_pool             | 545 us                                                 | 514 us: 1.06x faster                                                            |
| xml_etree_parse               | 109 ms                                                 | 104 ms: 1.05x faster                                                            |
| many_optionals                | 486 us                                                 | 466 us: 1.04x faster                                                            |
| meteor_contest                | 77.8 ms                                                | 75.6 ms: 1.03x faster                                                           |
| regex_effbot                  | 2.34 ms                                                | 2.27 ms: 1.03x faster                                                           |
| dask                          | 789 ms                                                 | 769 ms: 1.03x faster                                                            |
| fannkuch                      | 303 ms                                                 | 296 ms: 1.02x faster                                                            |
| connected_components          | 318 ms                                                 | 312 ms: 1.02x faster                                                            |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                                            |
| json                          | 3.10 ms                                                | 3.17 ms: 1.02x slower                                                           |
| shortest_path                 | 328 ms                                                 | 339 ms: 1.03x slower                                                            |
| sqlite_synth                  | 1.48 us                                                | 1.53 us: 1.04x slower                                                           |
| nqueens                       | 63.8 ms                                                | 66.4 ms: 1.04x slower                                                           |
| python_startup_no_site        | 12.8 ms                                                | 13.4 ms: 1.05x slower                                                           |
| xml_etree_generate            | 53.9 ms                                                | 56.9 ms: 1.05x slower                                                           |
| bench_mp_pool                 | 56.0 ms                                                | 60.4 ms: 1.08x slower                                                           |
| json_loads                    | 16.6 us                                                | 18.0 us: 1.09x slower                                                           |
| create_gc_cycles              | 1.16 ms                                                | 1.30 ms: 1.11x slower                                                           |
| coverage                      | 41.2 ms                                                | 46.7 ms: 1.13x slower                                                           |
| async_generators              | 233 ms                                                 | 265 ms: 1.14x slower                                                            |
| gc_traversal                  | 2.71 ms                                                | 3.13 ms: 1.15x slower                                                           |
| telco                         | 3.49 ms                                                | 4.66 ms: 1.34x slower                                                           |
| Geometric mean                | (ref)                                                  | 1.29x faster                                                                    |

Benchmark hidden because not significant (2): xml_etree_iterparse, asyncio_websockets
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250312-3.14.0a5+-490cf8d/bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.290x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: 1.15x