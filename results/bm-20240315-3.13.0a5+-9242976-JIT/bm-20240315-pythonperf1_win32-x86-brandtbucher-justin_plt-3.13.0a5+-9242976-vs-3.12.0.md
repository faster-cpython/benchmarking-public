# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_plt
- machine: windows-x86
- commit hash: 9242976
- commit date: 2024-03-15
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240315-pythonperf1_win32-x86-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 262 ms: 1.07x faster                                                        |
| chameleon      | 7.75 ms                                                         | 5.91 ms: 1.31x faster                                                       |
| docutils       | 1.98 sec                                                        | 1.87 sec: 1.06x faster                                                      |
| tornado_http   | 105 ms                                                          | 98.4 ms: 1.07x faster                                                       |
| Geometric mean | (ref)                                                           | 1.12x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240315-pythonperf1_win32-x86-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 307 ms: 1.14x faster                                                        |
| async_tree_none            | 298 ms                                                          | 261 ms: 1.14x faster                                                        |
| async_tree_memoization     | 364 ms                                                          | 320 ms: 1.14x faster                                                        |
| async_tree_none_tg         | 278 ms                                                          | 245 ms: 1.13x faster                                                        |
| async_tree_io_tg           | 677 ms                                                          | 608 ms: 1.11x faster                                                        |
| async_tree_io              | 693 ms                                                          | 623 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 510 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 498 ms: 1.10x faster                                                        |
| Geometric mean             | (ref)                                                           | 1.12x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240315-pythonperf1_win32-x86-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 54.7 ms: 1.40x faster                                                       |
| nbody          | 127 ms                                                          | 98.8 ms: 1.29x faster                                                       |
| pidigits       | 199 ms                                                          | 199 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                           | 1.22x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240315-pythonperf1_win32-x86-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 112 ms: 1.16x faster                                                        |
| regex_effbot   | 2.04 ms                                                         | 1.89 ms: 1.08x faster                                                       |
| regex_dna      | 127 ms                                                          | 122 ms: 1.04x faster                                                        |
| regex_v8       | 15.0 ms                                                         | 16.2 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240315-pythonperf1_win32-x86-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.71 sec: 1.29x faster                                                      |
| pickle_pure_python   | 286 us                                                          | 224 us: 1.28x faster                                                        |
| unpickle_pure_python | 210 us                                                          | 174 us: 1.21x faster                                                        |
| xml_etree_process    | 53.2 ms                                                         | 45.2 ms: 1.18x faster                                                       |
| xml_etree_iterparse  | 77.6 ms                                                         | 67.0 ms: 1.16x faster                                                       |
| xml_etree_generate   | 72.1 ms                                                         | 64.0 ms: 1.13x faster                                                       |
| json_dumps           | 7.40 ms                                                         | 6.98 ms: 1.06x faster                                                       |
| pickle_list          | 3.37 us                                                         | 3.19 us: 1.06x faster                                                       |
| xml_etree_parse      | 113 ms                                                          | 107 ms: 1.05x faster                                                        |
| unpickle_list        | 2.95 us                                                         | 2.88 us: 1.02x faster                                                       |
| json_loads           | 20.4 us                                                         | 20.1 us: 1.01x faster                                                       |
| pickle               | 7.79 us                                                         | 8.02 us: 1.03x slower                                                       |
| unpickle             | 9.71 us                                                         | 10.2 us: 1.05x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.09x faster                                                                |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240315-pythonperf1_win32-x86-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 22.4 ms                                                         | 25.8 ms: 1.15x slower                                                       |
| python_startup_no_site | 19.1 ms                                                         | 23.6 ms: 1.24x slower                                                       |
| Geometric mean         | (ref)                                                           | 1.20x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240315-pythonperf1_win32-x86-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 6.88 ms: 1.45x faster                                                       |
| django_template | 36.9 ms                                                         | 31.7 ms: 1.17x faster                                                       |
| Geometric mean  | (ref)                                                           | 1.30x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240315-pythonperf1_win32-x86-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| generators                 | 38.5 ms                                                         | 24.3 ms: 1.58x faster                                                       |
| logging_silent             | 101 ns                                                          | 67.8 ns: 1.49x faster                                                       |
| mako                       | 9.96 ms                                                         | 6.88 ms: 1.45x faster                                                       |
| unpack_sequence            | 62.5 ns                                                         | 44.0 ns: 1.42x faster                                                       |
| spectral_norm              | 104 ms                                                          | 73.2 ms: 1.42x faster                                                       |
| deepcopy_memo              | 38.4 us                                                         | 27.1 us: 1.42x faster                                                       |
| float                      | 76.7 ms                                                         | 54.7 ms: 1.40x faster                                                       |
| coroutines                 | 20.9 ms                                                         | 15.0 ms: 1.39x faster                                                       |
| deltablue                  | 3.58 ms                                                         | 2.69 ms: 1.33x faster                                                       |
| chameleon                  | 7.75 ms                                                         | 5.91 ms: 1.31x faster                                                       |
| comprehensions             | 19.2 us                                                         | 14.9 us: 1.29x faster                                                       |
| tomli_loads                | 2.20 sec                                                        | 1.71 sec: 1.29x faster                                                      |
| nbody                      | 127 ms                                                          | 98.8 ms: 1.29x faster                                                       |
| pickle_pure_python         | 286 us                                                          | 224 us: 1.28x faster                                                        |
| typing_runtime_protocols   | 126 us                                                          | 99.4 us: 1.27x faster                                                       |
| deepcopy_reduce            | 3.23 us                                                         | 2.60 us: 1.24x faster                                                       |
| sqlglot_parse              | 1.25 ms                                                         | 1.01 ms: 1.24x faster                                                       |
| deepcopy                   | 360 us                                                          | 291 us: 1.24x faster                                                        |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.11 ms: 1.24x faster                                                       |
| scimark_sor                | 130 ms                                                          | 106 ms: 1.23x faster                                                        |
| sqlglot_transpile          | 1.53 ms                                                         | 1.27 ms: 1.21x faster                                                       |
| unpickle_pure_python       | 210 us                                                          | 174 us: 1.21x faster                                                        |
| xml_etree_process          | 53.2 ms                                                         | 45.2 ms: 1.18x faster                                                       |
| logging_simple             | 9.75 us                                                         | 8.31 us: 1.17x faster                                                       |
| chaos                      | 69.4 ms                                                         | 59.1 ms: 1.17x faster                                                       |
| django_template            | 36.9 ms                                                         | 31.7 ms: 1.17x faster                                                       |
| logging_format             | 10.4 us                                                         | 8.96 us: 1.16x faster                                                       |
| xml_etree_iterparse        | 77.6 ms                                                         | 67.0 ms: 1.16x faster                                                       |
| regex_compile              | 129 ms                                                          | 112 ms: 1.16x faster                                                        |
| richards                   | 41.3 ms                                                         | 36.0 ms: 1.15x faster                                                       |
| crypto_pyaes               | 69.2 ms                                                         | 60.2 ms: 1.15x faster                                                       |
| raytrace                   | 308 ms                                                          | 269 ms: 1.15x faster                                                        |
| async_tree_memoization_tg  | 350 ms                                                          | 307 ms: 1.14x faster                                                        |
| async_tree_none            | 298 ms                                                          | 261 ms: 1.14x faster                                                        |
| scimark_fft                | 271 ms                                                          | 237 ms: 1.14x faster                                                        |
| richards_super             | 46.5 ms                                                         | 40.8 ms: 1.14x faster                                                       |
| async_tree_memoization     | 364 ms                                                          | 320 ms: 1.14x faster                                                        |
| async_tree_none_tg         | 278 ms                                                          | 245 ms: 1.13x faster                                                        |
| xml_etree_generate         | 72.1 ms                                                         | 64.0 ms: 1.13x faster                                                       |
| pyflate                    | 424 ms                                                          | 377 ms: 1.13x faster                                                        |
| async_tree_io_tg           | 677 ms                                                          | 608 ms: 1.11x faster                                                        |
| hexiom                     | 6.82 ms                                                         | 6.12 ms: 1.11x faster                                                       |
| pycparser                  | 978 ms                                                          | 878 ms: 1.11x faster                                                        |
| async_tree_io              | 693 ms                                                          | 623 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 510 ms: 1.10x faster                                                        |
| sympy_integrate            | 17.5 ms                                                         | 16.0 ms: 1.10x faster                                                       |
| go                         | 137 ms                                                          | 125 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 498 ms: 1.10x faster                                                        |
| sqlite_synth               | 2.07 us                                                         | 1.89 us: 1.09x faster                                                       |
| sympy_sum                  | 123 ms                                                          | 112 ms: 1.09x faster                                                        |
| sympy_str                  | 240 ms                                                          | 220 ms: 1.09x faster                                                        |
| mdp                        | 1.91 sec                                                        | 1.76 sec: 1.08x faster                                                      |
| regex_effbot               | 2.04 ms                                                         | 1.89 ms: 1.08x faster                                                       |
| async_generators           | 313 ms                                                          | 292 ms: 1.07x faster                                                        |
| 2to3                       | 280 ms                                                          | 262 ms: 1.07x faster                                                        |
| tornado_http               | 105 ms                                                          | 98.4 ms: 1.07x faster                                                       |
| pathlib                    | 91.4 ms                                                         | 86.1 ms: 1.06x faster                                                       |
| bench_thread_pool          | 1.10 ms                                                         | 1.04 ms: 1.06x faster                                                       |
| docutils                   | 1.98 sec                                                        | 1.87 sec: 1.06x faster                                                      |
| json_dumps                 | 7.40 ms                                                         | 6.98 ms: 1.06x faster                                                       |
| pickle_list                | 3.37 us                                                         | 3.19 us: 1.06x faster                                                       |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.7 sec: 1.06x faster                                                      |
| xml_etree_parse            | 113 ms                                                          | 107 ms: 1.05x faster                                                        |
| scimark_lu                 | 93.2 ms                                                         | 88.9 ms: 1.05x faster                                                       |
| meteor_contest             | 86.9 ms                                                         | 82.9 ms: 1.05x faster                                                       |
| fannkuch                   | 354 ms                                                          | 338 ms: 1.05x faster                                                        |
| regex_dna                  | 127 ms                                                          | 122 ms: 1.04x faster                                                        |
| scimark_monte_carlo        | 66.4 ms                                                         | 64.0 ms: 1.04x faster                                                       |
| sympy_expand               | 398 ms                                                          | 388 ms: 1.02x faster                                                        |
| unpickle_list              | 2.95 us                                                         | 2.88 us: 1.02x faster                                                       |
| gc_traversal               | 1.44 ms                                                         | 1.42 ms: 1.02x faster                                                       |
| json_loads                 | 20.4 us                                                         | 20.1 us: 1.01x faster                                                       |
| sqlglot_optimize           | 48.5 ms                                                         | 48.0 ms: 1.01x faster                                                       |
| bench_mp_pool              | 75.4 ms                                                         | 74.7 ms: 1.01x faster                                                       |
| pidigits                   | 199 ms                                                          | 199 ms: 1.00x faster                                                        |
| pprint_pformat             | 1.50 sec                                                        | 1.52 sec: 1.01x slower                                                      |
| json                       | 4.15 ms                                                         | 4.21 ms: 1.01x slower                                                       |
| create_gc_cycles           | 652 us                                                          | 661 us: 1.01x slower                                                        |
| nqueens                    | 93.7 ms                                                         | 95.0 ms: 1.01x slower                                                       |
| pickle                     | 7.79 us                                                         | 8.02 us: 1.03x slower                                                       |
| pprint_safe_repr           | 721 ms                                                          | 746 ms: 1.03x slower                                                        |
| unpickle                   | 9.71 us                                                         | 10.2 us: 1.05x slower                                                       |
| regex_v8                   | 15.0 ms                                                         | 16.2 ms: 1.07x slower                                                       |
| python_startup             | 22.4 ms                                                         | 25.8 ms: 1.15x slower                                                       |
| telco                      | 5.51 ms                                                         | 6.62 ms: 1.20x slower                                                       |
| python_startup_no_site     | 19.1 ms                                                         | 23.6 ms: 1.24x slower                                                       |
| sqlglot_normalize          | 100 ms                                                          | 241 ms: 2.40x slower                                                        |
| coverage                   | 48.4 ms                                                         | 489 ms: 10.09x slower                                                       |
| Geometric mean             | (ref)                                                           | 1.08x faster                                                                |

Benchmark hidden because not significant (2): asyncio_tcp, pickle_dict
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240315-3.13.0a5+-9242976-JIT/bm-20240315-pythonperf1_win32-x86-brandtbucher-justin_plt-3.13.0a5+-9242976.json: genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x


# Memory

- memory change: unknown