# Results vs. 3.12.0

- fork: brandtbucher
- ref: faster_jit_builds
- machine: windows-x86
- commit hash: 60b7e71
- commit date: 2024-07-27
- overall geometric mean: 1.22x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 258 ms: 1.08x faster                                                              |
| docutils       | 1.98 sec                                                        | 1.95 sec: 1.02x faster                                                            |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                      |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_none_tg         | 278 ms                                                          | 194 ms: 1.43x faster                                                              |
| async_tree_memoization_tg  | 350 ms                                                          | 246 ms: 1.43x faster                                                              |
| async_tree_none            | 298 ms                                                          | 219 ms: 1.36x faster                                                              |
| async_tree_memoization     | 364 ms                                                          | 271 ms: 1.34x faster                                                              |
| async_tree_io_tg           | 677 ms                                                          | 509 ms: 1.33x faster                                                              |
| async_tree_io              | 693 ms                                                          | 544 ms: 1.27x faster                                                              |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 471 ms: 1.20x faster                                                              |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 463 ms: 1.18x faster                                                              |
| Geometric mean             | (ref)                                                           | 1.31x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 53.1 ms: 2.39x faster                                                             |
| float          | 76.7 ms                                                         | 42.9 ms: 1.79x faster                                                             |
| pidigits       | 199 ms                                                          | 196 ms: 1.02x faster                                                              |
| Geometric mean | (ref)                                                           | 1.63x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 95.3 ms: 1.35x faster                                                             |
| regex_dna      | 127 ms                                                          | 116 ms: 1.09x faster                                                              |
| regex_v8       | 15.0 ms                                                         | 15.9 ms: 1.05x slower                                                             |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                      |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.46 sec: 1.50x faster                                                            |
| unpickle_pure_python | 210 us                                                          | 149 us: 1.41x faster                                                              |
| pickle_pure_python   | 286 us                                                          | 217 us: 1.32x faster                                                              |
| xml_etree_iterparse  | 77.6 ms                                                         | 64.1 ms: 1.21x faster                                                             |
| xml_etree_generate   | 72.1 ms                                                         | 59.6 ms: 1.21x faster                                                             |
| xml_etree_process    | 53.2 ms                                                         | 44.7 ms: 1.19x faster                                                             |
| json_dumps           | 7.40 ms                                                         | 7.00 ms: 1.06x faster                                                             |
| xml_etree_parse      | 113 ms                                                          | 108 ms: 1.05x faster                                                              |
| json_loads           | 20.4 us                                                         | 21.2 us: 1.04x slower                                                             |
| Geometric mean       | (ref)                                                           | 1.20x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.1 ms: 1.06x slower                                                             |
| python_startup         | 22.4 ms                                                         | 23.9 ms: 1.07x slower                                                             |
| Geometric mean         | (ref)                                                           | 1.06x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.41 ms: 1.84x faster                                                             |
| django_template | 36.9 ms                                                         | 32.2 ms: 1.14x faster                                                             |
| Geometric mean  | (ref)                                                           | 1.45x faster                                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 15.7 us: 2.44x faster                                                             |
| nbody                      | 127 ms                                                          | 53.1 ms: 2.39x faster                                                             |
| spectral_norm              | 104 ms                                                          | 47.3 ms: 2.19x faster                                                             |
| mako                       | 9.96 ms                                                         | 5.41 ms: 1.84x faster                                                             |
| float                      | 76.7 ms                                                         | 42.9 ms: 1.79x faster                                                             |
| logging_silent             | 101 ns                                                          | 59.0 ns: 1.71x faster                                                             |
| comprehensions             | 19.2 us                                                         | 11.4 us: 1.68x faster                                                             |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.37 ms: 1.63x faster                                                             |
| scimark_fft                | 271 ms                                                          | 167 ms: 1.62x faster                                                              |
| pyflate                    | 424 ms                                                          | 264 ms: 1.60x faster                                                              |
| deepcopy                   | 360 us                                                          | 237 us: 1.52x faster                                                              |
| scimark_monte_carlo        | 66.4 ms                                                         | 44.0 ms: 1.51x faster                                                             |
| tomli_loads                | 2.20 sec                                                        | 1.46 sec: 1.50x faster                                                            |
| fannkuch                   | 354 ms                                                          | 238 ms: 1.48x faster                                                              |
| hexiom                     | 6.82 ms                                                         | 4.62 ms: 1.48x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 194 ms: 1.43x faster                                                              |
| async_tree_memoization_tg  | 350 ms                                                          | 246 ms: 1.43x faster                                                              |
| crypto_pyaes               | 69.2 ms                                                         | 48.7 ms: 1.42x faster                                                             |
| unpickle_pure_python       | 210 us                                                          | 149 us: 1.41x faster                                                              |
| generators                 | 38.5 ms                                                         | 28.2 ms: 1.36x faster                                                             |
| raytrace                   | 308 ms                                                          | 226 ms: 1.36x faster                                                              |
| async_tree_none            | 298 ms                                                          | 219 ms: 1.36x faster                                                              |
| regex_compile              | 129 ms                                                          | 95.3 ms: 1.35x faster                                                             |
| chaos                      | 69.4 ms                                                         | 51.6 ms: 1.35x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 271 ms: 1.34x faster                                                              |
| sqlglot_parse              | 1.25 ms                                                         | 936 us: 1.33x faster                                                              |
| async_tree_io_tg           | 677 ms                                                          | 509 ms: 1.33x faster                                                              |
| deepcopy_reduce            | 3.23 us                                                         | 2.42 us: 1.33x faster                                                             |
| deltablue                  | 3.58 ms                                                         | 2.71 ms: 1.32x faster                                                             |
| pickle_pure_python         | 286 us                                                          | 217 us: 1.32x faster                                                              |
| logging_simple             | 9.75 us                                                         | 7.47 us: 1.31x faster                                                             |
| logging_format             | 10.4 us                                                         | 8.13 us: 1.28x faster                                                             |
| async_tree_io              | 693 ms                                                          | 544 ms: 1.27x faster                                                              |
| sqlglot_transpile          | 1.53 ms                                                         | 1.21 ms: 1.27x faster                                                             |
| nqueens                    | 93.7 ms                                                         | 74.3 ms: 1.26x faster                                                             |
| pprint_pformat             | 1.50 sec                                                        | 1.20 sec: 1.25x faster                                                            |
| pprint_safe_repr           | 721 ms                                                          | 582 ms: 1.24x faster                                                              |
| pycparser                  | 978 ms                                                          | 796 ms: 1.23x faster                                                              |
| meteor_contest             | 86.9 ms                                                         | 70.8 ms: 1.23x faster                                                             |
| richards                   | 41.3 ms                                                         | 33.8 ms: 1.22x faster                                                             |
| scimark_sor                | 130 ms                                                          | 107 ms: 1.22x faster                                                              |
| xml_etree_iterparse        | 77.6 ms                                                         | 64.1 ms: 1.21x faster                                                             |
| xml_etree_generate         | 72.1 ms                                                         | 59.6 ms: 1.21x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 471 ms: 1.20x faster                                                              |
| xml_etree_process          | 53.2 ms                                                         | 44.7 ms: 1.19x faster                                                             |
| go                         | 137 ms                                                          | 115 ms: 1.19x faster                                                              |
| scimark_lu                 | 93.2 ms                                                         | 78.9 ms: 1.18x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 463 ms: 1.18x faster                                                              |
| richards_super             | 46.5 ms                                                         | 39.5 ms: 1.18x faster                                                             |
| dulwich_log                | 58.5 ms                                                         | 49.8 ms: 1.17x faster                                                             |
| coroutines                 | 20.9 ms                                                         | 18.0 ms: 1.16x faster                                                             |
| mdp                        | 1.91 sec                                                        | 1.66 sec: 1.15x faster                                                            |
| django_template            | 36.9 ms                                                         | 32.2 ms: 1.14x faster                                                             |
| sympy_sum                  | 123 ms                                                          | 108 ms: 1.14x faster                                                              |
| sympy_str                  | 240 ms                                                          | 215 ms: 1.11x faster                                                              |
| sqlglot_optimize           | 48.5 ms                                                         | 43.6 ms: 1.11x faster                                                             |
| regex_dna                  | 127 ms                                                          | 116 ms: 1.09x faster                                                              |
| sympy_integrate            | 17.5 ms                                                         | 16.1 ms: 1.09x faster                                                             |
| 2to3                       | 280 ms                                                          | 258 ms: 1.08x faster                                                              |
| bench_thread_pool          | 1.10 ms                                                         | 1.03 ms: 1.07x faster                                                             |
| json_dumps                 | 7.40 ms                                                         | 7.00 ms: 1.06x faster                                                             |
| sympy_expand               | 398 ms                                                          | 380 ms: 1.05x faster                                                              |
| xml_etree_parse            | 113 ms                                                          | 108 ms: 1.05x faster                                                              |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.9 sec: 1.04x faster                                                            |
| pathlib                    | 91.4 ms                                                         | 88.8 ms: 1.03x faster                                                             |
| docutils                   | 1.98 sec                                                        | 1.95 sec: 1.02x faster                                                            |
| pidigits                   | 199 ms                                                          | 196 ms: 1.02x faster                                                              |
| async_generators           | 313 ms                                                          | 310 ms: 1.01x faster                                                              |
| gc_traversal               | 1.44 ms                                                         | 1.45 ms: 1.01x slower                                                             |
| bench_mp_pool              | 75.4 ms                                                         | 77.4 ms: 1.03x slower                                                             |
| json                       | 4.15 ms                                                         | 4.31 ms: 1.04x slower                                                             |
| json_loads                 | 20.4 us                                                         | 21.2 us: 1.04x slower                                                             |
| telco                      | 5.51 ms                                                         | 5.77 ms: 1.05x slower                                                             |
| regex_v8                   | 15.0 ms                                                         | 15.9 ms: 1.05x slower                                                             |
| python_startup_no_site     | 19.1 ms                                                         | 20.1 ms: 1.06x slower                                                             |
| python_startup             | 22.4 ms                                                         | 23.9 ms: 1.07x slower                                                             |
| coverage                   | 48.4 ms                                                         | 52.8 ms: 1.09x slower                                                             |
| typing_runtime_protocols   | 126 us                                                          | 146 us: 1.16x slower                                                              |
| create_gc_cycles           | 652 us                                                          | 769 us: 1.18x slower                                                              |
| sqlglot_normalize          | 100 ms                                                          | 236 ms: 2.35x slower                                                              |
| Geometric mean             | (ref)                                                           | 1.22x faster                                                                      |

Benchmark hidden because not significant (3): regex_effbot, tornado_http, asyncio_tcp
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240727-3.14.0a0-60b7e71-JIT/bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: unknown