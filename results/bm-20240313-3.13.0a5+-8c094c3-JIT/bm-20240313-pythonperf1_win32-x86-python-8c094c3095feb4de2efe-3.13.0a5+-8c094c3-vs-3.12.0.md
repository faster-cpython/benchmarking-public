# Results vs. 3.12.0

- fork: python
- ref: 8c094c3095feb4de2efe
- machine: windows-x86
- commit hash: 8c094c3
- commit date: 2024-03-13
- overall geometric mean: 1.10x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240313-pythonperf1_win32-x86-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 258 ms: 1.08x faster                                                            |
| chameleon      | 7.75 ms                                                         | 5.67 ms: 1.37x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.83 sec: 1.09x faster                                                          |
| tornado_http   | 105 ms                                                          | 96.2 ms: 1.09x faster                                                           |
| Geometric mean | (ref)                                                           | 1.15x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240313-pythonperf1_win32-x86-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 302 ms: 1.16x faster                                                            |
| async_tree_none            | 298 ms                                                          | 256 ms: 1.16x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 241 ms: 1.15x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 319 ms: 1.14x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 600 ms: 1.13x faster                                                            |
| async_tree_io              | 693 ms                                                          | 618 ms: 1.12x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 507 ms: 1.11x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 493 ms: 1.11x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.14x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240313-pythonperf1_win32-x86-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 53.9 ms: 1.42x faster                                                           |
| nbody          | 127 ms                                                          | 95.1 ms: 1.34x faster                                                           |
| pidigits       | 199 ms                                                          | 198 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                           | 1.24x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240313-pythonperf1_win32-x86-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 109 ms: 1.19x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.89 ms: 1.08x faster                                                           |
| regex_dna      | 127 ms                                                          | 122 ms: 1.04x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 16.0 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240313-pythonperf1_win32-x86-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 286 us                                                          | 210 us: 1.36x faster                                                            |
| tomli_loads          | 2.20 sec                                                        | 1.71 sec: 1.28x faster                                                          |
| unpickle_pure_python | 210 us                                                          | 167 us: 1.26x faster                                                            |
| xml_etree_process    | 53.2 ms                                                         | 42.7 ms: 1.25x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 61.7 ms: 1.17x faster                                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 67.4 ms: 1.15x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 6.91 ms: 1.07x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 108 ms: 1.05x faster                                                            |
| json_loads           | 20.4 us                                                         | 19.8 us: 1.03x faster                                                           |
| unpickle_list        | 2.95 us                                                         | 2.88 us: 1.02x faster                                                           |
| pickle_list          | 3.37 us                                                         | 3.31 us: 1.02x faster                                                           |
| pickle               | 7.79 us                                                         | 7.89 us: 1.01x slower                                                           |
| unpickle             | 9.71 us                                                         | 10.2 us: 1.05x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.11x faster                                                                    |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240313-pythonperf1_win32-x86-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 22.4 ms                                                         | 26.4 ms: 1.18x slower                                                           |
| python_startup_no_site | 19.1 ms                                                         | 23.9 ms: 1.25x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.21x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240313-pythonperf1_win32-x86-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 6.94 ms: 1.43x faster                                                           |
| django_template | 36.9 ms                                                         | 30.0 ms: 1.23x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.33x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240313-pythonperf1_win32-x86-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| generators                 | 38.5 ms                                                         | 22.2 ms: 1.73x faster                                                           |
| logging_silent             | 101 ns                                                          | 61.1 ns: 1.65x faster                                                           |
| deepcopy_memo              | 38.4 us                                                         | 24.2 us: 1.59x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 14.2 ms: 1.48x faster                                                           |
| spectral_norm              | 104 ms                                                          | 72.2 ms: 1.44x faster                                                           |
| mako                       | 9.96 ms                                                         | 6.94 ms: 1.43x faster                                                           |
| unpack_sequence            | 62.5 ns                                                         | 43.7 ns: 1.43x faster                                                           |
| float                      | 76.7 ms                                                         | 53.9 ms: 1.42x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.55 ms: 1.41x faster                                                           |
| scimark_sor                | 130 ms                                                          | 94.8 ms: 1.37x faster                                                           |
| chameleon                  | 7.75 ms                                                         | 5.67 ms: 1.37x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 210 us: 1.36x faster                                                            |
| nbody                      | 127 ms                                                          | 95.1 ms: 1.34x faster                                                           |
| typing_runtime_protocols   | 126 us                                                          | 96.4 us: 1.31x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.46 us: 1.31x faster                                                           |
| comprehensions             | 19.2 us                                                         | 14.7 us: 1.30x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 960 us: 1.30x faster                                                            |
| deepcopy                   | 360 us                                                          | 279 us: 1.29x faster                                                            |
| tomli_loads                | 2.20 sec                                                        | 1.71 sec: 1.28x faster                                                          |
| sqlglot_transpile          | 1.53 ms                                                         | 1.21 ms: 1.27x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 167 us: 1.26x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 42.7 ms: 1.25x faster                                                           |
| django_template            | 36.9 ms                                                         | 30.0 ms: 1.23x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.20 ms: 1.21x faster                                                           |
| richards                   | 41.3 ms                                                         | 34.7 ms: 1.19x faster                                                           |
| richards_super             | 46.5 ms                                                         | 39.0 ms: 1.19x faster                                                           |
| regex_compile              | 129 ms                                                          | 109 ms: 1.19x faster                                                            |
| logging_simple             | 9.75 us                                                         | 8.21 us: 1.19x faster                                                           |
| logging_format             | 10.4 us                                                         | 8.82 us: 1.18x faster                                                           |
| chaos                      | 69.4 ms                                                         | 58.8 ms: 1.18x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 61.7 ms: 1.17x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 302 ms: 1.16x faster                                                            |
| async_tree_none            | 298 ms                                                          | 256 ms: 1.16x faster                                                            |
| raytrace                   | 308 ms                                                          | 266 ms: 1.16x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 241 ms: 1.15x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 67.4 ms: 1.15x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 108 ms: 1.14x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 319 ms: 1.14x faster                                                            |
| pycparser                  | 978 ms                                                          | 860 ms: 1.14x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 15.4 ms: 1.14x faster                                                           |
| scimark_fft                | 271 ms                                                          | 239 ms: 1.14x faster                                                            |
| pyflate                    | 424 ms                                                          | 374 ms: 1.13x faster                                                            |
| sympy_str                  | 240 ms                                                          | 212 ms: 1.13x faster                                                            |
| hexiom                     | 6.82 ms                                                         | 6.04 ms: 1.13x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 61.3 ms: 1.13x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 600 ms: 1.13x faster                                                            |
| async_tree_io              | 693 ms                                                          | 618 ms: 1.12x faster                                                            |
| go                         | 137 ms                                                          | 123 ms: 1.12x faster                                                            |
| mdp                        | 1.91 sec                                                        | 1.71 sec: 1.12x faster                                                          |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 507 ms: 1.11x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 493 ms: 1.11x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 84.3 ms: 1.11x faster                                                           |
| fannkuch                   | 354 ms                                                          | 324 ms: 1.09x faster                                                            |
| tornado_http               | 105 ms                                                          | 96.2 ms: 1.09x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.01 ms: 1.09x faster                                                           |
| docutils                   | 1.98 sec                                                        | 1.83 sec: 1.09x faster                                                          |
| 2to3                       | 280 ms                                                          | 258 ms: 1.08x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.89 ms: 1.08x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.93 us: 1.07x faster                                                           |
| sympy_expand               | 398 ms                                                          | 370 ms: 1.07x faster                                                            |
| json_dumps                 | 7.40 ms                                                         | 6.91 ms: 1.07x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 86.0 ms: 1.06x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 82.2 ms: 1.06x faster                                                           |
| async_generators           | 313 ms                                                          | 297 ms: 1.06x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 63.0 ms: 1.05x faster                                                           |
| asyncio_tcp                | 662 ms                                                          | 628 ms: 1.05x faster                                                            |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.8 sec: 1.05x faster                                                          |
| xml_etree_parse            | 113 ms                                                          | 108 ms: 1.05x faster                                                            |
| sqlglot_optimize           | 48.5 ms                                                         | 46.4 ms: 1.04x faster                                                           |
| regex_dna                  | 127 ms                                                          | 122 ms: 1.04x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 90.0 ms: 1.04x faster                                                           |
| json_loads                 | 20.4 us                                                         | 19.8 us: 1.03x faster                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.40 ms: 1.03x faster                                                           |
| unpickle_list              | 2.95 us                                                         | 2.88 us: 1.02x faster                                                           |
| json                       | 4.15 ms                                                         | 4.08 ms: 1.02x faster                                                           |
| pickle_list                | 3.37 us                                                         | 3.31 us: 1.02x faster                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 74.6 ms: 1.01x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.49 sec: 1.01x faster                                                          |
| pidigits                   | 199 ms                                                          | 198 ms: 1.01x faster                                                            |
| pickle                     | 7.79 us                                                         | 7.89 us: 1.01x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 667 us: 1.02x slower                                                            |
| unpickle                   | 9.71 us                                                         | 10.2 us: 1.05x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 16.0 ms: 1.07x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.33 ms: 1.15x slower                                                           |
| python_startup             | 22.4 ms                                                         | 26.4 ms: 1.18x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 23.9 ms: 1.25x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 227 ms: 2.26x slower                                                            |
| coverage                   | 48.4 ms                                                         | 495 ms: 10.22x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.10x faster                                                                    |

Benchmark hidden because not significant (2): pickle_dict, pprint_safe_repr
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240313-3.13.0a5+-8c094c3-JIT/bm-20240313-pythonperf1_win32-x86-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3.json: genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.08x


# Memory

- memory change: unknown