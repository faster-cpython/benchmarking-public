# Results vs. 3.13.0b2

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: windows-x86
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.01x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 254 ms: 1.09x slower                                                           |
| chameleon      | 5.71 ms                                                             | 6.16 ms: 1.08x slower                                                          |
| docutils       | 1.81 sec                                                            | 2.03 sec: 1.12x slower                                                         |
| html5lib       | 45.4 ms                                                             | 50.2 ms: 1.10x slower                                                          |
| tornado_http   | 94.3 ms                                                             | 100 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                               | 1.09x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg           | 529 ms                                                              | 545 ms: 1.03x slower                                                           |
| async_tree_io              | 530 ms                                                              | 546 ms: 1.03x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 461 ms: 1.03x slower                                                           |
| async_tree_memoization     | 275 ms                                                              | 284 ms: 1.03x slower                                                           |
| async_tree_none            | 228 ms                                                              | 236 ms: 1.03x slower                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 488 ms: 1.03x slower                                                           |
| async_tree_none_tg         | 203 ms                                                              | 210 ms: 1.04x slower                                                           |
| async_tree_memoization_tg  | 254 ms                                                              | 263 ms: 1.04x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.03x slower                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 75.6 ms: 1.02x faster                                                          |
| float          | 52.4 ms                                                             | 51.7 ms: 1.01x faster                                                          |
| pidigits       | 199 ms                                                              | 198 ms: 1.00x faster                                                           |
| Geometric mean | (ref)                                                               | 1.01x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 118 ms                                                              | 117 ms: 1.01x faster                                                           |
| regex_v8       | 15.7 ms                                                             | 16.1 ms: 1.02x slower                                                          |
| regex_compile  | 99.9 ms                                                             | 128 ms: 1.28x slower                                                           |
| Geometric mean | (ref)                                                               | 1.07x slower                                                                   |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_loads           | 20.5 us                                                             | 20.3 us: 1.01x faster                                                          |
| tomli_loads          | 1.65 sec                                                            | 1.63 sec: 1.01x faster                                                         |
| xml_etree_parse      | 104 ms                                                              | 104 ms: 1.01x faster                                                           |
| pickle_dict          | 20.8 us                                                             | 20.6 us: 1.01x faster                                                          |
| json_dumps           | 6.84 ms                                                             | 6.97 ms: 1.02x slower                                                          |
| xml_etree_generate   | 59.6 ms                                                             | 60.9 ms: 1.02x slower                                                          |
| xml_etree_process    | 42.1 ms                                                             | 43.4 ms: 1.03x slower                                                          |
| pickle               | 8.07 us                                                             | 8.36 us: 1.04x slower                                                          |
| unpickle             | 9.79 us                                                             | 10.3 us: 1.05x slower                                                          |
| unpickle_list        | 2.93 us                                                             | 3.17 us: 1.08x slower                                                          |
| pickle_pure_python   | 213 us                                                              | 243 us: 1.14x slower                                                           |
| unpickle_pure_python | 147 us                                                              | 170 us: 1.15x slower                                                           |
| Geometric mean       | (ref)                                                               | 1.03x slower                                                                   |

Benchmark hidden because not significant (2): pickle_list, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 18.2 ms                                                             | 18.4 ms: 1.01x slower                                                          |
| python_startup         | 22.2 ms                                                             | 22.7 ms: 1.02x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.02x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 6.94 ms                                                             | 7.12 ms: 1.03x slower                                                          |
| django_template | 30.1 ms                                                             | 32.6 ms: 1.08x slower                                                          |
| genshi_text     | 20.1 ms                                                             | 21.8 ms: 1.09x slower                                                          |
| genshi_xml      | 44.3 ms                                                             | 48.6 ms: 1.10x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.07x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 743 us: 13.09x faster                                                          |
| coverage                   | 307 ms                                                              | 49.7 ms: 6.18x faster                                                          |
| asyncio_tcp                | 662 ms                                                              | 606 ms: 1.09x faster                                                           |
| richards                   | 31.2 ms                                                             | 30.4 ms: 1.03x faster                                                          |
| richards_super             | 35.5 ms                                                             | 34.7 ms: 1.02x faster                                                          |
| sqlite_synth               | 1.96 us                                                             | 1.93 us: 1.02x faster                                                          |
| nbody                      | 76.9 ms                                                             | 75.6 ms: 1.02x faster                                                          |
| telco                      | 6.03 ms                                                             | 5.93 ms: 1.02x faster                                                          |
| json_loads                 | 20.5 us                                                             | 20.3 us: 1.01x faster                                                          |
| tomli_loads                | 1.65 sec                                                            | 1.63 sec: 1.01x faster                                                         |
| float                      | 52.4 ms                                                             | 51.7 ms: 1.01x faster                                                          |
| xml_etree_parse            | 104 ms                                                              | 104 ms: 1.01x faster                                                           |
| pickle_dict                | 20.8 us                                                             | 20.6 us: 1.01x faster                                                          |
| regex_dna                  | 118 ms                                                              | 117 ms: 1.01x faster                                                           |
| pidigits                   | 199 ms                                                              | 198 ms: 1.00x faster                                                           |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.0 sec: 1.01x slower                                                         |
| pprint_pformat             | 1.24 sec                                                            | 1.25 sec: 1.01x slower                                                         |
| python_startup_no_site     | 18.2 ms                                                             | 18.4 ms: 1.01x slower                                                          |
| create_gc_cycles           | 756 us                                                              | 768 us: 1.02x slower                                                           |
| fannkuch                   | 270 ms                                                              | 275 ms: 1.02x slower                                                           |
| json_dumps                 | 6.84 ms                                                             | 6.97 ms: 1.02x slower                                                          |
| python_startup             | 22.2 ms                                                             | 22.7 ms: 1.02x slower                                                          |
| xml_etree_generate         | 59.6 ms                                                             | 60.9 ms: 1.02x slower                                                          |
| coroutines                 | 15.5 ms                                                             | 15.8 ms: 1.02x slower                                                          |
| regex_v8                   | 15.7 ms                                                             | 16.1 ms: 1.02x slower                                                          |
| mako                       | 6.94 ms                                                             | 7.12 ms: 1.03x slower                                                          |
| logging_format             | 8.13 us                                                             | 8.37 us: 1.03x slower                                                          |
| async_tree_io_tg           | 529 ms                                                              | 545 ms: 1.03x slower                                                           |
| logging_simple             | 7.47 us                                                             | 7.68 us: 1.03x slower                                                          |
| async_tree_io              | 530 ms                                                              | 546 ms: 1.03x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 461 ms: 1.03x slower                                                           |
| async_tree_memoization     | 275 ms                                                              | 284 ms: 1.03x slower                                                           |
| xml_etree_process          | 42.1 ms                                                             | 43.4 ms: 1.03x slower                                                          |
| sqlglot_parse              | 964 us                                                              | 997 us: 1.03x slower                                                           |
| async_tree_none            | 228 ms                                                              | 236 ms: 1.03x slower                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 488 ms: 1.03x slower                                                           |
| pickle                     | 8.07 us                                                             | 8.36 us: 1.04x slower                                                          |
| bench_thread_pool          | 985 us                                                              | 1.02 ms: 1.04x slower                                                          |
| async_tree_none_tg         | 203 ms                                                              | 210 ms: 1.04x slower                                                           |
| async_tree_memoization_tg  | 254 ms                                                              | 263 ms: 1.04x slower                                                           |
| mdp                        | 1.60 sec                                                            | 1.67 sec: 1.04x slower                                                         |
| pathlib                    | 83.9 ms                                                             | 87.3 ms: 1.04x slower                                                          |
| spectral_norm              | 68.0 ms                                                             | 70.9 ms: 1.04x slower                                                          |
| crypto_pyaes               | 55.8 ms                                                             | 58.2 ms: 1.04x slower                                                          |
| unpickle                   | 9.79 us                                                             | 10.3 us: 1.05x slower                                                          |
| meteor_contest             | 74.1 ms                                                             | 77.7 ms: 1.05x slower                                                          |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 3.01 ms: 1.05x slower                                                          |
| typing_runtime_protocols   | 136 us                                                              | 143 us: 1.05x slower                                                           |
| bench_mp_pool              | 69.4 ms                                                             | 73.1 ms: 1.05x slower                                                          |
| sqlglot_transpile          | 1.19 ms                                                             | 1.26 ms: 1.05x slower                                                          |
| tornado_http               | 94.3 ms                                                             | 100 ms: 1.06x slower                                                           |
| chaos                      | 48.0 ms                                                             | 51.0 ms: 1.06x slower                                                          |
| scimark_fft                | 198 ms                                                              | 213 ms: 1.07x slower                                                           |
| chameleon                  | 5.71 ms                                                             | 6.16 ms: 1.08x slower                                                          |
| unpickle_list              | 2.93 us                                                             | 3.17 us: 1.08x slower                                                          |
| nqueens                    | 68.7 ms                                                             | 74.4 ms: 1.08x slower                                                          |
| django_template            | 30.1 ms                                                             | 32.6 ms: 1.08x slower                                                          |
| genshi_text                | 20.1 ms                                                             | 21.8 ms: 1.09x slower                                                          |
| generators                 | 21.2 ms                                                             | 23.0 ms: 1.09x slower                                                          |
| 2to3                       | 233 ms                                                              | 254 ms: 1.09x slower                                                           |
| deepcopy                   | 280 us                                                              | 305 us: 1.09x slower                                                           |
| scimark_monte_carlo        | 45.2 ms                                                             | 49.4 ms: 1.09x slower                                                          |
| sqlglot_normalize          | 206 ms                                                              | 226 ms: 1.10x slower                                                           |
| genshi_xml                 | 44.3 ms                                                             | 48.6 ms: 1.10x slower                                                          |
| async_generators           | 266 ms                                                              | 293 ms: 1.10x slower                                                           |
| html5lib                   | 45.4 ms                                                             | 50.2 ms: 1.10x slower                                                          |
| raytrace                   | 189 ms                                                              | 210 ms: 1.11x slower                                                           |
| sqlglot_optimize           | 39.7 ms                                                             | 44.3 ms: 1.12x slower                                                          |
| docutils                   | 1.81 sec                                                            | 2.03 sec: 1.12x slower                                                         |
| sympy_sum                  | 105 ms                                                              | 118 ms: 1.12x slower                                                           |
| pylint                     | 217 ms                                                              | 243 ms: 1.12x slower                                                           |
| sympy_str                  | 211 ms                                                              | 237 ms: 1.13x slower                                                           |
| pycparser                  | 777 ms                                                              | 874 ms: 1.13x slower                                                           |
| deepcopy_reduce            | 2.59 us                                                             | 2.91 us: 1.13x slower                                                          |
| sympy_integrate            | 14.6 ms                                                             | 16.5 ms: 1.13x slower                                                          |
| comprehensions             | 11.9 us                                                             | 13.5 us: 1.14x slower                                                          |
| sympy_expand               | 375 ms                                                              | 428 ms: 1.14x slower                                                           |
| go                         | 101 ms                                                              | 115 ms: 1.14x slower                                                           |
| pickle_pure_python         | 213 us                                                              | 243 us: 1.14x slower                                                           |
| unpickle_pure_python       | 147 us                                                              | 170 us: 1.15x slower                                                           |
| deepcopy_memo              | 23.5 us                                                             | 27.2 us: 1.16x slower                                                          |
| pyflate                    | 308 ms                                                              | 369 ms: 1.20x slower                                                           |
| scimark_sor                | 81.0 ms                                                             | 97.0 ms: 1.20x slower                                                          |
| deltablue                  | 2.23 ms                                                             | 2.83 ms: 1.27x slower                                                          |
| logging_silent             | 57.9 ns                                                             | 73.4 ns: 1.27x slower                                                          |
| regex_compile              | 99.9 ms                                                             | 128 ms: 1.28x slower                                                           |
| hexiom                     | 4.23 ms                                                             | 5.58 ms: 1.32x slower                                                          |
| scimark_lu                 | 59.4 ms                                                             | 78.4 ms: 1.32x slower                                                          |
| Geometric mean             | (ref)                                                               | 1.01x slower                                                                   |

Benchmark hidden because not significant (7): pickle_list, flaskblogging, pprint_safe_repr, regex_effbot, json, gc_traversal, xml_etree_iterparse

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: unknown