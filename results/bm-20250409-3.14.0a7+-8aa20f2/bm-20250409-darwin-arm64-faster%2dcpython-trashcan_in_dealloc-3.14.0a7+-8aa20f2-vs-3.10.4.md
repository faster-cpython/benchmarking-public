# Results vs. 3.10.4

- fork: faster-cpython
- ref: trashcan_in_dealloc
- machine: darwin-arm64
- commit hash: 8aa20f2
- commit date: 2025-04-09
- overall geometric mean: 1.386x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 161 ms: 1.25x faster                                                            |
| docutils       | 1.74 sec                                               | 1.42 sec: 1.22x faster                                                          |
| html5lib       | 43.5 ms                                                | 29.8 ms: 1.46x faster                                                           |
| sphinx         | 729 ms                                                 | 578 ms: 1.26x faster                                                            |
| Geometric mean | (ref)                                                  | 1.29x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|-------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 63.0 ms: 6.22x faster                                                           |
| async_tree_eager_memoization  | 483 ms                                                 | 139 ms: 3.48x faster                                                            |
| async_tree_eager_io           | 1.01 sec                                               | 362 ms: 2.80x faster                                                            |
| async_tree_io                 | 1.02 sec                                               | 379 ms: 2.69x faster                                                            |
| async_tree_memoization        | 481 ms                                                 | 191 ms: 2.52x faster                                                            |
| async_tree_none               | 391 ms                                                 | 162 ms: 2.41x faster                                                            |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 360 ms: 1.86x faster                                                            |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 414 ms: 1.62x faster                                                            |
| coroutines                    | 20.5 ms                                                | 16.6 ms: 1.24x faster                                                           |
| async_generators              | 233 ms                                                 | 270 ms: 1.16x slower                                                            |
| Geometric mean                | (ref)                                                  | 2.08x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 47.1 ms: 1.54x faster                                                           |
| nbody          | 92.5 ms                                                | 71.6 ms: 1.29x faster                                                           |
| pidigits       | 280 ms                                                 | 283 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                  | 1.25x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 67.9 ms: 1.41x faster                                                           |
| regex_dna      | 175 ms                                                 | 141 ms: 1.24x faster                                                            |
| regex_v8       | 19.1 ms                                                | 15.6 ms: 1.23x faster                                                           |
| regex_effbot   | 2.34 ms                                                | 2.24 ms: 1.04x faster                                                           |
| Geometric mean | (ref)                                                  | 1.22x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.72 sec                                               | 1.22 sec: 1.41x faster                                                          |
| pickle_pure_python   | 285 us                                                 | 206 us: 1.38x faster                                                            |
| unpickle_pure_python | 198 us                                                 | 149 us: 1.33x faster                                                            |
| xml_etree_process    | 44.6 ms                                                | 38.5 ms: 1.16x faster                                                           |
| json_dumps           | 8.31 ms                                                | 7.65 ms: 1.09x faster                                                           |
| xml_etree_parse      | 109 ms                                                 | 105 ms: 1.05x faster                                                            |
| xml_etree_iterparse  | 74.5 ms                                                | 71.8 ms: 1.04x faster                                                           |
| xml_etree_generate   | 53.9 ms                                                | 54.8 ms: 1.02x slower                                                           |
| json_loads           | 16.6 us                                                | 18.2 us: 1.10x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 16.4 ms: 1.20x faster                                                           |
| python_startup_no_site | 12.8 ms                                                | 12.3 ms: 1.04x faster                                                           |
| Geometric mean         | (ref)                                                  | 1.12x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 7.49 ms: 1.31x faster                                                           |
| genshi_text     | 17.7 ms                                                | 13.9 ms: 1.28x faster                                                           |
| genshi_xml      | 35.1 ms                                                | 28.8 ms: 1.22x faster                                                           |
| django_template | 24.4 ms                                                | 21.1 ms: 1.16x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.24x faster                                                                    |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|-------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 63.0 ms: 6.22x faster                                                           |
| async_tree_eager_memoization  | 483 ms                                                 | 139 ms: 3.48x faster                                                            |
| typing_runtime_protocols      | 326 us                                                 | 94.2 us: 3.46x faster                                                           |
| subparsers                    | 39.8 ms                                                | 12.3 ms: 3.24x faster                                                           |
| async_tree_eager_io           | 1.01 sec                                               | 362 ms: 2.80x faster                                                            |
| async_tree_io                 | 1.02 sec                                               | 379 ms: 2.69x faster                                                            |
| async_tree_memoization        | 481 ms                                                 | 191 ms: 2.52x faster                                                            |
| async_tree_none               | 391 ms                                                 | 162 ms: 2.41x faster                                                            |
| mdp                           | 1.65 sec                                               | 765 ms: 2.16x faster                                                            |
| deltablue                     | 4.99 ms                                                | 2.36 ms: 2.12x faster                                                           |
| go                            | 163 ms                                                 | 80.1 ms: 2.04x faster                                                           |
| deepcopy_memo                 | 34.7 us                                                | 18.4 us: 1.88x faster                                                           |
| raytrace                      | 327 ms                                                 | 174 ms: 1.88x faster                                                            |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 360 ms: 1.86x faster                                                            |
| deepcopy                      | 276 us                                                 | 155 us: 1.78x faster                                                            |
| chaos                         | 67.7 ms                                                | 38.2 ms: 1.77x faster                                                           |
| scimark_sor                   | 140 ms                                                 | 79.6 ms: 1.76x faster                                                           |
| logging_silent                | 117 ns                                                 | 67.2 ns: 1.74x faster                                                           |
| scimark_monte_carlo           | 72.4 ms                                                | 42.6 ms: 1.70x faster                                                           |
| richards_super                | 61.0 ms                                                | 36.2 ms: 1.69x faster                                                           |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 414 ms: 1.62x faster                                                            |
| richards                      | 52.3 ms                                                | 32.7 ms: 1.60x faster                                                           |
| pyflate                       | 448 ms                                                 | 290 ms: 1.54x faster                                                            |
| float                         | 72.4 ms                                                | 47.1 ms: 1.54x faster                                                           |
| comprehensions                | 17.3 us                                                | 11.5 us: 1.50x faster                                                           |
| html5lib                      | 43.5 ms                                                | 29.8 ms: 1.46x faster                                                           |
| dulwich_log                   | 35.6 ms                                                | 24.5 ms: 1.45x faster                                                           |
| hexiom                        | 6.25 ms                                                | 4.33 ms: 1.44x faster                                                           |
| deepcopy_reduce               | 2.32 us                                                | 1.63 us: 1.42x faster                                                           |
| pylint                        | 231 ms                                                 | 162 ms: 1.42x faster                                                            |
| tomli_loads                   | 1.72 sec                                               | 1.22 sec: 1.41x faster                                                          |
| logging_simple                | 4.59 us                                                | 3.26 us: 1.41x faster                                                           |
| logging_format                | 5.03 us                                                | 3.58 us: 1.41x faster                                                           |
| regex_compile                 | 95.6 ms                                                | 67.9 ms: 1.41x faster                                                           |
| pickle_pure_python            | 285 us                                                 | 206 us: 1.38x faster                                                            |
| spectral_norm                 | 95.3 ms                                                | 69.0 ms: 1.38x faster                                                           |
| sqlalchemy_imperative         | 9.07 ms                                                | 6.58 ms: 1.38x faster                                                           |
| scimark_lu                    | 103 ms                                                 | 74.9 ms: 1.37x faster                                                           |
| pycparser                     | 887 ms                                                 | 655 ms: 1.35x faster                                                            |
| generators                    | 31.7 ms                                                | 23.5 ms: 1.35x faster                                                           |
| pprint_pformat                | 1.33 sec                                               | 987 ms: 1.35x faster                                                            |
| pprint_safe_repr              | 648 ms                                                 | 482 ms: 1.34x faster                                                            |
| unpickle_pure_python          | 198 us                                                 | 149 us: 1.33x faster                                                            |
| crypto_pyaes                  | 73.3 ms                                                | 55.4 ms: 1.32x faster                                                           |
| k_core                        | 2.01 sec                                               | 1.53 sec: 1.31x faster                                                          |
| mako                          | 9.81 ms                                                | 7.49 ms: 1.31x faster                                                           |
| nbody                         | 92.5 ms                                                | 71.6 ms: 1.29x faster                                                           |
| genshi_text                   | 17.7 ms                                                | 13.9 ms: 1.28x faster                                                           |
| sqlalchemy_declarative        | 75.7 ms                                                | 59.4 ms: 1.27x faster                                                           |
| sphinx                        | 729 ms                                                 | 578 ms: 1.26x faster                                                            |
| 2to3                          | 201 ms                                                 | 161 ms: 1.25x faster                                                            |
| regex_dna                     | 175 ms                                                 | 141 ms: 1.24x faster                                                            |
| coroutines                    | 20.5 ms                                                | 16.6 ms: 1.24x faster                                                           |
| regex_v8                      | 19.1 ms                                                | 15.6 ms: 1.23x faster                                                           |
| scimark_fft                   | 225 ms                                                 | 184 ms: 1.23x faster                                                            |
| sympy_sum                     | 92.7 ms                                                | 75.6 ms: 1.23x faster                                                           |
| genshi_xml                    | 35.1 ms                                                | 28.8 ms: 1.22x faster                                                           |
| docutils                      | 1.74 sec                                               | 1.42 sec: 1.22x faster                                                          |
| sympy_integrate               | 13.2 ms                                                | 10.8 ms: 1.21x faster                                                           |
| python_startup                | 19.6 ms                                                | 16.4 ms: 1.20x faster                                                           |
| sympy_str                     | 166 ms                                                 | 141 ms: 1.18x faster                                                            |
| xml_etree_process             | 44.6 ms                                                | 38.5 ms: 1.16x faster                                                           |
| django_template               | 24.4 ms                                                | 21.1 ms: 1.16x faster                                                           |
| fannkuch                      | 303 ms                                                 | 263 ms: 1.15x faster                                                            |
| sympy_expand                  | 269 ms                                                 | 238 ms: 1.13x faster                                                            |
| bpe_tokeniser                 | 3.44 sec                                               | 3.05 sec: 1.13x faster                                                          |
| bench_thread_pool             | 545 us                                                 | 494 us: 1.10x faster                                                            |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.14 ms: 1.09x faster                                                           |
| many_optionals                | 486 us                                                 | 447 us: 1.09x faster                                                            |
| json_dumps                    | 8.31 ms                                                | 7.65 ms: 1.09x faster                                                           |
| meteor_contest                | 77.8 ms                                                | 72.2 ms: 1.08x faster                                                           |
| nqueens                       | 63.8 ms                                                | 59.4 ms: 1.08x faster                                                           |
| pathlib                       | 25.7 ms                                                | 24.0 ms: 1.07x faster                                                           |
| connected_components          | 318 ms                                                 | 303 ms: 1.05x faster                                                            |
| xml_etree_parse               | 109 ms                                                 | 105 ms: 1.05x faster                                                            |
| regex_effbot                  | 2.34 ms                                                | 2.24 ms: 1.04x faster                                                           |
| python_startup_no_site        | 12.8 ms                                                | 12.3 ms: 1.04x faster                                                           |
| xml_etree_iterparse           | 74.5 ms                                                | 71.8 ms: 1.04x faster                                                           |
| json                          | 3.10 ms                                                | 3.08 ms: 1.01x faster                                                           |
| shortest_path                 | 328 ms                                                 | 330 ms: 1.01x slower                                                            |
| pidigits                      | 280 ms                                                 | 283 ms: 1.01x slower                                                            |
| xml_etree_generate            | 53.9 ms                                                | 54.8 ms: 1.02x slower                                                           |
| sqlite_synth                  | 1.48 us                                                | 1.56 us: 1.05x slower                                                           |
| bench_mp_pool                 | 56.0 ms                                                | 59.4 ms: 1.06x slower                                                           |
| json_loads                    | 16.6 us                                                | 18.2 us: 1.10x slower                                                           |
| create_gc_cycles              | 1.16 ms                                                | 1.29 ms: 1.11x slower                                                           |
| coverage                      | 41.2 ms                                                | 46.4 ms: 1.13x slower                                                           |
| async_generators              | 233 ms                                                 | 270 ms: 1.16x slower                                                            |
| gc_traversal                  | 2.71 ms                                                | 3.13 ms: 1.16x slower                                                           |
| telco                         | 3.49 ms                                                | 4.62 ms: 1.32x slower                                                           |
| Geometric mean                | (ref)                                                  | 1.38x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, dask, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250409-3.14.0a7+-8aa20f2/bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.386x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.13x