# Results vs. base

- fork: faster-cpython
- ref: trashcan_in_dealloc
- machine: linux-x86_64
- commit hash: 8aa20f2
- commit date: 2025-04-09
- overall geometric mean: 1.015x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250408-linux-x86_64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                                 | 252 ms: 1.01x slower                                                            |
| html5lib       | 59.8 ms                                                                | 61.0 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                    |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250408-linux-x86_64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization     | 310 ms                                                                 | 315 ms: 1.02x slower                                                            |
| async_tree_none_tg         | 245 ms                                                                 | 250 ms: 1.02x slower                                                            |
| async_tree_cpu_io_mixed_tg | 473 ms                                                                 | 484 ms: 1.02x slower                                                            |
| async_tree_none            | 255 ms                                                                 | 261 ms: 1.02x slower                                                            |
| async_tree_cpu_io_mixed    | 479 ms                                                                 | 490 ms: 1.02x slower                                                            |
| async_tree_io              | 604 ms                                                                 | 619 ms: 1.02x slower                                                            |
| coroutines                 | 23.3 ms                                                                | 24.0 ms: 1.03x slower                                                           |
| async_generators           | 391 ms                                                                 | 405 ms: 1.04x slower                                                            |
| Geometric mean             | (ref)                                                                  | 1.02x slower                                                                    |

Benchmark hidden because not significant (3): asyncio_websockets, async_tree_io_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250408-linux-x86_64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 90.2 ms                                                                | 89.3 ms: 1.01x faster                                                           |
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x slower                                                            |
| float          | 65.9 ms                                                                | 69.7 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250408-linux-x86_64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 23.0 ms                                                                | 22.0 ms: 1.04x faster                                                           |
| regex_dna      | 219 ms                                                                 | 213 ms: 1.03x faster                                                            |
| regex_effbot   | 3.31 ms                                                                | 3.33 ms: 1.00x slower                                                           |
| regex_compile  | 123 ms                                                                 | 126 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250408-linux-x86_64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_process    | 58.3 ms                                                                | 58.5 ms: 1.00x slower                                                           |
| xml_etree_generate   | 83.8 ms                                                                | 84.3 ms: 1.01x slower                                                           |
| xml_etree_parse      | 141 ms                                                                 | 142 ms: 1.01x slower                                                            |
| pickle_pure_python   | 310 us                                                                 | 314 us: 1.01x slower                                                            |
| json_loads           | 29.8 us                                                                | 30.3 us: 1.02x slower                                                           |
| unpickle_pure_python | 214 us                                                                 | 218 us: 1.02x slower                                                            |
| tomli_loads          | 1.91 sec                                                               | 1.97 sec: 1.03x slower                                                          |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                                    |

Benchmark hidden because not significant (2): json_dumps, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250408-linux-x86_64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 8.21 ms                                                                | 8.22 ms: 1.00x slower                                                           |
| python_startup         | 13.2 ms                                                                | 13.2 ms: 1.00x slower                                                           |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250408-linux-x86_64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                                | 11.1 ms: 1.01x faster                                                           |
| django_template | 32.0 ms                                                                | 31.9 ms: 1.00x faster                                                           |
| genshi_xml      | 48.5 ms                                                                | 48.9 ms: 1.01x slower                                                           |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                                    |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20250408-linux-x86_64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8                   | 23.0 ms                                                                | 22.0 ms: 1.04x faster                                                           |
| regex_dna                  | 219 ms                                                                 | 213 ms: 1.03x faster                                                            |
| generators                 | 30.0 ms                                                                | 29.5 ms: 1.02x faster                                                           |
| nbody                      | 90.2 ms                                                                | 89.3 ms: 1.01x faster                                                           |
| meteor_contest             | 106 ms                                                                 | 105 ms: 1.01x faster                                                            |
| richards                   | 42.8 ms                                                                | 42.5 ms: 1.01x faster                                                           |
| mako                       | 11.1 ms                                                                | 11.1 ms: 1.01x faster                                                           |
| django_template            | 32.0 ms                                                                | 31.9 ms: 1.00x faster                                                           |
| python_startup_no_site     | 8.21 ms                                                                | 8.22 ms: 1.00x slower                                                           |
| create_gc_cycles           | 2.46 ms                                                                | 2.47 ms: 1.00x slower                                                           |
| python_startup             | 13.2 ms                                                                | 13.2 ms: 1.00x slower                                                           |
| pidigits                   | 186 ms                                                                 | 186 ms: 1.00x slower                                                            |
| go                         | 108 ms                                                                 | 108 ms: 1.00x slower                                                            |
| regex_effbot               | 3.31 ms                                                                | 3.33 ms: 1.00x slower                                                           |
| xml_etree_process          | 58.3 ms                                                                | 58.5 ms: 1.00x slower                                                           |
| deltablue                  | 3.27 ms                                                                | 3.28 ms: 1.01x slower                                                           |
| xml_etree_generate         | 83.8 ms                                                                | 84.3 ms: 1.01x slower                                                           |
| genshi_xml                 | 48.5 ms                                                                | 48.9 ms: 1.01x slower                                                           |
| xml_etree_parse            | 141 ms                                                                 | 142 ms: 1.01x slower                                                            |
| shortest_path              | 492 ms                                                                 | 496 ms: 1.01x slower                                                            |
| sympy_integrate            | 19.0 ms                                                                | 19.1 ms: 1.01x slower                                                           |
| bpe_tokeniser              | 4.53 sec                                                               | 4.57 sec: 1.01x slower                                                          |
| sqlalchemy_imperative      | 16.9 ms                                                                | 17.0 ms: 1.01x slower                                                           |
| dulwich_log                | 59.3 ms                                                                | 59.9 ms: 1.01x slower                                                           |
| 2to3                       | 250 ms                                                                 | 252 ms: 1.01x slower                                                            |
| bench_thread_pool          | 874 us                                                                 | 883 us: 1.01x slower                                                            |
| many_optionals             | 923 us                                                                 | 934 us: 1.01x slower                                                            |
| pickle_pure_python         | 310 us                                                                 | 314 us: 1.01x slower                                                            |
| fannkuch                   | 409 ms                                                                 | 415 ms: 1.01x slower                                                            |
| sympy_sum                  | 147 ms                                                                 | 149 ms: 1.01x slower                                                            |
| hexiom                     | 6.04 ms                                                                | 6.12 ms: 1.01x slower                                                           |
| scimark_sor                | 115 ms                                                                 | 117 ms: 1.02x slower                                                            |
| sqlalchemy_declarative     | 131 ms                                                                 | 133 ms: 1.02x slower                                                            |
| json_loads                 | 29.8 us                                                                | 30.3 us: 1.02x slower                                                           |
| sqlglot_v2_parse           | 1.21 ms                                                                | 1.23 ms: 1.02x slower                                                           |
| sqlglot_v2_transpile       | 1.52 ms                                                                | 1.54 ms: 1.02x slower                                                           |
| unpickle_pure_python       | 214 us                                                                 | 218 us: 1.02x slower                                                            |
| async_tree_memoization     | 310 ms                                                                 | 315 ms: 1.02x slower                                                            |
| sympy_str                  | 264 ms                                                                 | 269 ms: 1.02x slower                                                            |
| mdp                        | 1.21 sec                                                               | 1.24 sec: 1.02x slower                                                          |
| pathlib                    | 16.6 ms                                                                | 16.9 ms: 1.02x slower                                                           |
| sqlglot_v2_optimize        | 51.7 ms                                                                | 52.7 ms: 1.02x slower                                                           |
| html5lib                   | 59.8 ms                                                                | 61.0 ms: 1.02x slower                                                           |
| sqlglot_v2_normalize       | 105 ms                                                                 | 107 ms: 1.02x slower                                                            |
| async_tree_none_tg         | 245 ms                                                                 | 250 ms: 1.02x slower                                                            |
| nqueens                    | 80.0 ms                                                                | 81.6 ms: 1.02x slower                                                           |
| pprint_pformat             | 1.44 sec                                                               | 1.48 sec: 1.02x slower                                                          |
| async_tree_cpu_io_mixed_tg | 473 ms                                                                 | 484 ms: 1.02x slower                                                            |
| async_tree_none            | 255 ms                                                                 | 261 ms: 1.02x slower                                                            |
| scimark_lu                 | 115 ms                                                                 | 118 ms: 1.02x slower                                                            |
| sympy_expand               | 448 ms                                                                 | 459 ms: 1.02x slower                                                            |
| async_tree_cpu_io_mixed    | 479 ms                                                                 | 490 ms: 1.02x slower                                                            |
| comprehensions             | 16.4 us                                                                | 16.9 us: 1.02x slower                                                           |
| async_tree_io              | 604 ms                                                                 | 619 ms: 1.02x slower                                                            |
| scimark_monte_carlo        | 65.1 ms                                                                | 66.7 ms: 1.02x slower                                                           |
| regex_compile              | 123 ms                                                                 | 126 ms: 1.03x slower                                                            |
| pprint_safe_repr           | 703 ms                                                                 | 721 ms: 1.03x slower                                                            |
| telco                      | 7.78 ms                                                                | 7.99 ms: 1.03x slower                                                           |
| connected_components       | 448 ms                                                                 | 461 ms: 1.03x slower                                                            |
| tomli_loads                | 1.91 sec                                                               | 1.97 sec: 1.03x slower                                                          |
| deepcopy_reduce            | 2.64 us                                                                | 2.72 us: 1.03x slower                                                           |
| coroutines                 | 23.3 ms                                                                | 24.0 ms: 1.03x slower                                                           |
| async_generators           | 391 ms                                                                 | 405 ms: 1.04x slower                                                            |
| json                       | 5.43 ms                                                                | 5.63 ms: 1.04x slower                                                           |
| gc_traversal               | 4.61 ms                                                                | 4.79 ms: 1.04x slower                                                           |
| raytrace                   | 255 ms                                                                 | 266 ms: 1.04x slower                                                            |
| deepcopy_memo              | 28.4 us                                                                | 29.7 us: 1.05x slower                                                           |
| deepcopy                   | 245 us                                                                 | 257 us: 1.05x slower                                                            |
| logging_simple             | 5.35 us                                                                | 5.60 us: 1.05x slower                                                           |
| logging_format             | 5.91 us                                                                | 6.21 us: 1.05x slower                                                           |
| scimark_sparse_mat_mult    | 4.68 ms                                                                | 4.92 ms: 1.05x slower                                                           |
| logging_silent             | 92.5 ns                                                                | 97.6 ns: 1.06x slower                                                           |
| float                      | 65.9 ms                                                                | 69.7 ms: 1.06x slower                                                           |
| scimark_fft                | 336 ms                                                                 | 356 ms: 1.06x slower                                                            |
| crypto_pyaes               | 71.7 ms                                                                | 76.0 ms: 1.06x slower                                                           |
| spectral_norm              | 98.5 ms                                                                | 105 ms: 1.06x slower                                                            |
| chaos                      | 54.6 ms                                                                | 58.1 ms: 1.06x slower                                                           |
| Geometric mean             | (ref)                                                                  | 1.02x slower                                                                    |

Benchmark hidden because not significant (18): json_dumps, typing_runtime_protocols, richards_super, sqlite_synth, asyncio_websockets, xml_etree_iterparse, genshi_text, docutils, pyflate, coverage, sphinx, subparsers, bench_mp_pool, async_tree_io_tg, pycparser, k_core, pylint, async_tree_memoization_tg

- Geometric mean (including insignificant results): 1.015x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x