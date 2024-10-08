# Results vs. base

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-x86
- commit hash: 2fa7b0e
- commit date: 2024-09-04
- overall geometric mean: 1.01x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 256 ms                                                                         | 251 ms: 1.02x faster                                                           |
| docutils       | 1.87 sec                                                                       | 1.86 sec: 1.01x faster                                                         |
| html5lib       | 45.4 ms                                                                        | 46.5 ms: 1.02x slower                                                          |
| tornado_http   | 103 ms                                                                         | 105 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                                          | 1.00x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 475 ms                                                                         | 460 ms: 1.03x faster                                                           |
| async_generators           | 307 ms                                                                         | 299 ms: 1.03x faster                                                           |
| coroutines                 | 18.0 ms                                                                        | 17.5 ms: 1.03x faster                                                          |
| async_tree_cpu_io_mixed_tg | 468 ms                                                                         | 456 ms: 1.03x faster                                                           |
| async_tree_memoization     | 277 ms                                                                         | 273 ms: 1.01x faster                                                           |
| Geometric mean             | (ref)                                                                          | 1.01x faster                                                                   |

Benchmark hidden because not significant (7): async_tree_none_tg, async_tree_none, async_tree_io, async_tree_io_tg, asyncio_tcp_ssl, async_tree_memoization_tg, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 61.9 ms                                                                        | 60.8 ms: 1.02x faster                                                          |
| pidigits       | 197 ms                                                                         | 201 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                                          | 1.00x faster                                                                   |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 132 ms                                                                         | 123 ms: 1.07x faster                                                           |
| regex_effbot   | 2.01 ms                                                                        | 1.93 ms: 1.04x faster                                                          |
| Geometric mean | (ref)                                                                          | 1.03x faster                                                                   |

Benchmark hidden because not significant (2): regex_v8, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle_pure_python | 179 us                                                                         | 171 us: 1.04x faster                                                           |
| tomli_loads          | 1.91 sec                                                                       | 1.89 sec: 1.01x faster                                                         |
| xml_etree_process    | 49.8 ms                                                                        | 49.3 ms: 1.01x faster                                                          |
| json_dumps           | 7.48 ms                                                                        | 7.42 ms: 1.01x faster                                                          |
| json_loads           | 20.5 us                                                                        | 20.4 us: 1.01x faster                                                          |
| pickle_pure_python   | 253 us                                                                         | 254 us: 1.01x slower                                                           |
| xml_etree_parse      | 107 ms                                                                         | 108 ms: 1.01x slower                                                           |
| xml_etree_generate   | 66.7 ms                                                                        | 67.9 ms: 1.02x slower                                                          |
| Geometric mean       | (ref)                                                                          | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_text    | 22.2 ms                                                                        | 21.6 ms: 1.03x faster                                                          |
| genshi_xml     | 47.2 ms                                                                        | 46.5 ms: 1.01x faster                                                          |
| mako           | 8.46 ms                                                                        | 8.38 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                                          | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| scimark_monte_carlo        | 59.1 ms                                                                        | 55.0 ms: 1.07x faster                                                          |
| regex_dna                  | 132 ms                                                                         | 123 ms: 1.07x faster                                                           |
| scimark_sor                | 104 ms                                                                         | 98.5 ms: 1.06x faster                                                          |
| unpickle_pure_python       | 179 us                                                                         | 171 us: 1.04x faster                                                           |
| crypto_pyaes               | 60.4 ms                                                                        | 57.8 ms: 1.04x faster                                                          |
| sqlglot_optimize           | 44.5 ms                                                                        | 42.8 ms: 1.04x faster                                                          |
| raytrace                   | 245 ms                                                                         | 236 ms: 1.04x faster                                                           |
| regex_effbot               | 2.01 ms                                                                        | 1.93 ms: 1.04x faster                                                          |
| logging_format             | 8.89 us                                                                        | 8.55 us: 1.04x faster                                                          |
| sqlglot_normalize          | 232 ms                                                                         | 223 ms: 1.04x faster                                                           |
| richards                   | 39.8 ms                                                                        | 38.5 ms: 1.04x faster                                                          |
| spectral_norm              | 78.5 ms                                                                        | 75.8 ms: 1.04x faster                                                          |
| nqueens                    | 78.6 ms                                                                        | 76.1 ms: 1.03x faster                                                          |
| async_tree_cpu_io_mixed    | 475 ms                                                                         | 460 ms: 1.03x faster                                                           |
| logging_simple             | 8.17 us                                                                        | 7.92 us: 1.03x faster                                                          |
| genshi_text                | 22.2 ms                                                                        | 21.6 ms: 1.03x faster                                                          |
| richards_super             | 44.4 ms                                                                        | 43.3 ms: 1.03x faster                                                          |
| async_generators           | 307 ms                                                                         | 299 ms: 1.03x faster                                                           |
| coroutines                 | 18.0 ms                                                                        | 17.5 ms: 1.03x faster                                                          |
| async_tree_cpu_io_mixed_tg | 468 ms                                                                         | 456 ms: 1.03x faster                                                           |
| thrift                     | 753 us                                                                         | 735 us: 1.02x faster                                                           |
| scimark_lu                 | 71.9 ms                                                                        | 70.2 ms: 1.02x faster                                                          |
| deltablue                  | 2.70 ms                                                                        | 2.64 ms: 1.02x faster                                                          |
| pprint_safe_repr           | 665 ms                                                                         | 651 ms: 1.02x faster                                                           |
| dulwich_log                | 50.6 ms                                                                        | 49.7 ms: 1.02x faster                                                          |
| comprehensions             | 13.8 us                                                                        | 13.5 us: 1.02x faster                                                          |
| mdp                        | 1.73 sec                                                                       | 1.70 sec: 1.02x faster                                                         |
| float                      | 61.9 ms                                                                        | 60.8 ms: 1.02x faster                                                          |
| fannkuch                   | 334 ms                                                                         | 328 ms: 1.02x faster                                                           |
| 2to3                       | 256 ms                                                                         | 251 ms: 1.02x faster                                                           |
| scimark_sparse_mat_mult    | 3.17 ms                                                                        | 3.12 ms: 1.02x faster                                                          |
| json                       | 4.25 ms                                                                        | 4.19 ms: 1.01x faster                                                          |
| genshi_xml                 | 47.2 ms                                                                        | 46.5 ms: 1.01x faster                                                          |
| async_tree_memoization     | 277 ms                                                                         | 273 ms: 1.01x faster                                                           |
| tomli_loads                | 1.91 sec                                                                       | 1.89 sec: 1.01x faster                                                         |
| pyflate                    | 360 ms                                                                         | 357 ms: 1.01x faster                                                           |
| xml_etree_process          | 49.8 ms                                                                        | 49.3 ms: 1.01x faster                                                          |
| gc_traversal               | 1.43 ms                                                                        | 1.42 ms: 1.01x faster                                                          |
| pprint_pformat             | 1.35 sec                                                                       | 1.34 sec: 1.01x faster                                                         |
| sqlglot_parse              | 1.09 ms                                                                        | 1.08 ms: 1.01x faster                                                          |
| deepcopy_reduce            | 2.46 us                                                                        | 2.43 us: 1.01x faster                                                          |
| docutils                   | 1.87 sec                                                                       | 1.86 sec: 1.01x faster                                                         |
| sympy_sum                  | 108 ms                                                                         | 107 ms: 1.01x faster                                                           |
| mako                       | 8.46 ms                                                                        | 8.38 ms: 1.01x faster                                                          |
| json_dumps                 | 7.48 ms                                                                        | 7.42 ms: 1.01x faster                                                          |
| sqlglot_transpile          | 1.34 ms                                                                        | 1.33 ms: 1.01x faster                                                          |
| sympy_expand               | 381 ms                                                                         | 379 ms: 1.01x faster                                                           |
| json_loads                 | 20.5 us                                                                        | 20.4 us: 1.01x faster                                                          |
| telco                      | 6.95 ms                                                                        | 6.92 ms: 1.00x faster                                                          |
| scimark_fft                | 240 ms                                                                         | 241 ms: 1.00x slower                                                           |
| pickle_pure_python         | 253 us                                                                         | 254 us: 1.01x slower                                                           |
| deepcopy_memo              | 22.3 us                                                                        | 22.5 us: 1.01x slower                                                          |
| pathlib                    | 87.0 ms                                                                        | 87.8 ms: 1.01x slower                                                          |
| xml_etree_parse            | 107 ms                                                                         | 108 ms: 1.01x slower                                                           |
| logging_silent             | 73.9 ns                                                                        | 74.7 ns: 1.01x slower                                                          |
| coverage                   | 50.8 ms                                                                        | 51.5 ms: 1.01x slower                                                          |
| typing_runtime_protocols   | 148 us                                                                         | 151 us: 1.02x slower                                                           |
| tornado_http               | 103 ms                                                                         | 105 ms: 1.02x slower                                                           |
| pidigits                   | 197 ms                                                                         | 201 ms: 1.02x slower                                                           |
| xml_etree_generate         | 66.7 ms                                                                        | 67.9 ms: 1.02x slower                                                          |
| generators                 | 27.2 ms                                                                        | 27.7 ms: 1.02x slower                                                          |
| bench_mp_pool              | 73.2 ms                                                                        | 74.9 ms: 1.02x slower                                                          |
| html5lib                   | 45.4 ms                                                                        | 46.5 ms: 1.02x slower                                                          |
| deepcopy                   | 237 us                                                                         | 247 us: 1.04x slower                                                           |
| Geometric mean             | (ref)                                                                          | 1.01x faster                                                                   |

Benchmark hidden because not significant (24): bench_thread_pool, async_tree_none_tg, async_tree_none, regex_v8, go, async_tree_io, async_tree_io_tg, nbody, chaos, meteor_contest, xml_etree_iterparse, sympy_str, asyncio_tcp_ssl, regex_compile, async_tree_memoization_tg, create_gc_cycles, hexiom, sympy_integrate, pylint, django_template, python_startup, pycparser, python_startup_no_site, asyncio_tcp

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown