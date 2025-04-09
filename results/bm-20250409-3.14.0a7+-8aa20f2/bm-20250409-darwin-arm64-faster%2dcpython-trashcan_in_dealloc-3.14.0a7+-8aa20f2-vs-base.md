# Results vs. base

- fork: faster-cpython
- ref: trashcan_in_dealloc
- machine: darwin-arm64
- commit hash: 8aa20f2
- commit date: 2025-04-09
- overall geometric mean: 1.012x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250408-darwin-arm64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 159 ms                                                                 | 161 ms: 1.01x slower                                                            |
| docutils       | 1.41 sec                                                               | 1.42 sec: 1.01x slower                                                          |
| html5lib       | 29.4 ms                                                                | 29.8 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250408-darwin-arm64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg               | 152 ms                                                                 | 154 ms: 1.01x slower                                                            |
| async_tree_eager_cpu_io_mixed_tg | 387 ms                                                                 | 392 ms: 1.01x slower                                                            |
| async_tree_cpu_io_mixed_tg       | 406 ms                                                                 | 411 ms: 1.01x slower                                                            |
| async_tree_memoization           | 188 ms                                                                 | 191 ms: 1.01x slower                                                            |
| coroutines                       | 16.3 ms                                                                | 16.6 ms: 1.01x slower                                                           |
| async_tree_eager_memoization_tg  | 168 ms                                                                 | 171 ms: 1.02x slower                                                            |
| async_tree_none                  | 160 ms                                                                 | 162 ms: 1.02x slower                                                            |
| async_tree_eager_cpu_io_mixed    | 353 ms                                                                 | 360 ms: 1.02x slower                                                            |
| async_tree_eager_memoization     | 136 ms                                                                 | 139 ms: 1.02x slower                                                            |
| async_tree_eager_io_tg           | 369 ms                                                                 | 377 ms: 1.02x slower                                                            |
| async_tree_cpu_io_mixed          | 405 ms                                                                 | 414 ms: 1.02x slower                                                            |
| async_tree_io                    | 370 ms                                                                 | 379 ms: 1.02x slower                                                            |
| async_tree_eager_tg              | 130 ms                                                                 | 133 ms: 1.03x slower                                                            |
| async_tree_eager                 | 61.3 ms                                                                | 63.0 ms: 1.03x slower                                                           |
| async_generators                 | 257 ms                                                                 | 270 ms: 1.05x slower                                                            |
| Geometric mean                   | (ref)                                                                  | 1.02x slower                                                                    |

Benchmark hidden because not significant (4): async_tree_io_tg, asyncio_websockets, async_tree_memoization_tg, async_tree_eager_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250408-darwin-arm64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 70.1 ms                                                                | 71.6 ms: 1.02x slower                                                           |
| float          | 45.8 ms                                                                | 47.1 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250408-darwin-arm64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.27 ms                                                                | 2.24 ms: 1.02x faster                                                           |
| regex_v8       | 15.6 ms                                                                | 15.6 ms: 1.01x faster                                                           |
| regex_dna      | 140 ms                                                                 | 141 ms: 1.00x slower                                                            |
| regex_compile  | 66.7 ms                                                                | 67.9 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250408-darwin-arm64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_pure_python | 148 us                                                                 | 149 us: 1.01x slower                                                            |
| xml_etree_process    | 38.1 ms                                                                | 38.5 ms: 1.01x slower                                                           |
| xml_etree_parse      | 103 ms                                                                 | 105 ms: 1.01x slower                                                            |
| tomli_loads          | 1.20 sec                                                               | 1.22 sec: 1.02x slower                                                          |
| pickle_pure_python   | 201 us                                                                 | 206 us: 1.02x slower                                                            |
| xml_etree_generate   | 53.4 ms                                                                | 54.8 ms: 1.03x slower                                                           |
| json_loads           | 17.7 us                                                                | 18.2 us: 1.03x slower                                                           |
| json_dumps           | 7.36 ms                                                                | 7.65 ms: 1.04x slower                                                           |
| Geometric mean       | (ref)                                                                  | 1.02x slower                                                                    |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250408-darwin-arm64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 12.7 ms                                                                | 12.3 ms: 1.03x faster                                                           |
| python_startup         | 16.8 ms                                                                | 16.4 ms: 1.02x faster                                                           |
| Geometric mean         | (ref)                                                                  | 1.03x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250408-darwin-arm64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 7.56 ms                                                                | 7.49 ms: 1.01x faster                                                           |
| genshi_xml      | 28.6 ms                                                                | 28.8 ms: 1.01x slower                                                           |
| genshi_text     | 13.7 ms                                                                | 13.9 ms: 1.01x slower                                                           |
| django_template | 20.8 ms                                                                | 21.1 ms: 1.01x slower                                                           |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                                    |

All benchmarks:
===============

| Benchmark                        | bm-20250408-darwin-arm64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-darwin-arm64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site           | 12.7 ms                                                                | 12.3 ms: 1.03x faster                                                           |
| python_startup                   | 16.8 ms                                                                | 16.4 ms: 1.02x faster                                                           |
| regex_effbot                     | 2.27 ms                                                                | 2.24 ms: 1.02x faster                                                           |
| mako                             | 7.56 ms                                                                | 7.49 ms: 1.01x faster                                                           |
| regex_v8                         | 15.6 ms                                                                | 15.6 ms: 1.01x faster                                                           |
| connected_components             | 304 ms                                                                 | 303 ms: 1.00x faster                                                            |
| meteor_contest                   | 72.3 ms                                                                | 72.2 ms: 1.00x faster                                                           |
| regex_dna                        | 140 ms                                                                 | 141 ms: 1.00x slower                                                            |
| create_gc_cycles                 | 1.28 ms                                                                | 1.29 ms: 1.00x slower                                                           |
| dulwich_log                      | 24.4 ms                                                                | 24.5 ms: 1.00x slower                                                           |
| sqlalchemy_declarative           | 59.0 ms                                                                | 59.4 ms: 1.01x slower                                                           |
| generators                       | 23.4 ms                                                                | 23.5 ms: 1.01x slower                                                           |
| richards_super                   | 35.9 ms                                                                | 36.2 ms: 1.01x slower                                                           |
| sqlalchemy_imperative            | 6.54 ms                                                                | 6.58 ms: 1.01x slower                                                           |
| docutils                         | 1.41 sec                                                               | 1.42 sec: 1.01x slower                                                          |
| spectral_norm                    | 68.4 ms                                                                | 69.0 ms: 1.01x slower                                                           |
| genshi_xml                       | 28.6 ms                                                                | 28.8 ms: 1.01x slower                                                           |
| unpickle_pure_python             | 148 us                                                                 | 149 us: 1.01x slower                                                            |
| genshi_text                      | 13.7 ms                                                                | 13.9 ms: 1.01x slower                                                           |
| crypto_pyaes                     | 54.8 ms                                                                | 55.4 ms: 1.01x slower                                                           |
| bench_thread_pool                | 489 us                                                                 | 494 us: 1.01x slower                                                            |
| xml_etree_process                | 38.1 ms                                                                | 38.5 ms: 1.01x slower                                                           |
| xml_etree_parse                  | 103 ms                                                                 | 105 ms: 1.01x slower                                                            |
| async_tree_none_tg               | 152 ms                                                                 | 154 ms: 1.01x slower                                                            |
| nqueens                          | 58.7 ms                                                                | 59.4 ms: 1.01x slower                                                           |
| async_tree_eager_cpu_io_mixed_tg | 387 ms                                                                 | 392 ms: 1.01x slower                                                            |
| async_tree_cpu_io_mixed_tg       | 406 ms                                                                 | 411 ms: 1.01x slower                                                            |
| sympy_str                        | 139 ms                                                                 | 141 ms: 1.01x slower                                                            |
| sympy_integrate                  | 10.7 ms                                                                | 10.8 ms: 1.01x slower                                                           |
| async_tree_memoization           | 188 ms                                                                 | 191 ms: 1.01x slower                                                            |
| richards                         | 32.2 ms                                                                | 32.7 ms: 1.01x slower                                                           |
| django_template                  | 20.8 ms                                                                | 21.1 ms: 1.01x slower                                                           |
| html5lib                         | 29.4 ms                                                                | 29.8 ms: 1.01x slower                                                           |
| coroutines                       | 16.3 ms                                                                | 16.6 ms: 1.01x slower                                                           |
| fannkuch                         | 259 ms                                                                 | 263 ms: 1.01x slower                                                            |
| 2to3                             | 159 ms                                                                 | 161 ms: 1.01x slower                                                            |
| pyflate                          | 286 ms                                                                 | 290 ms: 1.01x slower                                                            |
| pathlib                          | 23.7 ms                                                                | 24.0 ms: 1.01x slower                                                           |
| pprint_safe_repr                 | 475 ms                                                                 | 482 ms: 1.01x slower                                                            |
| scimark_fft                      | 181 ms                                                                 | 184 ms: 1.02x slower                                                            |
| tomli_loads                      | 1.20 sec                                                               | 1.22 sec: 1.02x slower                                                          |
| telco                            | 4.55 ms                                                                | 4.62 ms: 1.02x slower                                                           |
| chaos                            | 37.6 ms                                                                | 38.2 ms: 1.02x slower                                                           |
| go                               | 78.8 ms                                                                | 80.1 ms: 1.02x slower                                                           |
| hexiom                           | 4.26 ms                                                                | 4.33 ms: 1.02x slower                                                           |
| coverage                         | 45.7 ms                                                                | 46.4 ms: 1.02x slower                                                           |
| mdp                              | 753 ms                                                                 | 765 ms: 1.02x slower                                                            |
| sqlglot_v2_transpile             | 932 us                                                                 | 947 us: 1.02x slower                                                            |
| async_tree_eager_memoization_tg  | 168 ms                                                                 | 171 ms: 1.02x slower                                                            |
| scimark_sparse_mat_mult          | 3.09 ms                                                                | 3.14 ms: 1.02x slower                                                           |
| async_tree_none                  | 160 ms                                                                 | 162 ms: 1.02x slower                                                            |
| async_tree_eager_cpu_io_mixed    | 353 ms                                                                 | 360 ms: 1.02x slower                                                            |
| regex_compile                    | 66.7 ms                                                                | 67.9 ms: 1.02x slower                                                           |
| subparsers                       | 12.1 ms                                                                | 12.3 ms: 1.02x slower                                                           |
| logging_simple                   | 3.21 us                                                                | 3.26 us: 1.02x slower                                                           |
| comprehensions                   | 11.3 us                                                                | 11.5 us: 1.02x slower                                                           |
| sqlglot_v2_normalize             | 65.7 ms                                                                | 67.0 ms: 1.02x slower                                                           |
| scimark_monte_carlo              | 41.8 ms                                                                | 42.6 ms: 1.02x slower                                                           |
| sqlite_synth                     | 1.53 us                                                                | 1.56 us: 1.02x slower                                                           |
| async_tree_eager_memoization     | 136 ms                                                                 | 139 ms: 1.02x slower                                                            |
| sympy_expand                     | 233 ms                                                                 | 238 ms: 1.02x slower                                                            |
| logging_format                   | 3.51 us                                                                | 3.58 us: 1.02x slower                                                           |
| sqlglot_v2_parse                 | 769 us                                                                 | 785 us: 1.02x slower                                                            |
| sympy_sum                        | 74.1 ms                                                                | 75.6 ms: 1.02x slower                                                           |
| json                             | 3.02 ms                                                                | 3.08 ms: 1.02x slower                                                           |
| async_tree_eager_io_tg           | 369 ms                                                                 | 377 ms: 1.02x slower                                                            |
| deltablue                        | 2.31 ms                                                                | 2.36 ms: 1.02x slower                                                           |
| async_tree_cpu_io_mixed          | 405 ms                                                                 | 414 ms: 1.02x slower                                                            |
| nbody                            | 70.1 ms                                                                | 71.6 ms: 1.02x slower                                                           |
| pickle_pure_python               | 201 us                                                                 | 206 us: 1.02x slower                                                            |
| scimark_lu                       | 73.3 ms                                                                | 74.9 ms: 1.02x slower                                                           |
| bpe_tokeniser                    | 2.98 sec                                                               | 3.05 sec: 1.02x slower                                                          |
| scimark_sor                      | 77.8 ms                                                                | 79.6 ms: 1.02x slower                                                           |
| sqlglot_v2_optimize              | 32.0 ms                                                                | 32.7 ms: 1.02x slower                                                           |
| async_tree_io                    | 370 ms                                                                 | 379 ms: 1.02x slower                                                            |
| xml_etree_generate               | 53.4 ms                                                                | 54.8 ms: 1.03x slower                                                           |
| pprint_pformat                   | 961 ms                                                                 | 987 ms: 1.03x slower                                                            |
| async_tree_eager_tg              | 130 ms                                                                 | 133 ms: 1.03x slower                                                            |
| async_tree_eager                 | 61.3 ms                                                                | 63.0 ms: 1.03x slower                                                           |
| json_loads                       | 17.7 us                                                                | 18.2 us: 1.03x slower                                                           |
| float                            | 45.8 ms                                                                | 47.1 ms: 1.03x slower                                                           |
| raytrace                         | 169 ms                                                                 | 174 ms: 1.03x slower                                                            |
| deepcopy_reduce                  | 1.58 us                                                                | 1.63 us: 1.03x slower                                                           |
| deepcopy_memo                    | 17.8 us                                                                | 18.4 us: 1.03x slower                                                           |
| json_dumps                       | 7.36 ms                                                                | 7.65 ms: 1.04x slower                                                           |
| logging_silent                   | 64.5 ns                                                                | 67.2 ns: 1.04x slower                                                           |
| deepcopy                         | 148 us                                                                 | 155 us: 1.04x slower                                                            |
| async_generators                 | 257 ms                                                                 | 270 ms: 1.05x slower                                                            |
| Geometric mean                   | (ref)                                                                  | 1.01x slower                                                                    |

Benchmark hidden because not significant (15): bench_mp_pool, async_tree_io_tg, xml_etree_iterparse, shortest_path, pidigits, asyncio_websockets, k_core, gc_traversal, typing_runtime_protocols, async_tree_memoization_tg, many_optionals, pylint, sphinx, pycparser, async_tree_eager_io

- Geometric mean (including insignificant results): 1.012x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 0.99x