# Results vs. base

- fork: faster-cpython
- ref: make_decref_a_call
- machine: linux-aarch64
- commit hash: bdf907f
- commit date: 2025-05-08
- overall geometric mean: 1.058x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250508-arminc-aarch64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 | bm-20250508-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 304 ms                                                                  | 315 ms: 1.04x slower                                                            |
| html5lib       | 62.4 ms                                                                 | 63.6 ms: 1.02x slower                                                           |
| sphinx         | 1.15 sec                                                                | 1.19 sec: 1.03x slower                                                          |
| Geometric mean | (ref)                                                                   | 1.02x slower                                                                    |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20250508-arminc-aarch64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 | bm-20250508-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|------------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg | 924 ms                                                                  | 935 ms: 1.01x slower                                                            |
| async_tree_none  | 393 ms                                                                  | 401 ms: 1.02x slower                                                            |
| async_tree_io    | 879 ms                                                                  | 899 ms: 1.02x slower                                                            |
| async_generators | 452 ms                                                                  | 475 ms: 1.05x slower                                                            |
| Geometric mean   | (ref)                                                                   | 1.01x slower                                                                    |

Benchmark hidden because not significant (7): coroutines, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_memoization, async_tree_none_tg, asyncio_websockets, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250508-arminc-aarch64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 | bm-20250508-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 86.4 ms                                                                 | 88.6 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                                    |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250508-arminc-aarch64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 | bm-20250508-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 230 ms                                                                  | 238 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                                   | 1.02x slower                                                                    |

Benchmark hidden because not significant (3): regex_v8, regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250508-arminc-aarch64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 | bm-20250508-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|---------------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads         | 2.47 sec                                                                | 2.55 sec: 1.03x slower                                                          |
| xml_etree_iterparse | 144 ms                                                                  | 150 ms: 1.04x slower                                                            |
| xml_etree_process   | 80.0 ms                                                                 | 84.1 ms: 1.05x slower                                                           |
| pickle_pure_python  | 379 us                                                                  | 402 us: 1.06x slower                                                            |
| xml_etree_generate  | 112 ms                                                                  | 120 ms: 1.06x slower                                                            |
| xml_etree_parse     | 178 ms                                                                  | 191 ms: 1.08x slower                                                            |
| json_dumps          | 14.4 ms                                                                 | 15.7 ms: 1.10x slower                                                           |
| Geometric mean      | (ref)                                                                   | 1.05x slower                                                                    |

Benchmark hidden because not significant (2): json_loads, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250508-arminc-aarch64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 | bm-20250508-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|-----------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 13.9 ms                                                                 | 14.1 ms: 1.02x slower                                                           |
| django_template | 39.6 ms                                                                 | 42.0 ms: 1.06x slower                                                           |
| genshi_text     | 26.6 ms                                                                 | 28.9 ms: 1.09x slower                                                           |
| Geometric mean  | (ref)                                                                   | 1.05x slower                                                                    |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark            | bm-20250508-arminc-aarch64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 | bm-20250508-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift               | 192 ms                                                                  | 987 us: 195.00x faster                                                          |
| coverage             | 545 ms                                                                  | 110 ms: 4.97x faster                                                            |
| create_gc_cycles     | 3.89 ms                                                                 | 3.71 ms: 1.05x faster                                                           |
| async_tree_io_tg     | 924 ms                                                                  | 935 ms: 1.01x slower                                                            |
| richards_super       | 57.2 ms                                                                 | 58.0 ms: 1.01x slower                                                           |
| hexiom               | 7.04 ms                                                                 | 7.17 ms: 1.02x slower                                                           |
| mako                 | 13.9 ms                                                                 | 14.1 ms: 1.02x slower                                                           |
| html5lib             | 62.4 ms                                                                 | 63.6 ms: 1.02x slower                                                           |
| async_tree_none      | 393 ms                                                                  | 401 ms: 1.02x slower                                                            |
| pycparser            | 1.27 sec                                                                | 1.30 sec: 1.02x slower                                                          |
| async_tree_io        | 879 ms                                                                  | 899 ms: 1.02x slower                                                            |
| subparsers           | 27.9 ms                                                                 | 28.5 ms: 1.02x slower                                                           |
| many_optionals       | 857 us                                                                  | 877 us: 1.02x slower                                                            |
| float                | 86.4 ms                                                                 | 88.6 ms: 1.03x slower                                                           |
| sphinx               | 1.15 sec                                                                | 1.19 sec: 1.03x slower                                                          |
| deltablue            | 3.78 ms                                                                 | 3.89 ms: 1.03x slower                                                           |
| tomli_loads          | 2.47 sec                                                                | 2.55 sec: 1.03x slower                                                          |
| regex_dna            | 230 ms                                                                  | 238 ms: 1.03x slower                                                            |
| 2to3                 | 304 ms                                                                  | 315 ms: 1.04x slower                                                            |
| connected_components | 552 ms                                                                  | 574 ms: 1.04x slower                                                            |
| meteor_contest       | 113 ms                                                                  | 118 ms: 1.04x slower                                                            |
| xml_etree_iterparse  | 144 ms                                                                  | 150 ms: 1.04x slower                                                            |
| bpe_tokeniser        | 5.46 sec                                                                | 5.72 sec: 1.05x slower                                                          |
| async_generators     | 452 ms                                                                  | 475 ms: 1.05x slower                                                            |
| deepcopy             | 330 us                                                                  | 346 us: 1.05x slower                                                            |
| logging_simple       | 6.92 us                                                                 | 7.27 us: 1.05x slower                                                           |
| telco                | 9.63 ms                                                                 | 10.1 ms: 1.05x slower                                                           |
| xml_etree_process    | 80.0 ms                                                                 | 84.1 ms: 1.05x slower                                                           |
| shortest_path        | 568 ms                                                                  | 598 ms: 1.05x slower                                                            |
| deepcopy_memo        | 37.4 us                                                                 | 39.4 us: 1.05x slower                                                           |
| pyflate              | 546 ms                                                                  | 575 ms: 1.05x slower                                                            |
| pprint_safe_repr     | 898 ms                                                                  | 946 ms: 1.05x slower                                                            |
| json                 | 6.01 ms                                                                 | 6.34 ms: 1.06x slower                                                           |
| nqueens              | 101 ms                                                                  | 107 ms: 1.06x slower                                                            |
| mdp                  | 1.61 sec                                                                | 1.71 sec: 1.06x slower                                                          |
| pickle_pure_python   | 379 us                                                                  | 402 us: 1.06x slower                                                            |
| django_template      | 39.6 ms                                                                 | 42.0 ms: 1.06x slower                                                           |
| xml_etree_generate   | 112 ms                                                                  | 120 ms: 1.06x slower                                                            |
| deepcopy_reduce      | 3.47 us                                                                 | 3.70 us: 1.07x slower                                                           |
| logging_format       | 7.65 us                                                                 | 8.20 us: 1.07x slower                                                           |
| scimark_lu           | 146 ms                                                                  | 157 ms: 1.07x slower                                                            |
| pprint_pformat       | 1.82 sec                                                                | 1.96 sec: 1.07x slower                                                          |
| xml_etree_parse      | 178 ms                                                                  | 191 ms: 1.08x slower                                                            |
| fannkuch             | 471 ms                                                                  | 509 ms: 1.08x slower                                                            |
| sqlite_synth         | 3.76 us                                                                 | 4.07 us: 1.08x slower                                                           |
| sympy_str            | 260 ms                                                                  | 283 ms: 1.09x slower                                                            |
| genshi_text          | 26.6 ms                                                                 | 28.9 ms: 1.09x slower                                                           |
| comprehensions       | 20.9 us                                                                 | 22.9 us: 1.09x slower                                                           |
| json_dumps           | 14.4 ms                                                                 | 15.7 ms: 1.10x slower                                                           |
| Geometric mean       | (ref)                                                                   | 1.05x faster                                                                    |

Benchmark hidden because not significant (45): bench_mp_pool, sqlglot_v2_transpile, pylint, coroutines, logging_silent, pidigits, spectral_norm, json_loads, chaos, async_tree_cpu_io_mixed_tg, bench_thread_pool, scimark_sparse_mat_mult, pathlib, python_startup, gc_traversal, async_tree_memoization_tg, python_startup_no_site, async_tree_memoization, docutils, go, async_tree_none_tg, regex_v8, scimark_sor, asyncio_websockets, k_core, dulwich_log, regex_effbot, scimark_monte_carlo, async_tree_cpu_io_mixed, generators, raytrace, sympy_integrate, unpickle_pure_python, sqlglot_v2_optimize, sqlglot_v2_parse, nbody, regex_compile, typing_runtime_protocols, scimark_fft, sympy_sum, sympy_expand, richards, genshi_xml, crypto_pyaes, sqlglot_v2_normalize
Ignored benchmarks (1) of results/bm-20250508-3.15.0a0-bdf907f/bm-20250508-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f.json: djangocms

- Geometric mean (including insignificant results): 1.058x faster

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 0.99x