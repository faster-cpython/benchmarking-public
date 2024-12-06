# Results vs. base

- fork: brandtbucher
- ref: justin_cold_19
- machine: linux-x86_64
- commit hash: b477ad2
- commit date: 2024-12-05
- overall geometric mean: 1.003x slower
- HPT reliability: 99.83%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241205-linux-x86_64-brandtbucher-justin_cold_19-3.14.0a2+-b477ad2 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 258 ms                                                                 | 259 ms: 1.00x slower                                                   |
| docutils       | 2.68 sec                                                               | 2.78 sec: 1.04x slower                                                 |
| sphinx         | 1.05 sec                                                               | 1.07 sec: 1.02x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                           |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241205-linux-x86_64-brandtbucher-justin_cold_19-3.14.0a2+-b477ad2 |
|---------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| coroutines                | 23.1 ms                                                                | 23.2 ms: 1.01x slower                                                  |
| async_tree_memoization_tg | 313 ms                                                                 | 315 ms: 1.01x slower                                                   |
| async_tree_io             | 616 ms                                                                 | 621 ms: 1.01x slower                                                   |
| async_tree_none_tg        | 249 ms                                                                 | 252 ms: 1.01x slower                                                   |
| async_tree_cpu_io_mixed   | 490 ms                                                                 | 494 ms: 1.01x slower                                                   |
| async_generators          | 445 ms                                                                 | 452 ms: 1.02x slower                                                   |
| async_tree_io_tg          | 600 ms                                                                 | 626 ms: 1.04x slower                                                   |
| Geometric mean            | (ref)                                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_memoization, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241205-linux-x86_64-brandtbucher-justin_cold_19-3.14.0a2+-b477ad2 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 82.8 ms                                                                | 86.0 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241205-linux-x86_64-brandtbucher-justin_cold_19-3.14.0a2+-b477ad2 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 25.0 ms                                                                | 24.9 ms: 1.00x faster                                                  |
| regex_effbot   | 3.20 ms                                                                | 3.25 ms: 1.02x slower                                                  |
| regex_dna      | 212 ms                                                                 | 216 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241205-linux-x86_64-brandtbucher-justin_cold_19-3.14.0a2+-b477ad2 |
|---------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_iterparse | 95.2 ms                                                                | 94.5 ms: 1.01x faster                                                  |
| json_dumps          | 11.1 ms                                                                | 11.0 ms: 1.01x faster                                                  |
| xml_etree_process   | 55.0 ms                                                                | 54.7 ms: 1.01x faster                                                  |
| json_loads          | 26.2 us                                                                | 26.0 us: 1.01x faster                                                  |
| tomli_loads         | 1.91 sec                                                               | 1.92 sec: 1.00x slower                                                 |
| Geometric mean      | (ref)                                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (4): unpickle_pure_python, xml_etree_parse, xml_etree_generate, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241205-linux-x86_64-brandtbucher-justin_cold_19-3.14.0a2+-b477ad2 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 7.04 ms                                                                | 7.04 ms: 1.00x slower                                                  |
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x slower                                                  |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241205-linux-x86_64-brandtbucher-justin_cold_19-3.14.0a2+-b477ad2 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml     | 57.7 ms                                                                | 57.1 ms: 1.01x faster                                                  |
| mako           | 10.1 ms                                                                | 9.98 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                 | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241205-linux-x86_64-brandtbucher-justin_cold_19-3.14.0a2+-b477ad2 |
|---------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| gc_traversal              | 5.01 ms                                                                | 4.74 ms: 1.06x faster                                                  |
| richards                  | 37.4 ms                                                                | 36.6 ms: 1.02x faster                                                  |
| fannkuch                  | 389 ms                                                                 | 381 ms: 1.02x faster                                                   |
| connected_components      | 438 ms                                                                 | 429 ms: 1.02x faster                                                   |
| deepcopy_reduce           | 2.73 us                                                                | 2.67 us: 1.02x faster                                                  |
| richards_super            | 43.7 ms                                                                | 43.1 ms: 1.01x faster                                                  |
| genshi_xml                | 57.7 ms                                                                | 57.1 ms: 1.01x faster                                                  |
| hexiom                    | 7.12 ms                                                                | 7.04 ms: 1.01x faster                                                  |
| json                      | 4.79 ms                                                                | 4.74 ms: 1.01x faster                                                  |
| create_gc_cycles          | 2.46 ms                                                                | 2.44 ms: 1.01x faster                                                  |
| deepcopy_memo             | 29.4 us                                                                | 29.1 us: 1.01x faster                                                  |
| mako                      | 10.1 ms                                                                | 9.98 ms: 1.01x faster                                                  |
| pyflate                   | 449 ms                                                                 | 445 ms: 1.01x faster                                                   |
| bpe_tokeniser             | 4.41 sec                                                               | 4.38 sec: 1.01x faster                                                 |
| xml_etree_iterparse       | 95.2 ms                                                                | 94.5 ms: 1.01x faster                                                  |
| json_dumps                | 11.1 ms                                                                | 11.0 ms: 1.01x faster                                                  |
| deepcopy                  | 269 us                                                                 | 268 us: 1.01x faster                                                   |
| xml_etree_process         | 55.0 ms                                                                | 54.7 ms: 1.01x faster                                                  |
| json_loads                | 26.2 us                                                                | 26.0 us: 1.01x faster                                                  |
| shortest_path             | 481 ms                                                                 | 479 ms: 1.00x faster                                                   |
| sympy_sum                 | 156 ms                                                                 | 156 ms: 1.00x faster                                                   |
| dulwich_log               | 67.8 ms                                                                | 67.6 ms: 1.00x faster                                                  |
| regex_v8                  | 25.0 ms                                                                | 24.9 ms: 1.00x faster                                                  |
| python_startup_no_site    | 7.04 ms                                                                | 7.04 ms: 1.00x slower                                                  |
| python_startup            | 12.8 ms                                                                | 12.8 ms: 1.00x slower                                                  |
| bench_thread_pool         | 872 us                                                                 | 875 us: 1.00x slower                                                   |
| 2to3                      | 258 ms                                                                 | 259 ms: 1.00x slower                                                   |
| sympy_str                 | 282 ms                                                                 | 283 ms: 1.00x slower                                                   |
| tomli_loads               | 1.91 sec                                                               | 1.92 sec: 1.00x slower                                                 |
| bench_mp_pool             | 80.9 ms                                                                | 81.3 ms: 1.00x slower                                                  |
| coroutines                | 23.1 ms                                                                | 23.2 ms: 1.01x slower                                                  |
| sqlalchemy_declarative    | 129 ms                                                                 | 130 ms: 1.01x slower                                                   |
| async_tree_memoization_tg | 313 ms                                                                 | 315 ms: 1.01x slower                                                   |
| raytrace                  | 285 ms                                                                 | 287 ms: 1.01x slower                                                   |
| async_tree_io             | 616 ms                                                                 | 621 ms: 1.01x slower                                                   |
| async_tree_none_tg        | 249 ms                                                                 | 252 ms: 1.01x slower                                                   |
| async_tree_cpu_io_mixed   | 490 ms                                                                 | 494 ms: 1.01x slower                                                   |
| go                        | 132 ms                                                                 | 134 ms: 1.01x slower                                                   |
| sqlalchemy_imperative     | 16.6 ms                                                                | 16.8 ms: 1.01x slower                                                  |
| typing_runtime_protocols  | 169 us                                                                 | 171 us: 1.01x slower                                                   |
| deltablue                 | 3.14 ms                                                                | 3.20 ms: 1.02x slower                                                  |
| regex_effbot              | 3.20 ms                                                                | 3.25 ms: 1.02x slower                                                  |
| logging_silent            | 102 ns                                                                 | 103 ns: 1.02x slower                                                   |
| async_generators          | 445 ms                                                                 | 452 ms: 1.02x slower                                                   |
| scimark_fft               | 319 ms                                                                 | 325 ms: 1.02x slower                                                   |
| thrift                    | 768 us                                                                 | 782 us: 1.02x slower                                                   |
| regex_dna                 | 212 ms                                                                 | 216 ms: 1.02x slower                                                   |
| chaos                     | 59.0 ms                                                                | 60.1 ms: 1.02x slower                                                  |
| sphinx                    | 1.05 sec                                                               | 1.07 sec: 1.02x slower                                                 |
| scimark_sparse_mat_mult   | 4.86 ms                                                                | 5.01 ms: 1.03x slower                                                  |
| sympy_expand              | 475 ms                                                                 | 490 ms: 1.03x slower                                                   |
| docutils                  | 2.68 sec                                                               | 2.78 sec: 1.04x slower                                                 |
| nbody                     | 82.8 ms                                                                | 86.0 ms: 1.04x slower                                                  |
| async_tree_io_tg          | 600 ms                                                                 | 626 ms: 1.04x slower                                                   |
| mdp                       | 2.58 sec                                                               | 2.74 sec: 1.06x slower                                                 |
| Geometric mean            | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (42): spectral_norm, k_core, unpickle_pure_python, meteor_contest, coverage, xml_etree_parse, comprehensions, logging_simple, django_template, generators, pprint_safe_repr, async_tree_cpu_io_mixed_tg, sqlglot_parse, telco, float, subparsers, sqlglot_optimize, scimark_monte_carlo, pidigits, html5lib, crypto_pyaes, sqlglot_transpile, scimark_lu, regex_compile, asyncio_websockets, sympy_integrate, xml_etree_generate, scimark_sor, pathlib, many_optionals, sqlglot_normalize, pickle_pure_python, nqueens, sqlite_synth, pprint_pformat, logging_format, pycparser, async_tree_memoization, async_tree_none, genshi_text, djangocms, pylint

- Geometric mean (including insignificant results): 1.003x slower

# HPT report

- Reliability score: 99.83% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x