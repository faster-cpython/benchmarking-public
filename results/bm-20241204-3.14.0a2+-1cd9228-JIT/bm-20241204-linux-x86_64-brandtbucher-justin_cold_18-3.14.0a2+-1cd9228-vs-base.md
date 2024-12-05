# Results vs. base

- fork: brandtbucher
- ref: justin_cold_18
- machine: linux-x86_64
- commit hash: 1cd9228
- commit date: 2024-12-04
- overall geometric mean: 1.004x slower
- HPT reliability: 99.66%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241204-linux-x86_64-brandtbucher-justin_cold_18-3.14.0a2+-1cd9228 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 258 ms                                                                 | 260 ms: 1.01x slower                                                   |
| docutils       | 2.68 sec                                                               | 2.72 sec: 1.02x slower                                                 |
| html5lib       | 64.2 ms                                                                | 65.2 ms: 1.01x slower                                                  |
| sphinx         | 1.05 sec                                                               | 1.06 sec: 1.01x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241204-linux-x86_64-brandtbucher-justin_cold_18-3.14.0a2+-1cd9228 |
|---------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_cpu_io_mixed   | 490 ms                                                                 | 493 ms: 1.01x slower                                                   |
| async_tree_memoization_tg | 313 ms                                                                 | 316 ms: 1.01x slower                                                   |
| async_tree_none           | 267 ms                                                                 | 271 ms: 1.01x slower                                                   |
| async_tree_io             | 616 ms                                                                 | 626 ms: 1.02x slower                                                   |
| async_generators          | 445 ms                                                                 | 456 ms: 1.02x slower                                                   |
| coroutines                | 23.1 ms                                                                | 23.8 ms: 1.03x slower                                                  |
| async_tree_io_tg          | 600 ms                                                                 | 628 ms: 1.05x slower                                                   |
| Geometric mean            | (ref)                                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_none_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241204-linux-x86_64-brandtbucher-justin_cold_18-3.14.0a2+-1cd9228 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 82.8 ms                                                                | 81.3 ms: 1.02x faster                                                  |
| pidigits       | 186 ms                                                                 | 188 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241204-linux-x86_64-brandtbucher-justin_cold_18-3.14.0a2+-1cd9228 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 130 ms                                                                 | 128 ms: 1.01x faster                                                   |
| regex_v8       | 25.0 ms                                                                | 24.9 ms: 1.00x faster                                                  |
| regex_dna      | 212 ms                                                                 | 215 ms: 1.02x slower                                                   |
| regex_effbot   | 3.20 ms                                                                | 3.26 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241204-linux-x86_64-brandtbucher-justin_cold_18-3.14.0a2+-1cd9228 |
|---------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse     | 138 ms                                                                 | 137 ms: 1.01x faster                                                   |
| xml_etree_iterparse | 95.2 ms                                                                | 95.0 ms: 1.00x faster                                                  |
| tomli_loads         | 1.91 sec                                                               | 1.93 sec: 1.01x slower                                                 |
| json_dumps          | 11.1 ms                                                                | 11.2 ms: 1.01x slower                                                  |
| Geometric mean      | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (5): pickle_pure_python, xml_etree_generate, json_loads, xml_etree_process, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241204-linux-x86_64-brandtbucher-justin_cold_18-3.14.0a2+-1cd9228 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 7.04 ms                                                                | 7.08 ms: 1.01x slower                                                  |
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241204-linux-x86_64-brandtbucher-justin_cold_18-3.14.0a2+-1cd9228 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml     | 57.7 ms                                                                | 56.7 ms: 1.02x faster                                                  |
| mako           | 10.1 ms                                                                | 10.1 ms: 1.00x slower                                                  |
| genshi_text    | 23.9 ms                                                                | 24.2 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                 | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241204-linux-x86_64-brandtbucher-justin_cold_18-3.14.0a2+-1cd9228 |
|---------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| scimark_sparse_mat_mult   | 4.86 ms                                                                | 4.72 ms: 1.03x faster                                                  |
| deepcopy_reduce           | 2.73 us                                                                | 2.67 us: 1.02x faster                                                  |
| richards                  | 37.4 ms                                                                | 36.6 ms: 1.02x faster                                                  |
| nbody                     | 82.8 ms                                                                | 81.3 ms: 1.02x faster                                                  |
| connected_components      | 438 ms                                                                 | 431 ms: 1.02x faster                                                   |
| genshi_xml                | 57.7 ms                                                                | 56.7 ms: 1.02x faster                                                  |
| richards_super            | 43.7 ms                                                                | 43.1 ms: 1.02x faster                                                  |
| deepcopy                  | 269 us                                                                 | 266 us: 1.01x faster                                                   |
| hexiom                    | 7.12 ms                                                                | 7.04 ms: 1.01x faster                                                  |
| gc_traversal              | 5.01 ms                                                                | 4.96 ms: 1.01x faster                                                  |
| meteor_contest            | 110 ms                                                                 | 109 ms: 1.01x faster                                                   |
| pprint_safe_repr          | 718 ms                                                                 | 711 ms: 1.01x faster                                                   |
| xml_etree_parse           | 138 ms                                                                 | 137 ms: 1.01x faster                                                   |
| regex_compile             | 130 ms                                                                 | 128 ms: 1.01x faster                                                   |
| bpe_tokeniser             | 4.41 sec                                                               | 4.38 sec: 1.01x faster                                                 |
| xml_etree_iterparse       | 95.2 ms                                                                | 95.0 ms: 1.00x faster                                                  |
| regex_v8                  | 25.0 ms                                                                | 24.9 ms: 1.00x faster                                                  |
| mako                      | 10.1 ms                                                                | 10.1 ms: 1.00x slower                                                  |
| bench_thread_pool         | 872 us                                                                 | 874 us: 1.00x slower                                                   |
| create_gc_cycles          | 2.46 ms                                                                | 2.47 ms: 1.00x slower                                                  |
| scimark_fft               | 319 ms                                                                 | 321 ms: 1.00x slower                                                   |
| python_startup_no_site    | 7.04 ms                                                                | 7.08 ms: 1.01x slower                                                  |
| pathlib                   | 16.2 ms                                                                | 16.3 ms: 1.01x slower                                                  |
| sqlglot_parse             | 1.32 ms                                                                | 1.32 ms: 1.01x slower                                                  |
| python_startup            | 12.8 ms                                                                | 12.8 ms: 1.01x slower                                                  |
| sqlalchemy_declarative    | 129 ms                                                                 | 130 ms: 1.01x slower                                                   |
| sqlglot_transpile         | 1.63 ms                                                                | 1.64 ms: 1.01x slower                                                  |
| pidigits                  | 186 ms                                                                 | 188 ms: 1.01x slower                                                   |
| bench_mp_pool             | 80.9 ms                                                                | 81.5 ms: 1.01x slower                                                  |
| sympy_str                 | 282 ms                                                                 | 284 ms: 1.01x slower                                                   |
| nqueens                   | 89.9 ms                                                                | 90.6 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed   | 490 ms                                                                 | 493 ms: 1.01x slower                                                   |
| sphinx                    | 1.05 sec                                                               | 1.06 sec: 1.01x slower                                                 |
| raytrace                  | 285 ms                                                                 | 288 ms: 1.01x slower                                                   |
| sqlalchemy_imperative     | 16.6 ms                                                                | 16.7 ms: 1.01x slower                                                  |
| tomli_loads               | 1.91 sec                                                               | 1.93 sec: 1.01x slower                                                 |
| scimark_monte_carlo       | 64.2 ms                                                                | 64.9 ms: 1.01x slower                                                  |
| 2to3                      | 258 ms                                                                 | 260 ms: 1.01x slower                                                   |
| logging_silent            | 102 ns                                                                 | 103 ns: 1.01x slower                                                   |
| deltablue                 | 3.14 ms                                                                | 3.18 ms: 1.01x slower                                                  |
| json_dumps                | 11.1 ms                                                                | 11.2 ms: 1.01x slower                                                  |
| async_tree_memoization_tg | 313 ms                                                                 | 316 ms: 1.01x slower                                                   |
| scimark_lu                | 115 ms                                                                 | 116 ms: 1.01x slower                                                   |
| scimark_sor               | 119 ms                                                                 | 120 ms: 1.01x slower                                                   |
| async_tree_none           | 267 ms                                                                 | 271 ms: 1.01x slower                                                   |
| genshi_text               | 23.9 ms                                                                | 24.2 ms: 1.01x slower                                                  |
| telco                     | 7.52 ms                                                                | 7.63 ms: 1.01x slower                                                  |
| chaos                     | 59.0 ms                                                                | 59.9 ms: 1.01x slower                                                  |
| html5lib                  | 64.2 ms                                                                | 65.2 ms: 1.01x slower                                                  |
| regex_dna                 | 212 ms                                                                 | 215 ms: 1.02x slower                                                   |
| async_tree_io             | 616 ms                                                                 | 626 ms: 1.02x slower                                                   |
| docutils                  | 2.68 sec                                                               | 2.72 sec: 1.02x slower                                                 |
| regex_effbot              | 3.20 ms                                                                | 3.26 ms: 1.02x slower                                                  |
| go                        | 132 ms                                                                 | 135 ms: 1.02x slower                                                   |
| async_generators          | 445 ms                                                                 | 456 ms: 1.02x slower                                                   |
| coroutines                | 23.1 ms                                                                | 23.8 ms: 1.03x slower                                                  |
| thrift                    | 768 us                                                                 | 791 us: 1.03x slower                                                   |
| sympy_expand              | 475 ms                                                                 | 490 ms: 1.03x slower                                                   |
| mdp                       | 2.58 sec                                                               | 2.70 sec: 1.05x slower                                                 |
| async_tree_io_tg          | 600 ms                                                                 | 628 ms: 1.05x slower                                                   |
| Geometric mean            | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (37): fannkuch, k_core, coverage, json, logging_format, djangocms, async_tree_cpu_io_mixed_tg, pickle_pure_python, float, logging_simple, xml_etree_generate, pprint_pformat, deepcopy_memo, subparsers, many_optionals, sympy_sum, spectral_norm, crypto_pyaes, dulwich_log, shortest_path, sqlglot_normalize, asyncio_websockets, django_template, json_loads, sqlglot_optimize, sqlite_synth, pyflate, generators, sympy_integrate, pycparser, xml_etree_process, comprehensions, async_tree_none_tg, async_tree_memoization, unpickle_pure_python, typing_runtime_protocols, pylint

- Geometric mean (including insignificant results): 1.004x slower

# HPT report

- Reliability score: 99.66% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x