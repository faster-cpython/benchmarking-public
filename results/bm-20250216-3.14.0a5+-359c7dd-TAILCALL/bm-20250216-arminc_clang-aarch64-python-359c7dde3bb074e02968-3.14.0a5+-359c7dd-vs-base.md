# Results vs. base

- fork: python
- ref: 359c7dde3bb074e02968
- machine: linux-aarch64
- commit hash: 359c7dd
- commit date: 2025-02-16
- overall geometric mean: 1.003x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250216-3.14.0a5+-359c7dd/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json | results/bm-20250216-3.14.0a5+-359c7dd-CLANG/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| sphinx         | 1.17 sec                                                                                                            | 1.14 sec: 1.02x faster                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.02x faster                                                                                                              |

Benchmark hidden because not significant (3): 2to3, docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250216-3.14.0a5+-359c7dd/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json | results/bm-20250216-3.14.0a5+-359c7dd-CLANG/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| async_generators           | 454 ms                                                                                                              | 425 ms: 1.07x faster                                                                                                      |
| async_tree_cpu_io_mixed    | 686 ms                                                                                                              | 755 ms: 1.10x slower                                                                                                      |
| async_tree_cpu_io_mixed_tg | 684 ms                                                                                                              | 755 ms: 1.10x slower                                                                                                      |
| Geometric mean             | (ref)                                                                                                               | 1.00x slower                                                                                                              |

Benchmark hidden because not significant (10): async_tree_none_tg, coroutines, async_tree_none, async_tree_io, async_tree_memoization, async_tree_memoization_tg, async_tree_io_tg, asyncio_websockets, asyncio_tcp_ssl, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250216-3.14.0a5+-359c7dd/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json | results/bm-20250216-3.14.0a5+-359c7dd-CLANG/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| pidigits       | 245 ms                                                                                                              | 305 ms: 1.25x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.06x slower                                                                                                              |

Benchmark hidden because not significant (2): nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250216-3.14.0a5+-359c7dd/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json | results/bm-20250216-3.14.0a5+-359c7dd-CLANG/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 4.17 ms                                                                                                             | 4.81 ms: 1.15x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                               | 1.05x slower                                                                                                              |

Benchmark hidden because not significant (3): regex_dna, regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | results/bm-20250216-3.14.0a5+-359c7dd/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json | results/bm-20250216-3.14.0a5+-359c7dd-CLANG/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json |
|---------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| xml_etree_process   | 83.2 ms                                                                                                             | 75.5 ms: 1.10x faster                                                                                                     |
| unpickle_list       | 6.44 us                                                                                                             | 5.86 us: 1.10x faster                                                                                                     |
| pickle_dict         | 39.5 us                                                                                                             | 36.7 us: 1.07x faster                                                                                                     |
| pickle_list         | 6.06 us                                                                                                             | 5.65 us: 1.07x faster                                                                                                     |
| unpickle            | 17.8 us                                                                                                             | 16.8 us: 1.06x faster                                                                                                     |
| pickle              | 16.3 us                                                                                                             | 15.4 us: 1.06x faster                                                                                                     |
| xml_etree_generate  | 113 ms                                                                                                              | 108 ms: 1.05x faster                                                                                                      |
| tomli_loads         | 2.58 sec                                                                                                            | 2.49 sec: 1.04x faster                                                                                                    |
| xml_etree_iterparse | 145 ms                                                                                                              | 156 ms: 1.07x slower                                                                                                      |
| xml_etree_parse     | 184 ms                                                                                                              | 212 ms: 1.15x slower                                                                                                      |
| Geometric mean      | (ref)                                                                                                               | 1.03x faster                                                                                                              |

Benchmark hidden because not significant (4): json_dumps, json_loads, pickle_pure_python, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_xml, django_template, genshi_text, mako

All benchmarks:
===============

| Benchmark                  | results/bm-20250216-3.14.0a5+-359c7dd/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json | results/bm-20250216-3.14.0a5+-359c7dd-CLANG/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| logging_silent             | 139 ns                                                                                                              | 118 ns: 1.18x faster                                                                                                      |
| spectral_norm              | 123 ms                                                                                                              | 107 ms: 1.15x faster                                                                                                      |
| deepcopy_memo              | 41.0 us                                                                                                             | 36.5 us: 1.12x faster                                                                                                     |
| scimark_sor                | 157 ms                                                                                                              | 142 ms: 1.11x faster                                                                                                      |
| xml_etree_process          | 83.2 ms                                                                                                             | 75.5 ms: 1.10x faster                                                                                                     |
| unpickle_list              | 6.44 us                                                                                                             | 5.86 us: 1.10x faster                                                                                                     |
| scimark_fft                | 420 ms                                                                                                              | 383 ms: 1.10x faster                                                                                                      |
| pyflate                    | 590 ms                                                                                                              | 541 ms: 1.09x faster                                                                                                      |
| typing_runtime_protocols   | 201 us                                                                                                              | 186 us: 1.08x faster                                                                                                      |
| comprehensions             | 21.2 us                                                                                                             | 19.6 us: 1.08x faster                                                                                                     |
| deepcopy                   | 345 us                                                                                                              | 320 us: 1.08x faster                                                                                                      |
| pickle_dict                | 39.5 us                                                                                                             | 36.7 us: 1.07x faster                                                                                                     |
| pickle_list                | 6.06 us                                                                                                             | 5.65 us: 1.07x faster                                                                                                     |
| async_generators           | 454 ms                                                                                                              | 425 ms: 1.07x faster                                                                                                      |
| unpickle                   | 17.8 us                                                                                                             | 16.8 us: 1.06x faster                                                                                                     |
| pickle                     | 16.3 us                                                                                                             | 15.4 us: 1.06x faster                                                                                                     |
| mdp                        | 3.46 sec                                                                                                            | 3.28 sec: 1.05x faster                                                                                                    |
| xml_etree_generate         | 113 ms                                                                                                              | 108 ms: 1.05x faster                                                                                                      |
| hexiom                     | 7.47 ms                                                                                                             | 7.13 ms: 1.05x faster                                                                                                     |
| sympy_integrate            | 21.7 ms                                                                                                             | 20.7 ms: 1.05x faster                                                                                                     |
| tomli_loads                | 2.58 sec                                                                                                            | 2.49 sec: 1.04x faster                                                                                                    |
| bpe_tokeniser              | 5.57 sec                                                                                                            | 5.39 sec: 1.03x faster                                                                                                    |
| k_core                     | 2.86 sec                                                                                                            | 2.79 sec: 1.02x faster                                                                                                    |
| sphinx                     | 1.17 sec                                                                                                            | 1.14 sec: 1.02x faster                                                                                                    |
| sqlalchemy_imperative      | 15.0 ms                                                                                                             | 15.7 ms: 1.05x slower                                                                                                     |
| xml_etree_iterparse        | 145 ms                                                                                                              | 156 ms: 1.07x slower                                                                                                      |
| create_gc_cycles           | 3.57 ms                                                                                                             | 3.86 ms: 1.08x slower                                                                                                     |
| async_tree_cpu_io_mixed    | 686 ms                                                                                                              | 755 ms: 1.10x slower                                                                                                      |
| async_tree_cpu_io_mixed_tg | 684 ms                                                                                                              | 755 ms: 1.10x slower                                                                                                      |
| regex_effbot               | 4.17 ms                                                                                                             | 4.81 ms: 1.15x slower                                                                                                     |
| xml_etree_parse            | 184 ms                                                                                                              | 212 ms: 1.15x slower                                                                                                      |
| pidigits                   | 245 ms                                                                                                              | 305 ms: 1.25x slower                                                                                                      |
| Geometric mean             | (ref)                                                                                                               | 1.02x faster                                                                                                              |

Benchmark hidden because not significant (72): bench_mp_pool, scimark_monte_carlo, richards_super, scimark_sparse_mat_mult, json_dumps, json_loads, sqlglot_transpile, coverage, pathlib, nbody, logging_format, logging_simple, gc_traversal, async_tree_none_tg, sqlglot_parse, richards, deepcopy_reduce, pickle_pure_python, go, html5lib, unpack_sequence, chaos, telco, coroutines, sympy_sum, bench_thread_pool, genshi_xml, raytrace, regex_dna, deltablue, sympy_str, async_tree_none, pprint_pformat, async_tree_io, django_template, nqueens, sqlalchemy_declarative, genshi_text, async_tree_memoization, 2to3, sympy_expand, async_tree_memoization_tg, dulwich_log, async_tree_io_tg, shortest_path, asyncio_websockets, unpickle_pure_python, pycparser, generators, json, sqlglot_normalize, float, pprint_safe_repr, docutils, thrift, connected_components, sqlite_synth, regex_compile, scimark_lu, python_startup_no_site, mako, fannkuch, meteor_contest, asyncio_tcp_ssl, sqlglot_optimize, python_startup, subparsers, asyncio_tcp, many_optionals, pylint, crypto_pyaes, regex_v8

- Geometric mean (including insignificant results): 1.003x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.03x