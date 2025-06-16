# Results vs. base

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: linux-x86_64
- commit hash: c41d531
- commit date: 2025-06-16
- overall geometric mean: 1.002x faster
- HPT reliability: 98.91%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250616-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                                | 254 ms: 1.00x faster                                                            |
| docutils       | 2.57 sec                                                              | 2.57 sec: 1.00x faster                                                          |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250616-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| coroutines                 | 26.4 ms                                                               | 25.1 ms: 1.05x faster                                                           |
| async_tree_cpu_io_mixed    | 491 ms                                                                | 499 ms: 1.02x slower                                                            |
| async_tree_memoization_tg  | 309 ms                                                                | 315 ms: 1.02x slower                                                            |
| async_tree_cpu_io_mixed_tg | 482 ms                                                                | 492 ms: 1.02x slower                                                            |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (7): async_tree_none, async_tree_io, asyncio_websockets, async_tree_io_tg, async_tree_memoization, async_generators, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250616-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 100 ms                                                                | 97.8 ms: 1.03x faster                                                           |
| pidigits       | 188 ms                                                                | 188 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250616-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 128 ms                                                                | 127 ms: 1.01x faster                                                            |
| regex_effbot   | 3.09 ms                                                               | 3.15 ms: 1.02x slower                                                           |
| regex_dna      | 182 ms                                                                | 191 ms: 1.05x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250616-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|---------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python  | 324 us                                                                | 319 us: 1.02x faster                                                            |
| tomli_loads         | 2.06 sec                                                              | 2.03 sec: 1.02x faster                                                          |
| xml_etree_iterparse | 98.7 ms                                                               | 99.3 ms: 1.01x slower                                                           |
| xml_etree_generate  | 85.3 ms                                                               | 85.9 ms: 1.01x slower                                                           |
| json_loads          | 28.1 us                                                               | 28.5 us: 1.01x slower                                                           |
| Geometric mean      | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (4): json_dumps, xml_etree_process, unpickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250616-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 6.93 ms: 1.01x slower                                                           |
| python_startup         | 12.1 ms                                                               | 12.2 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250616-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako           | 11.4 ms                                                               | 11.3 ms: 1.00x faster                                                           |
| genshi_xml     | 49.2 ms                                                               | 50.0 ms: 1.02x slower                                                           |
| genshi_text    | 21.2 ms                                                               | 21.7 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250616-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| coroutines                 | 26.4 ms                                                               | 25.1 ms: 1.05x faster                                                           |
| chaos                      | 61.6 ms                                                               | 59.2 ms: 1.04x faster                                                           |
| scimark_lu                 | 120 ms                                                                | 116 ms: 1.03x faster                                                            |
| crypto_pyaes               | 76.4 ms                                                               | 74.2 ms: 1.03x faster                                                           |
| raytrace                   | 276 ms                                                                | 269 ms: 1.03x faster                                                            |
| nbody                      | 100 ms                                                                | 97.8 ms: 1.03x faster                                                           |
| pyflate                    | 445 ms                                                                | 435 ms: 1.02x faster                                                            |
| sqlglot_v2_parse           | 1.27 ms                                                               | 1.24 ms: 1.02x faster                                                           |
| go                         | 113 ms                                                                | 111 ms: 1.02x faster                                                            |
| sqlglot_v2_transpile       | 1.58 ms                                                               | 1.55 ms: 1.02x faster                                                           |
| pathlib                    | 17.3 ms                                                               | 17.0 ms: 1.02x faster                                                           |
| pickle_pure_python         | 324 us                                                                | 319 us: 1.02x faster                                                            |
| nqueens                    | 82.3 ms                                                               | 80.8 ms: 1.02x faster                                                           |
| hexiom                     | 6.16 ms                                                               | 6.05 ms: 1.02x faster                                                           |
| generators                 | 30.1 ms                                                               | 29.6 ms: 1.02x faster                                                           |
| scimark_sor                | 122 ms                                                                | 120 ms: 1.02x faster                                                            |
| logging_format             | 6.88 us                                                               | 6.77 us: 1.02x faster                                                           |
| tomli_loads                | 2.06 sec                                                              | 2.03 sec: 1.02x faster                                                          |
| scimark_monte_carlo        | 68.2 ms                                                               | 67.2 ms: 1.02x faster                                                           |
| coverage                   | 424 ms                                                                | 418 ms: 1.01x faster                                                            |
| bpe_tokeniser              | 4.57 sec                                                              | 4.50 sec: 1.01x faster                                                          |
| comprehensions             | 16.2 us                                                               | 16.0 us: 1.01x faster                                                           |
| deltablue                  | 3.54 ms                                                               | 3.49 ms: 1.01x faster                                                           |
| fannkuch                   | 423 ms                                                                | 418 ms: 1.01x faster                                                            |
| meteor_contest             | 107 ms                                                                | 106 ms: 1.01x faster                                                            |
| logging_simple             | 6.13 us                                                               | 6.07 us: 1.01x faster                                                           |
| telco                      | 8.06 ms                                                               | 7.98 ms: 1.01x faster                                                           |
| regex_compile              | 128 ms                                                                | 127 ms: 1.01x faster                                                            |
| many_optionals             | 960 us                                                                | 954 us: 1.01x faster                                                            |
| sympy_sum                  | 149 ms                                                                | 148 ms: 1.01x faster                                                            |
| mdp                        | 1.23 sec                                                              | 1.22 sec: 1.01x faster                                                          |
| deepcopy_memo              | 29.3 us                                                               | 29.2 us: 1.01x faster                                                           |
| dulwich_log                | 59.4 ms                                                               | 59.2 ms: 1.00x faster                                                           |
| 2to3                       | 255 ms                                                                | 254 ms: 1.00x faster                                                            |
| sympy_str                  | 267 ms                                                                | 266 ms: 1.00x faster                                                            |
| sympy_integrate            | 19.0 ms                                                               | 18.9 ms: 1.00x faster                                                           |
| docutils                   | 2.57 sec                                                              | 2.57 sec: 1.00x faster                                                          |
| mako                       | 11.4 ms                                                               | 11.3 ms: 1.00x faster                                                           |
| pidigits                   | 188 ms                                                                | 188 ms: 1.00x slower                                                            |
| sqlglot_v2_optimize        | 52.8 ms                                                               | 52.9 ms: 1.00x slower                                                           |
| thrift                     | 148 ms                                                                | 149 ms: 1.00x slower                                                            |
| python_startup_no_site     | 6.89 ms                                                               | 6.93 ms: 1.01x slower                                                           |
| create_gc_cycles           | 2.57 ms                                                               | 2.59 ms: 1.01x slower                                                           |
| python_startup             | 12.1 ms                                                               | 12.2 ms: 1.01x slower                                                           |
| xml_etree_iterparse        | 98.7 ms                                                               | 99.3 ms: 1.01x slower                                                           |
| xml_etree_generate         | 85.3 ms                                                               | 85.9 ms: 1.01x slower                                                           |
| typing_runtime_protocols   | 165 us                                                                | 166 us: 1.01x slower                                                            |
| deepcopy                   | 258 us                                                                | 261 us: 1.01x slower                                                            |
| json_loads                 | 28.1 us                                                               | 28.5 us: 1.01x slower                                                           |
| async_tree_cpu_io_mixed    | 491 ms                                                                | 499 ms: 1.02x slower                                                            |
| genshi_xml                 | 49.2 ms                                                               | 50.0 ms: 1.02x slower                                                           |
| async_tree_memoization_tg  | 309 ms                                                                | 315 ms: 1.02x slower                                                            |
| regex_effbot               | 3.09 ms                                                               | 3.15 ms: 1.02x slower                                                           |
| scimark_fft                | 375 ms                                                                | 383 ms: 1.02x slower                                                            |
| spectral_norm              | 109 ms                                                                | 111 ms: 1.02x slower                                                            |
| genshi_text                | 21.2 ms                                                               | 21.7 ms: 1.02x slower                                                           |
| async_tree_cpu_io_mixed_tg | 482 ms                                                                | 492 ms: 1.02x slower                                                            |
| shortest_path              | 509 ms                                                                | 521 ms: 1.02x slower                                                            |
| pycparser                  | 1.10 sec                                                              | 1.13 sec: 1.02x slower                                                          |
| gc_traversal               | 4.93 ms                                                               | 5.07 ms: 1.03x slower                                                           |
| scimark_sparse_mat_mult    | 4.91 ms                                                               | 5.11 ms: 1.04x slower                                                           |
| regex_dna                  | 182 ms                                                                | 191 ms: 1.05x slower                                                            |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (30): async_tree_none, pylint, async_tree_io, richards_super, richards, float, sphinx, html5lib, regex_v8, logging_silent, asyncio_websockets, async_tree_io_tg, async_tree_memoization, async_generators, sqlite_synth, django_template, sympy_expand, json_dumps, pprint_pformat, xml_etree_process, json, subparsers, unpickle_pure_python, pprint_safe_repr, k_core, sqlglot_v2_normalize, deepcopy_reduce, async_tree_none_tg, xml_etree_parse, connected_components

- Geometric mean (including insignificant results): 1.002x faster

# HPT report

- Reliability score: 98.91% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x