# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_align
- machine: windows-x86
- commit hash: 0081bcd
- commit date: 2024-05-23
- overall geometric mean: 1.23x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240523-pythonperf1_win32-x86-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 249 ms: 1.12x faster                                                         |
| chameleon      | 7.75 ms                                                         | 6.18 ms: 1.25x faster                                                        |
| docutils       | 1.98 sec                                                        | 1.90 sec: 1.04x faster                                                       |
| tornado_http   | 105 ms                                                          | 97.3 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                           | 1.12x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240523-pythonperf1_win32-x86-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none_tg         | 278 ms                                                          | 207 ms: 1.34x faster                                                         |
| async_tree_memoization_tg  | 350 ms                                                          | 262 ms: 1.34x faster                                                         |
| async_tree_none            | 298 ms                                                          | 232 ms: 1.28x faster                                                         |
| async_tree_memoization     | 364 ms                                                          | 284 ms: 1.28x faster                                                         |
| async_tree_io              | 693 ms                                                          | 545 ms: 1.27x faster                                                         |
| async_tree_io_tg           | 677 ms                                                          | 536 ms: 1.26x faster                                                         |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 456 ms: 1.20x faster                                                         |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 478 ms: 1.18x faster                                                         |
| Geometric mean             | (ref)                                                           | 1.27x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240523-pythonperf1_win32-x86-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 51.8 ms: 2.45x faster                                                        |
| float          | 76.7 ms                                                         | 40.9 ms: 1.87x faster                                                        |
| pidigits       | 199 ms                                                          | 198 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                           | 1.67x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240523-pythonperf1_win32-x86-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 96.3 ms: 1.34x faster                                                        |
| regex_effbot   | 2.04 ms                                                         | 1.88 ms: 1.08x faster                                                        |
| regex_dna      | 127 ms                                                          | 119 ms: 1.07x faster                                                         |
| regex_v8       | 15.0 ms                                                         | 15.7 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                           | 1.10x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240523-pythonperf1_win32-x86-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.37 sec: 1.61x faster                                                       |
| unpickle_pure_python | 210 us                                                          | 137 us: 1.54x faster                                                         |
| pickle_pure_python   | 286 us                                                          | 204 us: 1.40x faster                                                         |
| xml_etree_iterparse  | 77.6 ms                                                         | 59.9 ms: 1.30x faster                                                        |
| xml_etree_process    | 53.2 ms                                                         | 42.6 ms: 1.25x faster                                                        |
| xml_etree_generate   | 72.1 ms                                                         | 58.0 ms: 1.24x faster                                                        |
| json_dumps           | 7.40 ms                                                         | 6.63 ms: 1.12x faster                                                        |
| xml_etree_parse      | 113 ms                                                          | 102 ms: 1.11x faster                                                         |
| unpickle_list        | 2.95 us                                                         | 2.85 us: 1.03x faster                                                        |
| json_loads           | 20.4 us                                                         | 21.0 us: 1.03x slower                                                        |
| unpickle             | 9.71 us                                                         | 10.0 us: 1.03x slower                                                        |
| pickle_dict          | 19.9 us                                                         | 20.7 us: 1.04x slower                                                        |
| pickle_list          | 3.37 us                                                         | 3.60 us: 1.07x slower                                                        |
| pickle               | 7.79 us                                                         | 9.05 us: 1.16x slower                                                        |
| Geometric mean       | (ref)                                                           | 1.14x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240523-pythonperf1_win32-x86-brandtbucher-justin_align-3.14.0a0-0081bcd |
|------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.5 ms: 1.08x slower                                                        |
| python_startup         | 22.4 ms                                                         | 24.3 ms: 1.09x slower                                                        |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240523-pythonperf1_win32-x86-brandtbucher-justin_align-3.14.0a0-0081bcd |
|-----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.38 ms: 1.85x faster                                                        |
| django_template | 36.9 ms                                                         | 31.7 ms: 1.17x faster                                                        |
| Geometric mean  | (ref)                                                           | 1.47x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240523-pythonperf1_win32-x86-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody                      | 127 ms                                                          | 51.8 ms: 2.45x faster                                                        |
| spectral_norm              | 104 ms                                                          | 47.9 ms: 2.17x faster                                                        |
| float                      | 76.7 ms                                                         | 40.9 ms: 1.87x faster                                                        |
| deepcopy_memo              | 38.4 us                                                         | 20.6 us: 1.86x faster                                                        |
| mako                       | 9.96 ms                                                         | 5.38 ms: 1.85x faster                                                        |
| logging_silent             | 101 ns                                                          | 55.0 ns: 1.84x faster                                                        |
| comprehensions             | 19.2 us                                                         | 11.0 us: 1.74x faster                                                        |
| generators                 | 38.5 ms                                                         | 23.4 ms: 1.65x faster                                                        |
| fannkuch                   | 354 ms                                                          | 215 ms: 1.64x faster                                                         |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.37 ms: 1.63x faster                                                        |
| scimark_fft                | 271 ms                                                          | 167 ms: 1.62x faster                                                         |
| scimark_monte_carlo        | 66.4 ms                                                         | 41.2 ms: 1.61x faster                                                        |
| tomli_loads                | 2.20 sec                                                        | 1.37 sec: 1.61x faster                                                       |
| unpickle_pure_python       | 210 us                                                          | 137 us: 1.54x faster                                                         |
| hexiom                     | 6.82 ms                                                         | 4.45 ms: 1.53x faster                                                        |
| pyflate                    | 424 ms                                                          | 278 ms: 1.53x faster                                                         |
| raytrace                   | 308 ms                                                          | 202 ms: 1.52x faster                                                         |
| scimark_sor                | 130 ms                                                          | 89.4 ms: 1.45x faster                                                        |
| pickle_pure_python         | 286 us                                                          | 204 us: 1.40x faster                                                         |
| deltablue                  | 3.58 ms                                                         | 2.55 ms: 1.40x faster                                                        |
| crypto_pyaes               | 69.2 ms                                                         | 49.6 ms: 1.39x faster                                                        |
| chaos                      | 69.4 ms                                                         | 49.8 ms: 1.39x faster                                                        |
| nqueens                    | 93.7 ms                                                         | 67.5 ms: 1.39x faster                                                        |
| sqlglot_parse              | 1.25 ms                                                         | 922 us: 1.35x faster                                                         |
| richards                   | 41.3 ms                                                         | 30.7 ms: 1.35x faster                                                        |
| async_tree_none_tg         | 278 ms                                                          | 207 ms: 1.34x faster                                                         |
| async_tree_memoization_tg  | 350 ms                                                          | 262 ms: 1.34x faster                                                         |
| regex_compile              | 129 ms                                                          | 96.3 ms: 1.34x faster                                                        |
| pprint_safe_repr           | 721 ms                                                          | 542 ms: 1.33x faster                                                         |
| pprint_pformat             | 1.50 sec                                                        | 1.13 sec: 1.33x faster                                                       |
| scimark_lu                 | 93.2 ms                                                         | 70.6 ms: 1.32x faster                                                        |
| richards_super             | 46.5 ms                                                         | 35.5 ms: 1.31x faster                                                        |
| xml_etree_iterparse        | 77.6 ms                                                         | 59.9 ms: 1.30x faster                                                        |
| logging_simple             | 9.75 us                                                         | 7.54 us: 1.29x faster                                                        |
| logging_format             | 10.4 us                                                         | 8.07 us: 1.29x faster                                                        |
| sqlglot_transpile          | 1.53 ms                                                         | 1.19 ms: 1.29x faster                                                        |
| coroutines                 | 20.9 ms                                                         | 16.2 ms: 1.29x faster                                                        |
| async_tree_none            | 298 ms                                                          | 232 ms: 1.28x faster                                                         |
| async_tree_memoization     | 364 ms                                                          | 284 ms: 1.28x faster                                                         |
| async_tree_io              | 693 ms                                                          | 545 ms: 1.27x faster                                                         |
| go                         | 137 ms                                                          | 108 ms: 1.27x faster                                                         |
| async_tree_io_tg           | 677 ms                                                          | 536 ms: 1.26x faster                                                         |
| chameleon                  | 7.75 ms                                                         | 6.18 ms: 1.25x faster                                                        |
| xml_etree_process          | 53.2 ms                                                         | 42.6 ms: 1.25x faster                                                        |
| xml_etree_generate         | 72.1 ms                                                         | 58.0 ms: 1.24x faster                                                        |
| pycparser                  | 978 ms                                                          | 804 ms: 1.22x faster                                                         |
| deepcopy                   | 360 us                                                          | 300 us: 1.20x faster                                                         |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 456 ms: 1.20x faster                                                         |
| mdp                        | 1.91 sec                                                        | 1.60 sec: 1.19x faster                                                       |
| meteor_contest             | 86.9 ms                                                         | 73.5 ms: 1.18x faster                                                        |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 478 ms: 1.18x faster                                                         |
| deepcopy_reduce            | 3.23 us                                                         | 2.75 us: 1.17x faster                                                        |
| django_template            | 36.9 ms                                                         | 31.7 ms: 1.17x faster                                                        |
| sqlglot_optimize           | 48.5 ms                                                         | 42.3 ms: 1.15x faster                                                        |
| sympy_sum                  | 123 ms                                                          | 108 ms: 1.13x faster                                                         |
| sympy_str                  | 240 ms                                                          | 212 ms: 1.13x faster                                                         |
| 2to3                       | 280 ms                                                          | 249 ms: 1.12x faster                                                         |
| sympy_integrate            | 17.5 ms                                                         | 15.7 ms: 1.12x faster                                                        |
| sqlite_synth               | 2.07 us                                                         | 1.85 us: 1.12x faster                                                        |
| json_dumps                 | 7.40 ms                                                         | 6.63 ms: 1.12x faster                                                        |
| xml_etree_parse            | 113 ms                                                          | 102 ms: 1.11x faster                                                         |
| bench_thread_pool          | 1.10 ms                                                         | 1.01 ms: 1.09x faster                                                        |
| regex_effbot               | 2.04 ms                                                         | 1.88 ms: 1.08x faster                                                        |
| tornado_http               | 105 ms                                                          | 97.3 ms: 1.08x faster                                                        |
| async_generators           | 313 ms                                                          | 291 ms: 1.08x faster                                                         |
| regex_dna                  | 127 ms                                                          | 119 ms: 1.07x faster                                                         |
| sympy_expand               | 398 ms                                                          | 376 ms: 1.06x faster                                                         |
| pathlib                    | 91.4 ms                                                         | 86.4 ms: 1.06x faster                                                        |
| asyncio_tcp                | 662 ms                                                          | 634 ms: 1.04x faster                                                         |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.9 sec: 1.04x faster                                                       |
| docutils                   | 1.98 sec                                                        | 1.90 sec: 1.04x faster                                                       |
| unpickle_list              | 2.95 us                                                         | 2.85 us: 1.03x faster                                                        |
| bench_mp_pool              | 75.4 ms                                                         | 74.8 ms: 1.01x faster                                                        |
| pidigits                   | 199 ms                                                          | 198 ms: 1.01x faster                                                         |
| telco                      | 5.51 ms                                                         | 5.63 ms: 1.02x slower                                                        |
| json_loads                 | 20.4 us                                                         | 21.0 us: 1.03x slower                                                        |
| unpickle                   | 9.71 us                                                         | 10.0 us: 1.03x slower                                                        |
| json                       | 4.15 ms                                                         | 4.30 ms: 1.04x slower                                                        |
| coverage                   | 48.4 ms                                                         | 50.3 ms: 1.04x slower                                                        |
| pickle_dict                | 19.9 us                                                         | 20.7 us: 1.04x slower                                                        |
| regex_v8                   | 15.0 ms                                                         | 15.7 ms: 1.04x slower                                                        |
| pickle_list                | 3.37 us                                                         | 3.60 us: 1.07x slower                                                        |
| python_startup_no_site     | 19.1 ms                                                         | 20.5 ms: 1.08x slower                                                        |
| typing_runtime_protocols   | 126 us                                                          | 137 us: 1.08x slower                                                         |
| python_startup             | 22.4 ms                                                         | 24.3 ms: 1.09x slower                                                        |
| pickle                     | 7.79 us                                                         | 9.05 us: 1.16x slower                                                        |
| create_gc_cycles           | 652 us                                                          | 764 us: 1.17x slower                                                         |
| sqlglot_normalize          | 100 ms                                                          | 221 ms: 2.20x slower                                                         |
| Geometric mean             | (ref)                                                           | 1.23x faster                                                                 |

Benchmark hidden because not significant (1): gc_traversal
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240523-3.14.0a0-0081bcd-JIT/bm-20240523-pythonperf1_win32-x86-brandtbucher-justin_align-3.14.0a0-0081bcd.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: unknown