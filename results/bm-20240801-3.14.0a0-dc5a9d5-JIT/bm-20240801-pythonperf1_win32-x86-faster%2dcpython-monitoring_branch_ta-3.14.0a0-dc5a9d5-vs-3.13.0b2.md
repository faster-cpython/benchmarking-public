# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: monitoring_branch_ta
- machine: windows-x86
- commit hash: dc5a9d5
- commit date: 2024-08-01
- overall geometric mean: 1.03x faster
- HPT reliability: 97.35%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-pythonperf1_win32-x86-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 259 ms: 1.11x slower                                                                     |
| docutils       | 1.81 sec                                                            | 1.94 sec: 1.07x slower                                                                   |
| html5lib       | 45.4 ms                                                             | 46.9 ms: 1.03x slower                                                                    |
| tornado_http   | 94.3 ms                                                             | 106 ms: 1.13x slower                                                                     |
| Geometric mean | (ref)                                                               | 1.08x slower                                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-pythonperf1_win32-x86-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 529 ms                                                              | 513 ms: 1.03x faster                                                                     |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 459 ms: 1.03x slower                                                                     |
| async_tree_io              | 530 ms                                                              | 551 ms: 1.04x slower                                                                     |
| Geometric mean             | (ref)                                                               | 1.00x slower                                                                             |

Benchmark hidden because not significant (5): async_tree_none_tg, async_tree_none, async_tree_memoization_tg, async_tree_memoization, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-pythonperf1_win32-x86-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 52.7 ms: 1.46x faster                                                                    |
| float          | 52.4 ms                                                             | 43.1 ms: 1.21x faster                                                                    |
| pidigits       | 199 ms                                                              | 199 ms: 1.00x slower                                                                     |
| Geometric mean | (ref)                                                               | 1.21x faster                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-pythonperf1_win32-x86-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| regex_compile  | 99.9 ms                                                             | 94.0 ms: 1.06x faster                                                                    |
| regex_v8       | 15.7 ms                                                             | 15.8 ms: 1.00x slower                                                                    |
| regex_dna      | 118 ms                                                              | 119 ms: 1.01x slower                                                                     |
| regex_effbot   | 1.88 ms                                                             | 1.90 ms: 1.01x slower                                                                    |
| Geometric mean | (ref)                                                               | 1.01x faster                                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-pythonperf1_win32-x86-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| tomli_loads          | 1.65 sec                                                            | 1.50 sec: 1.10x faster                                                                   |
| xml_etree_iterparse  | 64.2 ms                                                             | 62.8 ms: 1.02x faster                                                                    |
| xml_etree_generate   | 59.6 ms                                                             | 58.9 ms: 1.01x faster                                                                    |
| xml_etree_parse      | 104 ms                                                              | 104 ms: 1.01x faster                                                                     |
| unpickle_pure_python | 147 us                                                              | 151 us: 1.02x slower                                                                     |
| json_loads           | 20.5 us                                                             | 21.7 us: 1.06x slower                                                                    |
| json_dumps           | 6.84 ms                                                             | 7.23 ms: 1.06x slower                                                                    |
| xml_etree_process    | 42.1 ms                                                             | 44.6 ms: 1.06x slower                                                                    |
| Geometric mean       | (ref)                                                               | 1.01x slower                                                                             |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-pythonperf1_win32-x86-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 24.1 ms: 1.08x slower                                                                    |
| python_startup_no_site | 18.2 ms                                                             | 20.0 ms: 1.10x slower                                                                    |
| Geometric mean         | (ref)                                                               | 1.09x slower                                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-pythonperf1_win32-x86-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|-----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| mako            | 6.94 ms                                                             | 5.44 ms: 1.28x faster                                                                    |
| django_template | 30.1 ms                                                             | 32.4 ms: 1.08x slower                                                                    |
| genshi_xml      | 44.3 ms                                                             | 47.9 ms: 1.08x slower                                                                    |
| genshi_text     | 20.1 ms                                                             | 22.8 ms: 1.13x slower                                                                    |
| Geometric mean  | (ref)                                                               | 1.01x slower                                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-pythonperf1_win32-x86-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 759 us: 12.83x faster                                                                    |
| coverage                   | 307 ms                                                              | 52.0 ms: 5.90x faster                                                                    |
| deepcopy_memo              | 23.5 us                                                             | 16.0 us: 1.46x faster                                                                    |
| nbody                      | 76.9 ms                                                             | 52.7 ms: 1.46x faster                                                                    |
| spectral_norm              | 68.0 ms                                                             | 49.1 ms: 1.38x faster                                                                    |
| mako                       | 6.94 ms                                                             | 5.44 ms: 1.28x faster                                                                    |
| float                      | 52.4 ms                                                             | 43.1 ms: 1.21x faster                                                                    |
| fannkuch                   | 270 ms                                                              | 225 ms: 1.20x faster                                                                     |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 2.42 ms: 1.19x faster                                                                    |
| scimark_fft                | 198 ms                                                              | 169 ms: 1.17x faster                                                                     |
| crypto_pyaes               | 55.8 ms                                                             | 47.9 ms: 1.17x faster                                                                    |
| deepcopy                   | 280 us                                                              | 243 us: 1.15x faster                                                                     |
| pyflate                    | 308 ms                                                              | 271 ms: 1.14x faster                                                                     |
| tomli_loads                | 1.65 sec                                                            | 1.50 sec: 1.10x faster                                                                   |
| deepcopy_reduce            | 2.59 us                                                             | 2.39 us: 1.08x faster                                                                    |
| scimark_monte_carlo        | 45.2 ms                                                             | 42.4 ms: 1.07x faster                                                                    |
| regex_compile              | 99.9 ms                                                             | 94.0 ms: 1.06x faster                                                                    |
| meteor_contest             | 74.1 ms                                                             | 71.0 ms: 1.04x faster                                                                    |
| comprehensions             | 11.9 us                                                             | 11.4 us: 1.04x faster                                                                    |
| pprint_safe_repr           | 607 ms                                                              | 587 ms: 1.03x faster                                                                     |
| async_tree_io_tg           | 529 ms                                                              | 513 ms: 1.03x faster                                                                     |
| pprint_pformat             | 1.24 sec                                                            | 1.20 sec: 1.03x faster                                                                   |
| xml_etree_iterparse        | 64.2 ms                                                             | 62.8 ms: 1.02x faster                                                                    |
| xml_etree_generate         | 59.6 ms                                                             | 58.9 ms: 1.01x faster                                                                    |
| telco                      | 6.03 ms                                                             | 5.97 ms: 1.01x faster                                                                    |
| xml_etree_parse            | 104 ms                                                              | 104 ms: 1.01x faster                                                                     |
| pidigits                   | 199 ms                                                              | 199 ms: 1.00x slower                                                                     |
| regex_v8                   | 15.7 ms                                                             | 15.8 ms: 1.00x slower                                                                    |
| regex_dna                  | 118 ms                                                              | 119 ms: 1.01x slower                                                                     |
| regex_effbot               | 1.88 ms                                                             | 1.90 ms: 1.01x slower                                                                    |
| gc_traversal               | 1.43 ms                                                             | 1.44 ms: 1.01x slower                                                                    |
| logging_silent             | 57.9 ns                                                             | 58.7 ns: 1.01x slower                                                                    |
| create_gc_cycles           | 756 us                                                              | 767 us: 1.01x slower                                                                     |
| sqlglot_parse              | 964 us                                                              | 978 us: 1.01x slower                                                                     |
| unpickle_pure_python       | 147 us                                                              | 151 us: 1.02x slower                                                                     |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 459 ms: 1.03x slower                                                                     |
| pycparser                  | 777 ms                                                              | 798 ms: 1.03x slower                                                                     |
| sympy_expand               | 375 ms                                                              | 386 ms: 1.03x slower                                                                     |
| logging_format             | 8.13 us                                                             | 8.38 us: 1.03x slower                                                                    |
| sympy_str                  | 211 ms                                                              | 218 ms: 1.03x slower                                                                     |
| html5lib                   | 45.4 ms                                                             | 46.9 ms: 1.03x slower                                                                    |
| logging_simple             | 7.47 us                                                             | 7.72 us: 1.03x slower                                                                    |
| async_tree_io              | 530 ms                                                              | 551 ms: 1.04x slower                                                                     |
| sympy_sum                  | 105 ms                                                              | 110 ms: 1.05x slower                                                                     |
| sqlglot_transpile          | 1.19 ms                                                             | 1.25 ms: 1.05x slower                                                                    |
| json                       | 4.10 ms                                                             | 4.31 ms: 1.05x slower                                                                    |
| json_loads                 | 20.5 us                                                             | 21.7 us: 1.06x slower                                                                    |
| json_dumps                 | 6.84 ms                                                             | 7.23 ms: 1.06x slower                                                                    |
| xml_etree_process          | 42.1 ms                                                             | 44.6 ms: 1.06x slower                                                                    |
| pathlib                    | 83.9 ms                                                             | 89.0 ms: 1.06x slower                                                                    |
| docutils                   | 1.81 sec                                                            | 1.94 sec: 1.07x slower                                                                   |
| mdp                        | 1.60 sec                                                            | 1.72 sec: 1.07x slower                                                                   |
| chaos                      | 48.0 ms                                                             | 51.6 ms: 1.08x slower                                                                    |
| django_template            | 30.1 ms                                                             | 32.4 ms: 1.08x slower                                                                    |
| genshi_xml                 | 44.3 ms                                                             | 47.9 ms: 1.08x slower                                                                    |
| python_startup             | 22.2 ms                                                             | 24.1 ms: 1.08x slower                                                                    |
| typing_runtime_protocols   | 136 us                                                              | 148 us: 1.10x slower                                                                     |
| python_startup_no_site     | 18.2 ms                                                             | 20.0 ms: 1.10x slower                                                                    |
| sqlglot_optimize           | 39.7 ms                                                             | 43.7 ms: 1.10x slower                                                                    |
| sqlglot_normalize          | 206 ms                                                              | 227 ms: 1.10x slower                                                                     |
| richards                   | 31.2 ms                                                             | 34.4 ms: 1.10x slower                                                                    |
| 2to3                       | 233 ms                                                              | 259 ms: 1.11x slower                                                                     |
| sympy_integrate            | 14.6 ms                                                             | 16.3 ms: 1.12x slower                                                                    |
| richards_super             | 35.5 ms                                                             | 39.7 ms: 1.12x slower                                                                    |
| bench_mp_pool              | 69.4 ms                                                             | 77.8 ms: 1.12x slower                                                                    |
| tornado_http               | 94.3 ms                                                             | 106 ms: 1.13x slower                                                                     |
| go                         | 101 ms                                                              | 113 ms: 1.13x slower                                                                     |
| genshi_text                | 20.1 ms                                                             | 22.8 ms: 1.13x slower                                                                    |
| hexiom                     | 4.23 ms                                                             | 4.86 ms: 1.15x slower                                                                    |
| pylint                     | 217 ms                                                              | 253 ms: 1.17x slower                                                                     |
| nqueens                    | 68.7 ms                                                             | 80.2 ms: 1.17x slower                                                                    |
| coroutines                 | 15.5 ms                                                             | 18.3 ms: 1.18x slower                                                                    |
| generators                 | 21.2 ms                                                             | 25.2 ms: 1.19x slower                                                                    |
| scimark_sor                | 81.0 ms                                                             | 101 ms: 1.24x slower                                                                     |
| raytrace                   | 189 ms                                                              | 235 ms: 1.25x slower                                                                     |
| async_generators           | 266 ms                                                              | 332 ms: 1.25x slower                                                                     |
| deltablue                  | 2.23 ms                                                             | 2.82 ms: 1.26x slower                                                                    |
| scimark_lu                 | 59.4 ms                                                             | 76.9 ms: 1.30x slower                                                                    |
| Geometric mean             | (ref)                                                               | 1.03x faster                                                                             |

Benchmark hidden because not significant (9): async_tree_none_tg, async_tree_none, async_tree_memoization_tg, async_tree_memoization, pickle_pure_python, async_tree_cpu_io_mixed, asyncio_tcp_ssl, bench_thread_pool, asyncio_tcp
Ignored benchmarks (8) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240801-3.14.0a0-dc5a9d5-JIT/bm-20240801-pythonperf1_win32-x86-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5.json: dulwich_log

# HPT report

- Reliability score: 97.35% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown