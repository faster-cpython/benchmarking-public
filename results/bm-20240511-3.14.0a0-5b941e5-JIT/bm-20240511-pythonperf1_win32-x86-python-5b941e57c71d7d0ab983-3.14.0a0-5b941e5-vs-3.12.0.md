# Results vs. 3.12.0

- fork: python
- ref: 5b941e57c71d7d0ab983
- machine: windows-x86
- commit hash: 5b941e5
- commit date: 2024-05-11
- overall geometric mean: 1.23x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 249 ms: 1.13x faster                                                           |
| chameleon      | 7.75 ms                                                         | 6.16 ms: 1.26x faster                                                          |
| docutils       | 1.98 sec                                                        | 1.88 sec: 1.06x faster                                                         |
| tornado_http   | 105 ms                                                          | 97.0 ms: 1.08x faster                                                          |
| Geometric mean | (ref)                                                           | 1.13x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none_tg         | 278 ms                                                          | 205 ms: 1.35x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 260 ms: 1.35x faster                                                           |
| async_tree_none            | 298 ms                                                          | 228 ms: 1.31x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 278 ms: 1.31x faster                                                           |
| async_tree_io              | 693 ms                                                          | 534 ms: 1.30x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 533 ms: 1.27x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 463 ms: 1.18x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 479 ms: 1.18x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.28x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 55.2 ms: 2.30x faster                                                          |
| float          | 76.7 ms                                                         | 41.1 ms: 1.87x faster                                                          |
| pidigits       | 199 ms                                                          | 197 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                           | 1.63x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 92.2 ms: 1.40x faster                                                          |
| regex_dna      | 127 ms                                                          | 118 ms: 1.08x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.99 ms: 1.02x faster                                                          |
| regex_v8       | 15.0 ms                                                         | 15.6 ms: 1.04x slower                                                          |
| Geometric mean | (ref)                                                           | 1.10x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.39 sec: 1.58x faster                                                         |
| unpickle_pure_python | 210 us                                                          | 137 us: 1.53x faster                                                           |
| pickle_pure_python   | 286 us                                                          | 202 us: 1.42x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 40.2 ms: 1.32x faster                                                          |
| xml_etree_generate   | 72.1 ms                                                         | 55.3 ms: 1.30x faster                                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 61.8 ms: 1.26x faster                                                          |
| json_dumps           | 7.40 ms                                                         | 6.53 ms: 1.13x faster                                                          |
| xml_etree_parse      | 113 ms                                                          | 105 ms: 1.08x faster                                                           |
| unpickle_list        | 2.95 us                                                         | 2.73 us: 1.08x faster                                                          |
| json_loads           | 20.4 us                                                         | 21.0 us: 1.03x slower                                                          |
| pickle_dict          | 19.9 us                                                         | 20.7 us: 1.04x slower                                                          |
| pickle_list          | 3.37 us                                                         | 3.54 us: 1.05x slower                                                          |
| pickle               | 7.79 us                                                         | 8.19 us: 1.05x slower                                                          |
| unpickle             | 9.71 us                                                         | 10.4 us: 1.07x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.16x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.5 ms: 1.08x slower                                                          |
| python_startup         | 22.4 ms                                                         | 24.4 ms: 1.09x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.31 ms: 1.88x faster                                                          |
| django_template | 36.9 ms                                                         | 32.0 ms: 1.15x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.47x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody                      | 127 ms                                                          | 55.2 ms: 2.30x faster                                                          |
| spectral_norm              | 104 ms                                                          | 47.2 ms: 2.20x faster                                                          |
| mako                       | 9.96 ms                                                         | 5.31 ms: 1.88x faster                                                          |
| float                      | 76.7 ms                                                         | 41.1 ms: 1.87x faster                                                          |
| logging_silent             | 101 ns                                                          | 54.7 ns: 1.85x faster                                                          |
| deepcopy_memo              | 38.4 us                                                         | 20.8 us: 1.85x faster                                                          |
| comprehensions             | 19.2 us                                                         | 10.8 us: 1.78x faster                                                          |
| generators                 | 38.5 ms                                                         | 23.2 ms: 1.66x faster                                                          |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.34 ms: 1.65x faster                                                          |
| scimark_monte_carlo        | 66.4 ms                                                         | 41.2 ms: 1.61x faster                                                          |
| scimark_fft                | 271 ms                                                          | 168 ms: 1.61x faster                                                           |
| fannkuch                   | 354 ms                                                          | 220 ms: 1.61x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.39 sec: 1.58x faster                                                         |
| unpickle_pure_python       | 210 us                                                          | 137 us: 1.53x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 4.53 ms: 1.51x faster                                                          |
| raytrace                   | 308 ms                                                          | 208 ms: 1.48x faster                                                           |
| scimark_sor                | 130 ms                                                          | 89.6 ms: 1.45x faster                                                          |
| crypto_pyaes               | 69.2 ms                                                         | 47.9 ms: 1.45x faster                                                          |
| pickle_pure_python         | 286 us                                                          | 202 us: 1.42x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.53 ms: 1.42x faster                                                          |
| regex_compile              | 129 ms                                                          | 92.2 ms: 1.40x faster                                                          |
| pyflate                    | 424 ms                                                          | 306 ms: 1.38x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 903 us: 1.38x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 69.2 ms: 1.35x faster                                                          |
| async_tree_none_tg         | 278 ms                                                          | 205 ms: 1.35x faster                                                           |
| chaos                      | 69.4 ms                                                         | 51.5 ms: 1.35x faster                                                          |
| async_tree_memoization_tg  | 350 ms                                                          | 260 ms: 1.35x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 40.2 ms: 1.32x faster                                                          |
| logging_simple             | 9.75 us                                                         | 7.37 us: 1.32x faster                                                          |
| richards                   | 41.3 ms                                                         | 31.3 ms: 1.32x faster                                                          |
| sqlglot_transpile          | 1.53 ms                                                         | 1.16 ms: 1.31x faster                                                          |
| async_tree_none            | 298 ms                                                          | 228 ms: 1.31x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 278 ms: 1.31x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 55.3 ms: 1.30x faster                                                          |
| richards_super             | 46.5 ms                                                         | 35.7 ms: 1.30x faster                                                          |
| async_tree_io              | 693 ms                                                          | 534 ms: 1.30x faster                                                           |
| go                         | 137 ms                                                          | 106 ms: 1.30x faster                                                           |
| logging_format             | 10.4 us                                                         | 8.03 us: 1.30x faster                                                          |
| pprint_pformat             | 1.50 sec                                                        | 1.16 sec: 1.29x faster                                                         |
| pprint_safe_repr           | 721 ms                                                          | 560 ms: 1.29x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 533 ms: 1.27x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 16.5 ms: 1.27x faster                                                          |
| chameleon                  | 7.75 ms                                                         | 6.16 ms: 1.26x faster                                                          |
| xml_etree_iterparse        | 77.6 ms                                                         | 61.8 ms: 1.26x faster                                                          |
| pycparser                  | 978 ms                                                          | 781 ms: 1.25x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 76.0 ms: 1.23x faster                                                          |
| deepcopy_reduce            | 3.23 us                                                         | 2.67 us: 1.21x faster                                                          |
| deepcopy                   | 360 us                                                          | 302 us: 1.19x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 73.3 ms: 1.19x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 463 ms: 1.18x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 479 ms: 1.18x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.63 sec: 1.18x faster                                                         |
| sqlglot_optimize           | 48.5 ms                                                         | 41.7 ms: 1.16x faster                                                          |
| sympy_sum                  | 123 ms                                                          | 106 ms: 1.16x faster                                                           |
| django_template            | 36.9 ms                                                         | 32.0 ms: 1.15x faster                                                          |
| sympy_str                  | 240 ms                                                          | 208 ms: 1.15x faster                                                           |
| json_dumps                 | 7.40 ms                                                         | 6.53 ms: 1.13x faster                                                          |
| sympy_integrate            | 17.5 ms                                                         | 15.5 ms: 1.13x faster                                                          |
| 2to3                       | 280 ms                                                          | 249 ms: 1.13x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 991 us: 1.11x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.88 us: 1.10x faster                                                          |
| async_generators           | 313 ms                                                          | 285 ms: 1.10x faster                                                           |
| tornado_http               | 105 ms                                                          | 97.0 ms: 1.08x faster                                                          |
| xml_etree_parse            | 113 ms                                                          | 105 ms: 1.08x faster                                                           |
| regex_dna                  | 127 ms                                                          | 118 ms: 1.08x faster                                                           |
| sympy_expand               | 398 ms                                                          | 369 ms: 1.08x faster                                                           |
| unpickle_list              | 2.95 us                                                         | 2.73 us: 1.08x faster                                                          |
| docutils                   | 1.98 sec                                                        | 1.88 sec: 1.06x faster                                                         |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.0 sec: 1.04x faster                                                         |
| pathlib                    | 91.4 ms                                                         | 87.9 ms: 1.04x faster                                                          |
| regex_effbot               | 2.04 ms                                                         | 1.99 ms: 1.02x faster                                                          |
| pidigits                   | 199 ms                                                          | 197 ms: 1.01x faster                                                           |
| json_loads                 | 20.4 us                                                         | 21.0 us: 1.03x slower                                                          |
| pickle_dict                | 19.9 us                                                         | 20.7 us: 1.04x slower                                                          |
| telco                      | 5.51 ms                                                         | 5.72 ms: 1.04x slower                                                          |
| regex_v8                   | 15.0 ms                                                         | 15.6 ms: 1.04x slower                                                          |
| json                       | 4.15 ms                                                         | 4.34 ms: 1.04x slower                                                          |
| pickle_list                | 3.37 us                                                         | 3.54 us: 1.05x slower                                                          |
| pickle                     | 7.79 us                                                         | 8.19 us: 1.05x slower                                                          |
| coverage                   | 48.4 ms                                                         | 51.2 ms: 1.06x slower                                                          |
| unpickle                   | 9.71 us                                                         | 10.4 us: 1.07x slower                                                          |
| asyncio_tcp                | 662 ms                                                          | 711 ms: 1.07x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 20.5 ms: 1.08x slower                                                          |
| python_startup             | 22.4 ms                                                         | 24.4 ms: 1.09x slower                                                          |
| typing_runtime_protocols   | 126 us                                                          | 140 us: 1.11x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 751 us: 1.15x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 220 ms: 2.20x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.23x faster                                                                   |

Benchmark hidden because not significant (2): bench_mp_pool, gc_traversal
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240511-3.14.0a0-5b941e5-JIT/bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: unknown