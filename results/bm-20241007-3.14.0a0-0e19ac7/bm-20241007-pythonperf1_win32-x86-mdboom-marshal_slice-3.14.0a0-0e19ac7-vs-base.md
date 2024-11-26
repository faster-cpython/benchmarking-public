# Results vs. base

- fork: mdboom
- ref: marshal_slice
- machine: windows-x86
- commit hash: 0e19ac7
- commit date: 2024-10-07
- overall geometric mean: 1.008x slower
- HPT reliability: 98.81%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:------------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 250 ms                                                                         | 255 ms: 1.02x slower                                                    |
| docutils       | 1.87 sec                                                                       | 1.90 sec: 1.02x slower                                                  |
| Geometric mean | (ref)                                                                          | 1.01x slower                                                            |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------------|:------------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 491 ms                                                                         | 473 ms: 1.04x faster                                                    |
| async_tree_cpu_io_mixed_tg | 475 ms                                                                         | 460 ms: 1.03x faster                                                    |
| async_tree_io_tg           | 527 ms                                                                         | 518 ms: 1.02x faster                                                    |
| async_tree_memoization     | 276 ms                                                                         | 274 ms: 1.01x faster                                                    |
| coroutines                 | 18.5 ms                                                                        | 18.4 ms: 1.01x faster                                                   |
| async_generators           | 302 ms                                                                         | 305 ms: 1.01x slower                                                    |
| Geometric mean             | (ref)                                                                          | 1.01x faster                                                            |

Benchmark hidden because not significant (6): async_tree_none_tg, async_tree_memoization_tg, async_tree_io, async_tree_none, asyncio_tcp_ssl, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:------------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 200 ms                                                                         | 201 ms: 1.01x slower                                                    |
| float          | 61.7 ms                                                                        | 63.6 ms: 1.03x slower                                                   |
| nbody          | 91.6 ms                                                                        | 96.4 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                                          | 1.03x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:------------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 120 ms                                                                         | 116 ms: 1.04x faster                                                    |
| regex_v8       | 16.2 ms                                                                        | 16.1 ms: 1.01x faster                                                   |
| regex_compile  | 110 ms                                                                         | 111 ms: 1.00x slower                                                    |
| Geometric mean | (ref)                                                                          | 1.01x faster                                                            |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------|:------------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_list          | 3.41 us                                                                        | 3.31 us: 1.03x faster                                                   |
| pickle               | 8.18 us                                                                        | 7.95 us: 1.03x faster                                                   |
| unpickle             | 10.4 us                                                                        | 10.2 us: 1.02x faster                                                   |
| json_loads           | 21.3 us                                                                        | 20.9 us: 1.02x faster                                                   |
| pickle_dict          | 20.7 us                                                                        | 20.3 us: 1.02x faster                                                   |
| tomli_loads          | 1.92 sec                                                                       | 1.91 sec: 1.01x faster                                                  |
| xml_etree_parse      | 108 ms                                                                         | 107 ms: 1.01x faster                                                    |
| unpickle_list        | 3.00 us                                                                        | 3.02 us: 1.01x slower                                                   |
| json_dumps           | 7.54 ms                                                                        | 7.75 ms: 1.03x slower                                                   |
| xml_etree_process    | 50.7 ms                                                                        | 52.5 ms: 1.04x slower                                                   |
| unpickle_pure_python | 183 us                                                                         | 190 us: 1.04x slower                                                    |
| Geometric mean       | (ref)                                                                          | 1.00x faster                                                            |

Benchmark hidden because not significant (3): xml_etree_iterparse, pickle_pure_python, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:------------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 24.1 ms                                                                        | 23.8 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                                          | 1.01x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|-----------------|:------------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 48.7 ms                                                                        | 46.6 ms: 1.05x faster                                                   |
| mako            | 8.12 ms                                                                        | 8.22 ms: 1.01x slower                                                   |
| genshi_text     | 22.6 ms                                                                        | 23.0 ms: 1.02x slower                                                   |
| django_template | 34.3 ms                                                                        | 35.2 ms: 1.02x slower                                                   |
| Geometric mean  | (ref)                                                                          | 1.00x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------------|:------------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml                 | 48.7 ms                                                                        | 46.6 ms: 1.05x faster                                                   |
| mdp                        | 1.77 sec                                                                       | 1.70 sec: 1.04x faster                                                  |
| async_tree_cpu_io_mixed    | 491 ms                                                                         | 473 ms: 1.04x faster                                                    |
| regex_dna                  | 120 ms                                                                         | 116 ms: 1.04x faster                                                    |
| deepcopy_memo              | 22.9 us                                                                        | 22.1 us: 1.03x faster                                                   |
| async_tree_cpu_io_mixed_tg | 475 ms                                                                         | 460 ms: 1.03x faster                                                    |
| thrift                     | 769 us                                                                         | 745 us: 1.03x faster                                                    |
| pickle_list                | 3.41 us                                                                        | 3.31 us: 1.03x faster                                                   |
| pickle                     | 8.18 us                                                                        | 7.95 us: 1.03x faster                                                   |
| unpack_sequence            | 46.7 ns                                                                        | 45.4 ns: 1.03x faster                                                   |
| unpickle                   | 10.4 us                                                                        | 10.2 us: 1.02x faster                                                   |
| json_loads                 | 21.3 us                                                                        | 20.9 us: 1.02x faster                                                   |
| pickle_dict                | 20.7 us                                                                        | 20.3 us: 1.02x faster                                                   |
| async_tree_io_tg           | 527 ms                                                                         | 518 ms: 1.02x faster                                                    |
| bench_thread_pool          | 1.01 ms                                                                        | 999 us: 1.01x faster                                                    |
| deepcopy                   | 247 us                                                                         | 244 us: 1.01x faster                                                    |
| richards                   | 41.4 ms                                                                        | 40.8 ms: 1.01x faster                                                   |
| sqlite_synth               | 1.98 us                                                                        | 1.95 us: 1.01x faster                                                   |
| typing_runtime_protocols   | 148 us                                                                         | 146 us: 1.01x faster                                                    |
| python_startup             | 24.1 ms                                                                        | 23.8 ms: 1.01x faster                                                   |
| async_tree_memoization     | 276 ms                                                                         | 274 ms: 1.01x faster                                                    |
| dulwich_log                | 52.5 ms                                                                        | 52.1 ms: 1.01x faster                                                   |
| regex_v8                   | 16.2 ms                                                                        | 16.1 ms: 1.01x faster                                                   |
| tomli_loads                | 1.92 sec                                                                       | 1.91 sec: 1.01x faster                                                  |
| coroutines                 | 18.5 ms                                                                        | 18.4 ms: 1.01x faster                                                   |
| xml_etree_parse            | 108 ms                                                                         | 107 ms: 1.01x faster                                                    |
| meteor_contest             | 79.8 ms                                                                        | 80.1 ms: 1.00x slower                                                   |
| regex_compile              | 110 ms                                                                         | 111 ms: 1.00x slower                                                    |
| bench_mp_pool              | 72.9 ms                                                                        | 73.1 ms: 1.00x slower                                                   |
| unpickle_list              | 3.00 us                                                                        | 3.02 us: 1.01x slower                                                   |
| logging_simple             | 8.18 us                                                                        | 8.23 us: 1.01x slower                                                   |
| pidigits                   | 200 ms                                                                         | 201 ms: 1.01x slower                                                    |
| coverage                   | 53.6 ms                                                                        | 54.0 ms: 1.01x slower                                                   |
| go                         | 110 ms                                                                         | 111 ms: 1.01x slower                                                    |
| async_generators           | 302 ms                                                                         | 305 ms: 1.01x slower                                                    |
| comprehensions             | 14.0 us                                                                        | 14.1 us: 1.01x slower                                                   |
| sympy_sum                  | 108 ms                                                                         | 109 ms: 1.01x slower                                                    |
| mako                       | 8.12 ms                                                                        | 8.22 ms: 1.01x slower                                                   |
| logging_silent             | 74.7 ns                                                                        | 75.6 ns: 1.01x slower                                                   |
| sqlglot_normalize          | 236 ms                                                                         | 240 ms: 1.01x slower                                                    |
| docutils                   | 1.87 sec                                                                       | 1.90 sec: 1.02x slower                                                  |
| pycparser                  | 861 ms                                                                         | 875 ms: 1.02x slower                                                    |
| genshi_text                | 22.6 ms                                                                        | 23.0 ms: 1.02x slower                                                   |
| scimark_fft                | 233 ms                                                                         | 237 ms: 1.02x slower                                                    |
| richards_super             | 46.2 ms                                                                        | 47.0 ms: 1.02x slower                                                   |
| gc_traversal               | 1.43 ms                                                                        | 1.45 ms: 1.02x slower                                                   |
| 2to3                       | 250 ms                                                                         | 255 ms: 1.02x slower                                                    |
| sqlglot_optimize           | 45.5 ms                                                                        | 46.4 ms: 1.02x slower                                                   |
| sympy_str                  | 218 ms                                                                         | 222 ms: 1.02x slower                                                    |
| crypto_pyaes               | 57.8 ms                                                                        | 59.0 ms: 1.02x slower                                                   |
| hexiom                     | 5.23 ms                                                                        | 5.34 ms: 1.02x slower                                                   |
| sympy_integrate            | 15.7 ms                                                                        | 16.0 ms: 1.02x slower                                                   |
| sympy_expand               | 385 ms                                                                         | 394 ms: 1.02x slower                                                    |
| django_template            | 34.3 ms                                                                        | 35.2 ms: 1.02x slower                                                   |
| spectral_norm              | 78.5 ms                                                                        | 80.5 ms: 1.02x slower                                                   |
| scimark_lu                 | 69.2 ms                                                                        | 71.1 ms: 1.03x slower                                                   |
| pprint_pformat             | 1.40 sec                                                                       | 1.44 sec: 1.03x slower                                                  |
| json_dumps                 | 7.54 ms                                                                        | 7.75 ms: 1.03x slower                                                   |
| generators                 | 26.7 ms                                                                        | 27.5 ms: 1.03x slower                                                   |
| float                      | 61.7 ms                                                                        | 63.6 ms: 1.03x slower                                                   |
| nqueens                    | 75.1 ms                                                                        | 77.5 ms: 1.03x slower                                                   |
| fannkuch                   | 313 ms                                                                         | 324 ms: 1.03x slower                                                    |
| xml_etree_process          | 50.7 ms                                                                        | 52.5 ms: 1.04x slower                                                   |
| unpickle_pure_python       | 183 us                                                                         | 190 us: 1.04x slower                                                    |
| sqlglot_transpile          | 1.32 ms                                                                        | 1.37 ms: 1.04x slower                                                   |
| scimark_sor                | 99.0 ms                                                                        | 103 ms: 1.04x slower                                                    |
| sqlglot_parse              | 1.07 ms                                                                        | 1.12 ms: 1.04x slower                                                   |
| create_gc_cycles           | 732 us                                                                         | 764 us: 1.04x slower                                                    |
| nbody                      | 91.6 ms                                                                        | 96.4 ms: 1.05x slower                                                   |
| telco                      | 6.48 ms                                                                        | 6.85 ms: 1.06x slower                                                   |
| scimark_sparse_mat_mult    | 3.11 ms                                                                        | 3.29 ms: 1.06x slower                                                   |
| scimark_monte_carlo        | 55.3 ms                                                                        | 58.6 ms: 1.06x slower                                                   |
| Geometric mean             | (ref)                                                                          | 1.01x slower                                                            |

Benchmark hidden because not significant (23): async_tree_none_tg, async_tree_memoization_tg, async_tree_io, async_tree_none, regex_effbot, raytrace, xml_etree_iterparse, chaos, logging_format, pyflate, pprint_safe_repr, deepcopy_reduce, python_startup_no_site, pathlib, html5lib, deltablue, pickle_pure_python, asyncio_tcp_ssl, xml_etree_generate, pylint, tornado_http, json, asyncio_tcp

- Geometric mean (including insignificant results): 1.008x slower
# HPT report

- Reliability score: 98.81% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown