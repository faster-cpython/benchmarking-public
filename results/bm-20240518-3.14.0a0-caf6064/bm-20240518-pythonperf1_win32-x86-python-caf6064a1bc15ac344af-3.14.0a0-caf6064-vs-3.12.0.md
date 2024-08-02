# Results vs. 3.12.0

- fork: python
- ref: caf6064a1bc15ac344af
- machine: windows-x86
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.20x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 235 ms: 1.19x faster                                                           |
| chameleon      | 7.75 ms                                                         | 5.69 ms: 1.36x faster                                                          |
| docutils       | 1.98 sec                                                        | 1.80 sec: 1.10x faster                                                         |
| tornado_http   | 105 ms                                                          | 94.0 ms: 1.12x faster                                                          |
| Geometric mean | (ref)                                                           | 1.19x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none_tg         | 278 ms                                                          | 203 ms: 1.37x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 256 ms: 1.37x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 277 ms: 1.31x faster                                                           |
| async_tree_none            | 298 ms                                                          | 228 ms: 1.30x faster                                                           |
| async_tree_io              | 693 ms                                                          | 533 ms: 1.30x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 527 ms: 1.29x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 475 ms: 1.15x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 496 ms: 1.14x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.28x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 78.9 ms: 1.61x faster                                                          |
| float          | 76.7 ms                                                         | 53.5 ms: 1.43x faster                                                          |
| pidigits       | 199 ms                                                          | 197 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                           | 1.33x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 97.6 ms: 1.32x faster                                                          |
| regex_dna      | 127 ms                                                          | 117 ms: 1.09x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.90 ms: 1.07x faster                                                          |
| regex_v8       | 15.0 ms                                                         | 15.8 ms: 1.05x slower                                                          |
| Geometric mean | (ref)                                                           | 1.10x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 150 us: 1.40x faster                                                           |
| tomli_loads          | 2.20 sec                                                        | 1.64 sec: 1.34x faster                                                         |
| pickle_pure_python   | 286 us                                                          | 223 us: 1.28x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 42.5 ms: 1.25x faster                                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 63.5 ms: 1.22x faster                                                          |
| xml_etree_generate   | 72.1 ms                                                         | 60.0 ms: 1.20x faster                                                          |
| xml_etree_parse      | 113 ms                                                          | 103 ms: 1.10x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 7.04 ms: 1.05x faster                                                          |
| json_loads           | 20.4 us                                                         | 20.5 us: 1.01x slower                                                          |
| pickle               | 7.79 us                                                         | 7.97 us: 1.02x slower                                                          |
| unpickle_list        | 2.95 us                                                         | 3.03 us: 1.03x slower                                                          |
| pickle_dict          | 19.9 us                                                         | 20.7 us: 1.04x slower                                                          |
| pickle_list          | 3.37 us                                                         | 3.51 us: 1.04x slower                                                          |
| unpickle             | 9.71 us                                                         | 10.2 us: 1.05x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.11x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup | 22.4 ms                                                         | 22.6 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                   |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.12 ms: 1.40x faster                                                          |
| django_template | 36.9 ms                                                         | 29.4 ms: 1.26x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.33x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| generators                 | 38.5 ms                                                         | 21.7 ms: 1.78x faster                                                          |
| logging_silent             | 101 ns                                                          | 57.8 ns: 1.75x faster                                                          |
| raytrace                   | 308 ms                                                          | 183 ms: 1.68x faster                                                           |
| comprehensions             | 19.2 us                                                         | 11.8 us: 1.63x faster                                                          |
| deltablue                  | 3.58 ms                                                         | 2.22 ms: 1.61x faster                                                          |
| nbody                      | 127 ms                                                          | 78.9 ms: 1.61x faster                                                          |
| deepcopy_memo              | 38.4 us                                                         | 24.6 us: 1.56x faster                                                          |
| hexiom                     | 6.82 ms                                                         | 4.38 ms: 1.56x faster                                                          |
| scimark_lu                 | 93.2 ms                                                         | 61.0 ms: 1.53x faster                                                          |
| spectral_norm              | 104 ms                                                          | 68.4 ms: 1.52x faster                                                          |
| chaos                      | 69.4 ms                                                         | 46.6 ms: 1.49x faster                                                          |
| float                      | 76.7 ms                                                         | 53.5 ms: 1.43x faster                                                          |
| scimark_sor                | 130 ms                                                          | 91.4 ms: 1.42x faster                                                          |
| mako                       | 9.96 ms                                                         | 7.12 ms: 1.40x faster                                                          |
| unpickle_pure_python       | 210 us                                                          | 150 us: 1.40x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 48.3 ms: 1.38x faster                                                          |
| async_tree_none_tg         | 278 ms                                                          | 203 ms: 1.37x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 68.5 ms: 1.37x faster                                                          |
| async_tree_memoization_tg  | 350 ms                                                          | 256 ms: 1.37x faster                                                           |
| pyflate                    | 424 ms                                                          | 310 ms: 1.37x faster                                                           |
| chameleon                  | 7.75 ms                                                         | 5.69 ms: 1.36x faster                                                          |
| go                         | 137 ms                                                          | 102 ms: 1.34x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.64 sec: 1.34x faster                                                         |
| regex_compile              | 129 ms                                                          | 97.6 ms: 1.32x faster                                                          |
| richards_super             | 46.5 ms                                                         | 35.4 ms: 1.31x faster                                                          |
| richards                   | 41.3 ms                                                         | 31.5 ms: 1.31x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 277 ms: 1.31x faster                                                           |
| scimark_fft                | 271 ms                                                          | 207 ms: 1.31x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 954 us: 1.31x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.95 ms: 1.31x faster                                                          |
| async_tree_none            | 298 ms                                                          | 228 ms: 1.30x faster                                                           |
| async_tree_io              | 693 ms                                                          | 533 ms: 1.30x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 16.1 ms: 1.29x faster                                                          |
| sqlglot_transpile          | 1.53 ms                                                         | 1.19 ms: 1.29x faster                                                          |
| async_tree_io_tg           | 677 ms                                                          | 527 ms: 1.29x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 223 us: 1.28x faster                                                           |
| logging_simple             | 9.75 us                                                         | 7.66 us: 1.27x faster                                                          |
| crypto_pyaes               | 69.2 ms                                                         | 54.6 ms: 1.27x faster                                                          |
| django_template            | 36.9 ms                                                         | 29.4 ms: 1.26x faster                                                          |
| xml_etree_process          | 53.2 ms                                                         | 42.5 ms: 1.25x faster                                                          |
| logging_format             | 10.4 us                                                         | 8.31 us: 1.25x faster                                                          |
| deepcopy                   | 360 us                                                          | 292 us: 1.23x faster                                                           |
| pycparser                  | 978 ms                                                          | 795 ms: 1.23x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.22 sec: 1.23x faster                                                         |
| fannkuch                   | 354 ms                                                          | 288 ms: 1.23x faster                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 39.6 ms: 1.22x faster                                                          |
| xml_etree_iterparse        | 77.6 ms                                                         | 63.5 ms: 1.22x faster                                                          |
| deepcopy_reduce            | 3.23 us                                                         | 2.66 us: 1.21x faster                                                          |
| sympy_integrate            | 17.5 ms                                                         | 14.6 ms: 1.20x faster                                                          |
| pprint_safe_repr           | 721 ms                                                          | 599 ms: 1.20x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 60.0 ms: 1.20x faster                                                          |
| 2to3                       | 280 ms                                                          | 235 ms: 1.19x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.61 sec: 1.19x faster                                                         |
| sympy_sum                  | 123 ms                                                          | 104 ms: 1.18x faster                                                           |
| sympy_str                  | 240 ms                                                          | 205 ms: 1.17x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 75.3 ms: 1.15x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 475 ms: 1.15x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 969 us: 1.14x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 496 ms: 1.14x faster                                                           |
| async_generators           | 313 ms                                                          | 276 ms: 1.14x faster                                                           |
| tornado_http               | 105 ms                                                          | 94.0 ms: 1.12x faster                                                          |
| xml_etree_parse            | 113 ms                                                          | 103 ms: 1.10x faster                                                           |
| docutils                   | 1.98 sec                                                        | 1.80 sec: 1.10x faster                                                         |
| sympy_expand               | 398 ms                                                          | 365 ms: 1.09x faster                                                           |
| regex_dna                  | 127 ms                                                          | 117 ms: 1.09x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.93 us: 1.07x faster                                                          |
| regex_effbot               | 2.04 ms                                                         | 1.90 ms: 1.07x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 85.8 ms: 1.07x faster                                                          |
| json_dumps                 | 7.40 ms                                                         | 7.04 ms: 1.05x faster                                                          |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.8 sec: 1.05x faster                                                         |
| bench_mp_pool              | 75.4 ms                                                         | 71.9 ms: 1.05x faster                                                          |
| pidigits                   | 199 ms                                                          | 197 ms: 1.01x faster                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.43 ms: 1.01x faster                                                          |
| json_loads                 | 20.4 us                                                         | 20.5 us: 1.01x slower                                                          |
| python_startup             | 22.4 ms                                                         | 22.6 ms: 1.01x slower                                                          |
| pickle                     | 7.79 us                                                         | 7.97 us: 1.02x slower                                                          |
| unpickle_list              | 2.95 us                                                         | 3.03 us: 1.03x slower                                                          |
| pickle_dict                | 19.9 us                                                         | 20.7 us: 1.04x slower                                                          |
| pickle_list                | 3.37 us                                                         | 3.51 us: 1.04x slower                                                          |
| regex_v8                   | 15.0 ms                                                         | 15.8 ms: 1.05x slower                                                          |
| coverage                   | 48.4 ms                                                         | 50.9 ms: 1.05x slower                                                          |
| typing_runtime_protocols   | 126 us                                                          | 133 us: 1.05x slower                                                           |
| unpickle                   | 9.71 us                                                         | 10.2 us: 1.05x slower                                                          |
| create_gc_cycles           | 652 us                                                          | 732 us: 1.12x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.28 ms: 1.14x slower                                                          |
| sqlglot_normalize          | 100 ms                                                          | 204 ms: 2.04x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.20x faster                                                                   |

Benchmark hidden because not significant (3): asyncio_tcp, python_startup_no_site, json
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240518-3.14.0a0-caf6064/bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: unknown