# Results vs. base

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-x86
- commit hash: 15b187e
- commit date: 2024-08-29
- overall geometric mean: 1.00x faster
- HPT reliability: 61.01%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| html5lib       | 46.8 ms                                                                        | 46.5 ms: 1.01x faster                                                          |
| tornado_http   | 106 ms                                                                         | 105 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                                          | 1.00x faster                                                                   |

Benchmark hidden because not significant (2): 2to3, docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| coroutines                 | 17.7 ms                                                                        | 17.5 ms: 1.01x faster                                                          |
| async_tree_memoization     | 273 ms                                                                         | 276 ms: 1.01x slower                                                           |
| async_generators           | 304 ms                                                                         | 307 ms: 1.01x slower                                                           |
| async_tree_cpu_io_mixed_tg | 459 ms                                                                         | 465 ms: 1.01x slower                                                           |
| Geometric mean             | (ref)                                                                          | 1.01x slower                                                                   |

Benchmark hidden because not significant (8): asyncio_tcp, asyncio_tcp_ssl, async_tree_cpu_io_mixed, async_tree_none, async_tree_io_tg, async_tree_none_tg, async_tree_io, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 62.3 ms                                                                        | 62.0 ms: 1.01x faster                                                          |
| pidigits       | 198 ms                                                                         | 202 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                                          | 1.00x slower                                                                   |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 124 ms                                                                         | 122 ms: 1.02x faster                                                           |
| regex_compile  | 108 ms                                                                         | 107 ms: 1.01x faster                                                           |
| regex_v8       | 16.1 ms                                                                        | 16.2 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                                          | 1.00x faster                                                                   |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 1.92 sec                                                                       | 1.86 sec: 1.03x faster                                                         |
| pickle_pure_python   | 262 us                                                                         | 254 us: 1.03x faster                                                           |
| xml_etree_process    | 50.6 ms                                                                        | 51.0 ms: 1.01x slower                                                          |
| json_dumps           | 7.60 ms                                                                        | 7.74 ms: 1.02x slower                                                          |
| unpickle_pure_python | 174 us                                                                         | 179 us: 1.02x slower                                                           |
| Geometric mean       | (ref)                                                                          | 1.00x faster                                                                   |

Benchmark hidden because not significant (4): xml_etree_parse, json_loads, xml_etree_iterparse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|------------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.9 ms                                                                        | 19.7 ms: 1.01x faster                                                          |
| Geometric mean         | (ref)                                                                          | 1.00x faster                                                                   |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_text    | 22.2 ms                                                                        | 21.8 ms: 1.02x faster                                                          |
| genshi_xml     | 47.2 ms                                                                        | 46.8 ms: 1.01x faster                                                          |
| mako           | 8.35 ms                                                                        | 8.41 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                                          | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| scimark_sparse_mat_mult    | 3.54 ms                                                                        | 3.19 ms: 1.11x faster                                                          |
| tomli_loads                | 1.92 sec                                                                       | 1.86 sec: 1.03x faster                                                         |
| comprehensions             | 14.0 us                                                                        | 13.5 us: 1.03x faster                                                          |
| pickle_pure_python         | 262 us                                                                         | 254 us: 1.03x faster                                                           |
| chaos                      | 54.9 ms                                                                        | 53.5 ms: 1.02x faster                                                          |
| genshi_text                | 22.2 ms                                                                        | 21.8 ms: 1.02x faster                                                          |
| logging_silent             | 76.0 ns                                                                        | 74.5 ns: 1.02x faster                                                          |
| thrift                     | 742 us                                                                         | 727 us: 1.02x faster                                                           |
| nqueens                    | 77.3 ms                                                                        | 75.9 ms: 1.02x faster                                                          |
| meteor_contest             | 81.3 ms                                                                        | 79.9 ms: 1.02x faster                                                          |
| sqlglot_parse              | 1.09 ms                                                                        | 1.07 ms: 1.02x faster                                                          |
| richards                   | 39.6 ms                                                                        | 39.0 ms: 1.02x faster                                                          |
| regex_dna                  | 124 ms                                                                         | 122 ms: 1.02x faster                                                           |
| scimark_lu                 | 71.7 ms                                                                        | 70.6 ms: 1.02x faster                                                          |
| spectral_norm              | 76.7 ms                                                                        | 75.6 ms: 1.01x faster                                                          |
| mdp                        | 1.72 sec                                                                       | 1.70 sec: 1.01x faster                                                         |
| pycparser                  | 868 ms                                                                         | 857 ms: 1.01x faster                                                           |
| sqlglot_transpile          | 1.34 ms                                                                        | 1.32 ms: 1.01x faster                                                          |
| gc_traversal               | 1.45 ms                                                                        | 1.44 ms: 1.01x faster                                                          |
| tornado_http               | 106 ms                                                                         | 105 ms: 1.01x faster                                                           |
| sqlglot_normalize          | 225 ms                                                                         | 223 ms: 1.01x faster                                                           |
| coroutines                 | 17.7 ms                                                                        | 17.5 ms: 1.01x faster                                                          |
| bench_mp_pool              | 73.4 ms                                                                        | 72.8 ms: 1.01x faster                                                          |
| regex_compile              | 108 ms                                                                         | 107 ms: 1.01x faster                                                           |
| genshi_xml                 | 47.2 ms                                                                        | 46.8 ms: 1.01x faster                                                          |
| pprint_pformat             | 1.34 sec                                                                       | 1.33 sec: 1.01x faster                                                         |
| sqlglot_optimize           | 43.8 ms                                                                        | 43.5 ms: 1.01x faster                                                          |
| python_startup_no_site     | 19.9 ms                                                                        | 19.7 ms: 1.01x faster                                                          |
| html5lib                   | 46.8 ms                                                                        | 46.5 ms: 1.01x faster                                                          |
| float                      | 62.3 ms                                                                        | 62.0 ms: 1.01x faster                                                          |
| sympy_expand               | 383 ms                                                                         | 381 ms: 1.00x faster                                                           |
| logging_simple             | 7.97 us                                                                        | 8.02 us: 1.01x slower                                                          |
| logging_format             | 8.73 us                                                                        | 8.78 us: 1.01x slower                                                          |
| regex_v8                   | 16.1 ms                                                                        | 16.2 ms: 1.01x slower                                                          |
| mako                       | 8.35 ms                                                                        | 8.41 ms: 1.01x slower                                                          |
| async_tree_memoization     | 273 ms                                                                         | 276 ms: 1.01x slower                                                           |
| xml_etree_process          | 50.6 ms                                                                        | 51.0 ms: 1.01x slower                                                          |
| sympy_str                  | 214 ms                                                                         | 216 ms: 1.01x slower                                                           |
| async_generators           | 304 ms                                                                         | 307 ms: 1.01x slower                                                           |
| deepcopy_memo              | 21.8 us                                                                        | 22.0 us: 1.01x slower                                                          |
| pyflate                    | 354 ms                                                                         | 358 ms: 1.01x slower                                                           |
| scimark_fft                | 234 ms                                                                         | 237 ms: 1.01x slower                                                           |
| async_tree_cpu_io_mixed_tg | 459 ms                                                                         | 465 ms: 1.01x slower                                                           |
| scimark_monte_carlo        | 55.9 ms                                                                        | 56.6 ms: 1.01x slower                                                          |
| fannkuch                   | 327 ms                                                                         | 332 ms: 1.01x slower                                                           |
| deltablue                  | 2.68 ms                                                                        | 2.72 ms: 1.02x slower                                                          |
| telco                      | 6.97 ms                                                                        | 7.08 ms: 1.02x slower                                                          |
| hexiom                     | 5.20 ms                                                                        | 5.29 ms: 1.02x slower                                                          |
| pidigits                   | 198 ms                                                                         | 202 ms: 1.02x slower                                                           |
| json_dumps                 | 7.60 ms                                                                        | 7.74 ms: 1.02x slower                                                          |
| unpickle_pure_python       | 174 us                                                                         | 179 us: 1.02x slower                                                           |
| scimark_sor                | 99.5 ms                                                                        | 102 ms: 1.03x slower                                                           |
| generators                 | 27.1 ms                                                                        | 27.9 ms: 1.03x slower                                                          |
| coverage                   | 51.2 ms                                                                        | 54.0 ms: 1.05x slower                                                          |
| Geometric mean             | (ref)                                                                          | 1.00x faster                                                                   |

Benchmark hidden because not significant (34): asyncio_tcp, nbody, asyncio_tcp_ssl, sympy_sum, json, deepcopy, sympy_integrate, docutils, pathlib, crypto_pyaes, typing_runtime_protocols, deepcopy_reduce, bench_thread_pool, xml_etree_parse, pylint, dulwich_log, raytrace, django_template, 2to3, regex_effbot, python_startup, json_loads, async_tree_cpu_io_mixed, xml_etree_iterparse, xml_etree_generate, pprint_safe_repr, create_gc_cycles, go, richards_super, async_tree_none, async_tree_io_tg, async_tree_none_tg, async_tree_io, async_tree_memoization_tg

# HPT report

- Reliability score: 61.01% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown