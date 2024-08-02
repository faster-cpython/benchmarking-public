# Results vs. 3.12.0

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: windows-x86
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.22x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 248 ms: 1.13x faster                                                           |
| chameleon      | 7.75 ms                                                         | 6.16 ms: 1.26x faster                                                          |
| docutils       | 1.98 sec                                                        | 1.88 sec: 1.05x faster                                                         |
| tornado_http   | 105 ms                                                          | 96.9 ms: 1.08x faster                                                          |
| Geometric mean | (ref)                                                           | 1.13x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none_tg         | 278 ms                                                          | 203 ms: 1.37x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 257 ms: 1.37x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 276 ms: 1.32x faster                                                           |
| async_tree_none            | 298 ms                                                          | 226 ms: 1.31x faster                                                           |
| async_tree_io              | 693 ms                                                          | 539 ms: 1.29x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 531 ms: 1.28x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 457 ms: 1.19x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 475 ms: 1.19x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.29x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 52.6 ms: 2.41x faster                                                          |
| float          | 76.7 ms                                                         | 41.8 ms: 1.84x faster                                                          |
| pidigits       | 199 ms                                                          | 195 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                           | 1.65x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 98.3 ms: 1.31x faster                                                          |
| regex_dna      | 127 ms                                                          | 118 ms: 1.08x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.98 ms: 1.03x faster                                                          |
| regex_v8       | 15.0 ms                                                         | 15.9 ms: 1.05x slower                                                          |
| Geometric mean | (ref)                                                           | 1.08x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 135 us: 1.56x faster                                                           |
| tomli_loads          | 2.20 sec                                                        | 1.41 sec: 1.56x faster                                                         |
| pickle_pure_python   | 286 us                                                          | 201 us: 1.42x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 55.7 ms: 1.30x faster                                                          |
| xml_etree_process    | 53.2 ms                                                         | 41.1 ms: 1.29x faster                                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 61.0 ms: 1.27x faster                                                          |
| json_dumps           | 7.40 ms                                                         | 6.76 ms: 1.10x faster                                                          |
| xml_etree_parse      | 113 ms                                                          | 103 ms: 1.09x faster                                                           |
| unpickle_list        | 2.95 us                                                         | 2.88 us: 1.02x faster                                                          |
| json_loads           | 20.4 us                                                         | 20.8 us: 1.02x slower                                                          |
| pickle_dict          | 19.9 us                                                         | 20.5 us: 1.03x slower                                                          |
| pickle               | 7.79 us                                                         | 8.10 us: 1.04x slower                                                          |
| unpickle             | 9.71 us                                                         | 10.3 us: 1.06x slower                                                          |
| pickle_list          | 3.37 us                                                         | 3.57 us: 1.06x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.15x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.5 ms: 1.08x slower                                                          |
| python_startup         | 22.4 ms                                                         | 24.8 ms: 1.11x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.29 ms: 1.88x faster                                                          |
| django_template | 36.9 ms                                                         | 32.3 ms: 1.14x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.47x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody                      | 127 ms                                                          | 52.6 ms: 2.41x faster                                                          |
| spectral_norm              | 104 ms                                                          | 47.6 ms: 2.18x faster                                                          |
| mako                       | 9.96 ms                                                         | 5.29 ms: 1.88x faster                                                          |
| deepcopy_memo              | 38.4 us                                                         | 20.6 us: 1.86x faster                                                          |
| float                      | 76.7 ms                                                         | 41.8 ms: 1.84x faster                                                          |
| logging_silent             | 101 ns                                                          | 57.3 ns: 1.76x faster                                                          |
| comprehensions             | 19.2 us                                                         | 11.1 us: 1.74x faster                                                          |
| generators                 | 38.5 ms                                                         | 23.4 ms: 1.64x faster                                                          |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.36 ms: 1.64x faster                                                          |
| scimark_monte_carlo        | 66.4 ms                                                         | 40.9 ms: 1.62x faster                                                          |
| fannkuch                   | 354 ms                                                          | 225 ms: 1.57x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 135 us: 1.56x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.41 sec: 1.56x faster                                                         |
| hexiom                     | 6.82 ms                                                         | 4.58 ms: 1.49x faster                                                          |
| scimark_fft                | 271 ms                                                          | 185 ms: 1.47x faster                                                           |
| raytrace                   | 308 ms                                                          | 211 ms: 1.46x faster                                                           |
| scimark_sor                | 130 ms                                                          | 90.3 ms: 1.44x faster                                                          |
| pickle_pure_python         | 286 us                                                          | 201 us: 1.42x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.57 ms: 1.40x faster                                                          |
| crypto_pyaes               | 69.2 ms                                                         | 49.7 ms: 1.39x faster                                                          |
| sqlglot_parse              | 1.25 ms                                                         | 908 us: 1.37x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 203 ms: 1.37x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 257 ms: 1.37x faster                                                           |
| pyflate                    | 424 ms                                                          | 313 ms: 1.36x faster                                                           |
| chaos                      | 69.4 ms                                                         | 51.4 ms: 1.35x faster                                                          |
| nqueens                    | 93.7 ms                                                         | 69.6 ms: 1.35x faster                                                          |
| logging_simple             | 9.75 us                                                         | 7.35 us: 1.33x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 276 ms: 1.32x faster                                                           |
| async_tree_none            | 298 ms                                                          | 226 ms: 1.31x faster                                                           |
| regex_compile              | 129 ms                                                          | 98.3 ms: 1.31x faster                                                          |
| logging_format             | 10.4 us                                                         | 7.93 us: 1.31x faster                                                          |
| sqlglot_transpile          | 1.53 ms                                                         | 1.17 ms: 1.31x faster                                                          |
| pprint_pformat             | 1.50 sec                                                        | 1.15 sec: 1.30x faster                                                         |
| xml_etree_generate         | 72.1 ms                                                         | 55.7 ms: 1.30x faster                                                          |
| richards_super             | 46.5 ms                                                         | 35.9 ms: 1.30x faster                                                          |
| richards                   | 41.3 ms                                                         | 31.9 ms: 1.29x faster                                                          |
| xml_etree_process          | 53.2 ms                                                         | 41.1 ms: 1.29x faster                                                          |
| scimark_lu                 | 93.2 ms                                                         | 72.1 ms: 1.29x faster                                                          |
| coroutines                 | 20.9 ms                                                         | 16.2 ms: 1.29x faster                                                          |
| async_tree_io              | 693 ms                                                          | 539 ms: 1.29x faster                                                           |
| pprint_safe_repr           | 721 ms                                                          | 562 ms: 1.28x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 531 ms: 1.28x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 61.0 ms: 1.27x faster                                                          |
| chameleon                  | 7.75 ms                                                         | 6.16 ms: 1.26x faster                                                          |
| go                         | 137 ms                                                          | 113 ms: 1.21x faster                                                           |
| pycparser                  | 978 ms                                                          | 811 ms: 1.21x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 457 ms: 1.19x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 72.9 ms: 1.19x faster                                                          |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 475 ms: 1.19x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.63 sec: 1.17x faster                                                         |
| deepcopy                   | 360 us                                                          | 310 us: 1.16x faster                                                           |
| django_template            | 36.9 ms                                                         | 32.3 ms: 1.14x faster                                                          |
| sqlglot_optimize           | 48.5 ms                                                         | 42.5 ms: 1.14x faster                                                          |
| sympy_sum                  | 123 ms                                                          | 108 ms: 1.14x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.84 us: 1.13x faster                                                          |
| sympy_str                  | 240 ms                                                          | 212 ms: 1.13x faster                                                           |
| 2to3                       | 280 ms                                                          | 248 ms: 1.13x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 981 us: 1.12x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 15.6 ms: 1.12x faster                                                          |
| sqlite_synth               | 2.07 us                                                         | 1.87 us: 1.11x faster                                                          |
| json_dumps                 | 7.40 ms                                                         | 6.76 ms: 1.10x faster                                                          |
| xml_etree_parse            | 113 ms                                                          | 103 ms: 1.09x faster                                                           |
| asyncio_tcp                | 662 ms                                                          | 608 ms: 1.09x faster                                                           |
| tornado_http               | 105 ms                                                          | 96.9 ms: 1.08x faster                                                          |
| regex_dna                  | 127 ms                                                          | 118 ms: 1.08x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 86.4 ms: 1.06x faster                                                          |
| async_generators           | 313 ms                                                          | 296 ms: 1.06x faster                                                           |
| docutils                   | 1.98 sec                                                        | 1.88 sec: 1.05x faster                                                         |
| sympy_expand               | 398 ms                                                          | 379 ms: 1.05x faster                                                           |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.9 sec: 1.05x faster                                                         |
| regex_effbot               | 2.04 ms                                                         | 1.98 ms: 1.03x faster                                                          |
| unpickle_list              | 2.95 us                                                         | 2.88 us: 1.02x faster                                                          |
| pidigits                   | 199 ms                                                          | 195 ms: 1.02x faster                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.47 ms: 1.02x slower                                                          |
| json_loads                 | 20.4 us                                                         | 20.8 us: 1.02x slower                                                          |
| coverage                   | 48.4 ms                                                         | 49.9 ms: 1.03x slower                                                          |
| pickle_dict                | 19.9 us                                                         | 20.5 us: 1.03x slower                                                          |
| pickle                     | 7.79 us                                                         | 8.10 us: 1.04x slower                                                          |
| regex_v8                   | 15.0 ms                                                         | 15.9 ms: 1.05x slower                                                          |
| unpickle                   | 9.71 us                                                         | 10.3 us: 1.06x slower                                                          |
| pickle_list                | 3.37 us                                                         | 3.57 us: 1.06x slower                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 20.5 ms: 1.08x slower                                                          |
| typing_runtime_protocols   | 126 us                                                          | 137 us: 1.09x slower                                                           |
| python_startup             | 22.4 ms                                                         | 24.8 ms: 1.11x slower                                                          |
| create_gc_cycles           | 652 us                                                          | 765 us: 1.17x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 222 ms: 2.22x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.22x faster                                                                   |

Benchmark hidden because not significant (3): telco, bench_mp_pool, json
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: unknown