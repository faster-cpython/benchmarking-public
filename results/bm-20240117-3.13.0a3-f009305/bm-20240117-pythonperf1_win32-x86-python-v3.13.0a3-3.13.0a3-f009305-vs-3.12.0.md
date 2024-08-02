# Results vs. 3.12.0

- fork: python
- ref: v3.13.0a3
- machine: windows-x86
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.21x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 232 ms: 1.21x faster                                                |
| chameleon      | 7.75 ms                                                         | 5.40 ms: 1.43x faster                                               |
| docutils       | 1.98 sec                                                        | 1.72 sec: 1.16x faster                                              |
| tornado_http   | 105 ms                                                          | 96.3 ms: 1.09x faster                                               |
| Geometric mean | (ref)                                                           | 1.22x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_none            | 298 ms                                                          | 241 ms: 1.23x faster                                                |
| async_tree_none_tg         | 278 ms                                                          | 229 ms: 1.21x faster                                                |
| async_tree_memoization_tg  | 350 ms                                                          | 290 ms: 1.21x faster                                                |
| async_tree_memoization     | 364 ms                                                          | 303 ms: 1.20x faster                                                |
| async_tree_io_tg           | 677 ms                                                          | 571 ms: 1.19x faster                                                |
| async_tree_io              | 693 ms                                                          | 588 ms: 1.18x faster                                                |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 499 ms: 1.13x faster                                                |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 489 ms: 1.12x faster                                                |
| Geometric mean             | (ref)                                                           | 1.18x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 74.0 ms: 1.72x faster                                               |
| float          | 76.7 ms                                                         | 51.1 ms: 1.50x faster                                               |
| Geometric mean | (ref)                                                           | 1.37x faster                                                        |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 92.5 ms: 1.40x faster                                               |
| regex_effbot   | 2.04 ms                                                         | 1.92 ms: 1.06x faster                                               |
| regex_dna      | 127 ms                                                          | 125 ms: 1.02x faster                                                |
| regex_v8       | 15.0 ms                                                         | 16.1 ms: 1.07x slower                                               |
| Geometric mean | (ref)                                                           | 1.09x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 140 us: 1.50x faster                                                |
| pickle_pure_python   | 286 us                                                          | 204 us: 1.40x faster                                                |
| tomli_loads          | 2.20 sec                                                        | 1.62 sec: 1.36x faster                                              |
| xml_etree_process    | 53.2 ms                                                         | 41.1 ms: 1.29x faster                                               |
| xml_etree_generate   | 72.1 ms                                                         | 58.8 ms: 1.23x faster                                               |
| xml_etree_iterparse  | 77.6 ms                                                         | 66.4 ms: 1.17x faster                                               |
| json_dumps           | 7.40 ms                                                         | 6.75 ms: 1.10x faster                                               |
| xml_etree_parse      | 113 ms                                                          | 108 ms: 1.04x faster                                                |
| json_loads           | 20.4 us                                                         | 19.8 us: 1.03x faster                                               |
| pickle_list          | 3.37 us                                                         | 3.33 us: 1.01x faster                                               |
| pickle               | 7.79 us                                                         | 7.71 us: 1.01x faster                                               |
| unpickle_list        | 2.95 us                                                         | 3.08 us: 1.04x slower                                               |
| Geometric mean       | (ref)                                                           | 1.14x faster                                                        |

Benchmark hidden because not significant (2): unpickle, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 22.4 ms                                                         | 22.7 ms: 1.01x slower                                               |
| python_startup_no_site | 19.1 ms                                                         | 20.5 ms: 1.07x slower                                               |
| Geometric mean         | (ref)                                                           | 1.04x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 6.84 ms: 1.45x faster                                               |
| django_template | 36.9 ms                                                         | 29.0 ms: 1.27x faster                                               |
| Geometric mean  | (ref)                                                           | 1.36x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 21.6 us: 1.78x faster                                               |
| logging_silent             | 101 ns                                                          | 57.1 ns: 1.77x faster                                               |
| nbody                      | 127 ms                                                          | 74.0 ms: 1.72x faster                                               |
| comprehensions             | 19.2 us                                                         | 11.2 us: 1.71x faster                                               |
| generators                 | 38.5 ms                                                         | 22.9 ms: 1.68x faster                                               |
| spectral_norm              | 104 ms                                                          | 63.0 ms: 1.65x faster                                               |
| hexiom                     | 6.82 ms                                                         | 4.14 ms: 1.65x faster                                               |
| deltablue                  | 3.58 ms                                                         | 2.18 ms: 1.64x faster                                               |
| scimark_sor                | 130 ms                                                          | 79.6 ms: 1.63x faster                                               |
| raytrace                   | 308 ms                                                          | 191 ms: 1.61x faster                                                |
| scimark_lu                 | 93.2 ms                                                         | 60.2 ms: 1.55x faster                                               |
| chaos                      | 69.4 ms                                                         | 45.5 ms: 1.52x faster                                               |
| float                      | 76.7 ms                                                         | 51.1 ms: 1.50x faster                                               |
| scimark_monte_carlo        | 66.4 ms                                                         | 44.3 ms: 1.50x faster                                               |
| unpickle_pure_python       | 210 us                                                          | 140 us: 1.50x faster                                                |
| richards                   | 41.3 ms                                                         | 27.8 ms: 1.48x faster                                               |
| richards_super             | 46.5 ms                                                         | 31.4 ms: 1.48x faster                                               |
| coroutines                 | 20.9 ms                                                         | 14.2 ms: 1.47x faster                                               |
| sqlglot_parse              | 1.25 ms                                                         | 848 us: 1.47x faster                                                |
| mako                       | 9.96 ms                                                         | 6.84 ms: 1.45x faster                                               |
| deepcopy_reduce            | 3.23 us                                                         | 2.22 us: 1.45x faster                                               |
| go                         | 137 ms                                                          | 95.1 ms: 1.44x faster                                               |
| typing_runtime_protocols   | 126 us                                                          | 87.7 us: 1.44x faster                                               |
| chameleon                  | 7.75 ms                                                         | 5.40 ms: 1.43x faster                                               |
| sqlglot_transpile          | 1.53 ms                                                         | 1.08 ms: 1.42x faster                                               |
| deepcopy                   | 360 us                                                          | 255 us: 1.41x faster                                                |
| pickle_pure_python         | 286 us                                                          | 204 us: 1.40x faster                                                |
| regex_compile              | 129 ms                                                          | 92.5 ms: 1.40x faster                                               |
| pyflate                    | 424 ms                                                          | 306 ms: 1.39x faster                                                |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.79 ms: 1.38x faster                                               |
| scimark_fft                | 271 ms                                                          | 198 ms: 1.37x faster                                                |
| tomli_loads                | 2.20 sec                                                        | 1.62 sec: 1.36x faster                                              |
| crypto_pyaes               | 69.2 ms                                                         | 51.0 ms: 1.36x faster                                               |
| pprint_pformat             | 1.50 sec                                                        | 1.12 sec: 1.34x faster                                              |
| pprint_safe_repr           | 721 ms                                                          | 543 ms: 1.33x faster                                                |
| fannkuch                   | 354 ms                                                          | 267 ms: 1.32x faster                                                |
| xml_etree_process          | 53.2 ms                                                         | 41.1 ms: 1.29x faster                                               |
| nqueens                    | 93.7 ms                                                         | 72.6 ms: 1.29x faster                                               |
| django_template            | 36.9 ms                                                         | 29.0 ms: 1.27x faster                                               |
| logging_simple             | 9.75 us                                                         | 7.69 us: 1.27x faster                                               |
| sqlglot_optimize           | 48.5 ms                                                         | 38.2 ms: 1.27x faster                                               |
| sympy_integrate            | 17.5 ms                                                         | 14.0 ms: 1.25x faster                                               |
| mdp                        | 1.91 sec                                                        | 1.53 sec: 1.25x faster                                              |
| logging_format             | 10.4 us                                                         | 8.33 us: 1.25x faster                                               |
| sympy_sum                  | 123 ms                                                          | 98.5 ms: 1.25x faster                                               |
| async_tree_none            | 298 ms                                                          | 241 ms: 1.23x faster                                                |
| sympy_str                  | 240 ms                                                          | 194 ms: 1.23x faster                                                |
| pycparser                  | 978 ms                                                          | 793 ms: 1.23x faster                                                |
| xml_etree_generate         | 72.1 ms                                                         | 58.8 ms: 1.23x faster                                               |
| async_tree_none_tg         | 278 ms                                                          | 229 ms: 1.21x faster                                                |
| async_tree_memoization_tg  | 350 ms                                                          | 290 ms: 1.21x faster                                                |
| 2to3                       | 280 ms                                                          | 232 ms: 1.21x faster                                                |
| async_tree_memoization     | 364 ms                                                          | 303 ms: 1.20x faster                                                |
| async_tree_io_tg           | 677 ms                                                          | 571 ms: 1.19x faster                                                |
| async_tree_io              | 693 ms                                                          | 588 ms: 1.18x faster                                                |
| meteor_contest             | 86.9 ms                                                         | 73.7 ms: 1.18x faster                                               |
| xml_etree_iterparse        | 77.6 ms                                                         | 66.4 ms: 1.17x faster                                               |
| sympy_expand               | 398 ms                                                          | 343 ms: 1.16x faster                                                |
| docutils                   | 1.98 sec                                                        | 1.72 sec: 1.16x faster                                              |
| async_generators           | 313 ms                                                          | 271 ms: 1.16x faster                                                |
| sqlite_synth               | 2.07 us                                                         | 1.81 us: 1.15x faster                                               |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 499 ms: 1.13x faster                                                |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 489 ms: 1.12x faster                                                |
| json_dumps                 | 7.40 ms                                                         | 6.75 ms: 1.10x faster                                               |
| tornado_http               | 105 ms                                                          | 96.3 ms: 1.09x faster                                               |
| bench_thread_pool          | 1.10 ms                                                         | 1.01 ms: 1.09x faster                                               |
| regex_effbot               | 2.04 ms                                                         | 1.92 ms: 1.06x faster                                               |
| xml_etree_parse            | 113 ms                                                          | 108 ms: 1.04x faster                                                |
| asyncio_tcp                | 662 ms                                                          | 638 ms: 1.04x faster                                                |
| pathlib                    | 91.4 ms                                                         | 88.6 ms: 1.03x faster                                               |
| gc_traversal               | 1.44 ms                                                         | 1.40 ms: 1.03x faster                                               |
| json_loads                 | 20.4 us                                                         | 19.8 us: 1.03x faster                                               |
| regex_dna                  | 127 ms                                                          | 125 ms: 1.02x faster                                                |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.4 sec: 1.02x faster                                              |
| pickle_list                | 3.37 us                                                         | 3.33 us: 1.01x faster                                               |
| pickle                     | 7.79 us                                                         | 7.71 us: 1.01x faster                                               |
| json                       | 4.15 ms                                                         | 4.12 ms: 1.01x faster                                               |
| bench_mp_pool              | 75.4 ms                                                         | 74.9 ms: 1.01x faster                                               |
| python_startup             | 22.4 ms                                                         | 22.7 ms: 1.01x slower                                               |
| telco                      | 5.51 ms                                                         | 5.62 ms: 1.02x slower                                               |
| unpickle_list              | 2.95 us                                                         | 3.08 us: 1.04x slower                                               |
| regex_v8                   | 15.0 ms                                                         | 16.1 ms: 1.07x slower                                               |
| python_startup_no_site     | 19.1 ms                                                         | 20.5 ms: 1.07x slower                                               |
| sqlglot_normalize          | 100 ms                                                          | 197 ms: 1.97x slower                                                |
| coverage                   | 48.4 ms                                                         | 479 ms: 9.88x slower                                                |
| Geometric mean             | (ref)                                                           | 1.21x faster                                                        |

Benchmark hidden because not significant (4): create_gc_cycles, pidigits, unpickle, pickle_dict
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240117-3.13.0a3-f009305/bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: unknown