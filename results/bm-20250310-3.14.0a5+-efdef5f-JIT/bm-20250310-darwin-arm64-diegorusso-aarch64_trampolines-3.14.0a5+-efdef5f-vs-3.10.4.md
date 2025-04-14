# Results vs. 3.10.4

- fork: diegorusso
- ref: aarch64_trampolines
- machine: darwin-arm64
- commit hash: efdef5f
- commit date: 2025-03-10
- overall geometric mean: 1.389x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250310-darwin-arm64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 163 ms: 1.23x faster                                                      |
| docutils       | 1.74 sec                                               | 1.44 sec: 1.21x faster                                                    |
| html5lib       | 43.5 ms                                                | 29.3 ms: 1.48x faster                                                     |
| sphinx         | 729 ms                                                 | 574 ms: 1.27x faster                                                      |
| Geometric mean | (ref)                                                  | 1.29x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250310-darwin-arm64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|-------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 61.1 ms: 6.41x faster                                                     |
| async_tree_eager_memoization  | 483 ms                                                 | 140 ms: 3.45x faster                                                      |
| async_tree_eager_io           | 1.01 sec                                               | 364 ms: 2.79x faster                                                      |
| async_tree_io                 | 1.02 sec                                               | 371 ms: 2.74x faster                                                      |
| async_tree_memoization        | 481 ms                                                 | 195 ms: 2.47x faster                                                      |
| async_tree_none               | 391 ms                                                 | 161 ms: 2.44x faster                                                      |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 358 ms: 1.87x faster                                                      |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 415 ms: 1.61x faster                                                      |
| coroutines                    | 20.5 ms                                                | 16.5 ms: 1.24x faster                                                     |
| async_generators              | 233 ms                                                 | 271 ms: 1.16x slower                                                      |
| Geometric mean                | (ref)                                                  | 2.09x faster                                                              |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250310-darwin-arm64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 44.5 ms: 1.63x faster                                                     |
| nbody          | 92.5 ms                                                | 64.0 ms: 1.45x faster                                                     |
| pidigits       | 280 ms                                                 | 283 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                  | 1.33x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250310-darwin-arm64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 68.2 ms: 1.40x faster                                                     |
| regex_dna      | 175 ms                                                 | 141 ms: 1.24x faster                                                      |
| regex_v8       | 19.1 ms                                                | 15.7 ms: 1.22x faster                                                     |
| regex_effbot   | 2.34 ms                                                | 2.27 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                  | 1.22x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250310-darwin-arm64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 132 us: 1.50x faster                                                      |
| tomli_loads          | 1.72 sec                                               | 1.18 sec: 1.46x faster                                                    |
| pickle_pure_python   | 285 us                                                 | 196 us: 1.45x faster                                                      |
| xml_etree_process    | 44.6 ms                                                | 35.6 ms: 1.25x faster                                                     |
| json_dumps           | 8.31 ms                                                | 7.29 ms: 1.14x faster                                                     |
| xml_etree_generate   | 53.9 ms                                                | 50.4 ms: 1.07x faster                                                     |
| xml_etree_parse      | 109 ms                                                 | 103 ms: 1.07x faster                                                      |
| xml_etree_iterparse  | 74.5 ms                                                | 71.0 ms: 1.05x faster                                                     |
| json_loads           | 16.6 us                                                | 17.6 us: 1.06x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.20x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250310-darwin-arm64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 16.5 ms: 1.19x faster                                                     |
| python_startup_no_site | 12.8 ms                                                | 12.4 ms: 1.03x faster                                                     |
| Geometric mean         | (ref)                                                  | 1.11x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250310-darwin-arm64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 6.47 ms: 1.52x faster                                                     |
| genshi_text     | 17.7 ms                                                | 13.7 ms: 1.29x faster                                                     |
| genshi_xml      | 35.1 ms                                                | 29.1 ms: 1.21x faster                                                     |
| django_template | 24.4 ms                                                | 20.9 ms: 1.16x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.29x faster                                                              |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250310-darwin-arm64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|-------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 61.1 ms: 6.41x faster                                                     |
| typing_runtime_protocols      | 326 us                                                 | 92.5 us: 3.52x faster                                                     |
| async_tree_eager_memoization  | 483 ms                                                 | 140 ms: 3.45x faster                                                      |
| subparsers                    | 39.8 ms                                                | 11.9 ms: 3.35x faster                                                     |
| async_tree_eager_io           | 1.01 sec                                               | 364 ms: 2.79x faster                                                      |
| async_tree_io                 | 1.02 sec                                               | 371 ms: 2.74x faster                                                      |
| async_tree_memoization        | 481 ms                                                 | 195 ms: 2.47x faster                                                      |
| async_tree_none               | 391 ms                                                 | 161 ms: 2.44x faster                                                      |
| deltablue                     | 4.99 ms                                                | 2.11 ms: 2.36x faster                                                     |
| deepcopy_memo                 | 34.7 us                                                | 18.3 us: 1.89x faster                                                     |
| richards_super                | 61.0 ms                                                | 32.3 ms: 1.89x faster                                                     |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 358 ms: 1.87x faster                                                      |
| raytrace                      | 327 ms                                                 | 178 ms: 1.84x faster                                                      |
| deepcopy                      | 276 us                                                 | 151 us: 1.83x faster                                                      |
| logging_silent                | 117 ns                                                 | 64.7 ns: 1.81x faster                                                     |
| richards                      | 52.3 ms                                                | 29.1 ms: 1.80x faster                                                     |
| go                            | 163 ms                                                 | 92.6 ms: 1.77x faster                                                     |
| scimark_sor                   | 140 ms                                                 | 79.4 ms: 1.76x faster                                                     |
| chaos                         | 67.7 ms                                                | 39.4 ms: 1.72x faster                                                     |
| scimark_monte_carlo           | 72.4 ms                                                | 43.6 ms: 1.66x faster                                                     |
| float                         | 72.4 ms                                                | 44.5 ms: 1.63x faster                                                     |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 415 ms: 1.61x faster                                                      |
| spectral_norm                 | 95.3 ms                                                | 62.2 ms: 1.53x faster                                                     |
| mako                          | 9.81 ms                                                | 6.47 ms: 1.52x faster                                                     |
| unpickle_pure_python          | 198 us                                                 | 132 us: 1.50x faster                                                      |
| html5lib                      | 43.5 ms                                                | 29.3 ms: 1.48x faster                                                     |
| deepcopy_reduce               | 2.32 us                                                | 1.58 us: 1.47x faster                                                     |
| pyflate                       | 448 ms                                                 | 306 ms: 1.46x faster                                                      |
| tomli_loads                   | 1.72 sec                                               | 1.18 sec: 1.46x faster                                                    |
| dulwich_log                   | 35.6 ms                                                | 24.4 ms: 1.46x faster                                                     |
| pickle_pure_python            | 285 us                                                 | 196 us: 1.45x faster                                                      |
| nbody                         | 92.5 ms                                                | 64.0 ms: 1.45x faster                                                     |
| logging_simple                | 4.59 us                                                | 3.19 us: 1.44x faster                                                     |
| comprehensions                | 17.3 us                                                | 12.1 us: 1.44x faster                                                     |
| logging_format                | 5.03 us                                                | 3.51 us: 1.43x faster                                                     |
| pylint                        | 231 ms                                                 | 162 ms: 1.43x faster                                                      |
| regex_compile                 | 95.6 ms                                                | 68.2 ms: 1.40x faster                                                     |
| scimark_lu                    | 103 ms                                                 | 73.3 ms: 1.40x faster                                                     |
| sqlalchemy_imperative         | 9.07 ms                                                | 6.61 ms: 1.37x faster                                                     |
| hexiom                        | 6.25 ms                                                | 4.60 ms: 1.36x faster                                                     |
| generators                    | 31.7 ms                                                | 23.4 ms: 1.36x faster                                                     |
| crypto_pyaes                  | 73.3 ms                                                | 54.8 ms: 1.34x faster                                                     |
| pprint_pformat                | 1.33 sec                                               | 993 ms: 1.34x faster                                                      |
| pycparser                     | 887 ms                                                 | 668 ms: 1.33x faster                                                      |
| pprint_safe_repr              | 648 ms                                                 | 488 ms: 1.33x faster                                                      |
| k_core                        | 2.01 sec                                               | 1.52 sec: 1.33x faster                                                    |
| sqlalchemy_declarative        | 75.7 ms                                                | 58.4 ms: 1.30x faster                                                     |
| thrift                        | 562 us                                                 | 436 us: 1.29x faster                                                      |
| genshi_text                   | 17.7 ms                                                | 13.7 ms: 1.29x faster                                                     |
| scimark_fft                   | 225 ms                                                 | 177 ms: 1.27x faster                                                      |
| sphinx                        | 729 ms                                                 | 574 ms: 1.27x faster                                                      |
| sympy_sum                     | 92.7 ms                                                | 73.8 ms: 1.26x faster                                                     |
| xml_etree_process             | 44.6 ms                                                | 35.6 ms: 1.25x faster                                                     |
| regex_dna                     | 175 ms                                                 | 141 ms: 1.24x faster                                                      |
| coroutines                    | 20.5 ms                                                | 16.5 ms: 1.24x faster                                                     |
| 2to3                          | 201 ms                                                 | 163 ms: 1.23x faster                                                      |
| regex_v8                      | 19.1 ms                                                | 15.7 ms: 1.22x faster                                                     |
| genshi_xml                    | 35.1 ms                                                | 29.1 ms: 1.21x faster                                                     |
| docutils                      | 1.74 sec                                               | 1.44 sec: 1.21x faster                                                    |
| python_startup                | 19.6 ms                                                | 16.5 ms: 1.19x faster                                                     |
| sympy_str                     | 166 ms                                                 | 140 ms: 1.18x faster                                                      |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 2.89 ms: 1.18x faster                                                     |
| bpe_tokeniser                 | 3.44 sec                                               | 2.91 sec: 1.18x faster                                                    |
| django_template               | 24.4 ms                                                | 20.9 ms: 1.16x faster                                                     |
| sympy_integrate               | 13.2 ms                                                | 11.3 ms: 1.16x faster                                                     |
| json_dumps                    | 8.31 ms                                                | 7.29 ms: 1.14x faster                                                     |
| sympy_expand                  | 269 ms                                                 | 237 ms: 1.13x faster                                                      |
| mdp                           | 1.65 sec                                               | 1.47 sec: 1.12x faster                                                    |
| bench_thread_pool             | 545 us                                                 | 487 us: 1.12x faster                                                      |
| pathlib                       | 25.7 ms                                                | 23.2 ms: 1.11x faster                                                     |
| nqueens                       | 63.8 ms                                                | 58.7 ms: 1.09x faster                                                     |
| fannkuch                      | 303 ms                                                 | 278 ms: 1.09x faster                                                      |
| many_optionals                | 486 us                                                 | 447 us: 1.09x faster                                                      |
| connected_components          | 318 ms                                                 | 297 ms: 1.07x faster                                                      |
| xml_etree_generate            | 53.9 ms                                                | 50.4 ms: 1.07x faster                                                     |
| xml_etree_parse               | 109 ms                                                 | 103 ms: 1.07x faster                                                      |
| xml_etree_iterparse           | 74.5 ms                                                | 71.0 ms: 1.05x faster                                                     |
| meteor_contest                | 77.8 ms                                                | 74.6 ms: 1.04x faster                                                     |
| python_startup_no_site        | 12.8 ms                                                | 12.4 ms: 1.03x faster                                                     |
| regex_effbot                  | 2.34 ms                                                | 2.27 ms: 1.03x faster                                                     |
| dask                          | 789 ms                                                 | 768 ms: 1.03x faster                                                      |
| json                          | 3.10 ms                                                | 3.04 ms: 1.02x faster                                                     |
| pidigits                      | 280 ms                                                 | 283 ms: 1.01x slower                                                      |
| sqlite_synth                  | 1.48 us                                                | 1.54 us: 1.04x slower                                                     |
| json_loads                    | 16.6 us                                                | 17.6 us: 1.06x slower                                                     |
| bench_mp_pool                 | 56.0 ms                                                | 59.7 ms: 1.07x slower                                                     |
| create_gc_cycles              | 1.16 ms                                                | 1.29 ms: 1.11x slower                                                     |
| coverage                      | 41.2 ms                                                | 46.1 ms: 1.12x slower                                                     |
| gc_traversal                  | 2.71 ms                                                | 3.12 ms: 1.15x slower                                                     |
| async_generators              | 233 ms                                                 | 271 ms: 1.16x slower                                                      |
| telco                         | 3.49 ms                                                | 4.46 ms: 1.28x slower                                                     |
| Geometric mean                | (ref)                                                  | 1.38x faster                                                              |

Benchmark hidden because not significant (2): asyncio_websockets, shortest_path
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250310-3.14.0a5+-efdef5f-JIT/bm-20250310-darwin-arm64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.389x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.16x