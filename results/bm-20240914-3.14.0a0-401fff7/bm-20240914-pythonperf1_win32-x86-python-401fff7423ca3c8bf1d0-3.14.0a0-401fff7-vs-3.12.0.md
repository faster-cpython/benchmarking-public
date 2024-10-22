# Results vs. 3.12.0

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: windows-x86
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.12x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 249 ms: 1.13x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.85 sec: 1.07x faster                                                         |
| tornado_http   | 105 ms                                                          | 95.2 ms: 1.10x faster                                                          |
| Geometric mean | (ref)                                                           | 1.10x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 253 ms: 1.39x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 201 ms: 1.38x faster                                                           |
| async_tree_none            | 298 ms                                                          | 221 ms: 1.35x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 276 ms: 1.32x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 522 ms: 1.30x faster                                                           |
| async_tree_io              | 693 ms                                                          | 542 ms: 1.28x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 466 ms: 1.21x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 461 ms: 1.19x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.30x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 94.2 ms: 1.35x faster                                                          |
| float          | 76.7 ms                                                         | 61.6 ms: 1.25x faster                                                          |
| pidigits       | 199 ms                                                          | 198 ms: 1.00x faster                                                           |
| Geometric mean | (ref)                                                           | 1.19x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 109 ms: 1.18x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.91 ms: 1.07x faster                                                          |
| regex_dna      | 127 ms                                                          | 119 ms: 1.07x faster                                                           |
| regex_v8       | 15.0 ms                                                         | 16.3 ms: 1.09x slower                                                          |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 179 us: 1.17x faster                                                           |
| tomli_loads          | 2.20 sec                                                        | 1.87 sec: 1.17x faster                                                         |
| xml_etree_iterparse  | 77.6 ms                                                         | 67.8 ms: 1.14x faster                                                          |
| pickle_pure_python   | 286 us                                                          | 269 us: 1.06x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 67.8 ms: 1.06x faster                                                          |
| xml_etree_process    | 53.2 ms                                                         | 50.1 ms: 1.06x faster                                                          |
| xml_etree_parse      | 113 ms                                                          | 108 ms: 1.04x faster                                                           |
| json_loads           | 20.4 us                                                         | 20.7 us: 1.02x slower                                                          |
| pickle_dict          | 19.9 us                                                         | 20.4 us: 1.02x slower                                                          |
| pickle               | 7.79 us                                                         | 7.99 us: 1.02x slower                                                          |
| unpickle             | 9.71 us                                                         | 10.3 us: 1.06x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.04x faster                                                                   |

Benchmark hidden because not significant (3): json_dumps, unpickle_list, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.3 ms: 1.06x slower                                                          |
| python_startup         | 22.4 ms                                                         | 23.9 ms: 1.07x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.07x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 8.00 ms: 1.24x faster                                                          |
| django_template | 36.9 ms                                                         | 34.7 ms: 1.06x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.15x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 21.8 us: 1.76x faster                                                          |
| generators                 | 38.5 ms                                                         | 25.9 ms: 1.49x faster                                                          |
| deepcopy                   | 360 us                                                          | 244 us: 1.48x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 253 ms: 1.39x faster                                                           |
| comprehensions             | 19.2 us                                                         | 13.9 us: 1.38x faster                                                          |
| async_tree_none_tg         | 278 ms                                                          | 201 ms: 1.38x faster                                                           |
| spectral_norm              | 104 ms                                                          | 75.6 ms: 1.37x faster                                                          |
| unpack_sequence            | 62.5 ns                                                         | 45.5 ns: 1.37x faster                                                          |
| scimark_lu                 | 93.2 ms                                                         | 69.0 ms: 1.35x faster                                                          |
| nbody                      | 127 ms                                                          | 94.2 ms: 1.35x faster                                                          |
| logging_silent             | 101 ns                                                          | 75.0 ns: 1.35x faster                                                          |
| async_tree_none            | 298 ms                                                          | 221 ms: 1.35x faster                                                           |
| scimark_sor                | 130 ms                                                          | 98.3 ms: 1.32x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 276 ms: 1.32x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 522 ms: 1.30x faster                                                           |
| raytrace                   | 308 ms                                                          | 238 ms: 1.30x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 5.27 ms: 1.29x faster                                                          |
| deltablue                  | 3.58 ms                                                         | 2.79 ms: 1.28x faster                                                          |
| async_tree_io              | 693 ms                                                          | 542 ms: 1.28x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.53 us: 1.27x faster                                                          |
| chaos                      | 69.4 ms                                                         | 54.7 ms: 1.27x faster                                                          |
| nqueens                    | 93.7 ms                                                         | 74.4 ms: 1.26x faster                                                          |
| float                      | 76.7 ms                                                         | 61.6 ms: 1.25x faster                                                          |
| mako                       | 9.96 ms                                                         | 8.00 ms: 1.24x faster                                                          |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.12 ms: 1.24x faster                                                          |
| go                         | 137 ms                                                          | 112 ms: 1.23x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 466 ms: 1.21x faster                                                           |
| pyflate                    | 424 ms                                                          | 353 ms: 1.20x faster                                                           |
| logging_simple             | 9.75 us                                                         | 8.15 us: 1.20x faster                                                          |
| crypto_pyaes               | 69.2 ms                                                         | 58.3 ms: 1.19x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 461 ms: 1.19x faster                                                           |
| logging_format             | 10.4 us                                                         | 8.81 us: 1.18x faster                                                          |
| sqlglot_parse              | 1.25 ms                                                         | 1.06 ms: 1.18x faster                                                          |
| regex_compile              | 129 ms                                                          | 109 ms: 1.18x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 179 us: 1.17x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.87 sec: 1.17x faster                                                         |
| scimark_monte_carlo        | 66.4 ms                                                         | 56.9 ms: 1.17x faster                                                          |
| sqlglot_transpile          | 1.53 ms                                                         | 1.32 ms: 1.16x faster                                                          |
| dulwich_log                | 58.5 ms                                                         | 50.9 ms: 1.15x faster                                                          |
| scimark_fft                | 271 ms                                                          | 236 ms: 1.15x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 107 ms: 1.15x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 67.8 ms: 1.14x faster                                                          |
| sympy_integrate            | 17.5 ms                                                         | 15.4 ms: 1.14x faster                                                          |
| coroutines                 | 20.9 ms                                                         | 18.5 ms: 1.13x faster                                                          |
| 2to3                       | 280 ms                                                          | 249 ms: 1.13x faster                                                           |
| pycparser                  | 978 ms                                                          | 876 ms: 1.12x faster                                                           |
| sympy_str                  | 240 ms                                                          | 217 ms: 1.11x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 82.9 ms: 1.10x faster                                                          |
| tornado_http               | 105 ms                                                          | 95.2 ms: 1.10x faster                                                          |
| bench_thread_pool          | 1.10 ms                                                         | 1.00 ms: 1.10x faster                                                          |
| fannkuch                   | 354 ms                                                          | 322 ms: 1.10x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.37 sec: 1.10x faster                                                         |
| sqlglot_optimize           | 48.5 ms                                                         | 44.4 ms: 1.09x faster                                                          |
| async_generators           | 313 ms                                                          | 291 ms: 1.08x faster                                                           |
| pprint_safe_repr           | 721 ms                                                          | 670 ms: 1.08x faster                                                           |
| docutils                   | 1.98 sec                                                        | 1.85 sec: 1.07x faster                                                         |
| meteor_contest             | 86.9 ms                                                         | 81.0 ms: 1.07x faster                                                          |
| regex_effbot               | 2.04 ms                                                         | 1.91 ms: 1.07x faster                                                          |
| regex_dna                  | 127 ms                                                          | 119 ms: 1.07x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 269 us: 1.06x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 67.8 ms: 1.06x faster                                                          |
| django_template            | 36.9 ms                                                         | 34.7 ms: 1.06x faster                                                          |
| xml_etree_process          | 53.2 ms                                                         | 50.1 ms: 1.06x faster                                                          |
| mdp                        | 1.91 sec                                                        | 1.80 sec: 1.06x faster                                                         |
| bench_mp_pool              | 75.4 ms                                                         | 71.5 ms: 1.05x faster                                                          |
| sqlite_synth               | 2.07 us                                                         | 1.97 us: 1.05x faster                                                          |
| xml_etree_parse            | 113 ms                                                          | 108 ms: 1.04x faster                                                           |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.0 sec: 1.04x faster                                                         |
| richards                   | 41.3 ms                                                         | 40.0 ms: 1.03x faster                                                          |
| sympy_expand               | 398 ms                                                          | 385 ms: 1.03x faster                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.41 ms: 1.02x faster                                                          |
| richards_super             | 46.5 ms                                                         | 46.0 ms: 1.01x faster                                                          |
| pidigits                   | 199 ms                                                          | 198 ms: 1.00x faster                                                           |
| json_loads                 | 20.4 us                                                         | 20.7 us: 1.02x slower                                                          |
| pickle_dict                | 19.9 us                                                         | 20.4 us: 1.02x slower                                                          |
| pickle                     | 7.79 us                                                         | 7.99 us: 1.02x slower                                                          |
| json                       | 4.15 ms                                                         | 4.29 ms: 1.03x slower                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 20.3 ms: 1.06x slower                                                          |
| unpickle                   | 9.71 us                                                         | 10.3 us: 1.06x slower                                                          |
| python_startup             | 22.4 ms                                                         | 23.9 ms: 1.07x slower                                                          |
| regex_v8                   | 15.0 ms                                                         | 16.3 ms: 1.09x slower                                                          |
| coverage                   | 48.4 ms                                                         | 53.2 ms: 1.10x slower                                                          |
| create_gc_cycles           | 652 us                                                          | 735 us: 1.13x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 148 us: 1.17x slower                                                           |
| telco                      | 5.51 ms                                                         | 7.04 ms: 1.28x slower                                                          |
| sqlglot_normalize          | 100 ms                                                          | 230 ms: 2.30x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.12x faster                                                                   |

Benchmark hidden because not significant (4): asyncio_tcp, json_dumps, unpickle_list, pickle_list
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240914-3.14.0a0-401fff7/bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown