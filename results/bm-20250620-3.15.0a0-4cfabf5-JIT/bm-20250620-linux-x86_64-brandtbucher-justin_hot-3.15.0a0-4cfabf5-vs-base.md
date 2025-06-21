# Results vs. base

- fork: brandtbucher
- ref: justin_hot
- machine: linux-x86_64
- commit hash: 4cfabf5
- commit date: 2025-06-20
- overall geometric mean: 1.001x faster
- HPT reliability: 55.98%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250620-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 261 ms                                                                | 260 ms: 1.00x faster                                              |
| docutils       | 2.65 sec                                                              | 2.64 sec: 1.00x faster                                            |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                      |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250620-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| coroutines                 | 26.0 ms                                                               | 25.3 ms: 1.03x faster                                             |
| async_tree_memoization     | 315 ms                                                                | 319 ms: 1.01x slower                                              |
| async_tree_cpu_io_mixed_tg | 486 ms                                                                | 492 ms: 1.01x slower                                              |
| async_generators           | 426 ms                                                                | 432 ms: 1.01x slower                                              |
| async_tree_cpu_io_mixed    | 491 ms                                                                | 500 ms: 1.02x slower                                              |
| Geometric mean             | (ref)                                                                 | 1.01x slower                                                      |

Benchmark hidden because not significant (6): asyncio_websockets, async_tree_none_tg, async_tree_memoization_tg, async_tree_none, async_tree_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250620-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 65.2 ms                                                               | 64.9 ms: 1.01x faster                                             |
| pidigits       | 187 ms                                                                | 187 ms: 1.00x faster                                              |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                      |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250620-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 129 ms                                                                | 127 ms: 1.01x faster                                              |
| regex_effbot   | 3.26 ms                                                               | 3.31 ms: 1.01x slower                                             |
| regex_v8       | 21.6 ms                                                               | 22.8 ms: 1.05x slower                                             |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                      |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250620-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| unpickle_pure_python | 200 us                                                                | 199 us: 1.01x faster                                              |
| tomli_loads          | 1.91 sec                                                              | 1.90 sec: 1.01x faster                                            |
| json_loads           | 28.4 us                                                               | 28.6 us: 1.01x slower                                             |
| xml_etree_process    | 55.4 ms                                                               | 56.0 ms: 1.01x slower                                             |
| xml_etree_parse      | 138 ms                                                                | 141 ms: 1.02x slower                                              |
| json_dumps           | 11.1 ms                                                               | 11.3 ms: 1.02x slower                                             |
| xml_etree_iterparse  | 97.9 ms                                                               | 100 ms: 1.02x slower                                              |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                      |

Benchmark hidden because not significant (2): xml_etree_generate, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250620-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 12.2 ms                                                               | 12.2 ms: 1.00x faster                                             |
| python_startup_no_site | 6.97 ms                                                               | 6.95 ms: 1.00x faster                                             |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250620-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako           | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                             |
| genshi_text    | 21.3 ms                                                               | 21.7 ms: 1.02x slower                                             |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                      |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250620-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| gc_traversal               | 5.08 ms                                                               | 4.75 ms: 1.07x faster                                             |
| go                         | 125 ms                                                                | 122 ms: 1.03x faster                                              |
| subparsers                 | 24.2 ms                                                               | 23.6 ms: 1.03x faster                                             |
| pprint_pformat             | 1.71 sec                                                              | 1.66 sec: 1.03x faster                                            |
| coroutines                 | 26.0 ms                                                               | 25.3 ms: 1.03x faster                                             |
| raytrace                   | 280 ms                                                                | 274 ms: 1.02x faster                                              |
| crypto_pyaes               | 76.3 ms                                                               | 74.9 ms: 1.02x faster                                             |
| deltablue                  | 3.17 ms                                                               | 3.12 ms: 1.02x faster                                             |
| deepcopy                   | 262 us                                                                | 258 us: 1.02x faster                                              |
| spectral_norm              | 106 ms                                                                | 104 ms: 1.02x faster                                              |
| telco                      | 7.79 ms                                                               | 7.67 ms: 1.02x faster                                             |
| comprehensions             | 17.3 us                                                               | 17.1 us: 1.01x faster                                             |
| sqlite_synth               | 2.83 us                                                               | 2.80 us: 1.01x faster                                             |
| regex_compile              | 129 ms                                                                | 127 ms: 1.01x faster                                              |
| dulwich_log                | 60.2 ms                                                               | 59.5 ms: 1.01x faster                                             |
| chaos                      | 63.1 ms                                                               | 62.4 ms: 1.01x faster                                             |
| fannkuch                   | 413 ms                                                                | 409 ms: 1.01x faster                                              |
| unpickle_pure_python       | 200 us                                                                | 199 us: 1.01x faster                                              |
| scimark_lu                 | 120 ms                                                                | 119 ms: 1.01x faster                                              |
| scimark_monte_carlo        | 67.4 ms                                                               | 66.8 ms: 1.01x faster                                             |
| shortest_path              | 495 ms                                                                | 492 ms: 1.01x faster                                              |
| logging_silent             | 475 ns                                                                | 472 ns: 1.01x faster                                              |
| sympy_expand               | 469 ms                                                                | 466 ms: 1.01x faster                                              |
| tomli_loads                | 1.91 sec                                                              | 1.90 sec: 1.01x faster                                            |
| float                      | 65.2 ms                                                               | 64.9 ms: 1.01x faster                                             |
| logging_format             | 6.86 us                                                               | 6.83 us: 1.01x faster                                             |
| sympy_sum                  | 151 ms                                                                | 150 ms: 1.01x faster                                              |
| scimark_fft                | 332 ms                                                                | 330 ms: 1.00x faster                                              |
| python_startup             | 12.2 ms                                                               | 12.2 ms: 1.00x faster                                             |
| create_gc_cycles           | 2.60 ms                                                               | 2.59 ms: 1.00x faster                                             |
| python_startup_no_site     | 6.97 ms                                                               | 6.95 ms: 1.00x faster                                             |
| docutils                   | 2.65 sec                                                              | 2.64 sec: 1.00x faster                                            |
| 2to3                       | 261 ms                                                                | 260 ms: 1.00x faster                                              |
| pidigits                   | 187 ms                                                                | 187 ms: 1.00x faster                                              |
| sympy_integrate            | 19.4 ms                                                               | 19.5 ms: 1.00x slower                                             |
| meteor_contest             | 106 ms                                                                | 107 ms: 1.01x slower                                              |
| sqlglot_v2_transpile       | 1.59 ms                                                               | 1.60 ms: 1.01x slower                                             |
| mdp                        | 1.26 sec                                                              | 1.27 sec: 1.01x slower                                            |
| json_loads                 | 28.4 us                                                               | 28.6 us: 1.01x slower                                             |
| mako                       | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                             |
| deepcopy_memo              | 29.7 us                                                               | 29.9 us: 1.01x slower                                             |
| xml_etree_process          | 55.4 ms                                                               | 56.0 ms: 1.01x slower                                             |
| async_tree_memoization     | 315 ms                                                                | 319 ms: 1.01x slower                                              |
| async_tree_cpu_io_mixed_tg | 486 ms                                                                | 492 ms: 1.01x slower                                              |
| async_generators           | 426 ms                                                                | 432 ms: 1.01x slower                                              |
| logging_simple             | 6.16 us                                                               | 6.25 us: 1.01x slower                                             |
| regex_effbot               | 3.26 ms                                                               | 3.31 ms: 1.01x slower                                             |
| xml_etree_parse            | 138 ms                                                                | 141 ms: 1.02x slower                                              |
| generators                 | 30.4 ms                                                               | 30.9 ms: 1.02x slower                                             |
| json_dumps                 | 11.1 ms                                                               | 11.3 ms: 1.02x slower                                             |
| json                       | 5.19 ms                                                               | 5.28 ms: 1.02x slower                                             |
| async_tree_cpu_io_mixed    | 491 ms                                                                | 500 ms: 1.02x slower                                              |
| genshi_text                | 21.3 ms                                                               | 21.7 ms: 1.02x slower                                             |
| xml_etree_iterparse        | 97.9 ms                                                               | 100 ms: 1.02x slower                                              |
| regex_v8                   | 21.6 ms                                                               | 22.8 ms: 1.05x slower                                             |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                      |

Benchmark hidden because not significant (38): richards_super, coverage, html5lib, richards, hexiom, many_optionals, sqlglot_v2_parse, xml_etree_generate, typing_runtime_protocols, asyncio_websockets, sqlglot_v2_optimize, sphinx, regex_dna, scimark_sor, nbody, deepcopy_reduce, nqueens, django_template, pylint, pprint_safe_repr, sympy_str, bpe_tokeniser, async_tree_none_tg, scimark_sparse_mat_mult, connected_components, pyflate, k_core, pathlib, pycparser, async_tree_memoization_tg, genshi_xml, async_tree_none, async_tree_io, thrift, djangocms, sqlglot_v2_normalize, async_tree_io_tg, pickle_pure_python

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 55.98% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x