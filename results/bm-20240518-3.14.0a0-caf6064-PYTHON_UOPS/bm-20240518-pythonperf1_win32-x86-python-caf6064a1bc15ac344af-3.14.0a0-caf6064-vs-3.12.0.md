# Results vs. 3.12.0

- fork: python
- ref: caf6064a1bc15ac344af
- machine: windows-x86
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.11x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 257 ms: 1.09x faster                                                           |
| chameleon      | 7.75 ms                                                         | 6.62 ms: 1.17x faster                                                          |
| docutils       | 1.98 sec                                                        | 2.02 sec: 1.02x slower                                                         |
| tornado_http   | 105 ms                                                          | 99.4 ms: 1.06x faster                                                          |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 263 ms: 1.33x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 210 ms: 1.32x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 284 ms: 1.28x faster                                                           |
| async_tree_io              | 693 ms                                                          | 545 ms: 1.27x faster                                                           |
| async_tree_none            | 298 ms                                                          | 236 ms: 1.26x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 544 ms: 1.24x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 468 ms: 1.17x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 498 ms: 1.13x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.25x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 80.5 ms: 1.58x faster                                                          |
| float          | 76.7 ms                                                         | 56.6 ms: 1.35x faster                                                          |
| pidigits       | 199 ms                                                          | 198 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                           | 1.29x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.92 ms: 1.06x faster                                                          |
| regex_compile  | 129 ms                                                          | 127 ms: 1.02x faster                                                           |
| regex_dna      | 127 ms                                                          | 125 ms: 1.01x faster                                                           |
| regex_v8       | 15.0 ms                                                         | 16.2 ms: 1.08x slower                                                          |
| Geometric mean | (ref)                                                           | 1.00x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.67 sec: 1.31x faster                                                         |
| xml_etree_process    | 53.2 ms                                                         | 44.6 ms: 1.19x faster                                                          |
| xml_etree_generate   | 72.1 ms                                                         | 61.5 ms: 1.17x faster                                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 66.9 ms: 1.16x faster                                                          |
| unpickle_pure_python | 210 us                                                          | 181 us: 1.16x faster                                                           |
| pickle_pure_python   | 286 us                                                          | 254 us: 1.12x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 104 ms: 1.09x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 7.00 ms: 1.06x faster                                                          |
| json_loads           | 20.4 us                                                         | 20.7 us: 1.02x slower                                                          |
| pickle_dict          | 19.9 us                                                         | 20.6 us: 1.03x slower                                                          |
| pickle               | 7.79 us                                                         | 8.10 us: 1.04x slower                                                          |
| unpickle             | 9.71 us                                                         | 10.2 us: 1.06x slower                                                          |
| unpickle_list        | 2.95 us                                                         | 3.11 us: 1.06x slower                                                          |
| pickle_list          | 3.37 us                                                         | 3.59 us: 1.06x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.07x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 18.7 ms: 1.02x faster                                                          |
| python_startup         | 22.4 ms                                                         | 22.2 ms: 1.01x faster                                                          |
| Geometric mean         | (ref)                                                           | 1.02x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.84 ms: 1.27x faster                                                          |
| django_template | 36.9 ms                                                         | 33.6 ms: 1.10x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.18x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| generators                 | 38.5 ms                                                         | 23.7 ms: 1.62x faster                                                          |
| nbody                      | 127 ms                                                          | 80.5 ms: 1.58x faster                                                          |
| raytrace                   | 308 ms                                                          | 214 ms: 1.44x faster                                                           |
| float                      | 76.7 ms                                                         | 56.6 ms: 1.35x faster                                                          |
| async_tree_memoization_tg  | 350 ms                                                          | 263 ms: 1.33x faster                                                           |
| scimark_sor                | 130 ms                                                          | 97.7 ms: 1.33x faster                                                          |
| comprehensions             | 19.2 us                                                         | 14.5 us: 1.33x faster                                                          |
| spectral_norm              | 104 ms                                                          | 78.4 ms: 1.32x faster                                                          |
| async_tree_none_tg         | 278 ms                                                          | 210 ms: 1.32x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.67 sec: 1.31x faster                                                         |
| coroutines                 | 20.9 ms                                                         | 16.3 ms: 1.28x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 284 ms: 1.28x faster                                                           |
| chaos                      | 69.4 ms                                                         | 54.3 ms: 1.28x faster                                                          |
| scimark_fft                | 271 ms                                                          | 212 ms: 1.28x faster                                                           |
| async_tree_io              | 693 ms                                                          | 545 ms: 1.27x faster                                                           |
| mako                       | 9.96 ms                                                         | 7.84 ms: 1.27x faster                                                          |
| logging_simple             | 9.75 us                                                         | 7.71 us: 1.26x faster                                                          |
| async_tree_none            | 298 ms                                                          | 236 ms: 1.26x faster                                                           |
| logging_silent             | 101 ns                                                          | 80.1 ns: 1.26x faster                                                          |
| richards                   | 41.3 ms                                                         | 32.9 ms: 1.26x faster                                                          |
| deepcopy_memo              | 38.4 us                                                         | 30.7 us: 1.25x faster                                                          |
| logging_format             | 10.4 us                                                         | 8.34 us: 1.25x faster                                                          |
| richards_super             | 46.5 ms                                                         | 37.3 ms: 1.25x faster                                                          |
| async_tree_io_tg           | 677 ms                                                          | 544 ms: 1.24x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.96 ms: 1.21x faster                                                          |
| fannkuch                   | 354 ms                                                          | 294 ms: 1.20x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 55.3 ms: 1.20x faster                                                          |
| sqlglot_parse              | 1.25 ms                                                         | 1.04 ms: 1.20x faster                                                          |
| xml_etree_process          | 53.2 ms                                                         | 44.6 ms: 1.19x faster                                                          |
| nqueens                    | 93.7 ms                                                         | 79.1 ms: 1.18x faster                                                          |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.26 ms: 1.18x faster                                                          |
| sqlglot_transpile          | 1.53 ms                                                         | 1.30 ms: 1.18x faster                                                          |
| xml_etree_generate         | 72.1 ms                                                         | 61.5 ms: 1.17x faster                                                          |
| chameleon                  | 7.75 ms                                                         | 6.62 ms: 1.17x faster                                                          |
| crypto_pyaes               | 69.2 ms                                                         | 59.3 ms: 1.17x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 468 ms: 1.17x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 66.9 ms: 1.16x faster                                                          |
| unpickle_pure_python       | 210 us                                                          | 181 us: 1.16x faster                                                           |
| go                         | 137 ms                                                          | 119 ms: 1.15x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.81 us: 1.15x faster                                                          |
| deepcopy                   | 360 us                                                          | 314 us: 1.15x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.68 sec: 1.14x faster                                                         |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 498 ms: 1.13x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 254 us: 1.12x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 83.0 ms: 1.12x faster                                                          |
| pprint_pformat             | 1.50 sec                                                        | 1.34 sec: 1.12x faster                                                         |
| pycparser                  | 978 ms                                                          | 878 ms: 1.11x faster                                                           |
| pprint_safe_repr           | 721 ms                                                          | 651 ms: 1.11x faster                                                           |
| pyflate                    | 424 ms                                                          | 385 ms: 1.10x faster                                                           |
| django_template            | 36.9 ms                                                         | 33.6 ms: 1.10x faster                                                          |
| bench_thread_pool          | 1.10 ms                                                         | 1.01 ms: 1.10x faster                                                          |
| hexiom                     | 6.82 ms                                                         | 6.23 ms: 1.10x faster                                                          |
| sqlite_synth               | 2.07 us                                                         | 1.90 us: 1.09x faster                                                          |
| 2to3                       | 280 ms                                                          | 257 ms: 1.09x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 104 ms: 1.09x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 80.2 ms: 1.08x faster                                                          |
| sqlglot_optimize           | 48.5 ms                                                         | 44.8 ms: 1.08x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 86.0 ms: 1.06x faster                                                          |
| regex_effbot               | 2.04 ms                                                         | 1.92 ms: 1.06x faster                                                          |
| json_dumps                 | 7.40 ms                                                         | 7.00 ms: 1.06x faster                                                          |
| tornado_http               | 105 ms                                                          | 99.4 ms: 1.06x faster                                                          |
| sympy_integrate            | 17.5 ms                                                         | 16.7 ms: 1.05x faster                                                          |
| bench_mp_pool              | 75.4 ms                                                         | 72.1 ms: 1.05x faster                                                          |
| asyncio_tcp                | 662 ms                                                          | 634 ms: 1.04x faster                                                           |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.0 sec: 1.04x faster                                                         |
| sympy_sum                  | 123 ms                                                          | 118 ms: 1.04x faster                                                           |
| async_generators           | 313 ms                                                          | 306 ms: 1.02x faster                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 18.7 ms: 1.02x faster                                                          |
| regex_compile              | 129 ms                                                          | 127 ms: 1.02x faster                                                           |
| regex_dna                  | 127 ms                                                          | 125 ms: 1.01x faster                                                           |
| python_startup             | 22.4 ms                                                         | 22.2 ms: 1.01x faster                                                          |
| pidigits                   | 199 ms                                                          | 198 ms: 1.01x faster                                                           |
| sympy_str                  | 240 ms                                                          | 239 ms: 1.00x faster                                                           |
| coverage                   | 48.4 ms                                                         | 48.9 ms: 1.01x slower                                                          |
| gc_traversal               | 1.44 ms                                                         | 1.46 ms: 1.02x slower                                                          |
| docutils                   | 1.98 sec                                                        | 2.02 sec: 1.02x slower                                                         |
| json_loads                 | 20.4 us                                                         | 20.7 us: 1.02x slower                                                          |
| pickle_dict                | 19.9 us                                                         | 20.6 us: 1.03x slower                                                          |
| pickle                     | 7.79 us                                                         | 8.10 us: 1.04x slower                                                          |
| unpickle                   | 9.71 us                                                         | 10.2 us: 1.06x slower                                                          |
| unpickle_list              | 2.95 us                                                         | 3.11 us: 1.06x slower                                                          |
| sympy_expand               | 398 ms                                                          | 421 ms: 1.06x slower                                                           |
| pickle_list                | 3.37 us                                                         | 3.59 us: 1.06x slower                                                          |
| regex_v8                   | 15.0 ms                                                         | 16.2 ms: 1.08x slower                                                          |
| json                       | 4.15 ms                                                         | 4.54 ms: 1.09x slower                                                          |
| create_gc_cycles           | 652 us                                                          | 757 us: 1.16x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.46 ms: 1.17x slower                                                          |
| typing_runtime_protocols   | 126 us                                                          | 149 us: 1.18x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 233 ms: 2.32x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.11x faster                                                                   |
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240518-3.14.0a0-caf6064-PYTHON_UOPS/bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown