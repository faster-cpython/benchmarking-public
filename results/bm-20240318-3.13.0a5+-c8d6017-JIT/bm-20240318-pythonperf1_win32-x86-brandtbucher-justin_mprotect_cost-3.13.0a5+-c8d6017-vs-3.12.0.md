# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_mprotect_cost
- machine: windows-x86
- commit hash: c8d6017
- commit date: 2024-03-18
- overall geometric mean: 1.10x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240318-pythonperf1_win32-x86-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 255 ms: 1.10x faster                                                                  |
| chameleon      | 7.75 ms                                                         | 5.84 ms: 1.33x faster                                                                 |
| docutils       | 1.98 sec                                                        | 1.81 sec: 1.10x faster                                                                |
| tornado_http   | 105 ms                                                          | 95.9 ms: 1.10x faster                                                                 |
| Geometric mean | (ref)                                                           | 1.15x faster                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240318-pythonperf1_win32-x86-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_none            | 298 ms                                                          | 258 ms: 1.15x faster                                                                  |
| async_tree_none_tg         | 278 ms                                                          | 242 ms: 1.15x faster                                                                  |
| async_tree_memoization_tg  | 350 ms                                                          | 306 ms: 1.15x faster                                                                  |
| async_tree_memoization     | 364 ms                                                          | 320 ms: 1.14x faster                                                                  |
| async_tree_io_tg           | 677 ms                                                          | 598 ms: 1.13x faster                                                                  |
| async_tree_io              | 693 ms                                                          | 616 ms: 1.12x faster                                                                  |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 519 ms: 1.09x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 505 ms: 1.08x faster                                                                  |
| Geometric mean             | (ref)                                                           | 1.13x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240318-pythonperf1_win32-x86-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 55.4 ms: 1.39x faster                                                                 |
| nbody          | 127 ms                                                          | 95.9 ms: 1.32x faster                                                                 |
| Geometric mean | (ref)                                                           | 1.23x faster                                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240318-pythonperf1_win32-x86-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 108 ms: 1.20x faster                                                                  |
| regex_effbot   | 2.04 ms                                                         | 1.89 ms: 1.08x faster                                                                 |
| regex_dna      | 127 ms                                                          | 121 ms: 1.05x faster                                                                  |
| regex_v8       | 15.0 ms                                                         | 16.2 ms: 1.07x slower                                                                 |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240318-pythonperf1_win32-x86-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| pickle_pure_python   | 286 us                                                          | 209 us: 1.37x faster                                                                  |
| tomli_loads          | 2.20 sec                                                        | 1.68 sec: 1.31x faster                                                                |
| unpickle_pure_python | 210 us                                                          | 164 us: 1.28x faster                                                                  |
| xml_etree_process    | 53.2 ms                                                         | 42.8 ms: 1.24x faster                                                                 |
| xml_etree_generate   | 72.1 ms                                                         | 62.0 ms: 1.16x faster                                                                 |
| xml_etree_iterparse  | 77.6 ms                                                         | 67.0 ms: 1.16x faster                                                                 |
| xml_etree_parse      | 113 ms                                                          | 108 ms: 1.05x faster                                                                  |
| json_dumps           | 7.40 ms                                                         | 7.07 ms: 1.05x faster                                                                 |
| json_loads           | 20.4 us                                                         | 19.8 us: 1.03x faster                                                                 |
| pickle_list          | 3.37 us                                                         | 3.31 us: 1.02x faster                                                                 |
| pickle_dict          | 19.9 us                                                         | 19.8 us: 1.01x faster                                                                 |
| unpickle             | 9.71 us                                                         | 9.96 us: 1.03x slower                                                                 |
| pickle               | 7.79 us                                                         | 8.03 us: 1.03x slower                                                                 |
| Geometric mean       | (ref)                                                           | 1.11x faster                                                                          |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240318-pythonperf1_win32-x86-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 22.4 ms                                                         | 25.1 ms: 1.12x slower                                                                 |
| python_startup_no_site | 19.1 ms                                                         | 23.0 ms: 1.21x slower                                                                 |
| Geometric mean         | (ref)                                                           | 1.16x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240318-pythonperf1_win32-x86-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.00 ms: 1.42x faster                                                                 |
| django_template | 36.9 ms                                                         | 29.1 ms: 1.27x faster                                                                 |
| Geometric mean  | (ref)                                                           | 1.34x faster                                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240318-pythonperf1_win32-x86-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| generators                 | 38.5 ms                                                         | 22.2 ms: 1.73x faster                                                                 |
| logging_silent             | 101 ns                                                          | 60.0 ns: 1.68x faster                                                                 |
| deepcopy_memo              | 38.4 us                                                         | 24.4 us: 1.57x faster                                                                 |
| coroutines                 | 20.9 ms                                                         | 14.0 ms: 1.50x faster                                                                 |
| spectral_norm              | 104 ms                                                          | 71.7 ms: 1.45x faster                                                                 |
| deltablue                  | 3.58 ms                                                         | 2.49 ms: 1.44x faster                                                                 |
| mako                       | 9.96 ms                                                         | 7.00 ms: 1.42x faster                                                                 |
| float                      | 76.7 ms                                                         | 55.4 ms: 1.39x faster                                                                 |
| unpack_sequence            | 62.5 ns                                                         | 45.2 ns: 1.38x faster                                                                 |
| pickle_pure_python         | 286 us                                                          | 209 us: 1.37x faster                                                                  |
| scimark_sor                | 130 ms                                                          | 97.7 ms: 1.33x faster                                                                 |
| chameleon                  | 7.75 ms                                                         | 5.84 ms: 1.33x faster                                                                 |
| nbody                      | 127 ms                                                          | 95.9 ms: 1.32x faster                                                                 |
| deepcopy_reduce            | 3.23 us                                                         | 2.45 us: 1.32x faster                                                                 |
| comprehensions             | 19.2 us                                                         | 14.6 us: 1.31x faster                                                                 |
| tomli_loads                | 2.20 sec                                                        | 1.68 sec: 1.31x faster                                                                |
| typing_runtime_protocols   | 126 us                                                          | 97.7 us: 1.29x faster                                                                 |
| deepcopy                   | 360 us                                                          | 281 us: 1.28x faster                                                                  |
| sqlglot_parse              | 1.25 ms                                                         | 972 us: 1.28x faster                                                                  |
| unpickle_pure_python       | 210 us                                                          | 164 us: 1.28x faster                                                                  |
| django_template            | 36.9 ms                                                         | 29.1 ms: 1.27x faster                                                                 |
| sqlglot_transpile          | 1.53 ms                                                         | 1.22 ms: 1.25x faster                                                                 |
| xml_etree_process          | 53.2 ms                                                         | 42.8 ms: 1.24x faster                                                                 |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.11 ms: 1.24x faster                                                                 |
| richards_super             | 46.5 ms                                                         | 37.7 ms: 1.23x faster                                                                 |
| richards                   | 41.3 ms                                                         | 33.8 ms: 1.22x faster                                                                 |
| logging_simple             | 9.75 us                                                         | 7.98 us: 1.22x faster                                                                 |
| logging_format             | 10.4 us                                                         | 8.62 us: 1.21x faster                                                                 |
| regex_compile              | 129 ms                                                          | 108 ms: 1.20x faster                                                                  |
| xml_etree_generate         | 72.1 ms                                                         | 62.0 ms: 1.16x faster                                                                 |
| go                         | 137 ms                                                          | 118 ms: 1.16x faster                                                                  |
| pycparser                  | 978 ms                                                          | 841 ms: 1.16x faster                                                                  |
| xml_etree_iterparse        | 77.6 ms                                                         | 67.0 ms: 1.16x faster                                                                 |
| chaos                      | 69.4 ms                                                         | 60.1 ms: 1.15x faster                                                                 |
| async_tree_none            | 298 ms                                                          | 258 ms: 1.15x faster                                                                  |
| scimark_fft                | 271 ms                                                          | 236 ms: 1.15x faster                                                                  |
| sympy_sum                  | 123 ms                                                          | 107 ms: 1.15x faster                                                                  |
| async_tree_none_tg         | 278 ms                                                          | 242 ms: 1.15x faster                                                                  |
| sympy_integrate            | 17.5 ms                                                         | 15.3 ms: 1.15x faster                                                                 |
| async_tree_memoization_tg  | 350 ms                                                          | 306 ms: 1.15x faster                                                                  |
| raytrace                   | 308 ms                                                          | 269 ms: 1.15x faster                                                                  |
| async_tree_memoization     | 364 ms                                                          | 320 ms: 1.14x faster                                                                  |
| hexiom                     | 6.82 ms                                                         | 5.99 ms: 1.14x faster                                                                 |
| sympy_str                  | 240 ms                                                          | 211 ms: 1.14x faster                                                                  |
| scimark_lu                 | 93.2 ms                                                         | 82.1 ms: 1.14x faster                                                                 |
| async_tree_io_tg           | 677 ms                                                          | 598 ms: 1.13x faster                                                                  |
| pyflate                    | 424 ms                                                          | 375 ms: 1.13x faster                                                                  |
| crypto_pyaes               | 69.2 ms                                                         | 61.3 ms: 1.13x faster                                                                 |
| async_tree_io              | 693 ms                                                          | 616 ms: 1.12x faster                                                                  |
| mdp                        | 1.91 sec                                                        | 1.73 sec: 1.11x faster                                                                |
| 2to3                       | 280 ms                                                          | 255 ms: 1.10x faster                                                                  |
| docutils                   | 1.98 sec                                                        | 1.81 sec: 1.10x faster                                                                |
| tornado_http               | 105 ms                                                          | 95.9 ms: 1.10x faster                                                                 |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 519 ms: 1.09x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 505 ms: 1.08x faster                                                                  |
| bench_thread_pool          | 1.10 ms                                                         | 1.02 ms: 1.08x faster                                                                 |
| regex_effbot               | 2.04 ms                                                         | 1.89 ms: 1.08x faster                                                                 |
| sympy_expand               | 398 ms                                                          | 370 ms: 1.08x faster                                                                  |
| sqlite_synth               | 2.07 us                                                         | 1.94 us: 1.07x faster                                                                 |
| pathlib                    | 91.4 ms                                                         | 86.1 ms: 1.06x faster                                                                 |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.8 sec: 1.05x faster                                                                |
| regex_dna                  | 127 ms                                                          | 121 ms: 1.05x faster                                                                  |
| meteor_contest             | 86.9 ms                                                         | 82.7 ms: 1.05x faster                                                                 |
| xml_etree_parse            | 113 ms                                                          | 108 ms: 1.05x faster                                                                  |
| scimark_monte_carlo        | 66.4 ms                                                         | 63.4 ms: 1.05x faster                                                                 |
| json_dumps                 | 7.40 ms                                                         | 7.07 ms: 1.05x faster                                                                 |
| async_generators           | 313 ms                                                          | 300 ms: 1.05x faster                                                                  |
| asyncio_tcp                | 662 ms                                                          | 634 ms: 1.04x faster                                                                  |
| sqlglot_optimize           | 48.5 ms                                                         | 46.7 ms: 1.04x faster                                                                 |
| fannkuch                   | 354 ms                                                          | 342 ms: 1.03x faster                                                                  |
| gc_traversal               | 1.44 ms                                                         | 1.40 ms: 1.03x faster                                                                 |
| bench_mp_pool              | 75.4 ms                                                         | 73.2 ms: 1.03x faster                                                                 |
| json_loads                 | 20.4 us                                                         | 19.8 us: 1.03x faster                                                                 |
| pickle_list                | 3.37 us                                                         | 3.31 us: 1.02x faster                                                                 |
| pprint_pformat             | 1.50 sec                                                        | 1.48 sec: 1.01x faster                                                                |
| pickle_dict                | 19.9 us                                                         | 19.8 us: 1.01x faster                                                                 |
| nqueens                    | 93.7 ms                                                         | 94.1 ms: 1.00x slower                                                                 |
| json                       | 4.15 ms                                                         | 4.19 ms: 1.01x slower                                                                 |
| pprint_safe_repr           | 721 ms                                                          | 728 ms: 1.01x slower                                                                  |
| create_gc_cycles           | 652 us                                                          | 662 us: 1.02x slower                                                                  |
| unpickle                   | 9.71 us                                                         | 9.96 us: 1.03x slower                                                                 |
| pickle                     | 7.79 us                                                         | 8.03 us: 1.03x slower                                                                 |
| regex_v8                   | 15.0 ms                                                         | 16.2 ms: 1.07x slower                                                                 |
| python_startup             | 22.4 ms                                                         | 25.1 ms: 1.12x slower                                                                 |
| telco                      | 5.51 ms                                                         | 6.57 ms: 1.19x slower                                                                 |
| python_startup_no_site     | 19.1 ms                                                         | 23.0 ms: 1.21x slower                                                                 |
| sqlglot_normalize          | 100 ms                                                          | 226 ms: 2.25x slower                                                                  |
| coverage                   | 48.4 ms                                                         | 501 ms: 10.35x slower                                                                 |
| Geometric mean             | (ref)                                                           | 1.10x faster                                                                          |

Benchmark hidden because not significant (2): unpickle_list, pidigits
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240318-3.13.0a5+-c8d6017-JIT/bm-20240318-pythonperf1_win32-x86-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017.json: genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.08x


# Memory

- memory change: unknown