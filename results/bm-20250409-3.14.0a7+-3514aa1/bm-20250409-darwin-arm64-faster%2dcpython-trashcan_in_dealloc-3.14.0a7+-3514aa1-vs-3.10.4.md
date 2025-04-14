# Results vs. 3.10.4

- fork: faster-cpython
- ref: trashcan_in_dealloc
- machine: darwin-arm64
- commit hash: 3514aa1
- commit date: 2025-04-09
- overall geometric mean: 1.384x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 161 ms: 1.25x faster                                                            |
| docutils       | 1.74 sec                                               | 1.43 sec: 1.22x faster                                                          |
| html5lib       | 43.5 ms                                                | 29.8 ms: 1.46x faster                                                           |
| sphinx         | 729 ms                                                 | 578 ms: 1.26x faster                                                            |
| Geometric mean | (ref)                                                  | 1.29x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|-------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 63.0 ms: 6.22x faster                                                           |
| async_tree_eager_memoization  | 483 ms                                                 | 138 ms: 3.51x faster                                                            |
| async_tree_eager_io           | 1.01 sec                                               | 358 ms: 2.83x faster                                                            |
| async_tree_io                 | 1.02 sec                                               | 374 ms: 2.72x faster                                                            |
| async_tree_memoization        | 481 ms                                                 | 191 ms: 2.52x faster                                                            |
| async_tree_none               | 391 ms                                                 | 162 ms: 2.42x faster                                                            |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 360 ms: 1.86x faster                                                            |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 413 ms: 1.62x faster                                                            |
| coroutines                    | 20.5 ms                                                | 16.7 ms: 1.23x faster                                                           |
| async_generators              | 233 ms                                                 | 265 ms: 1.14x slower                                                            |
| Geometric mean                | (ref)                                                  | 2.09x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 47.2 ms: 1.54x faster                                                           |
| nbody          | 92.5 ms                                                | 73.0 ms: 1.27x faster                                                           |
| pidigits       | 280 ms                                                 | 283 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                  | 1.24x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 67.6 ms: 1.41x faster                                                           |
| regex_dna      | 175 ms                                                 | 141 ms: 1.24x faster                                                            |
| regex_v8       | 19.1 ms                                                | 15.8 ms: 1.21x faster                                                           |
| regex_effbot   | 2.34 ms                                                | 2.27 ms: 1.03x faster                                                           |
| Geometric mean | (ref)                                                  | 1.22x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.72 sec                                               | 1.22 sec: 1.41x faster                                                          |
| pickle_pure_python   | 285 us                                                 | 205 us: 1.39x faster                                                            |
| unpickle_pure_python | 198 us                                                 | 151 us: 1.31x faster                                                            |
| xml_etree_process    | 44.6 ms                                                | 38.5 ms: 1.16x faster                                                           |
| json_dumps           | 8.31 ms                                                | 7.57 ms: 1.10x faster                                                           |
| xml_etree_parse      | 109 ms                                                 | 104 ms: 1.05x faster                                                            |
| xml_etree_iterparse  | 74.5 ms                                                | 71.8 ms: 1.04x faster                                                           |
| xml_etree_generate   | 53.9 ms                                                | 54.4 ms: 1.01x slower                                                           |
| json_loads           | 16.6 us                                                | 18.4 us: 1.11x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 17.8 ms: 1.11x faster                                                           |
| python_startup_no_site | 12.8 ms                                                | 13.6 ms: 1.07x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 7.52 ms: 1.30x faster                                                           |
| genshi_text     | 17.7 ms                                                | 13.9 ms: 1.27x faster                                                           |
| genshi_xml      | 35.1 ms                                                | 29.1 ms: 1.21x faster                                                           |
| django_template | 24.4 ms                                                | 21.2 ms: 1.15x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.23x faster                                                                    |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|-------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 63.0 ms: 6.22x faster                                                           |
| async_tree_eager_memoization  | 483 ms                                                 | 138 ms: 3.51x faster                                                            |
| typing_runtime_protocols      | 326 us                                                 | 94.3 us: 3.46x faster                                                           |
| subparsers                    | 39.8 ms                                                | 12.3 ms: 3.25x faster                                                           |
| async_tree_eager_io           | 1.01 sec                                               | 358 ms: 2.83x faster                                                            |
| async_tree_io                 | 1.02 sec                                               | 374 ms: 2.72x faster                                                            |
| async_tree_memoization        | 481 ms                                                 | 191 ms: 2.52x faster                                                            |
| async_tree_none               | 391 ms                                                 | 162 ms: 2.42x faster                                                            |
| mdp                           | 1.65 sec                                               | 759 ms: 2.17x faster                                                            |
| deltablue                     | 4.99 ms                                                | 2.36 ms: 2.11x faster                                                           |
| go                            | 163 ms                                                 | 79.8 ms: 2.05x faster                                                           |
| deepcopy_memo                 | 34.7 us                                                | 18.4 us: 1.89x faster                                                           |
| raytrace                      | 327 ms                                                 | 175 ms: 1.87x faster                                                            |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 360 ms: 1.86x faster                                                            |
| deepcopy                      | 276 us                                                 | 153 us: 1.80x faster                                                            |
| chaos                         | 67.7 ms                                                | 38.1 ms: 1.78x faster                                                           |
| scimark_sor                   | 140 ms                                                 | 80.0 ms: 1.75x faster                                                           |
| logging_silent                | 117 ns                                                 | 67.4 ns: 1.74x faster                                                           |
| scimark_monte_carlo           | 72.4 ms                                                | 42.6 ms: 1.70x faster                                                           |
| richards_super                | 61.0 ms                                                | 36.3 ms: 1.68x faster                                                           |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 413 ms: 1.62x faster                                                            |
| richards                      | 52.3 ms                                                | 32.8 ms: 1.59x faster                                                           |
| float                         | 72.4 ms                                                | 47.2 ms: 1.54x faster                                                           |
| pyflate                       | 448 ms                                                 | 292 ms: 1.53x faster                                                            |
| comprehensions                | 17.3 us                                                | 11.7 us: 1.48x faster                                                           |
| html5lib                      | 43.5 ms                                                | 29.8 ms: 1.46x faster                                                           |
| dulwich_log                   | 35.6 ms                                                | 24.5 ms: 1.45x faster                                                           |
| hexiom                        | 6.25 ms                                                | 4.34 ms: 1.44x faster                                                           |
| pylint                        | 231 ms                                                 | 162 ms: 1.42x faster                                                            |
| deepcopy_reduce               | 2.32 us                                                | 1.64 us: 1.42x faster                                                           |
| logging_simple                | 4.59 us                                                | 3.25 us: 1.41x faster                                                           |
| regex_compile                 | 95.6 ms                                                | 67.6 ms: 1.41x faster                                                           |
| logging_format                | 5.03 us                                                | 3.56 us: 1.41x faster                                                           |
| tomli_loads                   | 1.72 sec                                               | 1.22 sec: 1.41x faster                                                          |
| pprint_pformat                | 1.33 sec                                               | 946 ms: 1.40x faster                                                            |
| pprint_safe_repr              | 648 ms                                                 | 464 ms: 1.40x faster                                                            |
| pickle_pure_python            | 285 us                                                 | 205 us: 1.39x faster                                                            |
| sqlalchemy_imperative         | 9.07 ms                                                | 6.57 ms: 1.38x faster                                                           |
| spectral_norm                 | 95.3 ms                                                | 69.4 ms: 1.37x faster                                                           |
| pycparser                     | 887 ms                                                 | 653 ms: 1.36x faster                                                            |
| scimark_lu                    | 103 ms                                                 | 75.9 ms: 1.35x faster                                                           |
| generators                    | 31.7 ms                                                | 23.5 ms: 1.35x faster                                                           |
| crypto_pyaes                  | 73.3 ms                                                | 55.2 ms: 1.33x faster                                                           |
| k_core                        | 2.01 sec                                               | 1.53 sec: 1.32x faster                                                          |
| unpickle_pure_python          | 198 us                                                 | 151 us: 1.31x faster                                                            |
| mako                          | 9.81 ms                                                | 7.52 ms: 1.30x faster                                                           |
| genshi_text                   | 17.7 ms                                                | 13.9 ms: 1.27x faster                                                           |
| sqlalchemy_declarative        | 75.7 ms                                                | 59.5 ms: 1.27x faster                                                           |
| nbody                         | 92.5 ms                                                | 73.0 ms: 1.27x faster                                                           |
| sphinx                        | 729 ms                                                 | 578 ms: 1.26x faster                                                            |
| 2to3                          | 201 ms                                                 | 161 ms: 1.25x faster                                                            |
| regex_dna                     | 175 ms                                                 | 141 ms: 1.24x faster                                                            |
| sympy_sum                     | 92.7 ms                                                | 74.9 ms: 1.24x faster                                                           |
| coroutines                    | 20.5 ms                                                | 16.7 ms: 1.23x faster                                                           |
| sympy_integrate               | 13.2 ms                                                | 10.8 ms: 1.22x faster                                                           |
| scimark_fft                   | 225 ms                                                 | 185 ms: 1.22x faster                                                            |
| docutils                      | 1.74 sec                                               | 1.43 sec: 1.22x faster                                                          |
| genshi_xml                    | 35.1 ms                                                | 29.1 ms: 1.21x faster                                                           |
| regex_v8                      | 19.1 ms                                                | 15.8 ms: 1.21x faster                                                           |
| sympy_str                     | 166 ms                                                 | 141 ms: 1.18x faster                                                            |
| fannkuch                      | 303 ms                                                 | 260 ms: 1.16x faster                                                            |
| xml_etree_process             | 44.6 ms                                                | 38.5 ms: 1.16x faster                                                           |
| django_template               | 24.4 ms                                                | 21.2 ms: 1.15x faster                                                           |
| bpe_tokeniser                 | 3.44 sec                                               | 3.03 sec: 1.14x faster                                                          |
| sympy_expand                  | 269 ms                                                 | 237 ms: 1.13x faster                                                            |
| python_startup                | 19.6 ms                                                | 17.8 ms: 1.11x faster                                                           |
| bench_thread_pool             | 545 us                                                 | 495 us: 1.10x faster                                                            |
| json_dumps                    | 8.31 ms                                                | 7.57 ms: 1.10x faster                                                           |
| many_optionals                | 486 us                                                 | 446 us: 1.09x faster                                                            |
| nqueens                       | 63.8 ms                                                | 59.0 ms: 1.08x faster                                                           |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.17 ms: 1.08x faster                                                           |
| pathlib                       | 25.7 ms                                                | 23.9 ms: 1.08x faster                                                           |
| meteor_contest                | 77.8 ms                                                | 72.4 ms: 1.07x faster                                                           |
| xml_etree_parse               | 109 ms                                                 | 104 ms: 1.05x faster                                                            |
| connected_components          | 318 ms                                                 | 303 ms: 1.05x faster                                                            |
| xml_etree_iterparse           | 74.5 ms                                                | 71.8 ms: 1.04x faster                                                           |
| regex_effbot                  | 2.34 ms                                                | 2.27 ms: 1.03x faster                                                           |
| shortest_path                 | 328 ms                                                 | 330 ms: 1.01x slower                                                            |
| xml_etree_generate            | 53.9 ms                                                | 54.4 ms: 1.01x slower                                                           |
| pidigits                      | 280 ms                                                 | 283 ms: 1.01x slower                                                            |
| sqlite_synth                  | 1.48 us                                                | 1.55 us: 1.05x slower                                                           |
| python_startup_no_site        | 12.8 ms                                                | 13.6 ms: 1.07x slower                                                           |
| bench_mp_pool                 | 56.0 ms                                                | 60.0 ms: 1.07x slower                                                           |
| create_gc_cycles              | 1.16 ms                                                | 1.29 ms: 1.10x slower                                                           |
| json_loads                    | 16.6 us                                                | 18.4 us: 1.11x slower                                                           |
| async_generators              | 233 ms                                                 | 265 ms: 1.14x slower                                                            |
| gc_traversal                  | 2.71 ms                                                | 3.11 ms: 1.15x slower                                                           |
| coverage                      | 41.2 ms                                                | 47.4 ms: 1.15x slower                                                           |
| telco                         | 3.49 ms                                                | 4.60 ms: 1.32x slower                                                           |
| Geometric mean                | (ref)                                                  | 1.38x faster                                                                    |

Benchmark hidden because not significant (2): asyncio_websockets, json
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, dask, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250409-3.14.0a7+-3514aa1/bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.384x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.14x