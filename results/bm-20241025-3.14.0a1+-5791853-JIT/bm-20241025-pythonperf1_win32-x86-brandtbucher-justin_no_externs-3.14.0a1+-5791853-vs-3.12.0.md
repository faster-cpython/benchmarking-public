# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_no_externs
- machine: windows-x86
- commit hash: 5791853
- commit date: 2024-10-25
- overall geometric mean: 1.166x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 267 ms: 1.05x faster                                                               |
| docutils       | 1.98 sec                                                        | 2.05 sec: 1.04x slower                                                             |
| tornado_http   | 105 ms                                                          | 110 ms: 1.05x slower                                                               |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 252 ms: 1.39x faster                                                               |
| async_tree_none_tg         | 278 ms                                                          | 203 ms: 1.37x faster                                                               |
| async_tree_none            | 298 ms                                                          | 218 ms: 1.36x faster                                                               |
| async_tree_io              | 693 ms                                                          | 521 ms: 1.33x faster                                                               |
| async_tree_memoization     | 364 ms                                                          | 276 ms: 1.32x faster                                                               |
| async_tree_io_tg           | 677 ms                                                          | 552 ms: 1.23x faster                                                               |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 465 ms: 1.21x faster                                                               |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 462 ms: 1.18x faster                                                               |
| Geometric mean             | (ref)                                                           | 1.30x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 67.2 ms: 1.89x faster                                                              |
| float          | 76.7 ms                                                         | 49.7 ms: 1.54x faster                                                              |
| pidigits       | 199 ms                                                          | 207 ms: 1.04x slower                                                               |
| Geometric mean | (ref)                                                           | 1.41x faster                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 108 ms: 1.19x faster                                                               |
| regex_effbot   | 2.04 ms                                                         | 1.80 ms: 1.13x faster                                                              |
| regex_dna      | 127 ms                                                          | 120 ms: 1.06x faster                                                               |
| regex_v8       | 15.0 ms                                                         | 15.9 ms: 1.05x slower                                                              |
| Geometric mean | (ref)                                                           | 1.08x faster                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.56 sec: 1.41x faster                                                             |
| unpickle_pure_python | 210 us                                                          | 166 us: 1.26x faster                                                               |
| xml_etree_generate   | 72.1 ms                                                         | 60.5 ms: 1.19x faster                                                              |
| pickle_pure_python   | 286 us                                                          | 244 us: 1.17x faster                                                               |
| xml_etree_iterparse  | 77.6 ms                                                         | 66.6 ms: 1.17x faster                                                              |
| xml_etree_process    | 53.2 ms                                                         | 47.2 ms: 1.13x faster                                                              |
| xml_etree_parse      | 113 ms                                                          | 112 ms: 1.01x faster                                                               |
| json_loads           | 20.4 us                                                         | 20.9 us: 1.03x slower                                                              |
| json_dumps           | 7.40 ms                                                         | 8.11 ms: 1.10x slower                                                              |
| Geometric mean       | (ref)                                                           | 1.13x faster                                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.2 ms: 1.06x slower                                                              |
| python_startup         | 22.4 ms                                                         | 26.9 ms: 1.20x slower                                                              |
| Geometric mean         | (ref)                                                           | 1.13x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|-----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 6.29 ms: 1.58x faster                                                              |
| django_template | 36.9 ms                                                         | 32.4 ms: 1.14x faster                                                              |
| Geometric mean  | (ref)                                                           | 1.34x faster                                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 18.0 us: 2.13x faster                                                              |
| nbody                      | 127 ms                                                          | 67.2 ms: 1.89x faster                                                              |
| scimark_sor                | 130 ms                                                          | 78.0 ms: 1.66x faster                                                              |
| logging_silent             | 101 ns                                                          | 63.6 ns: 1.59x faster                                                              |
| mako                       | 9.96 ms                                                         | 6.29 ms: 1.58x faster                                                              |
| float                      | 76.7 ms                                                         | 49.7 ms: 1.54x faster                                                              |
| spectral_norm              | 104 ms                                                          | 68.5 ms: 1.52x faster                                                              |
| deepcopy                   | 360 us                                                          | 244 us: 1.47x faster                                                               |
| scimark_monte_carlo        | 66.4 ms                                                         | 45.2 ms: 1.47x faster                                                              |
| generators                 | 38.5 ms                                                         | 26.6 ms: 1.44x faster                                                              |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.73 ms: 1.41x faster                                                              |
| tomli_loads                | 2.20 sec                                                        | 1.56 sec: 1.41x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 252 ms: 1.39x faster                                                               |
| go                         | 137 ms                                                          | 99.8 ms: 1.38x faster                                                              |
| async_tree_none_tg         | 278 ms                                                          | 203 ms: 1.37x faster                                                               |
| comprehensions             | 19.2 us                                                         | 14.0 us: 1.37x faster                                                              |
| async_tree_none            | 298 ms                                                          | 218 ms: 1.36x faster                                                               |
| scimark_lu                 | 93.2 ms                                                         | 68.9 ms: 1.35x faster                                                              |
| async_tree_io              | 693 ms                                                          | 521 ms: 1.33x faster                                                               |
| deltablue                  | 3.58 ms                                                         | 2.71 ms: 1.32x faster                                                              |
| async_tree_memoization     | 364 ms                                                          | 276 ms: 1.32x faster                                                               |
| scimark_fft                | 271 ms                                                          | 206 ms: 1.32x faster                                                               |
| deepcopy_reduce            | 3.23 us                                                         | 2.50 us: 1.29x faster                                                              |
| crypto_pyaes               | 69.2 ms                                                         | 54.6 ms: 1.27x faster                                                              |
| logging_simple             | 9.75 us                                                         | 7.70 us: 1.27x faster                                                              |
| pyflate                    | 424 ms                                                          | 335 ms: 1.26x faster                                                               |
| unpickle_pure_python       | 210 us                                                          | 166 us: 1.26x faster                                                               |
| logging_format             | 10.4 us                                                         | 8.40 us: 1.24x faster                                                              |
| fannkuch                   | 354 ms                                                          | 286 ms: 1.24x faster                                                               |
| raytrace                   | 308 ms                                                          | 250 ms: 1.23x faster                                                               |
| async_tree_io_tg           | 677 ms                                                          | 552 ms: 1.23x faster                                                               |
| pprint_pformat             | 1.50 sec                                                        | 1.23 sec: 1.22x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 465 ms: 1.21x faster                                                               |
| pprint_safe_repr           | 721 ms                                                          | 602 ms: 1.20x faster                                                               |
| coroutines                 | 20.9 ms                                                         | 17.5 ms: 1.19x faster                                                              |
| xml_etree_generate         | 72.1 ms                                                         | 60.5 ms: 1.19x faster                                                              |
| regex_compile              | 129 ms                                                          | 108 ms: 1.19x faster                                                               |
| pycparser                  | 978 ms                                                          | 823 ms: 1.19x faster                                                               |
| sqlglot_parse              | 1.25 ms                                                         | 1.06 ms: 1.18x faster                                                              |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 462 ms: 1.18x faster                                                               |
| chaos                      | 69.4 ms                                                         | 59.1 ms: 1.17x faster                                                              |
| pickle_pure_python         | 286 us                                                          | 244 us: 1.17x faster                                                               |
| richards                   | 41.3 ms                                                         | 35.4 ms: 1.17x faster                                                              |
| nqueens                    | 93.7 ms                                                         | 80.3 ms: 1.17x faster                                                              |
| xml_etree_iterparse        | 77.6 ms                                                         | 66.6 ms: 1.17x faster                                                              |
| dulwich_log                | 58.5 ms                                                         | 50.4 ms: 1.16x faster                                                              |
| richards_super             | 46.5 ms                                                         | 40.0 ms: 1.16x faster                                                              |
| hexiom                     | 6.82 ms                                                         | 5.90 ms: 1.16x faster                                                              |
| meteor_contest             | 86.9 ms                                                         | 75.3 ms: 1.15x faster                                                              |
| django_template            | 36.9 ms                                                         | 32.4 ms: 1.14x faster                                                              |
| regex_effbot               | 2.04 ms                                                         | 1.80 ms: 1.13x faster                                                              |
| xml_etree_process          | 53.2 ms                                                         | 47.2 ms: 1.13x faster                                                              |
| sqlglot_transpile          | 1.53 ms                                                         | 1.37 ms: 1.11x faster                                                              |
| bench_thread_pool          | 1.10 ms                                                         | 1.01 ms: 1.09x faster                                                              |
| mdp                        | 1.91 sec                                                        | 1.75 sec: 1.09x faster                                                             |
| regex_dna                  | 127 ms                                                          | 120 ms: 1.06x faster                                                               |
| 2to3                       | 280 ms                                                          | 267 ms: 1.05x faster                                                               |
| sympy_sum                  | 123 ms                                                          | 118 ms: 1.04x faster                                                               |
| pathlib                    | 91.4 ms                                                         | 87.9 ms: 1.04x faster                                                              |
| sympy_str                  | 240 ms                                                          | 232 ms: 1.03x faster                                                               |
| xml_etree_parse            | 113 ms                                                          | 112 ms: 1.01x faster                                                               |
| sympy_expand               | 398 ms                                                          | 400 ms: 1.00x slower                                                               |
| sqlglot_normalize          | 100 ms                                                          | 102 ms: 1.02x slower                                                               |
| async_generators           | 313 ms                                                          | 320 ms: 1.02x slower                                                               |
| json_loads                 | 20.4 us                                                         | 20.9 us: 1.03x slower                                                              |
| sympy_integrate            | 17.5 ms                                                         | 18.1 ms: 1.03x slower                                                              |
| docutils                   | 1.98 sec                                                        | 2.05 sec: 1.04x slower                                                             |
| pidigits                   | 199 ms                                                          | 207 ms: 1.04x slower                                                               |
| sqlglot_optimize           | 48.5 ms                                                         | 50.3 ms: 1.04x slower                                                              |
| tornado_http               | 105 ms                                                          | 110 ms: 1.05x slower                                                               |
| regex_v8                   | 15.0 ms                                                         | 15.9 ms: 1.05x slower                                                              |
| python_startup_no_site     | 19.1 ms                                                         | 20.2 ms: 1.06x slower                                                              |
| coverage                   | 48.4 ms                                                         | 52.0 ms: 1.07x slower                                                              |
| json_dumps                 | 7.40 ms                                                         | 8.11 ms: 1.10x slower                                                              |
| telco                      | 5.51 ms                                                         | 6.14 ms: 1.11x slower                                                              |
| typing_runtime_protocols   | 126 us                                                          | 142 us: 1.12x slower                                                               |
| json                       | 4.15 ms                                                         | 4.77 ms: 1.15x slower                                                              |
| python_startup             | 22.4 ms                                                         | 26.9 ms: 1.20x slower                                                              |
| bench_mp_pool              | 75.4 ms                                                         | 94.4 ms: 1.25x slower                                                              |
| gc_traversal               | 1.44 ms                                                         | 1.82 ms: 1.26x slower                                                              |
| create_gc_cycles           | 652 us                                                          | 1.19 ms: 1.83x slower                                                              |
| Geometric mean             | (ref)                                                           | 1.16x faster                                                                       |
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241025-3.14.0a1+-5791853-JIT/bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-5791853.json: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.166x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown