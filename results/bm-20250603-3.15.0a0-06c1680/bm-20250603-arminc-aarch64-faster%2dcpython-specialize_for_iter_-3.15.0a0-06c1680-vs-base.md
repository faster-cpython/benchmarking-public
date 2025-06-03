# Results vs. base

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: linux-aarch64
- commit hash: 06c1680
- commit date: 2025-06-03
- overall geometric mean: 1.002x faster
- HPT reliability: 97.71%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (11): async_generators, async_tree_none, coroutines, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_memoization, asyncio_websockets, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250603-arminc-aarch64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 | bm-20250603-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_dna      | 235 ms                                                                  | 229 ms: 1.02x faster                                                              |
| Geometric mean | (ref)                                                                   | 1.01x faster                                                                      |

Benchmark hidden because not significant (3): regex_v8, regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark         | bm-20250603-arminc-aarch64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 | bm-20250603-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|-------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| tomli_loads       | 2.50 sec                                                                | 2.46 sec: 1.02x faster                                                            |
| json_dumps        | 13.6 ms                                                                 | 13.5 ms: 1.01x faster                                                             |
| xml_etree_process | 79.5 ms                                                                 | 80.0 ms: 1.01x slower                                                             |
| Geometric mean    | (ref)                                                                   | 1.00x faster                                                                      |

Benchmark hidden because not significant (6): json_loads, xml_etree_iterparse, xml_etree_parse, unpickle_pure_python, pickle_pure_python, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250603-arminc-aarch64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 | bm-20250603-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|------------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 8.62 ms                                                                 | 8.59 ms: 1.00x faster                                                             |
| Geometric mean         | (ref)                                                                   | 1.00x faster                                                                      |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250603-arminc-aarch64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 | bm-20250603-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml     | 62.3 ms                                                                 | 61.0 ms: 1.02x faster                                                             |
| mako           | 13.7 ms                                                                 | 13.9 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                                   | 1.00x faster                                                                      |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark              | bm-20250603-arminc-aarch64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 | bm-20250603-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|------------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pyflate                | 550 ms                                                                  | 526 ms: 1.05x faster                                                              |
| thrift                 | 197 ms                                                                  | 191 ms: 1.03x faster                                                              |
| pycparser              | 1.28 sec                                                                | 1.24 sec: 1.03x faster                                                            |
| logging_format         | 8.49 us                                                                 | 8.25 us: 1.03x faster                                                             |
| regex_dna              | 235 ms                                                                  | 229 ms: 1.02x faster                                                              |
| mdp                    | 1.68 sec                                                                | 1.65 sec: 1.02x faster                                                            |
| genshi_xml             | 62.3 ms                                                                 | 61.0 ms: 1.02x faster                                                             |
| deepcopy_reduce        | 3.60 us                                                                 | 3.52 us: 1.02x faster                                                             |
| pprint_safe_repr       | 1.00 sec                                                                | 983 ms: 1.02x faster                                                              |
| tomli_loads            | 2.50 sec                                                                | 2.46 sec: 1.02x faster                                                            |
| pprint_pformat         | 2.03 sec                                                                | 2.01 sec: 1.01x faster                                                            |
| sqlite_synth           | 3.86 us                                                                 | 3.83 us: 1.01x faster                                                             |
| json_dumps             | 13.6 ms                                                                 | 13.5 ms: 1.01x faster                                                             |
| shortest_path          | 582 ms                                                                  | 577 ms: 1.01x faster                                                              |
| python_startup_no_site | 8.62 ms                                                                 | 8.59 ms: 1.00x faster                                                             |
| generators             | 35.6 ms                                                                 | 35.8 ms: 1.01x slower                                                             |
| xml_etree_process      | 79.5 ms                                                                 | 80.0 ms: 1.01x slower                                                             |
| mako                   | 13.7 ms                                                                 | 13.9 ms: 1.01x slower                                                             |
| coverage               | 555 ms                                                                  | 568 ms: 1.02x slower                                                              |
| sqlglot_v2_parse       | 1.40 ms                                                                 | 1.44 ms: 1.03x slower                                                             |
| sympy_str              | 262 ms                                                                  | 277 ms: 1.06x slower                                                              |
| Geometric mean         | (ref)                                                                   | 1.00x faster                                                                      |

Benchmark hidden because not significant (71): regex_v8, nqueens, django_template, meteor_contest, deltablue, sqlglot_v2_optimize, go, richards, hexiom, gc_traversal, pylint, pathlib, json_loads, async_generators, logging_simple, async_tree_none, float, deepcopy, regex_compile, logging_silent, coroutines, crypto_pyaes, xml_etree_iterparse, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, scimark_sparse_mat_mult, sqlglot_v2_transpile, sympy_expand, xml_etree_parse, async_tree_memoization, asyncio_websockets, scimark_lu, python_startup, k_core, bpe_tokeniser, async_tree_none_tg, deepcopy_memo, async_tree_cpu_io_mixed, scimark_monte_carlo, scimark_fft, raytrace, json, async_tree_io_tg, unpickle_pure_python, sphinx, connected_components, chaos, docutils, pickle_pure_python, sympy_sum, pidigits, sympy_integrate, sqlglot_v2_normalize, html5lib, richards_super, async_tree_io, 2to3, comprehensions, fannkuch, scimark_sor, create_gc_cycles, many_optionals, spectral_norm, subparsers, genshi_text, dulwich_log, telco, regex_effbot, typing_runtime_protocols, nbody, xml_etree_generate

- Geometric mean (including insignificant results): 1.002x faster

# HPT report

- Reliability score: 97.71% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x