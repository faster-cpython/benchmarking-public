# Results vs. base

- fork: brandtbucher
- ref: no_cold_exits
- machine: windows-x86
- commit hash: f837cc6
- commit date: 2024-06-10
- overall geometric mean: 1.01x faster
- HPT reliability: 96.96%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240610-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 242 ms                                                                         | 244 ms: 1.01x slower                                                          |
| docutils       | 1.85 sec                                                                       | 1.87 sec: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                          | 1.01x slower                                                                  |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240610-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------------------|:------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 504 ms                                                                         | 479 ms: 1.05x faster                                                          |
| async_tree_cpu_io_mixed_tg | 484 ms                                                                         | 464 ms: 1.04x faster                                                          |
| async_tree_io_tg           | 537 ms                                                                         | 533 ms: 1.01x faster                                                          |
| Geometric mean             | (ref)                                                                          | 1.02x faster                                                                  |

Benchmark hidden because not significant (5): async_tree_io, async_tree_memoization, async_tree_none, async_tree_none_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240610-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pidigits       | 198 ms                                                                         | 195 ms: 1.02x faster                                                          |
| float          | 41.4 ms                                                                        | 41.6 ms: 1.00x slower                                                         |
| Geometric mean | (ref)                                                                          | 1.01x faster                                                                  |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240610-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 96.7 ms                                                                        | 96.3 ms: 1.00x faster                                                         |
| regex_effbot   | 1.98 ms                                                                        | 1.99 ms: 1.01x slower                                                         |
| regex_dna      | 123 ms                                                                         | 124 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                                          | 1.00x slower                                                                  |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240605-pythonperf1_win32-x86-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240610-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|--------------------|:------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| unpickle_list      | 2.90 us                                                                        | 2.76 us: 1.05x faster                                                         |
| pickle_list        | 3.72 us                                                                        | 3.58 us: 1.04x faster                                                         |
| xml_etree_parse    | 102 ms                                                                         | 99.5 ms: 1.03x faster                                                         |
| unpickle           | 10.5 us                                                                        | 10.3 us: 1.02x faster                                                         |
| tomli_loads        | 1.43 sec                                                                       | 1.39 sec: 1.02x faster                                                        |
| xml_etree_generate | 55.2 ms                                                                        | 54.5 ms: 1.01x faster                                                         |
| xml_etree_process  | 40.4 ms                                                                        | 40.2 ms: 1.00x faster                                                         |
| pickle_dict        | 20.7 us                                                                        | 20.9 us: 1.01x slower                                                         |
| pickle_pure_python | 199 us                                                                         | 201 us: 1.01x slower                                                          |
| json_dumps         | 6.51 ms                                                                        | 6.66 ms: 1.02x slower                                                         |
| Geometric mean     | (ref)                                                                          | 1.01x faster                                                                  |

Benchmark hidden because not significant (4): unpickle_pure_python, xml_etree_iterparse, json_loads, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240610-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|------------------------|:------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 20.2 ms                                                                        | 18.5 ms: 1.09x faster                                                         |
| python_startup         | 24.2 ms                                                                        | 22.9 ms: 1.06x faster                                                         |
| Geometric mean         | (ref)                                                                          | 1.07x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240610-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_xml     | 51.6 ms                                                                        | 50.7 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                                          | 1.00x faster                                                                  |

Benchmark hidden because not significant (3): mako, django_template, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240610-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------------------|:------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site     | 20.2 ms                                                                        | 18.5 ms: 1.09x faster                                                         |
| telco                      | 5.64 ms                                                                        | 5.23 ms: 1.08x faster                                                         |
| richards                   | 31.3 ms                                                                        | 29.2 ms: 1.07x faster                                                         |
| python_startup             | 24.2 ms                                                                        | 22.9 ms: 1.06x faster                                                         |
| richards_super             | 35.1 ms                                                                        | 33.3 ms: 1.05x faster                                                         |
| async_tree_cpu_io_mixed    | 504 ms                                                                         | 479 ms: 1.05x faster                                                          |
| unpickle_list              | 2.90 us                                                                        | 2.76 us: 1.05x faster                                                         |
| async_tree_cpu_io_mixed_tg | 484 ms                                                                         | 464 ms: 1.04x faster                                                          |
| coverage                   | 50.6 ms                                                                        | 48.6 ms: 1.04x faster                                                         |
| nqueens                    | 70.2 ms                                                                        | 67.4 ms: 1.04x faster                                                         |
| pickle_list                | 3.72 us                                                                        | 3.58 us: 1.04x faster                                                         |
| fannkuch                   | 219 ms                                                                         | 211 ms: 1.04x faster                                                          |
| deepcopy_memo              | 20.7 us                                                                        | 20.0 us: 1.03x faster                                                         |
| scimark_sor                | 90.4 ms                                                                        | 87.6 ms: 1.03x faster                                                         |
| xml_etree_parse            | 102 ms                                                                         | 99.5 ms: 1.03x faster                                                         |
| unpickle                   | 10.5 us                                                                        | 10.3 us: 1.02x faster                                                         |
| mdp                        | 1.63 sec                                                                       | 1.59 sec: 1.02x faster                                                        |
| tomli_loads                | 1.43 sec                                                                       | 1.39 sec: 1.02x faster                                                        |
| genshi_xml                 | 51.6 ms                                                                        | 50.7 ms: 1.02x faster                                                         |
| hexiom                     | 4.53 ms                                                                        | 4.45 ms: 1.02x faster                                                         |
| pidigits                   | 198 ms                                                                         | 195 ms: 1.02x faster                                                          |
| async_generators           | 305 ms                                                                         | 301 ms: 1.02x faster                                                          |
| bench_mp_pool              | 74.1 ms                                                                        | 73.0 ms: 1.01x faster                                                         |
| xml_etree_generate         | 55.2 ms                                                                        | 54.5 ms: 1.01x faster                                                         |
| logging_format             | 7.92 us                                                                        | 7.82 us: 1.01x faster                                                         |
| deltablue                  | 2.54 ms                                                                        | 2.51 ms: 1.01x faster                                                         |
| coroutines                 | 15.7 ms                                                                        | 15.6 ms: 1.01x faster                                                         |
| logging_simple             | 7.27 us                                                                        | 7.21 us: 1.01x faster                                                         |
| scimark_fft                | 164 ms                                                                         | 163 ms: 1.01x faster                                                          |
| async_tree_io_tg           | 537 ms                                                                         | 533 ms: 1.01x faster                                                          |
| xml_etree_process          | 40.4 ms                                                                        | 40.2 ms: 1.00x faster                                                         |
| regex_compile              | 96.7 ms                                                                        | 96.3 ms: 1.00x faster                                                         |
| pyflate                    | 271 ms                                                                         | 270 ms: 1.00x faster                                                          |
| sqlglot_normalize          | 218 ms                                                                         | 219 ms: 1.00x slower                                                          |
| float                      | 41.4 ms                                                                        | 41.6 ms: 1.00x slower                                                         |
| spectral_norm              | 47.6 ms                                                                        | 47.9 ms: 1.01x slower                                                         |
| regex_effbot               | 1.98 ms                                                                        | 1.99 ms: 1.01x slower                                                         |
| pickle_dict                | 20.7 us                                                                        | 20.9 us: 1.01x slower                                                         |
| pprint_safe_repr           | 546 ms                                                                         | 550 ms: 1.01x slower                                                          |
| sqlglot_optimize           | 41.3 ms                                                                        | 41.7 ms: 1.01x slower                                                         |
| 2to3                       | 242 ms                                                                         | 244 ms: 1.01x slower                                                          |
| docutils                   | 1.85 sec                                                                       | 1.87 sec: 1.01x slower                                                        |
| pickle_pure_python         | 199 us                                                                         | 201 us: 1.01x slower                                                          |
| sympy_expand               | 370 ms                                                                         | 374 ms: 1.01x slower                                                          |
| go                         | 109 ms                                                                         | 111 ms: 1.01x slower                                                          |
| sqlite_synth               | 1.90 us                                                                        | 1.92 us: 1.01x slower                                                         |
| regex_dna                  | 123 ms                                                                         | 124 ms: 1.01x slower                                                          |
| crypto_pyaes               | 47.9 ms                                                                        | 48.5 ms: 1.01x slower                                                         |
| sympy_sum                  | 106 ms                                                                         | 108 ms: 1.01x slower                                                          |
| sympy_str                  | 208 ms                                                                         | 211 ms: 1.01x slower                                                          |
| gc_traversal               | 1.44 ms                                                                        | 1.46 ms: 1.02x slower                                                         |
| logging_silent             | 53.9 ns                                                                        | 54.8 ns: 1.02x slower                                                         |
| thrift                     | 699 us                                                                         | 712 us: 1.02x slower                                                          |
| generators                 | 23.0 ms                                                                        | 23.5 ms: 1.02x slower                                                         |
| chaos                      | 50.1 ms                                                                        | 51.3 ms: 1.02x slower                                                         |
| json_dumps                 | 6.51 ms                                                                        | 6.66 ms: 1.02x slower                                                         |
| comprehensions             | 11.0 us                                                                        | 11.3 us: 1.03x slower                                                         |
| raytrace                   | 205 ms                                                                         | 213 ms: 1.04x slower                                                          |
| asyncio_tcp                | 600 ms                                                                         | 626 ms: 1.04x slower                                                          |
| typing_runtime_protocols   | 135 us                                                                         | 146 us: 1.07x slower                                                          |
| Geometric mean             | (ref)                                                                          | 1.01x faster                                                                  |

Benchmark hidden because not significant (33): async_tree_io, bench_thread_pool, async_tree_memoization, async_tree_none, nbody, pycparser, create_gc_cycles, async_tree_none_tg, unpickle_pure_python, xml_etree_iterparse, mako, pprint_pformat, sqlglot_parse, json_loads, html5lib, scimark_sparse_mat_mult, asyncio_tcp_ssl, sqlglot_transpile, deepcopy, deepcopy_reduce, scimark_lu, async_tree_memoization_tg, meteor_contest, django_template, pickle, sympy_integrate, genshi_text, regex_v8, scimark_monte_carlo, pathlib, pylint, tornado_http, json

# HPT report

- Reliability score: 96.96% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown