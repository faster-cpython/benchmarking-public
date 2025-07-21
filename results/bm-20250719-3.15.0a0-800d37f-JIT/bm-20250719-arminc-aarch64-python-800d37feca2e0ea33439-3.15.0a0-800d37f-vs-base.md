# Results vs. base

- fork: python
- ref: 800d37feca2e0ea33439
- machine: linux-aarch64
- commit hash: 800d37f
- commit date: 2025-07-19
- overall geometric mean: 1.018x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250719-3.15.0a0-800d37f/bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json | results/bm-20250719-3.15.0a0-800d37f-JIT/bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 303 ms                                                                                                            | 312 ms: 1.03x slower                                                                                                  |
| docutils       | 2.97 sec                                                                                                          | 3.08 sec: 1.04x slower                                                                                                |
| sphinx         | 1.14 sec                                                                                                          | 1.17 sec: 1.02x slower                                                                                                |
| Geometric mean | (ref)                                                                                                             | 1.03x slower                                                                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | results/bm-20250719-3.15.0a0-800d37f/bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json | results/bm-20250719-3.15.0a0-800d37f-JIT/bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json |
|---------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| async_tree_none           | 372 ms                                                                                                            | 375 ms: 1.01x slower                                                                                                  |
| async_tree_memoization_tg | 467 ms                                                                                                            | 472 ms: 1.01x slower                                                                                                  |
| async_tree_io             | 871 ms                                                                                                            | 880 ms: 1.01x slower                                                                                                  |
| async_tree_memoization    | 468 ms                                                                                                            | 477 ms: 1.02x slower                                                                                                  |
| asyncio_tcp_ssl           | 2.14 sec                                                                                                          | 2.20 sec: 1.03x slower                                                                                                |
| async_tree_none_tg        | 376 ms                                                                                                            | 389 ms: 1.03x slower                                                                                                  |
| async_generators          | 459 ms                                                                                                            | 485 ms: 1.05x slower                                                                                                  |
| Geometric mean            | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed, async_tree_io_tg, asyncio_websockets, async_tree_cpu_io_mixed_tg, asyncio_tcp, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250719-3.15.0a0-800d37f/bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json | results/bm-20250719-3.15.0a0-800d37f-JIT/bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| float          | 84.9 ms                                                                                                           | 82.0 ms: 1.04x faster                                                                                                 |
| nbody          | 120 ms                                                                                                            | 130 ms: 1.08x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.02x slower                                                                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250719-3.15.0a0-800d37f/bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json | results/bm-20250719-3.15.0a0-800d37f-JIT/bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 219 ms                                                                                                            | 220 ms: 1.01x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmark hidden because not significant (3): regex_v8, regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark          | results/bm-20250719-3.15.0a0-800d37f/bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json | results/bm-20250719-3.15.0a0-800d37f-JIT/bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json |
|--------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| tomli_loads        | 2.44 sec                                                                                                          | 2.33 sec: 1.05x faster                                                                                                |
| xml_etree_generate | 112 ms                                                                                                            | 109 ms: 1.03x faster                                                                                                  |
| xml_etree_process  | 79.0 ms                                                                                                           | 78.2 ms: 1.01x faster                                                                                                 |
| pickle_pure_python | 387 us                                                                                                            | 410 us: 1.06x slower                                                                                                  |
| Geometric mean     | (ref)                                                                                                             | 1.00x slower                                                                                                          |

Benchmark hidden because not significant (10): pickle, unpickle_list, xml_etree_iterparse, json_dumps, unpickle_pure_python, xml_etree_parse, unpickle, json_loads, pickle_dict, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250719-3.15.0a0-800d37f/bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json | results/bm-20250719-3.15.0a0-800d37f-JIT/bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.42 ms                                                                                                           | 8.56 ms: 1.02x slower                                                                                                 |
| python_startup         | 14.8 ms                                                                                                           | 15.1 ms: 1.02x slower                                                                                                 |
| Geometric mean         | (ref)                                                                                                             | 1.02x slower                                                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark      | results/bm-20250719-3.15.0a0-800d37f/bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json | results/bm-20250719-3.15.0a0-800d37f-JIT/bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako           | 13.6 ms                                                                                                           | 12.8 ms: 1.06x faster                                                                                                 |
| genshi_text    | 26.8 ms                                                                                                           | 27.0 ms: 1.01x slower                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.00x faster                                                                                                          |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                 | results/bm-20250719-3.15.0a0-800d37f/bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json | results/bm-20250719-3.15.0a0-800d37f-JIT/bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json |
|---------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| richards                  | 53.1 ms                                                                                                           | 45.5 ms: 1.17x faster                                                                                                 |
| richards_super            | 58.8 ms                                                                                                           | 53.2 ms: 1.10x faster                                                                                                 |
| mako                      | 13.6 ms                                                                                                           | 12.8 ms: 1.06x faster                                                                                                 |
| tomli_loads               | 2.44 sec                                                                                                          | 2.33 sec: 1.05x faster                                                                                                |
| deltablue                 | 4.05 ms                                                                                                           | 3.87 ms: 1.05x faster                                                                                                 |
| scimark_fft               | 424 ms                                                                                                            | 408 ms: 1.04x faster                                                                                                  |
| float                     | 84.9 ms                                                                                                           | 82.0 ms: 1.04x faster                                                                                                 |
| xml_etree_generate        | 112 ms                                                                                                            | 109 ms: 1.03x faster                                                                                                  |
| spectral_norm             | 118 ms                                                                                                            | 116 ms: 1.02x faster                                                                                                  |
| sqlite_synth              | 3.81 us                                                                                                           | 3.77 us: 1.01x faster                                                                                                 |
| xml_etree_process         | 79.0 ms                                                                                                           | 78.2 ms: 1.01x faster                                                                                                 |
| deepcopy                  | 331 us                                                                                                            | 332 us: 1.00x slower                                                                                                  |
| regex_dna                 | 219 ms                                                                                                            | 220 ms: 1.01x slower                                                                                                  |
| genshi_text               | 26.8 ms                                                                                                           | 27.0 ms: 1.01x slower                                                                                                 |
| async_tree_none           | 372 ms                                                                                                            | 375 ms: 1.01x slower                                                                                                  |
| async_tree_memoization_tg | 467 ms                                                                                                            | 472 ms: 1.01x slower                                                                                                  |
| async_tree_io             | 871 ms                                                                                                            | 880 ms: 1.01x slower                                                                                                  |
| logging_format            | 7.75 us                                                                                                           | 7.87 us: 1.02x slower                                                                                                 |
| python_startup_no_site    | 8.42 ms                                                                                                           | 8.56 ms: 1.02x slower                                                                                                 |
| shortest_path             | 582 ms                                                                                                            | 593 ms: 1.02x slower                                                                                                  |
| pathlib                   | 22.6 ms                                                                                                           | 23.0 ms: 1.02x slower                                                                                                 |
| async_tree_memoization    | 468 ms                                                                                                            | 477 ms: 1.02x slower                                                                                                  |
| deepcopy_reduce           | 3.61 us                                                                                                           | 3.68 us: 1.02x slower                                                                                                 |
| python_startup            | 14.8 ms                                                                                                           | 15.1 ms: 1.02x slower                                                                                                 |
| sphinx                    | 1.14 sec                                                                                                          | 1.17 sec: 1.02x slower                                                                                                |
| json                      | 5.65 ms                                                                                                           | 5.80 ms: 1.02x slower                                                                                                 |
| asyncio_tcp_ssl           | 2.14 sec                                                                                                          | 2.20 sec: 1.03x slower                                                                                                |
| sqlglot_v2_optimize       | 60.6 ms                                                                                                           | 62.2 ms: 1.03x slower                                                                                                 |
| connected_components      | 557 ms                                                                                                            | 573 ms: 1.03x slower                                                                                                  |
| logging_simple            | 6.97 us                                                                                                           | 7.18 us: 1.03x slower                                                                                                 |
| 2to3                      | 303 ms                                                                                                            | 312 ms: 1.03x slower                                                                                                  |
| async_tree_none_tg        | 376 ms                                                                                                            | 389 ms: 1.03x slower                                                                                                  |
| docutils                  | 2.97 sec                                                                                                          | 3.08 sec: 1.04x slower                                                                                                |
| sqlglot_v2_transpile      | 1.79 ms                                                                                                           | 1.86 ms: 1.04x slower                                                                                                 |
| pyflate                   | 534 ms                                                                                                            | 555 ms: 1.04x slower                                                                                                  |
| scimark_lu                | 146 ms                                                                                                            | 151 ms: 1.04x slower                                                                                                  |
| subparsers                | 28.1 ms                                                                                                           | 29.2 ms: 1.04x slower                                                                                                 |
| k_core                    | 2.78 sec                                                                                                          | 2.92 sec: 1.05x slower                                                                                                |
| async_generators          | 459 ms                                                                                                            | 485 ms: 1.05x slower                                                                                                  |
| meteor_contest            | 107 ms                                                                                                            | 113 ms: 1.06x slower                                                                                                  |
| sympy_expand              | 463 ms                                                                                                            | 489 ms: 1.06x slower                                                                                                  |
| pickle_pure_python        | 387 us                                                                                                            | 410 us: 1.06x slower                                                                                                  |
| scimark_monte_carlo       | 80.2 ms                                                                                                           | 85.1 ms: 1.06x slower                                                                                                 |
| typing_runtime_protocols  | 197 us                                                                                                            | 210 us: 1.06x slower                                                                                                  |
| many_optionals            | 760 us                                                                                                            | 812 us: 1.07x slower                                                                                                  |
| sympy_str                 | 262 ms                                                                                                            | 281 ms: 1.07x slower                                                                                                  |
| sqlglot_v2_parse          | 1.43 ms                                                                                                           | 1.54 ms: 1.07x slower                                                                                                 |
| sympy_sum                 | 145 ms                                                                                                            | 156 ms: 1.08x slower                                                                                                  |
| nbody                     | 120 ms                                                                                                            | 130 ms: 1.08x slower                                                                                                  |
| pycparser                 | 1.25 sec                                                                                                          | 1.35 sec: 1.08x slower                                                                                                |
| crypto_pyaes              | 86.4 ms                                                                                                           | 94.7 ms: 1.10x slower                                                                                                 |
| comprehensions            | 20.3 us                                                                                                           | 22.3 us: 1.10x slower                                                                                                 |
| hexiom                    | 6.80 ms                                                                                                           | 7.58 ms: 1.11x slower                                                                                                 |
| go                        | 129 ms                                                                                                            | 154 ms: 1.19x slower                                                                                                  |
| pprint_pformat            | 1.84 sec                                                                                                          | 2.28 sec: 1.24x slower                                                                                                |
| pprint_safe_repr          | 900 ms                                                                                                            | 1.12 sec: 1.25x slower                                                                                                |
| unpack_sequence           | 50.2 ns                                                                                                           | 73.4 ns: 1.46x slower                                                                                                 |
| Geometric mean            | (ref)                                                                                                             | 1.02x slower                                                                                                          |

Benchmark hidden because not significant (46): bench_mp_pool, pickle, create_gc_cycles, fannkuch, scimark_sor, gc_traversal, async_tree_cpu_io_mixed, scimark_sparse_mat_mult, async_tree_io_tg, bpe_tokeniser, regex_v8, unpickle_list, djangocms, regex_compile, generators, asyncio_websockets, xml_etree_iterparse, json_dumps, unpickle_pure_python, async_tree_cpu_io_mixed_tg, bench_thread_pool, xml_etree_parse, mdp, asyncio_tcp, dulwich_log, pidigits, unpickle, coverage, telco, json_loads, django_template, chaos, sqlglot_v2_normalize, pickle_dict, nqueens, thrift, regex_effbot, raytrace, genshi_xml, coroutines, logging_silent, pickle_list, html5lib, pylint, deepcopy_memo, sympy_integrate

- Geometric mean (including insignificant results): 1.018x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x