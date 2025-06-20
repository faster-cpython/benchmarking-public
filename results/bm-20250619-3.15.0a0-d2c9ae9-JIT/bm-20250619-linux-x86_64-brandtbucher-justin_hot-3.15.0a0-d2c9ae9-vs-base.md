# Results vs. base

- fork: brandtbucher
- ref: justin_hot
- machine: linux-x86_64
- commit hash: d2c9ae9
- commit date: 2025-06-19
- overall geometric mean: 1.005x slower
- HPT reliability: 65.39%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250619-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 261 ms                                                                | 260 ms: 1.00x faster                                              |
| docutils       | 2.64 sec                                                              | 2.65 sec: 1.00x slower                                            |
| html5lib       | 61.5 ms                                                               | 62.3 ms: 1.01x slower                                             |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                      |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250619-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| coroutines                 | 25.4 ms                                                               | 24.3 ms: 1.05x faster                                             |
| async_generators           | 435 ms                                                                | 433 ms: 1.01x faster                                              |
| async_tree_cpu_io_mixed_tg | 485 ms                                                                | 490 ms: 1.01x slower                                              |
| async_tree_cpu_io_mixed    | 491 ms                                                                | 498 ms: 1.01x slower                                              |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                      |

Benchmark hidden because not significant (7): async_tree_none_tg, async_tree_memoization, async_tree_io_tg, async_tree_io, async_tree_memoization_tg, asyncio_websockets, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250619-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| pidigits       | 190 ms                                                                | 187 ms: 1.02x faster                                              |
| float          | 65.7 ms                                                               | 66.3 ms: 1.01x slower                                             |
| nbody          | 90.9 ms                                                               | 95.0 ms: 1.04x slower                                             |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250619-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 129 ms                                                                | 128 ms: 1.01x faster                                              |
| regex_effbot   | 3.20 ms                                                               | 3.32 ms: 1.04x slower                                             |
| regex_v8       | 21.5 ms                                                               | 22.8 ms: 1.06x slower                                             |
| regex_dna      | 196 ms                                                                | 219 ms: 1.12x slower                                              |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250619-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| xml_etree_parse      | 141 ms                                                                | 140 ms: 1.01x faster                                              |
| xml_etree_generate   | 81.3 ms                                                               | 80.8 ms: 1.01x faster                                             |
| json_loads           | 28.7 us                                                               | 28.8 us: 1.00x slower                                             |
| pickle_pure_python   | 323 us                                                                | 325 us: 1.01x slower                                              |
| tomli_loads          | 1.90 sec                                                              | 1.92 sec: 1.01x slower                                            |
| unpickle_pure_python | 202 us                                                                | 205 us: 1.02x slower                                              |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                      |

Benchmark hidden because not significant (3): xml_etree_process, xml_etree_iterparse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250619-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 12.2 ms                                                               | 12.2 ms: 1.00x slower                                             |
| python_startup_no_site | 6.95 ms                                                               | 6.96 ms: 1.00x slower                                             |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250619-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_text    | 21.3 ms                                                               | 21.1 ms: 1.01x faster                                             |
| mako           | 10.5 ms                                                               | 10.8 ms: 1.03x slower                                             |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                      |

Benchmark hidden because not significant (2): genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250619-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| coroutines                 | 25.4 ms                                                               | 24.3 ms: 1.05x faster                                             |
| scimark_sor                | 123 ms                                                                | 121 ms: 1.02x faster                                              |
| generators                 | 31.1 ms                                                               | 30.5 ms: 1.02x faster                                             |
| meteor_contest             | 108 ms                                                                | 106 ms: 1.02x faster                                              |
| pidigits                   | 190 ms                                                                | 187 ms: 1.02x faster                                              |
| richards_super             | 39.9 ms                                                               | 39.3 ms: 1.02x faster                                             |
| regex_compile              | 129 ms                                                                | 128 ms: 1.01x faster                                              |
| pathlib                    | 17.1 ms                                                               | 16.9 ms: 1.01x faster                                             |
| genshi_text                | 21.3 ms                                                               | 21.1 ms: 1.01x faster                                             |
| thrift                     | 787 us                                                                | 780 us: 1.01x faster                                              |
| xml_etree_parse            | 141 ms                                                                | 140 ms: 1.01x faster                                              |
| xml_etree_generate         | 81.3 ms                                                               | 80.8 ms: 1.01x faster                                             |
| subparsers                 | 23.7 ms                                                               | 23.5 ms: 1.01x faster                                             |
| dulwich_log                | 60.0 ms                                                               | 59.6 ms: 1.01x faster                                             |
| async_generators           | 435 ms                                                                | 433 ms: 1.01x faster                                              |
| sqlglot_v2_optimize        | 53.2 ms                                                               | 52.9 ms: 1.00x faster                                             |
| bpe_tokeniser              | 4.45 sec                                                              | 4.43 sec: 1.00x faster                                            |
| sympy_str                  | 274 ms                                                                | 273 ms: 1.00x faster                                              |
| 2to3                       | 261 ms                                                                | 260 ms: 1.00x faster                                              |
| python_startup             | 12.2 ms                                                               | 12.2 ms: 1.00x slower                                             |
| python_startup_no_site     | 6.95 ms                                                               | 6.96 ms: 1.00x slower                                             |
| create_gc_cycles           | 2.59 ms                                                               | 2.59 ms: 1.00x slower                                             |
| docutils                   | 2.64 sec                                                              | 2.65 sec: 1.00x slower                                            |
| json_loads                 | 28.7 us                                                               | 28.8 us: 1.00x slower                                             |
| deepcopy_reduce            | 2.70 us                                                               | 2.72 us: 1.01x slower                                             |
| pickle_pure_python         | 323 us                                                                | 325 us: 1.01x slower                                              |
| sympy_integrate            | 19.4 ms                                                               | 19.5 ms: 1.01x slower                                             |
| hexiom                     | 6.47 ms                                                               | 6.53 ms: 1.01x slower                                             |
| tomli_loads                | 1.90 sec                                                              | 1.92 sec: 1.01x slower                                            |
| float                      | 65.7 ms                                                               | 66.3 ms: 1.01x slower                                             |
| fannkuch                   | 412 ms                                                                | 416 ms: 1.01x slower                                              |
| coverage                   | 87.2 ms                                                               | 88.1 ms: 1.01x slower                                             |
| deepcopy                   | 258 us                                                                | 260 us: 1.01x slower                                              |
| async_tree_cpu_io_mixed_tg | 485 ms                                                                | 490 ms: 1.01x slower                                              |
| html5lib                   | 61.5 ms                                                               | 62.3 ms: 1.01x slower                                             |
| nqueens                    | 82.9 ms                                                               | 84.0 ms: 1.01x slower                                             |
| async_tree_cpu_io_mixed    | 491 ms                                                                | 498 ms: 1.01x slower                                              |
| deltablue                  | 3.17 ms                                                               | 3.22 ms: 1.02x slower                                             |
| unpickle_pure_python       | 202 us                                                                | 205 us: 1.02x slower                                              |
| connected_components       | 455 ms                                                                | 462 ms: 1.02x slower                                              |
| pprint_pformat             | 1.70 sec                                                              | 1.73 sec: 1.02x slower                                            |
| scimark_fft                | 330 ms                                                                | 336 ms: 1.02x slower                                              |
| djangocms                  | 22.1 us                                                               | 22.5 us: 1.02x slower                                             |
| comprehensions             | 17.1 us                                                               | 17.4 us: 1.02x slower                                             |
| logging_simple             | 6.09 us                                                               | 6.21 us: 1.02x slower                                             |
| logging_format             | 6.72 us                                                               | 6.89 us: 1.03x slower                                             |
| mako                       | 10.5 ms                                                               | 10.8 ms: 1.03x slower                                             |
| gc_traversal               | 4.78 ms                                                               | 4.93 ms: 1.03x slower                                             |
| spectral_norm              | 101 ms                                                                | 105 ms: 1.04x slower                                              |
| regex_effbot               | 3.20 ms                                                               | 3.32 ms: 1.04x slower                                             |
| scimark_sparse_mat_mult    | 4.84 ms                                                               | 5.04 ms: 1.04x slower                                             |
| nbody                      | 90.9 ms                                                               | 95.0 ms: 1.04x slower                                             |
| pyflate                    | 414 ms                                                                | 432 ms: 1.04x slower                                              |
| regex_v8                   | 21.5 ms                                                               | 22.8 ms: 1.06x slower                                             |
| regex_dna                  | 196 ms                                                                | 219 ms: 1.12x slower                                              |
| Geometric mean             | (ref)                                                                 | 1.01x slower                                                      |

Benchmark hidden because not significant (38): scimark_lu, pycparser, sqlglot_v2_normalize, xml_etree_process, go, async_tree_none_tg, deepcopy_memo, chaos, logging_silent, shortest_path, many_optionals, sqlglot_v2_parse, pprint_safe_repr, xml_etree_iterparse, async_tree_memoization, k_core, richards, raytrace, scimark_monte_carlo, pylint, async_tree_io_tg, sympy_expand, sqlite_synth, async_tree_io, mdp, async_tree_memoization_tg, asyncio_websockets, sympy_sum, async_tree_none, json, sqlglot_v2_transpile, crypto_pyaes, json_dumps, genshi_xml, django_template, typing_runtime_protocols, sphinx, telco

- Geometric mean (including insignificant results): 1.005x slower

# HPT report

- Reliability score: 65.39% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x