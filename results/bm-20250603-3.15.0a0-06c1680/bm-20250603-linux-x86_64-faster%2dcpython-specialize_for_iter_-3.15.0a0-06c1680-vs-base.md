# Results vs. base

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: linux-x86_64
- commit hash: 06c1680
- commit date: 2025-06-03
- overall geometric mean: 1.004x slower
- HPT reliability: 93.66%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 | bm-20250603-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                                | 256 ms: 1.00x slower                                                            |
| html5lib       | 61.7 ms                                                               | 60.9 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 | bm-20250603-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg           | 634 ms                                                                | 615 ms: 1.03x faster                                                            |
| coroutines                 | 26.0 ms                                                               | 25.6 ms: 1.01x faster                                                           |
| async_generators           | 416 ms                                                                | 412 ms: 1.01x faster                                                            |
| async_tree_cpu_io_mixed_tg | 488 ms                                                                | 497 ms: 1.02x slower                                                            |
| async_tree_cpu_io_mixed    | 494 ms                                                                | 505 ms: 1.02x slower                                                            |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (6): async_tree_none, async_tree_memoization_tg, async_tree_none_tg, async_tree_io, async_tree_memoization, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 | bm-20250603-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 71.5 ms                                                               | 73.2 ms: 1.02x slower                                                           |
| pidigits       | 187 ms                                                                | 192 ms: 1.03x slower                                                            |
| nbody          | 98.1 ms                                                               | 102 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 | bm-20250603-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 23.2 ms                                                               | 23.2 ms: 1.00x slower                                                           |
| regex_effbot   | 3.22 ms                                                               | 3.26 ms: 1.01x slower                                                           |
| regex_dna      | 194 ms                                                                | 205 ms: 1.06x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                                    |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 | bm-20250603-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_pure_python | 220 us                                                                | 222 us: 1.01x slower                                                            |
| xml_etree_process    | 60.0 ms                                                               | 60.4 ms: 1.01x slower                                                           |
| json_dumps           | 10.9 ms                                                               | 11.0 ms: 1.01x slower                                                           |
| pickle_pure_python   | 319 us                                                                | 322 us: 1.01x slower                                                            |
| tomli_loads          | 2.01 sec                                                              | 2.03 sec: 1.01x slower                                                          |
| json_loads           | 27.9 us                                                               | 28.4 us: 1.02x slower                                                           |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (3): xml_etree_generate, xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 | bm-20250603-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.95 ms                                                               | 6.92 ms: 1.00x faster                                                           |
| python_startup         | 12.2 ms                                                               | 12.2 ms: 1.00x faster                                                           |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 | bm-20250603-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text    | 21.4 ms                                                               | 21.6 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (3): django_template, genshi_xml, mako

All benchmarks:
===============

| Benchmark                  | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 | bm-20250603-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| shortest_path              | 523 ms                                                                | 494 ms: 1.06x faster                                                            |
| async_tree_io_tg           | 634 ms                                                                | 615 ms: 1.03x faster                                                            |
| connected_components       | 479 ms                                                                | 466 ms: 1.03x faster                                                            |
| chaos                      | 61.0 ms                                                               | 60.2 ms: 1.01x faster                                                           |
| gc_traversal               | 5.00 ms                                                               | 4.93 ms: 1.01x faster                                                           |
| coroutines                 | 26.0 ms                                                               | 25.6 ms: 1.01x faster                                                           |
| html5lib                   | 61.7 ms                                                               | 60.9 ms: 1.01x faster                                                           |
| async_generators           | 416 ms                                                                | 412 ms: 1.01x faster                                                            |
| generators                 | 30.5 ms                                                               | 30.2 ms: 1.01x faster                                                           |
| bpe_tokeniser              | 4.53 sec                                                              | 4.50 sec: 1.01x faster                                                          |
| sqlglot_v2_parse           | 1.26 ms                                                               | 1.26 ms: 1.01x faster                                                           |
| many_optionals             | 958 us                                                                | 953 us: 1.00x faster                                                            |
| python_startup_no_site     | 6.95 ms                                                               | 6.92 ms: 1.00x faster                                                           |
| python_startup             | 12.2 ms                                                               | 12.2 ms: 1.00x faster                                                           |
| sqlglot_v2_optimize        | 52.2 ms                                                               | 52.0 ms: 1.00x faster                                                           |
| dulwich_log                | 59.7 ms                                                               | 59.6 ms: 1.00x faster                                                           |
| nqueens                    | 81.6 ms                                                               | 81.4 ms: 1.00x faster                                                           |
| 2to3                       | 255 ms                                                                | 256 ms: 1.00x slower                                                            |
| scimark_sparse_mat_mult    | 5.12 ms                                                               | 5.14 ms: 1.00x slower                                                           |
| regex_v8                   | 23.2 ms                                                               | 23.2 ms: 1.00x slower                                                           |
| deltablue                  | 3.52 ms                                                               | 3.54 ms: 1.00x slower                                                           |
| create_gc_cycles           | 2.57 ms                                                               | 2.59 ms: 1.00x slower                                                           |
| scimark_fft                | 380 ms                                                                | 382 ms: 1.01x slower                                                            |
| logging_silent             | 475 ns                                                                | 478 ns: 1.01x slower                                                            |
| fannkuch                   | 417 ms                                                                | 419 ms: 1.01x slower                                                            |
| thrift                     | 148 ms                                                                | 149 ms: 1.01x slower                                                            |
| unpickle_pure_python       | 220 us                                                                | 222 us: 1.01x slower                                                            |
| xml_etree_process          | 60.0 ms                                                               | 60.4 ms: 1.01x slower                                                           |
| genshi_text                | 21.4 ms                                                               | 21.6 ms: 1.01x slower                                                           |
| sympy_expand               | 452 ms                                                                | 455 ms: 1.01x slower                                                            |
| json_dumps                 | 10.9 ms                                                               | 11.0 ms: 1.01x slower                                                           |
| crypto_pyaes               | 75.5 ms                                                               | 76.2 ms: 1.01x slower                                                           |
| pickle_pure_python         | 319 us                                                                | 322 us: 1.01x slower                                                            |
| tomli_loads                | 2.01 sec                                                              | 2.03 sec: 1.01x slower                                                          |
| comprehensions             | 16.0 us                                                               | 16.2 us: 1.01x slower                                                           |
| raytrace                   | 270 ms                                                                | 273 ms: 1.01x slower                                                            |
| json                       | 5.15 ms                                                               | 5.21 ms: 1.01x slower                                                           |
| regex_effbot               | 3.22 ms                                                               | 3.26 ms: 1.01x slower                                                           |
| hexiom                     | 6.04 ms                                                               | 6.11 ms: 1.01x slower                                                           |
| go                         | 112 ms                                                                | 113 ms: 1.02x slower                                                            |
| spectral_norm              | 109 ms                                                                | 111 ms: 1.02x slower                                                            |
| json_loads                 | 27.9 us                                                               | 28.4 us: 1.02x slower                                                           |
| async_tree_cpu_io_mixed_tg | 488 ms                                                                | 497 ms: 1.02x slower                                                            |
| typing_runtime_protocols   | 166 us                                                                | 170 us: 1.02x slower                                                            |
| async_tree_cpu_io_mixed    | 494 ms                                                                | 505 ms: 1.02x slower                                                            |
| pathlib                    | 17.2 ms                                                               | 17.6 ms: 1.02x slower                                                           |
| float                      | 71.5 ms                                                               | 73.2 ms: 1.02x slower                                                           |
| pidigits                   | 187 ms                                                                | 192 ms: 1.03x slower                                                            |
| meteor_contest             | 105 ms                                                                | 108 ms: 1.03x slower                                                            |
| scimark_monte_carlo        | 67.9 ms                                                               | 69.9 ms: 1.03x slower                                                           |
| pyflate                    | 432 ms                                                                | 446 ms: 1.03x slower                                                            |
| coverage                   | 426 ms                                                                | 442 ms: 1.04x slower                                                            |
| nbody                      | 98.1 ms                                                               | 102 ms: 1.04x slower                                                            |
| pycparser                  | 1.13 sec                                                              | 1.18 sec: 1.04x slower                                                          |
| regex_dna                  | 194 ms                                                                | 205 ms: 1.06x slower                                                            |
| Geometric mean             | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (37): async_tree_none, async_tree_memoization_tg, async_tree_none_tg, sphinx, async_tree_io, sympy_sum, xml_etree_generate, logging_simple, async_tree_memoization, sqlite_synth, pprint_pformat, xml_etree_parse, django_template, deepcopy_reduce, richards_super, pprint_safe_repr, docutils, sqlglot_v2_normalize, pylint, scimark_sor, xml_etree_iterparse, sympy_integrate, sympy_str, sqlglot_v2_transpile, genshi_xml, mako, deepcopy_memo, deepcopy, asyncio_websockets, logging_format, richards, mdp, k_core, telco, regex_compile, subparsers, scimark_lu

- Geometric mean (including insignificant results): 1.004x slower

# HPT report

- Reliability score: 93.66% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x