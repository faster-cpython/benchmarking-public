# Results vs. base

- fork: brandtbucher
- ref: justin_cold_16
- machine: linux-x86_64
- commit hash: 189256b
- commit date: 2024-12-04
- overall geometric mean: 1.004x slower
- HPT reliability: 99.90%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241204-linux-x86_64-brandtbucher-justin_cold_16-3.14.0a2+-189256b |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 258 ms                                                                 | 260 ms: 1.01x slower                                                   |
| html5lib       | 64.2 ms                                                                | 64.9 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241204-linux-x86_64-brandtbucher-justin_cold_16-3.14.0a2+-189256b |
|---------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg | 313 ms                                                                 | 315 ms: 1.01x slower                                                   |
| async_tree_cpu_io_mixed   | 490 ms                                                                 | 493 ms: 1.01x slower                                                   |
| async_tree_none_tg        | 249 ms                                                                 | 252 ms: 1.01x slower                                                   |
| async_tree_io             | 616 ms                                                                 | 623 ms: 1.01x slower                                                   |
| async_tree_io_tg          | 600 ms                                                                 | 609 ms: 1.01x slower                                                   |
| async_tree_none           | 267 ms                                                                 | 271 ms: 1.01x slower                                                   |
| async_generators          | 445 ms                                                                 | 453 ms: 1.02x slower                                                   |
| coroutines                | 23.1 ms                                                                | 23.6 ms: 1.02x slower                                                  |
| Geometric mean            | (ref)                                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed_tg, async_tree_memoization, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241204-linux-x86_64-brandtbucher-justin_cold_16-3.14.0a2+-189256b |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 82.8 ms                                                                | 80.5 ms: 1.03x faster                                                  |
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241204-linux-x86_64-brandtbucher-justin_cold_16-3.14.0a2+-189256b |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 25.0 ms                                                                | 24.5 ms: 1.02x faster                                                  |
| regex_effbot   | 3.20 ms                                                                | 3.20 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (2): regex_compile, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241204-linux-x86_64-brandtbucher-justin_cold_16-3.14.0a2+-189256b |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 196 us                                                                 | 194 us: 1.01x faster                                                   |
| json_loads           | 26.2 us                                                                | 26.3 us: 1.01x slower                                                  |
| xml_etree_process    | 55.0 ms                                                                | 55.4 ms: 1.01x slower                                                  |
| tomli_loads          | 1.91 sec                                                               | 1.94 sec: 1.01x slower                                                 |
| json_dumps           | 11.1 ms                                                                | 11.3 ms: 1.02x slower                                                  |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (4): pickle_pure_python, xml_etree_generate, xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241204-linux-x86_64-brandtbucher-justin_cold_16-3.14.0a2+-189256b |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x slower                                                  |
| python_startup_no_site | 7.04 ms                                                                | 7.06 ms: 1.00x slower                                                  |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241204-linux-x86_64-brandtbucher-justin_cold_16-3.14.0a2+-189256b |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml     | 57.7 ms                                                                | 56.7 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (3): genshi_text, mako, django_template

All benchmarks:
===============

| Benchmark                 | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241204-linux-x86_64-brandtbucher-justin_cold_16-3.14.0a2+-189256b |
|---------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody                     | 82.8 ms                                                                | 80.5 ms: 1.03x faster                                                  |
| scimark_lu                | 115 ms                                                                 | 112 ms: 1.02x faster                                                   |
| richards_super            | 43.7 ms                                                                | 42.8 ms: 1.02x faster                                                  |
| genshi_xml                | 57.7 ms                                                                | 56.7 ms: 1.02x faster                                                  |
| regex_v8                  | 25.0 ms                                                                | 24.5 ms: 1.02x faster                                                  |
| coverage                  | 84.9 ms                                                                | 83.6 ms: 1.02x faster                                                  |
| meteor_contest            | 110 ms                                                                 | 109 ms: 1.01x faster                                                   |
| hexiom                    | 7.12 ms                                                                | 7.05 ms: 1.01x faster                                                  |
| unpickle_pure_python      | 196 us                                                                 | 194 us: 1.01x faster                                                   |
| sympy_sum                 | 156 ms                                                                 | 155 ms: 1.01x faster                                                   |
| sympy_str                 | 282 ms                                                                 | 281 ms: 1.00x faster                                                   |
| pidigits                  | 186 ms                                                                 | 186 ms: 1.00x slower                                                   |
| regex_effbot              | 3.20 ms                                                                | 3.20 ms: 1.00x slower                                                  |
| python_startup            | 12.8 ms                                                                | 12.8 ms: 1.00x slower                                                  |
| python_startup_no_site    | 7.04 ms                                                                | 7.06 ms: 1.00x slower                                                  |
| create_gc_cycles          | 2.46 ms                                                                | 2.47 ms: 1.00x slower                                                  |
| shortest_path             | 481 ms                                                                 | 484 ms: 1.01x slower                                                   |
| gc_traversal              | 5.01 ms                                                                | 5.04 ms: 1.01x slower                                                  |
| sqlglot_parse             | 1.32 ms                                                                | 1.32 ms: 1.01x slower                                                  |
| sqlglot_optimize          | 55.6 ms                                                                | 55.9 ms: 1.01x slower                                                  |
| json_loads                | 26.2 us                                                                | 26.3 us: 1.01x slower                                                  |
| xml_etree_process         | 55.0 ms                                                                | 55.4 ms: 1.01x slower                                                  |
| async_tree_memoization_tg | 313 ms                                                                 | 315 ms: 1.01x slower                                                   |
| bench_thread_pool         | 872 us                                                                 | 879 us: 1.01x slower                                                   |
| sqlglot_normalize         | 110 ms                                                                 | 111 ms: 1.01x slower                                                   |
| async_tree_cpu_io_mixed   | 490 ms                                                                 | 493 ms: 1.01x slower                                                   |
| generators                | 36.5 ms                                                                | 36.8 ms: 1.01x slower                                                  |
| sqlglot_transpile         | 1.63 ms                                                                | 1.65 ms: 1.01x slower                                                  |
| async_tree_none_tg        | 249 ms                                                                 | 252 ms: 1.01x slower                                                   |
| 2to3                      | 258 ms                                                                 | 260 ms: 1.01x slower                                                   |
| async_tree_io             | 616 ms                                                                 | 623 ms: 1.01x slower                                                   |
| sqlalchemy_declarative    | 129 ms                                                                 | 130 ms: 1.01x slower                                                   |
| html5lib                  | 64.2 ms                                                                | 64.9 ms: 1.01x slower                                                  |
| deltablue                 | 3.14 ms                                                                | 3.18 ms: 1.01x slower                                                  |
| json                      | 4.79 ms                                                                | 4.85 ms: 1.01x slower                                                  |
| tomli_loads               | 1.91 sec                                                               | 1.94 sec: 1.01x slower                                                 |
| pyflate                   | 449 ms                                                                 | 454 ms: 1.01x slower                                                   |
| dulwich_log               | 67.8 ms                                                                | 68.6 ms: 1.01x slower                                                  |
| raytrace                  | 285 ms                                                                 | 289 ms: 1.01x slower                                                   |
| crypto_pyaes              | 68.5 ms                                                                | 69.4 ms: 1.01x slower                                                  |
| richards                  | 37.4 ms                                                                | 37.9 ms: 1.01x slower                                                  |
| async_tree_io_tg          | 600 ms                                                                 | 609 ms: 1.01x slower                                                   |
| async_tree_none           | 267 ms                                                                 | 271 ms: 1.01x slower                                                   |
| sqlalchemy_imperative     | 16.6 ms                                                                | 16.9 ms: 1.02x slower                                                  |
| deepcopy_reduce           | 2.73 us                                                                | 2.78 us: 1.02x slower                                                  |
| go                        | 132 ms                                                                 | 135 ms: 1.02x slower                                                   |
| async_generators          | 445 ms                                                                 | 453 ms: 1.02x slower                                                   |
| json_dumps                | 11.1 ms                                                                | 11.3 ms: 1.02x slower                                                  |
| pprint_pformat            | 1.46 sec                                                               | 1.49 sec: 1.02x slower                                                 |
| thrift                    | 768 us                                                                 | 784 us: 1.02x slower                                                   |
| scimark_sparse_mat_mult   | 4.86 ms                                                                | 4.97 ms: 1.02x slower                                                  |
| coroutines                | 23.1 ms                                                                | 23.6 ms: 1.02x slower                                                  |
| chaos                     | 59.0 ms                                                                | 60.4 ms: 1.02x slower                                                  |
| scimark_fft               | 319 ms                                                                 | 327 ms: 1.02x slower                                                   |
| logging_silent            | 102 ns                                                                 | 106 ns: 1.04x slower                                                   |
| mdp                       | 2.58 sec                                                               | 2.70 sec: 1.04x slower                                                 |
| Geometric mean            | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (41): pickle_pure_python, xml_etree_generate, deepcopy_memo, spectral_norm, sqlite_synth, regex_compile, xml_etree_iterparse, sphinx, pylint, async_tree_cpu_io_mixed_tg, connected_components, nqueens, sympy_expand, subparsers, docutils, genshi_text, async_tree_memoization, pycparser, regex_dna, sympy_integrate, asyncio_websockets, bpe_tokeniser, xml_etree_parse, float, mako, k_core, pathlib, telco, logging_simple, many_optionals, django_template, logging_format, comprehensions, pprint_safe_repr, scimark_sor, bench_mp_pool, djangocms, deepcopy, typing_runtime_protocols, fannkuch, scimark_monte_carlo

- Geometric mean (including insignificant results): 1.004x slower

# HPT report

- Reliability score: 99.90% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x