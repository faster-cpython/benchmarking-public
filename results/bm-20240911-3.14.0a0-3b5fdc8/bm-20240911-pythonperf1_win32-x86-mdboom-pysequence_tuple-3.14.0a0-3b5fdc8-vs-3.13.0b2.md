# Results vs. 3.13.0b2

- fork: mdboom
- ref: pysequence_tuple
- machine: windows-x86
- commit hash: 3b5fdc8
- commit date: 2024-09-11
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 248 ms: 1.07x slower                                                       |
| docutils       | 1.81 sec                                                            | 1.86 sec: 1.02x slower                                                     |
| html5lib       | 45.4 ms                                                             | 45.7 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                               | 1.02x slower                                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 203 ms                                                              | 208 ms: 1.03x slower                                                       |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 488 ms: 1.04x slower                                                       |
| async_tree_io              | 530 ms                                                              | 551 ms: 1.04x slower                                                       |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 473 ms: 1.06x slower                                                       |
| Geometric mean             | (ref)                                                               | 1.02x slower                                                               |

Benchmark hidden because not significant (4): async_tree_none, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 199 ms                                                              | 197 ms: 1.01x faster                                                       |
| float          | 52.4 ms                                                             | 61.0 ms: 1.16x slower                                                      |
| nbody          | 76.9 ms                                                             | 91.4 ms: 1.19x slower                                                      |
| Geometric mean | (ref)                                                               | 1.11x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 118 ms                                                              | 117 ms: 1.01x faster                                                       |
| regex_effbot   | 1.88 ms                                                             | 1.91 ms: 1.01x slower                                                      |
| regex_v8       | 15.7 ms                                                             | 16.4 ms: 1.04x slower                                                      |
| regex_compile  | 99.9 ms                                                             | 107 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                               | 1.03x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_list          | 3.57 us                                                             | 3.34 us: 1.07x faster                                                      |
| pickle_dict          | 20.8 us                                                             | 20.3 us: 1.02x faster                                                      |
| pickle               | 8.07 us                                                             | 7.94 us: 1.02x faster                                                      |
| json_loads           | 20.5 us                                                             | 20.9 us: 1.02x slower                                                      |
| xml_etree_parse      | 104 ms                                                              | 107 ms: 1.03x slower                                                       |
| xml_etree_iterparse  | 64.2 ms                                                             | 66.8 ms: 1.04x slower                                                      |
| unpickle             | 9.79 us                                                             | 10.5 us: 1.08x slower                                                      |
| tomli_loads          | 1.65 sec                                                            | 1.85 sec: 1.12x slower                                                     |
| json_dumps           | 6.84 ms                                                             | 7.70 ms: 1.13x slower                                                      |
| xml_etree_generate   | 59.6 ms                                                             | 69.2 ms: 1.16x slower                                                      |
| pickle_pure_python   | 213 us                                                              | 256 us: 1.20x slower                                                       |
| xml_etree_process    | 42.1 ms                                                             | 50.7 ms: 1.20x slower                                                      |
| unpickle_pure_python | 147 us                                                              | 182 us: 1.23x slower                                                       |
| Geometric mean       | (ref)                                                               | 1.08x slower                                                               |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|------------------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 23.6 ms: 1.06x slower                                                      |
| python_startup_no_site | 18.2 ms                                                             | 19.4 ms: 1.06x slower                                                      |
| Geometric mean         | (ref)                                                               | 1.06x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|-----------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 44.3 ms                                                             | 47.0 ms: 1.06x slower                                                      |
| django_template | 30.1 ms                                                             | 32.4 ms: 1.08x slower                                                      |
| genshi_text     | 20.1 ms                                                             | 22.2 ms: 1.11x slower                                                      |
| mako            | 6.94 ms                                                             | 8.08 ms: 1.16x slower                                                      |
| Geometric mean  | (ref)                                                               | 1.10x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 763 us: 12.75x faster                                                      |
| coverage                   | 307 ms                                                              | 53.1 ms: 5.78x faster                                                      |
| deepcopy                   | 280 us                                                              | 242 us: 1.16x faster                                                       |
| pickle_list                | 3.57 us                                                             | 3.34 us: 1.07x faster                                                      |
| deepcopy_memo              | 23.5 us                                                             | 22.0 us: 1.07x faster                                                      |
| deepcopy_reduce            | 2.59 us                                                             | 2.49 us: 1.04x faster                                                      |
| pickle_dict                | 20.8 us                                                             | 20.3 us: 1.02x faster                                                      |
| pathlib                    | 83.9 ms                                                             | 82.1 ms: 1.02x faster                                                      |
| create_gc_cycles           | 756 us                                                              | 741 us: 1.02x faster                                                       |
| pickle                     | 8.07 us                                                             | 7.94 us: 1.02x faster                                                      |
| gc_traversal               | 1.43 ms                                                             | 1.42 ms: 1.01x faster                                                      |
| pidigits                   | 199 ms                                                              | 197 ms: 1.01x faster                                                       |
| regex_dna                  | 118 ms                                                              | 117 ms: 1.01x faster                                                       |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.0 sec: 1.01x slower                                                     |
| html5lib                   | 45.4 ms                                                             | 45.7 ms: 1.01x slower                                                      |
| sqlite_synth               | 1.96 us                                                             | 1.98 us: 1.01x slower                                                      |
| regex_effbot               | 1.88 ms                                                             | 1.91 ms: 1.01x slower                                                      |
| crypto_pyaes               | 55.8 ms                                                             | 56.8 ms: 1.02x slower                                                      |
| json_loads                 | 20.5 us                                                             | 20.9 us: 1.02x slower                                                      |
| go                         | 101 ms                                                              | 103 ms: 1.02x slower                                                       |
| sympy_sum                  | 105 ms                                                              | 107 ms: 1.02x slower                                                       |
| docutils                   | 1.81 sec                                                            | 1.86 sec: 1.02x slower                                                     |
| xml_etree_parse            | 104 ms                                                              | 107 ms: 1.03x slower                                                       |
| telco                      | 6.03 ms                                                             | 6.19 ms: 1.03x slower                                                      |
| async_tree_none_tg         | 203 ms                                                              | 208 ms: 1.03x slower                                                       |
| bench_mp_pool              | 69.4 ms                                                             | 71.5 ms: 1.03x slower                                                      |
| sympy_str                  | 211 ms                                                              | 218 ms: 1.03x slower                                                       |
| sympy_expand               | 375 ms                                                              | 388 ms: 1.03x slower                                                       |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 488 ms: 1.04x slower                                                       |
| async_tree_io              | 530 ms                                                              | 551 ms: 1.04x slower                                                       |
| typing_runtime_protocols   | 136 us                                                              | 141 us: 1.04x slower                                                       |
| xml_etree_iterparse        | 64.2 ms                                                             | 66.8 ms: 1.04x slower                                                      |
| json                       | 4.10 ms                                                             | 4.27 ms: 1.04x slower                                                      |
| regex_v8                   | 15.7 ms                                                             | 16.4 ms: 1.04x slower                                                      |
| logging_format             | 8.13 us                                                             | 8.55 us: 1.05x slower                                                      |
| sympy_integrate            | 14.6 ms                                                             | 15.5 ms: 1.06x slower                                                      |
| logging_simple             | 7.47 us                                                             | 7.89 us: 1.06x slower                                                      |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 473 ms: 1.06x slower                                                       |
| python_startup             | 22.2 ms                                                             | 23.6 ms: 1.06x slower                                                      |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 3.04 ms: 1.06x slower                                                      |
| genshi_xml                 | 44.3 ms                                                             | 47.0 ms: 1.06x slower                                                      |
| python_startup_no_site     | 18.2 ms                                                             | 19.4 ms: 1.06x slower                                                      |
| 2to3                       | 233 ms                                                              | 248 ms: 1.07x slower                                                       |
| nqueens                    | 68.7 ms                                                             | 73.3 ms: 1.07x slower                                                      |
| pylint                     | 217 ms                                                              | 232 ms: 1.07x slower                                                       |
| mdp                        | 1.60 sec                                                            | 1.72 sec: 1.07x slower                                                     |
| regex_compile              | 99.9 ms                                                             | 107 ms: 1.07x slower                                                       |
| unpickle                   | 9.79 us                                                             | 10.5 us: 1.08x slower                                                      |
| django_template            | 30.1 ms                                                             | 32.4 ms: 1.08x slower                                                      |
| chaos                      | 48.0 ms                                                             | 51.8 ms: 1.08x slower                                                      |
| meteor_contest             | 74.1 ms                                                             | 80.5 ms: 1.09x slower                                                      |
| pprint_pformat             | 1.24 sec                                                            | 1.36 sec: 1.09x slower                                                     |
| pprint_safe_repr           | 607 ms                                                              | 666 ms: 1.10x slower                                                       |
| sqlglot_parse              | 964 us                                                              | 1.06 ms: 1.10x slower                                                      |
| sqlglot_transpile          | 1.19 ms                                                             | 1.31 ms: 1.10x slower                                                      |
| genshi_text                | 20.1 ms                                                             | 22.2 ms: 1.11x slower                                                      |
| async_generators           | 266 ms                                                              | 294 ms: 1.11x slower                                                       |
| spectral_norm              | 68.0 ms                                                             | 75.7 ms: 1.11x slower                                                      |
| sqlglot_optimize           | 39.7 ms                                                             | 44.4 ms: 1.12x slower                                                      |
| tomli_loads                | 1.65 sec                                                            | 1.85 sec: 1.12x slower                                                     |
| json_dumps                 | 6.84 ms                                                             | 7.70 ms: 1.13x slower                                                      |
| pycparser                  | 777 ms                                                              | 882 ms: 1.14x slower                                                       |
| sqlglot_normalize          | 206 ms                                                              | 236 ms: 1.15x slower                                                       |
| scimark_lu                 | 59.4 ms                                                             | 68.5 ms: 1.15x slower                                                      |
| xml_etree_generate         | 59.6 ms                                                             | 69.2 ms: 1.16x slower                                                      |
| mako                       | 6.94 ms                                                             | 8.08 ms: 1.16x slower                                                      |
| float                      | 52.4 ms                                                             | 61.0 ms: 1.16x slower                                                      |
| scimark_fft                | 198 ms                                                              | 231 ms: 1.17x slower                                                       |
| pyflate                    | 308 ms                                                              | 360 ms: 1.17x slower                                                       |
| comprehensions             | 11.9 us                                                             | 13.9 us: 1.17x slower                                                      |
| coroutines                 | 15.5 ms                                                             | 18.3 ms: 1.18x slower                                                      |
| nbody                      | 76.9 ms                                                             | 91.4 ms: 1.19x slower                                                      |
| pickle_pure_python         | 213 us                                                              | 256 us: 1.20x slower                                                       |
| xml_etree_process          | 42.1 ms                                                             | 50.7 ms: 1.20x slower                                                      |
| raytrace                   | 189 ms                                                              | 227 ms: 1.20x slower                                                       |
| scimark_sor                | 81.0 ms                                                             | 97.5 ms: 1.20x slower                                                      |
| deltablue                  | 2.23 ms                                                             | 2.70 ms: 1.21x slower                                                      |
| scimark_monte_carlo        | 45.2 ms                                                             | 54.8 ms: 1.21x slower                                                      |
| hexiom                     | 4.23 ms                                                             | 5.13 ms: 1.21x slower                                                      |
| fannkuch                   | 270 ms                                                              | 328 ms: 1.21x slower                                                       |
| unpickle_pure_python       | 147 us                                                              | 182 us: 1.23x slower                                                       |
| richards_super             | 35.5 ms                                                             | 43.8 ms: 1.23x slower                                                      |
| generators                 | 21.2 ms                                                             | 26.8 ms: 1.27x slower                                                      |
| richards                   | 31.2 ms                                                             | 40.0 ms: 1.28x slower                                                      |
| logging_silent             | 57.9 ns                                                             | 74.4 ns: 1.29x slower                                                      |
| Geometric mean             | (ref)                                                               | 1.03x slower                                                               |

Benchmark hidden because not significant (8): asyncio_tcp, async_tree_none, tornado_http, unpickle_list, async_tree_io_tg, bench_thread_pool, async_tree_memoization, async_tree_memoization_tg
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging
Ignored benchmarks (2) of results/bm-20240911-3.14.0a0-3b5fdc8/bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8.json: dulwich_log, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown