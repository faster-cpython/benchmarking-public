# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_no_externs
- machine: windows-x86
- commit hash: 64b198a
- commit date: 2024-10-25
- overall geometric mean: 1.168x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 270 ms: 1.04x faster                                                               |
| docutils       | 1.98 sec                                                        | 2.08 sec: 1.05x slower                                                             |
| tornado_http   | 105 ms                                                          | 109 ms: 1.03x slower                                                               |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 252 ms: 1.39x faster                                                               |
| async_tree_none_tg         | 278 ms                                                          | 203 ms: 1.37x faster                                                               |
| async_tree_none            | 298 ms                                                          | 223 ms: 1.33x faster                                                               |
| async_tree_io              | 693 ms                                                          | 525 ms: 1.32x faster                                                               |
| async_tree_memoization     | 364 ms                                                          | 281 ms: 1.29x faster                                                               |
| async_tree_io_tg           | 677 ms                                                          | 551 ms: 1.23x faster                                                               |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 470 ms: 1.20x faster                                                               |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 465 ms: 1.17x faster                                                               |
| Geometric mean             | (ref)                                                           | 1.29x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 63.0 ms: 2.01x faster                                                              |
| float          | 76.7 ms                                                         | 49.6 ms: 1.55x faster                                                              |
| pidigits       | 199 ms                                                          | 203 ms: 1.02x slower                                                               |
| Geometric mean | (ref)                                                           | 1.45x faster                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 110 ms: 1.17x faster                                                               |
| regex_effbot   | 2.04 ms                                                         | 1.77 ms: 1.15x faster                                                              |
| regex_dna      | 127 ms                                                          | 120 ms: 1.06x faster                                                               |
| regex_v8       | 15.0 ms                                                         | 15.9 ms: 1.06x slower                                                              |
| Geometric mean | (ref)                                                           | 1.08x faster                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.59 sec: 1.38x faster                                                             |
| unpickle_pure_python | 210 us                                                          | 169 us: 1.24x faster                                                               |
| xml_etree_generate   | 72.1 ms                                                         | 58.2 ms: 1.24x faster                                                              |
| xml_etree_process    | 53.2 ms                                                         | 45.4 ms: 1.17x faster                                                              |
| pickle_pure_python   | 286 us                                                          | 245 us: 1.17x faster                                                               |
| xml_etree_iterparse  | 77.6 ms                                                         | 67.7 ms: 1.15x faster                                                              |
| xml_etree_parse      | 113 ms                                                          | 111 ms: 1.02x faster                                                               |
| json_loads           | 20.4 us                                                         | 21.2 us: 1.04x slower                                                              |
| json_dumps           | 7.40 ms                                                         | 7.99 ms: 1.08x slower                                                              |
| Geometric mean       | (ref)                                                           | 1.13x faster                                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.3 ms: 1.07x slower                                                              |
| python_startup         | 22.4 ms                                                         | 26.6 ms: 1.19x slower                                                              |
| Geometric mean         | (ref)                                                           | 1.13x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|-----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 6.44 ms: 1.55x faster                                                              |
| django_template | 36.9 ms                                                         | 33.0 ms: 1.12x faster                                                              |
| Geometric mean  | (ref)                                                           | 1.31x faster                                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 18.0 us: 2.13x faster                                                              |
| nbody                      | 127 ms                                                          | 63.0 ms: 2.01x faster                                                              |
| scimark_sor                | 130 ms                                                          | 76.9 ms: 1.69x faster                                                              |
| logging_silent             | 101 ns                                                          | 64.9 ns: 1.56x faster                                                              |
| float                      | 76.7 ms                                                         | 49.6 ms: 1.55x faster                                                              |
| mako                       | 9.96 ms                                                         | 6.44 ms: 1.55x faster                                                              |
| spectral_norm              | 104 ms                                                          | 67.5 ms: 1.54x faster                                                              |
| generators                 | 38.5 ms                                                         | 25.5 ms: 1.51x faster                                                              |
| deepcopy                   | 360 us                                                          | 245 us: 1.47x faster                                                               |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.65 ms: 1.46x faster                                                              |
| scimark_lu                 | 93.2 ms                                                         | 65.2 ms: 1.43x faster                                                              |
| async_tree_memoization_tg  | 350 ms                                                          | 252 ms: 1.39x faster                                                               |
| scimark_monte_carlo        | 66.4 ms                                                         | 47.7 ms: 1.39x faster                                                              |
| scimark_fft                | 271 ms                                                          | 195 ms: 1.39x faster                                                               |
| tomli_loads                | 2.20 sec                                                        | 1.59 sec: 1.38x faster                                                             |
| fannkuch                   | 354 ms                                                          | 256 ms: 1.38x faster                                                               |
| async_tree_none_tg         | 278 ms                                                          | 203 ms: 1.37x faster                                                               |
| go                         | 137 ms                                                          | 101 ms: 1.37x faster                                                               |
| comprehensions             | 19.2 us                                                         | 14.2 us: 1.36x faster                                                              |
| async_tree_none            | 298 ms                                                          | 223 ms: 1.33x faster                                                               |
| async_tree_io              | 693 ms                                                          | 525 ms: 1.32x faster                                                               |
| deltablue                  | 3.58 ms                                                         | 2.73 ms: 1.31x faster                                                              |
| async_tree_memoization     | 364 ms                                                          | 281 ms: 1.29x faster                                                               |
| pyflate                    | 424 ms                                                          | 330 ms: 1.28x faster                                                               |
| crypto_pyaes               | 69.2 ms                                                         | 54.0 ms: 1.28x faster                                                              |
| deepcopy_reduce            | 3.23 us                                                         | 2.53 us: 1.27x faster                                                              |
| logging_simple             | 9.75 us                                                         | 7.78 us: 1.25x faster                                                              |
| unpickle_pure_python       | 210 us                                                          | 169 us: 1.24x faster                                                               |
| chaos                      | 69.4 ms                                                         | 55.8 ms: 1.24x faster                                                              |
| xml_etree_generate         | 72.1 ms                                                         | 58.2 ms: 1.24x faster                                                              |
| logging_format             | 10.4 us                                                         | 8.45 us: 1.23x faster                                                              |
| async_tree_io_tg           | 677 ms                                                          | 551 ms: 1.23x faster                                                               |
| pprint_pformat             | 1.50 sec                                                        | 1.23 sec: 1.22x faster                                                             |
| coroutines                 | 20.9 ms                                                         | 17.3 ms: 1.21x faster                                                              |
| raytrace                   | 308 ms                                                          | 256 ms: 1.20x faster                                                               |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 470 ms: 1.20x faster                                                               |
| sqlglot_parse              | 1.25 ms                                                         | 1.04 ms: 1.20x faster                                                              |
| pprint_safe_repr           | 721 ms                                                          | 603 ms: 1.20x faster                                                               |
| meteor_contest             | 86.9 ms                                                         | 73.6 ms: 1.18x faster                                                              |
| regex_compile              | 129 ms                                                          | 110 ms: 1.17x faster                                                               |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 465 ms: 1.17x faster                                                               |
| xml_etree_process          | 53.2 ms                                                         | 45.4 ms: 1.17x faster                                                              |
| pickle_pure_python         | 286 us                                                          | 245 us: 1.17x faster                                                               |
| dulwich_log                | 58.5 ms                                                         | 50.2 ms: 1.17x faster                                                              |
| pycparser                  | 978 ms                                                          | 845 ms: 1.16x faster                                                               |
| richards                   | 41.3 ms                                                         | 35.9 ms: 1.15x faster                                                              |
| regex_effbot               | 2.04 ms                                                         | 1.77 ms: 1.15x faster                                                              |
| hexiom                     | 6.82 ms                                                         | 5.94 ms: 1.15x faster                                                              |
| xml_etree_iterparse        | 77.6 ms                                                         | 67.7 ms: 1.15x faster                                                              |
| richards_super             | 46.5 ms                                                         | 41.0 ms: 1.13x faster                                                              |
| sqlglot_transpile          | 1.53 ms                                                         | 1.36 ms: 1.13x faster                                                              |
| nqueens                    | 93.7 ms                                                         | 83.7 ms: 1.12x faster                                                              |
| django_template            | 36.9 ms                                                         | 33.0 ms: 1.12x faster                                                              |
| mdp                        | 1.91 sec                                                        | 1.76 sec: 1.09x faster                                                             |
| bench_thread_pool          | 1.10 ms                                                         | 1.02 ms: 1.08x faster                                                              |
| regex_dna                  | 127 ms                                                          | 120 ms: 1.06x faster                                                               |
| pathlib                    | 91.4 ms                                                         | 87.8 ms: 1.04x faster                                                              |
| 2to3                       | 280 ms                                                          | 270 ms: 1.04x faster                                                               |
| sympy_sum                  | 123 ms                                                          | 119 ms: 1.03x faster                                                               |
| xml_etree_parse            | 113 ms                                                          | 111 ms: 1.02x faster                                                               |
| sympy_str                  | 240 ms                                                          | 236 ms: 1.02x faster                                                               |
| pidigits                   | 199 ms                                                          | 203 ms: 1.02x slower                                                               |
| sympy_expand               | 398 ms                                                          | 406 ms: 1.02x slower                                                               |
| sympy_integrate            | 17.5 ms                                                         | 18.0 ms: 1.02x slower                                                              |
| tornado_http               | 105 ms                                                          | 109 ms: 1.03x slower                                                               |
| json_loads                 | 20.4 us                                                         | 21.2 us: 1.04x slower                                                              |
| docutils                   | 1.98 sec                                                        | 2.08 sec: 1.05x slower                                                             |
| sqlglot_optimize           | 48.5 ms                                                         | 50.8 ms: 1.05x slower                                                              |
| sqlglot_normalize          | 100 ms                                                          | 105 ms: 1.05x slower                                                               |
| async_generators           | 313 ms                                                          | 332 ms: 1.06x slower                                                               |
| regex_v8                   | 15.0 ms                                                         | 15.9 ms: 1.06x slower                                                              |
| python_startup_no_site     | 19.1 ms                                                         | 20.3 ms: 1.07x slower                                                              |
| json_dumps                 | 7.40 ms                                                         | 7.99 ms: 1.08x slower                                                              |
| telco                      | 5.51 ms                                                         | 6.01 ms: 1.09x slower                                                              |
| coverage                   | 48.4 ms                                                         | 53.8 ms: 1.11x slower                                                              |
| typing_runtime_protocols   | 126 us                                                          | 143 us: 1.13x slower                                                               |
| json                       | 4.15 ms                                                         | 4.93 ms: 1.19x slower                                                              |
| python_startup             | 22.4 ms                                                         | 26.6 ms: 1.19x slower                                                              |
| bench_mp_pool              | 75.4 ms                                                         | 94.4 ms: 1.25x slower                                                              |
| gc_traversal               | 1.44 ms                                                         | 1.81 ms: 1.26x slower                                                              |
| create_gc_cycles           | 652 us                                                          | 1.18 ms: 1.81x slower                                                              |
| Geometric mean             | (ref)                                                           | 1.16x faster                                                                       |
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241025-3.14.0a1+-64b198a-JIT/bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-64b198a.json: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.168x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown