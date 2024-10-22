# Results vs. 3.13.0

- fork: python
- ref: ad056f03aee8000a1564
- machine: windows-x86
- commit hash: ad056f0
- commit date: 2023-10-13
- overall geometric mean: 1.33x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 309 ms: 1.22x slower                                                           |
| chameleon      | 6.14 ms                                                         | 9.20 ms: 1.50x slower                                                          |
| docutils       | 1.82 sec                                                        | 2.17 sec: 1.19x slower                                                         |
| tornado_http   | 104 ms                                                          | 116 ms: 1.11x slower                                                           |
| Geometric mean | (ref)                                                           | 1.25x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| asyncio_tcp                | 842 ms                                                          | 674 ms: 1.25x faster                                                           |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.5 sec: 1.01x slower                                                         |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 579 ms: 1.17x slower                                                           |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 569 ms: 1.23x slower                                                           |
| async_tree_none            | 246 ms                                                          | 317 ms: 1.29x slower                                                           |
| async_tree_memoization     | 302 ms                                                          | 396 ms: 1.31x slower                                                           |
| async_generators           | 274 ms                                                          | 365 ms: 1.33x slower                                                           |
| async_tree_memoization_tg  | 287 ms                                                          | 386 ms: 1.35x slower                                                           |
| async_tree_none_tg         | 219 ms                                                          | 304 ms: 1.39x slower                                                           |
| async_tree_io              | 537 ms                                                          | 757 ms: 1.41x slower                                                           |
| async_tree_io_tg           | 509 ms                                                          | 743 ms: 1.46x slower                                                           |
| coroutines                 | 15.7 ms                                                         | 28.2 ms: 1.80x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.27x slower                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 202 ms                                                          | 198 ms: 1.02x faster                                                           |
| float          | 57.8 ms                                                         | 92.7 ms: 1.60x slower                                                          |
| nbody          | 81.9 ms                                                         | 167 ms: 2.04x slower                                                           |
| Geometric mean | (ref)                                                           | 1.48x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 117 ms                                                          | 119 ms: 1.02x slower                                                           |
| regex_effbot   | 1.81 ms                                                         | 1.93 ms: 1.07x slower                                                          |
| regex_v8       | 15.6 ms                                                         | 16.8 ms: 1.08x slower                                                          |
| regex_compile  | 103 ms                                                          | 159 ms: 1.54x slower                                                           |
| Geometric mean | (ref)                                                           | 1.16x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle             | 10.5 us                                                         | 9.47 us: 1.11x faster                                                          |
| pickle_dict          | 21.7 us                                                         | 19.9 us: 1.09x faster                                                          |
| pickle               | 8.42 us                                                         | 7.73 us: 1.09x faster                                                          |
| pickle_list          | 3.40 us                                                         | 3.28 us: 1.03x faster                                                          |
| unpickle_list        | 3.09 us                                                         | 3.00 us: 1.03x faster                                                          |
| json_loads           | 21.0 us                                                         | 20.4 us: 1.03x faster                                                          |
| xml_etree_parse      | 109 ms                                                          | 114 ms: 1.05x slower                                                           |
| json_dumps           | 7.40 ms                                                         | 8.05 ms: 1.09x slower                                                          |
| xml_etree_iterparse  | 65.1 ms                                                         | 86.1 ms: 1.32x slower                                                          |
| xml_etree_generate   | 62.6 ms                                                         | 84.7 ms: 1.35x slower                                                          |
| xml_etree_process    | 45.0 ms                                                         | 64.0 ms: 1.42x slower                                                          |
| pickle_pure_python   | 238 us                                                          | 348 us: 1.46x slower                                                           |
| tomli_loads          | 1.73 sec                                                        | 2.79 sec: 1.61x slower                                                         |
| unpickle_pure_python | 162 us                                                          | 279 us: 1.73x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.16x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup | 24.3 ms                                                         | 22.3 ms: 1.09x faster                                                          |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                   |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0 |
|-----------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako      | 7.31 ms                                                         | 12.4 ms: 1.70x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| sqlglot_normalize          | 220 ms                                                          | 118 ms: 1.86x faster                                                           |
| asyncio_tcp                | 842 ms                                                          | 674 ms: 1.25x faster                                                           |
| unpickle                   | 10.5 us                                                         | 9.47 us: 1.11x faster                                                          |
| create_gc_cycles           | 713 us                                                          | 645 us: 1.11x faster                                                           |
| pickle_dict                | 21.7 us                                                         | 19.9 us: 1.09x faster                                                          |
| pickle                     | 8.42 us                                                         | 7.73 us: 1.09x faster                                                          |
| python_startup             | 24.3 ms                                                         | 22.3 ms: 1.09x faster                                                          |
| gc_traversal               | 1.45 ms                                                         | 1.39 ms: 1.05x faster                                                          |
| pickle_list                | 3.40 us                                                         | 3.28 us: 1.03x faster                                                          |
| unpickle_list              | 3.09 us                                                         | 3.00 us: 1.03x faster                                                          |
| json_loads                 | 21.0 us                                                         | 20.4 us: 1.03x faster                                                          |
| pidigits                   | 202 ms                                                          | 198 ms: 1.02x faster                                                           |
| bench_mp_pool              | 74.3 ms                                                         | 73.9 ms: 1.01x faster                                                          |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.5 sec: 1.01x slower                                                         |
| pathlib                    | 89.4 ms                                                         | 90.9 ms: 1.02x slower                                                          |
| regex_dna                  | 117 ms                                                          | 119 ms: 1.02x slower                                                           |
| json                       | 4.27 ms                                                         | 4.41 ms: 1.03x slower                                                          |
| telco                      | 6.67 ms                                                         | 6.92 ms: 1.04x slower                                                          |
| typing_runtime_protocols   | 136 us                                                          | 143 us: 1.05x slower                                                           |
| xml_etree_parse            | 109 ms                                                          | 114 ms: 1.05x slower                                                           |
| regex_effbot               | 1.81 ms                                                         | 1.93 ms: 1.07x slower                                                          |
| regex_v8                   | 15.6 ms                                                         | 16.8 ms: 1.08x slower                                                          |
| sqlite_synth               | 1.97 us                                                         | 2.12 us: 1.08x slower                                                          |
| json_dumps                 | 7.40 ms                                                         | 8.05 ms: 1.09x slower                                                          |
| tornado_http               | 104 ms                                                          | 116 ms: 1.11x slower                                                           |
| bench_thread_pool          | 1.02 ms                                                         | 1.18 ms: 1.16x slower                                                          |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 579 ms: 1.17x slower                                                           |
| docutils                   | 1.82 sec                                                        | 2.17 sec: 1.19x slower                                                         |
| sympy_expand               | 375 ms                                                          | 457 ms: 1.22x slower                                                           |
| 2to3                       | 253 ms                                                          | 309 ms: 1.22x slower                                                           |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 569 ms: 1.23x slower                                                           |
| mdp                        | 1.67 sec                                                        | 2.06 sec: 1.23x slower                                                         |
| meteor_contest             | 77.0 ms                                                         | 96.7 ms: 1.26x slower                                                          |
| sympy_str                  | 215 ms                                                          | 276 ms: 1.28x slower                                                           |
| sympy_sum                  | 108 ms                                                          | 139 ms: 1.29x slower                                                           |
| async_tree_none            | 246 ms                                                          | 317 ms: 1.29x slower                                                           |
| pycparser                  | 869 ms                                                          | 1.13 sec: 1.30x slower                                                         |
| crypto_pyaes               | 58.2 ms                                                         | 76.0 ms: 1.31x slower                                                          |
| deepcopy_reduce            | 2.85 us                                                         | 3.73 us: 1.31x slower                                                          |
| async_tree_memoization     | 302 ms                                                          | 396 ms: 1.31x slower                                                           |
| sqlglot_optimize           | 42.5 ms                                                         | 55.9 ms: 1.32x slower                                                          |
| xml_etree_iterparse        | 65.1 ms                                                         | 86.1 ms: 1.32x slower                                                          |
| sympy_integrate            | 15.2 ms                                                         | 20.1 ms: 1.32x slower                                                          |
| async_generators           | 274 ms                                                          | 365 ms: 1.33x slower                                                           |
| async_tree_memoization_tg  | 287 ms                                                          | 386 ms: 1.35x slower                                                           |
| logging_format             | 8.57 us                                                         | 11.6 us: 1.35x slower                                                          |
| xml_etree_generate         | 62.6 ms                                                         | 84.7 ms: 1.35x slower                                                          |
| deepcopy                   | 307 us                                                          | 420 us: 1.37x slower                                                           |
| logging_simple             | 7.87 us                                                         | 10.9 us: 1.39x slower                                                          |
| async_tree_none_tg         | 219 ms                                                          | 304 ms: 1.39x slower                                                           |
| pprint_safe_repr           | 644 ms                                                          | 901 ms: 1.40x slower                                                           |
| sqlglot_transpile          | 1.29 ms                                                         | 1.82 ms: 1.41x slower                                                          |
| async_tree_io              | 537 ms                                                          | 757 ms: 1.41x slower                                                           |
| xml_etree_process          | 45.0 ms                                                         | 64.0 ms: 1.42x slower                                                          |
| pprint_pformat             | 1.30 sec                                                        | 1.85 sec: 1.43x slower                                                         |
| nqueens                    | 75.1 ms                                                         | 109 ms: 1.45x slower                                                           |
| sqlglot_parse              | 1.05 ms                                                         | 1.52 ms: 1.45x slower                                                          |
| async_tree_io_tg           | 509 ms                                                          | 743 ms: 1.46x slower                                                           |
| pickle_pure_python         | 238 us                                                          | 348 us: 1.46x slower                                                           |
| chameleon                  | 6.14 ms                                                         | 9.20 ms: 1.50x slower                                                          |
| regex_compile              | 103 ms                                                          | 159 ms: 1.54x slower                                                           |
| chaos                      | 51.2 ms                                                         | 80.1 ms: 1.57x slower                                                          |
| go                         | 111 ms                                                          | 175 ms: 1.57x slower                                                           |
| float                      | 57.8 ms                                                         | 92.7 ms: 1.60x slower                                                          |
| tomli_loads                | 1.73 sec                                                        | 2.79 sec: 1.61x slower                                                         |
| raytrace                   | 205 ms                                                          | 331 ms: 1.61x slower                                                           |
| fannkuch                   | 293 ms                                                          | 475 ms: 1.62x slower                                                           |
| scimark_fft                | 206 ms                                                          | 335 ms: 1.62x slower                                                           |
| scimark_sparse_mat_mult    | 2.90 ms                                                         | 4.77 ms: 1.64x slower                                                          |
| scimark_monte_carlo        | 50.3 ms                                                         | 83.1 ms: 1.65x slower                                                          |
| pyflate                    | 326 ms                                                          | 539 ms: 1.65x slower                                                           |
| richards_super             | 38.0 ms                                                         | 64.1 ms: 1.69x slower                                                          |
| mako                       | 7.31 ms                                                         | 12.4 ms: 1.70x slower                                                          |
| unpickle_pure_python       | 162 us                                                          | 279 us: 1.73x slower                                                           |
| richards                   | 33.8 ms                                                         | 59.1 ms: 1.75x slower                                                          |
| unpack_sequence            | 42.9 ns                                                         | 76.1 ns: 1.77x slower                                                          |
| coroutines                 | 15.7 ms                                                         | 28.2 ms: 1.80x slower                                                          |
| scimark_sor                | 91.8 ms                                                         | 168 ms: 1.83x slower                                                           |
| comprehensions             | 12.7 us                                                         | 23.3 us: 1.83x slower                                                          |
| deltablue                  | 2.41 ms                                                         | 4.47 ms: 1.86x slower                                                          |
| deepcopy_memo              | 26.2 us                                                         | 49.5 us: 1.89x slower                                                          |
| spectral_norm              | 71.3 ms                                                         | 135 ms: 1.90x slower                                                           |
| hexiom                     | 4.64 ms                                                         | 8.81 ms: 1.90x slower                                                          |
| scimark_lu                 | 63.5 ms                                                         | 123 ms: 1.93x slower                                                           |
| nbody                      | 81.9 ms                                                         | 167 ms: 2.04x slower                                                           |
| coverage                   | 333 ms                                                          | 690 ms: 2.07x slower                                                           |
| logging_silent             | 61.6 ns                                                         | 138 ns: 2.24x slower                                                           |
| generators                 | 22.1 ms                                                         | 50.6 ms: 2.29x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.33x slower                                                                   |

Benchmark hidden because not significant (1): python_startup_no_site
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: django_template, dulwich_log, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.32x
- 95% likely to have a slowdown of 1.31x
- 99% likely to have a slowdown of 1.29x

# Memory
- memory change: unknown