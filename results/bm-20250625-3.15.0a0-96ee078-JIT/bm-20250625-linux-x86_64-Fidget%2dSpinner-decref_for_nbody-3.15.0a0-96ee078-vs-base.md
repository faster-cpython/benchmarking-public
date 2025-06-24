# Results vs. base

- fork: Fidget-Spinner
- ref: decref_for_nbody
- machine: linux-x86_64
- commit hash: 96ee078
- commit date: 2025-06-25
- overall geometric mean: 1.001x faster
- HPT reliability: 67.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250624-linux-x86_64-python-bda121862e7d7f4684d9-3.15.0a0-bda1218 | bm-20250625-linux-x86_64-Fidget%2dSpinner-decref_for_nbody-3.15.0a0-96ee078 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                                | 260 ms: 1.00x slower                                                        |
| docutils       | 2.64 sec                                                              | 2.65 sec: 1.00x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250624-linux-x86_64-python-bda121862e7d7f4684d9-3.15.0a0-bda1218 | bm-20250625-linux-x86_64-Fidget%2dSpinner-decref_for_nbody-3.15.0a0-96ee078 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 264 ms                                                                | 260 ms: 1.02x faster                                                        |
| async_tree_none_tg         | 252 ms                                                                | 248 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed    | 501 ms                                                                | 494 ms: 1.01x faster                                                        |
| async_tree_cpu_io_mixed_tg | 494 ms                                                                | 488 ms: 1.01x faster                                                        |
| async_tree_io              | 605 ms                                                                | 599 ms: 1.01x faster                                                        |
| async_tree_memoization     | 315 ms                                                                | 312 ms: 1.01x faster                                                        |
| async_generators           | 428 ms                                                                | 430 ms: 1.00x slower                                                        |
| coroutines                 | 24.7 ms                                                               | 25.5 ms: 1.03x slower                                                       |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                                |

Benchmark hidden because not significant (3): async_tree_io_tg, async_tree_memoization_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250624-linux-x86_64-python-bda121862e7d7f4684d9-3.15.0a0-bda1218 | bm-20250625-linux-x86_64-Fidget%2dSpinner-decref_for_nbody-3.15.0a0-96ee078 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 96.9 ms                                                               | 90.3 ms: 1.07x faster                                                       |
| pidigits       | 188 ms                                                                | 188 ms: 1.00x faster                                                        |
| float          | 65.0 ms                                                               | 65.5 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250624-linux-x86_64-python-bda121862e7d7f4684d9-3.15.0a0-bda1218 | bm-20250625-linux-x86_64-Fidget%2dSpinner-decref_for_nbody-3.15.0a0-96ee078 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 208 ms                                                                | 210 ms: 1.01x slower                                                        |
| regex_effbot   | 3.25 ms                                                               | 3.38 ms: 1.04x slower                                                       |
| regex_v8       | 22.9 ms                                                               | 24.0 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                                |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark         | bm-20250624-linux-x86_64-python-bda121862e7d7f4684d9-3.15.0a0-bda1218 | bm-20250625-linux-x86_64-Fidget%2dSpinner-decref_for_nbody-3.15.0a0-96ee078 |
|-------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads       | 1.85 sec                                                              | 1.83 sec: 1.01x faster                                                      |
| xml_etree_process | 56.5 ms                                                               | 56.0 ms: 1.01x faster                                                       |
| json_loads        | 28.4 us                                                               | 28.8 us: 1.01x slower                                                       |
| Geometric mean    | (ref)                                                                 | 1.00x faster                                                                |

Benchmark hidden because not significant (6): xml_etree_iterparse, xml_etree_generate, unpickle_pure_python, xml_etree_parse, json_dumps, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250624-linux-x86_64-python-bda121862e7d7f4684d9-3.15.0a0-bda1218 | bm-20250625-linux-x86_64-Fidget%2dSpinner-decref_for_nbody-3.15.0a0-96ee078 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                               | 6.97 ms: 1.00x slower                                                       |
| python_startup         | 12.2 ms                                                               | 12.2 ms: 1.00x slower                                                       |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250624-linux-x86_64-python-bda121862e7d7f4684d9-3.15.0a0-bda1218 | bm-20250625-linux-x86_64-Fidget%2dSpinner-decref_for_nbody-3.15.0a0-96ee078 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 21.9 ms                                                               | 21.5 ms: 1.02x faster                                                       |
| django_template | 32.0 ms                                                               | 32.7 ms: 1.02x slower                                                       |
| genshi_xml      | 50.1 ms                                                               | 51.2 ms: 1.02x slower                                                       |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20250624-linux-x86_64-python-bda121862e7d7f4684d9-3.15.0a0-bda1218 | bm-20250625-linux-x86_64-Fidget%2dSpinner-decref_for_nbody-3.15.0a0-96ee078 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody                      | 96.9 ms                                                               | 90.3 ms: 1.07x faster                                                       |
| gc_traversal               | 5.09 ms                                                               | 4.75 ms: 1.07x faster                                                       |
| scimark_sparse_mat_mult    | 5.06 ms                                                               | 4.82 ms: 1.05x faster                                                       |
| djangocms                  | 23.1 us                                                               | 22.3 us: 1.03x faster                                                       |
| shortest_path              | 505 ms                                                                | 495 ms: 1.02x faster                                                        |
| genshi_text                | 21.9 ms                                                               | 21.5 ms: 1.02x faster                                                       |
| async_tree_none            | 264 ms                                                                | 260 ms: 1.02x faster                                                        |
| async_tree_none_tg         | 252 ms                                                                | 248 ms: 1.02x faster                                                        |
| go                         | 122 ms                                                                | 120 ms: 1.01x faster                                                        |
| meteor_contest             | 108 ms                                                                | 106 ms: 1.01x faster                                                        |
| sqlglot_v2_parse           | 1.27 ms                                                               | 1.25 ms: 1.01x faster                                                       |
| crypto_pyaes               | 76.6 ms                                                               | 75.5 ms: 1.01x faster                                                       |
| async_tree_cpu_io_mixed    | 501 ms                                                                | 494 ms: 1.01x faster                                                        |
| telco                      | 7.74 ms                                                               | 7.65 ms: 1.01x faster                                                       |
| scimark_monte_carlo        | 66.0 ms                                                               | 65.2 ms: 1.01x faster                                                       |
| comprehensions             | 17.2 us                                                               | 17.0 us: 1.01x faster                                                       |
| async_tree_cpu_io_mixed_tg | 494 ms                                                                | 488 ms: 1.01x faster                                                        |
| tomli_loads                | 1.85 sec                                                              | 1.83 sec: 1.01x faster                                                      |
| fannkuch                   | 401 ms                                                                | 397 ms: 1.01x faster                                                        |
| async_tree_io              | 605 ms                                                                | 599 ms: 1.01x faster                                                        |
| scimark_sor                | 119 ms                                                                | 118 ms: 1.01x faster                                                        |
| xml_etree_process          | 56.5 ms                                                               | 56.0 ms: 1.01x faster                                                       |
| async_tree_memoization     | 315 ms                                                                | 312 ms: 1.01x faster                                                        |
| logging_silent             | 477 ns                                                                | 473 ns: 1.01x faster                                                        |
| scimark_lu                 | 118 ms                                                                | 117 ms: 1.01x faster                                                        |
| pidigits                   | 188 ms                                                                | 188 ms: 1.00x faster                                                        |
| python_startup_no_site     | 6.96 ms                                                               | 6.97 ms: 1.00x slower                                                       |
| python_startup             | 12.2 ms                                                               | 12.2 ms: 1.00x slower                                                       |
| create_gc_cycles           | 2.59 ms                                                               | 2.60 ms: 1.00x slower                                                       |
| docutils                   | 2.64 sec                                                              | 2.65 sec: 1.00x slower                                                      |
| async_generators           | 428 ms                                                                | 430 ms: 1.00x slower                                                        |
| 2to3                       | 259 ms                                                                | 260 ms: 1.00x slower                                                        |
| sympy_integrate            | 19.3 ms                                                               | 19.4 ms: 1.01x slower                                                       |
| many_optionals             | 975 us                                                                | 981 us: 1.01x slower                                                        |
| sympy_sum                  | 149 ms                                                                | 150 ms: 1.01x slower                                                        |
| float                      | 65.0 ms                                                               | 65.5 ms: 1.01x slower                                                       |
| sympy_expand               | 465 ms                                                                | 469 ms: 1.01x slower                                                        |
| chaos                      | 60.1 ms                                                               | 60.6 ms: 1.01x slower                                                       |
| deepcopy                   | 255 us                                                                | 257 us: 1.01x slower                                                        |
| regex_dna                  | 208 ms                                                                | 210 ms: 1.01x slower                                                        |
| raytrace                   | 271 ms                                                                | 273 ms: 1.01x slower                                                        |
| sympy_str                  | 270 ms                                                                | 273 ms: 1.01x slower                                                        |
| subparsers                 | 23.5 ms                                                               | 23.8 ms: 1.01x slower                                                       |
| mdp                        | 1.23 sec                                                              | 1.24 sec: 1.01x slower                                                      |
| json_loads                 | 28.4 us                                                               | 28.8 us: 1.01x slower                                                       |
| spectral_norm              | 92.8 ms                                                               | 94.2 ms: 1.01x slower                                                       |
| logging_format             | 6.67 us                                                               | 6.77 us: 1.02x slower                                                       |
| pycparser                  | 1.15 sec                                                              | 1.17 sec: 1.02x slower                                                      |
| django_template            | 32.0 ms                                                               | 32.7 ms: 1.02x slower                                                       |
| genshi_xml                 | 50.1 ms                                                               | 51.2 ms: 1.02x slower                                                       |
| pyflate                    | 413 ms                                                                | 423 ms: 1.02x slower                                                        |
| coroutines                 | 24.7 ms                                                               | 25.5 ms: 1.03x slower                                                       |
| regex_effbot               | 3.25 ms                                                               | 3.38 ms: 1.04x slower                                                       |
| regex_v8                   | 22.9 ms                                                               | 24.0 ms: 1.05x slower                                                       |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                                |

Benchmark hidden because not significant (39): async_tree_io_tg, async_tree_memoization_tg, k_core, nqueens, pprint_pformat, pprint_safe_repr, pathlib, richards, json, thrift, hexiom, xml_etree_iterparse, xml_etree_generate, unpickle_pure_python, sqlglot_v2_transpile, sqlglot_v2_normalize, deepcopy_reduce, sqlite_synth, connected_components, xml_etree_parse, coverage, json_dumps, scimark_fft, deltablue, mako, sqlglot_v2_optimize, asyncio_websockets, regex_compile, typing_runtime_protocols, richards_super, deepcopy_memo, bpe_tokeniser, pylint, dulwich_log, generators, html5lib, pickle_pure_python, logging_simple, sphinx

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 67.98% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x