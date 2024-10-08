# Results vs. 3.13.0b2

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: windows-x86
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.04x faster
- HPT reliability: 88.66%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 257 ms: 1.10x slower                                                           |
| docutils       | 1.81 sec                                                            | 2.00 sec: 1.10x slower                                                         |
| html5lib       | 45.4 ms                                                             | 47.2 ms: 1.04x slower                                                          |
| tornado_http   | 94.3 ms                                                             | 99.7 ms: 1.06x slower                                                          |
| Geometric mean | (ref)                                                               | 1.07x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none            | 228 ms                                                              | 223 ms: 1.02x faster                                                           |
| async_tree_io_tg           | 529 ms                                                              | 524 ms: 1.01x faster                                                           |
| async_tree_memoization     | 275 ms                                                              | 281 ms: 1.02x slower                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 485 ms: 1.03x slower                                                           |
| async_tree_io              | 530 ms                                                              | 547 ms: 1.03x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 476 ms: 1.06x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.02x slower                                                                   |

Benchmark hidden because not significant (2): async_tree_none_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 50.6 ms: 1.52x faster                                                          |
| float          | 52.4 ms                                                             | 43.8 ms: 1.20x faster                                                          |
| pidigits       | 199 ms                                                              | 195 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                               | 1.23x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 118 ms                                                              | 116 ms: 1.01x faster                                                           |
| regex_v8       | 15.7 ms                                                             | 15.9 ms: 1.01x slower                                                          |
| regex_compile  | 99.9 ms                                                             | 103 ms: 1.03x slower                                                           |
| regex_effbot   | 1.88 ms                                                             | 1.95 ms: 1.04x slower                                                          |
| Geometric mean | (ref)                                                               | 1.02x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_generate   | 59.6 ms                                                             | 52.7 ms: 1.13x faster                                                          |
| tomli_loads          | 1.65 sec                                                            | 1.50 sec: 1.10x faster                                                         |
| pickle_list          | 3.57 us                                                             | 3.29 us: 1.08x faster                                                          |
| xml_etree_process    | 42.1 ms                                                             | 39.5 ms: 1.07x faster                                                          |
| pickle_dict          | 20.8 us                                                             | 19.9 us: 1.04x faster                                                          |
| xml_etree_iterparse  | 64.2 ms                                                             | 61.7 ms: 1.04x faster                                                          |
| json_dumps           | 6.84 ms                                                             | 6.71 ms: 1.02x faster                                                          |
| pickle               | 8.07 us                                                             | 7.94 us: 1.02x faster                                                          |
| xml_etree_parse      | 104 ms                                                              | 104 ms: 1.01x faster                                                           |
| json_loads           | 20.5 us                                                             | 20.6 us: 1.00x slower                                                          |
| unpickle_list        | 2.93 us                                                             | 2.97 us: 1.01x slower                                                          |
| unpickle             | 9.79 us                                                             | 10.3 us: 1.05x slower                                                          |
| unpickle_pure_python | 147 us                                                              | 164 us: 1.11x slower                                                           |
| pickle_pure_python   | 213 us                                                              | 247 us: 1.16x slower                                                           |
| Geometric mean       | (ref)                                                               | 1.01x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 23.7 ms: 1.07x slower                                                          |
| python_startup_no_site | 18.2 ms                                                             | 19.5 ms: 1.07x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.07x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 6.94 ms                                                             | 5.47 ms: 1.27x faster                                                          |
| django_template | 30.1 ms                                                             | 35.1 ms: 1.17x slower                                                          |
| genshi_xml      | 44.3 ms                                                             | 56.0 ms: 1.27x slower                                                          |
| genshi_text     | 20.1 ms                                                             | 25.8 ms: 1.28x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.11x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 768 us: 12.66x faster                                                          |
| coverage                   | 307 ms                                                              | 53.8 ms: 5.71x faster                                                          |
| sqlglot_normalize          | 206 ms                                                              | 100.0 ms: 2.06x faster                                                         |
| deepcopy_memo              | 23.5 us                                                             | 15.2 us: 1.54x faster                                                          |
| nbody                      | 76.9 ms                                                             | 50.6 ms: 1.52x faster                                                          |
| spectral_norm              | 68.0 ms                                                             | 46.0 ms: 1.48x faster                                                          |
| mako                       | 6.94 ms                                                             | 5.47 ms: 1.27x faster                                                          |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 2.39 ms: 1.20x faster                                                          |
| deepcopy                   | 280 us                                                              | 233 us: 1.20x faster                                                           |
| float                      | 52.4 ms                                                             | 43.8 ms: 1.20x faster                                                          |
| scimark_sor                | 81.0 ms                                                             | 68.7 ms: 1.18x faster                                                          |
| crypto_pyaes               | 55.8 ms                                                             | 47.5 ms: 1.17x faster                                                          |
| scimark_fft                | 198 ms                                                              | 174 ms: 1.14x faster                                                           |
| fannkuch                   | 270 ms                                                              | 238 ms: 1.13x faster                                                           |
| xml_etree_generate         | 59.6 ms                                                             | 52.7 ms: 1.13x faster                                                          |
| pyflate                    | 308 ms                                                              | 274 ms: 1.12x faster                                                           |
| tomli_loads                | 1.65 sec                                                            | 1.50 sec: 1.10x faster                                                         |
| pickle_list                | 3.57 us                                                             | 3.29 us: 1.08x faster                                                          |
| asyncio_tcp                | 662 ms                                                              | 612 ms: 1.08x faster                                                           |
| deltablue                  | 2.23 ms                                                             | 2.09 ms: 1.07x faster                                                          |
| xml_etree_process          | 42.1 ms                                                             | 39.5 ms: 1.07x faster                                                          |
| comprehensions             | 11.9 us                                                             | 11.3 us: 1.05x faster                                                          |
| pickle_dict                | 20.8 us                                                             | 19.9 us: 1.04x faster                                                          |
| xml_etree_iterparse        | 64.2 ms                                                             | 61.7 ms: 1.04x faster                                                          |
| deepcopy_reduce            | 2.59 us                                                             | 2.52 us: 1.03x faster                                                          |
| json                       | 4.10 ms                                                             | 4.01 ms: 1.02x faster                                                          |
| async_tree_none            | 228 ms                                                              | 223 ms: 1.02x faster                                                           |
| pathlib                    | 83.9 ms                                                             | 82.2 ms: 1.02x faster                                                          |
| json_dumps                 | 6.84 ms                                                             | 6.71 ms: 1.02x faster                                                          |
| meteor_contest             | 74.1 ms                                                             | 72.7 ms: 1.02x faster                                                          |
| pickle                     | 8.07 us                                                             | 7.94 us: 1.02x faster                                                          |
| pidigits                   | 199 ms                                                              | 195 ms: 1.02x faster                                                           |
| regex_dna                  | 118 ms                                                              | 116 ms: 1.01x faster                                                           |
| sqlite_synth               | 1.96 us                                                             | 1.94 us: 1.01x faster                                                          |
| pprint_safe_repr           | 607 ms                                                              | 600 ms: 1.01x faster                                                           |
| async_tree_io_tg           | 529 ms                                                              | 524 ms: 1.01x faster                                                           |
| xml_etree_parse            | 104 ms                                                              | 104 ms: 1.01x faster                                                           |
| json_loads                 | 20.5 us                                                             | 20.6 us: 1.00x slower                                                          |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.0 sec: 1.01x slower                                                         |
| scimark_lu                 | 59.4 ms                                                             | 59.9 ms: 1.01x slower                                                          |
| regex_v8                   | 15.7 ms                                                             | 15.9 ms: 1.01x slower                                                          |
| unpickle_list              | 2.93 us                                                             | 2.97 us: 1.01x slower                                                          |
| async_tree_memoization     | 275 ms                                                              | 281 ms: 1.02x slower                                                           |
| pprint_pformat             | 1.24 sec                                                            | 1.27 sec: 1.02x slower                                                         |
| go                         | 101 ms                                                              | 103 ms: 1.03x slower                                                           |
| richards_super             | 35.5 ms                                                             | 36.4 ms: 1.03x slower                                                          |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 485 ms: 1.03x slower                                                           |
| telco                      | 6.03 ms                                                             | 6.20 ms: 1.03x slower                                                          |
| regex_compile              | 99.9 ms                                                             | 103 ms: 1.03x slower                                                           |
| async_tree_io              | 530 ms                                                              | 547 ms: 1.03x slower                                                           |
| regex_effbot               | 1.88 ms                                                             | 1.95 ms: 1.04x slower                                                          |
| html5lib                   | 45.4 ms                                                             | 47.2 ms: 1.04x slower                                                          |
| logging_silent             | 57.9 ns                                                             | 60.3 ns: 1.04x slower                                                          |
| logging_format             | 8.13 us                                                             | 8.56 us: 1.05x slower                                                          |
| sympy_str                  | 211 ms                                                              | 222 ms: 1.05x slower                                                           |
| unpickle                   | 9.79 us                                                             | 10.3 us: 1.05x slower                                                          |
| richards                   | 31.2 ms                                                             | 33.0 ms: 1.06x slower                                                          |
| tornado_http               | 94.3 ms                                                             | 99.7 ms: 1.06x slower                                                          |
| logging_simple             | 7.47 us                                                             | 7.93 us: 1.06x slower                                                          |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 476 ms: 1.06x slower                                                           |
| python_startup             | 22.2 ms                                                             | 23.7 ms: 1.07x slower                                                          |
| sympy_expand               | 375 ms                                                              | 402 ms: 1.07x slower                                                           |
| python_startup_no_site     | 18.2 ms                                                             | 19.5 ms: 1.07x slower                                                          |
| pycparser                  | 777 ms                                                              | 839 ms: 1.08x slower                                                           |
| bench_mp_pool              | 69.4 ms                                                             | 75.0 ms: 1.08x slower                                                          |
| sympy_sum                  | 105 ms                                                              | 114 ms: 1.08x slower                                                           |
| sqlglot_parse              | 964 us                                                              | 1.05 ms: 1.09x slower                                                          |
| docutils                   | 1.81 sec                                                            | 2.00 sec: 1.10x slower                                                         |
| 2to3                       | 233 ms                                                              | 257 ms: 1.10x slower                                                           |
| scimark_monte_carlo        | 45.2 ms                                                             | 49.9 ms: 1.10x slower                                                          |
| typing_runtime_protocols   | 136 us                                                              | 151 us: 1.11x slower                                                           |
| unpickle_pure_python       | 147 us                                                              | 164 us: 1.11x slower                                                           |
| generators                 | 21.2 ms                                                             | 24.0 ms: 1.13x slower                                                          |
| chaos                      | 48.0 ms                                                             | 54.6 ms: 1.14x slower                                                          |
| sqlglot_transpile          | 1.19 ms                                                             | 1.36 ms: 1.14x slower                                                          |
| mdp                        | 1.60 sec                                                            | 1.83 sec: 1.14x slower                                                         |
| sympy_integrate            | 14.6 ms                                                             | 16.8 ms: 1.14x slower                                                          |
| nqueens                    | 68.7 ms                                                             | 78.7 ms: 1.15x slower                                                          |
| pickle_pure_python         | 213 us                                                              | 247 us: 1.16x slower                                                           |
| hexiom                     | 4.23 ms                                                             | 4.91 ms: 1.16x slower                                                          |
| django_template            | 30.1 ms                                                             | 35.1 ms: 1.17x slower                                                          |
| sqlglot_optimize           | 39.7 ms                                                             | 46.4 ms: 1.17x slower                                                          |
| coroutines                 | 15.5 ms                                                             | 18.5 ms: 1.19x slower                                                          |
| async_generators           | 266 ms                                                              | 320 ms: 1.20x slower                                                           |
| pylint                     | 217 ms                                                              | 265 ms: 1.22x slower                                                           |
| genshi_xml                 | 44.3 ms                                                             | 56.0 ms: 1.27x slower                                                          |
| genshi_text                | 20.1 ms                                                             | 25.8 ms: 1.28x slower                                                          |
| raytrace                   | 189 ms                                                              | 248 ms: 1.31x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.04x faster                                                                   |

Benchmark hidden because not significant (5): create_gc_cycles, gc_traversal, bench_thread_pool, async_tree_none_tg, async_tree_memoization_tg
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging
Ignored benchmarks (2) of results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: dulwich_log, unpack_sequence

# HPT report

- Reliability score: 88.66% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown