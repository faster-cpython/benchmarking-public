# Results vs. base

- fork: brandtbucher
- ref: justin_unlikely
- machine: windows-x86
- commit hash: 15229e0
- commit date: 2024-10-17
- overall geometric mean: 1.01x faster
- HPT reliability: 93.59%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241017-pythonperf1_win32-x86-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:-------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                                          | 264 ms: 1.01x faster                                                             |
| html5lib       | 45.9 ms                                                                         | 46.6 ms: 1.01x slower                                                            |
| sphinx         | 854 ms                                                                          | 848 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                                           | 1.00x slower                                                                     |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241017-pythonperf1_win32-x86-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------|:-------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp                | 875 ms                                                                          | 832 ms: 1.05x faster                                                             |
| async_tree_cpu_io_mixed    | 477 ms                                                                          | 462 ms: 1.03x faster                                                             |
| coroutines                 | 17.9 ms                                                                         | 17.4 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed_tg | 475 ms                                                                          | 462 ms: 1.03x faster                                                             |
| async_tree_none            | 223 ms                                                                          | 218 ms: 1.02x faster                                                             |
| async_generators           | 320 ms                                                                          | 314 ms: 1.02x faster                                                             |
| Geometric mean             | (ref)                                                                           | 1.01x faster                                                                     |

Benchmark hidden because not significant (6): async_tree_memoization, async_tree_memoization_tg, async_tree_none_tg, async_tree_io_tg, asyncio_tcp_ssl, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241017-pythonperf1_win32-x86-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:-------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 64.8 ms                                                                         | 57.1 ms: 1.13x faster                                                            |
| pidigits       | 201 ms                                                                          | 200 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                                           | 1.04x faster                                                                     |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241017-pythonperf1_win32-x86-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:-------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_v8       | 15.7 ms                                                                         | 15.0 ms: 1.04x faster                                                            |
| regex_effbot   | 1.81 ms                                                                         | 1.80 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                                           | 1.01x faster                                                                     |

Benchmark hidden because not significant (2): regex_dna, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241017-pythonperf1_win32-x86-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------|:-------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 163 us                                                                          | 156 us: 1.04x faster                                                             |
| pickle_list          | 3.50 us                                                                         | 3.40 us: 1.03x faster                                                            |
| json_loads           | 21.1 us                                                                         | 20.5 us: 1.03x faster                                                            |
| tomli_loads          | 1.52 sec                                                                        | 1.49 sec: 1.02x faster                                                           |
| json_dumps           | 8.14 ms                                                                         | 7.95 ms: 1.02x faster                                                            |
| xml_etree_parse      | 111 ms                                                                          | 109 ms: 1.02x faster                                                             |
| pickle_dict          | 21.6 us                                                                         | 21.2 us: 1.02x faster                                                            |
| xml_etree_iterparse  | 64.2 ms                                                                         | 63.0 ms: 1.02x faster                                                            |
| xml_etree_generate   | 55.6 ms                                                                         | 55.0 ms: 1.01x faster                                                            |
| unpickle             | 10.4 us                                                                         | 10.4 us: 1.01x slower                                                            |
| unpickle_list        | 2.80 us                                                                         | 2.98 us: 1.07x slower                                                            |
| Geometric mean       | (ref)                                                                           | 1.01x faster                                                                     |

Benchmark hidden because not significant (3): pickle_pure_python, xml_etree_process, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241017-pythonperf1_win32-x86-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|------------------------|:-------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 21.1 ms                                                                         | 20.3 ms: 1.04x faster                                                            |
| python_startup         | 27.7 ms                                                                         | 26.8 ms: 1.03x faster                                                            |
| Geometric mean         | (ref)                                                                           | 1.04x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241017-pythonperf1_win32-x86-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-----------------|:-------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 5.75 ms                                                                         | 5.82 ms: 1.01x slower                                                            |
| genshi_xml      | 54.4 ms                                                                         | 55.2 ms: 1.01x slower                                                            |
| django_template | 32.8 ms                                                                         | 33.3 ms: 1.02x slower                                                            |
| genshi_text     | 23.4 ms                                                                         | 24.6 ms: 1.05x slower                                                            |
| Geometric mean  | (ref)                                                                           | 1.02x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241017-pythonperf1_win32-x86-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------|:-------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody                      | 64.8 ms                                                                         | 57.1 ms: 1.13x faster                                                            |
| asyncio_tcp                | 875 ms                                                                          | 832 ms: 1.05x faster                                                             |
| logging_silent             | 57.2 ns                                                                         | 54.6 ns: 1.05x faster                                                            |
| typing_runtime_protocols   | 146 us                                                                          | 139 us: 1.05x faster                                                             |
| bench_mp_pool              | 99.8 ms                                                                         | 95.5 ms: 1.05x faster                                                            |
| regex_v8                   | 15.7 ms                                                                         | 15.0 ms: 1.04x faster                                                            |
| unpickle_pure_python       | 163 us                                                                          | 156 us: 1.04x faster                                                             |
| python_startup_no_site     | 21.1 ms                                                                         | 20.3 ms: 1.04x faster                                                            |
| go                         | 98.4 ms                                                                         | 94.8 ms: 1.04x faster                                                            |
| crypto_pyaes               | 51.7 ms                                                                         | 50.0 ms: 1.04x faster                                                            |
| deepcopy_reduce            | 2.36 us                                                                         | 2.28 us: 1.03x faster                                                            |
| python_startup             | 27.7 ms                                                                         | 26.8 ms: 1.03x faster                                                            |
| pickle_list                | 3.50 us                                                                         | 3.40 us: 1.03x faster                                                            |
| async_tree_cpu_io_mixed    | 477 ms                                                                          | 462 ms: 1.03x faster                                                             |
| scimark_sor                | 70.2 ms                                                                         | 68.1 ms: 1.03x faster                                                            |
| coroutines                 | 17.9 ms                                                                         | 17.4 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed_tg | 475 ms                                                                          | 462 ms: 1.03x faster                                                             |
| json_loads                 | 21.1 us                                                                         | 20.5 us: 1.03x faster                                                            |
| deepcopy_memo              | 16.3 us                                                                         | 15.9 us: 1.02x faster                                                            |
| tomli_loads                | 1.52 sec                                                                        | 1.49 sec: 1.02x faster                                                           |
| json_dumps                 | 8.14 ms                                                                         | 7.95 ms: 1.02x faster                                                            |
| async_tree_none            | 223 ms                                                                          | 218 ms: 1.02x faster                                                             |
| raytrace                   | 279 ms                                                                          | 273 ms: 1.02x faster                                                             |
| xml_etree_parse            | 111 ms                                                                          | 109 ms: 1.02x faster                                                             |
| deepcopy                   | 230 us                                                                          | 225 us: 1.02x faster                                                             |
| scimark_monte_carlo        | 40.3 ms                                                                         | 39.6 ms: 1.02x faster                                                            |
| async_generators           | 320 ms                                                                          | 314 ms: 1.02x faster                                                             |
| pickle_dict                | 21.6 us                                                                         | 21.2 us: 1.02x faster                                                            |
| dulwich_log                | 50.4 ms                                                                         | 49.5 ms: 1.02x faster                                                            |
| xml_etree_iterparse        | 64.2 ms                                                                         | 63.0 ms: 1.02x faster                                                            |
| fannkuch                   | 248 ms                                                                          | 244 ms: 1.02x faster                                                             |
| pprint_safe_repr           | 572 ms                                                                          | 564 ms: 1.01x faster                                                             |
| generators                 | 24.6 ms                                                                         | 24.3 ms: 1.01x faster                                                            |
| meteor_contest             | 73.9 ms                                                                         | 73.1 ms: 1.01x faster                                                            |
| pyflate                    | 315 ms                                                                          | 311 ms: 1.01x faster                                                             |
| xml_etree_generate         | 55.6 ms                                                                         | 55.0 ms: 1.01x faster                                                            |
| 2to3                       | 267 ms                                                                          | 264 ms: 1.01x faster                                                             |
| hexiom                     | 5.44 ms                                                                         | 5.39 ms: 1.01x faster                                                            |
| pidigits                   | 201 ms                                                                          | 200 ms: 1.01x faster                                                             |
| sphinx                     | 854 ms                                                                          | 848 ms: 1.01x faster                                                             |
| regex_effbot               | 1.81 ms                                                                         | 1.80 ms: 1.01x faster                                                            |
| scimark_fft                | 183 ms                                                                          | 183 ms: 1.01x faster                                                             |
| unpickle                   | 10.4 us                                                                         | 10.4 us: 1.01x slower                                                            |
| sympy_str                  | 229 ms                                                                          | 231 ms: 1.01x slower                                                             |
| sqlglot_normalize          | 102 ms                                                                          | 103 ms: 1.01x slower                                                             |
| sqlglot_optimize           | 49.8 ms                                                                         | 50.3 ms: 1.01x slower                                                            |
| scimark_lu                 | 59.9 ms                                                                         | 60.6 ms: 1.01x slower                                                            |
| mako                       | 5.75 ms                                                                         | 5.82 ms: 1.01x slower                                                            |
| scimark_sparse_mat_mult    | 2.52 ms                                                                         | 2.55 ms: 1.01x slower                                                            |
| html5lib                   | 45.9 ms                                                                         | 46.6 ms: 1.01x slower                                                            |
| genshi_xml                 | 54.4 ms                                                                         | 55.2 ms: 1.01x slower                                                            |
| sqlglot_transpile          | 1.35 ms                                                                         | 1.37 ms: 1.01x slower                                                            |
| pycparser                  | 821 ms                                                                          | 833 ms: 1.01x slower                                                             |
| coverage                   | 53.0 ms                                                                         | 53.8 ms: 1.01x slower                                                            |
| logging_simple             | 7.53 us                                                                         | 7.65 us: 1.02x slower                                                            |
| gc_traversal               | 1.80 ms                                                                         | 1.83 ms: 1.02x slower                                                            |
| sympy_sum                  | 117 ms                                                                          | 119 ms: 1.02x slower                                                             |
| django_template            | 32.8 ms                                                                         | 33.3 ms: 1.02x slower                                                            |
| nqueens                    | 76.0 ms                                                                         | 77.4 ms: 1.02x slower                                                            |
| sqlglot_parse              | 1.03 ms                                                                         | 1.05 ms: 1.02x slower                                                            |
| comprehensions             | 12.9 us                                                                         | 13.2 us: 1.02x slower                                                            |
| sqlite_synth               | 1.92 us                                                                         | 1.97 us: 1.02x slower                                                            |
| telco                      | 5.79 ms                                                                         | 5.95 ms: 1.03x slower                                                            |
| richards_super             | 44.5 ms                                                                         | 46.2 ms: 1.04x slower                                                            |
| thrift                     | 757 us                                                                          | 794 us: 1.05x slower                                                             |
| genshi_text                | 23.4 ms                                                                         | 24.6 ms: 1.05x slower                                                            |
| mdp                        | 1.70 sec                                                                        | 1.80 sec: 1.06x slower                                                           |
| unpickle_list              | 2.80 us                                                                         | 2.98 us: 1.07x slower                                                            |
| Geometric mean             | (ref)                                                                           | 1.01x faster                                                                     |

Benchmark hidden because not significant (28): spectral_norm, async_tree_memoization, pickle_pure_python, xml_etree_process, async_tree_memoization_tg, pprint_pformat, unpack_sequence, richards, pathlib, create_gc_cycles, regex_dna, docutils, pickle, async_tree_none_tg, deltablue, sympy_integrate, regex_compile, chaos, async_tree_io_tg, sympy_expand, float, pylint, tornado_http, asyncio_tcp_ssl, logging_format, async_tree_io, bench_thread_pool, json

# HPT report

- Reliability score: 93.59% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown