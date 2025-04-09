# Results vs. base

- fork: faster-cpython
- ref: trashcan_in_dealloc
- machine: linux-x86_64
- commit hash: 3514aa1
- commit date: 2025-04-09
- overall geometric mean: 1.015x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250408-linux-x86_64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                                 | 252 ms: 1.01x slower                                                            |
| docutils       | 2.59 sec                                                               | 2.60 sec: 1.01x slower                                                          |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                    |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250408-linux-x86_64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| coroutines                 | 23.3 ms                                                                | 23.4 ms: 1.00x slower                                                           |
| async_tree_memoization     | 309 ms                                                                 | 313 ms: 1.01x slower                                                            |
| async_tree_cpu_io_mixed    | 479 ms                                                                 | 486 ms: 1.01x slower                                                            |
| async_tree_cpu_io_mixed_tg | 474 ms                                                                 | 482 ms: 1.02x slower                                                            |
| async_tree_memoization_tg  | 311 ms                                                                 | 317 ms: 1.02x slower                                                            |
| async_tree_none_tg         | 246 ms                                                                 | 251 ms: 1.02x slower                                                            |
| async_tree_none            | 255 ms                                                                 | 261 ms: 1.02x slower                                                            |
| async_generators           | 384 ms                                                                 | 407 ms: 1.06x slower                                                            |
| Geometric mean             | (ref)                                                                  | 1.02x slower                                                                    |

Benchmark hidden because not significant (3): asyncio_websockets, async_tree_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250408-linux-x86_64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x faster                                                            |
| float          | 66.1 ms                                                                | 70.6 ms: 1.07x slower                                                           |
| nbody          | 87.8 ms                                                                | 94.6 ms: 1.08x slower                                                           |
| Geometric mean | (ref)                                                                  | 1.05x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250408-linux-x86_64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 214 ms                                                                 | 212 ms: 1.01x faster                                                            |
| regex_effbot   | 3.27 ms                                                                | 3.26 ms: 1.00x faster                                                           |
| regex_compile  | 123 ms                                                                 | 125 ms: 1.02x slower                                                            |
| regex_v8       | 22.9 ms                                                                | 23.8 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250408-linux-x86_64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 98.1 ms                                                                | 98.8 ms: 1.01x slower                                                           |
| xml_etree_parse      | 141 ms                                                                 | 142 ms: 1.01x slower                                                            |
| pickle_pure_python   | 312 us                                                                 | 316 us: 1.01x slower                                                            |
| unpickle_pure_python | 214 us                                                                 | 218 us: 1.02x slower                                                            |
| xml_etree_process    | 57.7 ms                                                                | 58.9 ms: 1.02x slower                                                           |
| json_loads           | 29.8 us                                                                | 30.5 us: 1.02x slower                                                           |
| xml_etree_generate   | 82.9 ms                                                                | 84.8 ms: 1.02x slower                                                           |
| tomli_loads          | 1.94 sec                                                               | 2.00 sec: 1.03x slower                                                          |
| Geometric mean       | (ref)                                                                  | 1.02x slower                                                                    |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250408-linux-x86_64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                                | 13.2 ms: 1.00x slower                                                           |
| python_startup_no_site | 8.20 ms                                                                | 8.23 ms: 1.00x slower                                                           |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250408-linux-x86_64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 31.9 ms                                                                | 31.5 ms: 1.01x faster                                                           |
| genshi_xml      | 48.6 ms                                                                | 49.0 ms: 1.01x slower                                                           |
| mako            | 11.2 ms                                                                | 11.5 ms: 1.02x slower                                                           |
| genshi_text     | 20.6 ms                                                                | 21.1 ms: 1.02x slower                                                           |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20250408-linux-x86_64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pycparser                  | 1.14 sec                                                               | 1.11 sec: 1.03x faster                                                          |
| generators                 | 29.6 ms                                                                | 29.1 ms: 1.02x faster                                                           |
| richards_super             | 49.2 ms                                                                | 48.5 ms: 1.01x faster                                                           |
| django_template            | 31.9 ms                                                                | 31.5 ms: 1.01x faster                                                           |
| logging_simple             | 5.56 us                                                                | 5.49 us: 1.01x faster                                                           |
| regex_dna                  | 214 ms                                                                 | 212 ms: 1.01x faster                                                            |
| logging_format             | 6.10 us                                                                | 6.06 us: 1.01x faster                                                           |
| meteor_contest             | 106 ms                                                                 | 106 ms: 1.00x faster                                                            |
| pidigits                   | 186 ms                                                                 | 186 ms: 1.00x faster                                                            |
| regex_effbot               | 3.27 ms                                                                | 3.26 ms: 1.00x faster                                                           |
| coroutines                 | 23.3 ms                                                                | 23.4 ms: 1.00x slower                                                           |
| python_startup             | 13.2 ms                                                                | 13.2 ms: 1.00x slower                                                           |
| python_startup_no_site     | 8.20 ms                                                                | 8.23 ms: 1.00x slower                                                           |
| sqlglot_v2_normalize       | 106 ms                                                                 | 106 ms: 1.00x slower                                                            |
| bench_mp_pool              | 82.0 ms                                                                | 82.4 ms: 1.01x slower                                                           |
| logging_silent             | 97.1 ns                                                                | 97.8 ns: 1.01x slower                                                           |
| docutils                   | 2.59 sec                                                               | 2.60 sec: 1.01x slower                                                          |
| xml_etree_iterparse        | 98.1 ms                                                                | 98.8 ms: 1.01x slower                                                           |
| xml_etree_parse            | 141 ms                                                                 | 142 ms: 1.01x slower                                                            |
| mdp                        | 1.23 sec                                                               | 1.23 sec: 1.01x slower                                                          |
| genshi_xml                 | 48.6 ms                                                                | 49.0 ms: 1.01x slower                                                           |
| sqlglot_v2_optimize        | 52.0 ms                                                                | 52.5 ms: 1.01x slower                                                           |
| sympy_integrate            | 19.0 ms                                                                | 19.2 ms: 1.01x slower                                                           |
| 2to3                       | 250 ms                                                                 | 252 ms: 1.01x slower                                                            |
| bench_thread_pool          | 874 us                                                                 | 884 us: 1.01x slower                                                            |
| sqlalchemy_declarative     | 131 ms                                                                 | 133 ms: 1.01x slower                                                            |
| sympy_sum                  | 148 ms                                                                 | 150 ms: 1.01x slower                                                            |
| sympy_str                  | 266 ms                                                                 | 269 ms: 1.01x slower                                                            |
| sqlalchemy_imperative      | 16.8 ms                                                                | 17.0 ms: 1.01x slower                                                           |
| bpe_tokeniser              | 4.51 sec                                                               | 4.57 sec: 1.01x slower                                                          |
| async_tree_memoization     | 309 ms                                                                 | 313 ms: 1.01x slower                                                            |
| sqlglot_v2_parse           | 1.21 ms                                                                | 1.23 ms: 1.01x slower                                                           |
| sympy_expand               | 453 ms                                                                 | 459 ms: 1.01x slower                                                            |
| pickle_pure_python         | 312 us                                                                 | 316 us: 1.01x slower                                                            |
| sqlglot_v2_transpile       | 1.52 ms                                                                | 1.54 ms: 1.01x slower                                                           |
| async_tree_cpu_io_mixed    | 479 ms                                                                 | 486 ms: 1.01x slower                                                            |
| many_optionals             | 922 us                                                                 | 935 us: 1.01x slower                                                            |
| go                         | 109 ms                                                                 | 110 ms: 1.01x slower                                                            |
| pprint_safe_repr           | 704 ms                                                                 | 714 ms: 1.01x slower                                                            |
| telco                      | 7.72 ms                                                                | 7.85 ms: 1.02x slower                                                           |
| connected_components       | 445 ms                                                                 | 452 ms: 1.02x slower                                                            |
| scimark_sparse_mat_mult    | 4.63 ms                                                                | 4.71 ms: 1.02x slower                                                           |
| regex_compile              | 123 ms                                                                 | 125 ms: 1.02x slower                                                            |
| async_tree_cpu_io_mixed_tg | 474 ms                                                                 | 482 ms: 1.02x slower                                                            |
| fannkuch                   | 407 ms                                                                 | 415 ms: 1.02x slower                                                            |
| subparsers                 | 20.5 ms                                                                | 20.9 ms: 1.02x slower                                                           |
| pprint_pformat             | 1.44 sec                                                               | 1.47 sec: 1.02x slower                                                          |
| unpickle_pure_python       | 214 us                                                                 | 218 us: 1.02x slower                                                            |
| dulwich_log                | 58.6 ms                                                                | 59.7 ms: 1.02x slower                                                           |
| scimark_lu                 | 114 ms                                                                 | 117 ms: 1.02x slower                                                            |
| json                       | 5.41 ms                                                                | 5.51 ms: 1.02x slower                                                           |
| xml_etree_process          | 57.7 ms                                                                | 58.9 ms: 1.02x slower                                                           |
| async_tree_memoization_tg  | 311 ms                                                                 | 317 ms: 1.02x slower                                                            |
| async_tree_none_tg         | 246 ms                                                                 | 251 ms: 1.02x slower                                                            |
| mako                       | 11.2 ms                                                                | 11.5 ms: 1.02x slower                                                           |
| async_tree_none            | 255 ms                                                                 | 261 ms: 1.02x slower                                                            |
| genshi_text                | 20.6 ms                                                                | 21.1 ms: 1.02x slower                                                           |
| json_loads                 | 29.8 us                                                                | 30.5 us: 1.02x slower                                                           |
| xml_etree_generate         | 82.9 ms                                                                | 84.8 ms: 1.02x slower                                                           |
| comprehensions             | 16.6 us                                                                | 17.0 us: 1.02x slower                                                           |
| nqueens                    | 79.6 ms                                                                | 81.5 ms: 1.02x slower                                                           |
| typing_runtime_protocols   | 162 us                                                                 | 166 us: 1.03x slower                                                            |
| pathlib                    | 16.5 ms                                                                | 17.0 ms: 1.03x slower                                                           |
| tomli_loads                | 1.94 sec                                                               | 2.00 sec: 1.03x slower                                                          |
| deepcopy_memo              | 28.5 us                                                                | 29.4 us: 1.03x slower                                                           |
| scimark_monte_carlo        | 63.8 ms                                                                | 65.9 ms: 1.03x slower                                                           |
| deepcopy                   | 244 us                                                                 | 253 us: 1.04x slower                                                            |
| pyflate                    | 438 ms                                                                 | 454 ms: 1.04x slower                                                            |
| scimark_sor                | 115 ms                                                                 | 120 ms: 1.04x slower                                                            |
| regex_v8                   | 22.9 ms                                                                | 23.8 ms: 1.04x slower                                                           |
| deepcopy_reduce            | 2.55 us                                                                | 2.65 us: 1.04x slower                                                           |
| gc_traversal               | 4.82 ms                                                                | 5.03 ms: 1.04x slower                                                           |
| crypto_pyaes               | 71.3 ms                                                                | 74.4 ms: 1.04x slower                                                           |
| raytrace                   | 252 ms                                                                 | 264 ms: 1.05x slower                                                            |
| scimark_fft                | 341 ms                                                                 | 357 ms: 1.05x slower                                                            |
| chaos                      | 54.3 ms                                                                | 57.0 ms: 1.05x slower                                                           |
| async_generators           | 384 ms                                                                 | 407 ms: 1.06x slower                                                            |
| spectral_norm              | 98.3 ms                                                                | 104 ms: 1.06x slower                                                            |
| float                      | 66.1 ms                                                                | 70.6 ms: 1.07x slower                                                           |
| nbody                      | 87.8 ms                                                                | 94.6 ms: 1.08x slower                                                           |
| Geometric mean             | (ref)                                                                  | 1.02x slower                                                                    |

Benchmark hidden because not significant (15): richards, k_core, create_gc_cycles, asyncio_websockets, hexiom, json_dumps, deltablue, shortest_path, coverage, sqlite_synth, html5lib, pylint, sphinx, async_tree_io, async_tree_io_tg

- Geometric mean (including insignificant results): 1.015x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.00x