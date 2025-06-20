# Results vs. base

- fork: brandtbucher
- ref: justin_hot
- machine: linux-aarch64
- commit hash: d2c9ae9
- commit date: 2025-06-19
- overall geometric mean: 1.032x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250619-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 311 ms                                                                  | 317 ms: 1.02x slower                                                |
| docutils       | 3.12 sec                                                                | 3.15 sec: 1.01x slower                                              |
| Geometric mean | (ref)                                                                   | 1.00x slower                                                        |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250619-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization     | 468 ms                                                                  | 473 ms: 1.01x slower                                                |
| async_tree_cpu_io_mixed_tg | 655 ms                                                                  | 665 ms: 1.01x slower                                                |
| async_tree_none            | 396 ms                                                                  | 403 ms: 1.02x slower                                                |
| Geometric mean             | (ref)                                                                   | 1.01x slower                                                        |

Benchmark hidden because not significant (8): async_generators, asyncio_websockets, async_tree_none_tg, async_tree_io, async_tree_io_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250619-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 83.3 ms                                                                 | 88.6 ms: 1.06x slower                                               |
| nbody          | 122 ms                                                                  | 147 ms: 1.20x slower                                                |
| Geometric mean | (ref)                                                                   | 1.08x slower                                                        |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250619-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 122 ms                                                                  | 130 ms: 1.07x slower                                                |
| Geometric mean | (ref)                                                                   | 1.02x slower                                                        |

Benchmark hidden because not significant (3): regex_dna, regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250619-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_parse      | 187 ms                                                                  | 180 ms: 1.04x faster                                                |
| xml_etree_iterparse  | 149 ms                                                                  | 144 ms: 1.03x faster                                                |
| xml_etree_process    | 78.7 ms                                                                 | 80.9 ms: 1.03x slower                                               |
| tomli_loads          | 2.42 sec                                                                | 2.55 sec: 1.06x slower                                              |
| unpickle_pure_python | 251 us                                                                  | 295 us: 1.18x slower                                                |
| Geometric mean       | (ref)                                                                   | 1.02x slower                                                        |

Benchmark hidden because not significant (4): pickle_pure_python, json_loads, xml_etree_generate, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250619-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|------------------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                                 | 15.0 ms: 1.01x faster                                               |
| python_startup_no_site | 8.63 ms                                                                 | 8.60 ms: 1.00x faster                                               |
| Geometric mean         | (ref)                                                                   | 1.01x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250619-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako           | 13.2 ms                                                                 | 15.1 ms: 1.15x slower                                               |
| Geometric mean | (ref)                                                                   | 1.04x slower                                                        |

Benchmark hidden because not significant (3): django_template, genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250619-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_parse            | 187 ms                                                                  | 180 ms: 1.04x faster                                                |
| xml_etree_iterparse        | 149 ms                                                                  | 144 ms: 1.03x faster                                                |
| sympy_expand               | 509 ms                                                                  | 493 ms: 1.03x faster                                                |
| python_startup             | 15.2 ms                                                                 | 15.0 ms: 1.01x faster                                               |
| sqlite_synth               | 3.81 us                                                                 | 3.77 us: 1.01x faster                                               |
| logging_format             | 8.35 us                                                                 | 8.29 us: 1.01x faster                                               |
| python_startup_no_site     | 8.63 ms                                                                 | 8.60 ms: 1.00x faster                                               |
| async_tree_memoization     | 468 ms                                                                  | 473 ms: 1.01x slower                                                |
| docutils                   | 3.12 sec                                                                | 3.15 sec: 1.01x slower                                              |
| mdp                        | 1.70 sec                                                                | 1.72 sec: 1.01x slower                                              |
| async_tree_cpu_io_mixed_tg | 655 ms                                                                  | 665 ms: 1.01x slower                                                |
| async_tree_none            | 396 ms                                                                  | 403 ms: 1.02x slower                                                |
| 2to3                       | 311 ms                                                                  | 317 ms: 1.02x slower                                                |
| shortest_path              | 586 ms                                                                  | 598 ms: 1.02x slower                                                |
| connected_components       | 570 ms                                                                  | 583 ms: 1.02x slower                                                |
| xml_etree_process          | 78.7 ms                                                                 | 80.9 ms: 1.03x slower                                               |
| raytrace                   | 333 ms                                                                  | 343 ms: 1.03x slower                                                |
| dulwich_log                | 54.1 ms                                                                 | 56.1 ms: 1.04x slower                                               |
| nqueens                    | 101 ms                                                                  | 106 ms: 1.05x slower                                                |
| scimark_monte_carlo        | 82.8 ms                                                                 | 86.9 ms: 1.05x slower                                               |
| bpe_tokeniser              | 5.53 sec                                                                | 5.82 sec: 1.05x slower                                              |
| tomli_loads                | 2.42 sec                                                                | 2.55 sec: 1.06x slower                                              |
| pycparser                  | 1.37 sec                                                                | 1.46 sec: 1.06x slower                                              |
| float                      | 83.3 ms                                                                 | 88.6 ms: 1.06x slower                                               |
| regex_compile              | 122 ms                                                                  | 130 ms: 1.07x slower                                                |
| telco                      | 9.36 ms                                                                 | 10.1 ms: 1.08x slower                                               |
| richards_super             | 51.3 ms                                                                 | 55.7 ms: 1.09x slower                                               |
| meteor_contest             | 117 ms                                                                  | 127 ms: 1.09x slower                                                |
| scimark_fft                | 425 ms                                                                  | 466 ms: 1.10x slower                                                |
| sqlglot_v2_parse           | 1.54 ms                                                                 | 1.69 ms: 1.10x slower                                               |
| comprehensions             | 22.5 us                                                                 | 25.1 us: 1.12x slower                                               |
| pyflate                    | 539 ms                                                                  | 606 ms: 1.12x slower                                                |
| crypto_pyaes               | 90.9 ms                                                                 | 102 ms: 1.13x slower                                                |
| richards                   | 46.1 ms                                                                 | 52.1 ms: 1.13x slower                                               |
| mako                       | 13.2 ms                                                                 | 15.1 ms: 1.15x slower                                               |
| fannkuch                   | 482 ms                                                                  | 557 ms: 1.16x slower                                                |
| spectral_norm              | 131 ms                                                                  | 152 ms: 1.16x slower                                                |
| deltablue                  | 3.93 ms                                                                 | 4.57 ms: 1.16x slower                                               |
| unpickle_pure_python       | 251 us                                                                  | 295 us: 1.18x slower                                                |
| hexiom                     | 7.51 ms                                                                 | 8.91 ms: 1.19x slower                                               |
| nbody                      | 122 ms                                                                  | 147 ms: 1.20x slower                                                |
| pprint_pformat             | 2.66 sec                                                                | 3.25 sec: 1.22x slower                                              |
| go                         | 158 ms                                                                  | 193 ms: 1.23x slower                                                |
| pprint_safe_repr           | 1.26 sec                                                                | 1.54 sec: 1.23x slower                                              |
| Geometric mean             | (ref)                                                                   | 1.03x slower                                                        |

Benchmark hidden because not significant (49): typing_runtime_protocols, thrift, logging_simple, logging_silent, django_template, html5lib, json, create_gc_cycles, sphinx, coverage, deepcopy, pickle_pure_python, genshi_text, deepcopy_memo, async_generators, sympy_integrate, regex_dna, json_loads, pidigits, asyncio_websockets, sqlglot_v2_normalize, regex_v8, generators, djangocms, deepcopy_reduce, async_tree_none_tg, chaos, xml_etree_generate, async_tree_io, async_tree_io_tg, scimark_lu, sympy_sum, async_tree_memoization_tg, json_dumps, pathlib, scimark_sor, regex_effbot, many_optionals, subparsers, sqlglot_v2_optimize, async_tree_cpu_io_mixed, k_core, gc_traversal, sympy_str, coroutines, sqlglot_v2_transpile, pylint, genshi_xml, scimark_sparse_mat_mult

- Geometric mean (including insignificant results): 1.032x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x