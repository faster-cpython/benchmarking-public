# Results vs. 3.13.0b2

- fork: python
- ref: ad056f03aee8000a1564
- machine: windows-x86
- commit hash: ad056f0
- commit date: 2023-10-13
- overall geometric mean: 1.40x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 309 ms: 1.32x slower                                                           |
| chameleon      | 5.71 ms                                                             | 9.20 ms: 1.61x slower                                                          |
| docutils       | 1.81 sec                                                            | 2.17 sec: 1.20x slower                                                         |
| tornado_http   | 94.3 ms                                                             | 116 ms: 1.23x slower                                                           |
| Geometric mean | (ref)                                                               | 1.33x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 471 ms                                                              | 579 ms: 1.23x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 569 ms: 1.27x slower                                                           |
| async_tree_none            | 228 ms                                                              | 317 ms: 1.39x slower                                                           |
| async_tree_io_tg           | 529 ms                                                              | 743 ms: 1.40x slower                                                           |
| async_tree_io              | 530 ms                                                              | 757 ms: 1.43x slower                                                           |
| async_tree_memoization     | 275 ms                                                              | 396 ms: 1.44x slower                                                           |
| async_tree_none_tg         | 203 ms                                                              | 304 ms: 1.50x slower                                                           |
| async_tree_memoization_tg  | 254 ms                                                              | 386 ms: 1.52x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.39x slower                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 52.4 ms                                                             | 92.7 ms: 1.77x slower                                                          |
| nbody          | 76.9 ms                                                             | 167 ms: 2.18x slower                                                           |
| Geometric mean | (ref)                                                               | 1.57x slower                                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 118 ms                                                              | 119 ms: 1.01x slower                                                           |
| regex_effbot   | 1.88 ms                                                             | 1.93 ms: 1.03x slower                                                          |
| regex_v8       | 15.7 ms                                                             | 16.8 ms: 1.07x slower                                                          |
| regex_compile  | 99.9 ms                                                             | 159 ms: 1.60x slower                                                           |
| Geometric mean | (ref)                                                               | 1.15x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pickle_list          | 3.57 us                                                             | 3.28 us: 1.09x faster                                                          |
| pickle               | 8.07 us                                                             | 7.73 us: 1.04x faster                                                          |
| pickle_dict          | 20.8 us                                                             | 19.9 us: 1.04x faster                                                          |
| unpickle             | 9.79 us                                                             | 9.47 us: 1.03x faster                                                          |
| json_loads           | 20.5 us                                                             | 20.4 us: 1.01x faster                                                          |
| unpickle_list        | 2.93 us                                                             | 3.00 us: 1.02x slower                                                          |
| xml_etree_parse      | 104 ms                                                              | 114 ms: 1.09x slower                                                           |
| json_dumps           | 6.84 ms                                                             | 8.05 ms: 1.18x slower                                                          |
| xml_etree_iterparse  | 64.2 ms                                                             | 86.1 ms: 1.34x slower                                                          |
| xml_etree_generate   | 59.6 ms                                                             | 84.7 ms: 1.42x slower                                                          |
| xml_etree_process    | 42.1 ms                                                             | 64.0 ms: 1.52x slower                                                          |
| pickle_pure_python   | 213 us                                                              | 348 us: 1.63x slower                                                           |
| tomli_loads          | 1.65 sec                                                            | 2.79 sec: 1.69x slower                                                         |
| unpickle_pure_python | 147 us                                                              | 279 us: 1.90x slower                                                           |
| Geometric mean       | (ref)                                                               | 1.22x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 22.3 ms: 1.01x slower                                                          |
| python_startup_no_site | 18.2 ms                                                             | 19.6 ms: 1.08x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.04x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0 |
|-----------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako      | 6.94 ms                                                             | 12.4 ms: 1.79x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| sqlglot_normalize          | 206 ms                                                              | 118 ms: 1.75x faster                                                           |
| create_gc_cycles           | 756 us                                                              | 645 us: 1.17x faster                                                           |
| pickle_list                | 3.57 us                                                             | 3.28 us: 1.09x faster                                                          |
| pickle                     | 8.07 us                                                             | 7.73 us: 1.04x faster                                                          |
| pickle_dict                | 20.8 us                                                             | 19.9 us: 1.04x faster                                                          |
| unpickle                   | 9.79 us                                                             | 9.47 us: 1.03x faster                                                          |
| gc_traversal               | 1.43 ms                                                             | 1.39 ms: 1.03x faster                                                          |
| json_loads                 | 20.5 us                                                             | 20.4 us: 1.01x faster                                                          |
| python_startup             | 22.2 ms                                                             | 22.3 ms: 1.01x slower                                                          |
| regex_dna                  | 118 ms                                                              | 119 ms: 1.01x slower                                                           |
| unpickle_list              | 2.93 us                                                             | 3.00 us: 1.02x slower                                                          |
| regex_effbot               | 1.88 ms                                                             | 1.93 ms: 1.03x slower                                                          |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.5 sec: 1.04x slower                                                         |
| typing_runtime_protocols   | 136 us                                                              | 143 us: 1.05x slower                                                           |
| bench_mp_pool              | 69.4 ms                                                             | 73.9 ms: 1.07x slower                                                          |
| regex_v8                   | 15.7 ms                                                             | 16.8 ms: 1.07x slower                                                          |
| json                       | 4.10 ms                                                             | 4.41 ms: 1.08x slower                                                          |
| python_startup_no_site     | 18.2 ms                                                             | 19.6 ms: 1.08x slower                                                          |
| sqlite_synth               | 1.96 us                                                             | 2.12 us: 1.08x slower                                                          |
| pathlib                    | 83.9 ms                                                             | 90.9 ms: 1.08x slower                                                          |
| xml_etree_parse            | 104 ms                                                              | 114 ms: 1.09x slower                                                           |
| telco                      | 6.03 ms                                                             | 6.92 ms: 1.15x slower                                                          |
| json_dumps                 | 6.84 ms                                                             | 8.05 ms: 1.18x slower                                                          |
| docutils                   | 1.81 sec                                                            | 2.17 sec: 1.20x slower                                                         |
| bench_thread_pool          | 985 us                                                              | 1.18 ms: 1.20x slower                                                          |
| sympy_expand               | 375 ms                                                              | 457 ms: 1.22x slower                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 579 ms: 1.23x slower                                                           |
| tornado_http               | 94.3 ms                                                             | 116 ms: 1.23x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 569 ms: 1.27x slower                                                           |
| mdp                        | 1.60 sec                                                            | 2.06 sec: 1.29x slower                                                         |
| meteor_contest             | 74.1 ms                                                             | 96.7 ms: 1.31x slower                                                          |
| sympy_str                  | 211 ms                                                              | 276 ms: 1.31x slower                                                           |
| sympy_sum                  | 105 ms                                                              | 139 ms: 1.32x slower                                                           |
| 2to3                       | 233 ms                                                              | 309 ms: 1.32x slower                                                           |
| xml_etree_iterparse        | 64.2 ms                                                             | 86.1 ms: 1.34x slower                                                          |
| crypto_pyaes               | 55.8 ms                                                             | 76.0 ms: 1.36x slower                                                          |
| sympy_integrate            | 14.6 ms                                                             | 20.1 ms: 1.37x slower                                                          |
| async_generators           | 266 ms                                                              | 365 ms: 1.38x slower                                                           |
| async_tree_none            | 228 ms                                                              | 317 ms: 1.39x slower                                                           |
| async_tree_io_tg           | 529 ms                                                              | 743 ms: 1.40x slower                                                           |
| sqlglot_optimize           | 39.7 ms                                                             | 55.9 ms: 1.41x slower                                                          |
| xml_etree_generate         | 59.6 ms                                                             | 84.7 ms: 1.42x slower                                                          |
| logging_format             | 8.13 us                                                             | 11.6 us: 1.42x slower                                                          |
| async_tree_io              | 530 ms                                                              | 757 ms: 1.43x slower                                                           |
| async_tree_memoization     | 275 ms                                                              | 396 ms: 1.44x slower                                                           |
| deepcopy_reduce            | 2.59 us                                                             | 3.73 us: 1.44x slower                                                          |
| pycparser                  | 777 ms                                                              | 1.13 sec: 1.45x slower                                                         |
| logging_simple             | 7.47 us                                                             | 10.9 us: 1.46x slower                                                          |
| pprint_safe_repr           | 607 ms                                                              | 901 ms: 1.48x slower                                                           |
| pprint_pformat             | 1.24 sec                                                            | 1.85 sec: 1.49x slower                                                         |
| async_tree_none_tg         | 203 ms                                                              | 304 ms: 1.50x slower                                                           |
| deepcopy                   | 280 us                                                              | 420 us: 1.50x slower                                                           |
| xml_etree_process          | 42.1 ms                                                             | 64.0 ms: 1.52x slower                                                          |
| async_tree_memoization_tg  | 254 ms                                                              | 386 ms: 1.52x slower                                                           |
| sqlglot_transpile          | 1.19 ms                                                             | 1.82 ms: 1.53x slower                                                          |
| sqlglot_parse              | 964 us                                                              | 1.52 ms: 1.58x slower                                                          |
| nqueens                    | 68.7 ms                                                             | 109 ms: 1.58x slower                                                           |
| regex_compile              | 99.9 ms                                                             | 159 ms: 1.60x slower                                                           |
| chameleon                  | 5.71 ms                                                             | 9.20 ms: 1.61x slower                                                          |
| pickle_pure_python         | 213 us                                                              | 348 us: 1.63x slower                                                           |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 4.77 ms: 1.66x slower                                                          |
| chaos                      | 48.0 ms                                                             | 80.1 ms: 1.67x slower                                                          |
| tomli_loads                | 1.65 sec                                                            | 2.79 sec: 1.69x slower                                                         |
| scimark_fft                | 198 ms                                                              | 335 ms: 1.69x slower                                                           |
| go                         | 101 ms                                                              | 175 ms: 1.74x slower                                                           |
| pyflate                    | 308 ms                                                              | 539 ms: 1.75x slower                                                           |
| raytrace                   | 189 ms                                                              | 331 ms: 1.76x slower                                                           |
| fannkuch                   | 270 ms                                                              | 475 ms: 1.76x slower                                                           |
| float                      | 52.4 ms                                                             | 92.7 ms: 1.77x slower                                                          |
| mako                       | 6.94 ms                                                             | 12.4 ms: 1.79x slower                                                          |
| richards_super             | 35.5 ms                                                             | 64.1 ms: 1.81x slower                                                          |
| coroutines                 | 15.5 ms                                                             | 28.2 ms: 1.82x slower                                                          |
| scimark_monte_carlo        | 45.2 ms                                                             | 83.1 ms: 1.84x slower                                                          |
| richards                   | 31.2 ms                                                             | 59.1 ms: 1.89x slower                                                          |
| unpickle_pure_python       | 147 us                                                              | 279 us: 1.90x slower                                                           |
| comprehensions             | 11.9 us                                                             | 23.3 us: 1.96x slower                                                          |
| spectral_norm              | 68.0 ms                                                             | 135 ms: 1.99x slower                                                           |
| deltablue                  | 2.23 ms                                                             | 4.47 ms: 2.00x slower                                                          |
| scimark_lu                 | 59.4 ms                                                             | 123 ms: 2.07x slower                                                           |
| scimark_sor                | 81.0 ms                                                             | 168 ms: 2.07x slower                                                           |
| hexiom                     | 4.23 ms                                                             | 8.81 ms: 2.08x slower                                                          |
| deepcopy_memo              | 23.5 us                                                             | 49.5 us: 2.10x slower                                                          |
| nbody                      | 76.9 ms                                                             | 167 ms: 2.18x slower                                                           |
| coverage                   | 307 ms                                                              | 690 ms: 2.25x slower                                                           |
| logging_silent             | 57.9 ns                                                             | 138 ns: 2.38x slower                                                           |
| generators                 | 21.2 ms                                                             | 50.6 ms: 2.39x slower                                                          |
| Geometric mean             | (ref)                                                               | 1.40x slower                                                                   |

Benchmark hidden because not significant (2): pidigits, asyncio_tcp
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
Ignored benchmarks (1) of results/bm-20231013-3.13.0a1-ad056f0-PYTHON_UOPS/bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.37x
- 95% likely to have a slowdown of 1.35x
- 99% likely to have a slowdown of 1.32x

# Memory
- memory change: unknown