# Results vs. base

- fork: faster-cpython
- ref: explicit_check_perio
- machine: linux-aarch64
- commit hash: 494c825
- commit date: 2025-06-20
- overall geometric mean: 1.005x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 297 ms                                                                  | 301 ms: 1.01x slower                                                              |
| Geometric mean | (ref)                                                                   | 1.00x slower                                                                      |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|---------------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_none_tg        | 375 ms                                                                  | 380 ms: 1.01x slower                                                              |
| async_tree_cpu_io_mixed   | 654 ms                                                                  | 667 ms: 1.02x slower                                                              |
| async_tree_memoization_tg | 460 ms                                                                  | 469 ms: 1.02x slower                                                              |
| async_tree_memoization    | 463 ms                                                                  | 472 ms: 1.02x slower                                                              |
| async_tree_io_tg          | 906 ms                                                                  | 925 ms: 1.02x slower                                                              |
| async_tree_none           | 389 ms                                                                  | 398 ms: 1.02x slower                                                              |
| Geometric mean            | (ref)                                                                   | 1.01x slower                                                                      |

Benchmark hidden because not significant (5): async_tree_io, asyncio_websockets, async_generators, coroutines, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 86.1 ms                                                                 | 87.2 ms: 1.01x slower                                                             |
| nbody          | 120 ms                                                                  | 129 ms: 1.08x slower                                                              |
| Geometric mean | (ref)                                                                   | 1.04x slower                                                                      |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

Benchmark hidden because not significant (4): regex_effbot, regex_dna, regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|--------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| tomli_loads        | 2.45 sec                                                                | 2.47 sec: 1.01x slower                                                            |
| xml_etree_process  | 79.7 ms                                                                 | 81.1 ms: 1.02x slower                                                             |
| json_dumps         | 13.5 ms                                                                 | 13.8 ms: 1.02x slower                                                             |
| xml_etree_generate | 111 ms                                                                  | 116 ms: 1.04x slower                                                              |
| Geometric mean     | (ref)                                                                   | 1.02x slower                                                                      |

Benchmark hidden because not significant (5): xml_etree_parse, xml_etree_iterparse, json_loads, unpickle_pure_python, pickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako           | 14.0 ms                                                                 | 14.4 ms: 1.03x slower                                                             |
| genshi_text    | 26.6 ms                                                                 | 27.9 ms: 1.05x slower                                                             |
| Geometric mean | (ref)                                                                   | 1.03x slower                                                                      |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                 | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|---------------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators                | 37.3 ms                                                                 | 35.1 ms: 1.06x faster                                                             |
| gc_traversal              | 6.97 ms                                                                 | 6.72 ms: 1.04x faster                                                             |
| k_core                    | 2.86 sec                                                                | 2.78 sec: 1.03x faster                                                            |
| shortest_path             | 587 ms                                                                  | 573 ms: 1.02x faster                                                              |
| connected_components      | 566 ms                                                                  | 555 ms: 1.02x faster                                                              |
| sqlite_synth              | 3.80 us                                                                 | 3.77 us: 1.01x faster                                                             |
| bpe_tokeniser             | 5.53 sec                                                                | 5.57 sec: 1.01x slower                                                            |
| tomli_loads               | 2.45 sec                                                                | 2.47 sec: 1.01x slower                                                            |
| 2to3                      | 297 ms                                                                  | 301 ms: 1.01x slower                                                              |
| sqlglot_v2_transpile      | 1.77 ms                                                                 | 1.79 ms: 1.01x slower                                                             |
| float                     | 86.1 ms                                                                 | 87.2 ms: 1.01x slower                                                             |
| async_tree_none_tg        | 375 ms                                                                  | 380 ms: 1.01x slower                                                              |
| pprint_pformat            | 2.08 sec                                                                | 2.11 sec: 1.01x slower                                                            |
| scimark_sparse_mat_mult   | 6.85 ms                                                                 | 6.95 ms: 1.02x slower                                                             |
| pprint_safe_repr          | 1.01 sec                                                                | 1.03 sec: 1.02x slower                                                            |
| xml_etree_process         | 79.7 ms                                                                 | 81.1 ms: 1.02x slower                                                             |
| async_tree_cpu_io_mixed   | 654 ms                                                                  | 667 ms: 1.02x slower                                                              |
| async_tree_memoization_tg | 460 ms                                                                  | 469 ms: 1.02x slower                                                              |
| async_tree_memoization    | 463 ms                                                                  | 472 ms: 1.02x slower                                                              |
| async_tree_io_tg          | 906 ms                                                                  | 925 ms: 1.02x slower                                                              |
| async_tree_none           | 389 ms                                                                  | 398 ms: 1.02x slower                                                              |
| json_dumps                | 13.5 ms                                                                 | 13.8 ms: 1.02x slower                                                             |
| logging_silent            | 627 ns                                                                  | 643 ns: 1.02x slower                                                              |
| deltablue                 | 3.96 ms                                                                 | 4.07 ms: 1.03x slower                                                             |
| logging_format            | 8.30 us                                                                 | 8.57 us: 1.03x slower                                                             |
| spectral_norm             | 118 ms                                                                  | 122 ms: 1.03x slower                                                              |
| deepcopy_reduce           | 3.58 us                                                                 | 3.70 us: 1.03x slower                                                             |
| mako                      | 14.0 ms                                                                 | 14.4 ms: 1.03x slower                                                             |
| xml_etree_generate        | 111 ms                                                                  | 116 ms: 1.04x slower                                                              |
| deepcopy_memo             | 38.2 us                                                                 | 40.0 us: 1.05x slower                                                             |
| logging_simple            | 7.56 us                                                                 | 7.93 us: 1.05x slower                                                             |
| meteor_contest            | 109 ms                                                                  | 114 ms: 1.05x slower                                                              |
| deepcopy                  | 325 us                                                                  | 341 us: 1.05x slower                                                              |
| genshi_text               | 26.6 ms                                                                 | 27.9 ms: 1.05x slower                                                             |
| thrift                    | 943 us                                                                  | 1.01 ms: 1.07x slower                                                             |
| nbody                     | 120 ms                                                                  | 129 ms: 1.08x slower                                                              |
| Geometric mean            | (ref)                                                                   | 1.01x slower                                                                      |

Benchmark hidden because not significant (57): scimark_lu, subparsers, richards, sympy_str, hexiom, html5lib, json, sympy_sum, scimark_monte_carlo, python_startup, mdp, async_tree_io, asyncio_websockets, crypto_pyaes, typing_runtime_protocols, create_gc_cycles, djangocms, coverage, xml_etree_parse, xml_etree_iterparse, regex_effbot, regex_dna, json_loads, comprehensions, python_startup_no_site, scimark_sor, async_generators, unpickle_pure_python, sphinx, pylint, telco, sympy_expand, pyflate, go, docutils, regex_compile, richards_super, sqlglot_v2_normalize, sqlglot_v2_optimize, coroutines, fannkuch, pycparser, async_tree_cpu_io_mixed_tg, dulwich_log, sympy_integrate, nqueens, pidigits, sqlglot_v2_parse, django_template, chaos, scimark_fft, pathlib, genshi_xml, raytrace, many_optionals, pickle_pure_python, regex_v8

- Geometric mean (including insignificant results): 1.005x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x