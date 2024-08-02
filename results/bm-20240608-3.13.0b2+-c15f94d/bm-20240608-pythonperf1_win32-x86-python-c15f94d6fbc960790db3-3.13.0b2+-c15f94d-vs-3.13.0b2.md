# Results vs. 3.13.0b2

- fork: python
- ref: c15f94d6fbc960790db3
- machine: windows-x86
- commit hash: c15f94d
- commit date: 2024-06-08
- overall geometric mean: 1.00x slower
- HPT reliability: 50.59%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 235 ms: 1.01x slower                                                            |
| chameleon      | 5.71 ms                                                             | 5.74 ms: 1.01x slower                                                           |
| html5lib       | 45.4 ms                                                             | 45.9 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                               | 1.00x slower                                                                    |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_io_tg, async_tree_memoization, async_tree_io, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_none_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 74.7 ms: 1.03x faster                                                           |
| pidigits       | 199 ms                                                              | 197 ms: 1.01x faster                                                            |
| float          | 52.4 ms                                                             | 52.7 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                               | 1.01x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 99.9 ms                                                             | 98.6 ms: 1.01x faster                                                           |
| regex_dna      | 118 ms                                                              | 118 ms: 1.00x slower                                                            |
| regex_effbot   | 1.88 ms                                                             | 1.92 ms: 1.02x slower                                                           |
| regex_v8       | 15.7 ms                                                             | 16.0 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                               | 1.01x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.65 sec                                                            | 1.61 sec: 1.02x faster                                                          |
| unpickle_list        | 2.93 us                                                             | 2.87 us: 1.02x faster                                                           |
| pickle_dict          | 20.8 us                                                             | 20.5 us: 1.01x faster                                                           |
| xml_etree_parse      | 104 ms                                                              | 103 ms: 1.01x faster                                                            |
| unpickle_pure_python | 147 us                                                              | 146 us: 1.01x faster                                                            |
| xml_etree_iterparse  | 64.2 ms                                                             | 63.6 ms: 1.01x faster                                                           |
| pickle_pure_python   | 213 us                                                              | 215 us: 1.01x slower                                                            |
| json_dumps           | 6.84 ms                                                             | 6.94 ms: 1.01x slower                                                           |
| json_loads           | 20.5 us                                                             | 20.9 us: 1.02x slower                                                           |
| pickle_list          | 3.57 us                                                             | 3.71 us: 1.04x slower                                                           |
| Geometric mean       | (ref)                                                               | 1.00x slower                                                                    |

Benchmark hidden because not significant (4): xml_etree_generate, pickle, unpickle, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup | 22.2 ms                                                             | 22.6 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                               | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text    | 20.1 ms                                                             | 19.5 ms: 1.03x faster                                                           |
| mako           | 6.94 ms                                                             | 6.86 ms: 1.01x faster                                                           |
| genshi_xml     | 44.3 ms                                                             | 44.5 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                               | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nqueens                 | 68.7 ms                                                             | 65.9 ms: 1.04x faster                                                           |
| sympy_expand            | 375 ms                                                              | 362 ms: 1.04x faster                                                            |
| sqlglot_parse           | 964 us                                                              | 932 us: 1.03x faster                                                            |
| genshi_text             | 20.1 ms                                                             | 19.5 ms: 1.03x faster                                                           |
| scimark_sparse_mat_mult | 2.87 ms                                                             | 2.79 ms: 1.03x faster                                                           |
| nbody                   | 76.9 ms                                                             | 74.7 ms: 1.03x faster                                                           |
| richards                | 31.2 ms                                                             | 30.4 ms: 1.03x faster                                                           |
| richards_super          | 35.5 ms                                                             | 34.6 ms: 1.03x faster                                                           |
| sqlglot_transpile       | 1.19 ms                                                             | 1.16 ms: 1.02x faster                                                           |
| meteor_contest          | 74.1 ms                                                             | 72.5 ms: 1.02x faster                                                           |
| tomli_loads             | 1.65 sec                                                            | 1.61 sec: 1.02x faster                                                          |
| unpickle_list           | 2.93 us                                                             | 2.87 us: 1.02x faster                                                           |
| bench_thread_pool       | 985 us                                                              | 966 us: 1.02x faster                                                            |
| sympy_str               | 211 ms                                                              | 207 ms: 1.02x faster                                                            |
| sqlglot_normalize       | 206 ms                                                              | 202 ms: 1.02x faster                                                            |
| comprehensions          | 11.9 us                                                             | 11.7 us: 1.02x faster                                                           |
| pickle_dict             | 20.8 us                                                             | 20.5 us: 1.01x faster                                                           |
| sqlglot_optimize        | 39.7 ms                                                             | 39.2 ms: 1.01x faster                                                           |
| regex_compile           | 99.9 ms                                                             | 98.6 ms: 1.01x faster                                                           |
| xml_etree_parse         | 104 ms                                                              | 103 ms: 1.01x faster                                                            |
| mako                    | 6.94 ms                                                             | 6.86 ms: 1.01x faster                                                           |
| create_gc_cycles        | 756 us                                                              | 747 us: 1.01x faster                                                            |
| unpickle_pure_python    | 147 us                                                              | 146 us: 1.01x faster                                                            |
| crypto_pyaes            | 55.8 ms                                                             | 55.3 ms: 1.01x faster                                                           |
| xml_etree_iterparse     | 64.2 ms                                                             | 63.6 ms: 1.01x faster                                                           |
| coverage                | 307 ms                                                              | 305 ms: 1.01x faster                                                            |
| chaos                   | 48.0 ms                                                             | 47.6 ms: 1.01x faster                                                           |
| pidigits                | 199 ms                                                              | 197 ms: 1.01x faster                                                            |
| sqlite_synth            | 1.96 us                                                             | 1.95 us: 1.01x faster                                                           |
| pyflate                 | 308 ms                                                              | 307 ms: 1.00x faster                                                            |
| regex_dna               | 118 ms                                                              | 118 ms: 1.00x slower                                                            |
| chameleon               | 5.71 ms                                                             | 5.74 ms: 1.01x slower                                                           |
| logging_silent          | 57.9 ns                                                             | 58.2 ns: 1.01x slower                                                           |
| genshi_xml              | 44.3 ms                                                             | 44.5 ms: 1.01x slower                                                           |
| float                   | 52.4 ms                                                             | 52.7 ms: 1.01x slower                                                           |
| bench_mp_pool           | 69.4 ms                                                             | 69.9 ms: 1.01x slower                                                           |
| telco                   | 6.03 ms                                                             | 6.07 ms: 1.01x slower                                                           |
| scimark_sor             | 81.0 ms                                                             | 81.6 ms: 1.01x slower                                                           |
| go                      | 101 ms                                                              | 102 ms: 1.01x slower                                                            |
| hexiom                  | 4.23 ms                                                             | 4.27 ms: 1.01x slower                                                           |
| 2to3                    | 233 ms                                                              | 235 ms: 1.01x slower                                                            |
| logging_simple          | 7.47 us                                                             | 7.54 us: 1.01x slower                                                           |
| html5lib                | 45.4 ms                                                             | 45.9 ms: 1.01x slower                                                           |
| pickle_pure_python      | 213 us                                                              | 215 us: 1.01x slower                                                            |
| deepcopy                | 280 us                                                              | 283 us: 1.01x slower                                                            |
| generators              | 21.2 ms                                                             | 21.4 ms: 1.01x slower                                                           |
| json_dumps              | 6.84 ms                                                             | 6.94 ms: 1.01x slower                                                           |
| python_startup          | 22.2 ms                                                             | 22.6 ms: 1.01x slower                                                           |
| scimark_lu              | 59.4 ms                                                             | 60.3 ms: 1.02x slower                                                           |
| async_generators        | 266 ms                                                              | 270 ms: 1.02x slower                                                            |
| pprint_safe_repr        | 607 ms                                                              | 617 ms: 1.02x slower                                                            |
| json_loads              | 20.5 us                                                             | 20.9 us: 1.02x slower                                                           |
| deepcopy_memo           | 23.5 us                                                             | 23.9 us: 1.02x slower                                                           |
| regex_effbot            | 1.88 ms                                                             | 1.92 ms: 1.02x slower                                                           |
| regex_v8                | 15.7 ms                                                             | 16.0 ms: 1.02x slower                                                           |
| pprint_pformat          | 1.24 sec                                                            | 1.27 sec: 1.02x slower                                                          |
| fannkuch                | 270 ms                                                              | 277 ms: 1.02x slower                                                            |
| scimark_monte_carlo     | 45.2 ms                                                             | 46.4 ms: 1.03x slower                                                           |
| json                    | 4.10 ms                                                             | 4.22 ms: 1.03x slower                                                           |
| pycparser               | 777 ms                                                              | 802 ms: 1.03x slower                                                            |
| mdp                     | 1.60 sec                                                            | 1.66 sec: 1.04x slower                                                          |
| pickle_list             | 3.57 us                                                             | 3.71 us: 1.04x slower                                                           |
| deepcopy_reduce         | 2.59 us                                                             | 2.72 us: 1.05x slower                                                           |
| Geometric mean          | (ref)                                                               | 1.00x slower                                                                    |

Benchmark hidden because not significant (32): asyncio_tcp, asyncio_tcp_ssl, pathlib, tornado_http, async_tree_io_tg, sympy_integrate, docutils, pylint, gc_traversal, xml_etree_generate, thrift, sympy_sum, flaskblogging, deltablue, typing_runtime_protocols, async_tree_memoization, scimark_fft, spectral_norm, async_tree_io, python_startup_no_site, pickle, unpickle, logging_format, coroutines, xml_etree_process, async_tree_memoization_tg, raytrace, async_tree_cpu_io_mixed, django_template, async_tree_none, async_tree_none_tg, async_tree_cpu_io_mixed_tg

# HPT report

- Reliability score: 50.59% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown