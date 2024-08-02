# Results vs. 3.12.0

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: windows-x86
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.21x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 233 ms: 1.20x faster                                                           |
| chameleon      | 7.75 ms                                                         | 5.72 ms: 1.35x faster                                                          |
| docutils       | 1.98 sec                                                        | 1.81 sec: 1.09x faster                                                         |
| tornado_http   | 105 ms                                                          | 94.8 ms: 1.11x faster                                                          |
| Geometric mean | (ref)                                                           | 1.18x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 257 ms: 1.36x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 204 ms: 1.36x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 276 ms: 1.32x faster                                                           |
| async_tree_io              | 693 ms                                                          | 528 ms: 1.31x faster                                                           |
| async_tree_none            | 298 ms                                                          | 227 ms: 1.31x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 534 ms: 1.27x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 453 ms: 1.20x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 476 ms: 1.18x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.29x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 76.4 ms: 1.66x faster                                                          |
| float          | 76.7 ms                                                         | 52.6 ms: 1.46x faster                                                          |
| Geometric mean | (ref)                                                           | 1.34x faster                                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 98.9 ms: 1.31x faster                                                          |
| regex_dna      | 127 ms                                                          | 116 ms: 1.10x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.89 ms: 1.08x faster                                                          |
| regex_v8       | 15.0 ms                                                         | 15.9 ms: 1.06x slower                                                          |
| Geometric mean | (ref)                                                           | 1.10x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 148 us: 1.41x faster                                                           |
| tomli_loads          | 2.20 sec                                                        | 1.60 sec: 1.37x faster                                                         |
| pickle_pure_python   | 286 us                                                          | 221 us: 1.29x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 42.9 ms: 1.24x faster                                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 63.8 ms: 1.22x faster                                                          |
| xml_etree_generate   | 72.1 ms                                                         | 60.0 ms: 1.20x faster                                                          |
| xml_etree_parse      | 113 ms                                                          | 105 ms: 1.07x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 6.95 ms: 1.06x faster                                                          |
| unpickle_list        | 2.95 us                                                         | 2.97 us: 1.01x slower                                                          |
| json_loads           | 20.4 us                                                         | 20.9 us: 1.03x slower                                                          |
| pickle               | 7.79 us                                                         | 8.15 us: 1.05x slower                                                          |
| pickle_dict          | 19.9 us                                                         | 20.9 us: 1.05x slower                                                          |
| unpickle             | 9.71 us                                                         | 10.4 us: 1.07x slower                                                          |
| pickle_list          | 3.37 us                                                         | 3.63 us: 1.08x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.10x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 18.6 ms: 1.03x faster                                                          |
| python_startup         | 22.4 ms                                                         | 22.8 ms: 1.02x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.00x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 6.94 ms: 1.44x faster                                                          |
| django_template | 36.9 ms                                                         | 30.4 ms: 1.21x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.32x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| generators                 | 38.5 ms                                                         | 21.5 ms: 1.79x faster                                                          |
| logging_silent             | 101 ns                                                          | 57.7 ns: 1.75x faster                                                          |
| nbody                      | 127 ms                                                          | 76.4 ms: 1.66x faster                                                          |
| raytrace                   | 308 ms                                                          | 185 ms: 1.66x faster                                                           |
| deepcopy_memo              | 38.4 us                                                         | 23.5 us: 1.63x faster                                                          |
| comprehensions             | 19.2 us                                                         | 11.9 us: 1.61x faster                                                          |
| scimark_lu                 | 93.2 ms                                                         | 58.3 ms: 1.60x faster                                                          |
| deltablue                  | 3.58 ms                                                         | 2.26 ms: 1.59x faster                                                          |
| hexiom                     | 6.82 ms                                                         | 4.33 ms: 1.57x faster                                                          |
| spectral_norm              | 104 ms                                                          | 66.2 ms: 1.57x faster                                                          |
| scimark_sor                | 130 ms                                                          | 85.0 ms: 1.53x faster                                                          |
| chaos                      | 69.4 ms                                                         | 46.7 ms: 1.49x faster                                                          |
| float                      | 76.7 ms                                                         | 52.6 ms: 1.46x faster                                                          |
| mako                       | 9.96 ms                                                         | 6.94 ms: 1.44x faster                                                          |
| scimark_monte_carlo        | 66.4 ms                                                         | 46.3 ms: 1.43x faster                                                          |
| unpickle_pure_python       | 210 us                                                          | 148 us: 1.41x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 66.5 ms: 1.41x faster                                                          |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.80 ms: 1.38x faster                                                          |
| tomli_loads                | 2.20 sec                                                        | 1.60 sec: 1.37x faster                                                         |
| async_tree_memoization_tg  | 350 ms                                                          | 257 ms: 1.36x faster                                                           |
| pyflate                    | 424 ms                                                          | 311 ms: 1.36x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 204 ms: 1.36x faster                                                           |
| richards_super             | 46.5 ms                                                         | 34.2 ms: 1.36x faster                                                          |
| chameleon                  | 7.75 ms                                                         | 5.72 ms: 1.35x faster                                                          |
| richards                   | 41.3 ms                                                         | 30.5 ms: 1.35x faster                                                          |
| scimark_fft                | 271 ms                                                          | 203 ms: 1.33x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 276 ms: 1.32x faster                                                           |
| go                         | 137 ms                                                          | 104 ms: 1.32x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 15.9 ms: 1.32x faster                                                          |
| fannkuch                   | 354 ms                                                          | 269 ms: 1.31x faster                                                           |
| async_tree_io              | 693 ms                                                          | 528 ms: 1.31x faster                                                           |
| async_tree_none            | 298 ms                                                          | 227 ms: 1.31x faster                                                           |
| logging_simple             | 9.75 us                                                         | 7.47 us: 1.31x faster                                                          |
| regex_compile              | 129 ms                                                          | 98.9 ms: 1.31x faster                                                          |
| sqlglot_parse              | 1.25 ms                                                         | 965 us: 1.29x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 221 us: 1.29x faster                                                           |
| sqlglot_transpile          | 1.53 ms                                                         | 1.19 ms: 1.29x faster                                                          |
| crypto_pyaes               | 69.2 ms                                                         | 54.4 ms: 1.27x faster                                                          |
| deepcopy                   | 360 us                                                          | 283 us: 1.27x faster                                                           |
| logging_format             | 10.4 us                                                         | 8.19 us: 1.27x faster                                                          |
| async_tree_io_tg           | 677 ms                                                          | 534 ms: 1.27x faster                                                           |
| pycparser                  | 978 ms                                                          | 788 ms: 1.24x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 42.9 ms: 1.24x faster                                                          |
| sqlglot_optimize           | 48.5 ms                                                         | 39.6 ms: 1.22x faster                                                          |
| xml_etree_iterparse        | 77.6 ms                                                         | 63.8 ms: 1.22x faster                                                          |
| django_template            | 36.9 ms                                                         | 30.4 ms: 1.21x faster                                                          |
| deepcopy_reduce            | 3.23 us                                                         | 2.66 us: 1.21x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 453 ms: 1.20x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 14.6 ms: 1.20x faster                                                          |
| xml_etree_generate         | 72.1 ms                                                         | 60.0 ms: 1.20x faster                                                          |
| pprint_pformat             | 1.50 sec                                                        | 1.25 sec: 1.20x faster                                                         |
| 2to3                       | 280 ms                                                          | 233 ms: 1.20x faster                                                           |
| pprint_safe_repr           | 721 ms                                                          | 607 ms: 1.19x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 104 ms: 1.19x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 476 ms: 1.18x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.63 sec: 1.17x faster                                                         |
| meteor_contest             | 86.9 ms                                                         | 74.4 ms: 1.17x faster                                                          |
| sympy_str                  | 240 ms                                                          | 206 ms: 1.16x faster                                                           |
| async_generators           | 313 ms                                                          | 271 ms: 1.15x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 975 us: 1.13x faster                                                           |
| tornado_http               | 105 ms                                                          | 94.8 ms: 1.11x faster                                                          |
| sympy_expand               | 398 ms                                                          | 361 ms: 1.10x faster                                                           |
| regex_dna                  | 127 ms                                                          | 116 ms: 1.10x faster                                                           |
| docutils                   | 1.98 sec                                                        | 1.81 sec: 1.09x faster                                                         |
| regex_effbot               | 2.04 ms                                                         | 1.89 ms: 1.08x faster                                                          |
| xml_etree_parse            | 113 ms                                                          | 105 ms: 1.07x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.94 us: 1.07x faster                                                          |
| json_dumps                 | 7.40 ms                                                         | 6.95 ms: 1.06x faster                                                          |
| bench_mp_pool              | 75.4 ms                                                         | 71.2 ms: 1.06x faster                                                          |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.9 sec: 1.05x faster                                                         |
| pathlib                    | 91.4 ms                                                         | 87.5 ms: 1.04x faster                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 18.6 ms: 1.03x faster                                                          |
| unpickle_list              | 2.95 us                                                         | 2.97 us: 1.01x slower                                                          |
| python_startup             | 22.4 ms                                                         | 22.8 ms: 1.02x slower                                                          |
| json_loads                 | 20.4 us                                                         | 20.9 us: 1.03x slower                                                          |
| json                       | 4.15 ms                                                         | 4.27 ms: 1.03x slower                                                          |
| pickle                     | 7.79 us                                                         | 8.15 us: 1.05x slower                                                          |
| pickle_dict                | 19.9 us                                                         | 20.9 us: 1.05x slower                                                          |
| typing_runtime_protocols   | 126 us                                                          | 133 us: 1.05x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 15.9 ms: 1.06x slower                                                          |
| unpickle                   | 9.71 us                                                         | 10.4 us: 1.07x slower                                                          |
| pickle_list                | 3.37 us                                                         | 3.63 us: 1.08x slower                                                          |
| telco                      | 5.51 ms                                                         | 6.20 ms: 1.13x slower                                                          |
| create_gc_cycles           | 652 us                                                          | 750 us: 1.15x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 204 ms: 2.03x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.21x faster                                                                   |

Benchmark hidden because not significant (4): pidigits, coverage, gc_traversal, asyncio_tcp
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: unknown