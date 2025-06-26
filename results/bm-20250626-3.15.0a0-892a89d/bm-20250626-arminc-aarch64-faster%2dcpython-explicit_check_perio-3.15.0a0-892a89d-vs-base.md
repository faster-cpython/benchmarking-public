# Results vs. base

- fork: faster-cpython
- ref: explicit_check_perio
- machine: linux-aarch64
- commit hash: 892a89d
- commit date: 2025-06-26
- overall geometric mean: 1.003x slower
- HPT reliability: 99.81%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250626-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 299 ms                                                                  | 306 ms: 1.02x slower                                                              |
| html5lib       | 61.7 ms                                                                 | 62.9 ms: 1.02x slower                                                             |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                                      |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250626-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|---------------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 461 ms                                                                  | 467 ms: 1.01x slower                                                              |
| async_tree_none           | 389 ms                                                                  | 394 ms: 1.01x slower                                                              |
| async_tree_io_tg          | 895 ms                                                                  | 908 ms: 1.01x slower                                                              |
| async_tree_io             | 884 ms                                                                  | 901 ms: 1.02x slower                                                              |
| async_tree_none_tg        | 369 ms                                                                  | 380 ms: 1.03x slower                                                              |
| Geometric mean            | (ref)                                                                   | 1.01x slower                                                                      |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed_tg, coroutines, asyncio_websockets, async_tree_memoization, async_tree_cpu_io_mixed, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250626-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 85.9 ms                                                                 | 87.3 ms: 1.02x slower                                                             |
| Geometric mean | (ref)                                                                   | 1.00x faster                                                                      |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250626-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_dna      | 224 ms                                                                  | 220 ms: 1.02x faster                                                              |
| regex_v8       | 26.6 ms                                                                 | 27.1 ms: 1.02x slower                                                             |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                                      |

Benchmark hidden because not significant (2): regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250626-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|--------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_loads         | 33.6 us                                                                 | 32.4 us: 1.04x faster                                                             |
| json_dumps         | 13.8 ms                                                                 | 13.7 ms: 1.01x faster                                                             |
| xml_etree_generate | 112 ms                                                                  | 111 ms: 1.01x faster                                                              |
| Geometric mean     | (ref)                                                                   | 1.01x faster                                                                      |

Benchmark hidden because not significant (6): pickle_pure_python, xml_etree_parse, xml_etree_process, xml_etree_iterparse, tomli_loads, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250626-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako           | 13.7 ms                                                                 | 14.3 ms: 1.04x slower                                                             |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                                      |

Benchmark hidden because not significant (3): genshi_text, django_template, genshi_xml

All benchmarks:
===============

| Benchmark                 | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250626-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|---------------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| create_gc_cycles          | 3.94 ms                                                                 | 3.77 ms: 1.04x faster                                                             |
| json_loads                | 33.6 us                                                                 | 32.4 us: 1.04x faster                                                             |
| sqlglot_v2_transpile      | 1.82 ms                                                                 | 1.77 ms: 1.03x faster                                                             |
| logging_format            | 8.54 us                                                                 | 8.38 us: 1.02x faster                                                             |
| regex_dna                 | 224 ms                                                                  | 220 ms: 1.02x faster                                                              |
| shortest_path             | 583 ms                                                                  | 574 ms: 1.02x faster                                                              |
| json_dumps                | 13.8 ms                                                                 | 13.7 ms: 1.01x faster                                                             |
| xml_etree_generate        | 112 ms                                                                  | 111 ms: 1.01x faster                                                              |
| connected_components      | 557 ms                                                                  | 552 ms: 1.01x faster                                                              |
| async_tree_memoization_tg | 461 ms                                                                  | 467 ms: 1.01x slower                                                              |
| async_tree_none           | 389 ms                                                                  | 394 ms: 1.01x slower                                                              |
| async_tree_io_tg          | 895 ms                                                                  | 908 ms: 1.01x slower                                                              |
| float                     | 85.9 ms                                                                 | 87.3 ms: 1.02x slower                                                             |
| pprint_pformat            | 2.05 sec                                                                | 2.08 sec: 1.02x slower                                                            |
| regex_v8                  | 26.6 ms                                                                 | 27.1 ms: 1.02x slower                                                             |
| async_tree_io             | 884 ms                                                                  | 901 ms: 1.02x slower                                                              |
| html5lib                  | 61.7 ms                                                                 | 62.9 ms: 1.02x slower                                                             |
| pprint_safe_repr          | 1.01 sec                                                                | 1.03 sec: 1.02x slower                                                            |
| 2to3                      | 299 ms                                                                  | 306 ms: 1.02x slower                                                              |
| k_core                    | 2.77 sec                                                                | 2.84 sec: 1.03x slower                                                            |
| async_tree_none_tg        | 369 ms                                                                  | 380 ms: 1.03x slower                                                              |
| chaos                     | 67.3 ms                                                                 | 69.3 ms: 1.03x slower                                                             |
| scimark_monte_carlo       | 79.2 ms                                                                 | 82.2 ms: 1.04x slower                                                             |
| mako                      | 13.7 ms                                                                 | 14.3 ms: 1.04x slower                                                             |
| bpe_tokeniser             | 5.51 sec                                                                | 5.78 sec: 1.05x slower                                                            |
| sympy_str                 | 263 ms                                                                  | 277 ms: 1.05x slower                                                              |
| richards_super            | 58.7 ms                                                                 | 62.1 ms: 1.06x slower                                                             |
| richards                  | 52.2 ms                                                                 | 56.3 ms: 1.08x slower                                                             |
| Geometric mean            | (ref)                                                                   | 1.01x slower                                                                      |

Benchmark hidden because not significant (65): pickle_pure_python, sympy_sum, sqlite_synth, nbody, json, go, sympy_expand, genshi_text, comprehensions, sqlglot_v2_parse, xml_etree_parse, sphinx, scimark_sparse_mat_mult, fannkuch, dulwich_log, nqueens, sqlglot_v2_optimize, pyflate, raytrace, xml_etree_process, async_tree_cpu_io_mixed_tg, logging_simple, xml_etree_iterparse, mdp, coroutines, pidigits, djangocms, tomli_loads, subparsers, deepcopy_reduce, gc_traversal, many_optionals, unpickle_pure_python, asyncio_websockets, pylint, python_startup, python_startup_no_site, regex_compile, pycparser, async_tree_memoization, hexiom, coverage, docutils, sqlglot_v2_normalize, telco, django_template, async_tree_cpu_io_mixed, meteor_contest, async_generators, spectral_norm, deltablue, genshi_xml, deepcopy_memo, generators, crypto_pyaes, regex_effbot, scimark_sor, logging_silent, typing_runtime_protocols, scimark_lu, scimark_fft, sympy_integrate, deepcopy, pathlib, thrift

- Geometric mean (including insignificant results): 1.003x slower

# HPT report

- Reliability score: 99.81% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x