# Results vs. base

- fork: faster-cpython
- ref: explicit_check_perio
- machine: linux-aarch64
- commit hash: be0ebdc
- commit date: 2025-06-20
- overall geometric mean: 1.003x slower
- HPT reliability: 96.86%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark      | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_io  | 903 ms                                                                  | 884 ms: 1.02x faster                                                              |
| Geometric mean | (ref)                                                                   | 1.00x slower                                                                      |

Benchmark hidden because not significant (10): async_tree_none, async_tree_io_tg, async_generators, async_tree_memoization, asyncio_websockets, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 119 ms                                                                  | 124 ms: 1.05x slower                                                              |
| Geometric mean | (ref)                                                                   | 1.02x slower                                                                      |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_dna      | 219 ms                                                                  | 224 ms: 1.02x slower                                                              |
| Geometric mean | (ref)                                                                   | 1.00x slower                                                                      |

Benchmark hidden because not significant (3): regex_v8, regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_process    | 81.2 ms                                                                 | 79.3 ms: 1.02x faster                                                             |
| tomli_loads          | 2.44 sec                                                                | 2.52 sec: 1.03x slower                                                            |
| unpickle_pure_python | 260 us                                                                  | 270 us: 1.04x slower                                                              |
| Geometric mean       | (ref)                                                                   | 1.00x slower                                                                      |

Benchmark hidden because not significant (6): xml_etree_generate, json_dumps, pickle_pure_python, xml_etree_parse, xml_etree_iterparse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup | 15.3 ms                                                                 | 15.1 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                                   | 1.01x faster                                                                      |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako           | 13.9 ms                                                                 | 14.3 ms: 1.03x slower                                                             |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                                      |

Benchmark hidden because not significant (3): django_template, genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|-------------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 36.9 ms                                                                 | 34.9 ms: 1.06x faster                                                             |
| create_gc_cycles        | 3.92 ms                                                                 | 3.81 ms: 1.03x faster                                                             |
| xml_etree_process       | 81.2 ms                                                                 | 79.3 ms: 1.02x faster                                                             |
| async_tree_io           | 903 ms                                                                  | 884 ms: 1.02x faster                                                              |
| python_startup          | 15.3 ms                                                                 | 15.1 ms: 1.01x faster                                                             |
| dulwich_log             | 51.9 ms                                                                 | 52.3 ms: 1.01x slower                                                             |
| json                    | 5.68 ms                                                                 | 5.73 ms: 1.01x slower                                                             |
| bpe_tokeniser           | 5.46 sec                                                                | 5.53 sec: 1.01x slower                                                            |
| scimark_sparse_mat_mult | 6.86 ms                                                                 | 6.94 ms: 1.01x slower                                                             |
| sqlite_synth            | 3.80 us                                                                 | 3.85 us: 1.01x slower                                                             |
| logging_format          | 8.22 us                                                                 | 8.33 us: 1.01x slower                                                             |
| subparsers              | 27.8 ms                                                                 | 28.3 ms: 1.02x slower                                                             |
| regex_dna               | 219 ms                                                                  | 224 ms: 1.02x slower                                                              |
| deepcopy_memo           | 37.2 us                                                                 | 38.3 us: 1.03x slower                                                             |
| mako                    | 13.9 ms                                                                 | 14.3 ms: 1.03x slower                                                             |
| tomli_loads             | 2.44 sec                                                                | 2.52 sec: 1.03x slower                                                            |
| unpickle_pure_python    | 260 us                                                                  | 270 us: 1.04x slower                                                              |
| fannkuch                | 465 ms                                                                  | 486 ms: 1.05x slower                                                              |
| sympy_expand            | 464 ms                                                                  | 485 ms: 1.05x slower                                                              |
| nbody                   | 119 ms                                                                  | 124 ms: 1.05x slower                                                              |
| sympy_str               | 262 ms                                                                  | 275 ms: 1.05x slower                                                              |
| Geometric mean          | (ref)                                                                   | 1.01x slower                                                                      |

Benchmark hidden because not significant (72): regex_v8, logging_silent, coverage, raytrace, xml_etree_generate, go, pyflate, typing_runtime_protocols, spectral_norm, async_tree_none, json_dumps, mdp, pprint_pformat, scimark_monte_carlo, pycparser, sqlglot_v2_transpile, nqueens, docutils, pickle_pure_python, django_template, deltablue, xml_etree_parse, float, xml_etree_iterparse, deepcopy, async_tree_io_tg, async_generators, sympy_integrate, python_startup_no_site, async_tree_memoization, genshi_text, pylint, pprint_safe_repr, genshi_xml, asyncio_websockets, async_tree_none_tg, deepcopy_reduce, djangocms, scimark_sor, sympy_sum, async_tree_cpu_io_mixed_tg, comprehensions, richards, crypto_pyaes, pidigits, shortest_path, gc_traversal, connected_components, 2to3, html5lib, many_optionals, k_core, logging_simple, async_tree_memoization_tg, regex_compile, sphinx, async_tree_cpu_io_mixed, json_loads, telco, coroutines, sqlglot_v2_optimize, regex_effbot, richards_super, pathlib, chaos, scimark_lu, scimark_fft, hexiom, meteor_contest, thrift, sqlglot_v2_parse, sqlglot_v2_normalize

- Geometric mean (including insignificant results): 1.003x slower

# HPT report

- Reliability score: 96.86% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x