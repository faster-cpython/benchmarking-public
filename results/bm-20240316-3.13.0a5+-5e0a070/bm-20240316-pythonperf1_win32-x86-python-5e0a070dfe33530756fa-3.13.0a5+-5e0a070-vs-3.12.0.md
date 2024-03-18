# Results vs. 3.12.0

- fork: python
- ref: 5e0a070dfe33530756fa
- machine: windows-x86
- commit hash: 5e0a070
- commit date: 2024-03-16
- overall geometric mean: 1.22x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 230 ms: 1.22x faster                                                            |
| chameleon      | 7.75 ms                                                         | 5.50 ms: 1.41x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.70 sec: 1.17x faster                                                          |
| tornado_http   | 105 ms                                                          | 93.8 ms: 1.12x faster                                                           |
| Geometric mean | (ref)                                                           | 1.22x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none            | 298 ms                                                          | 241 ms: 1.24x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 284 ms: 1.24x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 230 ms: 1.21x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 303 ms: 1.20x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 569 ms: 1.19x faster                                                            |
| async_tree_io              | 693 ms                                                          | 585 ms: 1.19x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 497 ms: 1.13x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 500 ms: 1.09x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.18x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 75.2 ms: 1.69x faster                                                           |
| float          | 76.7 ms                                                         | 52.9 ms: 1.45x faster                                                           |
| pidigits       | 199 ms                                                          | 199 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                           | 1.35x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 94.8 ms: 1.36x faster                                                           |
| regex_dna      | 127 ms                                                          | 117 ms: 1.09x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.90 ms: 1.07x faster                                                           |
| regex_v8       | 15.0 ms                                                         | 16.0 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                           | 1.11x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 140 us: 1.50x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 199 us: 1.44x faster                                                            |
| tomli_loads          | 2.20 sec                                                        | 1.59 sec: 1.38x faster                                                          |
| xml_etree_process    | 53.2 ms                                                         | 41.0 ms: 1.30x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 58.0 ms: 1.24x faster                                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 65.2 ms: 1.19x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 6.60 ms: 1.12x faster                                                           |
| pickle_list          | 3.37 us                                                         | 3.20 us: 1.05x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 107 ms: 1.05x faster                                                            |
| unpickle_list        | 2.95 us                                                         | 2.80 us: 1.05x faster                                                           |
| json_loads           | 20.4 us                                                         | 19.8 us: 1.03x faster                                                           |
| unpickle             | 9.71 us                                                         | 9.81 us: 1.01x slower                                                           |
| pickle               | 7.79 us                                                         | 7.98 us: 1.02x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.15x faster                                                                    |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 22.4 ms                                                         | 22.2 ms: 1.01x faster                                                           |
| python_startup_no_site | 19.1 ms                                                         | 19.8 ms: 1.04x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.02x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 6.82 ms: 1.46x faster                                                           |
| django_template | 36.9 ms                                                         | 27.9 ms: 1.33x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.39x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| logging_silent             | 101 ns                                                          | 57.2 ns: 1.77x faster                                                           |
| generators                 | 38.5 ms                                                         | 21.9 ms: 1.76x faster                                                           |
| comprehensions             | 19.2 us                                                         | 11.0 us: 1.74x faster                                                           |
| deepcopy_memo              | 38.4 us                                                         | 22.4 us: 1.72x faster                                                           |
| nbody                      | 127 ms                                                          | 75.2 ms: 1.69x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.15 ms: 1.67x faster                                                           |
| scimark_sor                | 130 ms                                                          | 77.9 ms: 1.67x faster                                                           |
| raytrace                   | 308 ms                                                          | 191 ms: 1.61x faster                                                            |
| unpack_sequence            | 62.5 ns                                                         | 39.2 ns: 1.60x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 58.9 ms: 1.58x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 4.32 ms: 1.58x faster                                                           |
| spectral_norm              | 104 ms                                                          | 66.4 ms: 1.56x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 44.1 ms: 1.51x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 140 us: 1.50x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 14.1 ms: 1.48x faster                                                           |
| richards                   | 41.3 ms                                                         | 28.1 ms: 1.47x faster                                                           |
| richards_super             | 46.5 ms                                                         | 31.7 ms: 1.46x faster                                                           |
| mako                       | 9.96 ms                                                         | 6.82 ms: 1.46x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 857 us: 1.46x faster                                                            |
| float                      | 76.7 ms                                                         | 52.9 ms: 1.45x faster                                                           |
| go                         | 137 ms                                                          | 95.2 ms: 1.44x faster                                                           |
| typing_runtime_protocols   | 126 us                                                          | 87.8 us: 1.44x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 199 us: 1.44x faster                                                            |
| chaos                      | 69.4 ms                                                         | 48.7 ms: 1.43x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.27 us: 1.42x faster                                                           |
| chameleon                  | 7.75 ms                                                         | 5.50 ms: 1.41x faster                                                           |
| sqlglot_transpile          | 1.53 ms                                                         | 1.09 ms: 1.40x faster                                                           |
| deepcopy                   | 360 us                                                          | 258 us: 1.40x faster                                                            |
| tomli_loads                | 2.20 sec                                                        | 1.59 sec: 1.38x faster                                                          |
| pyflate                    | 424 ms                                                          | 309 ms: 1.37x faster                                                            |
| regex_compile              | 129 ms                                                          | 94.8 ms: 1.36x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 69.2 ms: 1.35x faster                                                           |
| scimark_fft                | 271 ms                                                          | 202 ms: 1.34x faster                                                            |
| pprint_pformat             | 1.50 sec                                                        | 1.13 sec: 1.33x faster                                                          |
| django_template            | 36.9 ms                                                         | 27.9 ms: 1.33x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.91 ms: 1.32x faster                                                           |
| logging_simple             | 9.75 us                                                         | 7.41 us: 1.32x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 53.0 ms: 1.31x faster                                                           |
| logging_format             | 10.4 us                                                         | 8.00 us: 1.30x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 41.0 ms: 1.30x faster                                                           |
| pprint_safe_repr           | 721 ms                                                          | 556 ms: 1.30x faster                                                            |
| fannkuch                   | 354 ms                                                          | 274 ms: 1.29x faster                                                            |
| sqlglot_optimize           | 48.5 ms                                                         | 37.6 ms: 1.29x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 13.9 ms: 1.27x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 97.6 ms: 1.26x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 58.0 ms: 1.24x faster                                                           |
| sympy_str                  | 240 ms                                                          | 194 ms: 1.24x faster                                                            |
| async_tree_none            | 298 ms                                                          | 241 ms: 1.24x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 284 ms: 1.24x faster                                                            |
| pycparser                  | 978 ms                                                          | 802 ms: 1.22x faster                                                            |
| 2to3                       | 280 ms                                                          | 230 ms: 1.22x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 230 ms: 1.21x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 303 ms: 1.20x faster                                                            |
| mdp                        | 1.91 sec                                                        | 1.60 sec: 1.20x faster                                                          |
| xml_etree_iterparse        | 77.6 ms                                                         | 65.2 ms: 1.19x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 569 ms: 1.19x faster                                                            |
| async_generators           | 313 ms                                                          | 264 ms: 1.19x faster                                                            |
| async_tree_io              | 693 ms                                                          | 585 ms: 1.19x faster                                                            |
| sympy_expand               | 398 ms                                                          | 337 ms: 1.18x faster                                                            |
| docutils                   | 1.98 sec                                                        | 1.70 sec: 1.17x faster                                                          |
| meteor_contest             | 86.9 ms                                                         | 75.7 ms: 1.15x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 968 us: 1.14x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 497 ms: 1.13x faster                                                            |
| json_dumps                 | 7.40 ms                                                         | 6.60 ms: 1.12x faster                                                           |
| tornado_http               | 105 ms                                                          | 93.8 ms: 1.12x faster                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 68.0 ms: 1.11x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 500 ms: 1.09x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.91 us: 1.09x faster                                                           |
| regex_dna                  | 127 ms                                                          | 117 ms: 1.09x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.90 ms: 1.07x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 85.7 ms: 1.07x faster                                                           |
| asyncio_tcp                | 662 ms                                                          | 623 ms: 1.06x faster                                                            |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.7 sec: 1.06x faster                                                          |
| pickle_list                | 3.37 us                                                         | 3.20 us: 1.05x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 107 ms: 1.05x faster                                                            |
| unpickle_list              | 2.95 us                                                         | 2.80 us: 1.05x faster                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.39 ms: 1.04x faster                                                           |
| json_loads                 | 20.4 us                                                         | 19.8 us: 1.03x faster                                                           |
| create_gc_cycles           | 652 us                                                          | 638 us: 1.02x faster                                                            |
| python_startup             | 22.4 ms                                                         | 22.2 ms: 1.01x faster                                                           |
| pidigits                   | 199 ms                                                          | 199 ms: 1.00x faster                                                            |
| unpickle                   | 9.71 us                                                         | 9.81 us: 1.01x slower                                                           |
| pickle                     | 7.79 us                                                         | 7.98 us: 1.02x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 19.8 ms: 1.04x slower                                                           |
| telco                      | 5.51 ms                                                         | 5.75 ms: 1.04x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 16.0 ms: 1.06x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 192 ms: 1.92x slower                                                            |
| coverage                   | 48.4 ms                                                         | 453 ms: 9.36x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.22x faster                                                                    |

Benchmark hidden because not significant (2): json, pickle_dict
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240316-3.13.0a5+-5e0a070/bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070.json: genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.18x


# Memory

- memory change: unknown