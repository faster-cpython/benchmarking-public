# Results vs. 3.13.0b2

- fork: python
- ref: d27a53fc02a87e76066f
- machine: windows-x86
- commit hash: d27a53f
- commit date: 2024-07-30
- overall geometric mean: 1.01x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 253 ms: 1.08x slower                                                           |
| docutils       | 1.81 sec                                                            | 1.90 sec: 1.05x slower                                                         |
| html5lib       | 45.4 ms                                                             | 47.9 ms: 1.05x slower                                                          |
| tornado_http   | 94.3 ms                                                             | 104 ms: 1.10x slower                                                           |
| Geometric mean | (ref)                                                               | 1.07x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg           | 529 ms                                                              | 500 ms: 1.06x faster                                                           |
| async_tree_none_tg         | 203 ms                                                              | 194 ms: 1.05x faster                                                           |
| async_tree_memoization_tg  | 254 ms                                                              | 245 ms: 1.04x faster                                                           |
| async_tree_none            | 228 ms                                                              | 222 ms: 1.03x faster                                                           |
| async_tree_memoization     | 275 ms                                                              | 270 ms: 1.02x faster                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 490 ms: 1.04x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 478 ms: 1.07x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 199 ms                                                              | 199 ms: 1.00x slower                                                           |
| float          | 52.4 ms                                                             | 59.1 ms: 1.13x slower                                                          |
| nbody          | 76.9 ms                                                             | 91.7 ms: 1.19x slower                                                          |
| Geometric mean | (ref)                                                               | 1.11x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 118 ms                                                              | 119 ms: 1.01x slower                                                           |
| regex_v8       | 15.7 ms                                                             | 16.0 ms: 1.01x slower                                                          |
| regex_effbot   | 1.88 ms                                                             | 1.92 ms: 1.02x slower                                                          |
| regex_compile  | 99.9 ms                                                             | 103 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                               | 1.02x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_parse      | 104 ms                                                              | 106 ms: 1.02x slower                                                           |
| xml_etree_iterparse  | 64.2 ms                                                             | 67.2 ms: 1.05x slower                                                          |
| tomli_loads          | 1.65 sec                                                            | 1.76 sec: 1.07x slower                                                         |
| pickle_pure_python   | 213 us                                                              | 235 us: 1.10x slower                                                           |
| xml_etree_generate   | 59.6 ms                                                             | 66.0 ms: 1.11x slower                                                          |
| json_dumps           | 6.84 ms                                                             | 7.64 ms: 1.12x slower                                                          |
| xml_etree_process    | 42.1 ms                                                             | 47.1 ms: 1.12x slower                                                          |
| unpickle_pure_python | 147 us                                                              | 168 us: 1.14x slower                                                           |
| Geometric mean       | (ref)                                                               | 1.08x slower                                                                   |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 23.7 ms: 1.07x slower                                                          |
| python_startup_no_site | 18.2 ms                                                             | 19.7 ms: 1.08x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.07x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 44.3 ms                                                             | 47.1 ms: 1.07x slower                                                          |
| genshi_text     | 20.1 ms                                                             | 21.7 ms: 1.08x slower                                                          |
| django_template | 30.1 ms                                                             | 34.0 ms: 1.13x slower                                                          |
| mako            | 6.94 ms                                                             | 8.06 ms: 1.16x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.11x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 744 us: 13.07x faster                                                          |
| coverage                   | 307 ms                                                              | 52.0 ms: 5.91x faster                                                          |
| deepcopy                   | 280 us                                                              | 240 us: 1.16x faster                                                           |
| deepcopy_memo              | 23.5 us                                                             | 20.5 us: 1.14x faster                                                          |
| async_tree_io_tg           | 529 ms                                                              | 500 ms: 1.06x faster                                                           |
| async_tree_none_tg         | 203 ms                                                              | 194 ms: 1.05x faster                                                           |
| async_tree_memoization_tg  | 254 ms                                                              | 245 ms: 1.04x faster                                                           |
| async_tree_none            | 228 ms                                                              | 222 ms: 1.03x faster                                                           |
| async_tree_memoization     | 275 ms                                                              | 270 ms: 1.02x faster                                                           |
| deepcopy_reduce            | 2.59 us                                                             | 2.54 us: 1.02x faster                                                          |
| pidigits                   | 199 ms                                                              | 199 ms: 1.00x slower                                                           |
| regex_dna                  | 118 ms                                                              | 119 ms: 1.01x slower                                                           |
| typing_runtime_protocols   | 136 us                                                              | 137 us: 1.01x slower                                                           |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.0 sec: 1.01x slower                                                         |
| regex_v8                   | 15.7 ms                                                             | 16.0 ms: 1.01x slower                                                          |
| regex_effbot               | 1.88 ms                                                             | 1.92 ms: 1.02x slower                                                          |
| xml_etree_parse            | 104 ms                                                              | 106 ms: 1.02x slower                                                           |
| gc_traversal               | 1.43 ms                                                             | 1.46 ms: 1.02x slower                                                          |
| json                       | 4.10 ms                                                             | 4.20 ms: 1.03x slower                                                          |
| sympy_sum                  | 105 ms                                                              | 108 ms: 1.03x slower                                                           |
| regex_compile              | 99.9 ms                                                             | 103 ms: 1.03x slower                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 490 ms: 1.04x slower                                                           |
| sympy_str                  | 211 ms                                                              | 221 ms: 1.05x slower                                                           |
| meteor_contest             | 74.1 ms                                                             | 77.5 ms: 1.05x slower                                                          |
| telco                      | 6.03 ms                                                             | 6.31 ms: 1.05x slower                                                          |
| xml_etree_iterparse        | 64.2 ms                                                             | 67.2 ms: 1.05x slower                                                          |
| sympy_integrate            | 14.6 ms                                                             | 15.3 ms: 1.05x slower                                                          |
| mdp                        | 1.60 sec                                                            | 1.68 sec: 1.05x slower                                                         |
| sympy_expand               | 375 ms                                                              | 393 ms: 1.05x slower                                                           |
| docutils                   | 1.81 sec                                                            | 1.90 sec: 1.05x slower                                                         |
| pathlib                    | 83.9 ms                                                             | 88.1 ms: 1.05x slower                                                          |
| html5lib                   | 45.4 ms                                                             | 47.9 ms: 1.05x slower                                                          |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 3.04 ms: 1.06x slower                                                          |
| bench_mp_pool              | 69.4 ms                                                             | 73.6 ms: 1.06x slower                                                          |
| async_generators           | 266 ms                                                              | 282 ms: 1.06x slower                                                           |
| nqueens                    | 68.7 ms                                                             | 73.1 ms: 1.06x slower                                                          |
| genshi_xml                 | 44.3 ms                                                             | 47.1 ms: 1.07x slower                                                          |
| python_startup             | 22.2 ms                                                             | 23.7 ms: 1.07x slower                                                          |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 478 ms: 1.07x slower                                                           |
| tomli_loads                | 1.65 sec                                                            | 1.76 sec: 1.07x slower                                                         |
| pylint                     | 217 ms                                                              | 232 ms: 1.07x slower                                                           |
| chaos                      | 48.0 ms                                                             | 51.5 ms: 1.07x slower                                                          |
| genshi_text                | 20.1 ms                                                             | 21.7 ms: 1.08x slower                                                          |
| pprint_safe_repr           | 607 ms                                                              | 653 ms: 1.08x slower                                                           |
| python_startup_no_site     | 18.2 ms                                                             | 19.7 ms: 1.08x slower                                                          |
| pyflate                    | 308 ms                                                              | 333 ms: 1.08x slower                                                           |
| sqlglot_parse              | 964 us                                                              | 1.04 ms: 1.08x slower                                                          |
| pprint_pformat             | 1.24 sec                                                            | 1.34 sec: 1.08x slower                                                         |
| 2to3                       | 233 ms                                                              | 253 ms: 1.08x slower                                                           |
| sqlglot_transpile          | 1.19 ms                                                             | 1.30 ms: 1.09x slower                                                          |
| pycparser                  | 777 ms                                                              | 847 ms: 1.09x slower                                                           |
| logging_format             | 8.13 us                                                             | 8.88 us: 1.09x slower                                                          |
| logging_simple             | 7.47 us                                                             | 8.19 us: 1.10x slower                                                          |
| asyncio_tcp                | 662 ms                                                              | 727 ms: 1.10x slower                                                           |
| coroutines                 | 15.5 ms                                                             | 17.0 ms: 1.10x slower                                                          |
| comprehensions             | 11.9 us                                                             | 13.0 us: 1.10x slower                                                          |
| tornado_http               | 94.3 ms                                                             | 104 ms: 1.10x slower                                                           |
| pickle_pure_python         | 213 us                                                              | 235 us: 1.10x slower                                                           |
| go                         | 101 ms                                                              | 111 ms: 1.11x slower                                                           |
| xml_etree_generate         | 59.6 ms                                                             | 66.0 ms: 1.11x slower                                                          |
| richards_super             | 35.5 ms                                                             | 39.4 ms: 1.11x slower                                                          |
| sqlglot_optimize           | 39.7 ms                                                             | 44.1 ms: 1.11x slower                                                          |
| spectral_norm              | 68.0 ms                                                             | 75.6 ms: 1.11x slower                                                          |
| sqlglot_normalize          | 206 ms                                                              | 230 ms: 1.11x slower                                                           |
| scimark_fft                | 198 ms                                                              | 221 ms: 1.12x slower                                                           |
| json_dumps                 | 6.84 ms                                                             | 7.64 ms: 1.12x slower                                                          |
| richards                   | 31.2 ms                                                             | 35.0 ms: 1.12x slower                                                          |
| xml_etree_process          | 42.1 ms                                                             | 47.1 ms: 1.12x slower                                                          |
| scimark_monte_carlo        | 45.2 ms                                                             | 50.7 ms: 1.12x slower                                                          |
| float                      | 52.4 ms                                                             | 59.1 ms: 1.13x slower                                                          |
| django_template            | 30.1 ms                                                             | 34.0 ms: 1.13x slower                                                          |
| unpickle_pure_python       | 147 us                                                              | 168 us: 1.14x slower                                                           |
| deltablue                  | 2.23 ms                                                             | 2.56 ms: 1.15x slower                                                          |
| scimark_lu                 | 59.4 ms                                                             | 68.7 ms: 1.16x slower                                                          |
| mako                       | 6.94 ms                                                             | 8.06 ms: 1.16x slower                                                          |
| hexiom                     | 4.23 ms                                                             | 4.92 ms: 1.16x slower                                                          |
| raytrace                   | 189 ms                                                              | 221 ms: 1.17x slower                                                           |
| fannkuch                   | 270 ms                                                              | 317 ms: 1.17x slower                                                           |
| nbody                      | 76.9 ms                                                             | 91.7 ms: 1.19x slower                                                          |
| scimark_sor                | 81.0 ms                                                             | 98.3 ms: 1.21x slower                                                          |
| generators                 | 21.2 ms                                                             | 25.7 ms: 1.21x slower                                                          |
| logging_silent             | 57.9 ns                                                             | 73.9 ns: 1.28x slower                                                          |
| Geometric mean             | (ref)                                                               | 1.01x slower                                                                   |

Benchmark hidden because not significant (5): json_loads, crypto_pyaes, create_gc_cycles, bench_thread_pool, async_tree_io
Ignored benchmarks (8) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240730-3.14.0a0-d27a53f/bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f.json: dulwich_log

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown