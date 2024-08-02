# Results vs. 3.12.0

- fork: python
- ref: 6b10467fbc0b67bf217e
- machine: windows-x86
- commit hash: 6b10467
- commit date: 2024-06-03
- overall geometric mean: 1.19x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240603-pythonperf1_win32-x86-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 230 ms: 1.22x faster                                                            |
| chameleon      | 7.75 ms                                                         | 5.70 ms: 1.36x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.81 sec: 1.10x faster                                                          |
| tornado_http   | 105 ms                                                          | 94.1 ms: 1.12x faster                                                           |
| Geometric mean | (ref)                                                           | 1.19x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240603-pythonperf1_win32-x86-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg         | 278 ms                                                          | 201 ms: 1.38x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 254 ms: 1.38x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 273 ms: 1.33x faster                                                            |
| async_tree_none            | 298 ms                                                          | 224 ms: 1.33x faster                                                            |
| async_tree_io              | 693 ms                                                          | 529 ms: 1.31x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 525 ms: 1.29x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 468 ms: 1.17x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 486 ms: 1.16x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.29x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240603-pythonperf1_win32-x86-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 75.9 ms: 1.67x faster                                                           |
| float          | 76.7 ms                                                         | 52.8 ms: 1.45x faster                                                           |
| pidigits       | 199 ms                                                          | 196 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                           | 1.35x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240603-pythonperf1_win32-x86-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 97.2 ms: 1.33x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.88 ms: 1.09x faster                                                           |
| regex_dna      | 127 ms                                                          | 119 ms: 1.06x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 15.8 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                           | 1.10x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240603-pythonperf1_win32-x86-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 147 us: 1.42x faster                                                            |
| tomli_loads          | 2.20 sec                                                        | 1.58 sec: 1.39x faster                                                          |
| pickle_pure_python   | 286 us                                                          | 221 us: 1.29x faster                                                            |
| xml_etree_process    | 53.2 ms                                                         | 41.6 ms: 1.28x faster                                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 63.4 ms: 1.23x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 59.1 ms: 1.22x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 103 ms: 1.10x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 6.84 ms: 1.08x faster                                                           |
| unpickle_list        | 2.95 us                                                         | 2.88 us: 1.02x faster                                                           |
| pickle               | 7.79 us                                                         | 7.95 us: 1.02x slower                                                           |
| json_loads           | 20.4 us                                                         | 20.8 us: 1.02x slower                                                           |
| pickle_dict          | 19.9 us                                                         | 20.6 us: 1.04x slower                                                           |
| unpickle             | 9.71 us                                                         | 10.1 us: 1.04x slower                                                           |
| pickle_list          | 3.37 us                                                         | 3.54 us: 1.05x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.12x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240603-pythonperf1_win32-x86-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 18.3 ms: 1.04x faster                                                           |
| Geometric mean         | (ref)                                                           | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240603-pythonperf1_win32-x86-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 6.95 ms: 1.43x faster                                                           |
| django_template | 36.9 ms                                                         | 29.1 ms: 1.27x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.35x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240603-pythonperf1_win32-x86-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| generators                 | 38.5 ms                                                         | 21.4 ms: 1.80x faster                                                           |
| logging_silent             | 101 ns                                                          | 58.1 ns: 1.74x faster                                                           |
| nbody                      | 127 ms                                                          | 75.9 ms: 1.67x faster                                                           |
| raytrace                   | 308 ms                                                          | 186 ms: 1.66x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 2.22 ms: 1.61x faster                                                           |
| deepcopy_memo              | 38.4 us                                                         | 23.8 us: 1.61x faster                                                           |
| comprehensions             | 19.2 us                                                         | 12.1 us: 1.58x faster                                                           |
| spectral_norm              | 104 ms                                                          | 66.6 ms: 1.56x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 4.38 ms: 1.56x faster                                                           |
| scimark_sor                | 130 ms                                                          | 84.1 ms: 1.54x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 61.7 ms: 1.51x faster                                                           |
| chaos                      | 69.4 ms                                                         | 47.1 ms: 1.47x faster                                                           |
| float                      | 76.7 ms                                                         | 52.8 ms: 1.45x faster                                                           |
| mako                       | 9.96 ms                                                         | 6.95 ms: 1.43x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 147 us: 1.42x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 47.5 ms: 1.40x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.58 sec: 1.39x faster                                                          |
| async_tree_none_tg         | 278 ms                                                          | 201 ms: 1.38x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 254 ms: 1.38x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 68.1 ms: 1.37x faster                                                           |
| pyflate                    | 424 ms                                                          | 308 ms: 1.37x faster                                                            |
| chameleon                  | 7.75 ms                                                         | 5.70 ms: 1.36x faster                                                           |
| go                         | 137 ms                                                          | 102 ms: 1.35x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 15.5 ms: 1.35x faster                                                           |
| logging_simple             | 9.75 us                                                         | 7.31 us: 1.33x faster                                                           |
| richards                   | 41.3 ms                                                         | 31.0 ms: 1.33x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 273 ms: 1.33x faster                                                            |
| async_tree_none            | 298 ms                                                          | 224 ms: 1.33x faster                                                            |
| regex_compile              | 129 ms                                                          | 97.2 ms: 1.33x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 940 us: 1.33x faster                                                            |
| richards_super             | 46.5 ms                                                         | 35.0 ms: 1.33x faster                                                           |
| logging_format             | 10.4 us                                                         | 7.93 us: 1.31x faster                                                           |
| async_tree_io              | 693 ms                                                          | 529 ms: 1.31x faster                                                            |
| sqlglot_transpile          | 1.53 ms                                                         | 1.17 ms: 1.31x faster                                                           |
| scimark_fft                | 271 ms                                                          | 207 ms: 1.31x faster                                                            |
| deepcopy                   | 360 us                                                          | 278 us: 1.29x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.98 ms: 1.29x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 221 us: 1.29x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 525 ms: 1.29x faster                                                            |
| fannkuch                   | 354 ms                                                          | 274 ms: 1.29x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 41.6 ms: 1.28x faster                                                           |
| django_template            | 36.9 ms                                                         | 29.1 ms: 1.27x faster                                                           |
| pycparser                  | 978 ms                                                          | 776 ms: 1.26x faster                                                            |
| pprint_pformat             | 1.50 sec                                                        | 1.19 sec: 1.26x faster                                                          |
| crypto_pyaes               | 69.2 ms                                                         | 55.6 ms: 1.25x faster                                                           |
| pprint_safe_repr           | 721 ms                                                          | 583 ms: 1.24x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 63.4 ms: 1.23x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 59.1 ms: 1.22x faster                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 39.7 ms: 1.22x faster                                                           |
| 2to3                       | 280 ms                                                          | 230 ms: 1.22x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 2.66 us: 1.21x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 14.5 ms: 1.21x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 104 ms: 1.19x faster                                                            |
| mdp                        | 1.91 sec                                                        | 1.63 sec: 1.17x faster                                                          |
| meteor_contest             | 86.9 ms                                                         | 74.4 ms: 1.17x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 468 ms: 1.17x faster                                                            |
| async_generators           | 313 ms                                                          | 269 ms: 1.16x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 486 ms: 1.16x faster                                                            |
| sympy_str                  | 240 ms                                                          | 207 ms: 1.16x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 982 us: 1.12x faster                                                            |
| tornado_http               | 105 ms                                                          | 94.1 ms: 1.12x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 103 ms: 1.10x faster                                                            |
| pathlib                    | 91.4 ms                                                         | 83.1 ms: 1.10x faster                                                           |
| sympy_expand               | 398 ms                                                          | 363 ms: 1.10x faster                                                            |
| docutils                   | 1.98 sec                                                        | 1.81 sec: 1.10x faster                                                          |
| bench_mp_pool              | 75.4 ms                                                         | 69.1 ms: 1.09x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.88 ms: 1.09x faster                                                           |
| json_dumps                 | 7.40 ms                                                         | 6.84 ms: 1.08x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.93 us: 1.08x faster                                                           |
| regex_dna                  | 127 ms                                                          | 119 ms: 1.06x faster                                                            |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.9 sec: 1.05x faster                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 18.3 ms: 1.04x faster                                                           |
| unpickle_list              | 2.95 us                                                         | 2.88 us: 1.02x faster                                                           |
| pidigits                   | 199 ms                                                          | 196 ms: 1.02x faster                                                            |
| json                       | 4.15 ms                                                         | 4.11 ms: 1.01x faster                                                           |
| pickle                     | 7.79 us                                                         | 7.95 us: 1.02x slower                                                           |
| json_loads                 | 20.4 us                                                         | 20.8 us: 1.02x slower                                                           |
| pickle_dict                | 19.9 us                                                         | 20.6 us: 1.04x slower                                                           |
| unpickle                   | 9.71 us                                                         | 10.1 us: 1.04x slower                                                           |
| telco                      | 5.51 ms                                                         | 5.75 ms: 1.04x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 15.8 ms: 1.05x slower                                                           |
| pickle_list                | 3.37 us                                                         | 3.54 us: 1.05x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 135 us: 1.07x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 756 us: 1.16x slower                                                            |
| sqlglot_normalize          | 100 ms                                                          | 209 ms: 2.08x slower                                                            |
| coverage                   | 48.4 ms                                                         | 308 ms: 6.36x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.19x faster                                                                    |

Benchmark hidden because not significant (3): gc_traversal, python_startup, asyncio_tcp
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240603-3.13.0b1+-6b10467/bm-20240603-pythonperf1_win32-x86-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: unknown