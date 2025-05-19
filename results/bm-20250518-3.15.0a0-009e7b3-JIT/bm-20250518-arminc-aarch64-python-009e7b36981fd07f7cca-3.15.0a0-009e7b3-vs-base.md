# Results vs. base

- fork: python
- ref: 009e7b36981fd07f7cca
- machine: linux-aarch64
- commit hash: 009e7b3
- commit date: 2025-05-18
- overall geometric mean: 1.022x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250518-3.15.0a0-009e7b3/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json | results/bm-20250518-3.15.0a0-009e7b3-JIT/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 299 ms                                                                                                            | 314 ms: 1.05x slower                                                                                                  |
| docutils       | 2.94 sec                                                                                                          | 3.09 sec: 1.05x slower                                                                                                |
| sphinx         | 1.15 sec                                                                                                          | 1.19 sec: 1.04x slower                                                                                                |
| Geometric mean | (ref)                                                                                                             | 1.03x slower                                                                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250518-3.15.0a0-009e7b3/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json | results/bm-20250518-3.15.0a0-009e7b3-JIT/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| coroutines                 | 29.5 ms                                                                                                           | 29.9 ms: 1.01x slower                                                                                                 |
| async_tree_cpu_io_mixed_tg | 654 ms                                                                                                            | 667 ms: 1.02x slower                                                                                                  |
| asyncio_tcp_ssl            | 2.20 sec                                                                                                          | 2.25 sec: 1.02x slower                                                                                                |
| async_tree_memoization_tg  | 467 ms                                                                                                            | 479 ms: 1.03x slower                                                                                                  |
| async_tree_io_tg           | 903 ms                                                                                                            | 928 ms: 1.03x slower                                                                                                  |
| asyncio_tcp                | 539 ms                                                                                                            | 555 ms: 1.03x slower                                                                                                  |
| async_tree_none_tg         | 373 ms                                                                                                            | 386 ms: 1.03x slower                                                                                                  |
| async_tree_cpu_io_mixed    | 649 ms                                                                                                            | 675 ms: 1.04x slower                                                                                                  |
| async_tree_io              | 868 ms                                                                                                            | 908 ms: 1.05x slower                                                                                                  |
| async_tree_none            | 392 ms                                                                                                            | 411 ms: 1.05x slower                                                                                                  |
| async_tree_memoization     | 461 ms                                                                                                            | 489 ms: 1.06x slower                                                                                                  |
| async_generators           | 449 ms                                                                                                            | 485 ms: 1.08x slower                                                                                                  |
| Geometric mean             | (ref)                                                                                                             | 1.03x slower                                                                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250518-3.15.0a0-009e7b3/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json | results/bm-20250518-3.15.0a0-009e7b3-JIT/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| nbody          | 122 ms                                                                                                            | 118 ms: 1.04x faster                                                                                                  |
| float          | 86.4 ms                                                                                                           | 84.8 ms: 1.02x faster                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.02x faster                                                                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250518-3.15.0a0-009e7b3/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json | results/bm-20250518-3.15.0a0-009e7b3-JIT/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 231 ms                                                                                                            | 238 ms: 1.03x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.02x slower                                                                                                          |

Benchmark hidden because not significant (3): regex_v8, regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | results/bm-20250518-3.15.0a0-009e7b3/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json | results/bm-20250518-3.15.0a0-009e7b3-JIT/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json |
|---------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| tomli_loads         | 2.44 sec                                                                                                          | 2.35 sec: 1.04x faster                                                                                                |
| xml_etree_process   | 79.3 ms                                                                                                           | 77.8 ms: 1.02x faster                                                                                                 |
| xml_etree_iterparse | 141 ms                                                                                                            | 143 ms: 1.02x slower                                                                                                  |
| xml_etree_parse     | 178 ms                                                                                                            | 182 ms: 1.02x slower                                                                                                  |
| pickle              | 15.2 us                                                                                                           | 15.6 us: 1.03x slower                                                                                                 |
| pickle_pure_python  | 382 us                                                                                                            | 396 us: 1.04x slower                                                                                                  |
| Geometric mean      | (ref)                                                                                                             | 1.00x slower                                                                                                          |

Benchmark hidden because not significant (8): json_dumps, xml_etree_generate, json_loads, unpickle_pure_python, pickle_dict, pickle_list, unpickle, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250518-3.15.0a0-009e7b3/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json | results/bm-20250518-3.15.0a0-009e7b3-JIT/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 15.1 ms                                                                                                           | 15.3 ms: 1.01x slower                                                                                                 |
| python_startup_no_site | 8.62 ms                                                                                                           | 8.75 ms: 1.02x slower                                                                                                 |
| Geometric mean         | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark      | results/bm-20250518-3.15.0a0-009e7b3/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json | results/bm-20250518-3.15.0a0-009e7b3-JIT/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako           | 13.9 ms                                                                                                           | 13.5 ms: 1.04x faster                                                                                                 |
| genshi_xml     | 60.3 ms                                                                                                           | 63.0 ms: 1.04x slower                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                  | results/bm-20250518-3.15.0a0-009e7b3/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json | results/bm-20250518-3.15.0a0-009e7b3-JIT/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| richards_super             | 57.5 ms                                                                                                           | 51.9 ms: 1.11x faster                                                                                                 |
| richards                   | 50.5 ms                                                                                                           | 47.2 ms: 1.07x faster                                                                                                 |
| sqlite_synth               | 3.94 us                                                                                                           | 3.77 us: 1.04x faster                                                                                                 |
| tomli_loads                | 2.44 sec                                                                                                          | 2.35 sec: 1.04x faster                                                                                                |
| nbody                      | 122 ms                                                                                                            | 118 ms: 1.04x faster                                                                                                  |
| mako                       | 13.9 ms                                                                                                           | 13.5 ms: 1.04x faster                                                                                                 |
| bpe_tokeniser              | 5.56 sec                                                                                                          | 5.42 sec: 1.03x faster                                                                                                |
| xml_etree_process          | 79.3 ms                                                                                                           | 77.8 ms: 1.02x faster                                                                                                 |
| float                      | 86.4 ms                                                                                                           | 84.8 ms: 1.02x faster                                                                                                 |
| logging_format             | 8.27 us                                                                                                           | 8.36 us: 1.01x slower                                                                                                 |
| coroutines                 | 29.5 ms                                                                                                           | 29.9 ms: 1.01x slower                                                                                                 |
| connected_components       | 552 ms                                                                                                            | 559 ms: 1.01x slower                                                                                                  |
| python_startup             | 15.1 ms                                                                                                           | 15.3 ms: 1.01x slower                                                                                                 |
| python_startup_no_site     | 8.62 ms                                                                                                           | 8.75 ms: 1.02x slower                                                                                                 |
| xml_etree_iterparse        | 141 ms                                                                                                            | 143 ms: 1.02x slower                                                                                                  |
| sqlglot_v2_normalize       | 124 ms                                                                                                            | 127 ms: 1.02x slower                                                                                                  |
| async_tree_cpu_io_mixed_tg | 654 ms                                                                                                            | 667 ms: 1.02x slower                                                                                                  |
| mdp                        | 1.65 sec                                                                                                          | 1.68 sec: 1.02x slower                                                                                                |
| xml_etree_parse            | 178 ms                                                                                                            | 182 ms: 1.02x slower                                                                                                  |
| k_core                     | 2.80 sec                                                                                                          | 2.87 sec: 1.02x slower                                                                                                |
| asyncio_tcp_ssl            | 2.20 sec                                                                                                          | 2.25 sec: 1.02x slower                                                                                                |
| async_tree_memoization_tg  | 467 ms                                                                                                            | 479 ms: 1.03x slower                                                                                                  |
| async_tree_io_tg           | 903 ms                                                                                                            | 928 ms: 1.03x slower                                                                                                  |
| shortest_path              | 573 ms                                                                                                            | 588 ms: 1.03x slower                                                                                                  |
| pickle                     | 15.2 us                                                                                                           | 15.6 us: 1.03x slower                                                                                                 |
| regex_dna                  | 231 ms                                                                                                            | 238 ms: 1.03x slower                                                                                                  |
| asyncio_tcp                | 539 ms                                                                                                            | 555 ms: 1.03x slower                                                                                                  |
| deltablue                  | 3.74 ms                                                                                                           | 3.85 ms: 1.03x slower                                                                                                 |
| async_tree_none_tg         | 373 ms                                                                                                            | 386 ms: 1.03x slower                                                                                                  |
| sphinx                     | 1.15 sec                                                                                                          | 1.19 sec: 1.04x slower                                                                                                |
| raytrace                   | 322 ms                                                                                                            | 334 ms: 1.04x slower                                                                                                  |
| logging_silent             | 604 ns                                                                                                            | 626 ns: 1.04x slower                                                                                                  |
| pickle_pure_python         | 382 us                                                                                                            | 396 us: 1.04x slower                                                                                                  |
| bench_thread_pool          | 1.35 ms                                                                                                           | 1.40 ms: 1.04x slower                                                                                                 |
| async_tree_cpu_io_mixed    | 649 ms                                                                                                            | 675 ms: 1.04x slower                                                                                                  |
| sympy_integrate            | 20.2 ms                                                                                                           | 21.1 ms: 1.04x slower                                                                                                 |
| pyflate                    | 525 ms                                                                                                            | 548 ms: 1.04x slower                                                                                                  |
| genshi_xml                 | 60.3 ms                                                                                                           | 63.0 ms: 1.04x slower                                                                                                 |
| async_tree_io              | 868 ms                                                                                                            | 908 ms: 1.05x slower                                                                                                  |
| async_tree_none            | 392 ms                                                                                                            | 411 ms: 1.05x slower                                                                                                  |
| meteor_contest             | 114 ms                                                                                                            | 120 ms: 1.05x slower                                                                                                  |
| sqlglot_v2_transpile       | 1.74 ms                                                                                                           | 1.83 ms: 1.05x slower                                                                                                 |
| 2to3                       | 299 ms                                                                                                            | 314 ms: 1.05x slower                                                                                                  |
| docutils                   | 2.94 sec                                                                                                          | 3.09 sec: 1.05x slower                                                                                                |
| fannkuch                   | 466 ms                                                                                                            | 492 ms: 1.05x slower                                                                                                  |
| async_tree_memoization     | 461 ms                                                                                                            | 489 ms: 1.06x slower                                                                                                  |
| many_optionals             | 878 us                                                                                                            | 940 us: 1.07x slower                                                                                                  |
| async_generators           | 449 ms                                                                                                            | 485 ms: 1.08x slower                                                                                                  |
| dulwich_log                | 54.7 ms                                                                                                           | 59.2 ms: 1.08x slower                                                                                                 |
| sqlglot_v2_parse           | 1.41 ms                                                                                                           | 1.54 ms: 1.09x slower                                                                                                 |
| hexiom                     | 7.25 ms                                                                                                           | 7.90 ms: 1.09x slower                                                                                                 |
| pylint                     | 307 ms                                                                                                            | 335 ms: 1.09x slower                                                                                                  |
| crypto_pyaes               | 86.2 ms                                                                                                           | 94.4 ms: 1.10x slower                                                                                                 |
| pycparser                  | 1.26 sec                                                                                                          | 1.39 sec: 1.10x slower                                                                                                |
| comprehensions             | 21.2 us                                                                                                           | 23.6 us: 1.12x slower                                                                                                 |
| pprint_safe_repr           | 905 ms                                                                                                            | 1.14 sec: 1.26x slower                                                                                                |
| pprint_pformat             | 1.85 sec                                                                                                          | 2.35 sec: 1.27x slower                                                                                                |
| go                         | 131 ms                                                                                                            | 168 ms: 1.28x slower                                                                                                  |
| unpack_sequence            | 50.8 ns                                                                                                           | 84.8 ns: 1.67x slower                                                                                                 |
| Geometric mean             | (ref)                                                                                                             | 1.03x slower                                                                                                          |

Benchmark hidden because not significant (43): bench_mp_pool, html5lib, json_dumps, xml_etree_generate, scimark_fft, generators, scimark_sparse_mat_mult, json_loads, json, deepcopy_reduce, thrift, deepcopy_memo, unpickle_pure_python, pidigits, pickle_dict, scimark_lu, deepcopy, django_template, pickle_list, sympy_str, coverage, create_gc_cycles, asyncio_websockets, regex_v8, telco, gc_traversal, scimark_sor, regex_effbot, chaos, logging_simple, subparsers, spectral_norm, sympy_expand, pathlib, typing_runtime_protocols, regex_compile, sympy_sum, sqlglot_v2_optimize, unpickle, nqueens, genshi_text, unpickle_list, scimark_monte_carlo

- Geometric mean (including insignificant results): 1.022x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.02x