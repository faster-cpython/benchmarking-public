# Results vs. base

- fork: faster-cpython
- ref: explicit_check_perio
- machine: linux-aarch64
- commit hash: c84beef
- commit date: 2025-06-23
- overall geometric mean: 1.000x slower
- HPT reliability: 52.37%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250623-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| docutils       | 2.92 sec                                                                | 2.95 sec: 1.01x slower                                                            |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                                      |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark       | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250623-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|-----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_none | 395 ms                                                                  | 389 ms: 1.02x faster                                                              |
| Geometric mean  | (ref)                                                                   | 1.00x slower                                                                      |

Benchmark hidden because not significant (10): async_tree_none_tg, asyncio_websockets, async_tree_memoization_tg, async_generators, async_tree_cpu_io_mixed, coroutines, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250623-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 119 ms                                                                  | 125 ms: 1.05x slower                                                              |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                                      |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250623-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_v8       | 26.3 ms                                                                 | 27.3 ms: 1.04x slower                                                             |
| regex_effbot   | 3.83 ms                                                                 | 4.03 ms: 1.05x slower                                                             |
| Geometric mean | (ref)                                                                   | 1.02x slower                                                                      |

Benchmark hidden because not significant (2): regex_compile, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250623-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|---------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_iterparse | 145 ms                                                                  | 142 ms: 1.02x faster                                                              |
| tomli_loads         | 2.45 sec                                                                | 2.42 sec: 1.01x faster                                                            |
| xml_etree_process   | 80.3 ms                                                                 | 79.4 ms: 1.01x faster                                                             |
| Geometric mean      | (ref)                                                                   | 1.00x faster                                                                      |

Benchmark hidden because not significant (6): json_loads, xml_etree_parse, json_dumps, pickle_pure_python, unpickle_pure_python, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250623-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|------------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 15.1 ms                                                                 | 15.2 ms: 1.01x slower                                                             |
| python_startup_no_site | 8.55 ms                                                                 | 8.69 ms: 1.02x slower                                                             |
| Geometric mean         | (ref)                                                                   | 1.01x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250623-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako           | 13.8 ms                                                                 | 14.3 ms: 1.03x slower                                                             |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                                      |

Benchmark hidden because not significant (3): genshi_xml, genshi_text, django_template

All benchmarks:
===============

| Benchmark              | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250623-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|------------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| logging_silent         | 634 ns                                                                  | 614 ns: 1.03x faster                                                              |
| sqlite_synth           | 3.79 us                                                                 | 3.70 us: 1.02x faster                                                             |
| pyflate                | 524 ms                                                                  | 513 ms: 1.02x faster                                                              |
| xml_etree_iterparse    | 145 ms                                                                  | 142 ms: 1.02x faster                                                              |
| async_tree_none        | 395 ms                                                                  | 389 ms: 1.02x faster                                                              |
| tomli_loads            | 2.45 sec                                                                | 2.42 sec: 1.01x faster                                                            |
| xml_etree_process      | 80.3 ms                                                                 | 79.4 ms: 1.01x faster                                                             |
| json                   | 5.74 ms                                                                 | 5.68 ms: 1.01x faster                                                             |
| bpe_tokeniser          | 5.55 sec                                                                | 5.51 sec: 1.01x faster                                                            |
| coverage               | 101 ms                                                                  | 101 ms: 1.00x faster                                                              |
| python_startup         | 15.1 ms                                                                 | 15.2 ms: 1.01x slower                                                             |
| docutils               | 2.92 sec                                                                | 2.95 sec: 1.01x slower                                                            |
| sqlglot_v2_normalize   | 123 ms                                                                  | 125 ms: 1.02x slower                                                              |
| python_startup_no_site | 8.55 ms                                                                 | 8.69 ms: 1.02x slower                                                             |
| logging_format         | 8.15 us                                                                 | 8.29 us: 1.02x slower                                                             |
| dulwich_log            | 51.9 ms                                                                 | 53.4 ms: 1.03x slower                                                             |
| mako                   | 13.8 ms                                                                 | 14.3 ms: 1.03x slower                                                             |
| regex_v8               | 26.3 ms                                                                 | 27.3 ms: 1.04x slower                                                             |
| nbody                  | 119 ms                                                                  | 125 ms: 1.05x slower                                                              |
| regex_effbot           | 3.83 ms                                                                 | 4.03 ms: 1.05x slower                                                             |
| Geometric mean         | (ref)                                                                   | 1.00x slower                                                                      |

Benchmark hidden because not significant (73): richards_super, richards, regex_compile, nqueens, sympy_expand, subparsers, raytrace, thrift, pidigits, deepcopy, genshi_xml, deepcopy_reduce, k_core, sqlglot_v2_optimize, go, scimark_sor, fannkuch, async_tree_none_tg, sympy_str, asyncio_websockets, shortest_path, generators, pprint_pformat, genshi_text, mdp, gc_traversal, sqlglot_v2_parse, html5lib, json_loads, xml_etree_parse, typing_runtime_protocols, djangocms, async_tree_memoization_tg, async_generators, sphinx, pylint, connected_components, async_tree_cpu_io_mixed, coroutines, pprint_safe_repr, regex_dna, json_dumps, many_optionals, comprehensions, sympy_sum, async_tree_cpu_io_mixed_tg, float, crypto_pyaes, pickle_pure_python, async_tree_memoization, async_tree_io_tg, 2to3, unpickle_pure_python, pycparser, spectral_norm, scimark_monte_carlo, async_tree_io, scimark_fft, telco, django_template, pathlib, create_gc_cycles, sqlglot_v2_transpile, xml_etree_generate, hexiom, sympy_integrate, deltablue, meteor_contest, chaos, scimark_lu, logging_simple, deepcopy_memo, scimark_sparse_mat_mult

- Geometric mean (including insignificant results): 1.000x slower

# HPT report

- Reliability score: 52.37% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x