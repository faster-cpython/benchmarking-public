# Results vs. 3.13.0b2

- fork: python
- ref: 9c4347ef8b60f54dd357
- machine: windows-x86
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.14x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 268 ms: 1.15x slower                                                           |
| chameleon      | 5.71 ms                                                             | 6.15 ms: 1.08x slower                                                          |
| docutils       | 1.81 sec                                                            | 1.94 sec: 1.07x slower                                                         |
| tornado_http   | 94.3 ms                                                             | 112 ms: 1.19x slower                                                           |
| Geometric mean | (ref)                                                               | 1.12x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 471 ms                                                              | 523 ms: 1.11x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 518 ms: 1.16x slower                                                           |
| async_tree_none            | 228 ms                                                              | 270 ms: 1.19x slower                                                           |
| async_tree_memoization     | 275 ms                                                              | 329 ms: 1.19x slower                                                           |
| async_tree_io_tg           | 529 ms                                                              | 634 ms: 1.20x slower                                                           |
| async_tree_io              | 530 ms                                                              | 651 ms: 1.23x slower                                                           |
| async_tree_memoization_tg  | 254 ms                                                              | 327 ms: 1.29x slower                                                           |
| async_tree_none_tg         | 203 ms                                                              | 264 ms: 1.30x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.21x slower                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 52.4 ms                                                             | 62.3 ms: 1.19x slower                                                          |
| nbody          | 76.9 ms                                                             | 91.9 ms: 1.20x slower                                                          |
| Geometric mean | (ref)                                                               | 1.12x slower                                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 15.7 ms                                                             | 16.3 ms: 1.04x slower                                                          |
| regex_effbot   | 1.88 ms                                                             | 2.01 ms: 1.07x slower                                                          |
| regex_dna      | 118 ms                                                              | 132 ms: 1.12x slower                                                           |
| regex_compile  | 99.9 ms                                                             | 131 ms: 1.31x slower                                                           |
| Geometric mean | (ref)                                                               | 1.13x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pickle_list          | 3.57 us                                                             | 3.20 us: 1.11x faster                                                          |
| unpickle_list        | 2.93 us                                                             | 2.69 us: 1.09x faster                                                          |
| pickle               | 8.07 us                                                             | 7.66 us: 1.05x faster                                                          |
| pickle_dict          | 20.8 us                                                             | 19.7 us: 1.05x faster                                                          |
| json_loads           | 20.5 us                                                             | 19.9 us: 1.03x faster                                                          |
| unpickle             | 9.79 us                                                             | 9.65 us: 1.01x faster                                                          |
| json_dumps           | 6.84 ms                                                             | 7.11 ms: 1.04x slower                                                          |
| xml_etree_parse      | 104 ms                                                              | 111 ms: 1.06x slower                                                           |
| tomli_loads          | 1.65 sec                                                            | 1.79 sec: 1.09x slower                                                         |
| pickle_pure_python   | 213 us                                                              | 235 us: 1.10x slower                                                           |
| xml_etree_iterparse  | 64.2 ms                                                             | 71.7 ms: 1.12x slower                                                          |
| xml_etree_generate   | 59.6 ms                                                             | 67.3 ms: 1.13x slower                                                          |
| xml_etree_process    | 42.1 ms                                                             | 47.9 ms: 1.14x slower                                                          |
| unpickle_pure_python | 147 us                                                              | 173 us: 1.18x slower                                                           |
| Geometric mean       | (ref)                                                               | 1.03x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 23.3 ms: 1.05x slower                                                          |
| python_startup_no_site | 18.2 ms                                                             | 21.2 ms: 1.16x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.10x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e |
|-----------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako      | 6.94 ms                                                             | 8.20 ms: 1.18x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols   | 136 us                                                              | 105 us: 1.29x faster                                                           |
| create_gc_cycles           | 756 us                                                              | 648 us: 1.17x faster                                                           |
| pickle_list                | 3.57 us                                                             | 3.20 us: 1.11x faster                                                          |
| unpickle_list              | 2.93 us                                                             | 2.69 us: 1.09x faster                                                          |
| pickle                     | 8.07 us                                                             | 7.66 us: 1.05x faster                                                          |
| pickle_dict                | 20.8 us                                                             | 19.7 us: 1.05x faster                                                          |
| sqlite_synth               | 1.96 us                                                             | 1.87 us: 1.05x faster                                                          |
| json_loads                 | 20.5 us                                                             | 19.9 us: 1.03x faster                                                          |
| gc_traversal               | 1.43 ms                                                             | 1.40 ms: 1.02x faster                                                          |
| unpickle                   | 9.79 us                                                             | 9.65 us: 1.01x faster                                                          |
| deepcopy_reduce            | 2.59 us                                                             | 2.64 us: 1.02x slower                                                          |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.4 sec: 1.03x slower                                                         |
| regex_v8                   | 15.7 ms                                                             | 16.3 ms: 1.04x slower                                                          |
| json_dumps                 | 6.84 ms                                                             | 7.11 ms: 1.04x slower                                                          |
| python_startup             | 22.2 ms                                                             | 23.3 ms: 1.05x slower                                                          |
| crypto_pyaes               | 55.8 ms                                                             | 58.8 ms: 1.05x slower                                                          |
| xml_etree_parse            | 104 ms                                                              | 111 ms: 1.06x slower                                                           |
| telco                      | 6.03 ms                                                             | 6.40 ms: 1.06x slower                                                          |
| pathlib                    | 83.9 ms                                                             | 89.1 ms: 1.06x slower                                                          |
| regex_effbot               | 1.88 ms                                                             | 2.01 ms: 1.07x slower                                                          |
| pprint_safe_repr           | 607 ms                                                              | 649 ms: 1.07x slower                                                           |
| docutils                   | 1.81 sec                                                            | 1.94 sec: 1.07x slower                                                         |
| pprint_pformat             | 1.24 sec                                                            | 1.33 sec: 1.07x slower                                                         |
| chameleon                  | 5.71 ms                                                             | 6.15 ms: 1.08x slower                                                          |
| bench_mp_pool              | 69.4 ms                                                             | 75.2 ms: 1.08x slower                                                          |
| tomli_loads                | 1.65 sec                                                            | 1.79 sec: 1.09x slower                                                         |
| sympy_expand               | 375 ms                                                              | 408 ms: 1.09x slower                                                           |
| sqlglot_parse              | 964 us                                                              | 1.06 ms: 1.10x slower                                                          |
| pickle_pure_python         | 213 us                                                              | 235 us: 1.10x slower                                                           |
| deepcopy                   | 280 us                                                              | 310 us: 1.11x slower                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 523 ms: 1.11x slower                                                           |
| bench_thread_pool          | 985 us                                                              | 1.09 ms: 1.11x slower                                                          |
| regex_dna                  | 118 ms                                                              | 132 ms: 1.12x slower                                                           |
| xml_etree_iterparse        | 64.2 ms                                                             | 71.7 ms: 1.12x slower                                                          |
| sqlglot_transpile          | 1.19 ms                                                             | 1.33 ms: 1.12x slower                                                          |
| meteor_contest             | 74.1 ms                                                             | 83.2 ms: 1.12x slower                                                          |
| logging_format             | 8.13 us                                                             | 9.15 us: 1.12x slower                                                          |
| xml_etree_generate         | 59.6 ms                                                             | 67.3 ms: 1.13x slower                                                          |
| mdp                        | 1.60 sec                                                            | 1.81 sec: 1.13x slower                                                         |
| xml_etree_process          | 42.1 ms                                                             | 47.9 ms: 1.14x slower                                                          |
| richards                   | 31.2 ms                                                             | 35.6 ms: 1.14x slower                                                          |
| async_generators           | 266 ms                                                              | 304 ms: 1.14x slower                                                           |
| richards_super             | 35.5 ms                                                             | 40.6 ms: 1.14x slower                                                          |
| sympy_str                  | 211 ms                                                              | 241 ms: 1.14x slower                                                           |
| logging_simple             | 7.47 us                                                             | 8.58 us: 1.15x slower                                                          |
| sqlglot_normalize          | 206 ms                                                              | 237 ms: 1.15x slower                                                           |
| 2to3                       | 233 ms                                                              | 268 ms: 1.15x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 518 ms: 1.16x slower                                                           |
| python_startup_no_site     | 18.2 ms                                                             | 21.2 ms: 1.16x slower                                                          |
| sympy_sum                  | 105 ms                                                              | 123 ms: 1.17x slower                                                           |
| sqlglot_optimize           | 39.7 ms                                                             | 46.8 ms: 1.18x slower                                                          |
| unpickle_pure_python       | 147 us                                                              | 173 us: 1.18x slower                                                           |
| deepcopy_memo              | 23.5 us                                                             | 27.8 us: 1.18x slower                                                          |
| mako                       | 6.94 ms                                                             | 8.20 ms: 1.18x slower                                                          |
| coroutines                 | 15.5 ms                                                             | 18.3 ms: 1.18x slower                                                          |
| tornado_http               | 94.3 ms                                                             | 112 ms: 1.19x slower                                                           |
| async_tree_none            | 228 ms                                                              | 270 ms: 1.19x slower                                                           |
| fannkuch                   | 270 ms                                                              | 321 ms: 1.19x slower                                                           |
| sympy_integrate            | 14.6 ms                                                             | 17.4 ms: 1.19x slower                                                          |
| float                      | 52.4 ms                                                             | 62.3 ms: 1.19x slower                                                          |
| pyflate                    | 308 ms                                                              | 367 ms: 1.19x slower                                                           |
| chaos                      | 48.0 ms                                                             | 57.2 ms: 1.19x slower                                                          |
| async_tree_memoization     | 275 ms                                                              | 329 ms: 1.19x slower                                                           |
| nbody                      | 76.9 ms                                                             | 91.9 ms: 1.20x slower                                                          |
| async_tree_io_tg           | 529 ms                                                              | 634 ms: 1.20x slower                                                           |
| go                         | 101 ms                                                              | 121 ms: 1.20x slower                                                           |
| scimark_fft                | 198 ms                                                              | 243 ms: 1.22x slower                                                           |
| async_tree_io              | 530 ms                                                              | 651 ms: 1.23x slower                                                           |
| pycparser                  | 777 ms                                                              | 955 ms: 1.23x slower                                                           |
| scimark_sor                | 81.0 ms                                                             | 102 ms: 1.26x slower                                                           |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 3.63 ms: 1.27x slower                                                          |
| scimark_monte_carlo        | 45.2 ms                                                             | 57.8 ms: 1.28x slower                                                          |
| async_tree_memoization_tg  | 254 ms                                                              | 327 ms: 1.29x slower                                                           |
| async_tree_none_tg         | 203 ms                                                              | 264 ms: 1.30x slower                                                           |
| regex_compile              | 99.9 ms                                                             | 131 ms: 1.31x slower                                                           |
| comprehensions             | 11.9 us                                                             | 15.7 us: 1.32x slower                                                          |
| logging_silent             | 57.9 ns                                                             | 76.8 ns: 1.33x slower                                                          |
| nqueens                    | 68.7 ms                                                             | 91.2 ms: 1.33x slower                                                          |
| scimark_lu                 | 59.4 ms                                                             | 79.2 ms: 1.33x slower                                                          |
| raytrace                   | 189 ms                                                              | 257 ms: 1.36x slower                                                           |
| deltablue                  | 2.23 ms                                                             | 3.08 ms: 1.38x slower                                                          |
| generators                 | 21.2 ms                                                             | 29.6 ms: 1.40x slower                                                          |
| spectral_norm              | 68.0 ms                                                             | 96.9 ms: 1.43x slower                                                          |
| hexiom                     | 4.23 ms                                                             | 6.24 ms: 1.48x slower                                                          |
| coverage                   | 307 ms                                                              | 510 ms: 1.66x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.14x slower                                                                   |

Benchmark hidden because not significant (3): asyncio_tcp, pidigits, json
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
Ignored benchmarks (2) of results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e.json: dask, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.13x
- 95% likely to have a slowdown of 1.13x
- 99% likely to have a slowdown of 1.12x

# Memory
- memory change: unknown