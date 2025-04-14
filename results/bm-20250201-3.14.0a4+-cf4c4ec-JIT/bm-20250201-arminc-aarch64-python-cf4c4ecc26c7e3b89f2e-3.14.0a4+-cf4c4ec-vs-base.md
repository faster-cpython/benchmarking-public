# Results vs. base

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: linux-aarch64
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.074x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json | results/bm-20250201-3.14.0a4+-cf4c4ec-JIT/bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 301 ms                                                                                                              | 321 ms: 1.07x slower                                                                                                    |
| docutils       | 2.96 sec                                                                                                            | 3.30 sec: 1.11x slower                                                                                                  |
| html5lib       | 66.0 ms                                                                                                             | 75.6 ms: 1.15x slower                                                                                                   |
| sphinx         | 1.16 sec                                                                                                            | 1.25 sec: 1.08x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                               | 1.10x slower                                                                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json | results/bm-20250201-3.14.0a4+-cf4c4ec-JIT/bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 671 ms                                                                                                              | 688 ms: 1.02x slower                                                                                                    |
| asyncio_tcp_ssl            | 2.26 sec                                                                                                            | 2.31 sec: 1.03x slower                                                                                                  |
| async_tree_cpu_io_mixed    | 694 ms                                                                                                              | 722 ms: 1.04x slower                                                                                                    |
| async_tree_io              | 924 ms                                                                                                              | 965 ms: 1.04x slower                                                                                                    |
| async_tree_memoization     | 505 ms                                                                                                              | 528 ms: 1.05x slower                                                                                                    |
| async_tree_none            | 402 ms                                                                                                              | 425 ms: 1.06x slower                                                                                                    |
| async_tree_memoization_tg  | 481 ms                                                                                                              | 514 ms: 1.07x slower                                                                                                    |
| async_generators           | 450 ms                                                                                                              | 491 ms: 1.09x slower                                                                                                    |
| asyncio_tcp                | 546 ms                                                                                                              | 598 ms: 1.10x slower                                                                                                    |
| Geometric mean             | (ref)                                                                                                               | 1.04x slower                                                                                                            |

Benchmark hidden because not significant (4): asyncio_websockets, coroutines, async_tree_io_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json | results/bm-20250201-3.14.0a4+-cf4c4ec-JIT/bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 247 ms                                                                                                              | 272 ms: 1.10x slower                                                                                                    |
| regex_compile  | 127 ms                                                                                                              | 146 ms: 1.15x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.06x slower                                                                                                            |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

Benchmark hidden because not significant (14): xml_etree_generate, pickle, unpickle, json_dumps, xml_etree_process, tomli_loads, xml_etree_parse, xml_etree_iterparse, pickle_list, unpickle_list, pickle_pure_python, pickle_dict, json_loads, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json | results/bm-20250201-3.14.0a4+-cf4c4ec-JIT/bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json |
|-----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| django_template | 40.1 ms                                                                                                             | 48.3 ms: 1.20x slower                                                                                                   |
| genshi_text     | 27.2 ms                                                                                                             | 33.8 ms: 1.24x slower                                                                                                   |
| genshi_xml      | 62.4 ms                                                                                                             | 85.8 ms: 1.37x slower                                                                                                   |
| Geometric mean  | (ref)                                                                                                               | 1.18x slower                                                                                                            |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json | results/bm-20250201-3.14.0a4+-cf4c4ec-JIT/bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool              | 5.94 sec                                                                                                            | 1.56 sec: 3.81x faster                                                                                                  |
| async_tree_cpu_io_mixed_tg | 671 ms                                                                                                              | 688 ms: 1.02x slower                                                                                                    |
| asyncio_tcp_ssl            | 2.26 sec                                                                                                            | 2.31 sec: 1.03x slower                                                                                                  |
| bpe_tokeniser              | 5.52 sec                                                                                                            | 5.70 sec: 1.03x slower                                                                                                  |
| async_tree_cpu_io_mixed    | 694 ms                                                                                                              | 722 ms: 1.04x slower                                                                                                    |
| scimark_sor                | 152 ms                                                                                                              | 158 ms: 1.04x slower                                                                                                    |
| async_tree_io              | 924 ms                                                                                                              | 965 ms: 1.04x slower                                                                                                    |
| async_tree_memoization     | 505 ms                                                                                                              | 528 ms: 1.05x slower                                                                                                    |
| mdp                        | 3.39 sec                                                                                                            | 3.55 sec: 1.05x slower                                                                                                  |
| pathlib                    | 21.1 ms                                                                                                             | 22.2 ms: 1.05x slower                                                                                                   |
| gc_traversal               | 6.50 ms                                                                                                             | 6.87 ms: 1.06x slower                                                                                                   |
| async_tree_none            | 402 ms                                                                                                              | 425 ms: 1.06x slower                                                                                                    |
| telco                      | 9.52 ms                                                                                                             | 10.1 ms: 1.06x slower                                                                                                   |
| bench_thread_pool          | 1.29 ms                                                                                                             | 1.36 ms: 1.06x slower                                                                                                   |
| pyflate                    | 568 ms                                                                                                              | 605 ms: 1.06x slower                                                                                                    |
| 2to3                       | 301 ms                                                                                                              | 321 ms: 1.07x slower                                                                                                    |
| fannkuch                   | 477 ms                                                                                                              | 508 ms: 1.07x slower                                                                                                    |
| async_tree_memoization_tg  | 481 ms                                                                                                              | 514 ms: 1.07x slower                                                                                                    |
| sqlglot_normalize          | 131 ms                                                                                                              | 140 ms: 1.07x slower                                                                                                    |
| sqlglot_transpile          | 1.83 ms                                                                                                             | 1.96 ms: 1.07x slower                                                                                                   |
| subparsers                 | 25.4 ms                                                                                                             | 27.3 ms: 1.07x slower                                                                                                   |
| sympy_integrate            | 21.5 ms                                                                                                             | 23.1 ms: 1.08x slower                                                                                                   |
| sympy_sum                  | 150 ms                                                                                                              | 162 ms: 1.08x slower                                                                                                    |
| sphinx                     | 1.16 sec                                                                                                            | 1.25 sec: 1.08x slower                                                                                                  |
| async_generators           | 450 ms                                                                                                              | 491 ms: 1.09x slower                                                                                                    |
| logging_silent             | 136 ns                                                                                                              | 149 ns: 1.09x slower                                                                                                    |
| logging_simple             | 7.38 us                                                                                                             | 8.08 us: 1.09x slower                                                                                                   |
| sympy_expand               | 476 ms                                                                                                              | 521 ms: 1.09x slower                                                                                                    |
| logging_format             | 8.07 us                                                                                                             | 8.83 us: 1.10x slower                                                                                                   |
| asyncio_tcp                | 546 ms                                                                                                              | 598 ms: 1.10x slower                                                                                                    |
| meteor_contest             | 115 ms                                                                                                              | 126 ms: 1.10x slower                                                                                                    |
| regex_dna                  | 247 ms                                                                                                              | 272 ms: 1.10x slower                                                                                                    |
| scimark_sparse_mat_mult    | 6.27 ms                                                                                                             | 6.93 ms: 1.11x slower                                                                                                   |
| docutils                   | 2.96 sec                                                                                                            | 3.30 sec: 1.11x slower                                                                                                  |
| sqlglot_parse              | 1.45 ms                                                                                                             | 1.62 ms: 1.12x slower                                                                                                   |
| unpack_sequence            | 58.1 ns                                                                                                             | 65.0 ns: 1.12x slower                                                                                                   |
| sqlalchemy_imperative      | 15.3 ms                                                                                                             | 17.1 ms: 1.12x slower                                                                                                   |
| spectral_norm              | 123 ms                                                                                                              | 138 ms: 1.13x slower                                                                                                    |
| sympy_str                  | 268 ms                                                                                                              | 303 ms: 1.13x slower                                                                                                    |
| crypto_pyaes               | 88.8 ms                                                                                                             | 101 ms: 1.14x slower                                                                                                    |
| sqlglot_optimize           | 61.7 ms                                                                                                             | 70.6 ms: 1.15x slower                                                                                                   |
| raytrace                   | 315 ms                                                                                                              | 361 ms: 1.15x slower                                                                                                    |
| html5lib                   | 66.0 ms                                                                                                             | 75.6 ms: 1.15x slower                                                                                                   |
| scimark_lu                 | 139 ms                                                                                                              | 159 ms: 1.15x slower                                                                                                    |
| deepcopy_reduce            | 3.82 us                                                                                                             | 4.39 us: 1.15x slower                                                                                                   |
| regex_compile              | 127 ms                                                                                                              | 146 ms: 1.15x slower                                                                                                    |
| dulwich_log                | 60.6 ms                                                                                                             | 70.0 ms: 1.15x slower                                                                                                   |
| deltablue                  | 3.86 ms                                                                                                             | 4.51 ms: 1.17x slower                                                                                                   |
| many_optionals             | 706 us                                                                                                              | 832 us: 1.18x slower                                                                                                    |
| typing_runtime_protocols   | 193 us                                                                                                              | 227 us: 1.18x slower                                                                                                    |
| comprehensions             | 21.3 us                                                                                                             | 25.1 us: 1.18x slower                                                                                                   |
| go                         | 144 ms                                                                                                              | 170 ms: 1.18x slower                                                                                                    |
| deepcopy                   | 344 us                                                                                                              | 409 us: 1.19x slower                                                                                                    |
| django_template            | 40.1 ms                                                                                                             | 48.3 ms: 1.20x slower                                                                                                   |
| pycparser                  | 1.27 sec                                                                                                            | 1.54 sec: 1.21x slower                                                                                                  |
| genshi_text                | 27.2 ms                                                                                                             | 33.8 ms: 1.24x slower                                                                                                   |
| chaos                      | 68.4 ms                                                                                                             | 86.7 ms: 1.27x slower                                                                                                   |
| pprint_safe_repr           | 988 ms                                                                                                              | 1.30 sec: 1.32x slower                                                                                                  |
| nqueens                    | 101 ms                                                                                                              | 134 ms: 1.33x slower                                                                                                    |
| pprint_pformat             | 1.99 sec                                                                                                            | 2.69 sec: 1.35x slower                                                                                                  |
| genshi_xml                 | 62.4 ms                                                                                                             | 85.8 ms: 1.37x slower                                                                                                   |
| hexiom                     | 7.38 ms                                                                                                             | 10.2 ms: 1.38x slower                                                                                                   |
| generators                 | 37.8 ms                                                                                                             | 55.5 ms: 1.47x slower                                                                                                   |
| Geometric mean             | (ref)                                                                                                               | 1.07x slower                                                                                                            |

Benchmark hidden because not significant (41): mako, xml_etree_generate, pickle, unpickle, sqlite_synth, regex_v8, json_dumps, xml_etree_process, create_gc_cycles, connected_components, tomli_loads, asyncio_websockets, xml_etree_parse, python_startup_no_site, xml_etree_iterparse, nbody, coroutines, pickle_list, python_startup, scimark_fft, sqlalchemy_declarative, k_core, pidigits, async_tree_io_tg, float, unpickle_list, shortest_path, pickle_pure_python, coverage, async_tree_none_tg, pickle_dict, scimark_monte_carlo, regex_effbot, json_loads, thrift, deepcopy_memo, json, richards_super, pylint, unpickle_pure_python, richards

- Geometric mean (including insignificant results): 1.074x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 1.01x