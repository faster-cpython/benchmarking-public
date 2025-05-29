# Results vs. 3.10.4

- fork: faster-cpython
- ref: tos_caching_1
- machine: darwin-arm64
- commit hash: 5bbc96e
- commit date: 2025-04-08
- overall geometric mean: 1.485x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 149 ms: 1.35x faster                                                      |
| docutils       | 1.74 sec                                               | 1.36 sec: 1.27x faster                                                    |
| html5lib       | 43.5 ms                                                | 28.1 ms: 1.55x faster                                                     |
| sphinx         | 729 ms                                                 | 548 ms: 1.33x faster                                                      |
| Geometric mean | (ref)                                                  | 1.37x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|-------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 55.3 ms: 7.09x faster                                                     |
| async_tree_eager_memoization  | 483 ms                                                 | 130 ms: 3.73x faster                                                      |
| async_tree_io                 | 1.02 sec                                               | 336 ms: 3.02x faster                                                      |
| async_tree_eager_io           | 1.01 sec                                               | 342 ms: 2.97x faster                                                      |
| async_tree_memoization        | 481 ms                                                 | 178 ms: 2.70x faster                                                      |
| async_tree_none               | 391 ms                                                 | 150 ms: 2.62x faster                                                      |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 343 ms: 1.95x faster                                                      |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 398 ms: 1.68x faster                                                      |
| coroutines                    | 20.5 ms                                                | 14.2 ms: 1.45x faster                                                     |
| asyncio_websockets            | 242 ms                                                 | 242 ms: 1.00x faster                                                      |
| async_generators              | 233 ms                                                 | 249 ms: 1.07x slower                                                      |
| Geometric mean                | (ref)                                                  | 2.25x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 41.0 ms: 1.77x faster                                                     |
| nbody          | 92.5 ms                                                | 69.0 ms: 1.34x faster                                                     |
| pidigits       | 280 ms                                                 | 280 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                  | 1.33x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 63.9 ms: 1.50x faster                                                     |
| regex_dna      | 175 ms                                                 | 148 ms: 1.18x faster                                                      |
| regex_v8       | 19.1 ms                                                | 16.7 ms: 1.14x faster                                                     |
| regex_effbot   | 2.34 ms                                                | 2.39 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                  | 1.19x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 285 us                                                 | 180 us: 1.58x faster                                                      |
| unpickle_pure_python | 198 us                                                 | 128 us: 1.55x faster                                                      |
| tomli_loads          | 1.72 sec                                               | 1.14 sec: 1.51x faster                                                    |
| xml_etree_process    | 44.6 ms                                                | 35.4 ms: 1.26x faster                                                     |
| json_dumps           | 8.31 ms                                                | 7.15 ms: 1.16x faster                                                     |
| xml_etree_iterparse  | 74.5 ms                                                | 68.8 ms: 1.08x faster                                                     |
| xml_etree_generate   | 53.9 ms                                                | 50.9 ms: 1.06x faster                                                     |
| xml_etree_parse      | 109 ms                                                 | 104 ms: 1.06x faster                                                      |
| json_loads           | 16.6 us                                                | 17.9 us: 1.08x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.22x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 19.2 ms: 1.02x faster                                                     |
| python_startup_no_site | 12.8 ms                                                | 14.9 ms: 1.16x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 17.7 ms                                                | 12.7 ms: 1.40x faster                                                     |
| genshi_xml      | 35.1 ms                                                | 26.8 ms: 1.31x faster                                                     |
| django_template | 24.4 ms                                                | 18.8 ms: 1.29x faster                                                     |
| mako            | 9.81 ms                                                | 8.36 ms: 1.17x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.29x faster                                                              |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|-------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 55.3 ms: 7.09x faster                                                     |
| typing_runtime_protocols      | 326 us                                                 | 87.3 us: 3.73x faster                                                     |
| async_tree_eager_memoization  | 483 ms                                                 | 130 ms: 3.73x faster                                                      |
| subparsers                    | 39.8 ms                                                | 11.4 ms: 3.49x faster                                                     |
| async_tree_io                 | 1.02 sec                                               | 336 ms: 3.02x faster                                                      |
| async_tree_eager_io           | 1.01 sec                                               | 342 ms: 2.97x faster                                                      |
| async_tree_memoization        | 481 ms                                                 | 178 ms: 2.70x faster                                                      |
| async_tree_none               | 391 ms                                                 | 150 ms: 2.62x faster                                                      |
| deltablue                     | 4.99 ms                                                | 1.92 ms: 2.59x faster                                                     |
| go                            | 163 ms                                                 | 66.0 ms: 2.48x faster                                                     |
| mdp                           | 1.65 sec                                               | 675 ms: 2.45x faster                                                      |
| raytrace                      | 327 ms                                                 | 150 ms: 2.18x faster                                                      |
| logging_silent                | 117 ns                                                 | 54.4 ns: 2.15x faster                                                     |
| chaos                         | 67.7 ms                                                | 33.1 ms: 2.05x faster                                                     |
| scimark_monte_carlo           | 72.4 ms                                                | 36.9 ms: 1.96x faster                                                     |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 343 ms: 1.95x faster                                                      |
| scimark_sor                   | 140 ms                                                 | 72.7 ms: 1.93x faster                                                     |
| deepcopy                      | 276 us                                                 | 144 us: 1.92x faster                                                      |
| richards_super                | 61.0 ms                                                | 31.9 ms: 1.91x faster                                                     |
| deepcopy_memo                 | 34.7 us                                                | 18.5 us: 1.88x faster                                                     |
| richards                      | 52.3 ms                                                | 28.7 ms: 1.82x faster                                                     |
| comprehensions                | 17.3 us                                                | 9.78 us: 1.77x faster                                                     |
| float                         | 72.4 ms                                                | 41.0 ms: 1.77x faster                                                     |
| generators                    | 31.7 ms                                                | 17.9 ms: 1.77x faster                                                     |
| pyflate                       | 448 ms                                                 | 257 ms: 1.74x faster                                                      |
| hexiom                        | 6.25 ms                                                | 3.68 ms: 1.70x faster                                                     |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 398 ms: 1.68x faster                                                      |
| crypto_pyaes                  | 73.3 ms                                                | 44.8 ms: 1.64x faster                                                     |
| pickle_pure_python            | 285 us                                                 | 180 us: 1.58x faster                                                      |
| logging_format                | 5.03 us                                                | 3.24 us: 1.55x faster                                                     |
| pylint                        | 231 ms                                                 | 149 ms: 1.55x faster                                                      |
| logging_simple                | 4.59 us                                                | 2.96 us: 1.55x faster                                                     |
| html5lib                      | 43.5 ms                                                | 28.1 ms: 1.55x faster                                                     |
| unpickle_pure_python          | 198 us                                                 | 128 us: 1.55x faster                                                      |
| dulwich_log                   | 35.6 ms                                                | 23.1 ms: 1.54x faster                                                     |
| deepcopy_reduce               | 2.32 us                                                | 1.53 us: 1.52x faster                                                     |
| tomli_loads                   | 1.72 sec                                               | 1.14 sec: 1.51x faster                                                    |
| spectral_norm                 | 95.3 ms                                                | 63.0 ms: 1.51x faster                                                     |
| regex_compile                 | 95.6 ms                                                | 63.9 ms: 1.50x faster                                                     |
| scimark_lu                    | 103 ms                                                 | 69.2 ms: 1.48x faster                                                     |
| sqlalchemy_imperative         | 9.07 ms                                                | 6.13 ms: 1.48x faster                                                     |
| pycparser                     | 887 ms                                                 | 613 ms: 1.45x faster                                                      |
| coroutines                    | 20.5 ms                                                | 14.2 ms: 1.45x faster                                                     |
| pprint_pformat                | 1.33 sec                                               | 946 ms: 1.40x faster                                                      |
| genshi_text                   | 17.7 ms                                                | 12.7 ms: 1.40x faster                                                     |
| sqlalchemy_declarative        | 75.7 ms                                                | 54.4 ms: 1.39x faster                                                     |
| pprint_safe_repr              | 648 ms                                                 | 469 ms: 1.38x faster                                                      |
| sympy_integrate               | 13.2 ms                                                | 9.67 ms: 1.36x faster                                                     |
| k_core                        | 2.01 sec                                               | 1.48 sec: 1.36x faster                                                    |
| 2to3                          | 201 ms                                                 | 149 ms: 1.35x faster                                                      |
| nbody                         | 92.5 ms                                                | 69.0 ms: 1.34x faster                                                     |
| sphinx                        | 729 ms                                                 | 548 ms: 1.33x faster                                                      |
| sympy_sum                     | 92.7 ms                                                | 69.8 ms: 1.33x faster                                                     |
| genshi_xml                    | 35.1 ms                                                | 26.8 ms: 1.31x faster                                                     |
| django_template               | 24.4 ms                                                | 18.8 ms: 1.29x faster                                                     |
| sympy_str                     | 166 ms                                                 | 128 ms: 1.29x faster                                                      |
| docutils                      | 1.74 sec                                               | 1.36 sec: 1.27x faster                                                    |
| nqueens                       | 63.8 ms                                                | 50.4 ms: 1.27x faster                                                     |
| bpe_tokeniser                 | 3.44 sec                                               | 2.72 sec: 1.26x faster                                                    |
| fannkuch                      | 303 ms                                                 | 240 ms: 1.26x faster                                                      |
| xml_etree_process             | 44.6 ms                                                | 35.4 ms: 1.26x faster                                                     |
| sympy_expand                  | 269 ms                                                 | 217 ms: 1.24x faster                                                      |
| scimark_fft                   | 225 ms                                                 | 183 ms: 1.23x faster                                                      |
| regex_dna                     | 175 ms                                                 | 148 ms: 1.18x faster                                                      |
| bench_thread_pool             | 545 us                                                 | 464 us: 1.17x faster                                                      |
| mako                          | 9.81 ms                                                | 8.36 ms: 1.17x faster                                                     |
| many_optionals                | 486 us                                                 | 417 us: 1.16x faster                                                      |
| json_dumps                    | 8.31 ms                                                | 7.15 ms: 1.16x faster                                                     |
| regex_v8                      | 19.1 ms                                                | 16.7 ms: 1.14x faster                                                     |
| meteor_contest                | 77.8 ms                                                | 68.8 ms: 1.13x faster                                                     |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.05 ms: 1.12x faster                                                     |
| pathlib                       | 25.7 ms                                                | 23.2 ms: 1.11x faster                                                     |
| xml_etree_iterparse           | 74.5 ms                                                | 68.8 ms: 1.08x faster                                                     |
| xml_etree_generate            | 53.9 ms                                                | 50.9 ms: 1.06x faster                                                     |
| xml_etree_parse               | 109 ms                                                 | 104 ms: 1.06x faster                                                      |
| connected_components          | 318 ms                                                 | 302 ms: 1.06x faster                                                      |
| json                          | 3.10 ms                                                | 3.02 ms: 1.03x faster                                                     |
| python_startup                | 19.6 ms                                                | 19.2 ms: 1.02x faster                                                     |
| pidigits                      | 280 ms                                                 | 280 ms: 1.00x faster                                                      |
| asyncio_websockets            | 242 ms                                                 | 242 ms: 1.00x faster                                                      |
| sqlite_synth                  | 1.48 us                                                | 1.51 us: 1.02x slower                                                     |
| regex_effbot                  | 2.34 ms                                                | 2.39 ms: 1.02x slower                                                     |
| bench_mp_pool                 | 56.0 ms                                                | 59.8 ms: 1.07x slower                                                     |
| async_generators              | 233 ms                                                 | 249 ms: 1.07x slower                                                      |
| json_loads                    | 16.6 us                                                | 17.9 us: 1.08x slower                                                     |
| coverage                      | 41.2 ms                                                | 44.6 ms: 1.08x slower                                                     |
| create_gc_cycles              | 1.16 ms                                                | 1.27 ms: 1.09x slower                                                     |
| gc_traversal                  | 2.71 ms                                                | 3.10 ms: 1.14x slower                                                     |
| python_startup_no_site        | 12.8 ms                                                | 14.9 ms: 1.16x slower                                                     |
| telco                         | 3.49 ms                                                | 4.53 ms: 1.30x slower                                                     |
| Geometric mean                | (ref)                                                  | 1.48x faster                                                              |

Benchmark hidden because not significant (1): shortest_path
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, dask, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250408-3.14.0a6+-5bbc96e-CLANG/bm-20250408-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.485x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.13x