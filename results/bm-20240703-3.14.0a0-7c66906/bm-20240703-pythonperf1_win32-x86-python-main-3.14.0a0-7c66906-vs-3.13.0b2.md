# Results vs. 3.13.0b2

- fork: python
- ref: main
- machine: windows-x86
- commit hash: 7c66906
- commit date: 2024-07-03
- overall geometric mean: 1.01x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-pythonperf1_win32-x86-python-main-3.14.0a0-7c66906 |
|----------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 249 ms: 1.07x slower                                           |
| docutils       | 1.81 sec                                                            | 1.87 sec: 1.03x slower                                         |
| html5lib       | 45.4 ms                                                             | 48.2 ms: 1.06x slower                                          |
| tornado_http   | 94.3 ms                                                             | 95.4 ms: 1.01x slower                                          |
| Geometric mean | (ref)                                                               | 1.04x slower                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-pythonperf1_win32-x86-python-main-3.14.0a0-7c66906 |
|----------------------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_io_tg           | 529 ms                                                              | 494 ms: 1.07x faster                                           |
| async_tree_none_tg         | 203 ms                                                              | 192 ms: 1.06x faster                                           |
| async_tree_memoization_tg  | 254 ms                                                              | 242 ms: 1.05x faster                                           |
| async_tree_none            | 228 ms                                                              | 221 ms: 1.03x faster                                           |
| async_tree_memoization     | 275 ms                                                              | 270 ms: 1.02x faster                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 463 ms: 1.02x faster                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 455 ms: 1.02x slower                                           |
| Geometric mean             | (ref)                                                               | 1.03x faster                                                   |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-pythonperf1_win32-x86-python-main-3.14.0a0-7c66906 |
|----------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------:|
| pidigits       | 199 ms                                                              | 200 ms: 1.01x slower                                           |
| float          | 52.4 ms                                                             | 60.0 ms: 1.15x slower                                          |
| nbody          | 76.9 ms                                                             | 93.9 ms: 1.22x slower                                          |
| Geometric mean | (ref)                                                               | 1.12x slower                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-pythonperf1_win32-x86-python-main-3.14.0a0-7c66906 |
|----------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_effbot   | 1.88 ms                                                             | 1.87 ms: 1.01x faster                                          |
| regex_dna      | 118 ms                                                              | 119 ms: 1.01x slower                                           |
| regex_v8       | 15.7 ms                                                             | 15.9 ms: 1.01x slower                                          |
| regex_compile  | 99.9 ms                                                             | 106 ms: 1.06x slower                                           |
| Geometric mean | (ref)                                                               | 1.02x slower                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-pythonperf1_win32-x86-python-main-3.14.0a0-7c66906 |
|----------------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------:|
| json_loads           | 20.5 us                                                             | 20.4 us: 1.01x faster                                          |
| xml_etree_parse      | 104 ms                                                              | 105 ms: 1.01x slower                                           |
| json_dumps           | 6.84 ms                                                             | 6.93 ms: 1.01x slower                                          |
| xml_etree_iterparse  | 64.2 ms                                                             | 67.1 ms: 1.05x slower                                          |
| tomli_loads          | 1.65 sec                                                            | 1.77 sec: 1.07x slower                                         |
| xml_etree_generate   | 59.6 ms                                                             | 66.0 ms: 1.11x slower                                          |
| pickle_pure_python   | 213 us                                                              | 245 us: 1.15x slower                                           |
| unpickle_pure_python | 147 us                                                              | 170 us: 1.15x slower                                           |
| xml_etree_process    | 42.1 ms                                                             | 49.8 ms: 1.18x slower                                          |
| Geometric mean       | (ref)                                                               | 1.08x slower                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-pythonperf1_win32-x86-python-main-3.14.0a0-7c66906 |
|------------------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 23.1 ms: 1.04x slower                                          |
| python_startup_no_site | 18.2 ms                                                             | 19.0 ms: 1.04x slower                                          |
| Geometric mean         | (ref)                                                               | 1.04x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-pythonperf1_win32-x86-python-main-3.14.0a0-7c66906 |
|-----------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------:|
| genshi_xml      | 44.3 ms                                                             | 46.6 ms: 1.05x slower                                          |
| genshi_text     | 20.1 ms                                                             | 21.9 ms: 1.09x slower                                          |
| django_template | 30.1 ms                                                             | 33.2 ms: 1.11x slower                                          |
| mako            | 6.94 ms                                                             | 7.93 ms: 1.14x slower                                          |
| Geometric mean  | (ref)                                                               | 1.10x slower                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-pythonperf1_win32-x86-python-main-3.14.0a0-7c66906 |
|----------------------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 763 us: 12.76x faster                                          |
| coverage                   | 307 ms                                                              | 51.3 ms: 5.99x faster                                          |
| deepcopy                   | 280 us                                                              | 241 us: 1.16x faster                                           |
| deepcopy_memo              | 23.5 us                                                             | 21.6 us: 1.09x faster                                          |
| async_tree_io_tg           | 529 ms                                                              | 494 ms: 1.07x faster                                           |
| deepcopy_reduce            | 2.59 us                                                             | 2.45 us: 1.06x faster                                          |
| async_tree_none_tg         | 203 ms                                                              | 192 ms: 1.06x faster                                           |
| async_tree_memoization_tg  | 254 ms                                                              | 242 ms: 1.05x faster                                           |
| async_tree_none            | 228 ms                                                              | 221 ms: 1.03x faster                                           |
| async_tree_memoization     | 275 ms                                                              | 270 ms: 1.02x faster                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 463 ms: 1.02x faster                                           |
| bench_thread_pool          | 985 us                                                              | 971 us: 1.01x faster                                           |
| json_loads                 | 20.5 us                                                             | 20.4 us: 1.01x faster                                          |
| regex_effbot               | 1.88 ms                                                             | 1.87 ms: 1.01x faster                                          |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 16.8 sec: 1.01x faster                                         |
| regex_dna                  | 118 ms                                                              | 119 ms: 1.01x slower                                           |
| pidigits                   | 199 ms                                                              | 200 ms: 1.01x slower                                           |
| xml_etree_parse            | 104 ms                                                              | 105 ms: 1.01x slower                                           |
| regex_v8                   | 15.7 ms                                                             | 15.9 ms: 1.01x slower                                          |
| json                       | 4.10 ms                                                             | 4.14 ms: 1.01x slower                                          |
| tornado_http               | 94.3 ms                                                             | 95.4 ms: 1.01x slower                                          |
| json_dumps                 | 6.84 ms                                                             | 6.93 ms: 1.01x slower                                          |
| bench_mp_pool              | 69.4 ms                                                             | 70.4 ms: 1.01x slower                                          |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 455 ms: 1.02x slower                                           |
| sympy_expand               | 375 ms                                                              | 383 ms: 1.02x slower                                           |
| sympy_str                  | 211 ms                                                              | 217 ms: 1.03x slower                                           |
| docutils                   | 1.81 sec                                                            | 1.87 sec: 1.03x slower                                         |
| sympy_sum                  | 105 ms                                                              | 109 ms: 1.03x slower                                           |
| crypto_pyaes               | 55.8 ms                                                             | 57.7 ms: 1.03x slower                                          |
| python_startup             | 22.2 ms                                                             | 23.1 ms: 1.04x slower                                          |
| python_startup_no_site     | 18.2 ms                                                             | 19.0 ms: 1.04x slower                                          |
| xml_etree_iterparse        | 64.2 ms                                                             | 67.1 ms: 1.05x slower                                          |
| mdp                        | 1.60 sec                                                            | 1.68 sec: 1.05x slower                                         |
| logging_simple             | 7.47 us                                                             | 7.82 us: 1.05x slower                                          |
| logging_format             | 8.13 us                                                             | 8.52 us: 1.05x slower                                          |
| pylint                     | 217 ms                                                              | 228 ms: 1.05x slower                                           |
| pprint_pformat             | 1.24 sec                                                            | 1.30 sec: 1.05x slower                                         |
| pprint_safe_repr           | 607 ms                                                              | 638 ms: 1.05x slower                                           |
| genshi_xml                 | 44.3 ms                                                             | 46.6 ms: 1.05x slower                                          |
| sympy_integrate            | 14.6 ms                                                             | 15.4 ms: 1.05x slower                                          |
| regex_compile              | 99.9 ms                                                             | 106 ms: 1.06x slower                                           |
| html5lib                   | 45.4 ms                                                             | 48.2 ms: 1.06x slower                                          |
| 2to3                       | 233 ms                                                              | 249 ms: 1.07x slower                                           |
| tomli_loads                | 1.65 sec                                                            | 1.77 sec: 1.07x slower                                         |
| meteor_contest             | 74.1 ms                                                             | 79.7 ms: 1.08x slower                                          |
| async_generators           | 266 ms                                                              | 287 ms: 1.08x slower                                           |
| sqlglot_transpile          | 1.19 ms                                                             | 1.29 ms: 1.08x slower                                          |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 3.10 ms: 1.08x slower                                          |
| sqlglot_parse              | 964 us                                                              | 1.04 ms: 1.08x slower                                          |
| pycparser                  | 777 ms                                                              | 841 ms: 1.08x slower                                           |
| genshi_text                | 20.1 ms                                                             | 21.9 ms: 1.09x slower                                          |
| chaos                      | 48.0 ms                                                             | 52.6 ms: 1.10x slower                                          |
| pyflate                    | 308 ms                                                              | 338 ms: 1.10x slower                                           |
| sqlglot_optimize           | 39.7 ms                                                             | 43.7 ms: 1.10x slower                                          |
| nqueens                    | 68.7 ms                                                             | 75.5 ms: 1.10x slower                                          |
| django_template            | 30.1 ms                                                             | 33.2 ms: 1.11x slower                                          |
| xml_etree_generate         | 59.6 ms                                                             | 66.0 ms: 1.11x slower                                          |
| sqlglot_normalize          | 206 ms                                                              | 228 ms: 1.11x slower                                           |
| spectral_norm              | 68.0 ms                                                             | 75.3 ms: 1.11x slower                                          |
| scimark_fft                | 198 ms                                                              | 220 ms: 1.11x slower                                           |
| typing_runtime_protocols   | 136 us                                                              | 151 us: 1.11x slower                                           |
| go                         | 101 ms                                                              | 114 ms: 1.13x slower                                           |
| coroutines                 | 15.5 ms                                                             | 17.5 ms: 1.13x slower                                          |
| mako                       | 6.94 ms                                                             | 7.93 ms: 1.14x slower                                          |
| comprehensions             | 11.9 us                                                             | 13.6 us: 1.14x slower                                          |
| float                      | 52.4 ms                                                             | 60.0 ms: 1.15x slower                                          |
| pickle_pure_python         | 213 us                                                              | 245 us: 1.15x slower                                           |
| scimark_lu                 | 59.4 ms                                                             | 68.4 ms: 1.15x slower                                          |
| unpickle_pure_python       | 147 us                                                              | 170 us: 1.15x slower                                           |
| raytrace                   | 189 ms                                                              | 220 ms: 1.17x slower                                           |
| fannkuch                   | 270 ms                                                              | 318 ms: 1.18x slower                                           |
| xml_etree_process          | 42.1 ms                                                             | 49.8 ms: 1.18x slower                                          |
| richards                   | 31.2 ms                                                             | 37.1 ms: 1.19x slower                                          |
| deltablue                  | 2.23 ms                                                             | 2.66 ms: 1.19x slower                                          |
| scimark_monte_carlo        | 45.2 ms                                                             | 54.0 ms: 1.19x slower                                          |
| richards_super             | 35.5 ms                                                             | 42.5 ms: 1.20x slower                                          |
| hexiom                     | 4.23 ms                                                             | 5.12 ms: 1.21x slower                                          |
| scimark_sor                | 81.0 ms                                                             | 98.4 ms: 1.22x slower                                          |
| nbody                      | 76.9 ms                                                             | 93.9 ms: 1.22x slower                                          |
| generators                 | 21.2 ms                                                             | 27.0 ms: 1.27x slower                                          |
| logging_silent             | 57.9 ns                                                             | 74.2 ns: 1.28x slower                                          |
| Geometric mean             | (ref)                                                               | 1.01x slower                                                   |

Benchmark hidden because not significant (6): create_gc_cycles, pathlib, telco, asyncio_tcp, gc_traversal, async_tree_io
Ignored benchmarks (8) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown