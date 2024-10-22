# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: deferred_globals_fin
- machine: windows-x86
- commit hash: bfd4400
- commit date: 2024-08-28
- overall geometric mean: 1.11x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 258 ms: 1.09x faster                                                                     |
| docutils       | 1.98 sec                                                        | 1.94 sec: 1.02x faster                                                                   |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                             |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 251 ms: 1.39x faster                                                                     |
| async_tree_none_tg         | 278 ms                                                          | 200 ms: 1.39x faster                                                                     |
| async_tree_memoization     | 364 ms                                                          | 276 ms: 1.32x faster                                                                     |
| async_tree_io_tg           | 677 ms                                                          | 514 ms: 1.32x faster                                                                     |
| async_tree_none            | 298 ms                                                          | 226 ms: 1.32x faster                                                                     |
| async_tree_io              | 693 ms                                                          | 553 ms: 1.25x faster                                                                     |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 471 ms: 1.20x faster                                                                     |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 460 ms: 1.19x faster                                                                     |
| Geometric mean             | (ref)                                                           | 1.29x faster                                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 92.7 ms: 1.37x faster                                                                    |
| float          | 76.7 ms                                                         | 62.8 ms: 1.22x faster                                                                    |
| pidigits       | 199 ms                                                          | 198 ms: 1.01x faster                                                                     |
| Geometric mean | (ref)                                                           | 1.19x faster                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 109 ms: 1.18x faster                                                                     |
| regex_dna      | 127 ms                                                          | 118 ms: 1.07x faster                                                                     |
| regex_effbot   | 2.04 ms                                                         | 1.93 ms: 1.05x faster                                                                    |
| regex_v8       | 15.0 ms                                                         | 16.4 ms: 1.09x slower                                                                    |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 178 us: 1.18x faster                                                                     |
| tomli_loads          | 2.20 sec                                                        | 1.91 sec: 1.15x faster                                                                   |
| xml_etree_iterparse  | 77.6 ms                                                         | 69.8 ms: 1.11x faster                                                                    |
| pickle_pure_python   | 286 us                                                          | 262 us: 1.09x faster                                                                     |
| xml_etree_generate   | 72.1 ms                                                         | 68.1 ms: 1.06x faster                                                                    |
| xml_etree_parse      | 113 ms                                                          | 108 ms: 1.05x faster                                                                     |
| xml_etree_process    | 53.2 ms                                                         | 51.2 ms: 1.04x faster                                                                    |
| json_dumps           | 7.40 ms                                                         | 7.47 ms: 1.01x slower                                                                    |
| json_loads           | 20.4 us                                                         | 21.3 us: 1.05x slower                                                                    |
| Geometric mean       | (ref)                                                           | 1.07x faster                                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.1 ms: 1.05x slower                                                                    |
| python_startup         | 22.4 ms                                                         | 24.0 ms: 1.07x slower                                                                    |
| Geometric mean         | (ref)                                                           | 1.06x slower                                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|-----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 8.27 ms: 1.20x faster                                                                    |
| django_template | 36.9 ms                                                         | 33.2 ms: 1.11x faster                                                                    |
| Geometric mean  | (ref)                                                           | 1.16x faster                                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 23.0 us: 1.67x faster                                                                    |
| deepcopy                   | 360 us                                                          | 252 us: 1.43x faster                                                                     |
| generators                 | 38.5 ms                                                         | 27.0 ms: 1.43x faster                                                                    |
| async_tree_memoization_tg  | 350 ms                                                          | 251 ms: 1.39x faster                                                                     |
| async_tree_none_tg         | 278 ms                                                          | 200 ms: 1.39x faster                                                                     |
| nbody                      | 127 ms                                                          | 92.7 ms: 1.37x faster                                                                    |
| raytrace                   | 308 ms                                                          | 228 ms: 1.35x faster                                                                     |
| logging_silent             | 101 ns                                                          | 75.6 ns: 1.34x faster                                                                    |
| comprehensions             | 19.2 us                                                         | 14.4 us: 1.34x faster                                                                    |
| spectral_norm              | 104 ms                                                          | 78.4 ms: 1.32x faster                                                                    |
| async_tree_memoization     | 364 ms                                                          | 276 ms: 1.32x faster                                                                     |
| async_tree_io_tg           | 677 ms                                                          | 514 ms: 1.32x faster                                                                     |
| async_tree_none            | 298 ms                                                          | 226 ms: 1.32x faster                                                                     |
| scimark_lu                 | 93.2 ms                                                         | 71.0 ms: 1.31x faster                                                                    |
| deltablue                  | 3.58 ms                                                         | 2.76 ms: 1.30x faster                                                                    |
| deepcopy_reduce            | 3.23 us                                                         | 2.50 us: 1.29x faster                                                                    |
| chaos                      | 69.4 ms                                                         | 54.0 ms: 1.28x faster                                                                    |
| hexiom                     | 6.82 ms                                                         | 5.42 ms: 1.26x faster                                                                    |
| scimark_sor                | 130 ms                                                          | 104 ms: 1.25x faster                                                                     |
| async_tree_io              | 693 ms                                                          | 553 ms: 1.25x faster                                                                     |
| logging_format             | 10.4 us                                                         | 8.49 us: 1.23x faster                                                                    |
| logging_simple             | 9.75 us                                                         | 7.99 us: 1.22x faster                                                                    |
| float                      | 76.7 ms                                                         | 62.8 ms: 1.22x faster                                                                    |
| mako                       | 9.96 ms                                                         | 8.27 ms: 1.20x faster                                                                    |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 471 ms: 1.20x faster                                                                     |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.24 ms: 1.19x faster                                                                    |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 460 ms: 1.19x faster                                                                     |
| regex_compile              | 129 ms                                                          | 109 ms: 1.18x faster                                                                     |
| unpickle_pure_python       | 210 us                                                          | 178 us: 1.18x faster                                                                     |
| dulwich_log                | 58.5 ms                                                         | 50.0 ms: 1.17x faster                                                                    |
| crypto_pyaes               | 69.2 ms                                                         | 59.5 ms: 1.16x faster                                                                    |
| nqueens                    | 93.7 ms                                                         | 81.6 ms: 1.15x faster                                                                    |
| tomli_loads                | 2.20 sec                                                        | 1.91 sec: 1.15x faster                                                                   |
| pycparser                  | 978 ms                                                          | 857 ms: 1.14x faster                                                                     |
| sqlglot_transpile          | 1.53 ms                                                         | 1.34 ms: 1.14x faster                                                                    |
| pyflate                    | 424 ms                                                          | 372 ms: 1.14x faster                                                                     |
| sqlglot_parse              | 1.25 ms                                                         | 1.10 ms: 1.14x faster                                                                    |
| scimark_monte_carlo        | 66.4 ms                                                         | 58.9 ms: 1.13x faster                                                                    |
| mdp                        | 1.91 sec                                                        | 1.70 sec: 1.13x faster                                                                   |
| scimark_fft                | 271 ms                                                          | 241 ms: 1.13x faster                                                                     |
| coroutines                 | 20.9 ms                                                         | 18.6 ms: 1.12x faster                                                                    |
| go                         | 137 ms                                                          | 122 ms: 1.12x faster                                                                     |
| sympy_integrate            | 17.5 ms                                                         | 15.7 ms: 1.12x faster                                                                    |
| django_template            | 36.9 ms                                                         | 33.2 ms: 1.11x faster                                                                    |
| xml_etree_iterparse        | 77.6 ms                                                         | 69.8 ms: 1.11x faster                                                                    |
| sympy_sum                  | 123 ms                                                          | 112 ms: 1.10x faster                                                                     |
| pickle_pure_python         | 286 us                                                          | 262 us: 1.09x faster                                                                     |
| 2to3                       | 280 ms                                                          | 258 ms: 1.09x faster                                                                     |
| sqlglot_optimize           | 48.5 ms                                                         | 45.0 ms: 1.08x faster                                                                    |
| sympy_str                  | 240 ms                                                          | 222 ms: 1.08x faster                                                                     |
| fannkuch                   | 354 ms                                                          | 329 ms: 1.07x faster                                                                     |
| regex_dna                  | 127 ms                                                          | 118 ms: 1.07x faster                                                                     |
| pprint_safe_repr           | 721 ms                                                          | 672 ms: 1.07x faster                                                                     |
| meteor_contest             | 86.9 ms                                                         | 81.2 ms: 1.07x faster                                                                    |
| pprint_pformat             | 1.50 sec                                                        | 1.41 sec: 1.06x faster                                                                   |
| xml_etree_generate         | 72.1 ms                                                         | 68.1 ms: 1.06x faster                                                                    |
| bench_thread_pool          | 1.10 ms                                                         | 1.04 ms: 1.06x faster                                                                    |
| pathlib                    | 91.4 ms                                                         | 86.5 ms: 1.06x faster                                                                    |
| regex_effbot               | 2.04 ms                                                         | 1.93 ms: 1.05x faster                                                                    |
| xml_etree_parse            | 113 ms                                                          | 108 ms: 1.05x faster                                                                     |
| xml_etree_process          | 53.2 ms                                                         | 51.2 ms: 1.04x faster                                                                    |
| richards                   | 41.3 ms                                                         | 40.0 ms: 1.03x faster                                                                    |
| richards_super             | 46.5 ms                                                         | 45.0 ms: 1.03x faster                                                                    |
| bench_mp_pool              | 75.4 ms                                                         | 73.1 ms: 1.03x faster                                                                    |
| async_generators           | 313 ms                                                          | 304 ms: 1.03x faster                                                                     |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.2 sec: 1.03x faster                                                                   |
| sympy_expand               | 398 ms                                                          | 389 ms: 1.02x faster                                                                     |
| docutils                   | 1.98 sec                                                        | 1.94 sec: 1.02x faster                                                                   |
| pidigits                   | 199 ms                                                          | 198 ms: 1.01x faster                                                                     |
| json_dumps                 | 7.40 ms                                                         | 7.47 ms: 1.01x slower                                                                    |
| json                       | 4.15 ms                                                         | 4.25 ms: 1.02x slower                                                                    |
| json_loads                 | 20.4 us                                                         | 21.3 us: 1.05x slower                                                                    |
| python_startup_no_site     | 19.1 ms                                                         | 20.1 ms: 1.05x slower                                                                    |
| python_startup             | 22.4 ms                                                         | 24.0 ms: 1.07x slower                                                                    |
| regex_v8                   | 15.0 ms                                                         | 16.4 ms: 1.09x slower                                                                    |
| asyncio_tcp                | 662 ms                                                          | 722 ms: 1.09x slower                                                                     |
| coverage                   | 48.4 ms                                                         | 54.0 ms: 1.11x slower                                                                    |
| create_gc_cycles           | 652 us                                                          | 760 us: 1.17x slower                                                                     |
| telco                      | 5.51 ms                                                         | 6.49 ms: 1.18x slower                                                                    |
| typing_runtime_protocols   | 126 us                                                          | 152 us: 1.20x slower                                                                     |
| sqlglot_normalize          | 100 ms                                                          | 233 ms: 2.33x slower                                                                     |
| Geometric mean             | (ref)                                                           | 1.11x faster                                                                             |

Benchmark hidden because not significant (2): gc_traversal, tornado_http
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240828-3.14.0a0-bfd4400/bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown