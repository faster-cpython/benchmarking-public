# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_no_externs
- machine: windows-x86
- commit hash: 9698931
- commit date: 2024-10-24
- overall geometric mean: 1.123x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 274 ms: 1.02x faster                                                               |
| docutils       | 1.98 sec                                                        | 2.10 sec: 1.06x slower                                                             |
| tornado_http   | 105 ms                                                          | 110 ms: 1.05x slower                                                               |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 264 ms: 1.33x faster                                                               |
| async_tree_none_tg         | 278 ms                                                          | 212 ms: 1.31x faster                                                               |
| async_tree_none            | 298 ms                                                          | 228 ms: 1.30x faster                                                               |
| async_tree_io              | 693 ms                                                          | 540 ms: 1.28x faster                                                               |
| async_tree_memoization     | 364 ms                                                          | 287 ms: 1.27x faster                                                               |
| async_tree_io_tg           | 677 ms                                                          | 559 ms: 1.21x faster                                                               |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 474 ms: 1.19x faster                                                               |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 471 ms: 1.16x faster                                                               |
| Geometric mean             | (ref)                                                           | 1.26x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 70.3 ms: 1.81x faster                                                              |
| float          | 76.7 ms                                                         | 52.2 ms: 1.47x faster                                                              |
| pidigits       | 199 ms                                                          | 207 ms: 1.04x slower                                                               |
| Geometric mean | (ref)                                                           | 1.37x faster                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.79 ms: 1.14x faster                                                              |
| regex_compile  | 129 ms                                                          | 113 ms: 1.14x faster                                                               |
| regex_dna      | 127 ms                                                          | 119 ms: 1.07x faster                                                               |
| regex_v8       | 15.0 ms                                                         | 15.7 ms: 1.04x slower                                                              |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.64 sec: 1.34x faster                                                             |
| unpickle_pure_python | 210 us                                                          | 173 us: 1.21x faster                                                               |
| xml_etree_iterparse  | 77.6 ms                                                         | 68.2 ms: 1.14x faster                                                              |
| xml_etree_generate   | 72.1 ms                                                         | 63.8 ms: 1.13x faster                                                              |
| xml_etree_process    | 53.2 ms                                                         | 47.7 ms: 1.12x faster                                                              |
| pickle_pure_python   | 286 us                                                          | 258 us: 1.11x faster                                                               |
| json_loads           | 20.4 us                                                         | 21.7 us: 1.06x slower                                                              |
| json_dumps           | 7.40 ms                                                         | 8.50 ms: 1.15x slower                                                              |
| Geometric mean       | (ref)                                                           | 1.09x faster                                                                       |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.1 ms: 1.06x slower                                                              |
| python_startup         | 22.4 ms                                                         | 26.4 ms: 1.18x slower                                                              |
| Geometric mean         | (ref)                                                           | 1.12x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|-----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 6.83 ms: 1.46x faster                                                              |
| django_template | 36.9 ms                                                         | 34.7 ms: 1.06x faster                                                              |
| Geometric mean  | (ref)                                                           | 1.25x faster                                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 19.6 us: 1.96x faster                                                              |
| nbody                      | 127 ms                                                          | 70.3 ms: 1.81x faster                                                              |
| scimark_sor                | 130 ms                                                          | 83.3 ms: 1.56x faster                                                              |
| deepcopy                   | 360 us                                                          | 244 us: 1.48x faster                                                               |
| float                      | 76.7 ms                                                         | 52.2 ms: 1.47x faster                                                              |
| mako                       | 9.96 ms                                                         | 6.83 ms: 1.46x faster                                                              |
| spectral_norm              | 104 ms                                                          | 72.5 ms: 1.43x faster                                                              |
| scimark_lu                 | 93.2 ms                                                         | 65.7 ms: 1.42x faster                                                              |
| generators                 | 38.5 ms                                                         | 28.1 ms: 1.37x faster                                                              |
| tomli_loads                | 2.20 sec                                                        | 1.64 sec: 1.34x faster                                                             |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.89 ms: 1.34x faster                                                              |
| async_tree_memoization_tg  | 350 ms                                                          | 264 ms: 1.33x faster                                                               |
| logging_silent             | 101 ns                                                          | 76.8 ns: 1.32x faster                                                              |
| async_tree_none_tg         | 278 ms                                                          | 212 ms: 1.31x faster                                                               |
| async_tree_none            | 298 ms                                                          | 228 ms: 1.30x faster                                                               |
| scimark_monte_carlo        | 66.4 ms                                                         | 51.0 ms: 1.30x faster                                                              |
| scimark_fft                | 271 ms                                                          | 210 ms: 1.29x faster                                                               |
| async_tree_io              | 693 ms                                                          | 540 ms: 1.28x faster                                                               |
| deepcopy_reduce            | 3.23 us                                                         | 2.52 us: 1.28x faster                                                              |
| async_tree_memoization     | 364 ms                                                          | 287 ms: 1.27x faster                                                               |
| go                         | 137 ms                                                          | 109 ms: 1.26x faster                                                               |
| comprehensions             | 19.2 us                                                         | 15.3 us: 1.26x faster                                                              |
| deltablue                  | 3.58 ms                                                         | 2.91 ms: 1.23x faster                                                              |
| logging_simple             | 9.75 us                                                         | 7.96 us: 1.23x faster                                                              |
| logging_format             | 10.4 us                                                         | 8.57 us: 1.21x faster                                                              |
| fannkuch                   | 354 ms                                                          | 291 ms: 1.21x faster                                                               |
| async_tree_io_tg           | 677 ms                                                          | 559 ms: 1.21x faster                                                               |
| unpickle_pure_python       | 210 us                                                          | 173 us: 1.21x faster                                                               |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 474 ms: 1.19x faster                                                               |
| pyflate                    | 424 ms                                                          | 358 ms: 1.18x faster                                                               |
| chaos                      | 69.4 ms                                                         | 58.7 ms: 1.18x faster                                                              |
| dulwich_log                | 58.5 ms                                                         | 50.1 ms: 1.17x faster                                                              |
| coroutines                 | 20.9 ms                                                         | 17.9 ms: 1.17x faster                                                              |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 471 ms: 1.16x faster                                                               |
| crypto_pyaes               | 69.2 ms                                                         | 59.7 ms: 1.16x faster                                                              |
| regex_effbot               | 2.04 ms                                                         | 1.79 ms: 1.14x faster                                                              |
| regex_compile              | 129 ms                                                          | 113 ms: 1.14x faster                                                               |
| xml_etree_iterparse        | 77.6 ms                                                         | 68.2 ms: 1.14x faster                                                              |
| sqlglot_parse              | 1.25 ms                                                         | 1.10 ms: 1.14x faster                                                              |
| pycparser                  | 978 ms                                                          | 862 ms: 1.13x faster                                                               |
| nqueens                    | 93.7 ms                                                         | 82.6 ms: 1.13x faster                                                              |
| pprint_pformat             | 1.50 sec                                                        | 1.33 sec: 1.13x faster                                                             |
| xml_etree_generate         | 72.1 ms                                                         | 63.8 ms: 1.13x faster                                                              |
| pprint_safe_repr           | 721 ms                                                          | 642 ms: 1.12x faster                                                               |
| xml_etree_process          | 53.2 ms                                                         | 47.7 ms: 1.12x faster                                                              |
| raytrace                   | 308 ms                                                          | 277 ms: 1.11x faster                                                               |
| pickle_pure_python         | 286 us                                                          | 258 us: 1.11x faster                                                               |
| sqlglot_transpile          | 1.53 ms                                                         | 1.42 ms: 1.08x faster                                                              |
| bench_thread_pool          | 1.10 ms                                                         | 1.03 ms: 1.07x faster                                                              |
| mdp                        | 1.91 sec                                                        | 1.79 sec: 1.07x faster                                                             |
| regex_dna                  | 127 ms                                                          | 119 ms: 1.07x faster                                                               |
| meteor_contest             | 86.9 ms                                                         | 81.3 ms: 1.07x faster                                                              |
| hexiom                     | 6.82 ms                                                         | 6.40 ms: 1.07x faster                                                              |
| django_template            | 36.9 ms                                                         | 34.7 ms: 1.06x faster                                                              |
| richards                   | 41.3 ms                                                         | 39.5 ms: 1.05x faster                                                              |
| richards_super             | 46.5 ms                                                         | 44.6 ms: 1.04x faster                                                              |
| pathlib                    | 91.4 ms                                                         | 88.3 ms: 1.04x faster                                                              |
| 2to3                       | 280 ms                                                          | 274 ms: 1.02x faster                                                               |
| sympy_sum                  | 123 ms                                                          | 122 ms: 1.01x faster                                                               |
| sqlglot_normalize          | 100 ms                                                          | 102 ms: 1.02x slower                                                               |
| sympy_expand               | 398 ms                                                          | 410 ms: 1.03x slower                                                               |
| pidigits                   | 199 ms                                                          | 207 ms: 1.04x slower                                                               |
| async_generators           | 313 ms                                                          | 326 ms: 1.04x slower                                                               |
| sympy_integrate            | 17.5 ms                                                         | 18.3 ms: 1.04x slower                                                              |
| sqlglot_optimize           | 48.5 ms                                                         | 50.6 ms: 1.04x slower                                                              |
| regex_v8                   | 15.0 ms                                                         | 15.7 ms: 1.04x slower                                                              |
| tornado_http               | 105 ms                                                          | 110 ms: 1.05x slower                                                               |
| python_startup_no_site     | 19.1 ms                                                         | 20.1 ms: 1.06x slower                                                              |
| docutils                   | 1.98 sec                                                        | 2.10 sec: 1.06x slower                                                             |
| json_loads                 | 20.4 us                                                         | 21.7 us: 1.06x slower                                                              |
| coverage                   | 48.4 ms                                                         | 54.3 ms: 1.12x slower                                                              |
| telco                      | 5.51 ms                                                         | 6.32 ms: 1.15x slower                                                              |
| json_dumps                 | 7.40 ms                                                         | 8.50 ms: 1.15x slower                                                              |
| python_startup             | 22.4 ms                                                         | 26.4 ms: 1.18x slower                                                              |
| typing_runtime_protocols   | 126 us                                                          | 152 us: 1.21x slower                                                               |
| json                       | 4.15 ms                                                         | 5.19 ms: 1.25x slower                                                              |
| gc_traversal               | 1.44 ms                                                         | 1.81 ms: 1.25x slower                                                              |
| bench_mp_pool              | 75.4 ms                                                         | 94.6 ms: 1.25x slower                                                              |
| create_gc_cycles           | 652 us                                                          | 1.19 ms: 1.83x slower                                                              |
| Geometric mean             | (ref)                                                           | 1.12x faster                                                                       |

Benchmark hidden because not significant (2): sympy_str, xml_etree_parse
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241024-3.14.0a1+-9698931-JIT/bm-20241024-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-9698931.json: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.123x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: unknown