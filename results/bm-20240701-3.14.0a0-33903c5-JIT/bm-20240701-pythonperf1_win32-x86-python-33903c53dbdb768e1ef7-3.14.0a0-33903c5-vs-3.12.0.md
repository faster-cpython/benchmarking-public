# Results vs. 3.12.0

- fork: python
- ref: 33903c53dbdb768e1ef7
- machine: windows-x86
- commit hash: 33903c5
- commit date: 2024-07-01
- overall geometric mean: 1.20x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-pythonperf1_win32-x86-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 261 ms: 1.07x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.98 sec: 1.00x faster                                                         |
| tornado_http   | 105 ms                                                          | 101 ms: 1.04x faster                                                           |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-pythonperf1_win32-x86-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 266 ms: 1.32x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 213 ms: 1.30x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 534 ms: 1.27x faster                                                           |
| async_tree_none            | 298 ms                                                          | 238 ms: 1.25x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 294 ms: 1.24x faster                                                           |
| async_tree_io              | 693 ms                                                          | 576 ms: 1.20x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 506 ms: 1.11x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 493 ms: 1.11x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.22x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-pythonperf1_win32-x86-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 55.3 ms: 2.30x faster                                                          |
| float          | 76.7 ms                                                         | 44.5 ms: 1.72x faster                                                          |
| pidigits       | 199 ms                                                          | 197 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                           | 1.59x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-pythonperf1_win32-x86-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 100.0 ms: 1.29x faster                                                         |
| regex_dna      | 127 ms                                                          | 120 ms: 1.06x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 2.00 ms: 1.02x faster                                                          |
| regex_v8       | 15.0 ms                                                         | 16.0 ms: 1.06x slower                                                          |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-pythonperf1_win32-x86-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.57 sec: 1.40x faster                                                         |
| unpickle_pure_python | 210 us                                                          | 159 us: 1.32x faster                                                           |
| pickle_pure_python   | 286 us                                                          | 223 us: 1.28x faster                                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 62.7 ms: 1.24x faster                                                          |
| xml_etree_generate   | 72.1 ms                                                         | 63.9 ms: 1.13x faster                                                          |
| xml_etree_process    | 53.2 ms                                                         | 48.5 ms: 1.10x faster                                                          |
| xml_etree_parse      | 113 ms                                                          | 105 ms: 1.07x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 7.26 ms: 1.02x faster                                                          |
| json_loads           | 20.4 us                                                         | 21.2 us: 1.04x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.16x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-pythonperf1_win32-x86-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.3 ms: 1.01x slower                                                          |
| python_startup         | 22.4 ms                                                         | 23.4 ms: 1.05x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.03x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-pythonperf1_win32-x86-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.36 ms: 1.86x faster                                                          |
| django_template | 36.9 ms                                                         | 36.0 ms: 1.03x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.38x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-pythonperf1_win32-x86-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 16.3 us: 2.36x faster                                                          |
| nbody                      | 127 ms                                                          | 55.3 ms: 2.30x faster                                                          |
| spectral_norm              | 104 ms                                                          | 49.3 ms: 2.11x faster                                                          |
| mako                       | 9.96 ms                                                         | 5.36 ms: 1.86x faster                                                          |
| float                      | 76.7 ms                                                         | 44.5 ms: 1.72x faster                                                          |
| logging_silent             | 101 ns                                                          | 59.9 ns: 1.69x faster                                                          |
| comprehensions             | 19.2 us                                                         | 11.5 us: 1.67x faster                                                          |
| scimark_fft                | 271 ms                                                          | 163 ms: 1.66x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.37 ms: 1.63x faster                                                          |
| scimark_monte_carlo        | 66.4 ms                                                         | 42.2 ms: 1.57x faster                                                          |
| fannkuch                   | 354 ms                                                          | 236 ms: 1.50x faster                                                           |
| pyflate                    | 424 ms                                                          | 284 ms: 1.50x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 4.63 ms: 1.47x faster                                                          |
| crypto_pyaes               | 69.2 ms                                                         | 48.0 ms: 1.44x faster                                                          |
| deepcopy                   | 360 us                                                          | 254 us: 1.42x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.57 sec: 1.40x faster                                                         |
| unpickle_pure_python       | 210 us                                                          | 159 us: 1.32x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 266 ms: 1.32x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 213 ms: 1.30x faster                                                           |
| regex_compile              | 129 ms                                                          | 100.0 ms: 1.29x faster                                                         |
| sqlglot_parse              | 1.25 ms                                                         | 967 us: 1.29x faster                                                           |
| generators                 | 38.5 ms                                                         | 29.9 ms: 1.29x faster                                                          |
| pickle_pure_python         | 286 us                                                          | 223 us: 1.28x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 73.2 ms: 1.28x faster                                                          |
| chaos                      | 69.4 ms                                                         | 54.7 ms: 1.27x faster                                                          |
| async_tree_io_tg           | 677 ms                                                          | 534 ms: 1.27x faster                                                           |
| async_tree_none            | 298 ms                                                          | 238 ms: 1.25x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 62.7 ms: 1.24x faster                                                          |
| sqlglot_transpile          | 1.53 ms                                                         | 1.24 ms: 1.24x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 294 ms: 1.24x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.22 sec: 1.23x faster                                                         |
| raytrace                   | 308 ms                                                          | 252 ms: 1.22x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.64 us: 1.22x faster                                                          |
| deltablue                  | 3.58 ms                                                         | 2.95 ms: 1.21x faster                                                          |
| pprint_safe_repr           | 721 ms                                                          | 594 ms: 1.21x faster                                                           |
| async_tree_io              | 693 ms                                                          | 576 ms: 1.20x faster                                                           |
| logging_simple             | 9.75 us                                                         | 8.18 us: 1.19x faster                                                          |
| logging_format             | 10.4 us                                                         | 8.86 us: 1.17x faster                                                          |
| scimark_sor                | 130 ms                                                          | 111 ms: 1.17x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.65 sec: 1.16x faster                                                         |
| richards                   | 41.3 ms                                                         | 36.0 ms: 1.15x faster                                                          |
| meteor_contest             | 86.9 ms                                                         | 76.2 ms: 1.14x faster                                                          |
| scimark_lu                 | 93.2 ms                                                         | 82.1 ms: 1.13x faster                                                          |
| go                         | 137 ms                                                          | 121 ms: 1.13x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 63.9 ms: 1.13x faster                                                          |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 506 ms: 1.11x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 991 us: 1.11x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 493 ms: 1.11x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 111 ms: 1.11x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 48.5 ms: 1.10x faster                                                          |
| sympy_integrate            | 17.5 ms                                                         | 16.0 ms: 1.10x faster                                                          |
| pycparser                  | 978 ms                                                          | 897 ms: 1.09x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 83.9 ms: 1.09x faster                                                          |
| xml_etree_parse            | 113 ms                                                          | 105 ms: 1.07x faster                                                           |
| 2to3                       | 280 ms                                                          | 261 ms: 1.07x faster                                                           |
| sympy_str                  | 240 ms                                                          | 224 ms: 1.07x faster                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 45.7 ms: 1.06x faster                                                          |
| regex_dna                  | 127 ms                                                          | 120 ms: 1.06x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 19.8 ms: 1.05x faster                                                          |
| asyncio_tcp                | 662 ms                                                          | 629 ms: 1.05x faster                                                           |
| richards_super             | 46.5 ms                                                         | 44.2 ms: 1.05x faster                                                          |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.9 sec: 1.04x faster                                                         |
| tornado_http               | 105 ms                                                          | 101 ms: 1.04x faster                                                           |
| django_template            | 36.9 ms                                                         | 36.0 ms: 1.03x faster                                                          |
| regex_effbot               | 2.04 ms                                                         | 2.00 ms: 1.02x faster                                                          |
| json_dumps                 | 7.40 ms                                                         | 7.26 ms: 1.02x faster                                                          |
| sympy_expand               | 398 ms                                                          | 391 ms: 1.02x faster                                                           |
| pidigits                   | 199 ms                                                          | 197 ms: 1.01x faster                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 74.6 ms: 1.01x faster                                                          |
| docutils                   | 1.98 sec                                                        | 1.98 sec: 1.00x faster                                                         |
| sqlglot_normalize          | 100 ms                                                          | 101 ms: 1.01x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 19.3 ms: 1.01x slower                                                          |
| telco                      | 5.51 ms                                                         | 5.65 ms: 1.03x slower                                                          |
| json                       | 4.15 ms                                                         | 4.28 ms: 1.03x slower                                                          |
| json_loads                 | 20.4 us                                                         | 21.2 us: 1.04x slower                                                          |
| python_startup             | 22.4 ms                                                         | 23.4 ms: 1.05x slower                                                          |
| regex_v8                   | 15.0 ms                                                         | 16.0 ms: 1.06x slower                                                          |
| async_generators           | 313 ms                                                          | 336 ms: 1.07x slower                                                           |
| coverage                   | 48.4 ms                                                         | 52.6 ms: 1.09x slower                                                          |
| create_gc_cycles           | 652 us                                                          | 750 us: 1.15x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 157 us: 1.25x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.20x faster                                                                   |

Benchmark hidden because not significant (1): gc_traversal
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240701-3.14.0a0-33903c5-JIT/bm-20240701-pythonperf1_win32-x86-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown