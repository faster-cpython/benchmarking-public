# Results vs. 3.13.0b2

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: windows-x86
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 249 ms: 1.07x slower                                                           |
| docutils       | 1.81 sec                                                            | 1.85 sec: 1.02x slower                                                         |
| html5lib       | 45.4 ms                                                             | 47.3 ms: 1.04x slower                                                          |
| tornado_http   | 94.3 ms                                                             | 95.2 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                               | 1.03x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none            | 228 ms                                                              | 221 ms: 1.03x faster                                                           |
| async_tree_io_tg           | 529 ms                                                              | 522 ms: 1.01x faster                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 466 ms: 1.01x faster                                                           |
| async_tree_io              | 530 ms                                                              | 542 ms: 1.02x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 461 ms: 1.03x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.00x faster                                                                   |

Benchmark hidden because not significant (3): async_tree_none_tg, async_tree_memoization_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 52.4 ms                                                             | 61.6 ms: 1.18x slower                                                          |
| nbody          | 76.9 ms                                                             | 94.2 ms: 1.22x slower                                                          |
| Geometric mean | (ref)                                                               | 1.13x slower                                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 118 ms                                                              | 119 ms: 1.01x slower                                                           |
| regex_effbot   | 1.88 ms                                                             | 1.91 ms: 1.01x slower                                                          |
| regex_v8       | 15.7 ms                                                             | 16.3 ms: 1.04x slower                                                          |
| regex_compile  | 99.9 ms                                                             | 109 ms: 1.10x slower                                                           |
| Geometric mean | (ref)                                                               | 1.04x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pickle_list          | 3.57 us                                                             | 3.44 us: 1.04x faster                                                          |
| pickle_dict          | 20.8 us                                                             | 20.4 us: 1.02x faster                                                          |
| pickle               | 8.07 us                                                             | 7.99 us: 1.01x faster                                                          |
| json_loads           | 20.5 us                                                             | 20.7 us: 1.01x slower                                                          |
| unpickle_list        | 2.93 us                                                             | 2.96 us: 1.01x slower                                                          |
| xml_etree_parse      | 104 ms                                                              | 108 ms: 1.04x slower                                                           |
| unpickle             | 9.79 us                                                             | 10.3 us: 1.05x slower                                                          |
| xml_etree_iterparse  | 64.2 ms                                                             | 67.8 ms: 1.06x slower                                                          |
| json_dumps           | 6.84 ms                                                             | 7.43 ms: 1.09x slower                                                          |
| xml_etree_generate   | 59.6 ms                                                             | 67.8 ms: 1.14x slower                                                          |
| tomli_loads          | 1.65 sec                                                            | 1.87 sec: 1.14x slower                                                         |
| xml_etree_process    | 42.1 ms                                                             | 50.1 ms: 1.19x slower                                                          |
| unpickle_pure_python | 147 us                                                              | 179 us: 1.22x slower                                                           |
| pickle_pure_python   | 213 us                                                              | 269 us: 1.26x slower                                                           |
| Geometric mean       | (ref)                                                               | 1.08x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 23.9 ms: 1.08x slower                                                          |
| python_startup_no_site | 18.2 ms                                                             | 20.3 ms: 1.11x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.09x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_text     | 20.1 ms                                                             | 21.7 ms: 1.08x slower                                                          |
| genshi_xml      | 44.3 ms                                                             | 48.9 ms: 1.11x slower                                                          |
| mako            | 6.94 ms                                                             | 8.00 ms: 1.15x slower                                                          |
| django_template | 30.1 ms                                                             | 34.7 ms: 1.15x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.12x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 748 us: 13.00x faster                                                          |
| coverage                   | 307 ms                                                              | 53.2 ms: 5.77x faster                                                          |
| deepcopy                   | 280 us                                                              | 244 us: 1.15x faster                                                           |
| deepcopy_memo              | 23.5 us                                                             | 21.8 us: 1.08x faster                                                          |
| pickle_list                | 3.57 us                                                             | 3.44 us: 1.04x faster                                                          |
| async_tree_none            | 228 ms                                                              | 221 ms: 1.03x faster                                                           |
| create_gc_cycles           | 756 us                                                              | 735 us: 1.03x faster                                                           |
| deepcopy_reduce            | 2.59 us                                                             | 2.53 us: 1.02x faster                                                          |
| pickle_dict                | 20.8 us                                                             | 20.4 us: 1.02x faster                                                          |
| gc_traversal               | 1.43 ms                                                             | 1.41 ms: 1.02x faster                                                          |
| async_tree_io_tg           | 529 ms                                                              | 522 ms: 1.01x faster                                                           |
| pathlib                    | 83.9 ms                                                             | 82.9 ms: 1.01x faster                                                          |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 466 ms: 1.01x faster                                                           |
| pickle                     | 8.07 us                                                             | 7.99 us: 1.01x faster                                                          |
| sqlite_synth               | 1.96 us                                                             | 1.97 us: 1.00x slower                                                          |
| json_loads                 | 20.5 us                                                             | 20.7 us: 1.01x slower                                                          |
| regex_dna                  | 118 ms                                                              | 119 ms: 1.01x slower                                                           |
| tornado_http               | 94.3 ms                                                             | 95.2 ms: 1.01x slower                                                          |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.0 sec: 1.01x slower                                                         |
| unpickle_list              | 2.93 us                                                             | 2.96 us: 1.01x slower                                                          |
| regex_effbot               | 1.88 ms                                                             | 1.91 ms: 1.01x slower                                                          |
| docutils                   | 1.81 sec                                                            | 1.85 sec: 1.02x slower                                                         |
| sympy_sum                  | 105 ms                                                              | 107 ms: 1.02x slower                                                           |
| async_tree_io              | 530 ms                                                              | 542 ms: 1.02x slower                                                           |
| sympy_str                  | 211 ms                                                              | 217 ms: 1.03x slower                                                           |
| sympy_expand               | 375 ms                                                              | 385 ms: 1.03x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 461 ms: 1.03x slower                                                           |
| bench_mp_pool              | 69.4 ms                                                             | 71.5 ms: 1.03x slower                                                          |
| xml_etree_parse            | 104 ms                                                              | 108 ms: 1.04x slower                                                           |
| regex_v8                   | 15.7 ms                                                             | 16.3 ms: 1.04x slower                                                          |
| html5lib                   | 45.4 ms                                                             | 47.3 ms: 1.04x slower                                                          |
| crypto_pyaes               | 55.8 ms                                                             | 58.3 ms: 1.05x slower                                                          |
| json                       | 4.10 ms                                                             | 4.29 ms: 1.05x slower                                                          |
| unpickle                   | 9.79 us                                                             | 10.3 us: 1.05x slower                                                          |
| sympy_integrate            | 14.6 ms                                                             | 15.4 ms: 1.05x slower                                                          |
| pylint                     | 217 ms                                                              | 229 ms: 1.06x slower                                                           |
| xml_etree_iterparse        | 64.2 ms                                                             | 67.8 ms: 1.06x slower                                                          |
| 2to3                       | 233 ms                                                              | 249 ms: 1.07x slower                                                           |
| python_startup             | 22.2 ms                                                             | 23.9 ms: 1.08x slower                                                          |
| genshi_text                | 20.1 ms                                                             | 21.7 ms: 1.08x slower                                                          |
| logging_format             | 8.13 us                                                             | 8.81 us: 1.08x slower                                                          |
| nqueens                    | 68.7 ms                                                             | 74.4 ms: 1.08x slower                                                          |
| json_dumps                 | 6.84 ms                                                             | 7.43 ms: 1.09x slower                                                          |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 3.12 ms: 1.09x slower                                                          |
| typing_runtime_protocols   | 136 us                                                              | 148 us: 1.09x slower                                                           |
| logging_simple             | 7.47 us                                                             | 8.15 us: 1.09x slower                                                          |
| meteor_contest             | 74.1 ms                                                             | 81.0 ms: 1.09x slower                                                          |
| async_generators           | 266 ms                                                              | 291 ms: 1.10x slower                                                           |
| regex_compile              | 99.9 ms                                                             | 109 ms: 1.10x slower                                                           |
| sqlglot_parse              | 964 us                                                              | 1.06 ms: 1.10x slower                                                          |
| pprint_pformat             | 1.24 sec                                                            | 1.37 sec: 1.10x slower                                                         |
| pprint_safe_repr           | 607 ms                                                              | 670 ms: 1.10x slower                                                           |
| genshi_xml                 | 44.3 ms                                                             | 48.9 ms: 1.11x slower                                                          |
| sqlglot_transpile          | 1.19 ms                                                             | 1.32 ms: 1.11x slower                                                          |
| go                         | 101 ms                                                              | 112 ms: 1.11x slower                                                           |
| spectral_norm              | 68.0 ms                                                             | 75.6 ms: 1.11x slower                                                          |
| python_startup_no_site     | 18.2 ms                                                             | 20.3 ms: 1.11x slower                                                          |
| sqlglot_normalize          | 206 ms                                                              | 230 ms: 1.12x slower                                                           |
| sqlglot_optimize           | 39.7 ms                                                             | 44.4 ms: 1.12x slower                                                          |
| mdp                        | 1.60 sec                                                            | 1.80 sec: 1.12x slower                                                         |
| pycparser                  | 777 ms                                                              | 876 ms: 1.13x slower                                                           |
| xml_etree_generate         | 59.6 ms                                                             | 67.8 ms: 1.14x slower                                                          |
| tomli_loads                | 1.65 sec                                                            | 1.87 sec: 1.14x slower                                                         |
| chaos                      | 48.0 ms                                                             | 54.7 ms: 1.14x slower                                                          |
| pyflate                    | 308 ms                                                              | 353 ms: 1.14x slower                                                           |
| mako                       | 6.94 ms                                                             | 8.00 ms: 1.15x slower                                                          |
| django_template            | 30.1 ms                                                             | 34.7 ms: 1.15x slower                                                          |
| scimark_lu                 | 59.4 ms                                                             | 69.0 ms: 1.16x slower                                                          |
| telco                      | 6.03 ms                                                             | 7.04 ms: 1.17x slower                                                          |
| comprehensions             | 11.9 us                                                             | 13.9 us: 1.17x slower                                                          |
| float                      | 52.4 ms                                                             | 61.6 ms: 1.18x slower                                                          |
| fannkuch                   | 270 ms                                                              | 322 ms: 1.19x slower                                                           |
| xml_etree_process          | 42.1 ms                                                             | 50.1 ms: 1.19x slower                                                          |
| scimark_fft                | 198 ms                                                              | 236 ms: 1.19x slower                                                           |
| coroutines                 | 15.5 ms                                                             | 18.5 ms: 1.20x slower                                                          |
| scimark_sor                | 81.0 ms                                                             | 98.3 ms: 1.21x slower                                                          |
| unpickle_pure_python       | 147 us                                                              | 179 us: 1.22x slower                                                           |
| nbody                      | 76.9 ms                                                             | 94.2 ms: 1.22x slower                                                          |
| generators                 | 21.2 ms                                                             | 25.9 ms: 1.23x slower                                                          |
| hexiom                     | 4.23 ms                                                             | 5.27 ms: 1.25x slower                                                          |
| deltablue                  | 2.23 ms                                                             | 2.79 ms: 1.25x slower                                                          |
| scimark_monte_carlo        | 45.2 ms                                                             | 56.9 ms: 1.26x slower                                                          |
| raytrace                   | 189 ms                                                              | 238 ms: 1.26x slower                                                           |
| pickle_pure_python         | 213 us                                                              | 269 us: 1.26x slower                                                           |
| richards                   | 31.2 ms                                                             | 40.0 ms: 1.28x slower                                                          |
| richards_super             | 35.5 ms                                                             | 46.0 ms: 1.30x slower                                                          |
| logging_silent             | 57.9 ns                                                             | 75.0 ns: 1.30x slower                                                          |
| Geometric mean             | (ref)                                                               | 1.03x slower                                                                   |

Benchmark hidden because not significant (6): asyncio_tcp, async_tree_none_tg, async_tree_memoization_tg, pidigits, async_tree_memoization, bench_thread_pool
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging
Ignored benchmarks (2) of results/bm-20240914-3.14.0a0-401fff7/bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: dulwich_log, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown