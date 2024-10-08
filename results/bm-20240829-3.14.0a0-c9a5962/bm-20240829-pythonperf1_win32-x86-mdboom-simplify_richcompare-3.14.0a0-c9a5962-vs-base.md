# Results vs. base

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-x86
- commit hash: c9a5962
- commit date: 2024-08-29
- overall geometric mean: 1.02x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                                         | 248 ms: 1.01x faster                                                           |
| docutils       | 1.89 sec                                                                       | 1.86 sec: 1.02x faster                                                         |
| html5lib       | 46.5 ms                                                                        | 45.8 ms: 1.01x faster                                                          |
| tornado_http   | 106 ms                                                                         | 104 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                                          | 1.01x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none            | 226 ms                                                                         | 213 ms: 1.06x faster                                                           |
| async_tree_io              | 556 ms                                                                         | 533 ms: 1.04x faster                                                           |
| async_tree_memoization     | 284 ms                                                                         | 274 ms: 1.04x faster                                                           |
| async_tree_cpu_io_mixed    | 479 ms                                                                         | 464 ms: 1.03x faster                                                           |
| async_tree_memoization_tg  | 257 ms                                                                         | 249 ms: 1.03x faster                                                           |
| async_tree_io_tg           | 531 ms                                                                         | 515 ms: 1.03x faster                                                           |
| async_tree_cpu_io_mixed_tg | 471 ms                                                                         | 460 ms: 1.02x faster                                                           |
| coroutines                 | 17.7 ms                                                                        | 17.4 ms: 1.02x faster                                                          |
| async_generators           | 294 ms                                                                         | 292 ms: 1.00x faster                                                           |
| Geometric mean             | (ref)                                                                          | 1.03x faster                                                                   |

Benchmark hidden because not significant (3): async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 97.8 ms                                                                        | 94.3 ms: 1.04x faster                                                          |
| pidigits       | 198 ms                                                                         | 201 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                                          | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 121 ms                                                                         | 118 ms: 1.02x faster                                                           |
| regex_compile  | 110 ms                                                                         | 107 ms: 1.02x faster                                                           |
| regex_effbot   | 1.94 ms                                                                        | 1.92 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                                          | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 1.91 sec                                                                       | 1.84 sec: 1.04x faster                                                         |
| xml_etree_process    | 51.2 ms                                                                        | 49.9 ms: 1.03x faster                                                          |
| json_loads           | 20.7 us                                                                        | 20.3 us: 1.02x faster                                                          |
| json_dumps           | 7.52 ms                                                                        | 7.39 ms: 1.02x faster                                                          |
| xml_etree_iterparse  | 68.1 ms                                                                        | 68.8 ms: 1.01x slower                                                          |
| xml_etree_parse      | 108 ms                                                                         | 109 ms: 1.01x slower                                                           |
| unpickle_pure_python | 180 us                                                                         | 183 us: 1.02x slower                                                           |
| pickle_pure_python   | 258 us                                                                         | 263 us: 1.02x slower                                                           |
| Geometric mean       | (ref)                                                                          | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|-----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| django_template | 33.2 ms                                                                        | 31.9 ms: 1.04x faster                                                          |
| mako            | 8.45 ms                                                                        | 8.24 ms: 1.03x faster                                                          |
| genshi_text     | 22.3 ms                                                                        | 22.0 ms: 1.01x faster                                                          |
| genshi_xml      | 45.9 ms                                                                        | 46.1 ms: 1.00x slower                                                          |
| Geometric mean  | (ref)                                                                          | 1.02x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols   | 158 us                                                                         | 143 us: 1.11x faster                                                           |
| raytrace                   | 245 ms                                                                         | 229 ms: 1.07x faster                                                           |
| async_tree_none            | 226 ms                                                                         | 213 ms: 1.06x faster                                                           |
| chaos                      | 55.5 ms                                                                        | 52.8 ms: 1.05x faster                                                          |
| thrift                     | 752 us                                                                         | 719 us: 1.05x faster                                                           |
| telco                      | 6.99 ms                                                                        | 6.69 ms: 1.04x faster                                                          |
| sqlglot_parse              | 1.12 ms                                                                        | 1.07 ms: 1.04x faster                                                          |
| async_tree_io              | 556 ms                                                                         | 533 ms: 1.04x faster                                                           |
| sqlglot_transpile          | 1.38 ms                                                                        | 1.32 ms: 1.04x faster                                                          |
| richards_super             | 45.7 ms                                                                        | 43.9 ms: 1.04x faster                                                          |
| crypto_pyaes               | 58.9 ms                                                                        | 56.7 ms: 1.04x faster                                                          |
| django_template            | 33.2 ms                                                                        | 31.9 ms: 1.04x faster                                                          |
| tomli_loads                | 1.91 sec                                                                       | 1.84 sec: 1.04x faster                                                         |
| logging_format             | 8.94 us                                                                        | 8.61 us: 1.04x faster                                                          |
| nbody                      | 97.8 ms                                                                        | 94.3 ms: 1.04x faster                                                          |
| nqueens                    | 78.0 ms                                                                        | 75.3 ms: 1.04x faster                                                          |
| richards                   | 40.8 ms                                                                        | 39.4 ms: 1.04x faster                                                          |
| async_tree_memoization     | 284 ms                                                                         | 274 ms: 1.04x faster                                                           |
| async_tree_cpu_io_mixed    | 479 ms                                                                         | 464 ms: 1.03x faster                                                           |
| async_tree_memoization_tg  | 257 ms                                                                         | 249 ms: 1.03x faster                                                           |
| async_tree_io_tg           | 531 ms                                                                         | 515 ms: 1.03x faster                                                           |
| deepcopy                   | 249 us                                                                         | 242 us: 1.03x faster                                                           |
| scimark_sparse_mat_mult    | 3.23 ms                                                                        | 3.14 ms: 1.03x faster                                                          |
| deepcopy_reduce            | 2.48 us                                                                        | 2.42 us: 1.03x faster                                                          |
| comprehensions             | 14.0 us                                                                        | 13.7 us: 1.03x faster                                                          |
| logging_simple             | 8.15 us                                                                        | 7.94 us: 1.03x faster                                                          |
| xml_etree_process          | 51.2 ms                                                                        | 49.9 ms: 1.03x faster                                                          |
| pprint_safe_repr           | 658 ms                                                                         | 642 ms: 1.03x faster                                                           |
| mako                       | 8.45 ms                                                                        | 8.24 ms: 1.03x faster                                                          |
| generators                 | 27.5 ms                                                                        | 26.8 ms: 1.02x faster                                                          |
| async_tree_cpu_io_mixed_tg | 471 ms                                                                         | 460 ms: 1.02x faster                                                           |
| regex_dna                  | 121 ms                                                                         | 118 ms: 1.02x faster                                                           |
| sympy_str                  | 219 ms                                                                         | 215 ms: 1.02x faster                                                           |
| json_loads                 | 20.7 us                                                                        | 20.3 us: 1.02x faster                                                          |
| regex_compile              | 110 ms                                                                         | 107 ms: 1.02x faster                                                           |
| dulwich_log                | 50.9 ms                                                                        | 49.9 ms: 1.02x faster                                                          |
| pprint_pformat             | 1.35 sec                                                                       | 1.33 sec: 1.02x faster                                                         |
| logging_silent             | 74.6 ns                                                                        | 73.1 ns: 1.02x faster                                                          |
| sympy_sum                  | 109 ms                                                                         | 107 ms: 1.02x faster                                                           |
| coroutines                 | 17.7 ms                                                                        | 17.4 ms: 1.02x faster                                                          |
| sqlglot_normalize          | 230 ms                                                                         | 225 ms: 1.02x faster                                                           |
| pyflate                    | 360 ms                                                                         | 354 ms: 1.02x faster                                                           |
| json_dumps                 | 7.52 ms                                                                        | 7.39 ms: 1.02x faster                                                          |
| tornado_http               | 106 ms                                                                         | 104 ms: 1.02x faster                                                           |
| docutils                   | 1.89 sec                                                                       | 1.86 sec: 1.02x faster                                                         |
| html5lib                   | 46.5 ms                                                                        | 45.8 ms: 1.01x faster                                                          |
| hexiom                     | 5.27 ms                                                                        | 5.20 ms: 1.01x faster                                                          |
| scimark_lu                 | 69.6 ms                                                                        | 68.7 ms: 1.01x faster                                                          |
| pycparser                  | 873 ms                                                                         | 862 ms: 1.01x faster                                                           |
| genshi_text                | 22.3 ms                                                                        | 22.0 ms: 1.01x faster                                                          |
| sympy_integrate            | 15.7 ms                                                                        | 15.5 ms: 1.01x faster                                                          |
| regex_effbot               | 1.94 ms                                                                        | 1.92 ms: 1.01x faster                                                          |
| deltablue                  | 2.74 ms                                                                        | 2.71 ms: 1.01x faster                                                          |
| sympy_expand               | 386 ms                                                                         | 383 ms: 1.01x faster                                                           |
| sqlglot_optimize           | 44.2 ms                                                                        | 43.8 ms: 1.01x faster                                                          |
| scimark_fft                | 239 ms                                                                         | 237 ms: 1.01x faster                                                           |
| 2to3                       | 250 ms                                                                         | 248 ms: 1.01x faster                                                           |
| go                         | 105 ms                                                                         | 104 ms: 1.01x faster                                                           |
| async_generators           | 294 ms                                                                         | 292 ms: 1.00x faster                                                           |
| genshi_xml                 | 45.9 ms                                                                        | 46.1 ms: 1.00x slower                                                          |
| fannkuch                   | 334 ms                                                                         | 336 ms: 1.01x slower                                                           |
| gc_traversal               | 1.43 ms                                                                        | 1.45 ms: 1.01x slower                                                          |
| xml_etree_iterparse        | 68.1 ms                                                                        | 68.8 ms: 1.01x slower                                                          |
| xml_etree_parse            | 108 ms                                                                         | 109 ms: 1.01x slower                                                           |
| coverage                   | 52.8 ms                                                                        | 53.6 ms: 1.01x slower                                                          |
| pidigits                   | 198 ms                                                                         | 201 ms: 1.02x slower                                                           |
| unpickle_pure_python       | 180 us                                                                         | 183 us: 1.02x slower                                                           |
| pickle_pure_python         | 258 us                                                                         | 263 us: 1.02x slower                                                           |
| spectral_norm              | 76.2 ms                                                                        | 77.6 ms: 1.02x slower                                                          |
| scimark_monte_carlo        | 56.0 ms                                                                        | 57.4 ms: 1.02x slower                                                          |
| Geometric mean             | (ref)                                                                          | 1.02x faster                                                                   |

Benchmark hidden because not significant (18): async_tree_none_tg, asyncio_tcp, pylint, json, scimark_sor, create_gc_cycles, xml_etree_generate, python_startup, regex_v8, mdp, asyncio_tcp_ssl, pathlib, bench_mp_pool, deepcopy_memo, meteor_contest, float, python_startup_no_site, bench_thread_pool

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown