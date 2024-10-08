# Results vs. 3.13.0b2

- fork: python
- ref: 11fa11987990eb7ed75b
- machine: windows-x86
- commit hash: 11fa119
- commit date: 2024-09-07
- overall geometric mean: 1.04x faster
- HPT reliability: 90.66%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 264 ms: 1.13x slower                                                           |
| docutils       | 1.81 sec                                                            | 2.01 sec: 1.11x slower                                                         |
| html5lib       | 45.4 ms                                                             | 46.3 ms: 1.02x slower                                                          |
| tornado_http   | 94.3 ms                                                             | 110 ms: 1.16x slower                                                           |
| Geometric mean | (ref)                                                               | 1.10x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none            | 228 ms                                                              | 220 ms: 1.04x faster                                                           |
| async_tree_io              | 530 ms                                                              | 544 ms: 1.03x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 465 ms: 1.04x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.00x slower                                                                   |

Benchmark hidden because not significant (5): async_tree_none_tg, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 50.1 ms: 1.53x faster                                                          |
| float          | 52.4 ms                                                             | 44.5 ms: 1.18x faster                                                          |
| Geometric mean | (ref)                                                               | 1.22x faster                                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 15.7 ms                                                             | 15.9 ms: 1.01x slower                                                          |
| regex_compile  | 99.9 ms                                                             | 101 ms: 1.01x slower                                                           |
| regex_effbot   | 1.88 ms                                                             | 2.00 ms: 1.06x slower                                                          |
| regex_dna      | 118 ms                                                              | 129 ms: 1.09x slower                                                           |
| Geometric mean | (ref)                                                               | 1.04x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_generate   | 59.6 ms                                                             | 53.3 ms: 1.12x faster                                                          |
| tomli_loads          | 1.65 sec                                                            | 1.48 sec: 1.11x faster                                                         |
| unpickle_list        | 2.93 us                                                             | 2.79 us: 1.05x faster                                                          |
| xml_etree_process    | 42.1 ms                                                             | 40.1 ms: 1.05x faster                                                          |
| pickle_list          | 3.57 us                                                             | 3.43 us: 1.04x faster                                                          |
| pickle               | 8.07 us                                                             | 7.84 us: 1.03x faster                                                          |
| xml_etree_iterparse  | 64.2 ms                                                             | 62.4 ms: 1.03x faster                                                          |
| pickle_dict          | 20.8 us                                                             | 20.2 us: 1.03x faster                                                          |
| json_dumps           | 6.84 ms                                                             | 6.92 ms: 1.01x slower                                                          |
| unpickle             | 9.79 us                                                             | 10.6 us: 1.08x slower                                                          |
| unpickle_pure_python | 147 us                                                              | 161 us: 1.10x slower                                                           |
| pickle_pure_python   | 213 us                                                              | 241 us: 1.13x slower                                                           |
| Geometric mean       | (ref)                                                               | 1.01x faster                                                                   |

Benchmark hidden because not significant (2): json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 25.0 ms: 1.12x slower                                                          |
| python_startup_no_site | 18.2 ms                                                             | 20.9 ms: 1.15x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.13x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 6.94 ms                                                             | 5.57 ms: 1.25x faster                                                          |
| django_template | 30.1 ms                                                             | 33.5 ms: 1.11x slower                                                          |
| genshi_text     | 20.1 ms                                                             | 23.7 ms: 1.18x slower                                                          |
| genshi_xml      | 44.3 ms                                                             | 55.6 ms: 1.26x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.07x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 756 us: 12.86x faster                                                          |
| coverage                   | 307 ms                                                              | 54.7 ms: 5.62x faster                                                          |
| sqlglot_normalize          | 206 ms                                                              | 100 ms: 2.05x faster                                                           |
| nbody                      | 76.9 ms                                                             | 50.1 ms: 1.53x faster                                                          |
| deepcopy_memo              | 23.5 us                                                             | 15.7 us: 1.50x faster                                                          |
| spectral_norm              | 68.0 ms                                                             | 49.2 ms: 1.38x faster                                                          |
| mako                       | 6.94 ms                                                             | 5.57 ms: 1.25x faster                                                          |
| deepcopy                   | 280 us                                                              | 232 us: 1.20x faster                                                           |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 2.40 ms: 1.20x faster                                                          |
| scimark_sor                | 81.0 ms                                                             | 68.1 ms: 1.19x faster                                                          |
| float                      | 52.4 ms                                                             | 44.5 ms: 1.18x faster                                                          |
| scimark_fft                | 198 ms                                                              | 172 ms: 1.15x faster                                                           |
| crypto_pyaes               | 55.8 ms                                                             | 48.4 ms: 1.15x faster                                                          |
| fannkuch                   | 270 ms                                                              | 237 ms: 1.14x faster                                                           |
| pyflate                    | 308 ms                                                              | 275 ms: 1.12x faster                                                           |
| xml_etree_generate         | 59.6 ms                                                             | 53.3 ms: 1.12x faster                                                          |
| tomli_loads                | 1.65 sec                                                            | 1.48 sec: 1.11x faster                                                         |
| deltablue                  | 2.23 ms                                                             | 2.04 ms: 1.10x faster                                                          |
| pprint_safe_repr           | 607 ms                                                              | 574 ms: 1.06x faster                                                           |
| sqlite_synth               | 1.96 us                                                             | 1.86 us: 1.06x faster                                                          |
| unpickle_list              | 2.93 us                                                             | 2.79 us: 1.05x faster                                                          |
| xml_etree_process          | 42.1 ms                                                             | 40.1 ms: 1.05x faster                                                          |
| pickle_list                | 3.57 us                                                             | 3.43 us: 1.04x faster                                                          |
| async_tree_none            | 228 ms                                                              | 220 ms: 1.04x faster                                                           |
| pprint_pformat             | 1.24 sec                                                            | 1.20 sec: 1.03x faster                                                         |
| pickle                     | 8.07 us                                                             | 7.84 us: 1.03x faster                                                          |
| xml_etree_iterparse        | 64.2 ms                                                             | 62.4 ms: 1.03x faster                                                          |
| deepcopy_reduce            | 2.59 us                                                             | 2.52 us: 1.03x faster                                                          |
| pickle_dict                | 20.8 us                                                             | 20.2 us: 1.03x faster                                                          |
| go                         | 101 ms                                                              | 98.9 ms: 1.02x faster                                                          |
| json                       | 4.10 ms                                                             | 4.03 ms: 1.02x faster                                                          |
| telco                      | 6.03 ms                                                             | 5.93 ms: 1.02x faster                                                          |
| meteor_contest             | 74.1 ms                                                             | 74.5 ms: 1.01x slower                                                          |
| regex_v8                   | 15.7 ms                                                             | 15.9 ms: 1.01x slower                                                          |
| comprehensions             | 11.9 us                                                             | 12.0 us: 1.01x slower                                                          |
| regex_compile              | 99.9 ms                                                             | 101 ms: 1.01x slower                                                           |
| json_dumps                 | 6.84 ms                                                             | 6.92 ms: 1.01x slower                                                          |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.1 sec: 1.01x slower                                                         |
| scimark_lu                 | 59.4 ms                                                             | 60.3 ms: 1.02x slower                                                          |
| html5lib                   | 45.4 ms                                                             | 46.3 ms: 1.02x slower                                                          |
| richards_super             | 35.5 ms                                                             | 36.2 ms: 1.02x slower                                                          |
| async_tree_io              | 530 ms                                                              | 544 ms: 1.03x slower                                                           |
| logging_simple             | 7.47 us                                                             | 7.75 us: 1.04x slower                                                          |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 465 ms: 1.04x slower                                                           |
| logging_format             | 8.13 us                                                             | 8.46 us: 1.04x slower                                                          |
| pathlib                    | 83.9 ms                                                             | 87.4 ms: 1.04x slower                                                          |
| mdp                        | 1.60 sec                                                            | 1.68 sec: 1.05x slower                                                         |
| richards                   | 31.2 ms                                                             | 32.9 ms: 1.05x slower                                                          |
| pycparser                  | 777 ms                                                              | 821 ms: 1.06x slower                                                           |
| sympy_str                  | 211 ms                                                              | 224 ms: 1.06x slower                                                           |
| regex_effbot               | 1.88 ms                                                             | 2.00 ms: 1.06x slower                                                          |
| logging_silent             | 57.9 ns                                                             | 61.5 ns: 1.06x slower                                                          |
| typing_runtime_protocols   | 136 us                                                              | 145 us: 1.07x slower                                                           |
| sympy_expand               | 375 ms                                                              | 402 ms: 1.07x slower                                                           |
| sqlglot_parse              | 964 us                                                              | 1.04 ms: 1.08x slower                                                          |
| unpickle                   | 9.79 us                                                             | 10.6 us: 1.08x slower                                                          |
| regex_dna                  | 118 ms                                                              | 129 ms: 1.09x slower                                                           |
| unpickle_pure_python       | 147 us                                                              | 161 us: 1.10x slower                                                           |
| sympy_sum                  | 105 ms                                                              | 115 ms: 1.10x slower                                                           |
| scimark_monte_carlo        | 45.2 ms                                                             | 49.6 ms: 1.10x slower                                                          |
| docutils                   | 1.81 sec                                                            | 2.01 sec: 1.11x slower                                                         |
| django_template            | 30.1 ms                                                             | 33.5 ms: 1.11x slower                                                          |
| generators                 | 21.2 ms                                                             | 23.6 ms: 1.12x slower                                                          |
| python_startup             | 22.2 ms                                                             | 25.0 ms: 1.12x slower                                                          |
| 2to3                       | 233 ms                                                              | 264 ms: 1.13x slower                                                           |
| pickle_pure_python         | 213 us                                                              | 241 us: 1.13x slower                                                           |
| sqlglot_transpile          | 1.19 ms                                                             | 1.35 ms: 1.13x slower                                                          |
| sympy_integrate            | 14.6 ms                                                             | 16.8 ms: 1.15x slower                                                          |
| python_startup_no_site     | 18.2 ms                                                             | 20.9 ms: 1.15x slower                                                          |
| chaos                      | 48.0 ms                                                             | 55.0 ms: 1.15x slower                                                          |
| nqueens                    | 68.7 ms                                                             | 79.3 ms: 1.16x slower                                                          |
| bench_mp_pool              | 69.4 ms                                                             | 80.2 ms: 1.16x slower                                                          |
| tornado_http               | 94.3 ms                                                             | 110 ms: 1.16x slower                                                           |
| hexiom                     | 4.23 ms                                                             | 4.96 ms: 1.17x slower                                                          |
| sqlglot_optimize           | 39.7 ms                                                             | 46.8 ms: 1.18x slower                                                          |
| genshi_text                | 20.1 ms                                                             | 23.7 ms: 1.18x slower                                                          |
| coroutines                 | 15.5 ms                                                             | 18.5 ms: 1.19x slower                                                          |
| async_generators           | 266 ms                                                              | 322 ms: 1.21x slower                                                           |
| pylint                     | 217 ms                                                              | 270 ms: 1.25x slower                                                           |
| genshi_xml                 | 44.3 ms                                                             | 55.6 ms: 1.26x slower                                                          |
| raytrace                   | 189 ms                                                              | 248 ms: 1.32x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.04x faster                                                                   |

Benchmark hidden because not significant (12): async_tree_none_tg, async_tree_io_tg, create_gc_cycles, pidigits, async_tree_cpu_io_mixed, async_tree_memoization, json_loads, gc_traversal, xml_etree_parse, async_tree_memoization_tg, bench_thread_pool, asyncio_tcp
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging
Ignored benchmarks (2) of results/bm-20240907-3.14.0a0-11fa119-JIT/bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json: dulwich_log, unpack_sequence

# HPT report

- Reliability score: 90.66% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown