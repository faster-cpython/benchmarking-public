# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: clang_hot
- machine: darwin-arm64
- commit hash: 37fb620
- commit date: 2025-03-06
- overall geometric mean: 1.254x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 176 ms: 1.14x faster                                                  |
| docutils       | 1.74 sec                                               | 1.50 sec: 1.16x faster                                                |
| html5lib       | 43.5 ms                                                | 33.2 ms: 1.31x faster                                                 |
| sphinx         | 729 ms                                                 | 643 ms: 1.13x faster                                                  |
| Geometric mean | (ref)                                                  | 1.18x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 68.2 ms: 5.74x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 150 ms: 3.22x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 394 ms: 2.58x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 398 ms: 2.56x faster                                                  |
| async_tree_none               | 391 ms                                                 | 178 ms: 2.20x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 222 ms: 2.17x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 365 ms: 1.83x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 437 ms: 1.53x faster                                                  |
| coroutines                    | 20.5 ms                                                | 18.5 ms: 1.11x faster                                                 |
| async_generators              | 233 ms                                                 | 267 ms: 1.15x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.95x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 54.6 ms: 1.33x faster                                                 |
| nbody          | 92.5 ms                                                | 91.7 ms: 1.01x faster                                                 |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 175 ms                                                 | 141 ms: 1.24x faster                                                  |
| regex_compile  | 95.6 ms                                                | 77.9 ms: 1.23x faster                                                 |
| regex_v8       | 19.1 ms                                                | 16.9 ms: 1.13x faster                                                 |
| regex_effbot   | 2.34 ms                                                | 2.27 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.15x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 285 us                                                 | 230 us: 1.24x faster                                                  |
| tomli_loads          | 1.72 sec                                               | 1.43 sec: 1.20x faster                                                |
| unpickle_pure_python | 198 us                                                 | 170 us: 1.17x faster                                                  |
| json_dumps           | 8.31 ms                                                | 7.59 ms: 1.09x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 104 ms: 1.06x faster                                                  |
| xml_etree_process    | 44.6 ms                                                | 42.9 ms: 1.04x faster                                                 |
| json_loads           | 16.6 us                                                | 17.7 us: 1.07x slower                                                 |
| xml_etree_generate   | 53.9 ms                                                | 58.0 ms: 1.08x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 19.0 ms: 1.04x faster                                                 |
| python_startup_no_site | 12.8 ms                                                | 14.0 ms: 1.10x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 8.39 ms: 1.17x faster                                                 |
| genshi_text     | 17.7 ms                                                | 16.3 ms: 1.09x faster                                                 |
| genshi_xml      | 35.1 ms                                                | 33.8 ms: 1.04x faster                                                 |
| django_template | 24.4 ms                                                | 24.2 ms: 1.01x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                          |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 68.2 ms: 5.74x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 150 ms: 3.22x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 102 us: 3.20x faster                                                  |
| subparsers                    | 39.8 ms                                                | 13.0 ms: 3.07x faster                                                 |
| async_tree_eager_io           | 1.01 sec                                               | 394 ms: 2.58x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 398 ms: 2.56x faster                                                  |
| async_tree_none               | 391 ms                                                 | 178 ms: 2.20x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 222 ms: 2.17x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 365 ms: 1.83x faster                                                  |
| deltablue                     | 4.99 ms                                                | 2.76 ms: 1.81x faster                                                 |
| go                            | 163 ms                                                 | 94.8 ms: 1.72x faster                                                 |
| deepcopy_memo                 | 34.7 us                                                | 20.9 us: 1.66x faster                                                 |
| deepcopy                      | 276 us                                                 | 168 us: 1.64x faster                                                  |
| logging_silent                | 117 ns                                                 | 73.2 ns: 1.60x faster                                                 |
| raytrace                      | 327 ms                                                 | 212 ms: 1.54x faster                                                  |
| chaos                         | 67.7 ms                                                | 44.0 ms: 1.54x faster                                                 |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 437 ms: 1.53x faster                                                  |
| sqlglot_parse                 | 1.35 ms                                                | 890 us: 1.52x faster                                                  |
| scimark_sor                   | 140 ms                                                 | 95.4 ms: 1.47x faster                                                 |
| sqlglot_transpile             | 1.56 ms                                                | 1.07 ms: 1.46x faster                                                 |
| scimark_monte_carlo           | 72.4 ms                                                | 49.9 ms: 1.45x faster                                                 |
| richards_super                | 61.0 ms                                                | 42.9 ms: 1.42x faster                                                 |
| pylint                        | 231 ms                                                 | 171 ms: 1.35x faster                                                  |
| float                         | 72.4 ms                                                | 54.6 ms: 1.33x faster                                                 |
| deepcopy_reduce               | 2.32 us                                                | 1.75 us: 1.32x faster                                                 |
| comprehensions                | 17.3 us                                                | 13.1 us: 1.32x faster                                                 |
| html5lib                      | 43.5 ms                                                | 33.2 ms: 1.31x faster                                                 |
| richards                      | 52.3 ms                                                | 39.9 ms: 1.31x faster                                                 |
| k_core                        | 2.01 sec                                               | 1.54 sec: 1.31x faster                                                |
| sqlalchemy_imperative         | 9.07 ms                                                | 7.07 ms: 1.28x faster                                                 |
| pyflate                       | 448 ms                                                 | 351 ms: 1.28x faster                                                  |
| pycparser                     | 887 ms                                                 | 702 ms: 1.26x faster                                                  |
| logging_format                | 5.03 us                                                | 4.04 us: 1.25x faster                                                 |
| regex_dna                     | 175 ms                                                 | 141 ms: 1.24x faster                                                  |
| crypto_pyaes                  | 73.3 ms                                                | 59.2 ms: 1.24x faster                                                 |
| logging_simple                | 4.59 us                                                | 3.71 us: 1.24x faster                                                 |
| pickle_pure_python            | 285 us                                                 | 230 us: 1.24x faster                                                  |
| scimark_lu                    | 103 ms                                                 | 83.1 ms: 1.23x faster                                                 |
| regex_compile                 | 95.6 ms                                                | 77.9 ms: 1.23x faster                                                 |
| thrift                        | 562 us                                                 | 464 us: 1.21x faster                                                  |
| sqlalchemy_declarative        | 75.7 ms                                                | 62.7 ms: 1.21x faster                                                 |
| tomli_loads                   | 1.72 sec                                               | 1.43 sec: 1.20x faster                                                |
| pprint_pformat                | 1.33 sec                                               | 1.11 sec: 1.20x faster                                                |
| hexiom                        | 6.25 ms                                                | 5.27 ms: 1.19x faster                                                 |
| dulwich_log                   | 35.6 ms                                                | 30.0 ms: 1.18x faster                                                 |
| pprint_safe_repr              | 648 ms                                                 | 549 ms: 1.18x faster                                                  |
| sympy_sum                     | 92.7 ms                                                | 79.2 ms: 1.17x faster                                                 |
| mako                          | 9.81 ms                                                | 8.39 ms: 1.17x faster                                                 |
| unpickle_pure_python          | 198 us                                                 | 170 us: 1.17x faster                                                  |
| docutils                      | 1.74 sec                                               | 1.50 sec: 1.16x faster                                                |
| scimark_fft                   | 225 ms                                                 | 196 ms: 1.15x faster                                                  |
| 2to3                          | 201 ms                                                 | 176 ms: 1.14x faster                                                  |
| sphinx                        | 729 ms                                                 | 643 ms: 1.13x faster                                                  |
| regex_v8                      | 19.1 ms                                                | 16.9 ms: 1.13x faster                                                 |
| spectral_norm                 | 95.3 ms                                                | 84.4 ms: 1.13x faster                                                 |
| coroutines                    | 20.5 ms                                                | 18.5 ms: 1.11x faster                                                 |
| json_dumps                    | 8.31 ms                                                | 7.59 ms: 1.09x faster                                                 |
| genshi_text                   | 17.7 ms                                                | 16.3 ms: 1.09x faster                                                 |
| sympy_str                     | 166 ms                                                 | 153 ms: 1.09x faster                                                  |
| pathlib                       | 25.7 ms                                                | 23.8 ms: 1.08x faster                                                 |
| generators                    | 31.7 ms                                                | 29.3 ms: 1.08x faster                                                 |
| sympy_integrate               | 13.2 ms                                                | 12.2 ms: 1.08x faster                                                 |
| bpe_tokeniser                 | 3.44 sec                                               | 3.24 sec: 1.06x faster                                                |
| mdp                           | 1.65 sec                                               | 1.56 sec: 1.06x faster                                                |
| xml_etree_parse               | 109 ms                                                 | 104 ms: 1.06x faster                                                  |
| sympy_expand                  | 269 ms                                                 | 256 ms: 1.05x faster                                                  |
| bench_thread_pool             | 545 us                                                 | 522 us: 1.04x faster                                                  |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.28 ms: 1.04x faster                                                 |
| xml_etree_process             | 44.6 ms                                                | 42.9 ms: 1.04x faster                                                 |
| genshi_xml                    | 35.1 ms                                                | 33.8 ms: 1.04x faster                                                 |
| sqlglot_optimize              | 37.2 ms                                                | 35.9 ms: 1.04x faster                                                 |
| python_startup                | 19.6 ms                                                | 19.0 ms: 1.04x faster                                                 |
| many_optionals                | 486 us                                                 | 470 us: 1.03x faster                                                  |
| fannkuch                      | 303 ms                                                 | 293 ms: 1.03x faster                                                  |
| regex_effbot                  | 2.34 ms                                                | 2.27 ms: 1.03x faster                                                 |
| json                          | 3.10 ms                                                | 3.02 ms: 1.03x faster                                                 |
| dask                          | 789 ms                                                 | 770 ms: 1.02x faster                                                  |
| connected_components          | 318 ms                                                 | 315 ms: 1.01x faster                                                  |
| nbody                         | 92.5 ms                                                | 91.7 ms: 1.01x faster                                                 |
| django_template               | 24.4 ms                                                | 24.2 ms: 1.01x faster                                                 |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                                  |
| nqueens                       | 63.8 ms                                                | 65.0 ms: 1.02x slower                                                 |
| sqlglot_normalize             | 192 ms                                                 | 196 ms: 1.02x slower                                                  |
| shortest_path                 | 328 ms                                                 | 341 ms: 1.04x slower                                                  |
| sqlite_synth                  | 1.48 us                                                | 1.54 us: 1.04x slower                                                 |
| json_loads                    | 16.6 us                                                | 17.7 us: 1.07x slower                                                 |
| xml_etree_generate            | 53.9 ms                                                | 58.0 ms: 1.08x slower                                                 |
| bench_mp_pool                 | 56.0 ms                                                | 61.2 ms: 1.09x slower                                                 |
| python_startup_no_site        | 12.8 ms                                                | 14.0 ms: 1.10x slower                                                 |
| create_gc_cycles              | 1.16 ms                                                | 1.28 ms: 1.10x slower                                                 |
| async_generators              | 233 ms                                                 | 267 ms: 1.15x slower                                                  |
| coverage                      | 41.2 ms                                                | 47.3 ms: 1.15x slower                                                 |
| gc_traversal                  | 2.71 ms                                                | 3.11 ms: 1.15x slower                                                 |
| telco                         | 3.49 ms                                                | 4.74 ms: 1.36x slower                                                 |
| Geometric mean                | (ref)                                                  | 1.25x faster                                                          |

Benchmark hidden because not significant (3): asyncio_websockets, meteor_contest, xml_etree_iterparse
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, tornado_http
Ignored benchmarks (8) of results/bm-20250306-3.14.0a5+-37fb620/bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.254x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: 1.14x