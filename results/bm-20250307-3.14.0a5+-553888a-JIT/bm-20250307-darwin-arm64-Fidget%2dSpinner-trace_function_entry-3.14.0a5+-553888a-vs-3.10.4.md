# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: trace_function_entry
- machine: darwin-arm64
- commit hash: 553888a
- commit date: 2025-03-07
- overall geometric mean: 1.360x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 165 ms: 1.22x faster                                                             |
| html5lib       | 43.5 ms                                                | 29.7 ms: 1.46x faster                                                            |
| sphinx         | 729 ms                                                 | 578 ms: 1.26x faster                                                             |
| Geometric mean | (ref)                                                  | 1.31x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|-------------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 62.1 ms: 6.31x faster                                                            |
| async_tree_eager_memoization  | 483 ms                                                 | 141 ms: 3.42x faster                                                             |
| async_tree_eager_io           | 1.01 sec                                               | 362 ms: 2.80x faster                                                             |
| async_tree_io                 | 1.02 sec                                               | 366 ms: 2.78x faster                                                             |
| async_tree_none               | 391 ms                                                 | 161 ms: 2.43x faster                                                             |
| async_tree_memoization        | 481 ms                                                 | 203 ms: 2.37x faster                                                             |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 359 ms: 1.87x faster                                                             |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 417 ms: 1.60x faster                                                             |
| coroutines                    | 20.5 ms                                                | 16.8 ms: 1.22x faster                                                            |
| async_generators              | 233 ms                                                 | 255 ms: 1.09x slower                                                             |
| Geometric mean                | (ref)                                                  | 2.08x faster                                                                     |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 47.9 ms: 1.51x faster                                                            |
| nbody          | 92.5 ms                                                | 67.7 ms: 1.37x faster                                                            |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                  | 1.27x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 71.0 ms: 1.35x faster                                                            |
| regex_dna      | 175 ms                                                 | 141 ms: 1.24x faster                                                             |
| regex_v8       | 19.1 ms                                                | 16.7 ms: 1.14x faster                                                            |
| regex_effbot   | 2.34 ms                                                | 2.24 ms: 1.04x faster                                                            |
| Geometric mean | (ref)                                                  | 1.19x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 142 us: 1.40x faster                                                             |
| tomli_loads          | 1.72 sec                                               | 1.29 sec: 1.33x faster                                                           |
| pickle_pure_python   | 285 us                                                 | 214 us: 1.33x faster                                                             |
| xml_etree_process    | 44.6 ms                                                | 37.2 ms: 1.20x faster                                                            |
| json_dumps           | 8.31 ms                                                | 7.29 ms: 1.14x faster                                                            |
| xml_etree_parse      | 109 ms                                                 | 103 ms: 1.06x faster                                                             |
| xml_etree_iterparse  | 74.5 ms                                                | 71.1 ms: 1.05x faster                                                            |
| xml_etree_generate   | 53.9 ms                                                | 52.2 ms: 1.03x faster                                                            |
| json_loads           | 16.6 us                                                | 17.7 us: 1.07x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 19.6 ms: 1.00x faster                                                            |
| python_startup_no_site | 12.8 ms                                                | 15.1 ms: 1.18x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 6.66 ms: 1.47x faster                                                            |
| genshi_text     | 17.7 ms                                                | 14.1 ms: 1.26x faster                                                            |
| genshi_xml      | 35.1 ms                                                | 29.6 ms: 1.19x faster                                                            |
| django_template | 24.4 ms                                                | 21.3 ms: 1.14x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.26x faster                                                                     |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|-------------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 62.1 ms: 6.31x faster                                                            |
| typing_runtime_protocols      | 326 us                                                 | 94.5 us: 3.45x faster                                                            |
| async_tree_eager_memoization  | 483 ms                                                 | 141 ms: 3.42x faster                                                             |
| subparsers                    | 39.8 ms                                                | 12.2 ms: 3.26x faster                                                            |
| async_tree_eager_io           | 1.01 sec                                               | 362 ms: 2.80x faster                                                             |
| async_tree_io                 | 1.02 sec                                               | 366 ms: 2.78x faster                                                             |
| async_tree_none               | 391 ms                                                 | 161 ms: 2.43x faster                                                             |
| async_tree_memoization        | 481 ms                                                 | 203 ms: 2.37x faster                                                             |
| deltablue                     | 4.99 ms                                                | 2.42 ms: 2.06x faster                                                            |
| go                            | 163 ms                                                 | 83.1 ms: 1.97x faster                                                            |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 359 ms: 1.87x faster                                                             |
| deepcopy_memo                 | 34.7 us                                                | 18.7 us: 1.86x faster                                                            |
| deepcopy                      | 276 us                                                 | 152 us: 1.81x faster                                                             |
| raytrace                      | 327 ms                                                 | 183 ms: 1.79x faster                                                             |
| scimark_sor                   | 140 ms                                                 | 80.9 ms: 1.73x faster                                                            |
| logging_silent                | 117 ns                                                 | 67.7 ns: 1.73x faster                                                            |
| chaos                         | 67.7 ms                                                | 39.6 ms: 1.71x faster                                                            |
| scimark_monte_carlo           | 72.4 ms                                                | 43.5 ms: 1.66x faster                                                            |
| richards_super                | 61.0 ms                                                | 37.2 ms: 1.64x faster                                                            |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 417 ms: 1.60x faster                                                             |
| richards                      | 52.3 ms                                                | 32.8 ms: 1.59x faster                                                            |
| float                         | 72.4 ms                                                | 47.9 ms: 1.51x faster                                                            |
| sqlglot_parse                 | 1.35 ms                                                | 900 us: 1.50x faster                                                             |
| mako                          | 9.81 ms                                                | 6.66 ms: 1.47x faster                                                            |
| comprehensions                | 17.3 us                                                | 11.8 us: 1.47x faster                                                            |
| deepcopy_reduce               | 2.32 us                                                | 1.58 us: 1.47x faster                                                            |
| html5lib                      | 43.5 ms                                                | 29.7 ms: 1.46x faster                                                            |
| sqlglot_transpile             | 1.56 ms                                                | 1.07 ms: 1.46x faster                                                            |
| pyflate                       | 448 ms                                                 | 313 ms: 1.43x faster                                                             |
| logging_simple                | 4.59 us                                                | 3.22 us: 1.43x faster                                                            |
| logging_format                | 5.03 us                                                | 3.53 us: 1.42x faster                                                            |
| pylint                        | 231 ms                                                 | 164 ms: 1.41x faster                                                             |
| unpickle_pure_python          | 198 us                                                 | 142 us: 1.40x faster                                                             |
| hexiom                        | 6.25 ms                                                | 4.47 ms: 1.40x faster                                                            |
| scimark_lu                    | 103 ms                                                 | 74.3 ms: 1.38x faster                                                            |
| nbody                         | 92.5 ms                                                | 67.7 ms: 1.37x faster                                                            |
| regex_compile                 | 95.6 ms                                                | 71.0 ms: 1.35x faster                                                            |
| sqlalchemy_imperative         | 9.07 ms                                                | 6.76 ms: 1.34x faster                                                            |
| generators                    | 31.7 ms                                                | 23.8 ms: 1.33x faster                                                            |
| tomli_loads                   | 1.72 sec                                               | 1.29 sec: 1.33x faster                                                           |
| pickle_pure_python            | 285 us                                                 | 214 us: 1.33x faster                                                             |
| k_core                        | 2.01 sec                                               | 1.52 sec: 1.32x faster                                                           |
| spectral_norm                 | 95.3 ms                                                | 72.2 ms: 1.32x faster                                                            |
| crypto_pyaes                  | 73.3 ms                                                | 56.0 ms: 1.31x faster                                                            |
| pycparser                     | 887 ms                                                 | 678 ms: 1.31x faster                                                             |
| thrift                        | 562 us                                                 | 435 us: 1.29x faster                                                             |
| sqlalchemy_declarative        | 75.7 ms                                                | 59.2 ms: 1.28x faster                                                            |
| sphinx                        | 729 ms                                                 | 578 ms: 1.26x faster                                                             |
| genshi_text                   | 17.7 ms                                                | 14.1 ms: 1.26x faster                                                            |
| sympy_sum                     | 92.7 ms                                                | 74.2 ms: 1.25x faster                                                            |
| regex_dna                     | 175 ms                                                 | 141 ms: 1.24x faster                                                             |
| dulwich_log                   | 35.6 ms                                                | 28.8 ms: 1.24x faster                                                            |
| coroutines                    | 20.5 ms                                                | 16.8 ms: 1.22x faster                                                            |
| 2to3                          | 201 ms                                                 | 165 ms: 1.22x faster                                                             |
| scimark_fft                   | 225 ms                                                 | 187 ms: 1.20x faster                                                             |
| xml_etree_process             | 44.6 ms                                                | 37.2 ms: 1.20x faster                                                            |
| genshi_xml                    | 35.1 ms                                                | 29.6 ms: 1.19x faster                                                            |
| sympy_str                     | 166 ms                                                 | 142 ms: 1.17x faster                                                             |
| sympy_integrate               | 13.2 ms                                                | 11.5 ms: 1.15x faster                                                            |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 2.97 ms: 1.15x faster                                                            |
| bpe_tokeniser                 | 3.44 sec                                               | 3.00 sec: 1.15x faster                                                           |
| regex_v8                      | 19.1 ms                                                | 16.7 ms: 1.14x faster                                                            |
| django_template               | 24.4 ms                                                | 21.3 ms: 1.14x faster                                                            |
| json_dumps                    | 8.31 ms                                                | 7.29 ms: 1.14x faster                                                            |
| sympy_expand                  | 269 ms                                                 | 241 ms: 1.12x faster                                                             |
| mdp                           | 1.65 sec                                               | 1.49 sec: 1.11x faster                                                           |
| pathlib                       | 25.7 ms                                                | 23.4 ms: 1.10x faster                                                            |
| bench_thread_pool             | 545 us                                                 | 496 us: 1.10x faster                                                             |
| many_optionals                | 486 us                                                 | 456 us: 1.07x faster                                                             |
| connected_components          | 318 ms                                                 | 299 ms: 1.06x faster                                                             |
| nqueens                       | 63.8 ms                                                | 60.1 ms: 1.06x faster                                                            |
| xml_etree_parse               | 109 ms                                                 | 103 ms: 1.06x faster                                                             |
| meteor_contest                | 77.8 ms                                                | 74.0 ms: 1.05x faster                                                            |
| xml_etree_iterparse           | 74.5 ms                                                | 71.1 ms: 1.05x faster                                                            |
| regex_effbot                  | 2.34 ms                                                | 2.24 ms: 1.04x faster                                                            |
| xml_etree_generate            | 53.9 ms                                                | 52.2 ms: 1.03x faster                                                            |
| dask                          | 789 ms                                                 | 767 ms: 1.03x faster                                                             |
| json                          | 3.10 ms                                                | 3.02 ms: 1.03x faster                                                            |
| python_startup                | 19.6 ms                                                | 19.6 ms: 1.00x faster                                                            |
| fannkuch                      | 303 ms                                                 | 305 ms: 1.01x slower                                                             |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                                             |
| sqlite_synth                  | 1.48 us                                                | 1.54 us: 1.04x slower                                                            |
| json_loads                    | 16.6 us                                                | 17.7 us: 1.07x slower                                                            |
| create_gc_cycles              | 1.16 ms                                                | 1.27 ms: 1.09x slower                                                            |
| bench_mp_pool                 | 56.0 ms                                                | 61.2 ms: 1.09x slower                                                            |
| async_generators              | 233 ms                                                 | 255 ms: 1.09x slower                                                             |
| coverage                      | 41.2 ms                                                | 46.4 ms: 1.13x slower                                                            |
| gc_traversal                  | 2.71 ms                                                | 3.09 ms: 1.14x slower                                                            |
| python_startup_no_site        | 12.8 ms                                                | 15.1 ms: 1.18x slower                                                            |
| telco                         | 3.49 ms                                                | 4.55 ms: 1.30x slower                                                            |
| Geometric mean                | (ref)                                                  | 1.36x faster                                                                     |

Benchmark hidden because not significant (2): asyncio_websockets, shortest_path
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, docutils, gevent_hub, pprint_pformat, pprint_safe_repr, sqlglot_normalize, sqlglot_optimize, tornado_http
Ignored benchmarks (8) of results/bm-20250307-3.14.0a5+-553888a-JIT/bm-20250307-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.360x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: 1.16x