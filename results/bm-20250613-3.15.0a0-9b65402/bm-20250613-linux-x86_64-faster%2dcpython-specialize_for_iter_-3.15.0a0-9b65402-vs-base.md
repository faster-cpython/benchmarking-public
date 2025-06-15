# Results vs. base

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: linux-x86_64
- commit hash: 9b65402
- commit date: 2025-06-13
- overall geometric mean: 1.004x slower
- HPT reliability: 90.21%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250613-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| docutils       | 2.58 sec                                                              | 2.56 sec: 1.01x faster                                                          |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250613-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|---------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg          | 631 ms                                                                | 611 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed   | 502 ms                                                                | 496 ms: 1.01x faster                                                            |
| async_generators          | 411 ms                                                                | 407 ms: 1.01x faster                                                            |
| coroutines                | 25.0 ms                                                               | 25.0 ms: 1.00x slower                                                           |
| async_tree_memoization    | 310 ms                                                                | 313 ms: 1.01x slower                                                            |
| async_tree_none_tg        | 245 ms                                                                | 249 ms: 1.02x slower                                                            |
| async_tree_memoization_tg | 307 ms                                                                | 314 ms: 1.02x slower                                                            |
| Geometric mean            | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed_tg, async_tree_none, asyncio_websockets, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250613-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 192 ms                                                                | 188 ms: 1.02x faster                                                            |
| float          | 72.4 ms                                                               | 73.9 ms: 1.02x slower                                                           |
| nbody          | 97.3 ms                                                               | 100 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250613-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 127 ms                                                                | 127 ms: 1.00x slower                                                            |
| regex_dna      | 184 ms                                                                | 184 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250613-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.04 sec                                                              | 1.99 sec: 1.03x faster                                                          |
| pickle_pure_python   | 322 us                                                                | 317 us: 1.01x faster                                                            |
| xml_etree_iterparse  | 98.7 ms                                                               | 99.3 ms: 1.01x slower                                                           |
| json_loads           | 27.4 us                                                               | 27.7 us: 1.01x slower                                                           |
| xml_etree_process    | 59.6 ms                                                               | 60.2 ms: 1.01x slower                                                           |
| unpickle_pure_python | 217 us                                                                | 220 us: 1.01x slower                                                            |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (3): xml_etree_parse, json_dumps, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250613-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.91 ms                                                               | 6.91 ms: 1.00x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250613-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako           | 11.4 ms                                                               | 11.3 ms: 1.01x faster                                                           |
| genshi_text    | 21.0 ms                                                               | 21.5 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                 | bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250613-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|---------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| coverage                  | 433 ms                                                                | 419 ms: 1.03x faster                                                            |
| async_tree_io_tg          | 631 ms                                                                | 611 ms: 1.03x faster                                                            |
| tomli_loads               | 2.04 sec                                                              | 1.99 sec: 1.03x faster                                                          |
| logging_simple            | 6.32 us                                                               | 6.17 us: 1.02x faster                                                           |
| pathlib                   | 17.4 ms                                                               | 17.0 ms: 1.02x faster                                                           |
| pidigits                  | 192 ms                                                                | 188 ms: 1.02x faster                                                            |
| logging_format            | 7.00 us                                                               | 6.89 us: 1.02x faster                                                           |
| pickle_pure_python        | 322 us                                                                | 317 us: 1.01x faster                                                            |
| chaos                     | 60.3 ms                                                               | 59.5 ms: 1.01x faster                                                           |
| async_tree_cpu_io_mixed   | 502 ms                                                                | 496 ms: 1.01x faster                                                            |
| async_generators          | 411 ms                                                                | 407 ms: 1.01x faster                                                            |
| raytrace                  | 272 ms                                                                | 270 ms: 1.01x faster                                                            |
| mako                      | 11.4 ms                                                               | 11.3 ms: 1.01x faster                                                           |
| bpe_tokeniser             | 4.50 sec                                                              | 4.47 sec: 1.01x faster                                                          |
| docutils                  | 2.58 sec                                                              | 2.56 sec: 1.01x faster                                                          |
| thrift                    | 148 ms                                                                | 147 ms: 1.00x faster                                                            |
| sympy_sum                 | 149 ms                                                                | 149 ms: 1.00x faster                                                            |
| create_gc_cycles          | 2.59 ms                                                               | 2.58 ms: 1.00x faster                                                           |
| dulwich_log               | 59.7 ms                                                               | 59.5 ms: 1.00x faster                                                           |
| python_startup_no_site    | 6.91 ms                                                               | 6.91 ms: 1.00x slower                                                           |
| regex_compile             | 127 ms                                                                | 127 ms: 1.00x slower                                                            |
| sympy_integrate           | 18.9 ms                                                               | 19.0 ms: 1.00x slower                                                           |
| regex_dna                 | 184 ms                                                                | 184 ms: 1.00x slower                                                            |
| coroutines                | 25.0 ms                                                               | 25.0 ms: 1.00x slower                                                           |
| mdp                       | 1.23 sec                                                              | 1.23 sec: 1.00x slower                                                          |
| sympy_str                 | 266 ms                                                                | 268 ms: 1.00x slower                                                            |
| sqlglot_v2_optimize       | 52.5 ms                                                               | 52.7 ms: 1.01x slower                                                           |
| xml_etree_iterparse       | 98.7 ms                                                               | 99.3 ms: 1.01x slower                                                           |
| pyflate                   | 427 ms                                                                | 430 ms: 1.01x slower                                                            |
| json_loads                | 27.4 us                                                               | 27.7 us: 1.01x slower                                                           |
| crypto_pyaes              | 74.5 ms                                                               | 75.1 ms: 1.01x slower                                                           |
| sympy_expand              | 451 ms                                                                | 455 ms: 1.01x slower                                                            |
| nqueens                   | 80.6 ms                                                               | 81.3 ms: 1.01x slower                                                           |
| xml_etree_process         | 59.6 ms                                                               | 60.2 ms: 1.01x slower                                                           |
| typing_runtime_protocols  | 168 us                                                                | 170 us: 1.01x slower                                                            |
| hexiom                    | 5.97 ms                                                               | 6.03 ms: 1.01x slower                                                           |
| async_tree_memoization    | 310 ms                                                                | 313 ms: 1.01x slower                                                            |
| logging_silent            | 468 ns                                                                | 473 ns: 1.01x slower                                                            |
| sqlglot_v2_normalize      | 106 ms                                                                | 107 ms: 1.01x slower                                                            |
| scimark_monte_carlo       | 67.6 ms                                                               | 68.4 ms: 1.01x slower                                                           |
| unpickle_pure_python      | 217 us                                                                | 220 us: 1.01x slower                                                            |
| fannkuch                  | 408 ms                                                                | 414 ms: 1.01x slower                                                            |
| subparsers                | 23.4 ms                                                               | 23.7 ms: 1.01x slower                                                           |
| deepcopy_memo             | 28.8 us                                                               | 29.2 us: 1.01x slower                                                           |
| async_tree_none_tg        | 245 ms                                                                | 249 ms: 1.02x slower                                                            |
| go                        | 110 ms                                                                | 112 ms: 1.02x slower                                                            |
| shortest_path             | 497 ms                                                                | 506 ms: 1.02x slower                                                            |
| richards_super            | 48.6 ms                                                               | 49.5 ms: 1.02x slower                                                           |
| pprint_pformat            | 1.63 sec                                                              | 1.67 sec: 1.02x slower                                                          |
| float                     | 72.4 ms                                                               | 73.9 ms: 1.02x slower                                                           |
| deltablue                 | 3.47 ms                                                               | 3.54 ms: 1.02x slower                                                           |
| async_tree_memoization_tg | 307 ms                                                                | 314 ms: 1.02x slower                                                            |
| pprint_safe_repr          | 799 ms                                                                | 818 ms: 1.02x slower                                                            |
| richards                  | 42.4 ms                                                               | 43.4 ms: 1.02x slower                                                           |
| sqlglot_v2_transpile      | 1.54 ms                                                               | 1.58 ms: 1.03x slower                                                           |
| sqlglot_v2_parse          | 1.24 ms                                                               | 1.27 ms: 1.03x slower                                                           |
| genshi_text               | 21.0 ms                                                               | 21.5 ms: 1.03x slower                                                           |
| deepcopy                  | 254 us                                                                | 261 us: 1.03x slower                                                            |
| nbody                     | 97.3 ms                                                               | 100 ms: 1.03x slower                                                            |
| scimark_fft               | 372 ms                                                                | 384 ms: 1.03x slower                                                            |
| gc_traversal              | 4.78 ms                                                               | 5.17 ms: 1.08x slower                                                           |
| Geometric mean            | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (31): xml_etree_parse, sphinx, k_core, meteor_contest, pylint, telco, async_tree_cpu_io_mixed_tg, scimark_sor, async_tree_none, sqlite_synth, scimark_sparse_mat_mult, pycparser, scimark_lu, generators, 2to3, many_optionals, asyncio_websockets, regex_v8, python_startup, django_template, async_tree_io, json_dumps, xml_etree_generate, regex_effbot, comprehensions, spectral_norm, json, connected_components, deepcopy_reduce, genshi_xml, html5lib

- Geometric mean (including insignificant results): 1.004x slower

# HPT report

- Reliability score: 90.21% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x