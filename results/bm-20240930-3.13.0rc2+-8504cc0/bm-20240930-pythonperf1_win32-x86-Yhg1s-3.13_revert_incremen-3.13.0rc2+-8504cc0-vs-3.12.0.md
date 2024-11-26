# Results vs. 3.12.0

- fork: Yhg1s
- ref: 3.13_revert_incremen
- machine: windows-x86
- commit hash: 8504cc0
- commit date: 2024-09-30
- overall geometric mean: 1.186x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 243 ms: 1.15x faster                                                            |
| chameleon      | 7.75 ms                                                         | 5.73 ms: 1.35x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.79 sec: 1.11x faster                                                          |
| tornado_http   | 105 ms                                                          | 104 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                           | 1.15x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 490 ms: 1.38x faster                                                            |
| async_tree_io              | 693 ms                                                          | 515 ms: 1.35x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 214 ms: 1.30x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 290 ms: 1.26x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 280 ms: 1.25x faster                                                            |
| async_tree_none            | 298 ms                                                          | 238 ms: 1.25x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 454 ms: 1.20x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 480 ms: 1.17x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.27x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 75.5 ms: 1.68x faster                                                           |
| float          | 76.7 ms                                                         | 54.8 ms: 1.40x faster                                                           |
| pidigits       | 199 ms                                                          | 196 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                           | 1.34x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 100 ms: 1.29x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.91 ms: 1.07x faster                                                           |
| regex_dna      | 127 ms                                                          | 119 ms: 1.06x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 15.8 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 150 us: 1.39x faster                                                            |
| tomli_loads          | 2.20 sec                                                        | 1.69 sec: 1.30x faster                                                          |
| pickle_pure_python   | 286 us                                                          | 225 us: 1.27x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 62.0 ms: 1.25x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 43.9 ms: 1.21x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 60.1 ms: 1.20x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 106 ms: 1.07x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 7.06 ms: 1.05x faster                                                           |
| pickle_list          | 3.37 us                                                         | 3.39 us: 1.01x slower                                                           |
| pickle_dict          | 19.9 us                                                         | 20.3 us: 1.02x slower                                                           |
| pickle               | 7.79 us                                                         | 7.98 us: 1.02x slower                                                           |
| json_loads           | 20.4 us                                                         | 20.9 us: 1.03x slower                                                           |
| unpickle             | 9.71 us                                                         | 10.5 us: 1.09x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.10x faster                                                                    |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.9 ms: 1.04x slower                                                           |
| python_startup         | 22.4 ms                                                         | 24.1 ms: 1.08x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.06x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 6.90 ms: 1.44x faster                                                           |
| django_template | 36.9 ms                                                         | 30.1 ms: 1.22x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.33x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| generators                 | 38.5 ms                                                         | 21.4 ms: 1.80x faster                                                           |
| logging_silent             | 101 ns                                                          | 58.4 ns: 1.73x faster                                                           |
| nbody                      | 127 ms                                                          | 75.5 ms: 1.68x faster                                                           |
| raytrace                   | 308 ms                                                          | 189 ms: 1.63x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 2.23 ms: 1.61x faster                                                           |
| comprehensions             | 19.2 us                                                         | 12.2 us: 1.57x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 4.38 ms: 1.56x faster                                                           |
| deepcopy_memo              | 38.4 us                                                         | 24.7 us: 1.55x faster                                                           |
| scimark_sor                | 130 ms                                                          | 84.6 ms: 1.53x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 61.0 ms: 1.53x faster                                                           |
| spectral_norm              | 104 ms                                                          | 68.8 ms: 1.51x faster                                                           |
| chaos                      | 69.4 ms                                                         | 47.3 ms: 1.47x faster                                                           |
| mako                       | 9.96 ms                                                         | 6.90 ms: 1.44x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 46.6 ms: 1.43x faster                                                           |
| float                      | 76.7 ms                                                         | 54.8 ms: 1.40x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 150 us: 1.39x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 490 ms: 1.38x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.82 ms: 1.37x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 69.0 ms: 1.36x faster                                                           |
| scimark_fft                | 271 ms                                                          | 200 ms: 1.35x faster                                                            |
| chameleon                  | 7.75 ms                                                         | 5.73 ms: 1.35x faster                                                           |
| async_tree_io              | 693 ms                                                          | 515 ms: 1.35x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 15.7 ms: 1.33x faster                                                           |
| pyflate                    | 424 ms                                                          | 326 ms: 1.30x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 214 ms: 1.30x faster                                                            |
| tomli_loads                | 2.20 sec                                                        | 1.69 sec: 1.30x faster                                                          |
| sqlglot_parse              | 1.25 ms                                                         | 962 us: 1.30x faster                                                            |
| regex_compile              | 129 ms                                                          | 100 ms: 1.29x faster                                                            |
| go                         | 137 ms                                                          | 106 ms: 1.29x faster                                                            |
| logging_simple             | 9.75 us                                                         | 7.58 us: 1.29x faster                                                           |
| sqlglot_transpile          | 1.53 ms                                                         | 1.19 ms: 1.28x faster                                                           |
| richards                   | 41.3 ms                                                         | 32.3 ms: 1.28x faster                                                           |
| fannkuch                   | 354 ms                                                          | 277 ms: 1.28x faster                                                            |
| richards_super             | 46.5 ms                                                         | 36.5 ms: 1.27x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 225 us: 1.27x faster                                                            |
| unpack_sequence            | 62.5 ns                                                         | 49.4 ns: 1.26x faster                                                           |
| logging_format             | 10.4 us                                                         | 8.26 us: 1.26x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 290 ms: 1.26x faster                                                            |
| deepcopy                   | 360 us                                                          | 287 us: 1.26x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 62.0 ms: 1.25x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 280 ms: 1.25x faster                                                            |
| async_tree_none            | 298 ms                                                          | 238 ms: 1.25x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 55.8 ms: 1.24x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.21 sec: 1.24x faster                                                          |
| django_template            | 36.9 ms                                                         | 30.1 ms: 1.22x faster                                                           |
| pprint_safe_repr           | 721 ms                                                          | 591 ms: 1.22x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 43.9 ms: 1.21x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.67 us: 1.21x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 454 ms: 1.20x faster                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 60.1 ms: 1.20x faster                                                           |
| dulwich_log                | 58.5 ms                                                         | 49.1 ms: 1.19x faster                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 41.0 ms: 1.18x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 14.9 ms: 1.18x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 480 ms: 1.17x faster                                                            |
| pycparser                  | 978 ms                                                          | 834 ms: 1.17x faster                                                            |
| mdp                        | 1.91 sec                                                        | 1.63 sec: 1.17x faster                                                          |
| meteor_contest             | 86.9 ms                                                         | 74.8 ms: 1.16x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 106 ms: 1.16x faster                                                            |
| 2to3                       | 280 ms                                                          | 243 ms: 1.15x faster                                                            |
| async_generators           | 313 ms                                                          | 274 ms: 1.14x faster                                                            |
| sympy_str                  | 240 ms                                                          | 212 ms: 1.13x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 983 us: 1.12x faster                                                            |
| docutils                   | 1.98 sec                                                        | 1.79 sec: 1.11x faster                                                          |
| xml_etree_parse            | 113 ms                                                          | 106 ms: 1.07x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.91 ms: 1.07x faster                                                           |
| regex_dna                  | 127 ms                                                          | 119 ms: 1.06x faster                                                            |
| sympy_expand               | 398 ms                                                          | 374 ms: 1.06x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.97 us: 1.05x faster                                                           |
| json_dumps                 | 7.40 ms                                                         | 7.06 ms: 1.05x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 88.6 ms: 1.03x faster                                                           |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.1 sec: 1.03x faster                                                          |
| pidigits                   | 199 ms                                                          | 196 ms: 1.02x faster                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 74.1 ms: 1.02x faster                                                           |
| tornado_http               | 105 ms                                                          | 104 ms: 1.01x faster                                                            |
| pickle_list                | 3.37 us                                                         | 3.39 us: 1.01x slower                                                           |
| json                       | 4.15 ms                                                         | 4.23 ms: 1.02x slower                                                           |
| pickle_dict                | 19.9 us                                                         | 20.3 us: 1.02x slower                                                           |
| pickle                     | 7.79 us                                                         | 7.98 us: 1.02x slower                                                           |
| json_loads                 | 20.4 us                                                         | 20.9 us: 1.03x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 19.9 ms: 1.04x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 15.8 ms: 1.05x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 691 us: 1.06x slower                                                            |
| python_startup             | 22.4 ms                                                         | 24.1 ms: 1.08x slower                                                           |
| unpickle                   | 9.71 us                                                         | 10.5 us: 1.09x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 138 us: 1.10x slower                                                            |
| asyncio_tcp                | 662 ms                                                          | 751 ms: 1.13x slower                                                            |
| telco                      | 5.51 ms                                                         | 6.55 ms: 1.19x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 209 ms: 2.09x slower                                                            |
| coverage                   | 48.4 ms                                                         | 320 ms: 6.62x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.17x faster                                                                    |

Benchmark hidden because not significant (2): unpickle_list, gc_traversal
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240930-3.13.0rc2+-8504cc0/bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.186x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: unknown