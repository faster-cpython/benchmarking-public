# Results vs. 3.12.0

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: windows-x86
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.15x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 254 ms: 1.10x faster                                                           |
| chameleon      | 7.75 ms                                                         | 6.16 ms: 1.26x faster                                                          |
| docutils       | 1.98 sec                                                        | 2.03 sec: 1.02x slower                                                         |
| tornado_http   | 105 ms                                                          | 100 ms: 1.05x faster                                                           |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 263 ms: 1.33x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 210 ms: 1.32x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 284 ms: 1.28x faster                                                           |
| async_tree_io              | 693 ms                                                          | 546 ms: 1.27x faster                                                           |
| async_tree_none            | 298 ms                                                          | 236 ms: 1.26x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 545 ms: 1.24x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 461 ms: 1.19x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 488 ms: 1.16x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.26x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 75.6 ms: 1.68x faster                                                          |
| float          | 76.7 ms                                                         | 51.7 ms: 1.48x faster                                                          |
| pidigits       | 199 ms                                                          | 198 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                           | 1.36x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 127 ms                                                          | 117 ms: 1.08x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.89 ms: 1.08x faster                                                          |
| regex_compile  | 129 ms                                                          | 128 ms: 1.01x faster                                                           |
| regex_v8       | 15.0 ms                                                         | 16.1 ms: 1.07x slower                                                          |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.63 sec: 1.35x faster                                                         |
| unpickle_pure_python | 210 us                                                          | 170 us: 1.24x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 43.4 ms: 1.23x faster                                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 64.4 ms: 1.21x faster                                                          |
| xml_etree_generate   | 72.1 ms                                                         | 60.9 ms: 1.18x faster                                                          |
| pickle_pure_python   | 286 us                                                          | 243 us: 1.17x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 104 ms: 1.09x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 6.97 ms: 1.06x faster                                                          |
| json_loads           | 20.4 us                                                         | 20.3 us: 1.00x faster                                                          |
| pickle_dict          | 19.9 us                                                         | 20.6 us: 1.04x slower                                                          |
| pickle_list          | 3.37 us                                                         | 3.54 us: 1.05x slower                                                          |
| unpickle             | 9.71 us                                                         | 10.3 us: 1.06x slower                                                          |
| pickle               | 7.79 us                                                         | 8.36 us: 1.07x slower                                                          |
| unpickle_list        | 2.95 us                                                         | 3.17 us: 1.08x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.08x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 18.4 ms: 1.04x faster                                                          |
| python_startup         | 22.4 ms                                                         | 22.7 ms: 1.02x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.01x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.12 ms: 1.40x faster                                                          |
| django_template | 36.9 ms                                                         | 32.6 ms: 1.13x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.26x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody                      | 127 ms                                                          | 75.6 ms: 1.68x faster                                                          |
| generators                 | 38.5 ms                                                         | 23.0 ms: 1.67x faster                                                          |
| float                      | 76.7 ms                                                         | 51.7 ms: 1.48x faster                                                          |
| raytrace                   | 308 ms                                                          | 210 ms: 1.47x faster                                                           |
| spectral_norm              | 104 ms                                                          | 70.9 ms: 1.46x faster                                                          |
| comprehensions             | 19.2 us                                                         | 13.5 us: 1.42x faster                                                          |
| deepcopy_memo              | 38.4 us                                                         | 27.2 us: 1.41x faster                                                          |
| mako                       | 9.96 ms                                                         | 7.12 ms: 1.40x faster                                                          |
| logging_silent             | 101 ns                                                          | 73.4 ns: 1.38x faster                                                          |
| chaos                      | 69.4 ms                                                         | 51.0 ms: 1.36x faster                                                          |
| richards                   | 41.3 ms                                                         | 30.4 ms: 1.36x faster                                                          |
| tomli_loads                | 2.20 sec                                                        | 1.63 sec: 1.35x faster                                                         |
| scimark_monte_carlo        | 66.4 ms                                                         | 49.4 ms: 1.35x faster                                                          |
| scimark_sor                | 130 ms                                                          | 97.0 ms: 1.34x faster                                                          |
| richards_super             | 46.5 ms                                                         | 34.7 ms: 1.34x faster                                                          |
| async_tree_memoization_tg  | 350 ms                                                          | 263 ms: 1.33x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 210 ms: 1.32x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 15.8 ms: 1.32x faster                                                          |
| fannkuch                   | 354 ms                                                          | 275 ms: 1.29x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 284 ms: 1.28x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.01 ms: 1.28x faster                                                          |
| scimark_fft                | 271 ms                                                          | 213 ms: 1.27x faster                                                           |
| async_tree_io              | 693 ms                                                          | 546 ms: 1.27x faster                                                           |
| logging_simple             | 9.75 us                                                         | 7.68 us: 1.27x faster                                                          |
| deltablue                  | 3.58 ms                                                         | 2.83 ms: 1.27x faster                                                          |
| async_tree_none            | 298 ms                                                          | 236 ms: 1.26x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 74.4 ms: 1.26x faster                                                          |
| chameleon                  | 7.75 ms                                                         | 6.16 ms: 1.26x faster                                                          |
| sqlglot_parse              | 1.25 ms                                                         | 997 us: 1.25x faster                                                           |
| logging_format             | 10.4 us                                                         | 8.37 us: 1.24x faster                                                          |
| async_tree_io_tg           | 677 ms                                                          | 545 ms: 1.24x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 170 us: 1.24x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 43.4 ms: 1.23x faster                                                          |
| hexiom                     | 6.82 ms                                                         | 5.58 ms: 1.22x faster                                                          |
| sqlglot_transpile          | 1.53 ms                                                         | 1.26 ms: 1.22x faster                                                          |
| xml_etree_iterparse        | 77.6 ms                                                         | 64.4 ms: 1.21x faster                                                          |
| pprint_pformat             | 1.50 sec                                                        | 1.25 sec: 1.20x faster                                                         |
| go                         | 137 ms                                                          | 115 ms: 1.20x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 78.4 ms: 1.19x faster                                                          |
| crypto_pyaes               | 69.2 ms                                                         | 58.2 ms: 1.19x faster                                                          |
| pprint_safe_repr           | 721 ms                                                          | 607 ms: 1.19x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 461 ms: 1.19x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 60.9 ms: 1.18x faster                                                          |
| deepcopy                   | 360 us                                                          | 305 us: 1.18x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 243 us: 1.17x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 488 ms: 1.16x faster                                                           |
| pyflate                    | 424 ms                                                          | 369 ms: 1.15x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.67 sec: 1.15x faster                                                         |
| django_template            | 36.9 ms                                                         | 32.6 ms: 1.13x faster                                                          |
| pycparser                  | 978 ms                                                          | 874 ms: 1.12x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 77.7 ms: 1.12x faster                                                          |
| deepcopy_reduce            | 3.23 us                                                         | 2.91 us: 1.11x faster                                                          |
| 2to3                       | 280 ms                                                          | 254 ms: 1.10x faster                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 44.3 ms: 1.09x faster                                                          |
| asyncio_tcp                | 662 ms                                                          | 606 ms: 1.09x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 104 ms: 1.09x faster                                                           |
| regex_dna                  | 127 ms                                                          | 117 ms: 1.08x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.02 ms: 1.08x faster                                                          |
| regex_effbot               | 2.04 ms                                                         | 1.89 ms: 1.08x faster                                                          |
| sqlite_synth               | 2.07 us                                                         | 1.93 us: 1.07x faster                                                          |
| async_generators           | 313 ms                                                          | 293 ms: 1.07x faster                                                           |
| json_dumps                 | 7.40 ms                                                         | 6.97 ms: 1.06x faster                                                          |
| sympy_integrate            | 17.5 ms                                                         | 16.5 ms: 1.06x faster                                                          |
| tornado_http               | 105 ms                                                          | 100 ms: 1.05x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 87.3 ms: 1.05x faster                                                          |
| sympy_sum                  | 123 ms                                                          | 118 ms: 1.04x faster                                                           |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.0 sec: 1.04x faster                                                         |
| python_startup_no_site     | 19.1 ms                                                         | 18.4 ms: 1.04x faster                                                          |
| bench_mp_pool              | 75.4 ms                                                         | 73.1 ms: 1.03x faster                                                          |
| json                       | 4.15 ms                                                         | 4.11 ms: 1.01x faster                                                          |
| regex_compile              | 129 ms                                                          | 128 ms: 1.01x faster                                                           |
| pidigits                   | 199 ms                                                          | 198 ms: 1.01x faster                                                           |
| sympy_str                  | 240 ms                                                          | 237 ms: 1.01x faster                                                           |
| json_loads                 | 20.4 us                                                         | 20.3 us: 1.00x faster                                                          |
| python_startup             | 22.4 ms                                                         | 22.7 ms: 1.02x slower                                                          |
| docutils                   | 1.98 sec                                                        | 2.03 sec: 1.02x slower                                                         |
| coverage                   | 48.4 ms                                                         | 49.7 ms: 1.03x slower                                                          |
| pickle_dict                | 19.9 us                                                         | 20.6 us: 1.04x slower                                                          |
| pickle_list                | 3.37 us                                                         | 3.54 us: 1.05x slower                                                          |
| unpickle                   | 9.71 us                                                         | 10.3 us: 1.06x slower                                                          |
| regex_v8                   | 15.0 ms                                                         | 16.1 ms: 1.07x slower                                                          |
| pickle                     | 7.79 us                                                         | 8.36 us: 1.07x slower                                                          |
| unpickle_list              | 2.95 us                                                         | 3.17 us: 1.08x slower                                                          |
| sympy_expand               | 398 ms                                                          | 428 ms: 1.08x slower                                                           |
| telco                      | 5.51 ms                                                         | 5.93 ms: 1.08x slower                                                          |
| typing_runtime_protocols   | 126 us                                                          | 143 us: 1.13x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 768 us: 1.18x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 226 ms: 2.25x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.15x faster                                                                   |

Benchmark hidden because not significant (1): gc_traversal
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240525-3.14.0a0-e418fc3-PYTHON_UOPS/bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown