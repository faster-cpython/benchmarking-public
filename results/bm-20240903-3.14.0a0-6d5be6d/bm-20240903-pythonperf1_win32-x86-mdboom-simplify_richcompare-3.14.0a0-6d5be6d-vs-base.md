# Results vs. base

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-x86
- commit hash: 6d5be6d
- commit date: 2024-09-03
- overall geometric mean: 1.00x faster
- HPT reliability: 75.23%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| docutils       | 1.86 sec                                                                       | 1.86 sec: 1.00x faster                                                         |
| html5lib       | 46.8 ms                                                                        | 46.1 ms: 1.02x faster                                                          |
| tornado_http   | 106 ms                                                                         | 104 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                                          | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| asyncio_tcp                | 756 ms                                                                         | 716 ms: 1.06x faster                                                           |
| async_generators           | 304 ms                                                                         | 297 ms: 1.03x faster                                                           |
| async_tree_cpu_io_mixed_tg | 459 ms                                                                         | 463 ms: 1.01x slower                                                           |
| async_tree_none            | 213 ms                                                                         | 216 ms: 1.01x slower                                                           |
| Geometric mean             | (ref)                                                                          | 1.01x faster                                                                   |

Benchmark hidden because not significant (8): async_tree_io_tg, async_tree_memoization, asyncio_tcp_ssl, async_tree_memoization_tg, async_tree_io, async_tree_none_tg, async_tree_cpu_io_mixed, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 62.3 ms                                                                        | 61.5 ms: 1.01x faster                                                          |
| pidigits       | 198 ms                                                                         | 202 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                                          | 1.00x faster                                                                   |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 124 ms                                                                         | 121 ms: 1.03x faster                                                           |
| regex_v8       | 16.1 ms                                                                        | 16.4 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                                          | 1.00x faster                                                                   |

Benchmark hidden because not significant (2): regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pickle_pure_python   | 262 us                                                                         | 251 us: 1.05x faster                                                           |
| tomli_loads          | 1.92 sec                                                                       | 1.86 sec: 1.03x faster                                                         |
| json_dumps           | 7.60 ms                                                                        | 7.46 ms: 1.02x faster                                                          |
| xml_etree_generate   | 68.1 ms                                                                        | 67.3 ms: 1.01x faster                                                          |
| xml_etree_process    | 50.6 ms                                                                        | 50.0 ms: 1.01x faster                                                          |
| unpickle_pure_python | 174 us                                                                         | 179 us: 1.03x slower                                                           |
| json_loads           | 20.4 us                                                                        | 21.1 us: 1.03x slower                                                          |
| Geometric mean       | (ref)                                                                          | 1.01x faster                                                                   |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|------------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 24.0 ms                                                                        | 23.8 ms: 1.01x faster                                                          |
| python_startup_no_site | 19.9 ms                                                                        | 19.7 ms: 1.01x faster                                                          |
| Geometric mean         | (ref)                                                                          | 1.01x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml     | 47.2 ms                                                                        | 46.1 ms: 1.03x faster                                                          |
| mako           | 8.35 ms                                                                        | 8.20 ms: 1.02x faster                                                          |
| genshi_text    | 22.2 ms                                                                        | 21.9 ms: 1.02x faster                                                          |
| Geometric mean | (ref)                                                                          | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| scimark_sparse_mat_mult    | 3.54 ms                                                                        | 3.15 ms: 1.13x faster                                                          |
| asyncio_tcp                | 756 ms                                                                         | 716 ms: 1.06x faster                                                           |
| pickle_pure_python         | 262 us                                                                         | 251 us: 1.05x faster                                                           |
| deepcopy                   | 247 us                                                                         | 238 us: 1.04x faster                                                           |
| tomli_loads                | 1.92 sec                                                                       | 1.86 sec: 1.03x faster                                                         |
| telco                      | 6.97 ms                                                                        | 6.77 ms: 1.03x faster                                                          |
| comprehensions             | 14.0 us                                                                        | 13.6 us: 1.03x faster                                                          |
| async_generators           | 304 ms                                                                         | 297 ms: 1.03x faster                                                           |
| regex_dna                  | 124 ms                                                                         | 121 ms: 1.03x faster                                                           |
| genshi_xml                 | 47.2 ms                                                                        | 46.1 ms: 1.03x faster                                                          |
| scimark_lu                 | 71.7 ms                                                                        | 70.0 ms: 1.02x faster                                                          |
| sqlglot_optimize           | 43.8 ms                                                                        | 42.9 ms: 1.02x faster                                                          |
| deepcopy_reduce            | 2.51 us                                                                        | 2.46 us: 1.02x faster                                                          |
| raytrace                   | 236 ms                                                                         | 231 ms: 1.02x faster                                                           |
| json_dumps                 | 7.60 ms                                                                        | 7.46 ms: 1.02x faster                                                          |
| mako                       | 8.35 ms                                                                        | 8.20 ms: 1.02x faster                                                          |
| html5lib                   | 46.8 ms                                                                        | 46.1 ms: 1.02x faster                                                          |
| mdp                        | 1.72 sec                                                                       | 1.70 sec: 1.02x faster                                                         |
| sqlglot_parse              | 1.09 ms                                                                        | 1.07 ms: 1.02x faster                                                          |
| logging_silent             | 76.0 ns                                                                        | 74.8 ns: 1.02x faster                                                          |
| genshi_text                | 22.2 ms                                                                        | 21.9 ms: 1.02x faster                                                          |
| tornado_http               | 106 ms                                                                         | 104 ms: 1.01x faster                                                           |
| pprint_pformat             | 1.34 sec                                                                       | 1.32 sec: 1.01x faster                                                         |
| dulwich_log                | 49.9 ms                                                                        | 49.2 ms: 1.01x faster                                                          |
| chaos                      | 54.9 ms                                                                        | 54.1 ms: 1.01x faster                                                          |
| float                      | 62.3 ms                                                                        | 61.5 ms: 1.01x faster                                                          |
| xml_etree_generate         | 68.1 ms                                                                        | 67.3 ms: 1.01x faster                                                          |
| xml_etree_process          | 50.6 ms                                                                        | 50.0 ms: 1.01x faster                                                          |
| pprint_safe_repr           | 650 ms                                                                         | 643 ms: 1.01x faster                                                           |
| sqlglot_normalize          | 225 ms                                                                         | 223 ms: 1.01x faster                                                           |
| gc_traversal               | 1.45 ms                                                                        | 1.44 ms: 1.01x faster                                                          |
| python_startup             | 24.0 ms                                                                        | 23.8 ms: 1.01x faster                                                          |
| logging_format             | 8.73 us                                                                        | 8.65 us: 1.01x faster                                                          |
| python_startup_no_site     | 19.9 ms                                                                        | 19.7 ms: 1.01x faster                                                          |
| logging_simple             | 7.97 us                                                                        | 7.92 us: 1.01x faster                                                          |
| docutils                   | 1.86 sec                                                                       | 1.86 sec: 1.00x faster                                                         |
| sympy_expand               | 383 ms                                                                         | 384 ms: 1.00x slower                                                           |
| sympy_integrate            | 15.4 ms                                                                        | 15.5 ms: 1.01x slower                                                          |
| scimark_monte_carlo        | 55.9 ms                                                                        | 56.4 ms: 1.01x slower                                                          |
| async_tree_cpu_io_mixed_tg | 459 ms                                                                         | 463 ms: 1.01x slower                                                           |
| meteor_contest             | 81.3 ms                                                                        | 82.0 ms: 1.01x slower                                                          |
| sympy_str                  | 214 ms                                                                         | 216 ms: 1.01x slower                                                           |
| create_gc_cycles           | 747 us                                                                         | 754 us: 1.01x slower                                                           |
| coverage                   | 51.2 ms                                                                        | 51.8 ms: 1.01x slower                                                          |
| pyflate                    | 354 ms                                                                         | 358 ms: 1.01x slower                                                           |
| deepcopy_memo              | 21.8 us                                                                        | 22.0 us: 1.01x slower                                                          |
| scimark_fft                | 234 ms                                                                         | 237 ms: 1.01x slower                                                           |
| async_tree_none            | 213 ms                                                                         | 216 ms: 1.01x slower                                                           |
| regex_v8                   | 16.1 ms                                                                        | 16.4 ms: 1.01x slower                                                          |
| go                         | 102 ms                                                                         | 104 ms: 1.02x slower                                                           |
| pidigits                   | 198 ms                                                                         | 202 ms: 1.02x slower                                                           |
| crypto_pyaes               | 58.3 ms                                                                        | 59.5 ms: 1.02x slower                                                          |
| generators                 | 27.1 ms                                                                        | 27.6 ms: 1.02x slower                                                          |
| pycparser                  | 868 ms                                                                         | 888 ms: 1.02x slower                                                           |
| scimark_sor                | 99.5 ms                                                                        | 102 ms: 1.03x slower                                                           |
| nqueens                    | 77.3 ms                                                                        | 79.3 ms: 1.03x slower                                                          |
| deltablue                  | 2.68 ms                                                                        | 2.75 ms: 1.03x slower                                                          |
| unpickle_pure_python       | 174 us                                                                         | 179 us: 1.03x slower                                                           |
| hexiom                     | 5.20 ms                                                                        | 5.36 ms: 1.03x slower                                                          |
| json_loads                 | 20.4 us                                                                        | 21.1 us: 1.03x slower                                                          |
| fannkuch                   | 327 ms                                                                         | 342 ms: 1.04x slower                                                           |
| richards_super             | 44.4 ms                                                                        | 46.9 ms: 1.06x slower                                                          |
| richards                   | 39.6 ms                                                                        | 41.9 ms: 1.06x slower                                                          |
| Geometric mean             | (ref)                                                                          | 1.00x faster                                                                   |

Benchmark hidden because not significant (25): async_tree_io_tg, xml_etree_parse, async_tree_memoization, 2to3, nbody, sympy_sum, regex_compile, sqlglot_transpile, asyncio_tcp_ssl, async_tree_memoization_tg, bench_mp_pool, regex_effbot, json, pathlib, thrift, async_tree_io, bench_thread_pool, xml_etree_iterparse, async_tree_none_tg, async_tree_cpu_io_mixed, spectral_norm, django_template, typing_runtime_protocols, coroutines, pylint

# HPT report

- Reliability score: 75.23% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown