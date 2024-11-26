# Results vs. base

- fork: mdboom
- ref: unicode_check_exact
- machine: windows-x86
- commit hash: 76aa43c
- commit date: 2024-09-11
- overall geometric mean: 1.006x faster
- HPT reliability: 94.14%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-pythonperf1_win32-x86-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 249 ms                                                                         | 250 ms: 1.01x slower                                                          |
| docutils       | 1.86 sec                                                                       | 1.86 sec: 1.00x faster                                                        |
| html5lib       | 44.1 ms                                                                        | 46.5 ms: 1.05x slower                                                         |
| tornado_http   | 94.8 ms                                                                        | 95.8 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                                          | 1.02x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-pythonperf1_win32-x86-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------------|:------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_generators           | 305 ms                                                                         | 297 ms: 1.03x faster                                                          |
| coroutines                 | 18.7 ms                                                                        | 18.5 ms: 1.01x faster                                                         |
| async_tree_cpu_io_mixed_tg | 457 ms                                                                         | 461 ms: 1.01x slower                                                          |
| async_tree_cpu_io_mixed    | 464 ms                                                                         | 469 ms: 1.01x slower                                                          |
| Geometric mean             | (ref)                                                                          | 1.00x faster                                                                  |

Benchmark hidden because not significant (8): asyncio_tcp, async_tree_none, async_tree_memoization, asyncio_tcp_ssl, async_tree_memoization_tg, async_tree_io, async_tree_io_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-pythonperf1_win32-x86-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 62.2 ms                                                                        | 61.4 ms: 1.01x faster                                                         |
| pidigits       | 196 ms                                                                         | 201 ms: 1.02x slower                                                          |
| Geometric mean | (ref)                                                                          | 1.00x slower                                                                  |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-pythonperf1_win32-x86-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                                         | 116 ms: 1.03x faster                                                          |
| regex_effbot   | 1.92 ms                                                                        | 1.89 ms: 1.02x faster                                                         |
| regex_compile  | 108 ms                                                                         | 107 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                                          | 1.01x faster                                                                  |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-pythonperf1_win32-x86-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------|:------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pickle_list          | 3.65 us                                                                        | 3.50 us: 1.04x faster                                                         |
| json_dumps           | 7.62 ms                                                                        | 7.41 ms: 1.03x faster                                                         |
| pickle_dict          | 21.0 us                                                                        | 20.5 us: 1.03x faster                                                         |
| xml_etree_process    | 49.8 ms                                                                        | 48.6 ms: 1.02x faster                                                         |
| pickle_pure_python   | 262 us                                                                         | 256 us: 1.02x faster                                                          |
| xml_etree_generate   | 68.2 ms                                                                        | 66.8 ms: 1.02x faster                                                         |
| unpickle_pure_python | 181 us                                                                         | 178 us: 1.02x faster                                                          |
| unpickle_list        | 3.10 us                                                                        | 3.08 us: 1.01x faster                                                         |
| pickle               | 7.99 us                                                                        | 7.96 us: 1.00x faster                                                         |
| tomli_loads          | 1.89 sec                                                                       | 1.90 sec: 1.01x slower                                                        |
| unpickle             | 10.3 us                                                                        | 10.4 us: 1.01x slower                                                         |
| json_loads           | 20.6 us                                                                        | 20.8 us: 1.01x slower                                                         |
| xml_etree_iterparse  | 66.9 ms                                                                        | 67.8 ms: 1.01x slower                                                         |
| Geometric mean       | (ref)                                                                          | 1.01x faster                                                                  |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-pythonperf1_win32-x86-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|------------------------|:------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 19.8 ms                                                                        | 19.4 ms: 1.02x faster                                                         |
| python_startup         | 24.0 ms                                                                        | 23.5 ms: 1.02x faster                                                         |
| Geometric mean         | (ref)                                                                          | 1.02x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-pythonperf1_win32-x86-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako           | 8.18 ms                                                                        | 7.98 ms: 1.03x faster                                                         |
| genshi_text    | 22.2 ms                                                                        | 21.8 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                                          | 1.01x faster                                                                  |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-pythonperf1_win32-x86-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------------|:------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| unpack_sequence            | 49.3 ns                                                                        | 46.7 ns: 1.06x faster                                                         |
| coverage                   | 54.7 ms                                                                        | 51.9 ms: 1.06x faster                                                         |
| fannkuch                   | 338 ms                                                                         | 322 ms: 1.05x faster                                                          |
| pickle_list                | 3.65 us                                                                        | 3.50 us: 1.04x faster                                                         |
| sqlglot_transpile          | 1.35 ms                                                                        | 1.30 ms: 1.04x faster                                                         |
| scimark_sor                | 104 ms                                                                         | 101 ms: 1.03x faster                                                          |
| sqlglot_parse              | 1.08 ms                                                                        | 1.05 ms: 1.03x faster                                                         |
| comprehensions             | 14.0 us                                                                        | 13.6 us: 1.03x faster                                                         |
| sympy_expand               | 388 ms                                                                         | 377 ms: 1.03x faster                                                          |
| json_dumps                 | 7.62 ms                                                                        | 7.41 ms: 1.03x faster                                                         |
| async_generators           | 305 ms                                                                         | 297 ms: 1.03x faster                                                          |
| pickle_dict                | 21.0 us                                                                        | 20.5 us: 1.03x faster                                                         |
| mako                       | 8.18 ms                                                                        | 7.98 ms: 1.03x faster                                                         |
| meteor_contest             | 81.9 ms                                                                        | 79.8 ms: 1.03x faster                                                         |
| richards                   | 39.8 ms                                                                        | 38.8 ms: 1.03x faster                                                         |
| regex_dna                  | 119 ms                                                                         | 116 ms: 1.03x faster                                                          |
| xml_etree_process          | 49.8 ms                                                                        | 48.6 ms: 1.02x faster                                                         |
| python_startup_no_site     | 19.8 ms                                                                        | 19.4 ms: 1.02x faster                                                         |
| pickle_pure_python         | 262 us                                                                         | 256 us: 1.02x faster                                                          |
| sqlglot_normalize          | 226 ms                                                                         | 221 ms: 1.02x faster                                                          |
| json                       | 4.25 ms                                                                        | 4.16 ms: 1.02x faster                                                         |
| python_startup             | 24.0 ms                                                                        | 23.5 ms: 1.02x faster                                                         |
| sympy_str                  | 218 ms                                                                         | 213 ms: 1.02x faster                                                          |
| xml_etree_generate         | 68.2 ms                                                                        | 66.8 ms: 1.02x faster                                                         |
| unpickle_pure_python       | 181 us                                                                         | 178 us: 1.02x faster                                                          |
| crypto_pyaes               | 58.1 ms                                                                        | 57.0 ms: 1.02x faster                                                         |
| sympy_integrate            | 15.4 ms                                                                        | 15.1 ms: 1.02x faster                                                         |
| richards_super             | 45.0 ms                                                                        | 44.3 ms: 1.02x faster                                                         |
| genshi_text                | 22.2 ms                                                                        | 21.8 ms: 1.02x faster                                                         |
| sqlglot_optimize           | 43.2 ms                                                                        | 42.5 ms: 1.02x faster                                                         |
| typing_runtime_protocols   | 145 us                                                                         | 142 us: 1.02x faster                                                          |
| regex_effbot               | 1.92 ms                                                                        | 1.89 ms: 1.02x faster                                                         |
| nqueens                    | 74.9 ms                                                                        | 73.8 ms: 1.01x faster                                                         |
| go                         | 104 ms                                                                         | 103 ms: 1.01x faster                                                          |
| coroutines                 | 18.7 ms                                                                        | 18.5 ms: 1.01x faster                                                         |
| logging_format             | 8.77 us                                                                        | 8.66 us: 1.01x faster                                                         |
| float                      | 62.2 ms                                                                        | 61.4 ms: 1.01x faster                                                         |
| hexiom                     | 5.15 ms                                                                        | 5.10 ms: 1.01x faster                                                         |
| sympy_sum                  | 108 ms                                                                         | 107 ms: 1.01x faster                                                          |
| regex_compile              | 108 ms                                                                         | 107 ms: 1.01x faster                                                          |
| deepcopy                   | 246 us                                                                         | 244 us: 1.01x faster                                                          |
| deltablue                  | 2.72 ms                                                                        | 2.70 ms: 1.01x faster                                                         |
| unpickle_list              | 3.10 us                                                                        | 3.08 us: 1.01x faster                                                         |
| raytrace                   | 235 ms                                                                         | 234 ms: 1.01x faster                                                          |
| logging_simple             | 8.04 us                                                                        | 7.99 us: 1.01x faster                                                         |
| deepcopy_memo              | 22.3 us                                                                        | 22.2 us: 1.01x faster                                                         |
| telco                      | 6.37 ms                                                                        | 6.34 ms: 1.00x faster                                                         |
| pickle                     | 7.99 us                                                                        | 7.96 us: 1.00x faster                                                         |
| docutils                   | 1.86 sec                                                                       | 1.86 sec: 1.00x faster                                                        |
| chaos                      | 53.7 ms                                                                        | 53.9 ms: 1.00x slower                                                         |
| 2to3                       | 249 ms                                                                         | 250 ms: 1.01x slower                                                          |
| pprint_pformat             | 1.35 sec                                                                       | 1.36 sec: 1.01x slower                                                        |
| tomli_loads                | 1.89 sec                                                                       | 1.90 sec: 1.01x slower                                                        |
| pathlib                    | 81.8 ms                                                                        | 82.5 ms: 1.01x slower                                                         |
| async_tree_cpu_io_mixed_tg | 457 ms                                                                         | 461 ms: 1.01x slower                                                          |
| tornado_http               | 94.8 ms                                                                        | 95.8 ms: 1.01x slower                                                         |
| async_tree_cpu_io_mixed    | 464 ms                                                                         | 469 ms: 1.01x slower                                                          |
| unpickle                   | 10.3 us                                                                        | 10.4 us: 1.01x slower                                                         |
| gc_traversal               | 1.39 ms                                                                        | 1.41 ms: 1.01x slower                                                         |
| json_loads                 | 20.6 us                                                                        | 20.8 us: 1.01x slower                                                         |
| xml_etree_iterparse        | 66.9 ms                                                                        | 67.8 ms: 1.01x slower                                                         |
| generators                 | 26.2 ms                                                                        | 26.6 ms: 1.02x slower                                                         |
| scimark_sparse_mat_mult    | 3.08 ms                                                                        | 3.13 ms: 1.02x slower                                                         |
| spectral_norm              | 76.1 ms                                                                        | 77.7 ms: 1.02x slower                                                         |
| thrift                     | 737 us                                                                         | 753 us: 1.02x slower                                                          |
| pidigits                   | 196 ms                                                                         | 201 ms: 1.02x slower                                                          |
| mdp                        | 1.70 sec                                                                       | 1.75 sec: 1.03x slower                                                        |
| scimark_lu                 | 68.1 ms                                                                        | 70.5 ms: 1.03x slower                                                         |
| scimark_fft                | 236 ms                                                                         | 246 ms: 1.04x slower                                                          |
| html5lib                   | 44.1 ms                                                                        | 46.5 ms: 1.05x slower                                                         |
| Geometric mean             | (ref)                                                                          | 1.01x faster                                                                  |

Benchmark hidden because not significant (25): asyncio_tcp, pyflate, xml_etree_parse, dulwich_log, logging_silent, nbody, django_template, async_tree_none, sqlite_synth, genshi_xml, pylint, async_tree_memoization, regex_v8, deepcopy_reduce, pycparser, scimark_monte_carlo, bench_thread_pool, asyncio_tcp_ssl, create_gc_cycles, bench_mp_pool, pprint_safe_repr, async_tree_memoization_tg, async_tree_io, async_tree_io_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.006x faster
# HPT report

- Reliability score: 94.14% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown