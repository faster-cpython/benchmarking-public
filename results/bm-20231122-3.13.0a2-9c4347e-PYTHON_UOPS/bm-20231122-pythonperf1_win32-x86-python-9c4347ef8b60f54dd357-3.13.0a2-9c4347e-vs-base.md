# Results vs. base

- fork: python
- ref: 9c4347ef8b60f54dd357
- machine: windows-x86
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.07x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e | bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                              | 268 ms: 1.09x slower                                                           |
| chameleon      | 5.96 ms                                                             | 6.15 ms: 1.03x slower                                                          |
| docutils       | 1.78 sec                                                            | 1.94 sec: 1.09x slower                                                         |
| tornado_http   | 98.2 ms                                                             | 112 ms: 1.14x slower                                                           |
| Geometric mean | (ref)                                                               | 1.09x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e | bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 511 ms                                                              | 523 ms: 1.02x slower                                                           |
| async_tree_io_tg           | 619 ms                                                              | 634 ms: 1.03x slower                                                           |
| async_tree_cpu_io_mixed_tg | 506 ms                                                              | 518 ms: 1.03x slower                                                           |
| async_tree_memoization     | 317 ms                                                              | 329 ms: 1.04x slower                                                           |
| async_tree_io              | 623 ms                                                              | 651 ms: 1.05x slower                                                           |
| async_tree_memoization_tg  | 312 ms                                                              | 327 ms: 1.05x slower                                                           |
| async_tree_none_tg         | 248 ms                                                              | 264 ms: 1.06x slower                                                           |
| async_tree_none            | 254 ms                                                              | 270 ms: 1.06x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.04x slower                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e | bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 200 ms                                                              | 198 ms: 1.01x faster                                                           |
| nbody          | 88.9 ms                                                             | 91.9 ms: 1.03x slower                                                          |
| float          | 59.8 ms                                                             | 62.3 ms: 1.04x slower                                                          |
| Geometric mean | (ref)                                                               | 1.02x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e | bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 16.2 ms                                                             | 16.3 ms: 1.01x slower                                                          |
| regex_effbot   | 1.92 ms                                                             | 2.01 ms: 1.05x slower                                                          |
| regex_dna      | 120 ms                                                              | 132 ms: 1.09x slower                                                           |
| regex_compile  | 106 ms                                                              | 131 ms: 1.24x slower                                                           |
| Geometric mean | (ref)                                                               | 1.09x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e | bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle_list        | 2.94 us                                                             | 2.69 us: 1.09x faster                                                          |
| tomli_loads          | 1.81 sec                                                            | 1.79 sec: 1.01x faster                                                         |
| pickle_dict          | 19.8 us                                                             | 19.7 us: 1.01x faster                                                          |
| json_loads           | 19.8 us                                                             | 19.9 us: 1.01x slower                                                          |
| unpickle             | 9.58 us                                                             | 9.65 us: 1.01x slower                                                          |
| pickle               | 7.57 us                                                             | 7.66 us: 1.01x slower                                                          |
| pickle_pure_python   | 231 us                                                              | 235 us: 1.02x slower                                                           |
| json_dumps           | 6.96 ms                                                             | 7.11 ms: 1.02x slower                                                          |
| xml_etree_parse      | 108 ms                                                              | 111 ms: 1.03x slower                                                           |
| xml_etree_iterparse  | 69.5 ms                                                             | 71.7 ms: 1.03x slower                                                          |
| xml_etree_process    | 45.8 ms                                                             | 47.9 ms: 1.04x slower                                                          |
| xml_etree_generate   | 62.8 ms                                                             | 67.3 ms: 1.07x slower                                                          |
| unpickle_pure_python | 156 us                                                              | 173 us: 1.11x slower                                                           |
| Geometric mean       | (ref)                                                               | 1.02x slower                                                                   |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e | bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 23.3 ms: 1.05x slower                                                          |
| python_startup_no_site | 20.0 ms                                                             | 21.2 ms: 1.06x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.05x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e | bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e |
|-----------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako      | 7.72 ms                                                             | 8.20 ms: 1.06x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e | bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle_list              | 2.94 us                                                             | 2.69 us: 1.09x faster                                                          |
| pidigits                   | 200 ms                                                              | 198 ms: 1.01x faster                                                           |
| pathlib                    | 89.7 ms                                                             | 89.1 ms: 1.01x faster                                                          |
| tomli_loads                | 1.81 sec                                                            | 1.79 sec: 1.01x faster                                                         |
| pickle_dict                | 19.8 us                                                             | 19.7 us: 1.01x faster                                                          |
| json                       | 4.14 ms                                                             | 4.12 ms: 1.01x faster                                                          |
| coverage                   | 512 ms                                                              | 510 ms: 1.01x faster                                                           |
| regex_v8                   | 16.2 ms                                                             | 16.3 ms: 1.01x slower                                                          |
| json_loads                 | 19.8 us                                                             | 19.9 us: 1.01x slower                                                          |
| unpickle                   | 9.58 us                                                             | 9.65 us: 1.01x slower                                                          |
| asyncio_tcp_ssl            | 17.2 sec                                                            | 17.4 sec: 1.01x slower                                                         |
| gc_traversal               | 1.39 ms                                                             | 1.40 ms: 1.01x slower                                                          |
| pickle                     | 7.57 us                                                             | 7.66 us: 1.01x slower                                                          |
| sqlite_synth               | 1.84 us                                                             | 1.87 us: 1.02x slower                                                          |
| pickle_pure_python         | 231 us                                                              | 235 us: 1.02x slower                                                           |
| json_dumps                 | 6.96 ms                                                             | 7.11 ms: 1.02x slower                                                          |
| async_tree_cpu_io_mixed    | 511 ms                                                              | 523 ms: 1.02x slower                                                           |
| async_tree_io_tg           | 619 ms                                                              | 634 ms: 1.03x slower                                                           |
| async_tree_cpu_io_mixed_tg | 506 ms                                                              | 518 ms: 1.03x slower                                                           |
| xml_etree_parse            | 108 ms                                                              | 111 ms: 1.03x slower                                                           |
| logging_simple             | 8.35 us                                                             | 8.58 us: 1.03x slower                                                          |
| logging_format             | 8.90 us                                                             | 9.15 us: 1.03x slower                                                          |
| xml_etree_iterparse        | 69.5 ms                                                             | 71.7 ms: 1.03x slower                                                          |
| chameleon                  | 5.96 ms                                                             | 6.15 ms: 1.03x slower                                                          |
| nbody                      | 88.9 ms                                                             | 91.9 ms: 1.03x slower                                                          |
| meteor_contest             | 80.4 ms                                                             | 83.2 ms: 1.03x slower                                                          |
| async_tree_memoization     | 317 ms                                                              | 329 ms: 1.04x slower                                                           |
| float                      | 59.8 ms                                                             | 62.3 ms: 1.04x slower                                                          |
| deepcopy_memo              | 26.6 us                                                             | 27.8 us: 1.04x slower                                                          |
| scimark_sor                | 97.7 ms                                                             | 102 ms: 1.04x slower                                                           |
| pprint_pformat             | 1.28 sec                                                            | 1.33 sec: 1.04x slower                                                         |
| pprint_safe_repr           | 621 ms                                                              | 649 ms: 1.04x slower                                                           |
| xml_etree_process          | 45.8 ms                                                             | 47.9 ms: 1.04x slower                                                          |
| bench_thread_pool          | 1.05 ms                                                             | 1.09 ms: 1.05x slower                                                          |
| async_tree_io              | 623 ms                                                              | 651 ms: 1.05x slower                                                           |
| async_tree_memoization_tg  | 312 ms                                                              | 327 ms: 1.05x slower                                                           |
| python_startup             | 22.2 ms                                                             | 23.3 ms: 1.05x slower                                                          |
| regex_effbot               | 1.92 ms                                                             | 2.01 ms: 1.05x slower                                                          |
| deepcopy                   | 295 us                                                              | 310 us: 1.05x slower                                                           |
| telco                      | 6.08 ms                                                             | 6.40 ms: 1.05x slower                                                          |
| richards                   | 33.7 ms                                                             | 35.6 ms: 1.06x slower                                                          |
| python_startup_no_site     | 20.0 ms                                                             | 21.2 ms: 1.06x slower                                                          |
| crypto_pyaes               | 55.4 ms                                                             | 58.8 ms: 1.06x slower                                                          |
| typing_runtime_protocols   | 98.7 us                                                             | 105 us: 1.06x slower                                                           |
| fannkuch                   | 302 ms                                                              | 321 ms: 1.06x slower                                                           |
| mako                       | 7.72 ms                                                             | 8.20 ms: 1.06x slower                                                          |
| mdp                        | 1.70 sec                                                            | 1.81 sec: 1.06x slower                                                         |
| async_tree_none_tg         | 248 ms                                                              | 264 ms: 1.06x slower                                                           |
| async_tree_none            | 254 ms                                                              | 270 ms: 1.06x slower                                                           |
| richards_super             | 38.0 ms                                                             | 40.6 ms: 1.07x slower                                                          |
| xml_etree_generate         | 62.8 ms                                                             | 67.3 ms: 1.07x slower                                                          |
| bench_mp_pool              | 69.3 ms                                                             | 75.2 ms: 1.09x slower                                                          |
| 2to3                       | 246 ms                                                              | 268 ms: 1.09x slower                                                           |
| docutils                   | 1.78 sec                                                            | 1.94 sec: 1.09x slower                                                         |
| logging_silent             | 70.3 ns                                                             | 76.8 ns: 1.09x slower                                                          |
| regex_dna                  | 120 ms                                                              | 132 ms: 1.09x slower                                                           |
| async_generators           | 278 ms                                                              | 304 ms: 1.09x slower                                                           |
| pyflate                    | 335 ms                                                              | 367 ms: 1.09x slower                                                           |
| coroutines                 | 16.7 ms                                                             | 18.3 ms: 1.10x slower                                                          |
| generators                 | 27.0 ms                                                             | 29.6 ms: 1.10x slower                                                          |
| scimark_fft                | 220 ms                                                              | 243 ms: 1.10x slower                                                           |
| chaos                      | 51.8 ms                                                             | 57.2 ms: 1.10x slower                                                          |
| sqlglot_transpile          | 1.21 ms                                                             | 1.33 ms: 1.11x slower                                                          |
| pycparser                  | 862 ms                                                              | 955 ms: 1.11x slower                                                           |
| unpickle_pure_python       | 156 us                                                              | 173 us: 1.11x slower                                                           |
| sqlglot_parse              | 953 us                                                              | 1.06 ms: 1.11x slower                                                          |
| sqlglot_normalize          | 212 ms                                                              | 237 ms: 1.12x slower                                                           |
| go                         | 108 ms                                                              | 121 ms: 1.12x slower                                                           |
| sqlglot_optimize           | 41.5 ms                                                             | 46.8 ms: 1.13x slower                                                          |
| sympy_expand               | 362 ms                                                              | 408 ms: 1.13x slower                                                           |
| nqueens                    | 80.1 ms                                                             | 91.2 ms: 1.14x slower                                                          |
| tornado_http               | 98.2 ms                                                             | 112 ms: 1.14x slower                                                           |
| scimark_monte_carlo        | 50.6 ms                                                             | 57.8 ms: 1.14x slower                                                          |
| scimark_lu                 | 69.0 ms                                                             | 79.2 ms: 1.15x slower                                                          |
| raytrace                   | 223 ms                                                              | 257 ms: 1.15x slower                                                           |
| sympy_str                  | 207 ms                                                              | 241 ms: 1.16x slower                                                           |
| sympy_integrate            | 14.9 ms                                                             | 17.4 ms: 1.17x slower                                                          |
| scimark_sparse_mat_mult    | 3.07 ms                                                             | 3.63 ms: 1.19x slower                                                          |
| sympy_sum                  | 104 ms                                                              | 123 ms: 1.19x slower                                                           |
| deltablue                  | 2.55 ms                                                             | 3.08 ms: 1.21x slower                                                          |
| regex_compile              | 106 ms                                                              | 131 ms: 1.24x slower                                                           |
| comprehensions             | 12.6 us                                                             | 15.7 us: 1.25x slower                                                          |
| hexiom                     | 4.97 ms                                                             | 6.24 ms: 1.26x slower                                                          |
| spectral_norm              | 75.0 ms                                                             | 96.9 ms: 1.29x slower                                                          |
| Geometric mean             | (ref)                                                               | 1.07x slower                                                                   |

Benchmark hidden because not significant (4): deepcopy_reduce, create_gc_cycles, asyncio_tcp, pickle_list
Ignored benchmarks (7) of results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e.json: django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
Ignored benchmarks (2) of results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e.json: dask, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown