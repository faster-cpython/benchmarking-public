# Results vs. base

- fork: brandtbucher
- ref: jit_oz
- machine: linux-aarch64
- commit hash: 6448067
- commit date: 2025-06-28
- overall geometric mean: 1.014x slower
- HPT reliability: 99.97%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-arminc-aarch64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 308 ms                                                                  | 315 ms: 1.02x slower                                            |
| docutils       | 3.12 sec                                                                | 3.16 sec: 1.01x slower                                          |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                    |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-arminc-aarch64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|---------------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_memoization_tg | 479 ms                                                                  | 468 ms: 1.02x faster                                            |
| async_tree_none_tg        | 384 ms                                                                  | 376 ms: 1.02x faster                                            |
| coroutines                | 29.0 ms                                                                 | 29.1 ms: 1.00x slower                                           |
| Geometric mean            | (ref)                                                                   | 1.00x faster                                                    |

Benchmark hidden because not significant (8): async_tree_none, async_tree_io_tg, async_generators, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-arminc-aarch64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 83.1 ms                                                                 | 84.4 ms: 1.02x slower                                           |
| Geometric mean | (ref)                                                                   | 1.00x slower                                                    |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-arminc-aarch64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 122 ms                                                                  | 124 ms: 1.02x slower                                            |
| regex_dna      | 215 ms                                                                  | 220 ms: 1.02x slower                                            |
| Geometric mean | (ref)                                                                   | 1.02x slower                                                    |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-arminc-aarch64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| json_loads           | 32.3 us                                                                 | 33.3 us: 1.03x slower                                           |
| xml_etree_generate   | 108 ms                                                                  | 112 ms: 1.04x slower                                            |
| tomli_loads          | 2.32 sec                                                                | 2.43 sec: 1.05x slower                                          |
| xml_etree_process    | 77.6 ms                                                                 | 81.4 ms: 1.05x slower                                           |
| unpickle_pure_python | 254 us                                                                  | 267 us: 1.05x slower                                            |
| Geometric mean       | (ref)                                                                   | 1.02x slower                                                    |

Benchmark hidden because not significant (4): json_dumps, pickle_pure_python, xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-arminc-aarch64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|------------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 8.62 ms                                                                 | 8.68 ms: 1.01x slower                                           |
| Geometric mean         | (ref)                                                                   | 1.01x slower                                                    |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-arminc-aarch64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| mako           | 13.2 ms                                                                 | 14.2 ms: 1.08x slower                                           |
| Geometric mean | (ref)                                                                   | 1.02x slower                                                    |

Benchmark hidden because not significant (3): genshi_text, genshi_xml, django_template

All benchmarks:
===============

| Benchmark                 | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-arminc-aarch64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|---------------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_memoization_tg | 479 ms                                                                  | 468 ms: 1.02x faster                                            |
| async_tree_none_tg        | 384 ms                                                                  | 376 ms: 1.02x faster                                            |
| sqlglot_v2_normalize      | 130 ms                                                                  | 127 ms: 1.02x faster                                            |
| logging_simple            | 7.09 us                                                                 | 7.00 us: 1.01x faster                                           |
| coroutines                | 29.0 ms                                                                 | 29.1 ms: 1.00x slower                                           |
| subparsers                | 28.5 ms                                                                 | 28.6 ms: 1.00x slower                                           |
| python_startup_no_site    | 8.62 ms                                                                 | 8.68 ms: 1.01x slower                                           |
| docutils                  | 3.12 sec                                                                | 3.16 sec: 1.01x slower                                          |
| float                     | 83.1 ms                                                                 | 84.4 ms: 1.02x slower                                           |
| sqlglot_v2_transpile      | 1.84 ms                                                                 | 1.87 ms: 1.02x slower                                           |
| regex_compile             | 122 ms                                                                  | 124 ms: 1.02x slower                                            |
| deltablue                 | 3.87 ms                                                                 | 3.94 ms: 1.02x slower                                           |
| 2to3                      | 308 ms                                                                  | 315 ms: 1.02x slower                                            |
| mdp                       | 1.66 sec                                                                | 1.70 sec: 1.02x slower                                          |
| regex_dna                 | 215 ms                                                                  | 220 ms: 1.02x slower                                            |
| pycparser                 | 1.37 sec                                                                | 1.40 sec: 1.03x slower                                          |
| richards_super            | 50.5 ms                                                                 | 51.9 ms: 1.03x slower                                           |
| json_loads                | 32.3 us                                                                 | 33.3 us: 1.03x slower                                           |
| k_core                    | 2.84 sec                                                                | 2.93 sec: 1.03x slower                                          |
| create_gc_cycles          | 3.67 ms                                                                 | 3.78 ms: 1.03x slower                                           |
| comprehensions            | 21.8 us                                                                 | 22.5 us: 1.03x slower                                           |
| xml_etree_generate        | 108 ms                                                                  | 112 ms: 1.04x slower                                            |
| pprint_pformat            | 2.44 sec                                                                | 2.54 sec: 1.04x slower                                          |
| go                        | 155 ms                                                                  | 162 ms: 1.04x slower                                            |
| hexiom                    | 7.41 ms                                                                 | 7.77 ms: 1.05x slower                                           |
| tomli_loads               | 2.32 sec                                                                | 2.43 sec: 1.05x slower                                          |
| xml_etree_process         | 77.6 ms                                                                 | 81.4 ms: 1.05x slower                                           |
| pprint_safe_repr          | 1.17 sec                                                                | 1.23 sec: 1.05x slower                                          |
| unpickle_pure_python      | 254 us                                                                  | 267 us: 1.05x slower                                            |
| shortest_path             | 587 ms                                                                  | 618 ms: 1.05x slower                                            |
| crypto_pyaes              | 92.7 ms                                                                 | 97.7 ms: 1.05x slower                                           |
| bpe_tokeniser             | 5.42 sec                                                                | 5.74 sec: 1.06x slower                                          |
| connected_components      | 558 ms                                                                  | 593 ms: 1.06x slower                                            |
| pyflate                   | 533 ms                                                                  | 569 ms: 1.07x slower                                            |
| mako                      | 13.2 ms                                                                 | 14.2 ms: 1.08x slower                                           |
| scimark_fft               | 412 ms                                                                  | 448 ms: 1.09x slower                                            |
| fannkuch                  | 476 ms                                                                  | 527 ms: 1.11x slower                                            |
| spectral_norm             | 120 ms                                                                  | 134 ms: 1.12x slower                                            |
| Geometric mean            | (ref)                                                                   | 1.01x slower                                                    |

Benchmark hidden because not significant (55): sympy_sum, telco, deepcopy, generators, dulwich_log, json_dumps, scimark_monte_carlo, logging_format, scimark_lu, nqueens, async_tree_none, html5lib, nbody, sqlglot_v2_parse, genshi_text, sympy_str, async_tree_io_tg, gc_traversal, sympy_expand, logging_silent, genshi_xml, async_generators, sqlglot_v2_optimize, pickle_pure_python, async_tree_memoization, pidigits, xml_etree_iterparse, sphinx, djangocms, scimark_sor, async_tree_cpu_io_mixed, coverage, async_tree_cpu_io_mixed_tg, xml_etree_parse, python_startup, asyncio_websockets, json, richards, async_tree_io, raytrace, regex_v8, deepcopy_memo, regex_effbot, pathlib, chaos, django_template, sympy_integrate, sqlite_synth, thrift, deepcopy_reduce, many_optionals, typing_runtime_protocols, pylint, scimark_sparse_mat_mult, meteor_contest

- Geometric mean (including insignificant results): 1.014x slower

# HPT report

- Reliability score: 99.97% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x