# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_ghccc
- machine: windows-x86
- commit hash: 98575b4
- commit date: 2024-03-21
- overall geometric mean: 1.01x slower
- HPT reliability: 99.91%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-pythonperf1_win32-x86-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 259 ms: 1.08x faster                                                          |
| chameleon      | 7.75 ms                                                         | 5.92 ms: 1.31x faster                                                         |
| docutils       | 1.98 sec                                                        | 2.42 sec: 1.22x slower                                                        |
| tornado_http   | 105 ms                                                          | 101 ms: 1.04x faster                                                          |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-pythonperf1_win32-x86-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 564 ms                                                          | 1.58 sec: 2.81x slower                                                        |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 1.63 sec: 2.99x slower                                                        |
| async_tree_memoization     | 364 ms                                                          | 1.46 sec: 4.00x slower                                                        |
| async_tree_none            | 298 ms                                                          | 1.21 sec: 4.07x slower                                                        |
| async_tree_memoization_tg  | 350 ms                                                          | 1.49 sec: 4.26x slower                                                        |
| async_tree_none_tg         | 278 ms                                                          | 1.25 sec: 4.51x slower                                                        |
| async_tree_io              | 693 ms                                                          | 4.63 sec: 6.69x slower                                                        |
| async_tree_io_tg           | 677 ms                                                          | 4.75 sec: 7.02x slower                                                        |
| Geometric mean             | (ref)                                                           | 4.33x slower                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-pythonperf1_win32-x86-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 53.7 ms: 2.37x faster                                                         |
| float          | 76.7 ms                                                         | 75.6 ms: 1.01x faster                                                         |
| pidigits       | 199 ms                                                          | 197 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                           | 1.34x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-pythonperf1_win32-x86-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 101 ms: 1.28x faster                                                          |
| regex_dna      | 127 ms                                                          | 118 ms: 1.08x faster                                                          |
| regex_effbot   | 2.04 ms                                                         | 1.93 ms: 1.06x faster                                                         |
| regex_v8       | 15.0 ms                                                         | 15.9 ms: 1.06x slower                                                         |
| Geometric mean | (ref)                                                           | 1.08x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-pythonperf1_win32-x86-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.42 sec: 1.55x faster                                                        |
| unpickle_pure_python | 210 us                                                          | 136 us: 1.54x faster                                                          |
| pickle_pure_python   | 286 us                                                          | 228 us: 1.25x faster                                                          |
| unpickle_list        | 2.95 us                                                         | 2.61 us: 1.13x faster                                                         |
| xml_etree_process    | 53.2 ms                                                         | 47.9 ms: 1.11x faster                                                         |
| xml_etree_generate   | 72.1 ms                                                         | 65.9 ms: 1.10x faster                                                         |
| pickle_list          | 3.37 us                                                         | 3.15 us: 1.07x faster                                                         |
| json_dumps           | 7.40 ms                                                         | 6.95 ms: 1.06x faster                                                         |
| pickle               | 7.79 us                                                         | 7.67 us: 1.02x faster                                                         |
| json_loads           | 20.4 us                                                         | 20.1 us: 1.01x faster                                                         |
| pickle_dict          | 19.9 us                                                         | 19.8 us: 1.01x faster                                                         |
| unpickle             | 9.71 us                                                         | 9.88 us: 1.02x slower                                                         |
| xml_etree_iterparse  | 77.6 ms                                                         | 88.7 ms: 1.14x slower                                                         |
| xml_etree_parse      | 113 ms                                                          | 130 ms: 1.15x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.10x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-pythonperf1_win32-x86-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 22.4 ms                                                         | 26.3 ms: 1.18x slower                                                         |
| python_startup_no_site | 19.1 ms                                                         | 23.7 ms: 1.24x slower                                                         |
| Geometric mean         | (ref)                                                           | 1.21x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-pythonperf1_win32-x86-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|-----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.46 ms: 1.82x faster                                                         |
| django_template | 36.9 ms                                                         | 31.1 ms: 1.19x faster                                                         |
| Geometric mean  | (ref)                                                           | 1.47x faster                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-pythonperf1_win32-x86-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody                      | 127 ms                                                          | 53.7 ms: 2.37x faster                                                         |
| spectral_norm              | 104 ms                                                          | 51.1 ms: 2.03x faster                                                         |
| mako                       | 9.96 ms                                                         | 5.46 ms: 1.82x faster                                                         |
| comprehensions             | 19.2 us                                                         | 11.6 us: 1.65x faster                                                         |
| generators                 | 38.5 ms                                                         | 24.0 ms: 1.61x faster                                                         |
| scimark_fft                | 271 ms                                                          | 170 ms: 1.59x faster                                                          |
| scimark_monte_carlo        | 66.4 ms                                                         | 42.6 ms: 1.56x faster                                                         |
| tomli_loads                | 2.20 sec                                                        | 1.42 sec: 1.55x faster                                                        |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.50 ms: 1.55x faster                                                         |
| unpickle_pure_python       | 210 us                                                          | 136 us: 1.54x faster                                                          |
| pyflate                    | 424 ms                                                          | 276 ms: 1.54x faster                                                          |
| fannkuch                   | 354 ms                                                          | 231 ms: 1.53x faster                                                          |
| deepcopy_memo              | 38.4 us                                                         | 25.4 us: 1.51x faster                                                         |
| hexiom                     | 6.82 ms                                                         | 4.55 ms: 1.50x faster                                                         |
| logging_silent             | 101 ns                                                          | 67.7 ns: 1.49x faster                                                         |
| deltablue                  | 3.58 ms                                                         | 2.49 ms: 1.44x faster                                                         |
| crypto_pyaes               | 69.2 ms                                                         | 48.2 ms: 1.44x faster                                                         |
| scimark_sor                | 130 ms                                                          | 90.9 ms: 1.43x faster                                                         |
| typing_runtime_protocols   | 126 us                                                          | 90.9 us: 1.39x faster                                                         |
| coroutines                 | 20.9 ms                                                         | 15.2 ms: 1.37x faster                                                         |
| richards                   | 41.3 ms                                                         | 31.0 ms: 1.33x faster                                                         |
| chameleon                  | 7.75 ms                                                         | 5.92 ms: 1.31x faster                                                         |
| chaos                      | 69.4 ms                                                         | 53.0 ms: 1.31x faster                                                         |
| richards_super             | 46.5 ms                                                         | 36.0 ms: 1.29x faster                                                         |
| regex_compile              | 129 ms                                                          | 101 ms: 1.28x faster                                                          |
| raytrace                   | 308 ms                                                          | 244 ms: 1.26x faster                                                          |
| deepcopy_reduce            | 3.23 us                                                         | 2.56 us: 1.26x faster                                                         |
| pickle_pure_python         | 286 us                                                          | 228 us: 1.25x faster                                                          |
| pprint_pformat             | 1.50 sec                                                        | 1.20 sec: 1.25x faster                                                        |
| logging_simple             | 9.75 us                                                         | 7.83 us: 1.25x faster                                                         |
| deepcopy                   | 360 us                                                          | 291 us: 1.24x faster                                                          |
| sqlglot_parse              | 1.25 ms                                                         | 1.01 ms: 1.23x faster                                                         |
| pprint_safe_repr           | 721 ms                                                          | 585 ms: 1.23x faster                                                          |
| logging_format             | 10.4 us                                                         | 8.48 us: 1.23x faster                                                         |
| scimark_lu                 | 93.2 ms                                                         | 76.7 ms: 1.22x faster                                                         |
| sqlglot_transpile          | 1.53 ms                                                         | 1.27 ms: 1.21x faster                                                         |
| go                         | 137 ms                                                          | 114 ms: 1.20x faster                                                          |
| nqueens                    | 93.7 ms                                                         | 78.5 ms: 1.19x faster                                                         |
| django_template            | 36.9 ms                                                         | 31.1 ms: 1.19x faster                                                         |
| meteor_contest             | 86.9 ms                                                         | 74.3 ms: 1.17x faster                                                         |
| sympy_sum                  | 123 ms                                                          | 106 ms: 1.16x faster                                                          |
| sympy_str                  | 240 ms                                                          | 210 ms: 1.14x faster                                                          |
| sympy_integrate            | 17.5 ms                                                         | 15.5 ms: 1.13x faster                                                         |
| unpickle_list              | 2.95 us                                                         | 2.61 us: 1.13x faster                                                         |
| gc_traversal               | 1.44 ms                                                         | 1.28 ms: 1.12x faster                                                         |
| sqlglot_optimize           | 48.5 ms                                                         | 43.1 ms: 1.12x faster                                                         |
| xml_etree_process          | 53.2 ms                                                         | 47.9 ms: 1.11x faster                                                         |
| mdp                        | 1.91 sec                                                        | 1.73 sec: 1.10x faster                                                        |
| xml_etree_generate         | 72.1 ms                                                         | 65.9 ms: 1.10x faster                                                         |
| bench_thread_pool          | 1.10 ms                                                         | 1.01 ms: 1.09x faster                                                         |
| sqlite_synth               | 2.07 us                                                         | 1.91 us: 1.09x faster                                                         |
| 2to3                       | 280 ms                                                          | 259 ms: 1.08x faster                                                          |
| regex_dna                  | 127 ms                                                          | 118 ms: 1.08x faster                                                          |
| sympy_expand               | 398 ms                                                          | 372 ms: 1.07x faster                                                          |
| pickle_list                | 3.37 us                                                         | 3.15 us: 1.07x faster                                                         |
| json_dumps                 | 7.40 ms                                                         | 6.95 ms: 1.06x faster                                                         |
| pathlib                    | 91.4 ms                                                         | 86.5 ms: 1.06x faster                                                         |
| regex_effbot               | 2.04 ms                                                         | 1.93 ms: 1.06x faster                                                         |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.8 sec: 1.05x faster                                                        |
| tornado_http               | 105 ms                                                          | 101 ms: 1.04x faster                                                          |
| pycparser                  | 978 ms                                                          | 951 ms: 1.03x faster                                                          |
| pickle                     | 7.79 us                                                         | 7.67 us: 1.02x faster                                                         |
| float                      | 76.7 ms                                                         | 75.6 ms: 1.01x faster                                                         |
| pidigits                   | 199 ms                                                          | 197 ms: 1.01x faster                                                          |
| json_loads                 | 20.4 us                                                         | 20.1 us: 1.01x faster                                                         |
| pickle_dict                | 19.9 us                                                         | 19.8 us: 1.01x faster                                                         |
| async_generators           | 313 ms                                                          | 315 ms: 1.01x slower                                                          |
| bench_mp_pool              | 75.4 ms                                                         | 76.2 ms: 1.01x slower                                                         |
| json                       | 4.15 ms                                                         | 4.22 ms: 1.02x slower                                                         |
| unpickle                   | 9.71 us                                                         | 9.88 us: 1.02x slower                                                         |
| create_gc_cycles           | 652 us                                                          | 670 us: 1.03x slower                                                          |
| telco                      | 5.51 ms                                                         | 5.80 ms: 1.05x slower                                                         |
| regex_v8                   | 15.0 ms                                                         | 15.9 ms: 1.06x slower                                                         |
| xml_etree_iterparse        | 77.6 ms                                                         | 88.7 ms: 1.14x slower                                                         |
| xml_etree_parse            | 113 ms                                                          | 130 ms: 1.15x slower                                                          |
| unpack_sequence            | 62.5 ns                                                         | 73.1 ns: 1.17x slower                                                         |
| python_startup             | 22.4 ms                                                         | 26.3 ms: 1.18x slower                                                         |
| docutils                   | 1.98 sec                                                        | 2.42 sec: 1.22x slower                                                        |
| python_startup_no_site     | 19.1 ms                                                         | 23.7 ms: 1.24x slower                                                         |
| sqlglot_normalize          | 100 ms                                                          | 216 ms: 2.16x slower                                                          |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 1.58 sec: 2.81x slower                                                        |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 1.63 sec: 2.99x slower                                                        |
| async_tree_memoization     | 364 ms                                                          | 1.46 sec: 4.00x slower                                                        |
| async_tree_none            | 298 ms                                                          | 1.21 sec: 4.07x slower                                                        |
| async_tree_memoization_tg  | 350 ms                                                          | 1.49 sec: 4.26x slower                                                        |
| async_tree_none_tg         | 278 ms                                                          | 1.25 sec: 4.51x slower                                                        |
| async_tree_io              | 693 ms                                                          | 4.63 sec: 6.69x slower                                                        |
| async_tree_io_tg           | 677 ms                                                          | 4.75 sec: 7.02x slower                                                        |
| coverage                   | 48.4 ms                                                         | 513 ms: 10.59x slower                                                         |
| Geometric mean             | (ref)                                                           | 1.01x slower                                                                  |

Benchmark hidden because not significant (1): asyncio_tcp
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240321-3.13.0a5+-98575b4-JIT/bm-20240321-pythonperf1_win32-x86-brandtbucher-justin_ghccc-3.13.0a5+-98575b4.json: genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 99.91% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.02x


# Memory

- memory change: unknown