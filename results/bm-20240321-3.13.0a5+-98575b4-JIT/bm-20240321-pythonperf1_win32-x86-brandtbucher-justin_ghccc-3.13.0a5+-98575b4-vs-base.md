# Results vs. base

- fork: brandtbucher
- ref: justin_ghccc
- machine: windows-x86
- commit hash: 98575b4
- commit date: 2024-03-21
- overall geometric mean: 1.06x faster
- HPT reliability: 99.91%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240320-pythonperf1_win32-x86-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a | bm-20240321-pythonperf1_win32-x86-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:-------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                                          | 259 ms: 1.03x faster                                                          |
| chameleon      | 5.84 ms                                                                         | 5.92 ms: 1.01x slower                                                         |
| docutils       | 2.45 sec                                                                        | 2.42 sec: 1.01x faster                                                        |
| html5lib       | 50.2 ms                                                                         | 48.9 ms: 1.03x faster                                                         |
| tornado_http   | 97.2 ms                                                                         | 101 ms: 1.04x slower                                                          |
| Geometric mean | (ref)                                                                           | 1.00x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240320-pythonperf1_win32-x86-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a | bm-20240321-pythonperf1_win32-x86-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------------------|:-------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io_tg           | 4.73 sec                                                                        | 4.75 sec: 1.01x slower                                                        |
| async_tree_none            | 1.20 sec                                                                        | 1.21 sec: 1.01x slower                                                        |
| async_tree_cpu_io_mixed    | 1.57 sec                                                                        | 1.58 sec: 1.01x slower                                                        |
| async_tree_none_tg         | 1.24 sec                                                                        | 1.25 sec: 1.01x slower                                                        |
| async_tree_memoization_tg  | 1.47 sec                                                                        | 1.49 sec: 1.01x slower                                                        |
| async_tree_cpu_io_mixed_tg | 1.61 sec                                                                        | 1.63 sec: 1.01x slower                                                        |
| Geometric mean             | (ref)                                                                           | 1.01x slower                                                                  |

Benchmark hidden because not significant (2): async_tree_memoization, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240320-pythonperf1_win32-x86-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a | bm-20240321-pythonperf1_win32-x86-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:-------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 100 ms                                                                          | 53.7 ms: 1.87x faster                                                         |
| float          | 82.2 ms                                                                         | 75.6 ms: 1.09x faster                                                         |
| pidigits       | 199 ms                                                                          | 197 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                                           | 1.27x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240320-pythonperf1_win32-x86-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a | bm-20240321-pythonperf1_win32-x86-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:-------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 110 ms                                                                          | 101 ms: 1.09x faster                                                          |
| regex_dna      | 124 ms                                                                          | 118 ms: 1.05x faster                                                          |
| regex_effbot   | 1.95 ms                                                                         | 1.93 ms: 1.01x faster                                                         |
| regex_v8       | 16.0 ms                                                                         | 15.9 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                                           | 1.04x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240320-pythonperf1_win32-x86-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a | bm-20240321-pythonperf1_win32-x86-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------------|:-------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| unpickle_pure_python | 174 us                                                                          | 136 us: 1.28x faster                                                          |
| tomli_loads          | 1.72 sec                                                                        | 1.42 sec: 1.21x faster                                                        |
| unpickle_list        | 3.04 us                                                                         | 2.61 us: 1.17x faster                                                         |
| pickle_list          | 3.46 us                                                                         | 3.15 us: 1.10x faster                                                         |
| unpickle             | 10.5 us                                                                         | 9.88 us: 1.06x faster                                                         |
| xml_etree_iterparse  | 93.8 ms                                                                         | 88.7 ms: 1.06x faster                                                         |
| xml_etree_generate   | 69.1 ms                                                                         | 65.9 ms: 1.05x faster                                                         |
| pickle               | 8.00 us                                                                         | 7.67 us: 1.04x faster                                                         |
| xml_etree_parse      | 133 ms                                                                          | 130 ms: 1.03x faster                                                          |
| pickle_dict          | 20.0 us                                                                         | 19.8 us: 1.01x faster                                                         |
| xml_etree_process    | 47.6 ms                                                                         | 47.9 ms: 1.01x slower                                                         |
| pickle_pure_python   | 215 us                                                                          | 228 us: 1.06x slower                                                          |
| Geometric mean       | (ref)                                                                           | 1.06x faster                                                                  |

Benchmark hidden because not significant (2): json_loads, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240320-pythonperf1_win32-x86-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a | bm-20240321-pythonperf1_win32-x86-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|------------------------|:-------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 24.2 ms                                                                         | 23.7 ms: 1.02x faster                                                         |
| python_startup         | 26.6 ms                                                                         | 26.3 ms: 1.01x faster                                                         |
| Geometric mean         | (ref)                                                                           | 1.02x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240320-pythonperf1_win32-x86-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a | bm-20240321-pythonperf1_win32-x86-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:-------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako           | 7.15 ms                                                                         | 5.46 ms: 1.31x faster                                                         |
| genshi_text    | 22.8 ms                                                                         | 21.7 ms: 1.05x faster                                                         |
| genshi_xml     | 50.0 ms                                                                         | 51.0 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                                           | 1.08x faster                                                                  |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20240320-pythonperf1_win32-x86-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a | bm-20240321-pythonperf1_win32-x86-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------------------|:-------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody                      | 100 ms                                                                          | 53.7 ms: 1.87x faster                                                         |
| scimark_monte_carlo        | 64.6 ms                                                                         | 42.6 ms: 1.51x faster                                                         |
| fannkuch                   | 329 ms                                                                          | 231 ms: 1.43x faster                                                          |
| scimark_fft                | 239 ms                                                                          | 170 ms: 1.40x faster                                                          |
| spectral_norm              | 71.6 ms                                                                         | 51.1 ms: 1.40x faster                                                         |
| pyflate                    | 376 ms                                                                          | 276 ms: 1.36x faster                                                          |
| hexiom                     | 5.98 ms                                                                         | 4.55 ms: 1.32x faster                                                         |
| mako                       | 7.15 ms                                                                         | 5.46 ms: 1.31x faster                                                         |
| crypto_pyaes               | 61.5 ms                                                                         | 48.2 ms: 1.28x faster                                                         |
| unpickle_pure_python       | 174 us                                                                          | 136 us: 1.28x faster                                                          |
| scimark_sparse_mat_mult    | 3.13 ms                                                                         | 2.50 ms: 1.26x faster                                                         |
| comprehensions             | 14.4 us                                                                         | 11.6 us: 1.24x faster                                                         |
| pprint_pformat             | 1.46 sec                                                                        | 1.20 sec: 1.22x faster                                                        |
| pprint_safe_repr           | 715 ms                                                                          | 585 ms: 1.22x faster                                                          |
| tomli_loads                | 1.72 sec                                                                        | 1.42 sec: 1.21x faster                                                        |
| unpickle_list              | 3.04 us                                                                         | 2.61 us: 1.17x faster                                                         |
| richards                   | 35.7 ms                                                                         | 31.0 ms: 1.15x faster                                                         |
| chaos                      | 60.9 ms                                                                         | 53.0 ms: 1.15x faster                                                         |
| nqueens                    | 90.2 ms                                                                         | 78.5 ms: 1.15x faster                                                         |
| richards_super             | 40.9 ms                                                                         | 36.0 ms: 1.14x faster                                                         |
| telco                      | 6.53 ms                                                                         | 5.80 ms: 1.13x faster                                                         |
| meteor_contest             | 83.4 ms                                                                         | 74.3 ms: 1.12x faster                                                         |
| go                         | 126 ms                                                                          | 114 ms: 1.10x faster                                                          |
| pickle_list                | 3.46 us                                                                         | 3.15 us: 1.10x faster                                                         |
| scimark_sor                | 99.3 ms                                                                         | 90.9 ms: 1.09x faster                                                         |
| float                      | 82.2 ms                                                                         | 75.6 ms: 1.09x faster                                                         |
| typing_runtime_protocols   | 98.8 us                                                                         | 90.9 us: 1.09x faster                                                         |
| regex_compile              | 110 ms                                                                          | 101 ms: 1.09x faster                                                          |
| scimark_lu                 | 83.3 ms                                                                         | 76.7 ms: 1.09x faster                                                         |
| raytrace                   | 264 ms                                                                          | 244 ms: 1.08x faster                                                          |
| logging_simple             | 8.38 us                                                                         | 7.83 us: 1.07x faster                                                         |
| deltablue                  | 2.67 ms                                                                         | 2.49 ms: 1.07x faster                                                         |
| logging_format             | 9.02 us                                                                         | 8.48 us: 1.06x faster                                                         |
| sqlglot_optimize           | 45.8 ms                                                                         | 43.1 ms: 1.06x faster                                                         |
| unpickle                   | 10.5 us                                                                         | 9.88 us: 1.06x faster                                                         |
| xml_etree_iterparse        | 93.8 ms                                                                         | 88.7 ms: 1.06x faster                                                         |
| regex_dna                  | 124 ms                                                                          | 118 ms: 1.05x faster                                                          |
| xml_etree_generate         | 69.1 ms                                                                         | 65.9 ms: 1.05x faster                                                         |
| genshi_text                | 22.8 ms                                                                         | 21.7 ms: 1.05x faster                                                         |
| pickle                     | 8.00 us                                                                         | 7.67 us: 1.04x faster                                                         |
| pycparser                  | 989 ms                                                                          | 951 ms: 1.04x faster                                                          |
| 2to3                       | 266 ms                                                                          | 259 ms: 1.03x faster                                                          |
| html5lib                   | 50.2 ms                                                                         | 48.9 ms: 1.03x faster                                                         |
| xml_etree_parse            | 133 ms                                                                          | 130 ms: 1.03x faster                                                          |
| sqlite_synth               | 1.95 us                                                                         | 1.91 us: 1.02x faster                                                         |
| sqlglot_parse              | 1.03 ms                                                                         | 1.01 ms: 1.02x faster                                                         |
| async_generators           | 322 ms                                                                          | 315 ms: 1.02x faster                                                          |
| sqlglot_normalize          | 221 ms                                                                          | 216 ms: 1.02x faster                                                          |
| python_startup_no_site     | 24.2 ms                                                                         | 23.7 ms: 1.02x faster                                                         |
| json                       | 4.30 ms                                                                         | 4.22 ms: 1.02x faster                                                         |
| sqlglot_transpile          | 1.29 ms                                                                         | 1.27 ms: 1.01x faster                                                         |
| python_startup             | 26.6 ms                                                                         | 26.3 ms: 1.01x faster                                                         |
| docutils                   | 2.45 sec                                                                        | 2.42 sec: 1.01x faster                                                        |
| pidigits                   | 199 ms                                                                          | 197 ms: 1.01x faster                                                          |
| regex_effbot               | 1.95 ms                                                                         | 1.93 ms: 1.01x faster                                                         |
| pickle_dict                | 20.0 us                                                                         | 19.8 us: 1.01x faster                                                         |
| regex_v8                   | 16.0 ms                                                                         | 15.9 ms: 1.01x faster                                                         |
| mdp                        | 1.74 sec                                                                        | 1.73 sec: 1.00x faster                                                        |
| sympy_sum                  | 105 ms                                                                          | 106 ms: 1.00x slower                                                          |
| async_tree_io_tg           | 4.73 sec                                                                        | 4.75 sec: 1.01x slower                                                        |
| xml_etree_process          | 47.6 ms                                                                         | 47.9 ms: 1.01x slower                                                         |
| bench_mp_pool              | 75.6 ms                                                                         | 76.2 ms: 1.01x slower                                                         |
| deepcopy_memo              | 25.2 us                                                                         | 25.4 us: 1.01x slower                                                         |
| asyncio_tcp_ssl            | 16.7 sec                                                                        | 16.8 sec: 1.01x slower                                                        |
| deepcopy                   | 289 us                                                                          | 291 us: 1.01x slower                                                          |
| create_gc_cycles           | 664 us                                                                          | 670 us: 1.01x slower                                                          |
| sympy_integrate            | 15.3 ms                                                                         | 15.5 ms: 1.01x slower                                                         |
| async_tree_none            | 1.20 sec                                                                        | 1.21 sec: 1.01x slower                                                        |
| async_tree_cpu_io_mixed    | 1.57 sec                                                                        | 1.58 sec: 1.01x slower                                                        |
| async_tree_none_tg         | 1.24 sec                                                                        | 1.25 sec: 1.01x slower                                                        |
| chameleon                  | 5.84 ms                                                                         | 5.92 ms: 1.01x slower                                                         |
| async_tree_memoization_tg  | 1.47 sec                                                                        | 1.49 sec: 1.01x slower                                                        |
| async_tree_cpu_io_mixed_tg | 1.61 sec                                                                        | 1.63 sec: 1.01x slower                                                        |
| pylint                     | 405 ms                                                                          | 412 ms: 1.02x slower                                                          |
| thrift                     | 10.8 ms                                                                         | 11.1 ms: 1.02x slower                                                         |
| deepcopy_reduce            | 2.51 us                                                                         | 2.56 us: 1.02x slower                                                         |
| genshi_xml                 | 50.0 ms                                                                         | 51.0 ms: 1.02x slower                                                         |
| coroutines                 | 14.9 ms                                                                         | 15.2 ms: 1.02x slower                                                         |
| tornado_http               | 97.2 ms                                                                         | 101 ms: 1.04x slower                                                          |
| asyncio_tcp                | 629 ms                                                                          | 654 ms: 1.04x slower                                                          |
| pickle_pure_python         | 215 us                                                                          | 228 us: 1.06x slower                                                          |
| generators                 | 22.4 ms                                                                         | 24.0 ms: 1.07x slower                                                         |
| logging_silent             | 60.6 ns                                                                         | 67.7 ns: 1.12x slower                                                         |
| unpack_sequence            | 43.1 ns                                                                         | 73.1 ns: 1.69x slower                                                         |
| Geometric mean             | (ref)                                                                           | 1.06x faster                                                                  |

Benchmark hidden because not significant (11): async_tree_memoization, bench_thread_pool, sympy_str, json_loads, async_tree_io, sympy_expand, pathlib, django_template, json_dumps, gc_traversal, coverage


# HPT report

- Reliability score: 99.91% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: unknown