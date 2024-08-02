
# Results vs. 3.12.0

- fork: python
- ref: ad056f03aee8000a1564
- machine: windows-x86
- commit hash: ad056f0
- commit date: 2023-10-13
- overall geometric mean: 1.17x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 309 ms: 1.10x slower                                                           |
| chameleon      | 7.75 ms                                                         | 9.20 ms: 1.19x slower                                                          |
| docutils       | 1.98 sec                                                        | 2.17 sec: 1.09x slower                                                         |
| tornado_http   | 105 ms                                                          | 116 ms: 1.10x slower                                                           |
| Geometric mean | (ref)                                                           | 1.12x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 564 ms                                                          | 579 ms: 1.03x slower                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 569 ms: 1.04x slower                                                           |
| async_tree_none            | 298 ms                                                          | 317 ms: 1.07x slower                                                           |
| async_tree_memoization     | 364 ms                                                          | 396 ms: 1.09x slower                                                           |
| async_tree_io              | 693 ms                                                          | 757 ms: 1.09x slower                                                           |
| async_tree_io_tg           | 677 ms                                                          | 743 ms: 1.10x slower                                                           |
| async_tree_none_tg         | 278 ms                                                          | 304 ms: 1.10x slower                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 386 ms: 1.10x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.08x slower                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 199 ms                                                          | 198 ms: 1.01x faster                                                           |
| float          | 76.7 ms                                                         | 92.7 ms: 1.21x slower                                                          |
| nbody          | 127 ms                                                          | 167 ms: 1.32x slower                                                           |
| Geometric mean | (ref)                                                           | 1.17x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 127 ms                                                          | 119 ms: 1.07x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.93 ms: 1.05x faster                                                          |
| regex_v8       | 15.0 ms                                                         | 16.8 ms: 1.12x slower                                                          |
| regex_compile  | 129 ms                                                          | 159 ms: 1.23x slower                                                           |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pickle_list          | 3.37 us                                                         | 3.28 us: 1.03x faster                                                          |
| unpickle             | 9.71 us                                                         | 9.47 us: 1.03x faster                                                          |
| pickle               | 7.79 us                                                         | 7.73 us: 1.01x faster                                                          |
| xml_etree_parse      | 113 ms                                                          | 114 ms: 1.01x slower                                                           |
| unpickle_list        | 2.95 us                                                         | 3.00 us: 1.02x slower                                                          |
| json_dumps           | 7.40 ms                                                         | 8.05 ms: 1.09x slower                                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 86.1 ms: 1.11x slower                                                          |
| xml_etree_generate   | 72.1 ms                                                         | 84.7 ms: 1.17x slower                                                          |
| xml_etree_process    | 53.2 ms                                                         | 64.0 ms: 1.20x slower                                                          |
| pickle_pure_python   | 286 us                                                          | 348 us: 1.22x slower                                                           |
| tomli_loads          | 2.20 sec                                                        | 2.79 sec: 1.27x slower                                                         |
| unpickle_pure_python | 210 us                                                          | 279 us: 1.33x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.09x slower                                                                   |

Benchmark hidden because not significant (2): pickle_dict, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.6 ms: 1.03x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.01x slower                                                                   |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0 |
|-----------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako      | 9.96 ms                                                         | 12.4 ms: 1.25x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna                  | 127 ms                                                          | 119 ms: 1.07x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.93 ms: 1.05x faster                                                          |
| gc_traversal               | 1.44 ms                                                         | 1.39 ms: 1.04x faster                                                          |
| pickle_list                | 3.37 us                                                         | 3.28 us: 1.03x faster                                                          |
| unpickle                   | 9.71 us                                                         | 9.47 us: 1.03x faster                                                          |
| bench_mp_pool              | 75.4 ms                                                         | 73.9 ms: 1.02x faster                                                          |
| create_gc_cycles           | 652 us                                                          | 645 us: 1.01x faster                                                           |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.5 sec: 1.01x faster                                                         |
| pickle                     | 7.79 us                                                         | 7.73 us: 1.01x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 90.9 ms: 1.01x faster                                                          |
| pidigits                   | 199 ms                                                          | 198 ms: 1.01x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 114 ms: 1.01x slower                                                           |
| unpickle_list              | 2.95 us                                                         | 3.00 us: 1.02x slower                                                          |
| sqlite_synth               | 2.07 us                                                         | 2.12 us: 1.02x slower                                                          |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 579 ms: 1.03x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 19.6 ms: 1.03x slower                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 569 ms: 1.04x slower                                                           |
| json                       | 4.15 ms                                                         | 4.41 ms: 1.06x slower                                                          |
| async_tree_none            | 298 ms                                                          | 317 ms: 1.07x slower                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.18 ms: 1.07x slower                                                          |
| raytrace                   | 308 ms                                                          | 331 ms: 1.08x slower                                                           |
| mdp                        | 1.91 sec                                                        | 2.06 sec: 1.08x slower                                                         |
| json_dumps                 | 7.40 ms                                                         | 8.05 ms: 1.09x slower                                                          |
| async_tree_memoization     | 364 ms                                                          | 396 ms: 1.09x slower                                                           |
| async_tree_io              | 693 ms                                                          | 757 ms: 1.09x slower                                                           |
| docutils                   | 1.98 sec                                                        | 2.17 sec: 1.09x slower                                                         |
| async_tree_io_tg           | 677 ms                                                          | 743 ms: 1.10x slower                                                           |
| async_tree_none_tg         | 278 ms                                                          | 304 ms: 1.10x slower                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 76.0 ms: 1.10x slower                                                          |
| 2to3                       | 280 ms                                                          | 309 ms: 1.10x slower                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 386 ms: 1.10x slower                                                           |
| tornado_http               | 105 ms                                                          | 116 ms: 1.10x slower                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 86.1 ms: 1.11x slower                                                          |
| logging_format             | 10.4 us                                                         | 11.6 us: 1.11x slower                                                          |
| meteor_contest             | 86.9 ms                                                         | 96.7 ms: 1.11x slower                                                          |
| regex_v8                   | 15.0 ms                                                         | 16.8 ms: 1.12x slower                                                          |
| logging_simple             | 9.75 us                                                         | 10.9 us: 1.12x slower                                                          |
| typing_runtime_protocols   | 126 us                                                          | 143 us: 1.13x slower                                                           |
| sympy_sum                  | 123 ms                                                          | 139 ms: 1.13x slower                                                           |
| sympy_integrate            | 17.5 ms                                                         | 20.1 ms: 1.15x slower                                                          |
| sympy_expand               | 398 ms                                                          | 457 ms: 1.15x slower                                                           |
| sympy_str                  | 240 ms                                                          | 276 ms: 1.15x slower                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 55.9 ms: 1.15x slower                                                          |
| pycparser                  | 978 ms                                                          | 1.13 sec: 1.15x slower                                                         |
| chaos                      | 69.4 ms                                                         | 80.1 ms: 1.15x slower                                                          |
| deepcopy_reduce            | 3.23 us                                                         | 3.73 us: 1.16x slower                                                          |
| nqueens                    | 93.7 ms                                                         | 109 ms: 1.16x slower                                                           |
| async_generators           | 313 ms                                                          | 365 ms: 1.17x slower                                                           |
| deepcopy                   | 360 us                                                          | 420 us: 1.17x slower                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 84.7 ms: 1.17x slower                                                          |
| sqlglot_normalize          | 100 ms                                                          | 118 ms: 1.18x slower                                                           |
| chameleon                  | 7.75 ms                                                         | 9.20 ms: 1.19x slower                                                          |
| sqlglot_transpile          | 1.53 ms                                                         | 1.82 ms: 1.19x slower                                                          |
| xml_etree_process          | 53.2 ms                                                         | 64.0 ms: 1.20x slower                                                          |
| float                      | 76.7 ms                                                         | 92.7 ms: 1.21x slower                                                          |
| comprehensions             | 19.2 us                                                         | 23.3 us: 1.21x slower                                                          |
| pickle_pure_python         | 286 us                                                          | 348 us: 1.22x slower                                                           |
| unpack_sequence            | 62.5 ns                                                         | 76.1 ns: 1.22x slower                                                          |
| sqlglot_parse              | 1.25 ms                                                         | 1.52 ms: 1.22x slower                                                          |
| regex_compile              | 129 ms                                                          | 159 ms: 1.23x slower                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.85 sec: 1.23x slower                                                         |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 4.77 ms: 1.24x slower                                                          |
| scimark_fft                | 271 ms                                                          | 335 ms: 1.24x slower                                                           |
| mako                       | 9.96 ms                                                         | 12.4 ms: 1.25x slower                                                          |
| deltablue                  | 3.58 ms                                                         | 4.47 ms: 1.25x slower                                                          |
| pprint_safe_repr           | 721 ms                                                          | 901 ms: 1.25x slower                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 83.1 ms: 1.25x slower                                                          |
| telco                      | 5.51 ms                                                         | 6.92 ms: 1.25x slower                                                          |
| tomli_loads                | 2.20 sec                                                        | 2.79 sec: 1.27x slower                                                         |
| pyflate                    | 424 ms                                                          | 539 ms: 1.27x slower                                                           |
| go                         | 137 ms                                                          | 175 ms: 1.27x slower                                                           |
| deepcopy_memo              | 38.4 us                                                         | 49.5 us: 1.29x slower                                                          |
| hexiom                     | 6.82 ms                                                         | 8.81 ms: 1.29x slower                                                          |
| scimark_sor                | 130 ms                                                          | 168 ms: 1.29x slower                                                           |
| spectral_norm              | 104 ms                                                          | 135 ms: 1.30x slower                                                           |
| generators                 | 38.5 ms                                                         | 50.6 ms: 1.32x slower                                                          |
| nbody                      | 127 ms                                                          | 167 ms: 1.32x slower                                                           |
| scimark_lu                 | 93.2 ms                                                         | 123 ms: 1.32x slower                                                           |
| unpickle_pure_python       | 210 us                                                          | 279 us: 1.33x slower                                                           |
| fannkuch                   | 354 ms                                                          | 475 ms: 1.34x slower                                                           |
| coroutines                 | 20.9 ms                                                         | 28.2 ms: 1.35x slower                                                          |
| logging_silent             | 101 ns                                                          | 138 ns: 1.37x slower                                                           |
| richards_super             | 46.5 ms                                                         | 64.1 ms: 1.38x slower                                                          |
| richards                   | 41.3 ms                                                         | 59.1 ms: 1.43x slower                                                          |
| coverage                   | 48.4 ms                                                         | 690 ms: 14.24x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.17x slower                                                                   |

Benchmark hidden because not significant (4): pickle_dict, python_startup, json_loads, asyncio_tcp
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, django_template, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.11x
- 95% likely to have a slowdown of 1.10x
- 99% likely to have a slowdown of 1.10x


# Memory

- memory change: unknown