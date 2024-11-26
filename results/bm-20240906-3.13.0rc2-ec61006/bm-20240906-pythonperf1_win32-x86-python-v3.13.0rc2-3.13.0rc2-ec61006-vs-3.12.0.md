# Results vs. 3.12.0

- fork: python
- ref: v3.13.0rc2
- machine: windows-x86
- commit hash: ec61006
- commit date: 2024-09-06
- overall geometric mean: 1.172x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 245 ms: 1.14x faster                                                  |
| chameleon      | 7.75 ms                                                         | 5.83 ms: 1.33x faster                                                 |
| docutils       | 1.98 sec                                                        | 1.85 sec: 1.07x faster                                                |
| Geometric mean | (ref)                                                           | 1.13x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 260 ms: 1.35x faster                                                  |
| async_tree_none_tg         | 278 ms                                                          | 208 ms: 1.34x faster                                                  |
| async_tree_memoization     | 364 ms                                                          | 279 ms: 1.31x faster                                                  |
| async_tree_none            | 298 ms                                                          | 230 ms: 1.29x faster                                                  |
| async_tree_io              | 693 ms                                                          | 537 ms: 1.29x faster                                                  |
| async_tree_io_tg           | 677 ms                                                          | 537 ms: 1.26x faster                                                  |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 452 ms: 1.21x faster                                                  |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 475 ms: 1.19x faster                                                  |
| Geometric mean             | (ref)                                                           | 1.28x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 79.6 ms: 1.60x faster                                                 |
| float          | 76.7 ms                                                         | 53.5 ms: 1.43x faster                                                 |
| Geometric mean | (ref)                                                           | 1.32x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 101 ms: 1.28x faster                                                  |
| regex_effbot   | 2.04 ms                                                         | 1.88 ms: 1.08x faster                                                 |
| regex_dna      | 127 ms                                                          | 119 ms: 1.06x faster                                                  |
| regex_v8       | 15.0 ms                                                         | 15.9 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                           | 1.09x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 155 us: 1.35x faster                                                  |
| tomli_loads          | 2.20 sec                                                        | 1.65 sec: 1.33x faster                                                |
| pickle_pure_python   | 286 us                                                          | 228 us: 1.26x faster                                                  |
| xml_etree_iterparse  | 77.6 ms                                                         | 65.3 ms: 1.19x faster                                                 |
| xml_etree_process    | 53.2 ms                                                         | 44.9 ms: 1.19x faster                                                 |
| xml_etree_generate   | 72.1 ms                                                         | 62.2 ms: 1.16x faster                                                 |
| pickle_list          | 3.37 us                                                         | 3.15 us: 1.07x faster                                                 |
| xml_etree_parse      | 113 ms                                                          | 107 ms: 1.06x faster                                                  |
| json_dumps           | 7.40 ms                                                         | 7.03 ms: 1.05x faster                                                 |
| json_loads           | 20.4 us                                                         | 20.6 us: 1.01x slower                                                 |
| pickle_dict          | 19.9 us                                                         | 20.4 us: 1.03x slower                                                 |
| pickle               | 7.79 us                                                         | 8.01 us: 1.03x slower                                                 |
| unpickle             | 9.71 us                                                         | 10.0 us: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                           | 1.10x faster                                                          |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.9 ms: 1.04x slower                                                 |
| python_startup         | 22.4 ms                                                         | 24.2 ms: 1.08x slower                                                 |
| Geometric mean         | (ref)                                                           | 1.06x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.08 ms: 1.41x faster                                                 |
| django_template | 36.9 ms                                                         | 31.1 ms: 1.19x faster                                                 |
| Geometric mean  | (ref)                                                           | 1.29x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| generators                 | 38.5 ms                                                         | 21.8 ms: 1.77x faster                                                 |
| logging_silent             | 101 ns                                                          | 60.1 ns: 1.68x faster                                                 |
| raytrace                   | 308 ms                                                          | 193 ms: 1.60x faster                                                  |
| nbody                      | 127 ms                                                          | 79.6 ms: 1.60x faster                                                 |
| deepcopy_memo              | 38.4 us                                                         | 24.9 us: 1.54x faster                                                 |
| comprehensions             | 19.2 us                                                         | 12.5 us: 1.54x faster                                                 |
| deltablue                  | 3.58 ms                                                         | 2.34 ms: 1.53x faster                                                 |
| scimark_lu                 | 93.2 ms                                                         | 62.0 ms: 1.50x faster                                                 |
| hexiom                     | 6.82 ms                                                         | 4.58 ms: 1.49x faster                                                 |
| scimark_sor                | 130 ms                                                          | 87.5 ms: 1.48x faster                                                 |
| spectral_norm              | 104 ms                                                          | 70.3 ms: 1.48x faster                                                 |
| unpack_sequence            | 62.5 ns                                                         | 42.8 ns: 1.46x faster                                                 |
| float                      | 76.7 ms                                                         | 53.5 ms: 1.43x faster                                                 |
| chaos                      | 69.4 ms                                                         | 48.9 ms: 1.42x faster                                                 |
| mako                       | 9.96 ms                                                         | 7.08 ms: 1.41x faster                                                 |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.82 ms: 1.37x faster                                                 |
| unpickle_pure_python       | 210 us                                                          | 155 us: 1.35x faster                                                  |
| scimark_monte_carlo        | 66.4 ms                                                         | 49.2 ms: 1.35x faster                                                 |
| async_tree_memoization_tg  | 350 ms                                                          | 260 ms: 1.35x faster                                                  |
| nqueens                    | 93.7 ms                                                         | 69.5 ms: 1.35x faster                                                 |
| async_tree_none_tg         | 278 ms                                                          | 208 ms: 1.34x faster                                                  |
| chameleon                  | 7.75 ms                                                         | 5.83 ms: 1.33x faster                                                 |
| tomli_loads                | 2.20 sec                                                        | 1.65 sec: 1.33x faster                                                |
| pyflate                    | 424 ms                                                          | 319 ms: 1.33x faster                                                  |
| scimark_fft                | 271 ms                                                          | 204 ms: 1.32x faster                                                  |
| async_tree_memoization     | 364 ms                                                          | 279 ms: 1.31x faster                                                  |
| coroutines                 | 20.9 ms                                                         | 16.0 ms: 1.31x faster                                                 |
| async_tree_none            | 298 ms                                                          | 230 ms: 1.29x faster                                                  |
| async_tree_io              | 693 ms                                                          | 537 ms: 1.29x faster                                                  |
| regex_compile              | 129 ms                                                          | 101 ms: 1.28x faster                                                  |
| go                         | 137 ms                                                          | 108 ms: 1.27x faster                                                  |
| sqlglot_parse              | 1.25 ms                                                         | 989 us: 1.26x faster                                                  |
| async_tree_io_tg           | 677 ms                                                          | 537 ms: 1.26x faster                                                  |
| sqlglot_transpile          | 1.53 ms                                                         | 1.22 ms: 1.26x faster                                                 |
| pickle_pure_python         | 286 us                                                          | 228 us: 1.26x faster                                                  |
| logging_simple             | 9.75 us                                                         | 7.79 us: 1.25x faster                                                 |
| crypto_pyaes               | 69.2 ms                                                         | 55.4 ms: 1.25x faster                                                 |
| deepcopy                   | 360 us                                                          | 288 us: 1.25x faster                                                  |
| richards                   | 41.3 ms                                                         | 33.3 ms: 1.24x faster                                                 |
| fannkuch                   | 354 ms                                                          | 286 ms: 1.24x faster                                                  |
| richards_super             | 46.5 ms                                                         | 37.7 ms: 1.23x faster                                                 |
| logging_format             | 10.4 us                                                         | 8.48 us: 1.23x faster                                                 |
| pycparser                  | 978 ms                                                          | 798 ms: 1.22x faster                                                  |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 452 ms: 1.21x faster                                                  |
| pprint_pformat             | 1.50 sec                                                        | 1.25 sec: 1.20x faster                                                |
| deepcopy_reduce            | 3.23 us                                                         | 2.70 us: 1.19x faster                                                 |
| sqlglot_optimize           | 48.5 ms                                                         | 40.6 ms: 1.19x faster                                                 |
| xml_etree_iterparse        | 77.6 ms                                                         | 65.3 ms: 1.19x faster                                                 |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 475 ms: 1.19x faster                                                  |
| dulwich_log                | 58.5 ms                                                         | 49.2 ms: 1.19x faster                                                 |
| xml_etree_process          | 53.2 ms                                                         | 44.9 ms: 1.19x faster                                                 |
| pprint_safe_repr           | 721 ms                                                          | 608 ms: 1.19x faster                                                  |
| django_template            | 36.9 ms                                                         | 31.1 ms: 1.19x faster                                                 |
| sympy_integrate            | 17.5 ms                                                         | 14.9 ms: 1.18x faster                                                 |
| xml_etree_generate         | 72.1 ms                                                         | 62.2 ms: 1.16x faster                                                 |
| mdp                        | 1.91 sec                                                        | 1.65 sec: 1.16x faster                                                |
| sympy_sum                  | 123 ms                                                          | 106 ms: 1.15x faster                                                  |
| meteor_contest             | 86.9 ms                                                         | 75.8 ms: 1.15x faster                                                 |
| 2to3                       | 280 ms                                                          | 245 ms: 1.14x faster                                                  |
| sympy_str                  | 240 ms                                                          | 211 ms: 1.14x faster                                                  |
| async_generators           | 313 ms                                                          | 278 ms: 1.13x faster                                                  |
| bench_thread_pool          | 1.10 ms                                                         | 1.01 ms: 1.09x faster                                                 |
| sympy_expand               | 398 ms                                                          | 368 ms: 1.08x faster                                                  |
| regex_effbot               | 2.04 ms                                                         | 1.88 ms: 1.08x faster                                                 |
| docutils                   | 1.98 sec                                                        | 1.85 sec: 1.07x faster                                                |
| pickle_list                | 3.37 us                                                         | 3.15 us: 1.07x faster                                                 |
| regex_dna                  | 127 ms                                                          | 119 ms: 1.06x faster                                                  |
| xml_etree_parse            | 113 ms                                                          | 107 ms: 1.06x faster                                                  |
| json_dumps                 | 7.40 ms                                                         | 7.03 ms: 1.05x faster                                                 |
| sqlite_synth               | 2.07 us                                                         | 1.98 us: 1.04x faster                                                 |
| bench_mp_pool              | 75.4 ms                                                         | 73.1 ms: 1.03x faster                                                 |
| pathlib                    | 91.4 ms                                                         | 88.7 ms: 1.03x faster                                                 |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.2 sec: 1.03x faster                                                |
| json_loads                 | 20.4 us                                                         | 20.6 us: 1.01x slower                                                 |
| pickle_dict                | 19.9 us                                                         | 20.4 us: 1.03x slower                                                 |
| pickle                     | 7.79 us                                                         | 8.01 us: 1.03x slower                                                 |
| json                       | 4.15 ms                                                         | 4.27 ms: 1.03x slower                                                 |
| unpickle                   | 9.71 us                                                         | 10.0 us: 1.03x slower                                                 |
| python_startup_no_site     | 19.1 ms                                                         | 19.9 ms: 1.04x slower                                                 |
| regex_v8                   | 15.0 ms                                                         | 15.9 ms: 1.06x slower                                                 |
| python_startup             | 22.4 ms                                                         | 24.2 ms: 1.08x slower                                                 |
| asyncio_tcp                | 662 ms                                                          | 717 ms: 1.08x slower                                                  |
| typing_runtime_protocols   | 126 us                                                          | 139 us: 1.10x slower                                                  |
| create_gc_cycles           | 652 us                                                          | 751 us: 1.15x slower                                                  |
| telco                      | 5.51 ms                                                         | 6.56 ms: 1.19x slower                                                 |
| sqlglot_normalize          | 100 ms                                                          | 210 ms: 2.10x slower                                                  |
| coverage                   | 48.4 ms                                                         | 324 ms: 6.70x slower                                                  |
| Geometric mean             | (ref)                                                           | 1.16x faster                                                          |

Benchmark hidden because not significant (4): tornado_http, unpickle_list, pidigits, gc_traversal
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240906-3.13.0rc2-ec61006/bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.172x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: unknown