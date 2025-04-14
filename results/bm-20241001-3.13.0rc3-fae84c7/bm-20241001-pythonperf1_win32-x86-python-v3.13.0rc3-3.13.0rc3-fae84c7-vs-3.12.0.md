# Results vs. 3.12.0

- fork: python
- ref: v3.13.0rc3
- machine: windows-x86
- commit hash: fae84c7
- commit date: 2024-10-01
- overall geometric mean: 1.178x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 243 ms: 1.15x faster                                                  |
| chameleon      | 7.75 ms                                                         | 5.98 ms: 1.30x faster                                                 |
| docutils       | 1.98 sec                                                        | 1.77 sec: 1.12x faster                                                |
| tornado_http   | 105 ms                                                          | 102 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                           | 1.15x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 482 ms: 1.40x faster                                                  |
| async_tree_io              | 693 ms                                                          | 508 ms: 1.36x faster                                                  |
| async_tree_none_tg         | 278 ms                                                          | 206 ms: 1.34x faster                                                  |
| async_tree_memoization     | 364 ms                                                          | 281 ms: 1.29x faster                                                  |
| async_tree_none            | 298 ms                                                          | 231 ms: 1.29x faster                                                  |
| async_tree_memoization_tg  | 350 ms                                                          | 273 ms: 1.28x faster                                                  |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 456 ms: 1.20x faster                                                  |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 473 ms: 1.19x faster                                                  |
| Geometric mean             | (ref)                                                           | 1.29x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 78.0 ms: 1.63x faster                                                 |
| float          | 76.7 ms                                                         | 55.2 ms: 1.39x faster                                                 |
| Geometric mean | (ref)                                                           | 1.31x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 99.5 ms: 1.30x faster                                                 |
| regex_dna      | 127 ms                                                          | 119 ms: 1.07x faster                                                  |
| regex_effbot   | 2.04 ms                                                         | 1.90 ms: 1.07x faster                                                 |
| regex_v8       | 15.0 ms                                                         | 15.8 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                           | 1.09x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 157 us: 1.34x faster                                                  |
| tomli_loads          | 2.20 sec                                                        | 1.67 sec: 1.32x faster                                                |
| xml_etree_iterparse  | 77.6 ms                                                         | 62.2 ms: 1.25x faster                                                 |
| pickle_pure_python   | 286 us                                                          | 231 us: 1.24x faster                                                  |
| xml_etree_process    | 53.2 ms                                                         | 44.3 ms: 1.20x faster                                                 |
| xml_etree_generate   | 72.1 ms                                                         | 62.6 ms: 1.15x faster                                                 |
| xml_etree_parse      | 113 ms                                                          | 103 ms: 1.10x faster                                                  |
| unpickle_list        | 2.95 us                                                         | 2.78 us: 1.06x faster                                                 |
| pickle_list          | 3.37 us                                                         | 3.32 us: 1.01x faster                                                 |
| json_dumps           | 7.40 ms                                                         | 7.48 ms: 1.01x slower                                                 |
| json_loads           | 20.4 us                                                         | 20.6 us: 1.01x slower                                                 |
| pickle_dict          | 19.9 us                                                         | 20.3 us: 1.02x slower                                                 |
| unpickle             | 9.71 us                                                         | 10.3 us: 1.06x slower                                                 |
| Geometric mean       | (ref)                                                           | 1.10x faster                                                          |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.6 ms: 1.08x slower                                                 |
| python_startup         | 22.4 ms                                                         | 24.7 ms: 1.10x slower                                                 |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.06 ms: 1.41x faster                                                 |
| django_template | 36.9 ms                                                         | 29.3 ms: 1.26x faster                                                 |
| Geometric mean  | (ref)                                                           | 1.33x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| generators                 | 38.5 ms                                                         | 21.5 ms: 1.79x faster                                                 |
| logging_silent             | 101 ns                                                          | 59.5 ns: 1.70x faster                                                 |
| nbody                      | 127 ms                                                          | 78.0 ms: 1.63x faster                                                 |
| raytrace                   | 308 ms                                                          | 191 ms: 1.61x faster                                                  |
| deltablue                  | 3.58 ms                                                         | 2.27 ms: 1.58x faster                                                 |
| comprehensions             | 19.2 us                                                         | 12.4 us: 1.55x faster                                                 |
| hexiom                     | 6.82 ms                                                         | 4.50 ms: 1.51x faster                                                 |
| scimark_lu                 | 93.2 ms                                                         | 62.1 ms: 1.50x faster                                                 |
| deepcopy_memo              | 38.4 us                                                         | 25.7 us: 1.49x faster                                                 |
| scimark_sor                | 130 ms                                                          | 88.0 ms: 1.48x faster                                                 |
| unpack_sequence            | 62.5 ns                                                         | 43.5 ns: 1.44x faster                                                 |
| chaos                      | 69.4 ms                                                         | 48.3 ms: 1.44x faster                                                 |
| spectral_norm              | 104 ms                                                          | 73.1 ms: 1.42x faster                                                 |
| mako                       | 9.96 ms                                                         | 7.06 ms: 1.41x faster                                                 |
| async_tree_io_tg           | 677 ms                                                          | 482 ms: 1.40x faster                                                  |
| float                      | 76.7 ms                                                         | 55.2 ms: 1.39x faster                                                 |
| scimark_monte_carlo        | 66.4 ms                                                         | 47.9 ms: 1.39x faster                                                 |
| async_tree_io              | 693 ms                                                          | 508 ms: 1.36x faster                                                  |
| pyflate                    | 424 ms                                                          | 313 ms: 1.35x faster                                                  |
| nqueens                    | 93.7 ms                                                         | 69.1 ms: 1.35x faster                                                 |
| async_tree_none_tg         | 278 ms                                                          | 206 ms: 1.34x faster                                                  |
| unpickle_pure_python       | 210 us                                                          | 157 us: 1.34x faster                                                  |
| coroutines                 | 20.9 ms                                                         | 15.6 ms: 1.34x faster                                                 |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.90 ms: 1.33x faster                                                 |
| scimark_fft                | 271 ms                                                          | 205 ms: 1.32x faster                                                  |
| tomli_loads                | 2.20 sec                                                        | 1.67 sec: 1.32x faster                                                |
| sqlglot_parse              | 1.25 ms                                                         | 956 us: 1.31x faster                                                  |
| go                         | 137 ms                                                          | 105 ms: 1.30x faster                                                  |
| regex_compile              | 129 ms                                                          | 99.5 ms: 1.30x faster                                                 |
| chameleon                  | 7.75 ms                                                         | 5.98 ms: 1.30x faster                                                 |
| async_tree_memoization     | 364 ms                                                          | 281 ms: 1.29x faster                                                  |
| async_tree_none            | 298 ms                                                          | 231 ms: 1.29x faster                                                  |
| sqlglot_transpile          | 1.53 ms                                                         | 1.19 ms: 1.29x faster                                                 |
| async_tree_memoization_tg  | 350 ms                                                          | 273 ms: 1.28x faster                                                  |
| logging_simple             | 9.75 us                                                         | 7.68 us: 1.27x faster                                                 |
| django_template            | 36.9 ms                                                         | 29.3 ms: 1.26x faster                                                 |
| richards_super             | 46.5 ms                                                         | 37.0 ms: 1.26x faster                                                 |
| fannkuch                   | 354 ms                                                          | 282 ms: 1.25x faster                                                  |
| logging_format             | 10.4 us                                                         | 8.31 us: 1.25x faster                                                 |
| xml_etree_iterparse        | 77.6 ms                                                         | 62.2 ms: 1.25x faster                                                 |
| deepcopy                   | 360 us                                                          | 291 us: 1.24x faster                                                  |
| pickle_pure_python         | 286 us                                                          | 231 us: 1.24x faster                                                  |
| richards                   | 41.3 ms                                                         | 33.5 ms: 1.24x faster                                                 |
| pycparser                  | 978 ms                                                          | 810 ms: 1.21x faster                                                  |
| crypto_pyaes               | 69.2 ms                                                         | 57.5 ms: 1.20x faster                                                 |
| xml_etree_process          | 53.2 ms                                                         | 44.3 ms: 1.20x faster                                                 |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 456 ms: 1.20x faster                                                  |
| sqlglot_optimize           | 48.5 ms                                                         | 40.5 ms: 1.20x faster                                                 |
| pprint_pformat             | 1.50 sec                                                        | 1.25 sec: 1.20x faster                                                |
| async_generators           | 313 ms                                                          | 263 ms: 1.19x faster                                                  |
| dulwich_log                | 58.5 ms                                                         | 49.0 ms: 1.19x faster                                                 |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 473 ms: 1.19x faster                                                  |
| deepcopy_reduce            | 3.23 us                                                         | 2.72 us: 1.19x faster                                                 |
| pprint_safe_repr           | 721 ms                                                          | 610 ms: 1.18x faster                                                  |
| sympy_integrate            | 17.5 ms                                                         | 14.9 ms: 1.18x faster                                                 |
| mdp                        | 1.91 sec                                                        | 1.64 sec: 1.17x faster                                                |
| sympy_sum                  | 123 ms                                                          | 106 ms: 1.16x faster                                                  |
| 2to3                       | 280 ms                                                          | 243 ms: 1.15x faster                                                  |
| xml_etree_generate         | 72.1 ms                                                         | 62.6 ms: 1.15x faster                                                 |
| meteor_contest             | 86.9 ms                                                         | 76.3 ms: 1.14x faster                                                 |
| sympy_str                  | 240 ms                                                          | 212 ms: 1.13x faster                                                  |
| docutils                   | 1.98 sec                                                        | 1.77 sec: 1.12x faster                                                |
| bench_thread_pool          | 1.10 ms                                                         | 989 us: 1.11x faster                                                  |
| xml_etree_parse            | 113 ms                                                          | 103 ms: 1.10x faster                                                  |
| regex_dna                  | 127 ms                                                          | 119 ms: 1.07x faster                                                  |
| sympy_expand               | 398 ms                                                          | 371 ms: 1.07x faster                                                  |
| regex_effbot               | 2.04 ms                                                         | 1.90 ms: 1.07x faster                                                 |
| unpickle_list              | 2.95 us                                                         | 2.78 us: 1.06x faster                                                 |
| sqlite_synth               | 2.07 us                                                         | 1.98 us: 1.05x faster                                                 |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.0 sec: 1.04x faster                                                |
| pathlib                    | 91.4 ms                                                         | 88.3 ms: 1.04x faster                                                 |
| tornado_http               | 105 ms                                                          | 102 ms: 1.03x faster                                                  |
| pickle_list                | 3.37 us                                                         | 3.32 us: 1.01x faster                                                 |
| gc_traversal               | 1.44 ms                                                         | 1.45 ms: 1.01x slower                                                 |
| json_dumps                 | 7.40 ms                                                         | 7.48 ms: 1.01x slower                                                 |
| json_loads                 | 20.4 us                                                         | 20.6 us: 1.01x slower                                                 |
| pickle_dict                | 19.9 us                                                         | 20.3 us: 1.02x slower                                                 |
| bench_mp_pool              | 75.4 ms                                                         | 76.8 ms: 1.02x slower                                                 |
| json                       | 4.15 ms                                                         | 4.25 ms: 1.02x slower                                                 |
| regex_v8                   | 15.0 ms                                                         | 15.8 ms: 1.05x slower                                                 |
| unpickle                   | 9.71 us                                                         | 10.3 us: 1.06x slower                                                 |
| create_gc_cycles           | 652 us                                                          | 699 us: 1.07x slower                                                  |
| python_startup_no_site     | 19.1 ms                                                         | 20.6 ms: 1.08x slower                                                 |
| typing_runtime_protocols   | 126 us                                                          | 137 us: 1.08x slower                                                  |
| python_startup             | 22.4 ms                                                         | 24.7 ms: 1.10x slower                                                 |
| asyncio_tcp                | 662 ms                                                          | 739 ms: 1.12x slower                                                  |
| telco                      | 5.51 ms                                                         | 6.35 ms: 1.15x slower                                                 |
| sqlglot_normalize          | 100 ms                                                          | 209 ms: 2.08x slower                                                  |
| coverage                   | 48.4 ms                                                         | 324 ms: 6.68x slower                                                  |
| Geometric mean             | (ref)                                                           | 1.17x faster                                                          |

Benchmark hidden because not significant (2): pickle, pidigits
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241001-3.13.0rc3-fae84c7/bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.178x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: unknown