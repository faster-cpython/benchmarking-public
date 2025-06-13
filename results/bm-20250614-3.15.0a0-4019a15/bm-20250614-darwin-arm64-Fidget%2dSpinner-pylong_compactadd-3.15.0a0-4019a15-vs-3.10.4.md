# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: pylong_compactadd
- machine: darwin-arm64
- commit hash: 4019a15
- commit date: 2025-06-14
- overall geometric mean: 1.246x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-darwin-arm64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 170 ms: 1.19x faster                                                         |
| docutils       | 1.74 sec                                               | 1.44 sec: 1.20x faster                                                       |
| html5lib       | 43.5 ms                                                | 31.7 ms: 1.37x faster                                                        |
| sphinx         | 729 ms                                                 | 584 ms: 1.25x faster                                                         |
| Geometric mean | (ref)                                                  | 1.25x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-darwin-arm64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 64.1 ms: 6.12x faster                                                        |
| async_tree_eager_memoization  | 483 ms                                                 | 140 ms: 3.45x faster                                                         |
| async_tree_eager_io           | 1.01 sec                                               | 364 ms: 2.79x faster                                                         |
| async_tree_io                 | 1.02 sec                                               | 380 ms: 2.68x faster                                                         |
| async_tree_memoization        | 481 ms                                                 | 196 ms: 2.46x faster                                                         |
| async_tree_none               | 391 ms                                                 | 165 ms: 2.38x faster                                                         |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 357 ms: 1.88x faster                                                         |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 418 ms: 1.60x faster                                                         |
| coroutines                    | 20.5 ms                                                | 17.1 ms: 1.20x faster                                                        |
| async_generators              | 233 ms                                                 | 262 ms: 1.12x slower                                                         |
| Geometric mean                | (ref)                                                  | 2.07x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-darwin-arm64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 49.6 ms: 1.46x faster                                                        |
| nbody          | 92.5 ms                                                | 73.8 ms: 1.25x faster                                                        |
| pidigits       | 280 ms                                                 | 283 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                  | 1.22x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-darwin-arm64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 71.8 ms: 1.33x faster                                                        |
| regex_dna      | 175 ms                                                 | 143 ms: 1.22x faster                                                         |
| regex_v8       | 19.1 ms                                                | 16.1 ms: 1.19x faster                                                        |
| regex_effbot   | 2.34 ms                                                | 2.35 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                  | 1.18x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-darwin-arm64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 285 us                                                 | 218 us: 1.30x faster                                                         |
| json_dumps           | 8.31 ms                                                | 6.54 ms: 1.27x faster                                                        |
| tomli_loads          | 1.72 sec                                               | 1.36 sec: 1.26x faster                                                       |
| unpickle_pure_python | 198 us                                                 | 160 us: 1.24x faster                                                         |
| xml_etree_process    | 44.6 ms                                                | 38.9 ms: 1.15x faster                                                        |
| xml_etree_parse      | 109 ms                                                 | 103 ms: 1.06x faster                                                         |
| xml_etree_iterparse  | 74.5 ms                                                | 72.7 ms: 1.02x faster                                                        |
| json_loads           | 16.6 us                                                | 16.5 us: 1.01x faster                                                        |
| xml_etree_generate   | 53.9 ms                                                | 53.7 ms: 1.00x faster                                                        |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-darwin-arm64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 15.9 ms: 1.23x faster                                                        |
| python_startup_no_site | 12.8 ms                                                | 11.6 ms: 1.10x faster                                                        |
| Geometric mean         | (ref)                                                  | 1.17x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-darwin-arm64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 7.72 ms: 1.27x faster                                                        |
| genshi_text     | 17.7 ms                                                | 14.6 ms: 1.22x faster                                                        |
| genshi_xml      | 35.1 ms                                                | 31.2 ms: 1.13x faster                                                        |
| django_template | 24.4 ms                                                | 22.0 ms: 1.11x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.18x faster                                                                 |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-darwin-arm64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 64.1 ms: 6.12x faster                                                        |
| async_tree_eager_memoization  | 483 ms                                                 | 140 ms: 3.45x faster                                                         |
| typing_runtime_protocols      | 326 us                                                 | 95.9 us: 3.40x faster                                                        |
| subparsers                    | 39.8 ms                                                | 13.7 ms: 2.91x faster                                                        |
| async_tree_eager_io           | 1.01 sec                                               | 364 ms: 2.79x faster                                                         |
| async_tree_io                 | 1.02 sec                                               | 380 ms: 2.68x faster                                                         |
| async_tree_memoization        | 481 ms                                                 | 196 ms: 2.46x faster                                                         |
| async_tree_none               | 391 ms                                                 | 165 ms: 2.38x faster                                                         |
| mdp                           | 1.65 sec                                               | 761 ms: 2.17x faster                                                         |
| deltablue                     | 4.99 ms                                                | 2.58 ms: 1.94x faster                                                        |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 357 ms: 1.88x faster                                                         |
| go                            | 163 ms                                                 | 87.6 ms: 1.87x faster                                                        |
| raytrace                      | 327 ms                                                 | 180 ms: 1.81x faster                                                         |
| deepcopy_memo                 | 34.7 us                                                | 19.2 us: 1.81x faster                                                        |
| deepcopy                      | 276 us                                                 | 156 us: 1.77x faster                                                         |
| chaos                         | 67.7 ms                                                | 40.1 ms: 1.69x faster                                                        |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 418 ms: 1.60x faster                                                         |
| scimark_sor                   | 140 ms                                                 | 88.7 ms: 1.58x faster                                                        |
| scimark_monte_carlo           | 72.4 ms                                                | 46.2 ms: 1.57x faster                                                        |
| richards_super                | 61.0 ms                                                | 39.7 ms: 1.54x faster                                                        |
| float                         | 72.4 ms                                                | 49.6 ms: 1.46x faster                                                        |
| richards                      | 52.3 ms                                                | 35.8 ms: 1.46x faster                                                        |
| comprehensions                | 17.3 us                                                | 12.0 us: 1.44x faster                                                        |
| pylint                        | 231 ms                                                 | 161 ms: 1.43x faster                                                         |
| dulwich_log                   | 35.6 ms                                                | 25.0 ms: 1.42x faster                                                        |
| pyflate                       | 448 ms                                                 | 317 ms: 1.41x faster                                                         |
| deepcopy_reduce               | 2.32 us                                                | 1.69 us: 1.38x faster                                                        |
| html5lib                      | 43.5 ms                                                | 31.7 ms: 1.37x faster                                                        |
| k_core                        | 2.01 sec                                               | 1.47 sec: 1.37x faster                                                       |
| spectral_norm                 | 95.3 ms                                                | 70.7 ms: 1.35x faster                                                        |
| hexiom                        | 6.25 ms                                                | 4.68 ms: 1.33x faster                                                        |
| regex_compile                 | 95.6 ms                                                | 71.8 ms: 1.33x faster                                                        |
| generators                    | 31.7 ms                                                | 24.1 ms: 1.32x faster                                                        |
| pycparser                     | 887 ms                                                 | 678 ms: 1.31x faster                                                         |
| pickle_pure_python            | 285 us                                                 | 218 us: 1.30x faster                                                         |
| crypto_pyaes                  | 73.3 ms                                                | 57.2 ms: 1.28x faster                                                        |
| mako                          | 9.81 ms                                                | 7.72 ms: 1.27x faster                                                        |
| json_dumps                    | 8.31 ms                                                | 6.54 ms: 1.27x faster                                                        |
| tomli_loads                   | 1.72 sec                                               | 1.36 sec: 1.26x faster                                                       |
| logging_format                | 5.03 us                                                | 4.00 us: 1.26x faster                                                        |
| nbody                         | 92.5 ms                                                | 73.8 ms: 1.25x faster                                                        |
| sphinx                        | 729 ms                                                 | 584 ms: 1.25x faster                                                         |
| logging_simple                | 4.59 us                                                | 3.68 us: 1.25x faster                                                        |
| unpickle_pure_python          | 198 us                                                 | 160 us: 1.24x faster                                                         |
| python_startup                | 19.6 ms                                                | 15.9 ms: 1.23x faster                                                        |
| scimark_lu                    | 103 ms                                                 | 83.5 ms: 1.23x faster                                                        |
| sympy_sum                     | 92.7 ms                                                | 75.5 ms: 1.23x faster                                                        |
| regex_dna                     | 175 ms                                                 | 143 ms: 1.22x faster                                                         |
| genshi_text                   | 17.7 ms                                                | 14.6 ms: 1.22x faster                                                        |
| docutils                      | 1.74 sec                                               | 1.44 sec: 1.20x faster                                                       |
| coroutines                    | 20.5 ms                                                | 17.1 ms: 1.20x faster                                                        |
| sympy_integrate               | 13.2 ms                                                | 11.0 ms: 1.19x faster                                                        |
| regex_v8                      | 19.1 ms                                                | 16.1 ms: 1.19x faster                                                        |
| 2to3                          | 201 ms                                                 | 170 ms: 1.19x faster                                                         |
| pprint_pformat                | 1.33 sec                                               | 1.13 sec: 1.17x faster                                                       |
| pprint_safe_repr              | 648 ms                                                 | 558 ms: 1.16x faster                                                         |
| sympy_str                     | 166 ms                                                 | 143 ms: 1.16x faster                                                         |
| scimark_fft                   | 225 ms                                                 | 195 ms: 1.15x faster                                                         |
| xml_etree_process             | 44.6 ms                                                | 38.9 ms: 1.15x faster                                                        |
| fannkuch                      | 303 ms                                                 | 266 ms: 1.14x faster                                                         |
| genshi_xml                    | 35.1 ms                                                | 31.2 ms: 1.13x faster                                                        |
| sympy_expand                  | 269 ms                                                 | 240 ms: 1.12x faster                                                         |
| bpe_tokeniser                 | 3.44 sec                                               | 3.08 sec: 1.12x faster                                                       |
| django_template               | 24.4 ms                                                | 22.0 ms: 1.11x faster                                                        |
| python_startup_no_site        | 12.8 ms                                                | 11.6 ms: 1.10x faster                                                        |
| pathlib                       | 25.7 ms                                                | 23.9 ms: 1.08x faster                                                        |
| xml_etree_parse               | 109 ms                                                 | 103 ms: 1.06x faster                                                         |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.23 ms: 1.06x faster                                                        |
| meteor_contest                | 77.8 ms                                                | 73.7 ms: 1.06x faster                                                        |
| json                          | 3.10 ms                                                | 2.94 ms: 1.06x faster                                                        |
| many_optionals                | 486 us                                                 | 466 us: 1.04x faster                                                         |
| nqueens                       | 63.8 ms                                                | 61.5 ms: 1.04x faster                                                        |
| connected_components          | 318 ms                                                 | 307 ms: 1.04x faster                                                         |
| dask                          | 789 ms                                                 | 769 ms: 1.03x faster                                                         |
| xml_etree_iterparse           | 74.5 ms                                                | 72.7 ms: 1.02x faster                                                        |
| json_loads                    | 16.6 us                                                | 16.5 us: 1.01x faster                                                        |
| xml_etree_generate            | 53.9 ms                                                | 53.7 ms: 1.00x faster                                                        |
| regex_effbot                  | 2.34 ms                                                | 2.35 ms: 1.01x slower                                                        |
| pidigits                      | 280 ms                                                 | 283 ms: 1.01x slower                                                         |
| sqlite_synth                  | 1.48 us                                                | 1.60 us: 1.08x slower                                                        |
| async_generators              | 233 ms                                                 | 262 ms: 1.12x slower                                                         |
| create_gc_cycles              | 1.16 ms                                                | 1.36 ms: 1.17x slower                                                        |
| gc_traversal                  | 2.71 ms                                                | 3.19 ms: 1.18x slower                                                        |
| telco                         | 3.49 ms                                                | 4.51 ms: 1.29x slower                                                        |
| logging_silent                | 117 ns                                                 | 328 ns: 2.80x slower                                                         |
| coverage                      | 41.2 ms                                                | 290 ms: 7.05x slower                                                         |
| thrift                        | 562 us                                                 | 43.5 ms: 77.38x slower                                                       |
| Geometric mean                | (ref)                                                  | 1.23x faster                                                                 |

Benchmark hidden because not significant (2): asyncio_websockets, shortest_path
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250614-3.15.0a0-4019a15/bm-20250614-darwin-arm64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.246x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: 1.17x