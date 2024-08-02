# Results vs. base

- fork: brandtbucher
- ref: warmer_side_exits
- machine: windows-x86
- commit hash: 8423e72
- commit date: 2024-07-01
- overall geometric mean: 1.00x slower
- HPT reliability: 99.86%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240701-pythonperf1_win32-x86-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240701-pythonperf1_win32-x86-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 261 ms                                                                         | 264 ms: 1.01x slower                                                              |
| docutils       | 1.98 sec                                                                       | 2.00 sec: 1.01x slower                                                            |
| html5lib       | 50.1 ms                                                                        | 51.6 ms: 1.03x slower                                                             |
| Geometric mean | (ref)                                                                          | 1.01x slower                                                                      |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240701-pythonperf1_win32-x86-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240701-pythonperf1_win32-x86-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------------------|:------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 493 ms                                                                         | 472 ms: 1.04x faster                                                              |
| async_tree_cpu_io_mixed    | 506 ms                                                                         | 490 ms: 1.03x faster                                                              |
| Geometric mean             | (ref)                                                                          | 1.01x faster                                                                      |

Benchmark hidden because not significant (6): async_tree_io, async_tree_io_tg, async_tree_none_tg, async_tree_memoization_tg, async_tree_memoization, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240701-pythonperf1_win32-x86-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240701-pythonperf1_win32-x86-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 55.3 ms                                                                        | 51.5 ms: 1.07x faster                                                             |
| float          | 44.5 ms                                                                        | 45.6 ms: 1.02x slower                                                             |
| Geometric mean | (ref)                                                                          | 1.02x faster                                                                      |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240701-pythonperf1_win32-x86-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240701-pythonperf1_win32-x86-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_dna      | 120 ms                                                                         | 119 ms: 1.01x faster                                                              |
| regex_v8       | 16.0 ms                                                                        | 15.9 ms: 1.00x faster                                                             |
| regex_compile  | 100.0 ms                                                                       | 101 ms: 1.01x slower                                                              |
| Geometric mean | (ref)                                                                          | 1.00x faster                                                                      |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240701-pythonperf1_win32-x86-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240701-pythonperf1_win32-x86-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------------|:------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| unpickle_pure_python | 159 us                                                                         | 130 us: 1.22x faster                                                              |
| xml_etree_generate   | 63.9 ms                                                                        | 63.0 ms: 1.01x faster                                                             |
| json_loads           | 21.2 us                                                                        | 20.9 us: 1.01x faster                                                             |
| xml_etree_iterparse  | 62.7 ms                                                                        | 63.5 ms: 1.01x slower                                                             |
| json_dumps           | 7.26 ms                                                                        | 7.39 ms: 1.02x slower                                                             |
| tomli_loads          | 1.57 sec                                                                       | 1.63 sec: 1.04x slower                                                            |
| Geometric mean       | (ref)                                                                          | 1.02x faster                                                                      |

Benchmark hidden because not significant (3): xml_etree_process, pickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240701-pythonperf1_win32-x86-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240701-pythonperf1_win32-x86-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup | 23.4 ms                                                                        | 23.2 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                                          | 1.01x faster                                                                      |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240701-pythonperf1_win32-x86-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240701-pythonperf1_win32-x86-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako           | 5.36 ms                                                                        | 5.43 ms: 1.01x slower                                                             |
| genshi_text    | 24.0 ms                                                                        | 25.8 ms: 1.07x slower                                                             |
| Geometric mean | (ref)                                                                          | 1.02x slower                                                                      |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20240701-pythonperf1_win32-x86-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240701-pythonperf1_win32-x86-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------------------|:------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| unpickle_pure_python       | 159 us                                                                         | 130 us: 1.22x faster                                                              |
| fannkuch                   | 236 ms                                                                         | 216 ms: 1.09x faster                                                              |
| nbody                      | 55.3 ms                                                                        | 51.5 ms: 1.07x faster                                                             |
| deltablue                  | 2.95 ms                                                                        | 2.82 ms: 1.05x faster                                                             |
| async_tree_cpu_io_mixed_tg | 493 ms                                                                         | 472 ms: 1.04x faster                                                              |
| async_tree_cpu_io_mixed    | 506 ms                                                                         | 490 ms: 1.03x faster                                                              |
| comprehensions             | 11.5 us                                                                        | 11.1 us: 1.03x faster                                                             |
| richards_super             | 44.2 ms                                                                        | 42.9 ms: 1.03x faster                                                             |
| json                       | 4.28 ms                                                                        | 4.16 ms: 1.03x faster                                                             |
| thrift                     | 808 us                                                                         | 786 us: 1.03x faster                                                              |
| coroutines                 | 19.8 ms                                                                        | 19.3 ms: 1.02x faster                                                             |
| nqueens                    | 73.2 ms                                                                        | 71.6 ms: 1.02x faster                                                             |
| logging_format             | 8.86 us                                                                        | 8.69 us: 1.02x faster                                                             |
| deepcopy_reduce            | 2.64 us                                                                        | 2.59 us: 1.02x faster                                                             |
| logging_simple             | 8.18 us                                                                        | 8.05 us: 1.02x faster                                                             |
| logging_silent             | 59.9 ns                                                                        | 59.0 ns: 1.01x faster                                                             |
| deepcopy                   | 254 us                                                                         | 250 us: 1.01x faster                                                              |
| xml_etree_generate         | 63.9 ms                                                                        | 63.0 ms: 1.01x faster                                                             |
| regex_dna                  | 120 ms                                                                         | 119 ms: 1.01x faster                                                              |
| json_loads                 | 21.2 us                                                                        | 20.9 us: 1.01x faster                                                             |
| python_startup             | 23.4 ms                                                                        | 23.2 ms: 1.01x faster                                                             |
| telco                      | 5.65 ms                                                                        | 5.61 ms: 1.01x faster                                                             |
| regex_v8                   | 16.0 ms                                                                        | 15.9 ms: 1.00x faster                                                             |
| meteor_contest             | 76.2 ms                                                                        | 76.5 ms: 1.00x slower                                                             |
| async_generators           | 336 ms                                                                         | 338 ms: 1.00x slower                                                              |
| crypto_pyaes               | 48.0 ms                                                                        | 48.3 ms: 1.01x slower                                                             |
| regex_compile              | 100.0 ms                                                                       | 101 ms: 1.01x slower                                                              |
| go                         | 121 ms                                                                         | 122 ms: 1.01x slower                                                              |
| generators                 | 29.9 ms                                                                        | 30.2 ms: 1.01x slower                                                             |
| 2to3                       | 261 ms                                                                         | 264 ms: 1.01x slower                                                              |
| mako                       | 5.36 ms                                                                        | 5.43 ms: 1.01x slower                                                             |
| hexiom                     | 4.63 ms                                                                        | 4.68 ms: 1.01x slower                                                             |
| docutils                   | 1.98 sec                                                                       | 2.00 sec: 1.01x slower                                                            |
| pprint_pformat             | 1.22 sec                                                                       | 1.23 sec: 1.01x slower                                                            |
| pprint_safe_repr           | 594 ms                                                                         | 602 ms: 1.01x slower                                                              |
| xml_etree_iterparse        | 62.7 ms                                                                        | 63.5 ms: 1.01x slower                                                             |
| deepcopy_memo              | 16.3 us                                                                        | 16.5 us: 1.01x slower                                                             |
| create_gc_cycles           | 750 us                                                                         | 761 us: 1.02x slower                                                              |
| scimark_monte_carlo        | 42.2 ms                                                                        | 42.9 ms: 1.02x slower                                                             |
| json_dumps                 | 7.26 ms                                                                        | 7.39 ms: 1.02x slower                                                             |
| typing_runtime_protocols   | 157 us                                                                         | 160 us: 1.02x slower                                                              |
| chaos                      | 54.7 ms                                                                        | 55.7 ms: 1.02x slower                                                             |
| sqlglot_optimize           | 45.7 ms                                                                        | 46.6 ms: 1.02x slower                                                             |
| sympy_str                  | 224 ms                                                                         | 229 ms: 1.02x slower                                                              |
| scimark_fft                | 163 ms                                                                         | 166 ms: 1.02x slower                                                              |
| pycparser                  | 897 ms                                                                         | 917 ms: 1.02x slower                                                              |
| float                      | 44.5 ms                                                                        | 45.6 ms: 1.02x slower                                                             |
| scimark_lu                 | 82.1 ms                                                                        | 84.2 ms: 1.03x slower                                                             |
| html5lib                   | 50.1 ms                                                                        | 51.6 ms: 1.03x slower                                                             |
| sympy_integrate            | 16.0 ms                                                                        | 16.6 ms: 1.04x slower                                                             |
| tomli_loads                | 1.57 sec                                                                       | 1.63 sec: 1.04x slower                                                            |
| sympy_sum                  | 111 ms                                                                         | 115 ms: 1.04x slower                                                              |
| richards                   | 36.0 ms                                                                        | 37.5 ms: 1.04x slower                                                             |
| sqlglot_transpile          | 1.24 ms                                                                        | 1.29 ms: 1.04x slower                                                             |
| mdp                        | 1.65 sec                                                                       | 1.73 sec: 1.05x slower                                                            |
| sqlglot_parse              | 967 us                                                                         | 1.02 ms: 1.05x slower                                                             |
| sympy_expand               | 391 ms                                                                         | 413 ms: 1.06x slower                                                              |
| raytrace                   | 252 ms                                                                         | 268 ms: 1.07x slower                                                              |
| genshi_text                | 24.0 ms                                                                        | 25.8 ms: 1.07x slower                                                             |
| Geometric mean             | (ref)                                                                          | 1.00x slower                                                                      |

Benchmark hidden because not significant (28): asyncio_tcp, scimark_sor, pathlib, pyflate, coverage, django_template, bench_thread_pool, python_startup_no_site, async_tree_io, sqlglot_normalize, scimark_sparse_mat_mult, regex_effbot, async_tree_io_tg, xml_etree_process, tornado_http, spectral_norm, gc_traversal, pidigits, asyncio_tcp_ssl, genshi_xml, async_tree_none_tg, pickle_pure_python, async_tree_memoization_tg, bench_mp_pool, xml_etree_parse, async_tree_memoization, async_tree_none, pylint

# HPT report

- Reliability score: 99.86% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown