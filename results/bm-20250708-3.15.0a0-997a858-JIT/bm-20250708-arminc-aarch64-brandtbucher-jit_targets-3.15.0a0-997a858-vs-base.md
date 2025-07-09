# Results vs. base

- fork: brandtbucher
- ref: jit_targets
- machine: linux-aarch64
- commit hash: 997a858
- commit date: 2025-07-08
- overall geometric mean: 1.004x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250707-arminc-aarch64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 309 ms                                                                  | 311 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                         |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20250707-arminc-aarch64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|------------------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization | 486 ms                                                                  | 480 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                                   | 1.00x faster                                                         |

Benchmark hidden because not significant (10): async_tree_memoization_tg, async_tree_io, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_none_tg, coroutines, async_tree_none, async_tree_cpu_io_mixed, asyncio_websockets, async_generators

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): pidigits, float, nbody

Benchmarks with tag 'regex':
============================

Benchmark hidden because not significant (4): regex_effbot, regex_dna, regex_v8, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250707-arminc-aarch64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|---------------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_parse     | 177 ms                                                                  | 179 ms: 1.01x slower                                                 |
| xml_etree_iterparse | 144 ms                                                                  | 146 ms: 1.01x slower                                                 |
| json_dumps          | 13.3 ms                                                                 | 13.5 ms: 1.01x slower                                                |
| pickle_pure_python  | 383 us                                                                  | 400 us: 1.04x slower                                                 |
| Geometric mean      | (ref)                                                                   | 1.01x slower                                                         |

Benchmark hidden because not significant (5): xml_etree_generate, json_loads, xml_etree_process, tomli_loads, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250707-arminc-aarch64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako           | 13.1 ms                                                                 | 13.0 ms: 1.01x faster                                                |
| genshi_xml     | 62.3 ms                                                                 | 63.3 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                                   | 1.02x slower                                                         |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark              | bm-20250707-arminc-aarch64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|------------------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization | 486 ms                                                                  | 480 ms: 1.01x faster                                                 |
| mako                   | 13.1 ms                                                                 | 13.0 ms: 1.01x faster                                                |
| logging_format         | 7.56 us                                                                 | 7.60 us: 1.01x slower                                                |
| 2to3                   | 309 ms                                                                  | 311 ms: 1.01x slower                                                 |
| sympy_sum              | 146 ms                                                                  | 147 ms: 1.01x slower                                                 |
| connected_components   | 564 ms                                                                  | 569 ms: 1.01x slower                                                 |
| richards               | 43.7 ms                                                                 | 44.1 ms: 1.01x slower                                                |
| xml_etree_parse        | 177 ms                                                                  | 179 ms: 1.01x slower                                                 |
| sqlite_synth           | 3.66 us                                                                 | 3.70 us: 1.01x slower                                                |
| xml_etree_iterparse    | 144 ms                                                                  | 146 ms: 1.01x slower                                                 |
| json_dumps             | 13.3 ms                                                                 | 13.5 ms: 1.01x slower                                                |
| pyflate                | 519 ms                                                                  | 526 ms: 1.01x slower                                                 |
| sqlglot_v2_parse       | 1.49 ms                                                                 | 1.51 ms: 1.02x slower                                                |
| pprint_safe_repr       | 1.14 sec                                                                | 1.15 sec: 1.02x slower                                               |
| genshi_xml             | 62.3 ms                                                                 | 63.3 ms: 1.02x slower                                                |
| nqueens                | 99.4 ms                                                                 | 101 ms: 1.02x slower                                                 |
| sympy_integrate        | 20.6 ms                                                                 | 20.9 ms: 1.02x slower                                                |
| sqlglot_v2_transpile   | 1.83 ms                                                                 | 1.86 ms: 1.02x slower                                                |
| create_gc_cycles       | 3.82 ms                                                                 | 3.93 ms: 1.03x slower                                                |
| shortest_path          | 585 ms                                                                  | 605 ms: 1.03x slower                                                 |
| dulwich_log            | 53.0 ms                                                                 | 54.9 ms: 1.04x slower                                                |
| json                   | 5.65 ms                                                                 | 5.89 ms: 1.04x slower                                                |
| pickle_pure_python     | 383 us                                                                  | 400 us: 1.04x slower                                                 |
| telco                  | 158 ms                                                                  | 167 ms: 1.06x slower                                                 |
| Geometric mean         | (ref)                                                                   | 1.01x slower                                                         |

Benchmark hidden because not significant (69): scimark_sparse_mat_mult, comprehensions, scimark_lu, typing_runtime_protocols, xml_etree_generate, coverage, scimark_fft, deepcopy, pidigits, sympy_str, async_tree_memoization_tg, raytrace, meteor_contest, async_tree_io, mdp, async_tree_io_tg, sqlglot_v2_normalize, json_loads, pprint_pformat, many_optionals, async_tree_cpu_io_mixed_tg, python_startup, scimark_monte_carlo, gc_traversal, float, hexiom, djangocms, python_startup_no_site, regex_effbot, sqlglot_v2_optimize, async_tree_none_tg, xml_etree_process, pycparser, go, coroutines, docutils, scimark_sor, regex_dna, bpe_tokeniser, async_tree_none, async_tree_cpu_io_mixed, deltablue, asyncio_websockets, tomli_loads, chaos, async_generators, html5lib, sphinx, spectral_norm, sympy_expand, pathlib, fannkuch, k_core, unpickle_pure_python, subparsers, thrift, generators, logging_simple, pylint, regex_v8, logging_silent, deepcopy_reduce, richards_super, genshi_text, regex_compile, nbody, django_template, deepcopy_memo, crypto_pyaes

- Geometric mean (including insignificant results): 1.004x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x