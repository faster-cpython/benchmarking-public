# Results vs. base

- fork: brandtbucher
- ref: justin_unlikely
- machine: windows-x86
- commit hash: 15229e0
- commit date: 2024-10-17
- overall geometric mean: 1.00x faster
- HPT reliability: 52.91%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241017-pythonperf1_win32-x86-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:-------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| docutils       | 2.06 sec                                                                        | 2.05 sec: 1.01x faster                                                           |
| html5lib       | 45.9 ms                                                                         | 46.6 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                                           | 1.00x slower                                                                     |

Benchmark hidden because not significant (3): 2to3, sphinx, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241017-pythonperf1_win32-x86-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------|:-------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_none            | 225 ms                                                                          | 218 ms: 1.03x faster                                                             |
| async_tree_cpu_io_mixed    | 471 ms                                                                          | 462 ms: 1.02x faster                                                             |
| async_tree_cpu_io_mixed_tg | 467 ms                                                                          | 462 ms: 1.01x faster                                                             |
| async_generators           | 311 ms                                                                          | 314 ms: 1.01x slower                                                             |
| async_tree_io_tg           | 551 ms                                                                          | 555 ms: 1.01x slower                                                             |
| Geometric mean             | (ref)                                                                           | 1.01x faster                                                                     |

Benchmark hidden because not significant (7): asyncio_tcp, async_tree_memoization_tg, async_tree_memoization, coroutines, asyncio_tcp_ssl, async_tree_none_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241017-pythonperf1_win32-x86-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:-------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 65.5 ms                                                                         | 57.1 ms: 1.15x faster                                                            |
| Geometric mean | (ref)                                                                           | 1.05x faster                                                                     |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241017-pythonperf1_win32-x86-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:-------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_v8       | 15.4 ms                                                                         | 15.0 ms: 1.03x faster                                                            |
| regex_effbot   | 1.85 ms                                                                         | 1.80 ms: 1.02x faster                                                            |
| regex_dna      | 116 ms                                                                          | 113 ms: 1.02x faster                                                             |
| Geometric mean | (ref)                                                                           | 1.02x faster                                                                     |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241017-pythonperf1_win32-x86-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------|:-------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 163 us                                                                          | 156 us: 1.05x faster                                                             |
| json_dumps           | 8.12 ms                                                                         | 7.95 ms: 1.02x faster                                                            |
| tomli_loads          | 1.51 sec                                                                        | 1.49 sec: 1.02x faster                                                           |
| xml_etree_parse      | 111 ms                                                                          | 109 ms: 1.01x faster                                                             |
| xml_etree_iterparse  | 63.7 ms                                                                         | 63.0 ms: 1.01x faster                                                            |
| unpickle             | 10.6 us                                                                         | 10.4 us: 1.01x faster                                                            |
| unpickle_list        | 2.94 us                                                                         | 2.98 us: 1.01x slower                                                            |
| pickle_pure_python   | 239 us                                                                          | 244 us: 1.02x slower                                                             |
| xml_etree_generate   | 53.8 ms                                                                         | 55.0 ms: 1.02x slower                                                            |
| xml_etree_process    | 40.3 ms                                                                         | 41.5 ms: 1.03x slower                                                            |
| pickle               | 8.27 us                                                                         | 8.55 us: 1.03x slower                                                            |
| Geometric mean       | (ref)                                                                           | 1.00x faster                                                                     |

Benchmark hidden because not significant (3): json_loads, pickle_list, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241017-pythonperf1_win32-x86-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:-------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup | 27.1 ms                                                                         | 26.8 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                                           | 1.01x faster                                                                     |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241017-pythonperf1_win32-x86-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-----------------|:-------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 5.75 ms                                                                         | 5.82 ms: 1.01x slower                                                            |
| genshi_xml      | 54.5 ms                                                                         | 55.2 ms: 1.01x slower                                                            |
| django_template | 32.3 ms                                                                         | 33.3 ms: 1.03x slower                                                            |
| genshi_text     | 22.9 ms                                                                         | 24.6 ms: 1.08x slower                                                            |
| Geometric mean  | (ref)                                                                           | 1.03x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241017-pythonperf1_win32-x86-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------|:-------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody                      | 65.5 ms                                                                         | 57.1 ms: 1.15x faster                                                            |
| unpack_sequence            | 42.9 ns                                                                         | 39.5 ns: 1.09x faster                                                            |
| deepcopy_reduce            | 2.44 us                                                                         | 2.28 us: 1.07x faster                                                            |
| unpickle_pure_python       | 163 us                                                                          | 156 us: 1.05x faster                                                             |
| coverage                   | 55.7 ms                                                                         | 53.8 ms: 1.04x faster                                                            |
| scimark_monte_carlo        | 40.8 ms                                                                         | 39.6 ms: 1.03x faster                                                            |
| deepcopy                   | 232 us                                                                          | 225 us: 1.03x faster                                                             |
| async_tree_none            | 225 ms                                                                          | 218 ms: 1.03x faster                                                             |
| logging_silent             | 56.1 ns                                                                         | 54.6 ns: 1.03x faster                                                            |
| typing_runtime_protocols   | 143 us                                                                          | 139 us: 1.03x faster                                                             |
| regex_v8                   | 15.4 ms                                                                         | 15.0 ms: 1.03x faster                                                            |
| regex_effbot               | 1.85 ms                                                                         | 1.80 ms: 1.02x faster                                                            |
| pyflate                    | 318 ms                                                                          | 311 ms: 1.02x faster                                                             |
| json_dumps                 | 8.12 ms                                                                         | 7.95 ms: 1.02x faster                                                            |
| regex_dna                  | 116 ms                                                                          | 113 ms: 1.02x faster                                                             |
| go                         | 96.7 ms                                                                         | 94.8 ms: 1.02x faster                                                            |
| async_tree_cpu_io_mixed    | 471 ms                                                                          | 462 ms: 1.02x faster                                                             |
| tomli_loads                | 1.51 sec                                                                        | 1.49 sec: 1.02x faster                                                           |
| scimark_sor                | 69.2 ms                                                                         | 68.1 ms: 1.02x faster                                                            |
| hexiom                     | 5.47 ms                                                                         | 5.39 ms: 1.01x faster                                                            |
| pprint_pformat             | 1.18 sec                                                                        | 1.17 sec: 1.01x faster                                                           |
| xml_etree_parse            | 111 ms                                                                          | 109 ms: 1.01x faster                                                             |
| deepcopy_memo              | 16.1 us                                                                         | 15.9 us: 1.01x faster                                                            |
| telco                      | 6.03 ms                                                                         | 5.95 ms: 1.01x faster                                                            |
| nqueens                    | 78.3 ms                                                                         | 77.4 ms: 1.01x faster                                                            |
| python_startup             | 27.1 ms                                                                         | 26.8 ms: 1.01x faster                                                            |
| xml_etree_iterparse        | 63.7 ms                                                                         | 63.0 ms: 1.01x faster                                                            |
| sympy_expand               | 401 ms                                                                          | 397 ms: 1.01x faster                                                             |
| crypto_pyaes               | 50.5 ms                                                                         | 50.0 ms: 1.01x faster                                                            |
| unpickle                   | 10.6 us                                                                         | 10.4 us: 1.01x faster                                                            |
| async_tree_cpu_io_mixed_tg | 467 ms                                                                          | 462 ms: 1.01x faster                                                             |
| pprint_safe_repr           | 569 ms                                                                          | 564 ms: 1.01x faster                                                             |
| sympy_integrate            | 17.5 ms                                                                         | 17.4 ms: 1.01x faster                                                            |
| docutils                   | 2.06 sec                                                                        | 2.05 sec: 1.01x faster                                                           |
| spectral_norm              | 58.0 ms                                                                         | 58.3 ms: 1.01x slower                                                            |
| async_generators           | 311 ms                                                                          | 314 ms: 1.01x slower                                                             |
| async_tree_io_tg           | 551 ms                                                                          | 555 ms: 1.01x slower                                                             |
| generators                 | 24.1 ms                                                                         | 24.3 ms: 1.01x slower                                                            |
| scimark_fft                | 181 ms                                                                          | 183 ms: 1.01x slower                                                             |
| mako                       | 5.75 ms                                                                         | 5.82 ms: 1.01x slower                                                            |
| sqlite_synth               | 1.94 us                                                                         | 1.97 us: 1.01x slower                                                            |
| bench_mp_pool              | 94.4 ms                                                                         | 95.5 ms: 1.01x slower                                                            |
| richards                   | 38.9 ms                                                                         | 39.3 ms: 1.01x slower                                                            |
| genshi_xml                 | 54.5 ms                                                                         | 55.2 ms: 1.01x slower                                                            |
| pycparser                  | 822 ms                                                                          | 833 ms: 1.01x slower                                                             |
| unpickle_list              | 2.94 us                                                                         | 2.98 us: 1.01x slower                                                            |
| html5lib                   | 45.9 ms                                                                         | 46.6 ms: 1.01x slower                                                            |
| sqlglot_parse              | 1.04 ms                                                                         | 1.05 ms: 1.02x slower                                                            |
| sympy_sum                  | 117 ms                                                                          | 119 ms: 1.02x slower                                                             |
| pickle_pure_python         | 239 us                                                                          | 244 us: 1.02x slower                                                             |
| gc_traversal               | 1.79 ms                                                                         | 1.83 ms: 1.02x slower                                                            |
| thrift                     | 778 us                                                                          | 794 us: 1.02x slower                                                             |
| xml_etree_generate         | 53.8 ms                                                                         | 55.0 ms: 1.02x slower                                                            |
| sqlglot_optimize           | 49.2 ms                                                                         | 50.3 ms: 1.02x slower                                                            |
| sqlglot_normalize          | 100 ms                                                                          | 103 ms: 1.03x slower                                                             |
| scimark_sparse_mat_mult    | 2.48 ms                                                                         | 2.55 ms: 1.03x slower                                                            |
| xml_etree_process          | 40.3 ms                                                                         | 41.5 ms: 1.03x slower                                                            |
| comprehensions             | 12.8 us                                                                         | 13.2 us: 1.03x slower                                                            |
| django_template            | 32.3 ms                                                                         | 33.3 ms: 1.03x slower                                                            |
| pickle                     | 8.27 us                                                                         | 8.55 us: 1.03x slower                                                            |
| chaos                      | 52.8 ms                                                                         | 55.2 ms: 1.04x slower                                                            |
| richards_super             | 44.0 ms                                                                         | 46.2 ms: 1.05x slower                                                            |
| raytrace                   | 256 ms                                                                          | 273 ms: 1.07x slower                                                             |
| mdp                        | 1.68 sec                                                                        | 1.80 sec: 1.07x slower                                                           |
| genshi_text                | 22.9 ms                                                                         | 24.6 ms: 1.08x slower                                                            |
| Geometric mean             | (ref)                                                                           | 1.00x faster                                                                     |

Benchmark hidden because not significant (31): asyncio_tcp, async_tree_memoization_tg, async_tree_memoization, regex_compile, python_startup_no_site, deltablue, sphinx, json_loads, scimark_lu, pickle_list, logging_format, pickle_dict, create_gc_cycles, logging_simple, float, pidigits, 2to3, pathlib, sqlglot_transpile, sympy_str, fannkuch, meteor_contest, coroutines, asyncio_tcp_ssl, dulwich_log, async_tree_none_tg, bench_thread_pool, tornado_http, pylint, async_tree_io, json

# HPT report

- Reliability score: 52.91% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown