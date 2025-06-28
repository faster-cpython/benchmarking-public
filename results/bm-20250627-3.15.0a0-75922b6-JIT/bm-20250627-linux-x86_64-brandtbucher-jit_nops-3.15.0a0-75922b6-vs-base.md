# Results vs. base

- fork: brandtbucher
- ref: jit_nops
- machine: linux-x86_64
- commit hash: 75922b6
- commit date: 2025-06-27
- overall geometric mean: 1.004x slower
- HPT reliability: 98.50%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 258 ms                                                                | 259 ms: 1.00x slower                                            |
| docutils       | 2.62 sec                                                              | 2.63 sec: 1.01x slower                                          |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                    |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_memoization_tg  | 314 ms                                                                | 310 ms: 1.01x faster                                            |
| async_generators           | 432 ms                                                                | 427 ms: 1.01x faster                                            |
| async_tree_none_tg         | 251 ms                                                                | 248 ms: 1.01x faster                                            |
| async_tree_cpu_io_mixed_tg | 494 ms                                                                | 489 ms: 1.01x faster                                            |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                    |

Benchmark hidden because not significant (7): async_tree_io_tg, async_tree_io, asyncio_websockets, async_tree_cpu_io_mixed, coroutines, async_tree_memoization, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 65.3 ms                                                               | 65.7 ms: 1.01x slower                                           |
| nbody          | 93.4 ms                                                               | 98.8 ms: 1.06x slower                                           |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 126 ms                                                                | 127 ms: 1.01x slower                                            |
| regex_effbot   | 3.18 ms                                                               | 3.25 ms: 1.02x slower                                           |
| regex_dna      | 202 ms                                                                | 213 ms: 1.06x slower                                            |
| regex_v8       | 21.9 ms                                                               | 23.7 ms: 1.08x slower                                           |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark         | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|-------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| xml_etree_process | 55.6 ms                                                               | 55.3 ms: 1.01x faster                                           |
| tomli_loads       | 1.81 sec                                                              | 1.82 sec: 1.01x slower                                          |
| Geometric mean    | (ref)                                                                 | 1.00x slower                                                    |

Benchmark hidden because not significant (7): json_dumps, xml_etree_iterparse, json_loads, xml_etree_generate, xml_etree_parse, unpickle_pure_python, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 12.2 ms                                                               | 12.2 ms: 1.01x slower                                           |
| python_startup_no_site | 6.94 ms                                                               | 6.98 ms: 1.01x slower                                           |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| django_template | 32.5 ms                                                               | 32.1 ms: 1.01x faster                                           |
| genshi_text     | 21.4 ms                                                               | 21.6 ms: 1.01x slower                                           |
| genshi_xml      | 50.1 ms                                                               | 50.7 ms: 1.01x slower                                           |
| mako            | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                           |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| meteor_contest             | 107 ms                                                                | 105 ms: 1.02x faster                                            |
| pyflate                    | 418 ms                                                                | 410 ms: 1.02x faster                                            |
| crypto_pyaes               | 75.5 ms                                                               | 74.5 ms: 1.01x faster                                           |
| django_template            | 32.5 ms                                                               | 32.1 ms: 1.01x faster                                           |
| async_tree_memoization_tg  | 314 ms                                                                | 310 ms: 1.01x faster                                            |
| async_generators           | 432 ms                                                                | 427 ms: 1.01x faster                                            |
| async_tree_none_tg         | 251 ms                                                                | 248 ms: 1.01x faster                                            |
| comprehensions             | 16.6 us                                                               | 16.4 us: 1.01x faster                                           |
| sqlglot_v2_normalize       | 107 ms                                                                | 106 ms: 1.01x faster                                            |
| fannkuch                   | 400 ms                                                                | 397 ms: 1.01x faster                                            |
| async_tree_cpu_io_mixed_tg | 494 ms                                                                | 489 ms: 1.01x faster                                            |
| hexiom                     | 6.24 ms                                                               | 6.19 ms: 1.01x faster                                           |
| xml_etree_process          | 55.6 ms                                                               | 55.3 ms: 1.01x faster                                           |
| deepcopy_memo              | 29.5 us                                                               | 29.4 us: 1.01x faster                                           |
| sqlglot_v2_parse           | 1.24 ms                                                               | 1.23 ms: 1.00x faster                                           |
| sqlglot_v2_optimize        | 52.7 ms                                                               | 52.8 ms: 1.00x slower                                           |
| sympy_integrate            | 19.2 ms                                                               | 19.3 ms: 1.00x slower                                           |
| go                         | 115 ms                                                                | 115 ms: 1.00x slower                                            |
| 2to3                       | 258 ms                                                                | 259 ms: 1.00x slower                                            |
| docutils                   | 2.62 sec                                                              | 2.63 sec: 1.01x slower                                          |
| python_startup             | 12.2 ms                                                               | 12.2 ms: 1.01x slower                                           |
| connected_components       | 456 ms                                                                | 458 ms: 1.01x slower                                            |
| python_startup_no_site     | 6.94 ms                                                               | 6.98 ms: 1.01x slower                                           |
| shortest_path              | 492 ms                                                                | 495 ms: 1.01x slower                                            |
| regex_compile              | 126 ms                                                                | 127 ms: 1.01x slower                                            |
| tomli_loads                | 1.81 sec                                                              | 1.82 sec: 1.01x slower                                          |
| float                      | 65.3 ms                                                               | 65.7 ms: 1.01x slower                                           |
| raytrace                   | 271 ms                                                                | 273 ms: 1.01x slower                                            |
| thrift                     | 774 us                                                                | 779 us: 1.01x slower                                            |
| telco                      | 7.65 ms                                                               | 7.70 ms: 1.01x slower                                           |
| create_gc_cycles           | 2.59 ms                                                               | 2.61 ms: 1.01x slower                                           |
| subparsers                 | 23.7 ms                                                               | 23.8 ms: 1.01x slower                                           |
| sympy_expand               | 466 ms                                                                | 469 ms: 1.01x slower                                            |
| deepcopy_reduce            | 2.68 us                                                               | 2.70 us: 1.01x slower                                           |
| scimark_fft                | 311 ms                                                                | 313 ms: 1.01x slower                                            |
| genshi_text                | 21.4 ms                                                               | 21.6 ms: 1.01x slower                                           |
| scimark_monte_carlo        | 65.2 ms                                                               | 65.9 ms: 1.01x slower                                           |
| logging_silent             | 101 ns                                                                | 102 ns: 1.01x slower                                            |
| genshi_xml                 | 50.1 ms                                                               | 50.7 ms: 1.01x slower                                           |
| gc_traversal               | 4.96 ms                                                               | 5.02 ms: 1.01x slower                                           |
| json                       | 5.17 ms                                                               | 5.24 ms: 1.01x slower                                           |
| mako                       | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                           |
| chaos                      | 60.1 ms                                                               | 61.3 ms: 1.02x slower                                           |
| logging_simple             | 5.61 us                                                               | 5.73 us: 1.02x slower                                           |
| regex_effbot               | 3.18 ms                                                               | 3.25 ms: 1.02x slower                                           |
| logging_format             | 6.24 us                                                               | 6.43 us: 1.03x slower                                           |
| regex_dna                  | 202 ms                                                                | 213 ms: 1.06x slower                                            |
| nbody                      | 93.4 ms                                                               | 98.8 ms: 1.06x slower                                           |
| regex_v8                   | 21.9 ms                                                               | 23.7 ms: 1.08x slower                                           |
| Geometric mean             | (ref)                                                                 | 1.00x slower                                                    |

Benchmark hidden because not significant (44): djangocms, pprint_pformat, async_tree_io_tg, typing_runtime_protocols, async_tree_io, json_dumps, spectral_norm, sympy_sum, k_core, deepcopy, deltablue, scimark_sor, dulwich_log, nqueens, coverage, asyncio_websockets, richards_super, pidigits, async_tree_cpu_io_mixed, sqlglot_v2_transpile, pycparser, many_optionals, coroutines, scimark_lu, sqlite_synth, richards, xml_etree_iterparse, sympy_str, bpe_tokeniser, json_loads, pathlib, xml_etree_generate, html5lib, async_tree_memoization, xml_etree_parse, unpickle_pure_python, mdp, generators, scimark_sparse_mat_mult, pickle_pure_python, sphinx, async_tree_none, pylint, pprint_safe_repr

- Geometric mean (including insignificant results): 1.004x slower

# HPT report

- Reliability score: 98.50% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x