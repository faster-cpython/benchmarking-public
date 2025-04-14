# Results vs. base

- fork: python
- ref: 359c7dde3bb074e02968
- machine: linux-aarch64
- commit hash: 359c7dd
- commit date: 2025-02-16
- overall geometric mean: 1.028x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250216-3.14.0a5+-359c7dd/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json | results/bm-20250216-3.14.0a5+-359c7dd-JIT/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 304 ms                                                                                                              | 322 ms: 1.06x slower                                                                                                    |
| docutils       | 3.01 sec                                                                                                            | 3.23 sec: 1.07x slower                                                                                                  |
| html5lib       | 62.1 ms                                                                                                             | 64.8 ms: 1.04x slower                                                                                                   |
| sphinx         | 1.17 sec                                                                                                            | 1.21 sec: 1.03x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                               | 1.05x slower                                                                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | results/bm-20250216-3.14.0a5+-359c7dd/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json | results/bm-20250216-3.14.0a5+-359c7dd-JIT/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json |
|---------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| asyncio_tcp_ssl           | 2.24 sec                                                                                                            | 2.28 sec: 1.02x slower                                                                                                  |
| async_tree_memoization_tg | 489 ms                                                                                                              | 509 ms: 1.04x slower                                                                                                    |
| async_generators          | 454 ms                                                                                                              | 485 ms: 1.07x slower                                                                                                    |
| Geometric mean            | (ref)                                                                                                               | 1.02x slower                                                                                                            |

Benchmark hidden because not significant (10): asyncio_websockets, async_tree_none_tg, async_tree_io_tg, async_tree_io, async_tree_cpu_io_mixed_tg, coroutines, asyncio_tcp, async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): pidigits, float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250216-3.14.0a5+-359c7dd/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json | results/bm-20250216-3.14.0a5+-359c7dd-JIT/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 267 ms                                                                                                              | 246 ms: 1.08x faster                                                                                                    |
| regex_effbot   | 4.17 ms                                                                                                             | 3.92 ms: 1.06x faster                                                                                                   |
| Geometric mean | (ref)                                                                                                               | 1.04x faster                                                                                                            |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250216-3.14.0a5+-359c7dd/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json | results/bm-20250216-3.14.0a5+-359c7dd-JIT/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json |
|----------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 2.58 sec                                                                                                            | 2.50 sec: 1.03x faster                                                                                                  |
| unpickle_pure_python | 263 us                                                                                                              | 282 us: 1.07x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                               | 1.01x slower                                                                                                            |

Benchmark hidden because not significant (12): json_loads, json_dumps, xml_etree_parse, pickle_list, unpickle, xml_etree_process, pickle_pure_python, xml_etree_generate, unpickle_list, xml_etree_iterparse, pickle, pickle_dict

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250216-3.14.0a5+-359c7dd/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json | results/bm-20250216-3.14.0a5+-359c7dd-JIT/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json |
|-----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| django_template | 39.0 ms                                                                                                             | 42.1 ms: 1.08x slower                                                                                                   |
| Geometric mean  | (ref)                                                                                                               | 1.02x slower                                                                                                            |

Benchmark hidden because not significant (3): mako, genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                 | results/bm-20250216-3.14.0a5+-359c7dd/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json | results/bm-20250216-3.14.0a5+-359c7dd-JIT/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json |
|---------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool             | 5.29 sec                                                                                                            | 2.72 sec: 1.95x faster                                                                                                  |
| regex_dna                 | 267 ms                                                                                                              | 246 ms: 1.08x faster                                                                                                    |
| unpack_sequence           | 67.7 ns                                                                                                             | 62.9 ns: 1.08x faster                                                                                                   |
| regex_effbot              | 4.17 ms                                                                                                             | 3.92 ms: 1.06x faster                                                                                                   |
| pyflate                   | 590 ms                                                                                                              | 567 ms: 1.04x faster                                                                                                    |
| tomli_loads               | 2.58 sec                                                                                                            | 2.50 sec: 1.03x faster                                                                                                  |
| asyncio_tcp_ssl           | 2.24 sec                                                                                                            | 2.28 sec: 1.02x slower                                                                                                  |
| sphinx                    | 1.17 sec                                                                                                            | 1.21 sec: 1.03x slower                                                                                                  |
| sympy_sum                 | 144 ms                                                                                                              | 149 ms: 1.04x slower                                                                                                    |
| async_tree_memoization_tg | 489 ms                                                                                                              | 509 ms: 1.04x slower                                                                                                    |
| create_gc_cycles          | 3.57 ms                                                                                                             | 3.72 ms: 1.04x slower                                                                                                   |
| html5lib                  | 62.1 ms                                                                                                             | 64.8 ms: 1.04x slower                                                                                                   |
| pylint                    | 305 ms                                                                                                              | 319 ms: 1.04x slower                                                                                                    |
| k_core                    | 2.86 sec                                                                                                            | 3.00 sec: 1.05x slower                                                                                                  |
| deltablue                 | 3.98 ms                                                                                                             | 4.18 ms: 1.05x slower                                                                                                   |
| bpe_tokeniser             | 5.57 sec                                                                                                            | 5.85 sec: 1.05x slower                                                                                                  |
| nqueens                   | 101 ms                                                                                                              | 106 ms: 1.05x slower                                                                                                    |
| dulwich_log               | 61.1 ms                                                                                                             | 64.5 ms: 1.06x slower                                                                                                   |
| 2to3                      | 304 ms                                                                                                              | 322 ms: 1.06x slower                                                                                                    |
| async_generators          | 454 ms                                                                                                              | 485 ms: 1.07x slower                                                                                                    |
| sympy_integrate           | 21.7 ms                                                                                                             | 23.2 ms: 1.07x slower                                                                                                   |
| unpickle_pure_python      | 263 us                                                                                                              | 282 us: 1.07x slower                                                                                                    |
| sympy_expand              | 466 ms                                                                                                              | 500 ms: 1.07x slower                                                                                                    |
| docutils                  | 3.01 sec                                                                                                            | 3.23 sec: 1.07x slower                                                                                                  |
| django_template           | 39.0 ms                                                                                                             | 42.1 ms: 1.08x slower                                                                                                   |
| sqlglot_optimize          | 61.3 ms                                                                                                             | 66.6 ms: 1.09x slower                                                                                                   |
| sqlalchemy_imperative     | 15.0 ms                                                                                                             | 16.3 ms: 1.09x slower                                                                                                   |
| meteor_contest            | 116 ms                                                                                                              | 126 ms: 1.09x slower                                                                                                    |
| scimark_sparse_mat_mult   | 6.45 ms                                                                                                             | 7.07 ms: 1.10x slower                                                                                                   |
| typing_runtime_protocols  | 201 us                                                                                                              | 222 us: 1.10x slower                                                                                                    |
| sqlglot_parse             | 1.47 ms                                                                                                             | 1.64 ms: 1.11x slower                                                                                                   |
| fannkuch                  | 494 ms                                                                                                              | 552 ms: 1.12x slower                                                                                                    |
| pycparser                 | 1.29 sec                                                                                                            | 1.45 sec: 1.12x slower                                                                                                  |
| go                        | 141 ms                                                                                                              | 160 ms: 1.14x slower                                                                                                    |
| hexiom                    | 7.47 ms                                                                                                             | 8.60 ms: 1.15x slower                                                                                                   |
| comprehensions            | 21.2 us                                                                                                             | 24.6 us: 1.16x slower                                                                                                   |
| crypto_pyaes              | 85.2 ms                                                                                                             | 101 ms: 1.19x slower                                                                                                    |
| pprint_safe_repr          | 969 ms                                                                                                              | 1.27 sec: 1.31x slower                                                                                                  |
| pprint_pformat            | 1.98 sec                                                                                                            | 2.64 sec: 1.33x slower                                                                                                  |
| Geometric mean            | (ref)                                                                                                               | 1.02x slower                                                                                                            |

Benchmark hidden because not significant (65): json_loads, sqlite_synth, deepcopy_reduce, logging_silent, json_dumps, json, logging_format, regex_compile, spectral_norm, deepcopy, deepcopy_memo, xml_etree_parse, pidigits, scimark_lu, gc_traversal, thrift, scimark_monte_carlo, scimark_sor, mdp, asyncio_websockets, mako, connected_components, logging_simple, pickle_list, async_tree_none_tg, python_startup_no_site, unpickle, regex_v8, float, python_startup, async_tree_io_tg, richards_super, async_tree_io, subparsers, generators, async_tree_cpu_io_mixed_tg, xml_etree_process, genshi_text, chaos, coroutines, genshi_xml, pathlib, pickle_pure_python, shortest_path, asyncio_tcp, xml_etree_generate, unpickle_list, async_tree_memoization, telco, raytrace, async_tree_none, async_tree_cpu_io_mixed, nbody, richards, xml_etree_iterparse, coverage, bench_thread_pool, sqlglot_normalize, sympy_str, pickle, pickle_dict, sqlalchemy_declarative, scimark_fft, sqlglot_transpile, many_optionals

- Geometric mean (including insignificant results): 1.028x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.01x