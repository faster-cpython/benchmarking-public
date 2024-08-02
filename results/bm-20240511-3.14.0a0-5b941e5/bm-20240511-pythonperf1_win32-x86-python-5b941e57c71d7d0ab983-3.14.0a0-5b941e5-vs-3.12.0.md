# Results vs. 3.12.0

- fork: python
- ref: 5b941e57c71d7d0ab983
- machine: windows-x86
- commit hash: 5b941e5
- commit date: 2024-05-11
- overall geometric mean: 1.21x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 234 ms: 1.20x faster                                                           |
| chameleon      | 7.75 ms                                                         | 5.83 ms: 1.33x faster                                                          |
| docutils       | 1.98 sec                                                        | 1.81 sec: 1.09x faster                                                         |
| tornado_http   | 105 ms                                                          | 94.6 ms: 1.11x faster                                                          |
| Geometric mean | (ref)                                                           | 1.18x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 255 ms: 1.38x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 202 ms: 1.37x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 277 ms: 1.31x faster                                                           |
| async_tree_none            | 298 ms                                                          | 228 ms: 1.30x faster                                                           |
| async_tree_io              | 693 ms                                                          | 538 ms: 1.29x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 530 ms: 1.28x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 450 ms: 1.21x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 470 ms: 1.20x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.29x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 75.0 ms: 1.69x faster                                                          |
| float          | 76.7 ms                                                         | 52.0 ms: 1.47x faster                                                          |
| Geometric mean | (ref)                                                           | 1.36x faster                                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 97.3 ms: 1.33x faster                                                          |
| regex_effbot   | 2.04 ms                                                         | 1.92 ms: 1.06x faster                                                          |
| regex_dna      | 127 ms                                                          | 120 ms: 1.06x faster                                                           |
| regex_v8       | 15.0 ms                                                         | 16.2 ms: 1.07x slower                                                          |
| Geometric mean | (ref)                                                           | 1.08x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 147 us: 1.43x faster                                                           |
| tomli_loads          | 2.20 sec                                                        | 1.63 sec: 1.35x faster                                                         |
| pickle_pure_python   | 286 us                                                          | 212 us: 1.35x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 41.7 ms: 1.28x faster                                                          |
| xml_etree_generate   | 72.1 ms                                                         | 58.1 ms: 1.24x faster                                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 63.9 ms: 1.21x faster                                                          |
| json_dumps           | 7.40 ms                                                         | 6.79 ms: 1.09x faster                                                          |
| xml_etree_parse      | 113 ms                                                          | 105 ms: 1.08x faster                                                           |
| pickle               | 7.79 us                                                         | 7.92 us: 1.02x slower                                                          |
| unpickle_list        | 2.95 us                                                         | 3.00 us: 1.02x slower                                                          |
| pickle_list          | 3.37 us                                                         | 3.45 us: 1.02x slower                                                          |
| unpickle             | 9.71 us                                                         | 9.98 us: 1.03x slower                                                          |
| pickle_dict          | 19.9 us                                                         | 20.6 us: 1.03x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.13x faster                                                                   |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 18.4 ms: 1.04x faster                                                          |
| python_startup         | 22.4 ms                                                         | 22.1 ms: 1.01x faster                                                          |
| Geometric mean         | (ref)                                                           | 1.02x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 6.85 ms: 1.45x faster                                                          |
| django_template | 36.9 ms                                                         | 30.1 ms: 1.23x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.34x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| generators                 | 38.5 ms                                                         | 21.3 ms: 1.81x faster                                                          |
| logging_silent             | 101 ns                                                          | 58.2 ns: 1.74x faster                                                          |
| nbody                      | 127 ms                                                          | 75.0 ms: 1.69x faster                                                          |
| raytrace                   | 308 ms                                                          | 184 ms: 1.67x faster                                                           |
| deepcopy_memo              | 38.4 us                                                         | 23.5 us: 1.63x faster                                                          |
| deltablue                  | 3.58 ms                                                         | 2.20 ms: 1.63x faster                                                          |
| comprehensions             | 19.2 us                                                         | 11.9 us: 1.61x faster                                                          |
| hexiom                     | 6.82 ms                                                         | 4.28 ms: 1.59x faster                                                          |
| scimark_lu                 | 93.2 ms                                                         | 59.9 ms: 1.55x faster                                                          |
| spectral_norm              | 104 ms                                                          | 67.9 ms: 1.53x faster                                                          |
| scimark_sor                | 130 ms                                                          | 86.2 ms: 1.51x faster                                                          |
| float                      | 76.7 ms                                                         | 52.0 ms: 1.47x faster                                                          |
| chaos                      | 69.4 ms                                                         | 47.3 ms: 1.47x faster                                                          |
| mako                       | 9.96 ms                                                         | 6.85 ms: 1.45x faster                                                          |
| unpickle_pure_python       | 210 us                                                          | 147 us: 1.43x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 46.9 ms: 1.42x faster                                                          |
| pyflate                    | 424 ms                                                          | 304 ms: 1.39x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 255 ms: 1.38x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 68.2 ms: 1.37x faster                                                          |
| async_tree_none_tg         | 278 ms                                                          | 202 ms: 1.37x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.63 sec: 1.35x faster                                                         |
| pickle_pure_python         | 286 us                                                          | 212 us: 1.35x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.87 ms: 1.34x faster                                                          |
| go                         | 137 ms                                                          | 102 ms: 1.34x faster                                                           |
| fannkuch                   | 354 ms                                                          | 266 ms: 1.33x faster                                                           |
| chameleon                  | 7.75 ms                                                         | 5.83 ms: 1.33x faster                                                          |
| regex_compile              | 129 ms                                                          | 97.3 ms: 1.33x faster                                                          |
| richards                   | 41.3 ms                                                         | 31.2 ms: 1.33x faster                                                          |
| richards_super             | 46.5 ms                                                         | 35.1 ms: 1.32x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 277 ms: 1.31x faster                                                           |
| scimark_fft                | 271 ms                                                          | 206 ms: 1.31x faster                                                           |
| logging_simple             | 9.75 us                                                         | 7.44 us: 1.31x faster                                                          |
| async_tree_none            | 298 ms                                                          | 228 ms: 1.30x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 958 us: 1.30x faster                                                           |
| deepcopy                   | 360 us                                                          | 277 us: 1.30x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 16.1 ms: 1.30x faster                                                          |
| async_tree_io              | 693 ms                                                          | 538 ms: 1.29x faster                                                           |
| logging_format             | 10.4 us                                                         | 8.08 us: 1.29x faster                                                          |
| sqlglot_transpile          | 1.53 ms                                                         | 1.19 ms: 1.29x faster                                                          |
| xml_etree_process          | 53.2 ms                                                         | 41.7 ms: 1.28x faster                                                          |
| async_tree_io_tg           | 677 ms                                                          | 530 ms: 1.28x faster                                                           |
| pycparser                  | 978 ms                                                          | 782 ms: 1.25x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 55.4 ms: 1.25x faster                                                          |
| xml_etree_generate         | 72.1 ms                                                         | 58.1 ms: 1.24x faster                                                          |
| django_template            | 36.9 ms                                                         | 30.1 ms: 1.23x faster                                                          |
| sympy_integrate            | 17.5 ms                                                         | 14.4 ms: 1.21x faster                                                          |
| xml_etree_iterparse        | 77.6 ms                                                         | 63.9 ms: 1.21x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 450 ms: 1.21x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.67 us: 1.21x faster                                                          |
| pprint_pformat             | 1.50 sec                                                        | 1.24 sec: 1.21x faster                                                         |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 470 ms: 1.20x faster                                                           |
| 2to3                       | 280 ms                                                          | 234 ms: 1.20x faster                                                           |
| pprint_safe_repr           | 721 ms                                                          | 604 ms: 1.19x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 104 ms: 1.18x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.64 sec: 1.16x faster                                                         |
| sympy_str                  | 240 ms                                                          | 206 ms: 1.16x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 74.8 ms: 1.16x faster                                                          |
| sqlglot_optimize           | 48.5 ms                                                         | 41.9 ms: 1.16x faster                                                          |
| async_generators           | 313 ms                                                          | 279 ms: 1.12x faster                                                           |
| tornado_http               | 105 ms                                                          | 94.6 ms: 1.11x faster                                                          |
| bench_thread_pool          | 1.10 ms                                                         | 1000 us: 1.10x faster                                                          |
| docutils                   | 1.98 sec                                                        | 1.81 sec: 1.09x faster                                                         |
| sympy_expand               | 398 ms                                                          | 364 ms: 1.09x faster                                                           |
| json_dumps                 | 7.40 ms                                                         | 6.79 ms: 1.09x faster                                                          |
| xml_etree_parse            | 113 ms                                                          | 105 ms: 1.08x faster                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 70.6 ms: 1.07x faster                                                          |
| sqlite_synth               | 2.07 us                                                         | 1.94 us: 1.07x faster                                                          |
| regex_effbot               | 2.04 ms                                                         | 1.92 ms: 1.06x faster                                                          |
| regex_dna                  | 127 ms                                                          | 120 ms: 1.06x faster                                                           |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.9 sec: 1.05x faster                                                         |
| python_startup_no_site     | 19.1 ms                                                         | 18.4 ms: 1.04x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 88.5 ms: 1.03x faster                                                          |
| python_startup             | 22.4 ms                                                         | 22.1 ms: 1.01x faster                                                          |
| gc_traversal               | 1.44 ms                                                         | 1.43 ms: 1.01x faster                                                          |
| coverage                   | 48.4 ms                                                         | 48.7 ms: 1.01x slower                                                          |
| pickle                     | 7.79 us                                                         | 7.92 us: 1.02x slower                                                          |
| unpickle_list              | 2.95 us                                                         | 3.00 us: 1.02x slower                                                          |
| pickle_list                | 3.37 us                                                         | 3.45 us: 1.02x slower                                                          |
| unpickle                   | 9.71 us                                                         | 9.98 us: 1.03x slower                                                          |
| pickle_dict                | 19.9 us                                                         | 20.6 us: 1.03x slower                                                          |
| asyncio_tcp                | 662 ms                                                          | 694 ms: 1.05x slower                                                           |
| telco                      | 5.51 ms                                                         | 5.78 ms: 1.05x slower                                                          |
| typing_runtime_protocols   | 126 us                                                          | 133 us: 1.05x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 16.2 ms: 1.07x slower                                                          |
| create_gc_cycles           | 652 us                                                          | 745 us: 1.14x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 211 ms: 2.10x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.21x faster                                                                   |

Benchmark hidden because not significant (3): json_loads, json, pidigits
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240511-3.14.0a0-5b941e5/bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: unknown