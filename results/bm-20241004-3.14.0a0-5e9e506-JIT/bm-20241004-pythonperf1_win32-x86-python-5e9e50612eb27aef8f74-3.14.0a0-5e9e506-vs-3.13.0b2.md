# Results vs. 3.13.0b2

- fork: python
- ref: 5e9e50612eb27aef8f74
- machine: windows-x86
- commit hash: 5e9e506
- commit date: 2024-10-04
- overall geometric mean: 1.01x faster
- HPT reliability: 97.09%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 261 ms: 1.12x slower                                                           |
| docutils       | 1.81 sec                                                            | 2.04 sec: 1.13x slower                                                         |
| html5lib       | 45.4 ms                                                             | 46.9 ms: 1.03x slower                                                          |
| tornado_http   | 94.3 ms                                                             | 109 ms: 1.16x slower                                                           |
| Geometric mean | (ref)                                                               | 1.11x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg           | 529 ms                                                              | 514 ms: 1.03x faster                                                           |
| async_tree_none            | 228 ms                                                              | 223 ms: 1.02x faster                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 467 ms: 1.04x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.00x faster                                                                   |

Benchmark hidden because not significant (5): async_tree_io, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 50.4 ms: 1.53x faster                                                          |
| float          | 52.4 ms                                                             | 46.2 ms: 1.13x faster                                                          |
| Geometric mean | (ref)                                                               | 1.20x faster                                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 1.88 ms                                                             | 1.81 ms: 1.04x faster                                                          |
| regex_v8       | 15.7 ms                                                             | 15.3 ms: 1.03x faster                                                          |
| regex_dna      | 118 ms                                                              | 116 ms: 1.02x faster                                                           |
| regex_compile  | 99.9 ms                                                             | 105 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                               | 1.01x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 1.65 sec                                                            | 1.51 sec: 1.09x faster                                                         |
| xml_etree_generate   | 59.6 ms                                                             | 54.7 ms: 1.09x faster                                                          |
| pickle_list          | 3.57 us                                                             | 3.47 us: 1.03x faster                                                          |
| xml_etree_process    | 42.1 ms                                                             | 41.5 ms: 1.01x faster                                                          |
| json_dumps           | 6.84 ms                                                             | 6.98 ms: 1.02x slower                                                          |
| json_loads           | 20.5 us                                                             | 21.0 us: 1.02x slower                                                          |
| pickle_dict          | 20.8 us                                                             | 21.3 us: 1.03x slower                                                          |
| pickle               | 8.07 us                                                             | 8.37 us: 1.04x slower                                                          |
| xml_etree_parse      | 104 ms                                                              | 109 ms: 1.05x slower                                                           |
| unpickle             | 9.79 us                                                             | 10.4 us: 1.06x slower                                                          |
| unpickle_pure_python | 147 us                                                              | 158 us: 1.07x slower                                                           |
| pickle_pure_python   | 213 us                                                              | 242 us: 1.14x slower                                                           |
| Geometric mean       | (ref)                                                               | 1.01x slower                                                                   |

Benchmark hidden because not significant (2): unpickle_list, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 18.2 ms                                                             | 20.5 ms: 1.12x slower                                                          |
| python_startup         | 22.2 ms                                                             | 26.8 ms: 1.20x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.16x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 6.94 ms                                                             | 5.57 ms: 1.25x faster                                                          |
| django_template | 30.1 ms                                                             | 32.0 ms: 1.06x slower                                                          |
| genshi_text     | 20.1 ms                                                             | 23.8 ms: 1.18x slower                                                          |
| genshi_xml      | 44.3 ms                                                             | 56.2 ms: 1.27x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.06x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 774 us: 12.57x faster                                                          |
| coverage                   | 307 ms                                                              | 53.5 ms: 5.74x faster                                                          |
| sqlglot_normalize          | 206 ms                                                              | 102 ms: 2.01x faster                                                           |
| nbody                      | 76.9 ms                                                             | 50.4 ms: 1.53x faster                                                          |
| deepcopy_memo              | 23.5 us                                                             | 16.0 us: 1.47x faster                                                          |
| mako                       | 6.94 ms                                                             | 5.57 ms: 1.25x faster                                                          |
| deepcopy                   | 280 us                                                              | 234 us: 1.19x faster                                                           |
| scimark_sor                | 81.0 ms                                                             | 68.5 ms: 1.18x faster                                                          |
| spectral_norm              | 68.0 ms                                                             | 58.4 ms: 1.16x faster                                                          |
| scimark_monte_carlo        | 45.2 ms                                                             | 39.0 ms: 1.16x faster                                                          |
| float                      | 52.4 ms                                                             | 46.2 ms: 1.13x faster                                                          |
| scimark_fft                | 198 ms                                                              | 177 ms: 1.12x faster                                                           |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 2.60 ms: 1.10x faster                                                          |
| fannkuch                   | 270 ms                                                              | 245 ms: 1.10x faster                                                           |
| crypto_pyaes               | 55.8 ms                                                             | 51.2 ms: 1.09x faster                                                          |
| tomli_loads                | 1.65 sec                                                            | 1.51 sec: 1.09x faster                                                         |
| xml_etree_generate         | 59.6 ms                                                             | 54.7 ms: 1.09x faster                                                          |
| pprint_safe_repr           | 607 ms                                                              | 565 ms: 1.07x faster                                                           |
| deepcopy_reduce            | 2.59 us                                                             | 2.43 us: 1.07x faster                                                          |
| pprint_pformat             | 1.24 sec                                                            | 1.18 sec: 1.05x faster                                                         |
| regex_effbot               | 1.88 ms                                                             | 1.81 ms: 1.04x faster                                                          |
| sqlite_synth               | 1.96 us                                                             | 1.89 us: 1.04x faster                                                          |
| go                         | 101 ms                                                              | 97.1 ms: 1.04x faster                                                          |
| regex_v8                   | 15.7 ms                                                             | 15.3 ms: 1.03x faster                                                          |
| async_tree_io_tg           | 529 ms                                                              | 514 ms: 1.03x faster                                                           |
| pickle_list                | 3.57 us                                                             | 3.47 us: 1.03x faster                                                          |
| async_tree_none            | 228 ms                                                              | 223 ms: 1.02x faster                                                           |
| regex_dna                  | 118 ms                                                              | 116 ms: 1.02x faster                                                           |
| xml_etree_process          | 42.1 ms                                                             | 41.5 ms: 1.01x faster                                                          |
| scimark_lu                 | 59.4 ms                                                             | 59.1 ms: 1.00x faster                                                          |
| meteor_contest             | 74.1 ms                                                             | 75.0 ms: 1.01x slower                                                          |
| json_dumps                 | 6.84 ms                                                             | 6.98 ms: 1.02x slower                                                          |
| json_loads                 | 20.5 us                                                             | 21.0 us: 1.02x slower                                                          |
| pickle_dict                | 20.8 us                                                             | 21.3 us: 1.03x slower                                                          |
| typing_runtime_protocols   | 136 us                                                              | 139 us: 1.03x slower                                                           |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.3 sec: 1.03x slower                                                         |
| json                       | 4.10 ms                                                             | 4.22 ms: 1.03x slower                                                          |
| html5lib                   | 45.4 ms                                                             | 46.9 ms: 1.03x slower                                                          |
| comprehensions             | 11.9 us                                                             | 12.3 us: 1.04x slower                                                          |
| pickle                     | 8.07 us                                                             | 8.37 us: 1.04x slower                                                          |
| bench_thread_pool          | 985 us                                                              | 1.02 ms: 1.04x slower                                                          |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 467 ms: 1.04x slower                                                           |
| logging_format             | 8.13 us                                                             | 8.52 us: 1.05x slower                                                          |
| regex_compile              | 99.9 ms                                                             | 105 ms: 1.05x slower                                                           |
| xml_etree_parse            | 104 ms                                                              | 109 ms: 1.05x slower                                                           |
| pathlib                    | 83.9 ms                                                             | 87.8 ms: 1.05x slower                                                          |
| sympy_expand               | 375 ms                                                              | 394 ms: 1.05x slower                                                           |
| pyflate                    | 308 ms                                                              | 325 ms: 1.05x slower                                                           |
| pycparser                  | 777 ms                                                              | 822 ms: 1.06x slower                                                           |
| unpickle                   | 9.79 us                                                             | 10.4 us: 1.06x slower                                                          |
| mdp                        | 1.60 sec                                                            | 1.70 sec: 1.06x slower                                                         |
| django_template            | 30.1 ms                                                             | 32.0 ms: 1.06x slower                                                          |
| telco                      | 6.03 ms                                                             | 6.42 ms: 1.07x slower                                                          |
| logging_simple             | 7.47 us                                                             | 8.02 us: 1.07x slower                                                          |
| unpickle_pure_python       | 147 us                                                              | 158 us: 1.07x slower                                                           |
| sympy_str                  | 211 ms                                                              | 227 ms: 1.07x slower                                                           |
| nqueens                    | 68.7 ms                                                             | 73.9 ms: 1.08x slower                                                          |
| chaos                      | 48.0 ms                                                             | 52.4 ms: 1.09x slower                                                          |
| sqlglot_parse              | 964 us                                                              | 1.07 ms: 1.11x slower                                                          |
| sympy_sum                  | 105 ms                                                              | 117 ms: 1.12x slower                                                           |
| 2to3                       | 233 ms                                                              | 261 ms: 1.12x slower                                                           |
| python_startup_no_site     | 18.2 ms                                                             | 20.5 ms: 1.12x slower                                                          |
| docutils                   | 1.81 sec                                                            | 2.04 sec: 1.13x slower                                                         |
| coroutines                 | 15.5 ms                                                             | 17.5 ms: 1.13x slower                                                          |
| pickle_pure_python         | 213 us                                                              | 242 us: 1.14x slower                                                           |
| sqlglot_transpile          | 1.19 ms                                                             | 1.37 ms: 1.15x slower                                                          |
| tornado_http               | 94.3 ms                                                             | 109 ms: 1.16x slower                                                           |
| asyncio_tcp                | 662 ms                                                              | 771 ms: 1.16x slower                                                           |
| sympy_integrate            | 14.6 ms                                                             | 17.1 ms: 1.17x slower                                                          |
| deltablue                  | 2.23 ms                                                             | 2.63 ms: 1.18x slower                                                          |
| genshi_text                | 20.1 ms                                                             | 23.8 ms: 1.18x slower                                                          |
| python_startup             | 22.2 ms                                                             | 26.8 ms: 1.20x slower                                                          |
| async_generators           | 266 ms                                                              | 326 ms: 1.23x slower                                                           |
| gc_traversal               | 1.43 ms                                                             | 1.78 ms: 1.24x slower                                                          |
| sqlglot_optimize           | 39.7 ms                                                             | 49.7 ms: 1.25x slower                                                          |
| genshi_xml                 | 44.3 ms                                                             | 56.2 ms: 1.27x slower                                                          |
| richards_super             | 35.5 ms                                                             | 45.2 ms: 1.27x slower                                                          |
| richards                   | 31.2 ms                                                             | 39.9 ms: 1.28x slower                                                          |
| generators                 | 21.2 ms                                                             | 27.1 ms: 1.28x slower                                                          |
| hexiom                     | 4.23 ms                                                             | 5.48 ms: 1.29x slower                                                          |
| pylint                     | 217 ms                                                              | 282 ms: 1.30x slower                                                           |
| raytrace                   | 189 ms                                                              | 255 ms: 1.35x slower                                                           |
| bench_mp_pool              | 69.4 ms                                                             | 94.3 ms: 1.36x slower                                                          |
| create_gc_cycles           | 756 us                                                              | 1.16 ms: 1.54x slower                                                          |
| Geometric mean             | (ref)                                                               | 1.01x faster                                                                   |

Benchmark hidden because not significant (9): async_tree_io, async_tree_none_tg, async_tree_cpu_io_mixed, unpickle_list, pidigits, async_tree_memoization_tg, xml_etree_iterparse, logging_silent, async_tree_memoization
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging
Ignored benchmarks (3) of results/bm-20241004-3.14.0a0-5e9e506-JIT/bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506.json: dulwich_log, sphinx, unpack_sequence

# HPT report

- Reliability score: 97.09% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown