# Results vs. base

- fork: python
- ref: 61b35f74aa4a6ac60663
- machine: linux-aarch64
- commit hash: 61b35f7
- commit date: 2025-01-18
- overall geometric mean: 1.072x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250118-3.14.0a4+-61b35f7/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7.json | results/bm-20250118-3.14.0a4+-61b35f7-JIT/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 306 ms                                                                                                              | 329 ms: 1.07x slower                                                                                                    |
| docutils       | 3.01 sec                                                                                                            | 3.24 sec: 1.08x slower                                                                                                  |
| html5lib       | 62.9 ms                                                                                                             | 70.5 ms: 1.12x slower                                                                                                   |
| sphinx         | 1.18 sec                                                                                                            | 1.26 sec: 1.07x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                               | 1.08x slower                                                                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | results/bm-20250118-3.14.0a4+-61b35f7/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7.json | results/bm-20250118-3.14.0a4+-61b35f7-JIT/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7.json |
|-------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| async_tree_io           | 895 ms                                                                                                              | 921 ms: 1.03x slower                                                                                                    |
| asyncio_tcp_ssl         | 2.26 sec                                                                                                            | 2.33 sec: 1.03x slower                                                                                                  |
| async_tree_cpu_io_mixed | 678 ms                                                                                                              | 701 ms: 1.03x slower                                                                                                    |
| async_tree_none_tg      | 374 ms                                                                                                              | 389 ms: 1.04x slower                                                                                                    |
| asyncio_tcp             | 570 ms                                                                                                              | 594 ms: 1.04x slower                                                                                                    |
| async_tree_none         | 385 ms                                                                                                              | 406 ms: 1.05x slower                                                                                                    |
| async_tree_memoization  | 490 ms                                                                                                              | 519 ms: 1.06x slower                                                                                                    |
| async_generators        | 454 ms                                                                                                              | 497 ms: 1.09x slower                                                                                                    |
| Geometric mean          | (ref)                                                                                                               | 1.03x slower                                                                                                            |

Benchmark hidden because not significant (5): coroutines, asyncio_websockets, async_tree_memoization_tg, async_tree_io_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250118-3.14.0a4+-61b35f7/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7.json | results/bm-20250118-3.14.0a4+-61b35f7-JIT/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 130 ms                                                                                                              | 144 ms: 1.11x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.02x slower                                                                                                            |

Benchmark hidden because not significant (3): regex_dna, regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

Benchmark hidden because not significant (14): xml_etree_generate, pickle, xml_etree_parse, unpickle_pure_python, json_loads, tomli_loads, xml_etree_process, pickle_dict, unpickle_list, xml_etree_iterparse, pickle_list, unpickle, json_dumps, pickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250118-3.14.0a4+-61b35f7/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7.json | results/bm-20250118-3.14.0a4+-61b35f7-JIT/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7.json |
|-----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| django_template | 39.4 ms                                                                                                             | 48.8 ms: 1.24x slower                                                                                                   |
| genshi_text     | 27.1 ms                                                                                                             | 33.7 ms: 1.24x slower                                                                                                   |
| genshi_xml      | 61.6 ms                                                                                                             | 87.0 ms: 1.41x slower                                                                                                   |
| Geometric mean  | (ref)                                                                                                               | 1.21x slower                                                                                                            |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | results/bm-20250118-3.14.0a4+-61b35f7/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7.json | results/bm-20250118-3.14.0a4+-61b35f7-JIT/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7.json |
|--------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool            | 7.08 sec                                                                                                            | 2.21 sec: 3.20x faster                                                                                                  |
| bpe_tokeniser            | 5.68 sec                                                                                                            | 5.77 sec: 1.02x slower                                                                                                  |
| async_tree_io            | 895 ms                                                                                                              | 921 ms: 1.03x slower                                                                                                    |
| asyncio_tcp_ssl          | 2.26 sec                                                                                                            | 2.33 sec: 1.03x slower                                                                                                  |
| sqlalchemy_declarative   | 148 ms                                                                                                              | 153 ms: 1.03x slower                                                                                                    |
| async_tree_cpu_io_mixed  | 678 ms                                                                                                              | 701 ms: 1.03x slower                                                                                                    |
| pathlib                  | 21.8 ms                                                                                                             | 22.7 ms: 1.04x slower                                                                                                   |
| k_core                   | 2.86 sec                                                                                                            | 2.98 sec: 1.04x slower                                                                                                  |
| async_tree_none_tg       | 374 ms                                                                                                              | 389 ms: 1.04x slower                                                                                                    |
| asyncio_tcp              | 570 ms                                                                                                              | 594 ms: 1.04x slower                                                                                                    |
| scimark_sor              | 150 ms                                                                                                              | 157 ms: 1.04x slower                                                                                                    |
| mdp                      | 3.42 sec                                                                                                            | 3.59 sec: 1.05x slower                                                                                                  |
| telco                    | 9.53 ms                                                                                                             | 10.0 ms: 1.05x slower                                                                                                   |
| deepcopy_memo            | 41.0 us                                                                                                             | 43.2 us: 1.05x slower                                                                                                   |
| async_tree_none          | 385 ms                                                                                                              | 406 ms: 1.05x slower                                                                                                    |
| async_tree_memoization   | 490 ms                                                                                                              | 519 ms: 1.06x slower                                                                                                    |
| subparsers               | 26.0 ms                                                                                                             | 27.6 ms: 1.06x slower                                                                                                   |
| sympy_integrate          | 21.7 ms                                                                                                             | 23.0 ms: 1.06x slower                                                                                                   |
| json                     | 5.80 ms                                                                                                             | 6.17 ms: 1.06x slower                                                                                                   |
| fannkuch                 | 484 ms                                                                                                              | 515 ms: 1.06x slower                                                                                                    |
| sphinx                   | 1.18 sec                                                                                                            | 1.26 sec: 1.07x slower                                                                                                  |
| typing_runtime_protocols | 207 us                                                                                                              | 222 us: 1.07x slower                                                                                                    |
| 2to3                     | 306 ms                                                                                                              | 329 ms: 1.07x slower                                                                                                    |
| docutils                 | 3.01 sec                                                                                                            | 3.24 sec: 1.08x slower                                                                                                  |
| logging_silent           | 139 ns                                                                                                              | 150 ns: 1.08x slower                                                                                                    |
| sqlglot_normalize        | 131 ms                                                                                                              | 142 ms: 1.09x slower                                                                                                    |
| richards                 | 51.9 ms                                                                                                             | 56.3 ms: 1.09x slower                                                                                                   |
| sqlalchemy_imperative    | 15.6 ms                                                                                                             | 17.0 ms: 1.09x slower                                                                                                   |
| async_generators         | 454 ms                                                                                                              | 497 ms: 1.09x slower                                                                                                    |
| pylint                   | 318 ms                                                                                                              | 349 ms: 1.10x slower                                                                                                    |
| raytrace                 | 315 ms                                                                                                              | 347 ms: 1.10x slower                                                                                                    |
| pyflate                  | 567 ms                                                                                                              | 624 ms: 1.10x slower                                                                                                    |
| sympy_str                | 272 ms                                                                                                              | 301 ms: 1.11x slower                                                                                                    |
| sqlglot_optimize         | 63.4 ms                                                                                                             | 70.2 ms: 1.11x slower                                                                                                   |
| spectral_norm            | 121 ms                                                                                                              | 135 ms: 1.11x slower                                                                                                    |
| regex_compile            | 130 ms                                                                                                              | 144 ms: 1.11x slower                                                                                                    |
| sympy_sum                | 146 ms                                                                                                              | 162 ms: 1.11x slower                                                                                                    |
| crypto_pyaes             | 84.4 ms                                                                                                             | 94.0 ms: 1.11x slower                                                                                                   |
| sympy_expand             | 471 ms                                                                                                              | 526 ms: 1.12x slower                                                                                                    |
| sqlglot_parse            | 1.45 ms                                                                                                             | 1.63 ms: 1.12x slower                                                                                                   |
| html5lib                 | 62.9 ms                                                                                                             | 70.5 ms: 1.12x slower                                                                                                   |
| comprehensions           | 22.0 us                                                                                                             | 24.8 us: 1.13x slower                                                                                                   |
| deltablue                | 3.86 ms                                                                                                             | 4.38 ms: 1.13x slower                                                                                                   |
| scimark_lu               | 137 ms                                                                                                              | 157 ms: 1.14x slower                                                                                                    |
| logging_format           | 7.75 us                                                                                                             | 8.91 us: 1.15x slower                                                                                                   |
| logging_simple           | 6.99 us                                                                                                             | 8.19 us: 1.17x slower                                                                                                   |
| deepcopy                 | 349 us                                                                                                              | 411 us: 1.18x slower                                                                                                    |
| pycparser                | 1.29 sec                                                                                                            | 1.54 sec: 1.19x slower                                                                                                  |
| dulwich_log              | 61.4 ms                                                                                                             | 73.7 ms: 1.20x slower                                                                                                   |
| deepcopy_reduce          | 3.55 us                                                                                                             | 4.26 us: 1.20x slower                                                                                                   |
| chaos                    | 67.8 ms                                                                                                             | 82.3 ms: 1.21x slower                                                                                                   |
| many_optionals           | 699 us                                                                                                              | 861 us: 1.23x slower                                                                                                    |
| django_template          | 39.4 ms                                                                                                             | 48.8 ms: 1.24x slower                                                                                                   |
| genshi_text              | 27.1 ms                                                                                                             | 33.7 ms: 1.24x slower                                                                                                   |
| nqueens                  | 99.7 ms                                                                                                             | 126 ms: 1.26x slower                                                                                                    |
| hexiom                   | 7.55 ms                                                                                                             | 9.71 ms: 1.29x slower                                                                                                   |
| go                       | 140 ms                                                                                                              | 188 ms: 1.34x slower                                                                                                    |
| pprint_pformat           | 1.97 sec                                                                                                            | 2.65 sec: 1.34x slower                                                                                                  |
| pprint_safe_repr         | 947 ms                                                                                                              | 1.29 sec: 1.36x slower                                                                                                  |
| genshi_xml               | 61.6 ms                                                                                                             | 87.0 ms: 1.41x slower                                                                                                   |
| generators               | 36.1 ms                                                                                                             | 55.5 ms: 1.54x slower                                                                                                   |
| Geometric mean           | (ref)                                                                                                               | 1.06x slower                                                                                                            |

Benchmark hidden because not significant (43): mako, sqlite_synth, coroutines, thrift, xml_etree_generate, pickle, xml_etree_parse, regex_dna, unpickle_pure_python, regex_v8, json_loads, tomli_loads, python_startup_no_site, xml_etree_process, pickle_dict, asyncio_websockets, unpickle_list, python_startup, xml_etree_iterparse, unpack_sequence, gc_traversal, connected_components, regex_effbot, nbody, create_gc_cycles, pickle_list, coverage, shortest_path, async_tree_memoization_tg, async_tree_io_tg, float, pidigits, scimark_monte_carlo, async_tree_cpu_io_mixed_tg, unpickle, json_dumps, pickle_pure_python, scimark_sparse_mat_mult, scimark_fft, richards_super, meteor_contest, bench_thread_pool, sqlglot_transpile

- Geometric mean (including insignificant results): 1.072x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 1.01x