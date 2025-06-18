# Results vs. base

- fork: python
- ref: fba5dded6df3c2b19435
- machine: linux-aarch64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.015x faster
- HPT reliability: 82.06%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json | results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 357 ms                                                                                                            | 369 ms: 1.03x slower                                                                                                  |
| docutils       | 3.44 sec                                                                                                          | 3.63 sec: 1.05x slower                                                                                                |
| html5lib       | 67.3 ms                                                                                                           | 68.6 ms: 1.02x slower                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.03x slower                                                                                                          |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json | results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json |
|---------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 534 ms                                                                                                            | 518 ms: 1.03x faster                                                                                                  |
| async_tree_none_tg        | 434 ms                                                                                                            | 426 ms: 1.02x faster                                                                                                  |
| async_tree_io_tg          | 1.04 sec                                                                                                          | 1.02 sec: 1.01x faster                                                                                                |
| asyncio_tcp_ssl           | 2.24 sec                                                                                                          | 2.27 sec: 1.01x slower                                                                                                |
| async_generators          | 515 ms                                                                                                            | 540 ms: 1.05x slower                                                                                                  |
| Geometric mean            | (ref)                                                                                                             | 1.00x slower                                                                                                          |

Benchmark hidden because not significant (8): async_tree_none, asyncio_websockets, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_io, asyncio_tcp, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json | results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| nbody          | 141 ms                                                                                                            | 132 ms: 1.07x faster                                                                                                  |
| float          | 96.7 ms                                                                                                           | 94.8 ms: 1.02x faster                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.03x faster                                                                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

Benchmark hidden because not significant (4): regex_compile, regex_effbot, regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json | results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| xml_etree_generate   | 163 ms                                                                                                            | 150 ms: 1.09x faster                                                                                                  |
| tomli_loads          | 2.93 sec                                                                                                          | 2.72 sec: 1.08x faster                                                                                                |
| xml_etree_process    | 110 ms                                                                                                            | 103 ms: 1.07x faster                                                                                                  |
| unpickle_pure_python | 329 us                                                                                                            | 308 us: 1.07x faster                                                                                                  |
| pickle               | 20.5 us                                                                                                           | 20.1 us: 1.02x faster                                                                                                 |
| pickle_pure_python   | 468 us                                                                                                            | 474 us: 1.01x slower                                                                                                  |
| xml_etree_iterparse  | 170 ms                                                                                                            | 173 ms: 1.02x slower                                                                                                  |
| Geometric mean       | (ref)                                                                                                             | 1.02x faster                                                                                                          |

Benchmark hidden because not significant (7): json_dumps, pickle_dict, json_loads, unpickle_list, unpickle, xml_etree_parse, pickle_list

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json | results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| genshi_text     | 33.3 ms                                                                                                           | 33.0 ms: 1.01x faster                                                                                                 |
| django_template | 53.6 ms                                                                                                           | 53.1 ms: 1.01x faster                                                                                                 |
| Geometric mean  | (ref)                                                                                                             | 1.00x faster                                                                                                          |

Benchmark hidden because not significant (2): mako, genshi_xml

All benchmarks:
===============

| Benchmark                 | results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json | results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json |
|---------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool             | 5.40 sec                                                                                                          | 3.00 sec: 1.80x faster                                                                                                |
| richards                  | 64.0 ms                                                                                                           | 52.8 ms: 1.21x faster                                                                                                 |
| richards_super            | 72.2 ms                                                                                                           | 62.3 ms: 1.16x faster                                                                                                 |
| xml_etree_generate        | 163 ms                                                                                                            | 150 ms: 1.09x faster                                                                                                  |
| tomli_loads               | 2.93 sec                                                                                                          | 2.72 sec: 1.08x faster                                                                                                |
| xml_etree_process         | 110 ms                                                                                                            | 103 ms: 1.07x faster                                                                                                  |
| unpickle_pure_python      | 329 us                                                                                                            | 308 us: 1.07x faster                                                                                                  |
| nbody                     | 141 ms                                                                                                            | 132 ms: 1.07x faster                                                                                                  |
| scimark_fft               | 498 ms                                                                                                            | 470 ms: 1.06x faster                                                                                                  |
| fannkuch                  | 590 ms                                                                                                            | 564 ms: 1.05x faster                                                                                                  |
| coverage                  | 141 ms                                                                                                            | 135 ms: 1.04x faster                                                                                                  |
| bpe_tokeniser             | 6.73 sec                                                                                                          | 6.45 sec: 1.04x faster                                                                                                |
| deltablue                 | 4.54 ms                                                                                                           | 4.37 ms: 1.04x faster                                                                                                 |
| logging_silent            | 946 ns                                                                                                            | 912 ns: 1.04x faster                                                                                                  |
| async_tree_memoization_tg | 534 ms                                                                                                            | 518 ms: 1.03x faster                                                                                                  |
| float                     | 96.7 ms                                                                                                           | 94.8 ms: 1.02x faster                                                                                                 |
| pickle                    | 20.5 us                                                                                                           | 20.1 us: 1.02x faster                                                                                                 |
| async_tree_none_tg        | 434 ms                                                                                                            | 426 ms: 1.02x faster                                                                                                  |
| shortest_path             | 608 ms                                                                                                            | 597 ms: 1.02x faster                                                                                                  |
| logging_simple            | 9.40 us                                                                                                           | 9.27 us: 1.01x faster                                                                                                 |
| async_tree_io_tg          | 1.04 sec                                                                                                          | 1.02 sec: 1.01x faster                                                                                                |
| genshi_text               | 33.3 ms                                                                                                           | 33.0 ms: 1.01x faster                                                                                                 |
| django_template           | 53.6 ms                                                                                                           | 53.1 ms: 1.01x faster                                                                                                 |
| mdp                       | 1.97 sec                                                                                                          | 1.99 sec: 1.01x slower                                                                                                |
| asyncio_tcp_ssl           | 2.24 sec                                                                                                          | 2.27 sec: 1.01x slower                                                                                                |
| json                      | 6.86 ms                                                                                                           | 6.95 ms: 1.01x slower                                                                                                 |
| pickle_pure_python        | 468 us                                                                                                            | 474 us: 1.01x slower                                                                                                  |
| sqlglot_v2_normalize      | 161 ms                                                                                                            | 163 ms: 1.01x slower                                                                                                  |
| sqlglot_v2_parse          | 1.77 ms                                                                                                           | 1.80 ms: 1.01x slower                                                                                                 |
| sqlglot_v2_optimize       | 77.0 ms                                                                                                           | 78.1 ms: 1.01x slower                                                                                                 |
| xml_etree_iterparse       | 170 ms                                                                                                            | 173 ms: 1.02x slower                                                                                                  |
| html5lib                  | 67.3 ms                                                                                                           | 68.6 ms: 1.02x slower                                                                                                 |
| subparsers                | 36.2 ms                                                                                                           | 37.0 ms: 1.02x slower                                                                                                 |
| raytrace                  | 390 ms                                                                                                            | 400 ms: 1.03x slower                                                                                                  |
| sympy_expand              | 606 ms                                                                                                            | 624 ms: 1.03x slower                                                                                                  |
| 2to3                      | 357 ms                                                                                                            | 369 ms: 1.03x slower                                                                                                  |
| nqueens                   | 125 ms                                                                                                            | 130 ms: 1.04x slower                                                                                                  |
| many_optionals            | 957 us                                                                                                            | 1.00 ms: 1.04x slower                                                                                                 |
| async_generators          | 515 ms                                                                                                            | 540 ms: 1.05x slower                                                                                                  |
| docutils                  | 3.44 sec                                                                                                          | 3.63 sec: 1.05x slower                                                                                                |
| hexiom                    | 8.23 ms                                                                                                           | 8.71 ms: 1.06x slower                                                                                                 |
| typing_runtime_protocols  | 259 us                                                                                                            | 275 us: 1.06x slower                                                                                                  |
| unpack_sequence           | 62.4 ns                                                                                                           | 66.6 ns: 1.07x slower                                                                                                 |
| comprehensions            | 23.1 us                                                                                                           | 24.7 us: 1.07x slower                                                                                                 |
| pycparser                 | 1.49 sec                                                                                                          | 1.65 sec: 1.10x slower                                                                                                |
| pprint_safe_repr          | 1.34 sec                                                                                                          | 1.58 sec: 1.18x slower                                                                                                |
| pprint_pformat            | 2.70 sec                                                                                                          | 3.24 sec: 1.20x slower                                                                                                |
| go                        | 141 ms                                                                                                            | 172 ms: 1.22x slower                                                                                                  |
| Geometric mean            | (ref)                                                                                                             | 1.00x faster                                                                                                          |

Benchmark hidden because not significant (55): spectral_norm, json_dumps, dulwich_log, pickle_dict, json_loads, unpickle_list, regex_compile, sqlite_synth, gc_traversal, bench_thread_pool, djangocms, create_gc_cycles, async_tree_none, asyncio_websockets, scimark_sparse_mat_mult, logging_format, async_tree_cpu_io_mixed, mako, pathlib, telco, k_core, unpickle, thrift, async_tree_memoization, scimark_monte_carlo, sqlglot_v2_transpile, async_tree_cpu_io_mixed_tg, pidigits, generators, python_startup_no_site, regex_effbot, deepcopy_reduce, python_startup, regex_v8, async_tree_io, deepcopy, pyflate, connected_components, asyncio_tcp, deepcopy_memo, xml_etree_parse, sphinx, meteor_contest, pickle_list, sympy_sum, regex_dna, scimark_lu, scimark_sor, genshi_xml, sympy_str, crypto_pyaes, coroutines, pylint, chaos, sympy_integrate

- Geometric mean (including insignificant results): 1.015x faster

# HPT report

- Reliability score: 82.06% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x