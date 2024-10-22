# Results vs. base

- fork: mdboom
- ref: remove_redundant_typ
- machine: windows-x86
- commit hash: b0f5f3a
- commit date: 2024-09-23
- overall geometric mean: 1.00x faster
- HPT reliability: 80.70%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75 | bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 249 ms                                                                         | 251 ms: 1.00x slower                                                           |
| html5lib       | 46.5 ms                                                                        | 45.5 ms: 1.02x faster                                                          |
| Geometric mean | (ref)                                                                          | 1.00x faster                                                                   |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75 | bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization     | 273 ms                                                                         | 270 ms: 1.01x faster                                                           |
| async_generators           | 301 ms                                                                         | 303 ms: 1.01x slower                                                           |
| async_tree_cpu_io_mixed_tg | 455 ms                                                                         | 476 ms: 1.05x slower                                                           |
| async_tree_cpu_io_mixed    | 464 ms                                                                         | 487 ms: 1.05x slower                                                           |
| Geometric mean             | (ref)                                                                          | 1.01x slower                                                                   |

Benchmark hidden because not significant (8): asyncio_tcp, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, asyncio_tcp_ssl, async_tree_io_tg, async_tree_io, coroutines

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75 | bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 121 ms                                                                         | 117 ms: 1.03x faster                                                           |
| regex_compile  | 109 ms                                                                         | 108 ms: 1.01x faster                                                           |
| regex_v8       | 16.2 ms                                                                        | 16.0 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                                          | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75 | bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle_pure_python | 180 us                                                                         | 177 us: 1.02x faster                                                           |
| pickle_pure_python   | 262 us                                                                         | 260 us: 1.01x faster                                                           |
| unpickle_list        | 3.00 us                                                                        | 3.01 us: 1.00x slower                                                          |
| pickle_dict          | 20.6 us                                                                        | 20.8 us: 1.01x slower                                                          |
| xml_etree_process    | 49.4 ms                                                                        | 49.9 ms: 1.01x slower                                                          |
| pickle_list          | 3.35 us                                                                        | 3.40 us: 1.01x slower                                                          |
| unpickle             | 10.3 us                                                                        | 10.4 us: 1.02x slower                                                          |
| xml_etree_generate   | 67.5 ms                                                                        | 69.1 ms: 1.02x slower                                                          |
| Geometric mean       | (ref)                                                                          | 1.00x slower                                                                   |

Benchmark hidden because not significant (6): pickle, tomli_loads, json_loads, xml_etree_parse, xml_etree_iterparse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75 | bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|------------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 23.5 ms                                                                        | 23.7 ms: 1.01x slower                                                          |
| python_startup_no_site | 19.4 ms                                                                        | 19.7 ms: 1.01x slower                                                          |
| Geometric mean         | (ref)                                                                          | 1.01x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75 | bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|-----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_text     | 24.2 ms                                                                        | 22.3 ms: 1.09x faster                                                          |
| genshi_xml      | 50.3 ms                                                                        | 47.7 ms: 1.05x faster                                                          |
| django_template | 33.6 ms                                                                        | 33.2 ms: 1.01x faster                                                          |
| mako            | 8.16 ms                                                                        | 8.09 ms: 1.01x faster                                                          |
| Geometric mean  | (ref)                                                                          | 1.04x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75 | bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_text                | 24.2 ms                                                                        | 22.3 ms: 1.09x faster                                                          |
| genshi_xml                 | 50.3 ms                                                                        | 47.7 ms: 1.05x faster                                                          |
| scimark_sor                | 105 ms                                                                         | 101 ms: 1.04x faster                                                           |
| nqueens                    | 77.3 ms                                                                        | 74.6 ms: 1.04x faster                                                          |
| fannkuch                   | 336 ms                                                                         | 326 ms: 1.03x faster                                                           |
| regex_dna                  | 121 ms                                                                         | 117 ms: 1.03x faster                                                           |
| comprehensions             | 14.1 us                                                                        | 13.7 us: 1.03x faster                                                          |
| unpickle_pure_python       | 180 us                                                                         | 177 us: 1.02x faster                                                           |
| pprint_pformat             | 1.40 sec                                                                       | 1.37 sec: 1.02x faster                                                         |
| html5lib                   | 46.5 ms                                                                        | 45.5 ms: 1.02x faster                                                          |
| deepcopy                   | 250 us                                                                         | 245 us: 1.02x faster                                                           |
| pycparser                  | 877 ms                                                                         | 862 ms: 1.02x faster                                                           |
| json                       | 4.32 ms                                                                        | 4.24 ms: 1.02x faster                                                          |
| logging_silent             | 74.6 ns                                                                        | 73.5 ns: 1.01x faster                                                          |
| django_template            | 33.6 ms                                                                        | 33.2 ms: 1.01x faster                                                          |
| dulwich_log                | 51.2 ms                                                                        | 50.6 ms: 1.01x faster                                                          |
| regex_compile              | 109 ms                                                                         | 108 ms: 1.01x faster                                                           |
| pprint_safe_repr           | 684 ms                                                                         | 676 ms: 1.01x faster                                                           |
| scimark_fft                | 239 ms                                                                         | 236 ms: 1.01x faster                                                           |
| pyflate                    | 362 ms                                                                         | 358 ms: 1.01x faster                                                           |
| async_tree_memoization     | 273 ms                                                                         | 270 ms: 1.01x faster                                                           |
| regex_v8                   | 16.2 ms                                                                        | 16.0 ms: 1.01x faster                                                          |
| pickle_pure_python         | 262 us                                                                         | 260 us: 1.01x faster                                                           |
| go                         | 107 ms                                                                         | 106 ms: 1.01x faster                                                           |
| meteor_contest             | 81.4 ms                                                                        | 80.6 ms: 1.01x faster                                                          |
| mako                       | 8.16 ms                                                                        | 8.09 ms: 1.01x faster                                                          |
| hexiom                     | 5.17 ms                                                                        | 5.13 ms: 1.01x faster                                                          |
| coverage                   | 53.2 ms                                                                        | 52.7 ms: 1.01x faster                                                          |
| sqlglot_parse              | 1.10 ms                                                                        | 1.09 ms: 1.01x faster                                                          |
| generators                 | 26.0 ms                                                                        | 25.8 ms: 1.01x faster                                                          |
| sqlglot_normalize          | 233 ms                                                                         | 231 ms: 1.01x faster                                                           |
| sqlglot_optimize           | 44.6 ms                                                                        | 44.4 ms: 1.01x faster                                                          |
| deepcopy_memo              | 22.6 us                                                                        | 22.5 us: 1.01x faster                                                          |
| spectral_norm              | 75.9 ms                                                                        | 75.5 ms: 1.01x faster                                                          |
| logging_format             | 8.66 us                                                                        | 8.62 us: 1.00x faster                                                          |
| sqlglot_transpile          | 1.35 ms                                                                        | 1.34 ms: 1.00x faster                                                          |
| logging_simple             | 7.93 us                                                                        | 7.91 us: 1.00x faster                                                          |
| unpickle_list              | 3.00 us                                                                        | 3.01 us: 1.00x slower                                                          |
| pathlib                    | 83.5 ms                                                                        | 83.9 ms: 1.00x slower                                                          |
| 2to3                       | 249 ms                                                                         | 251 ms: 1.00x slower                                                           |
| typing_runtime_protocols   | 143 us                                                                         | 144 us: 1.01x slower                                                           |
| async_generators           | 301 ms                                                                         | 303 ms: 1.01x slower                                                           |
| chaos                      | 54.3 ms                                                                        | 54.7 ms: 1.01x slower                                                          |
| python_startup             | 23.5 ms                                                                        | 23.7 ms: 1.01x slower                                                          |
| scimark_sparse_mat_mult    | 3.06 ms                                                                        | 3.09 ms: 1.01x slower                                                          |
| richards_super             | 44.3 ms                                                                        | 44.8 ms: 1.01x slower                                                          |
| python_startup_no_site     | 19.4 ms                                                                        | 19.7 ms: 1.01x slower                                                          |
| pickle_dict                | 20.6 us                                                                        | 20.8 us: 1.01x slower                                                          |
| xml_etree_process          | 49.4 ms                                                                        | 49.9 ms: 1.01x slower                                                          |
| scimark_lu                 | 68.7 ms                                                                        | 69.6 ms: 1.01x slower                                                          |
| sympy_integrate            | 15.3 ms                                                                        | 15.5 ms: 1.01x slower                                                          |
| sympy_str                  | 216 ms                                                                         | 219 ms: 1.01x slower                                                           |
| scimark_monte_carlo        | 56.9 ms                                                                        | 57.7 ms: 1.01x slower                                                          |
| sympy_expand               | 381 ms                                                                         | 387 ms: 1.01x slower                                                           |
| pickle_list                | 3.35 us                                                                        | 3.40 us: 1.01x slower                                                          |
| unpickle                   | 10.3 us                                                                        | 10.4 us: 1.02x slower                                                          |
| raytrace                   | 233 ms                                                                         | 237 ms: 1.02x slower                                                           |
| bench_mp_pool              | 69.9 ms                                                                        | 71.4 ms: 1.02x slower                                                          |
| xml_etree_generate         | 67.5 ms                                                                        | 69.1 ms: 1.02x slower                                                          |
| richards                   | 39.4 ms                                                                        | 40.5 ms: 1.03x slower                                                          |
| telco                      | 6.61 ms                                                                        | 6.79 ms: 1.03x slower                                                          |
| deltablue                  | 2.67 ms                                                                        | 2.76 ms: 1.03x slower                                                          |
| deepcopy_reduce            | 2.50 us                                                                        | 2.60 us: 1.04x slower                                                          |
| mdp                        | 1.66 sec                                                                       | 1.73 sec: 1.04x slower                                                         |
| thrift                     | 746 us                                                                         | 779 us: 1.04x slower                                                           |
| async_tree_cpu_io_mixed_tg | 455 ms                                                                         | 476 ms: 1.05x slower                                                           |
| async_tree_cpu_io_mixed    | 464 ms                                                                         | 487 ms: 1.05x slower                                                           |
| Geometric mean             | (ref)                                                                          | 1.00x faster                                                                   |

Benchmark hidden because not significant (28): asyncio_tcp, async_tree_memoization_tg, regex_effbot, gc_traversal, pickle, tomli_loads, docutils, float, crypto_pyaes, json_loads, async_tree_none, async_tree_none_tg, asyncio_tcp_ssl, sqlite_synth, pidigits, nbody, unpack_sequence, xml_etree_parse, xml_etree_iterparse, create_gc_cycles, sympy_sum, json_dumps, async_tree_io_tg, async_tree_io, tornado_http, coroutines, pylint, bench_thread_pool

# HPT report

- Reliability score: 80.70% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown