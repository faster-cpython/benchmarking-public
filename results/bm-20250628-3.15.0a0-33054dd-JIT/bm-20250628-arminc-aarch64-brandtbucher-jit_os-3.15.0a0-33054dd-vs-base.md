# Results vs. base

- fork: brandtbucher
- ref: jit_os
- machine: linux-aarch64
- commit hash: 33054dd
- commit date: 2025-06-28
- overall geometric mean: 1.000x faster
- HPT reliability: 97.43%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-arminc-aarch64-brandtbucher-jit_os-3.15.0a0-33054dd |
|------------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_memoization | 479 ms                                                                  | 473 ms: 1.01x faster                                            |
| Geometric mean         | (ref)                                                                   | 1.00x faster                                                    |

Benchmark hidden because not significant (10): async_tree_none, async_tree_memoization_tg, async_tree_none_tg, async_generators, asyncio_websockets, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_cpu_io_mixed, coroutines

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): pidigits, float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-arminc-aarch64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_v8       | 26.7 ms                                                                 | 26.4 ms: 1.01x faster                                           |
| regex_dna      | 217 ms                                                                  | 224 ms: 1.03x slower                                            |
| Geometric mean | (ref)                                                                   | 1.00x slower                                                    |

Benchmark hidden because not significant (2): regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-arminc-aarch64-brandtbucher-jit_os-3.15.0a0-33054dd |
|---------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| tomli_loads         | 2.36 sec                                                                | 2.32 sec: 1.02x faster                                          |
| xml_etree_iterparse | 145 ms                                                                  | 143 ms: 1.01x faster                                            |
| xml_etree_generate  | 109 ms                                                                  | 108 ms: 1.01x faster                                            |
| xml_etree_process   | 78.3 ms                                                                 | 77.6 ms: 1.01x faster                                           |
| json_loads          | 32.5 us                                                                 | 32.7 us: 1.01x slower                                           |
| pickle_pure_python  | 390 us                                                                  | 397 us: 1.02x slower                                            |
| Geometric mean      | (ref)                                                                   | 1.00x slower                                                    |

Benchmark hidden because not significant (3): xml_etree_parse, unpickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-arminc-aarch64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup | 15.1 ms                                                                 | 15.2 ms: 1.01x slower                                           |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                    |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-arminc-aarch64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| mako           | 13.2 ms                                                                 | 13.1 ms: 1.01x faster                                           |
| Geometric mean | (ref)                                                                   | 1.00x faster                                                    |

Benchmark hidden because not significant (3): genshi_xml, genshi_text, django_template

All benchmarks:
===============

| Benchmark              | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-arminc-aarch64-brandtbucher-jit_os-3.15.0a0-33054dd |
|------------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| deepcopy_memo          | 38.6 us                                                                 | 36.3 us: 1.06x faster                                           |
| deepcopy_reduce        | 3.70 us                                                                 | 3.56 us: 1.04x faster                                           |
| fannkuch               | 479 ms                                                                  | 464 ms: 1.03x faster                                            |
| pprint_pformat         | 2.38 sec                                                                | 2.32 sec: 1.02x faster                                          |
| go                     | 158 ms                                                                  | 154 ms: 1.02x faster                                            |
| tomli_loads            | 2.36 sec                                                                | 2.32 sec: 1.02x faster                                          |
| hexiom                 | 7.48 ms                                                                 | 7.36 ms: 1.02x faster                                           |
| xml_etree_iterparse    | 145 ms                                                                  | 143 ms: 1.01x faster                                            |
| async_tree_memoization | 479 ms                                                                  | 473 ms: 1.01x faster                                            |
| regex_v8               | 26.7 ms                                                                 | 26.4 ms: 1.01x faster                                           |
| mako                   | 13.2 ms                                                                 | 13.1 ms: 1.01x faster                                           |
| pyflate                | 525 ms                                                                  | 520 ms: 1.01x faster                                            |
| xml_etree_generate     | 109 ms                                                                  | 108 ms: 1.01x faster                                            |
| xml_etree_process      | 78.3 ms                                                                 | 77.6 ms: 1.01x faster                                           |
| json_loads             | 32.5 us                                                                 | 32.7 us: 1.01x slower                                           |
| python_startup         | 15.1 ms                                                                 | 15.2 ms: 1.01x slower                                           |
| subparsers             | 28.4 ms                                                                 | 28.6 ms: 1.01x slower                                           |
| djangocms              | 65.1 us                                                                 | 66.0 us: 1.01x slower                                           |
| pickle_pure_python     | 390 us                                                                  | 397 us: 1.02x slower                                            |
| regex_dna              | 217 ms                                                                  | 224 ms: 1.03x slower                                            |
| thrift                 | 949 us                                                                  | 991 us: 1.04x slower                                            |
| create_gc_cycles       | 3.67 ms                                                                 | 3.97 ms: 1.08x slower                                           |
| Geometric mean         | (ref)                                                                   | 1.00x slower                                                    |

Benchmark hidden because not significant (71): scimark_lu, scimark_monte_carlo, xml_etree_parse, richards_super, pathlib, generators, crypto_pyaes, genshi_xml, async_tree_none, typing_runtime_protocols, regex_effbot, pidigits, sympy_expand, sqlglot_v2_transpile, pprint_safe_repr, shortest_path, dulwich_log, chaos, async_tree_memoization_tg, logging_simple, docutils, richards, scimark_fft, connected_components, raytrace, logging_silent, genshi_text, async_tree_none_tg, json, regex_compile, sqlglot_v2_normalize, sqlglot_v2_optimize, async_generators, pycparser, logging_format, deepcopy, bpe_tokeniser, asyncio_websockets, html5lib, gc_traversal, comprehensions, spectral_norm, async_tree_io_tg, async_tree_cpu_io_mixed_tg, python_startup_no_site, async_tree_io, sqlglot_v2_parse, 2to3, many_optionals, async_tree_cpu_io_mixed, sphinx, float, pylint, meteor_contest, mdp, django_template, telco, k_core, deltablue, coroutines, scimark_sparse_mat_mult, sympy_str, nqueens, sqlite_synth, coverage, unpickle_pure_python, nbody, sympy_sum, scimark_sor, sympy_integrate, json_dumps

- Geometric mean (including insignificant results): 1.000x faster

# HPT report

- Reliability score: 97.43% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x