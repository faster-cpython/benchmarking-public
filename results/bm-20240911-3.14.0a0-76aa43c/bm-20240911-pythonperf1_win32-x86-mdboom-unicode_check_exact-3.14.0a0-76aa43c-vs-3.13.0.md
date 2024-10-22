# Results vs. 3.13.0

- fork: mdboom
- ref: unicode_check_exact
- machine: windows-x86
- commit hash: 76aa43c
- commit date: 2024-09-11
- overall geometric mean: 1.03x faster
- HPT reliability: 94.84%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1_win32-x86-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 250 ms: 1.01x faster                                                          |
| docutils       | 1.82 sec                                                        | 1.86 sec: 1.02x slower                                                        |
| html5lib       | 48.3 ms                                                         | 46.5 ms: 1.04x faster                                                         |
| tornado_http   | 104 ms                                                          | 95.8 ms: 1.09x faster                                                         |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1_win32-x86-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| asyncio_tcp                | 842 ms                                                          | 648 ms: 1.30x faster                                                          |
| async_tree_memoization_tg  | 287 ms                                                          | 251 ms: 1.14x faster                                                          |
| async_tree_none            | 246 ms                                                          | 218 ms: 1.13x faster                                                          |
| async_tree_memoization     | 302 ms                                                          | 271 ms: 1.11x faster                                                          |
| async_tree_none_tg         | 219 ms                                                          | 200 ms: 1.09x faster                                                          |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 469 ms: 1.05x faster                                                          |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.1 sec: 1.02x faster                                                        |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 461 ms: 1.01x faster                                                          |
| async_tree_io_tg           | 509 ms                                                          | 516 ms: 1.01x slower                                                          |
| async_generators           | 274 ms                                                          | 297 ms: 1.09x slower                                                          |
| coroutines                 | 15.7 ms                                                         | 18.5 ms: 1.18x slower                                                         |
| Geometric mean             | (ref)                                                           | 1.05x faster                                                                  |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1_win32-x86-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pidigits       | 202 ms                                                          | 201 ms: 1.01x faster                                                          |
| float          | 57.8 ms                                                         | 61.4 ms: 1.06x slower                                                         |
| nbody          | 81.9 ms                                                         | 91.6 ms: 1.12x slower                                                         |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1_win32-x86-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                          | 107 ms: 1.04x slower                                                          |
| regex_v8       | 15.6 ms                                                         | 16.3 ms: 1.04x slower                                                         |
| regex_effbot   | 1.81 ms                                                         | 1.89 ms: 1.04x slower                                                         |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                  |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1_win32-x86-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pickle_dict          | 21.7 us                                                         | 20.5 us: 1.06x faster                                                         |
| pickle               | 8.42 us                                                         | 7.96 us: 1.06x faster                                                         |
| unpickle             | 10.5 us                                                         | 10.4 us: 1.01x faster                                                         |
| json_loads           | 21.0 us                                                         | 20.8 us: 1.01x faster                                                         |
| xml_etree_parse      | 109 ms                                                          | 108 ms: 1.01x faster                                                          |
| pickle_list          | 3.40 us                                                         | 3.50 us: 1.03x slower                                                         |
| xml_etree_iterparse  | 65.1 ms                                                         | 67.8 ms: 1.04x slower                                                         |
| xml_etree_generate   | 62.6 ms                                                         | 66.8 ms: 1.07x slower                                                         |
| pickle_pure_python   | 238 us                                                          | 256 us: 1.07x slower                                                          |
| xml_etree_process    | 45.0 ms                                                         | 48.6 ms: 1.08x slower                                                         |
| tomli_loads          | 1.73 sec                                                        | 1.90 sec: 1.10x slower                                                        |
| unpickle_pure_python | 162 us                                                          | 178 us: 1.10x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.02x slower                                                                  |

Benchmark hidden because not significant (2): unpickle_list, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1_win32-x86-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 24.3 ms                                                         | 23.5 ms: 1.03x faster                                                         |
| python_startup_no_site | 19.9 ms                                                         | 19.4 ms: 1.03x faster                                                         |
| Geometric mean         | (ref)                                                           | 1.03x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1_win32-x86-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_xml     | 49.5 ms                                                         | 46.9 ms: 1.06x faster                                                         |
| genshi_text    | 22.4 ms                                                         | 21.8 ms: 1.03x faster                                                         |
| mako           | 7.31 ms                                                         | 7.98 ms: 1.09x slower                                                         |
| Geometric mean | (ref)                                                           | 1.00x slower                                                                  |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1_win32-x86-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| thrift                     | 10.1 ms                                                         | 753 us: 13.47x faster                                                         |
| coverage                   | 333 ms                                                          | 51.9 ms: 6.42x faster                                                         |
| asyncio_tcp                | 842 ms                                                          | 648 ms: 1.30x faster                                                          |
| deepcopy                   | 307 us                                                          | 244 us: 1.26x faster                                                          |
| deepcopy_memo              | 26.2 us                                                         | 22.2 us: 1.18x faster                                                         |
| async_tree_memoization_tg  | 287 ms                                                          | 251 ms: 1.14x faster                                                          |
| async_tree_none            | 246 ms                                                          | 218 ms: 1.13x faster                                                          |
| deepcopy_reduce            | 2.85 us                                                         | 2.54 us: 1.12x faster                                                         |
| async_tree_memoization     | 302 ms                                                          | 271 ms: 1.11x faster                                                          |
| async_tree_none_tg         | 219 ms                                                          | 200 ms: 1.09x faster                                                          |
| tornado_http               | 104 ms                                                          | 95.8 ms: 1.09x faster                                                         |
| pathlib                    | 89.4 ms                                                         | 82.5 ms: 1.08x faster                                                         |
| go                         | 111 ms                                                          | 103 ms: 1.08x faster                                                          |
| pickle_dict                | 21.7 us                                                         | 20.5 us: 1.06x faster                                                         |
| bench_mp_pool              | 74.3 ms                                                         | 70.1 ms: 1.06x faster                                                         |
| pickle                     | 8.42 us                                                         | 7.96 us: 1.06x faster                                                         |
| genshi_xml                 | 49.5 ms                                                         | 46.9 ms: 1.06x faster                                                         |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 469 ms: 1.05x faster                                                          |
| telco                      | 6.67 ms                                                         | 6.34 ms: 1.05x faster                                                         |
| html5lib                   | 48.3 ms                                                         | 46.5 ms: 1.04x faster                                                         |
| python_startup             | 24.3 ms                                                         | 23.5 ms: 1.03x faster                                                         |
| python_startup_no_site     | 19.9 ms                                                         | 19.4 ms: 1.03x faster                                                         |
| gc_traversal               | 1.45 ms                                                         | 1.41 ms: 1.03x faster                                                         |
| genshi_text                | 22.4 ms                                                         | 21.8 ms: 1.03x faster                                                         |
| crypto_pyaes               | 58.2 ms                                                         | 57.0 ms: 1.02x faster                                                         |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.1 sec: 1.02x faster                                                        |
| nqueens                    | 75.1 ms                                                         | 73.8 ms: 1.02x faster                                                         |
| unpickle                   | 10.5 us                                                         | 10.4 us: 1.01x faster                                                         |
| sympy_sum                  | 108 ms                                                          | 107 ms: 1.01x faster                                                          |
| 2to3                       | 253 ms                                                          | 250 ms: 1.01x faster                                                          |
| sympy_str                  | 215 ms                                                          | 213 ms: 1.01x faster                                                          |
| json_loads                 | 21.0 us                                                         | 20.8 us: 1.01x faster                                                         |
| xml_etree_parse            | 109 ms                                                          | 108 ms: 1.01x faster                                                          |
| pidigits                   | 202 ms                                                          | 201 ms: 1.01x faster                                                          |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 461 ms: 1.01x faster                                                          |
| sqlglot_normalize          | 220 ms                                                          | 221 ms: 1.00x slower                                                          |
| sqlglot_transpile          | 1.29 ms                                                         | 1.30 ms: 1.00x slower                                                         |
| sympy_expand               | 375 ms                                                          | 377 ms: 1.01x slower                                                          |
| logging_format             | 8.57 us                                                         | 8.66 us: 1.01x slower                                                         |
| async_tree_io_tg           | 509 ms                                                          | 516 ms: 1.01x slower                                                          |
| logging_simple             | 7.87 us                                                         | 7.99 us: 1.01x slower                                                         |
| dulwich_log                | 49.7 ms                                                         | 50.6 ms: 1.02x slower                                                         |
| docutils                   | 1.82 sec                                                        | 1.86 sec: 1.02x slower                                                        |
| pprint_safe_repr           | 644 ms                                                          | 662 ms: 1.03x slower                                                          |
| create_gc_cycles           | 713 us                                                          | 734 us: 1.03x slower                                                          |
| pickle_list                | 3.40 us                                                         | 3.50 us: 1.03x slower                                                         |
| regex_compile              | 103 ms                                                          | 107 ms: 1.04x slower                                                          |
| meteor_contest             | 77.0 ms                                                         | 79.8 ms: 1.04x slower                                                         |
| xml_etree_iterparse        | 65.1 ms                                                         | 67.8 ms: 1.04x slower                                                         |
| regex_v8                   | 15.6 ms                                                         | 16.3 ms: 1.04x slower                                                         |
| typing_runtime_protocols   | 136 us                                                          | 142 us: 1.04x slower                                                          |
| regex_effbot               | 1.81 ms                                                         | 1.89 ms: 1.04x slower                                                         |
| mdp                        | 1.67 sec                                                        | 1.75 sec: 1.05x slower                                                        |
| pprint_pformat             | 1.30 sec                                                        | 1.36 sec: 1.05x slower                                                        |
| chaos                      | 51.2 ms                                                         | 53.9 ms: 1.05x slower                                                         |
| float                      | 57.8 ms                                                         | 61.4 ms: 1.06x slower                                                         |
| comprehensions             | 12.7 us                                                         | 13.6 us: 1.07x slower                                                         |
| xml_etree_generate         | 62.6 ms                                                         | 66.8 ms: 1.07x slower                                                         |
| pickle_pure_python         | 238 us                                                          | 256 us: 1.07x slower                                                          |
| scimark_sparse_mat_mult    | 2.90 ms                                                         | 3.13 ms: 1.08x slower                                                         |
| xml_etree_process          | 45.0 ms                                                         | 48.6 ms: 1.08x slower                                                         |
| async_generators           | 274 ms                                                          | 297 ms: 1.09x slower                                                          |
| unpack_sequence            | 42.9 ns                                                         | 46.7 ns: 1.09x slower                                                         |
| spectral_norm              | 71.3 ms                                                         | 77.7 ms: 1.09x slower                                                         |
| mako                       | 7.31 ms                                                         | 7.98 ms: 1.09x slower                                                         |
| pyflate                    | 326 ms                                                          | 356 ms: 1.09x slower                                                          |
| scimark_sor                | 91.8 ms                                                         | 101 ms: 1.10x slower                                                          |
| tomli_loads                | 1.73 sec                                                        | 1.90 sec: 1.10x slower                                                        |
| fannkuch                   | 293 ms                                                          | 322 ms: 1.10x slower                                                          |
| hexiom                     | 4.64 ms                                                         | 5.10 ms: 1.10x slower                                                         |
| unpickle_pure_python       | 162 us                                                          | 178 us: 1.10x slower                                                          |
| scimark_lu                 | 63.5 ms                                                         | 70.5 ms: 1.11x slower                                                         |
| nbody                      | 81.9 ms                                                         | 91.6 ms: 1.12x slower                                                         |
| deltablue                  | 2.41 ms                                                         | 2.70 ms: 1.12x slower                                                         |
| raytrace                   | 205 ms                                                          | 234 ms: 1.14x slower                                                          |
| scimark_monte_carlo        | 50.3 ms                                                         | 57.6 ms: 1.14x slower                                                         |
| richards                   | 33.8 ms                                                         | 38.8 ms: 1.15x slower                                                         |
| richards_super             | 38.0 ms                                                         | 44.3 ms: 1.17x slower                                                         |
| coroutines                 | 15.7 ms                                                         | 18.5 ms: 1.18x slower                                                         |
| scimark_fft                | 206 ms                                                          | 246 ms: 1.19x slower                                                          |
| generators                 | 22.1 ms                                                         | 26.6 ms: 1.20x slower                                                         |
| logging_silent             | 61.6 ns                                                         | 74.8 ns: 1.21x slower                                                         |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                                  |

Benchmark hidden because not significant (13): json, async_tree_io, django_template, pycparser, unpickle_list, regex_dna, sympy_integrate, json_dumps, sqlglot_optimize, sqlite_synth, sqlglot_parse, bench_thread_pool, pylint
Ignored benchmarks (2) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, flaskblogging

# HPT report

- Reliability score: 94.84% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown