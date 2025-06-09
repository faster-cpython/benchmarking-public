# Results vs. base

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: linux-x86_64
- commit hash: baf4722
- commit date: 2025-06-09
- overall geometric mean: 1.000x slower
- HPT reliability: 97.46%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250609-linux-x86_64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a | bm-20250609-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                                | 254 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250609-linux-x86_64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a | bm-20250609-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| coroutines                 | 25.8 ms                                                               | 24.7 ms: 1.04x faster                                                           |
| async_tree_io_tg           | 632 ms                                                                | 619 ms: 1.02x faster                                                            |
| async_tree_none            | 264 ms                                                                | 260 ms: 1.01x faster                                                            |
| async_tree_io              | 602 ms                                                                | 595 ms: 1.01x faster                                                            |
| async_tree_memoization     | 317 ms                                                                | 314 ms: 1.01x faster                                                            |
| async_tree_cpu_io_mixed    | 495 ms                                                                | 491 ms: 1.01x faster                                                            |
| async_tree_cpu_io_mixed_tg | 486 ms                                                                | 483 ms: 1.01x faster                                                            |
| async_generators           | 406 ms                                                                | 410 ms: 1.01x slower                                                            |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                                    |

Benchmark hidden because not significant (3): async_tree_none_tg, asyncio_websockets, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250609-linux-x86_64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a | bm-20250609-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 102 ms                                                                | 96.8 ms: 1.06x faster                                                           |
| pidigits       | 188 ms                                                                | 188 ms: 1.00x slower                                                            |
| float          | 72.8 ms                                                               | 73.7 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250609-linux-x86_64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a | bm-20250609-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 22.0 ms                                                               | 23.4 ms: 1.06x slower                                                           |
| regex_effbot   | 3.07 ms                                                               | 3.29 ms: 1.07x slower                                                           |
| regex_dna      | 181 ms                                                                | 207 ms: 1.14x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                                    |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250609-linux-x86_64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a | bm-20250609-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|--------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps         | 11.2 ms                                                               | 11.0 ms: 1.01x faster                                                           |
| pickle_pure_python | 322 us                                                                | 318 us: 1.01x faster                                                            |
| json_loads         | 28.2 us                                                               | 28.1 us: 1.00x faster                                                           |
| xml_etree_generate | 85.5 ms                                                               | 85.2 ms: 1.00x faster                                                           |
| Geometric mean     | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (5): xml_etree_parse, unpickle_pure_python, tomli_loads, xml_etree_iterparse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250609-linux-x86_64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a | bm-20250609-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.90 ms                                                               | 6.90 ms: 1.00x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250609-linux-x86_64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a | bm-20250609-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text    | 21.5 ms                                                               | 21.0 ms: 1.02x faster                                                           |
| mako           | 11.3 ms                                                               | 11.2 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                    |

Benchmark hidden because not significant (2): genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20250609-linux-x86_64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a | bm-20250609-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody                      | 102 ms                                                                | 96.8 ms: 1.06x faster                                                           |
| coroutines                 | 25.8 ms                                                               | 24.7 ms: 1.04x faster                                                           |
| deepcopy_reduce            | 2.77 us                                                               | 2.66 us: 1.04x faster                                                           |
| chaos                      | 61.9 ms                                                               | 60.0 ms: 1.03x faster                                                           |
| genshi_text                | 21.5 ms                                                               | 21.0 ms: 1.02x faster                                                           |
| async_tree_io_tg           | 632 ms                                                                | 619 ms: 1.02x faster                                                            |
| connected_components       | 484 ms                                                                | 475 ms: 1.02x faster                                                            |
| hexiom                     | 6.08 ms                                                               | 5.98 ms: 1.02x faster                                                           |
| richards                   | 43.6 ms                                                               | 43.0 ms: 1.01x faster                                                           |
| scimark_sor                | 122 ms                                                                | 120 ms: 1.01x faster                                                            |
| async_tree_none            | 264 ms                                                                | 260 ms: 1.01x faster                                                            |
| json_dumps                 | 11.2 ms                                                               | 11.0 ms: 1.01x faster                                                           |
| pickle_pure_python         | 322 us                                                                | 318 us: 1.01x faster                                                            |
| coverage                   | 426 ms                                                                | 421 ms: 1.01x faster                                                            |
| async_tree_io              | 602 ms                                                                | 595 ms: 1.01x faster                                                            |
| sqlglot_v2_parse           | 1.26 ms                                                               | 1.25 ms: 1.01x faster                                                           |
| generators                 | 29.9 ms                                                               | 29.6 ms: 1.01x faster                                                           |
| sqlglot_v2_transpile       | 1.56 ms                                                               | 1.55 ms: 1.01x faster                                                           |
| mako                       | 11.3 ms                                                               | 11.2 ms: 1.01x faster                                                           |
| dulwich_log                | 59.9 ms                                                               | 59.3 ms: 1.01x faster                                                           |
| logging_format             | 6.84 us                                                               | 6.78 us: 1.01x faster                                                           |
| pathlib                    | 16.8 ms                                                               | 16.7 ms: 1.01x faster                                                           |
| pyflate                    | 433 ms                                                                | 430 ms: 1.01x faster                                                            |
| nqueens                    | 81.1 ms                                                               | 80.4 ms: 1.01x faster                                                           |
| async_tree_memoization     | 317 ms                                                                | 314 ms: 1.01x faster                                                            |
| async_tree_cpu_io_mixed    | 495 ms                                                                | 491 ms: 1.01x faster                                                            |
| logging_silent             | 475 ns                                                                | 471 ns: 1.01x faster                                                            |
| scimark_monte_carlo        | 68.6 ms                                                               | 68.1 ms: 1.01x faster                                                           |
| shortest_path              | 511 ms                                                                | 507 ms: 1.01x faster                                                            |
| async_tree_cpu_io_mixed_tg | 486 ms                                                                | 483 ms: 1.01x faster                                                            |
| crypto_pyaes               | 76.1 ms                                                               | 75.7 ms: 1.01x faster                                                           |
| sqlglot_v2_optimize        | 52.8 ms                                                               | 52.5 ms: 1.00x faster                                                           |
| json_loads                 | 28.2 us                                                               | 28.1 us: 1.00x faster                                                           |
| comprehensions             | 16.2 us                                                               | 16.1 us: 1.00x faster                                                           |
| bpe_tokeniser              | 4.54 sec                                                              | 4.52 sec: 1.00x faster                                                          |
| richards_super             | 49.8 ms                                                               | 49.6 ms: 1.00x faster                                                           |
| xml_etree_generate         | 85.5 ms                                                               | 85.2 ms: 1.00x faster                                                           |
| create_gc_cycles           | 2.59 ms                                                               | 2.58 ms: 1.00x faster                                                           |
| 2to3                       | 255 ms                                                                | 254 ms: 1.00x faster                                                            |
| python_startup_no_site     | 6.90 ms                                                               | 6.90 ms: 1.00x slower                                                           |
| meteor_contest             | 106 ms                                                                | 106 ms: 1.00x slower                                                            |
| sympy_expand               | 451 ms                                                                | 452 ms: 1.00x slower                                                            |
| sympy_integrate            | 19.0 ms                                                               | 19.0 ms: 1.00x slower                                                           |
| pidigits                   | 188 ms                                                                | 188 ms: 1.00x slower                                                            |
| sympy_str                  | 266 ms                                                                | 267 ms: 1.01x slower                                                            |
| deltablue                  | 3.51 ms                                                               | 3.54 ms: 1.01x slower                                                           |
| logging_simple             | 6.05 us                                                               | 6.10 us: 1.01x slower                                                           |
| async_generators           | 406 ms                                                                | 410 ms: 1.01x slower                                                            |
| deepcopy                   | 255 us                                                                | 258 us: 1.01x slower                                                            |
| pprint_safe_repr           | 797 ms                                                                | 806 ms: 1.01x slower                                                            |
| float                      | 72.8 ms                                                               | 73.7 ms: 1.01x slower                                                           |
| telco                      | 7.95 ms                                                               | 8.05 ms: 1.01x slower                                                           |
| spectral_norm              | 109 ms                                                                | 111 ms: 1.01x slower                                                            |
| gc_traversal               | 5.00 ms                                                               | 5.07 ms: 1.02x slower                                                           |
| typing_runtime_protocols   | 166 us                                                                | 169 us: 1.02x slower                                                            |
| deepcopy_memo              | 29.1 us                                                               | 29.6 us: 1.02x slower                                                           |
| scimark_sparse_mat_mult    | 5.04 ms                                                               | 5.15 ms: 1.02x slower                                                           |
| scimark_fft                | 373 ms                                                                | 382 ms: 1.02x slower                                                            |
| pycparser                  | 1.11 sec                                                              | 1.17 sec: 1.05x slower                                                          |
| regex_v8                   | 22.0 ms                                                               | 23.4 ms: 1.06x slower                                                           |
| regex_effbot               | 3.07 ms                                                               | 3.29 ms: 1.07x slower                                                           |
| regex_dna                  | 181 ms                                                                | 207 ms: 1.14x slower                                                            |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (30): json, html5lib, xml_etree_parse, genshi_xml, async_tree_none_tg, sympy_sum, scimark_lu, k_core, asyncio_websockets, go, fannkuch, pylint, regex_compile, sqlglot_v2_normalize, unpickle_pure_python, tomli_loads, python_startup, xml_etree_iterparse, mdp, raytrace, thrift, pprint_pformat, docutils, xml_etree_process, many_optionals, sqlite_synth, sphinx, django_template, subparsers, async_tree_memoization_tg

- Geometric mean (including insignificant results): 1.000x slower

# HPT report

- Reliability score: 97.46% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x