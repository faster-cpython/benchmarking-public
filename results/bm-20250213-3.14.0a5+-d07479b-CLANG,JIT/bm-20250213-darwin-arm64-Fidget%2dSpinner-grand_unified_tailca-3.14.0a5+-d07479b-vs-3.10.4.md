# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: grand_unified_tailca
- machine: darwin-arm64
- commit hash: d07479b
- commit date: 2025-02-13
- overall geometric mean: 1.436x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250213-darwin-arm64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 156 ms: 1.29x faster                                                             |
| docutils       | 1.74 sec                                               | 1.45 sec: 1.20x faster                                                           |
| html5lib       | 43.5 ms                                                | 29.2 ms: 1.49x faster                                                            |
| sphinx         | 729 ms                                                 | 548 ms: 1.33x faster                                                             |
| Geometric mean | (ref)                                                  | 1.32x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250213-darwin-arm64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|-------------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 60.3 ms: 6.50x faster                                                            |
| async_tree_eager_memoization  | 483 ms                                                 | 137 ms: 3.52x faster                                                             |
| async_tree_io                 | 1.02 sec                                               | 343 ms: 2.96x faster                                                             |
| async_tree_eager_io           | 1.01 sec                                               | 347 ms: 2.92x faster                                                             |
| async_tree_memoization        | 481 ms                                                 | 184 ms: 2.61x faster                                                             |
| async_tree_none               | 391 ms                                                 | 152 ms: 2.58x faster                                                             |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 352 ms: 1.90x faster                                                             |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 402 ms: 1.66x faster                                                             |
| coroutines                    | 20.5 ms                                                | 14.9 ms: 1.38x faster                                                            |
| async_generators              | 233 ms                                                 | 263 ms: 1.13x slower                                                             |
| Geometric mean                | (ref)                                                  | 2.18x faster                                                                     |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250213-darwin-arm64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 44.4 ms: 1.63x faster                                                            |
| nbody          | 92.5 ms                                                | 63.8 ms: 1.45x faster                                                            |
| pidigits       | 280 ms                                                 | 280 ms: 1.00x faster                                                             |
| Geometric mean | (ref)                                                  | 1.33x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250213-darwin-arm64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 63.4 ms: 1.51x faster                                                            |
| regex_dna      | 175 ms                                                 | 149 ms: 1.17x faster                                                             |
| regex_v8       | 19.1 ms                                                | 18.3 ms: 1.04x faster                                                            |
| regex_effbot   | 2.34 ms                                                | 2.45 ms: 1.05x slower                                                            |
| Geometric mean | (ref)                                                  | 1.15x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250213-darwin-arm64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 127 us: 1.56x faster                                                             |
| pickle_pure_python   | 285 us                                                 | 185 us: 1.54x faster                                                             |
| tomli_loads          | 1.72 sec                                               | 1.17 sec: 1.47x faster                                                           |
| xml_etree_process    | 44.6 ms                                                | 33.0 ms: 1.35x faster                                                            |
| json_dumps           | 8.31 ms                                                | 7.24 ms: 1.15x faster                                                            |
| xml_etree_parse      | 109 ms                                                 | 97.0 ms: 1.13x faster                                                            |
| xml_etree_generate   | 53.9 ms                                                | 47.8 ms: 1.13x faster                                                            |
| xml_etree_iterparse  | 74.5 ms                                                | 68.8 ms: 1.08x faster                                                            |
| json_loads           | 16.6 us                                                | 17.9 us: 1.08x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.24x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250213-darwin-arm64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 17.2 ms: 1.14x faster                                                            |
| python_startup_no_site | 12.8 ms                                                | 12.7 ms: 1.01x faster                                                            |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250213-darwin-arm64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 6.46 ms: 1.52x faster                                                            |
| genshi_text     | 17.7 ms                                                | 12.7 ms: 1.40x faster                                                            |
| genshi_xml      | 35.1 ms                                                | 27.0 ms: 1.30x faster                                                            |
| django_template | 24.4 ms                                                | 18.9 ms: 1.29x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.37x faster                                                                     |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250213-darwin-arm64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|-------------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 60.3 ms: 6.50x faster                                                            |
| typing_runtime_protocols      | 326 us                                                 | 87.9 us: 3.71x faster                                                            |
| async_tree_eager_memoization  | 483 ms                                                 | 137 ms: 3.52x faster                                                             |
| subparsers                    | 39.8 ms                                                | 11.5 ms: 3.46x faster                                                            |
| async_tree_io                 | 1.02 sec                                               | 343 ms: 2.96x faster                                                             |
| async_tree_eager_io           | 1.01 sec                                               | 347 ms: 2.92x faster                                                             |
| async_tree_memoization        | 481 ms                                                 | 184 ms: 2.61x faster                                                             |
| async_tree_none               | 391 ms                                                 | 152 ms: 2.58x faster                                                             |
| deltablue                     | 4.99 ms                                                | 2.06 ms: 2.42x faster                                                            |
| go                            | 163 ms                                                 | 72.6 ms: 2.25x faster                                                            |
| deepcopy_memo                 | 34.7 us                                                | 16.6 us: 2.09x faster                                                            |
| logging_silent                | 117 ns                                                 | 58.1 ns: 2.02x faster                                                            |
| raytrace                      | 327 ms                                                 | 162 ms: 2.01x faster                                                             |
| deepcopy                      | 276 us                                                 | 138 us: 1.99x faster                                                             |
| richards_super                | 61.0 ms                                                | 31.3 ms: 1.95x faster                                                            |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 352 ms: 1.90x faster                                                             |
| chaos                         | 67.7 ms                                                | 35.8 ms: 1.89x faster                                                            |
| scimark_sor                   | 140 ms                                                 | 74.2 ms: 1.89x faster                                                            |
| richards                      | 52.3 ms                                                | 27.7 ms: 1.89x faster                                                            |
| scimark_monte_carlo           | 72.4 ms                                                | 39.2 ms: 1.85x faster                                                            |
| generators                    | 31.7 ms                                                | 18.1 ms: 1.75x faster                                                            |
| sqlglot_parse                 | 1.35 ms                                                | 811 us: 1.67x faster                                                             |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 402 ms: 1.66x faster                                                             |
| float                         | 72.4 ms                                                | 44.4 ms: 1.63x faster                                                            |
| sqlglot_transpile             | 1.56 ms                                                | 968 us: 1.61x faster                                                             |
| hexiom                        | 6.25 ms                                                | 3.91 ms: 1.60x faster                                                            |
| logging_simple                | 4.59 us                                                | 2.93 us: 1.57x faster                                                            |
| logging_format                | 5.03 us                                                | 3.22 us: 1.56x faster                                                            |
| deepcopy_reduce               | 2.32 us                                                | 1.48 us: 1.56x faster                                                            |
| unpickle_pure_python          | 198 us                                                 | 127 us: 1.56x faster                                                             |
| pylint                        | 231 ms                                                 | 150 ms: 1.54x faster                                                             |
| pickle_pure_python            | 285 us                                                 | 185 us: 1.54x faster                                                             |
| mako                          | 9.81 ms                                                | 6.46 ms: 1.52x faster                                                            |
| pyflate                       | 448 ms                                                 | 296 ms: 1.51x faster                                                             |
| comprehensions                | 17.3 us                                                | 11.5 us: 1.51x faster                                                            |
| regex_compile                 | 95.6 ms                                                | 63.4 ms: 1.51x faster                                                            |
| html5lib                      | 43.5 ms                                                | 29.2 ms: 1.49x faster                                                            |
| tomli_loads                   | 1.72 sec                                               | 1.17 sec: 1.47x faster                                                           |
| scimark_lu                    | 103 ms                                                 | 70.7 ms: 1.45x faster                                                            |
| nbody                         | 92.5 ms                                                | 63.8 ms: 1.45x faster                                                            |
| sqlalchemy_imperative         | 9.07 ms                                                | 6.34 ms: 1.43x faster                                                            |
| crypto_pyaes                  | 73.3 ms                                                | 52.0 ms: 1.41x faster                                                            |
| spectral_norm                 | 95.3 ms                                                | 68.0 ms: 1.40x faster                                                            |
| genshi_text                   | 17.7 ms                                                | 12.7 ms: 1.40x faster                                                            |
| coroutines                    | 20.5 ms                                                | 14.9 ms: 1.38x faster                                                            |
| thrift                        | 562 us                                                 | 411 us: 1.37x faster                                                             |
| sqlalchemy_declarative        | 75.7 ms                                                | 55.3 ms: 1.37x faster                                                            |
| pycparser                     | 887 ms                                                 | 654 ms: 1.36x faster                                                             |
| xml_etree_process             | 44.6 ms                                                | 33.0 ms: 1.35x faster                                                            |
| sympy_sum                     | 92.7 ms                                                | 69.5 ms: 1.33x faster                                                            |
| sphinx                        | 729 ms                                                 | 548 ms: 1.33x faster                                                             |
| k_core                        | 2.01 sec                                               | 1.52 sec: 1.32x faster                                                           |
| pprint_pformat                | 1.33 sec                                               | 1.01 sec: 1.32x faster                                                           |
| dulwich_log                   | 35.6 ms                                                | 27.1 ms: 1.31x faster                                                            |
| genshi_xml                    | 35.1 ms                                                | 27.0 ms: 1.30x faster                                                            |
| 2to3                          | 201 ms                                                 | 156 ms: 1.29x faster                                                             |
| django_template               | 24.4 ms                                                | 18.9 ms: 1.29x faster                                                            |
| pprint_safe_repr              | 648 ms                                                 | 504 ms: 1.29x faster                                                             |
| sympy_integrate               | 13.2 ms                                                | 10.3 ms: 1.27x faster                                                            |
| sympy_str                     | 166 ms                                                 | 131 ms: 1.27x faster                                                             |
| scimark_fft                   | 225 ms                                                 | 183 ms: 1.23x faster                                                             |
| sympy_expand                  | 269 ms                                                 | 221 ms: 1.21x faster                                                             |
| nqueens                       | 63.8 ms                                                | 52.8 ms: 1.21x faster                                                            |
| sqlglot_optimize              | 37.2 ms                                                | 31.0 ms: 1.20x faster                                                            |
| docutils                      | 1.74 sec                                               | 1.45 sec: 1.20x faster                                                           |
| bench_thread_pool             | 545 us                                                 | 457 us: 1.19x faster                                                             |
| bpe_tokeniser                 | 3.44 sec                                               | 2.89 sec: 1.19x faster                                                           |
| regex_dna                     | 175 ms                                                 | 149 ms: 1.17x faster                                                             |
| mdp                           | 1.65 sec                                               | 1.43 sec: 1.15x faster                                                           |
| json_dumps                    | 8.31 ms                                                | 7.24 ms: 1.15x faster                                                            |
| sqlglot_normalize             | 192 ms                                                 | 168 ms: 1.15x faster                                                             |
| pathlib                       | 25.7 ms                                                | 22.5 ms: 1.14x faster                                                            |
| python_startup                | 19.6 ms                                                | 17.2 ms: 1.14x faster                                                            |
| many_optionals                | 486 us                                                 | 427 us: 1.14x faster                                                             |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.01 ms: 1.13x faster                                                            |
| xml_etree_parse               | 109 ms                                                 | 97.0 ms: 1.13x faster                                                            |
| xml_etree_generate            | 53.9 ms                                                | 47.8 ms: 1.13x faster                                                            |
| xml_etree_iterparse           | 74.5 ms                                                | 68.8 ms: 1.08x faster                                                            |
| fannkuch                      | 303 ms                                                 | 284 ms: 1.07x faster                                                             |
| connected_components          | 318 ms                                                 | 299 ms: 1.07x faster                                                             |
| regex_v8                      | 19.1 ms                                                | 18.3 ms: 1.04x faster                                                            |
| meteor_contest                | 77.8 ms                                                | 74.5 ms: 1.04x faster                                                            |
| dask                          | 789 ms                                                 | 766 ms: 1.03x faster                                                             |
| json                          | 3.10 ms                                                | 3.02 ms: 1.03x faster                                                            |
| python_startup_no_site        | 12.8 ms                                                | 12.7 ms: 1.01x faster                                                            |
| shortest_path                 | 328 ms                                                 | 326 ms: 1.01x faster                                                             |
| pidigits                      | 280 ms                                                 | 280 ms: 1.00x faster                                                             |
| sqlite_synth                  | 1.48 us                                                | 1.54 us: 1.04x slower                                                            |
| regex_effbot                  | 2.34 ms                                                | 2.45 ms: 1.05x slower                                                            |
| bench_mp_pool                 | 56.0 ms                                                | 60.2 ms: 1.07x slower                                                            |
| json_loads                    | 16.6 us                                                | 17.9 us: 1.08x slower                                                            |
| coverage                      | 41.2 ms                                                | 44.7 ms: 1.08x slower                                                            |
| create_gc_cycles              | 1.16 ms                                                | 1.27 ms: 1.09x slower                                                            |
| async_generators              | 233 ms                                                 | 263 ms: 1.13x slower                                                             |
| gc_traversal                  | 2.71 ms                                                | 3.10 ms: 1.14x slower                                                            |
| telco                         | 3.49 ms                                                | 4.49 ms: 1.29x slower                                                            |
| Geometric mean                | (ref)                                                  | 1.43x faster                                                                     |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, tornado_http
Ignored benchmarks (8) of results/bm-20250213-3.14.0a5+-d07479b-CLANG,JIT/bm-20250213-darwin-arm64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.436x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.14x