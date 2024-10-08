# Results vs. 3.12.0

- fork: python
- ref: 11fa11987990eb7ed75b
- machine: windows-x86
- commit hash: 11fa119
- commit date: 2024-09-07
- overall geometric mean: 1.12x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 252 ms: 1.11x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.87 sec: 1.06x faster                                                         |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none_tg         | 278 ms                                                          | 197 ms: 1.41x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 255 ms: 1.37x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 502 ms: 1.35x faster                                                           |
| async_tree_none            | 298 ms                                                          | 222 ms: 1.34x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 273 ms: 1.33x faster                                                           |
| async_tree_io              | 693 ms                                                          | 540 ms: 1.28x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 480 ms: 1.18x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 470 ms: 1.16x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.30x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 94.3 ms: 1.35x faster                                                          |
| float          | 76.7 ms                                                         | 62.0 ms: 1.24x faster                                                          |
| Geometric mean | (ref)                                                           | 1.18x faster                                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 109 ms: 1.19x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.89 ms: 1.08x faster                                                          |
| regex_dna      | 127 ms                                                          | 124 ms: 1.02x faster                                                           |
| regex_v8       | 15.0 ms                                                         | 16.2 ms: 1.07x slower                                                          |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 179 us: 1.17x faster                                                           |
| tomli_loads          | 2.20 sec                                                        | 1.89 sec: 1.16x faster                                                         |
| xml_etree_iterparse  | 77.6 ms                                                         | 68.0 ms: 1.14x faster                                                          |
| pickle_pure_python   | 286 us                                                          | 255 us: 1.12x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 66.7 ms: 1.08x faster                                                          |
| xml_etree_process    | 53.2 ms                                                         | 49.5 ms: 1.08x faster                                                          |
| xml_etree_parse      | 113 ms                                                          | 107 ms: 1.06x faster                                                           |
| json_loads           | 20.4 us                                                         | 20.5 us: 1.01x slower                                                          |
| pickle               | 7.79 us                                                         | 7.97 us: 1.02x slower                                                          |
| pickle_dict          | 19.9 us                                                         | 20.4 us: 1.02x slower                                                          |
| unpickle_list        | 2.95 us                                                         | 3.02 us: 1.02x slower                                                          |
| json_dumps           | 7.40 ms                                                         | 7.62 ms: 1.03x slower                                                          |
| unpickle             | 9.71 us                                                         | 10.6 us: 1.09x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.04x faster                                                                   |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.5 ms: 1.08x slower                                                          |
| python_startup         | 22.4 ms                                                         | 24.2 ms: 1.08x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 8.27 ms: 1.20x faster                                                          |
| django_template | 36.9 ms                                                         | 32.4 ms: 1.14x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.17x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 21.9 us: 1.75x faster                                                          |
| deepcopy                   | 360 us                                                          | 242 us: 1.49x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 197 ms: 1.41x faster                                                           |
| comprehensions             | 19.2 us                                                         | 13.7 us: 1.40x faster                                                          |
| generators                 | 38.5 ms                                                         | 27.6 ms: 1.39x faster                                                          |
| async_tree_memoization_tg  | 350 ms                                                          | 255 ms: 1.37x faster                                                           |
| spectral_norm              | 104 ms                                                          | 76.0 ms: 1.37x faster                                                          |
| async_tree_io_tg           | 677 ms                                                          | 502 ms: 1.35x faster                                                           |
| raytrace                   | 308 ms                                                          | 229 ms: 1.35x faster                                                           |
| nbody                      | 127 ms                                                          | 94.3 ms: 1.35x faster                                                          |
| unpack_sequence            | 62.5 ns                                                         | 46.5 ns: 1.34x faster                                                          |
| logging_silent             | 101 ns                                                          | 75.2 ns: 1.34x faster                                                          |
| async_tree_none            | 298 ms                                                          | 222 ms: 1.34x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.68 ms: 1.34x faster                                                          |
| go                         | 137 ms                                                          | 103 ms: 1.33x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 273 ms: 1.33x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.47 us: 1.31x faster                                                          |
| hexiom                     | 6.82 ms                                                         | 5.25 ms: 1.30x faster                                                          |
| scimark_lu                 | 93.2 ms                                                         | 72.3 ms: 1.29x faster                                                          |
| async_tree_io              | 693 ms                                                          | 540 ms: 1.28x faster                                                           |
| chaos                      | 69.4 ms                                                         | 54.1 ms: 1.28x faster                                                          |
| scimark_sor                | 130 ms                                                          | 103 ms: 1.26x faster                                                           |
| float                      | 76.7 ms                                                         | 62.0 ms: 1.24x faster                                                          |
| logging_simple             | 9.75 us                                                         | 7.94 us: 1.23x faster                                                          |
| nqueens                    | 93.7 ms                                                         | 76.5 ms: 1.22x faster                                                          |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.19 ms: 1.21x faster                                                          |
| logging_format             | 10.4 us                                                         | 8.61 us: 1.21x faster                                                          |
| mako                       | 9.96 ms                                                         | 8.27 ms: 1.20x faster                                                          |
| pyflate                    | 424 ms                                                          | 355 ms: 1.19x faster                                                           |
| regex_compile              | 129 ms                                                          | 109 ms: 1.19x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 58.7 ms: 1.18x faster                                                          |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 480 ms: 1.18x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 179 us: 1.17x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 56.8 ms: 1.17x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 470 ms: 1.16x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.89 sec: 1.16x faster                                                         |
| sqlglot_parse              | 1.25 ms                                                         | 1.08 ms: 1.16x faster                                                          |
| dulwich_log                | 58.5 ms                                                         | 50.4 ms: 1.16x faster                                                          |
| sqlglot_transpile          | 1.53 ms                                                         | 1.33 ms: 1.15x faster                                                          |
| sympy_sum                  | 123 ms                                                          | 107 ms: 1.15x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 68.0 ms: 1.14x faster                                                          |
| django_template            | 36.9 ms                                                         | 32.4 ms: 1.14x faster                                                          |
| sympy_integrate            | 17.5 ms                                                         | 15.4 ms: 1.14x faster                                                          |
| pprint_pformat             | 1.50 sec                                                        | 1.32 sec: 1.14x faster                                                         |
| coroutines                 | 20.9 ms                                                         | 18.4 ms: 1.14x faster                                                          |
| pycparser                  | 978 ms                                                          | 866 ms: 1.13x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 255 us: 1.12x faster                                                           |
| pprint_safe_repr           | 721 ms                                                          | 642 ms: 1.12x faster                                                           |
| 2to3                       | 280 ms                                                          | 252 ms: 1.11x faster                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 43.9 ms: 1.11x faster                                                          |
| sympy_str                  | 240 ms                                                          | 217 ms: 1.10x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.75 sec: 1.09x faster                                                         |
| bench_thread_pool          | 1.10 ms                                                         | 1.02 ms: 1.09x faster                                                          |
| xml_etree_generate         | 72.1 ms                                                         | 66.7 ms: 1.08x faster                                                          |
| regex_effbot               | 2.04 ms                                                         | 1.89 ms: 1.08x faster                                                          |
| xml_etree_process          | 53.2 ms                                                         | 49.5 ms: 1.08x faster                                                          |
| scimark_fft                | 271 ms                                                          | 253 ms: 1.07x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.94 us: 1.07x faster                                                          |
| meteor_contest             | 86.9 ms                                                         | 81.4 ms: 1.07x faster                                                          |
| richards                   | 41.3 ms                                                         | 38.8 ms: 1.07x faster                                                          |
| richards_super             | 46.5 ms                                                         | 43.7 ms: 1.06x faster                                                          |
| docutils                   | 1.98 sec                                                        | 1.87 sec: 1.06x faster                                                         |
| xml_etree_parse            | 113 ms                                                          | 107 ms: 1.06x faster                                                           |
| fannkuch                   | 354 ms                                                          | 336 ms: 1.05x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 86.9 ms: 1.05x faster                                                          |
| async_generators           | 313 ms                                                          | 298 ms: 1.05x faster                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 72.1 ms: 1.05x faster                                                          |
| sympy_expand               | 398 ms                                                          | 381 ms: 1.04x faster                                                           |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.2 sec: 1.03x faster                                                         |
| regex_dna                  | 127 ms                                                          | 124 ms: 1.02x faster                                                           |
| json_loads                 | 20.4 us                                                         | 20.5 us: 1.01x slower                                                          |
| json                       | 4.15 ms                                                         | 4.22 ms: 1.02x slower                                                          |
| pickle                     | 7.79 us                                                         | 7.97 us: 1.02x slower                                                          |
| pickle_dict                | 19.9 us                                                         | 20.4 us: 1.02x slower                                                          |
| unpickle_list              | 2.95 us                                                         | 3.02 us: 1.02x slower                                                          |
| json_dumps                 | 7.40 ms                                                         | 7.62 ms: 1.03x slower                                                          |
| regex_v8                   | 15.0 ms                                                         | 16.2 ms: 1.07x slower                                                          |
| coverage                   | 48.4 ms                                                         | 52.1 ms: 1.08x slower                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 20.5 ms: 1.08x slower                                                          |
| python_startup             | 22.4 ms                                                         | 24.2 ms: 1.08x slower                                                          |
| unpickle                   | 9.71 us                                                         | 10.6 us: 1.09x slower                                                          |
| create_gc_cycles           | 652 us                                                          | 739 us: 1.13x slower                                                           |
| asyncio_tcp                | 662 ms                                                          | 757 ms: 1.14x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 152 us: 1.21x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.90 ms: 1.25x slower                                                          |
| sqlglot_normalize          | 100 ms                                                          | 232 ms: 2.31x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.12x faster                                                                   |

Benchmark hidden because not significant (4): pickle_list, pidigits, tornado_http, gc_traversal
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240907-3.14.0a0-11fa119/bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown