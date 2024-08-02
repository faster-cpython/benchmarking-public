# Results vs. 3.13.0b2

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: windows-x86
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.03x faster
- HPT reliability: 97.10%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 261 ms: 1.12x slower                                                           |
| docutils       | 1.81 sec                                                            | 1.98 sec: 1.09x slower                                                         |
| html5lib       | 45.4 ms                                                             | 47.7 ms: 1.05x slower                                                          |
| tornado_http   | 94.3 ms                                                             | 107 ms: 1.13x slower                                                           |
| Geometric mean | (ref)                                                               | 1.10x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg           | 529 ms                                                              | 506 ms: 1.05x faster                                                           |
| async_tree_none_tg         | 203 ms                                                              | 197 ms: 1.03x faster                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 479 ms: 1.02x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 458 ms: 1.02x slower                                                           |
| async_tree_io              | 530 ms                                                              | 546 ms: 1.03x slower                                                           |
| async_tree_memoization     | 275 ms                                                              | 288 ms: 1.05x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.01x slower                                                                   |

Benchmark hidden because not significant (2): async_tree_memoization_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 52.6 ms: 1.46x faster                                                          |
| float          | 52.4 ms                                                             | 42.5 ms: 1.23x faster                                                          |
| pidigits       | 199 ms                                                              | 196 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                               | 1.22x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 99.9 ms                                                             | 96.1 ms: 1.04x faster                                                          |
| regex_dna      | 118 ms                                                              | 120 ms: 1.02x slower                                                           |
| regex_v8       | 15.7 ms                                                             | 16.1 ms: 1.03x slower                                                          |
| regex_effbot   | 1.88 ms                                                             | 2.00 ms: 1.06x slower                                                          |
| Geometric mean | (ref)                                                               | 1.02x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|---------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads         | 1.65 sec                                                            | 1.54 sec: 1.07x faster                                                         |
| xml_etree_iterparse | 64.2 ms                                                             | 63.9 ms: 1.01x faster                                                          |
| xml_etree_parse     | 104 ms                                                              | 107 ms: 1.02x slower                                                           |
| json_loads          | 20.5 us                                                             | 21.1 us: 1.03x slower                                                          |
| json_dumps          | 6.84 ms                                                             | 7.05 ms: 1.03x slower                                                          |
| xml_etree_process   | 42.1 ms                                                             | 44.9 ms: 1.07x slower                                                          |
| Geometric mean      | (ref)                                                               | 1.01x slower                                                                   |

Benchmark hidden because not significant (3): unpickle_pure_python, pickle_pure_python, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 24.8 ms: 1.12x slower                                                          |
| python_startup_no_site | 18.2 ms                                                             | 20.8 ms: 1.14x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.13x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 6.94 ms                                                             | 5.43 ms: 1.28x faster                                                          |
| django_template | 30.1 ms                                                             | 32.8 ms: 1.09x slower                                                          |
| genshi_xml      | 44.3 ms                                                             | 53.5 ms: 1.21x slower                                                          |
| genshi_text     | 20.1 ms                                                             | 24.5 ms: 1.22x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.06x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 774 us: 12.57x faster                                                          |
| coverage                   | 307 ms                                                              | 51.8 ms: 5.93x faster                                                          |
| nbody                      | 76.9 ms                                                             | 52.6 ms: 1.46x faster                                                          |
| deepcopy_memo              | 23.5 us                                                             | 16.4 us: 1.43x faster                                                          |
| spectral_norm              | 68.0 ms                                                             | 47.9 ms: 1.42x faster                                                          |
| mako                       | 6.94 ms                                                             | 5.43 ms: 1.28x faster                                                          |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 2.32 ms: 1.24x faster                                                          |
| float                      | 52.4 ms                                                             | 42.5 ms: 1.23x faster                                                          |
| scimark_sor                | 81.0 ms                                                             | 67.0 ms: 1.21x faster                                                          |
| fannkuch                   | 270 ms                                                              | 227 ms: 1.19x faster                                                           |
| crypto_pyaes               | 55.8 ms                                                             | 46.9 ms: 1.19x faster                                                          |
| scimark_fft                | 198 ms                                                              | 168 ms: 1.18x faster                                                           |
| pyflate                    | 308 ms                                                              | 269 ms: 1.15x faster                                                           |
| deepcopy                   | 280 us                                                              | 254 us: 1.10x faster                                                           |
| scimark_monte_carlo        | 45.2 ms                                                             | 41.8 ms: 1.08x faster                                                          |
| meteor_contest             | 74.1 ms                                                             | 69.0 ms: 1.07x faster                                                          |
| tomli_loads                | 1.65 sec                                                            | 1.54 sec: 1.07x faster                                                         |
| async_tree_io_tg           | 529 ms                                                              | 506 ms: 1.05x faster                                                           |
| regex_compile              | 99.9 ms                                                             | 96.1 ms: 1.04x faster                                                          |
| pprint_pformat             | 1.24 sec                                                            | 1.20 sec: 1.04x faster                                                         |
| pprint_safe_repr           | 607 ms                                                              | 586 ms: 1.03x faster                                                           |
| comprehensions             | 11.9 us                                                             | 11.5 us: 1.03x faster                                                          |
| async_tree_none_tg         | 203 ms                                                              | 197 ms: 1.03x faster                                                           |
| deepcopy_reduce            | 2.59 us                                                             | 2.54 us: 1.02x faster                                                          |
| pidigits                   | 199 ms                                                              | 196 ms: 1.01x faster                                                           |
| xml_etree_iterparse        | 64.2 ms                                                             | 63.9 ms: 1.01x faster                                                          |
| logging_silent             | 57.9 ns                                                             | 58.2 ns: 1.01x slower                                                          |
| scimark_lu                 | 59.4 ms                                                             | 59.7 ms: 1.01x slower                                                          |
| sqlglot_parse              | 964 us                                                              | 973 us: 1.01x slower                                                           |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.1 sec: 1.01x slower                                                         |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 479 ms: 1.02x slower                                                           |
| regex_dna                  | 118 ms                                                              | 120 ms: 1.02x slower                                                           |
| gc_traversal               | 1.43 ms                                                             | 1.46 ms: 1.02x slower                                                          |
| logging_simple             | 7.47 us                                                             | 7.62 us: 1.02x slower                                                          |
| create_gc_cycles           | 756 us                                                              | 771 us: 1.02x slower                                                           |
| pycparser                  | 777 ms                                                              | 793 ms: 1.02x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 458 ms: 1.02x slower                                                           |
| xml_etree_parse            | 104 ms                                                              | 107 ms: 1.02x slower                                                           |
| regex_v8                   | 15.7 ms                                                             | 16.1 ms: 1.03x slower                                                          |
| logging_format             | 8.13 us                                                             | 8.36 us: 1.03x slower                                                          |
| async_tree_io              | 530 ms                                                              | 546 ms: 1.03x slower                                                           |
| json_loads                 | 20.5 us                                                             | 21.1 us: 1.03x slower                                                          |
| json_dumps                 | 6.84 ms                                                             | 7.05 ms: 1.03x slower                                                          |
| bench_thread_pool          | 985 us                                                              | 1.02 ms: 1.03x slower                                                          |
| async_tree_memoization     | 275 ms                                                              | 288 ms: 1.05x slower                                                           |
| html5lib                   | 45.4 ms                                                             | 47.7 ms: 1.05x slower                                                          |
| sympy_str                  | 211 ms                                                              | 222 ms: 1.05x slower                                                           |
| sqlglot_transpile          | 1.19 ms                                                             | 1.25 ms: 1.05x slower                                                          |
| sympy_expand               | 375 ms                                                              | 394 ms: 1.05x slower                                                           |
| mdp                        | 1.60 sec                                                            | 1.69 sec: 1.06x slower                                                         |
| pathlib                    | 83.9 ms                                                             | 88.7 ms: 1.06x slower                                                          |
| regex_effbot               | 1.88 ms                                                             | 2.00 ms: 1.06x slower                                                          |
| xml_etree_process          | 42.1 ms                                                             | 44.9 ms: 1.07x slower                                                          |
| sympy_sum                  | 105 ms                                                              | 112 ms: 1.07x slower                                                           |
| chaos                      | 48.0 ms                                                             | 51.6 ms: 1.08x slower                                                          |
| json                       | 4.10 ms                                                             | 4.43 ms: 1.08x slower                                                          |
| django_template            | 30.1 ms                                                             | 32.8 ms: 1.09x slower                                                          |
| docutils                   | 1.81 sec                                                            | 1.98 sec: 1.09x slower                                                         |
| bench_mp_pool              | 69.4 ms                                                             | 77.3 ms: 1.11x slower                                                          |
| python_startup             | 22.2 ms                                                             | 24.8 ms: 1.12x slower                                                          |
| 2to3                       | 233 ms                                                              | 261 ms: 1.12x slower                                                           |
| richards                   | 31.2 ms                                                             | 35.1 ms: 1.12x slower                                                          |
| nqueens                    | 68.7 ms                                                             | 77.2 ms: 1.12x slower                                                          |
| sqlglot_normalize          | 206 ms                                                              | 232 ms: 1.13x slower                                                           |
| sqlglot_optimize           | 39.7 ms                                                             | 44.9 ms: 1.13x slower                                                          |
| sympy_integrate            | 14.6 ms                                                             | 16.6 ms: 1.13x slower                                                          |
| tornado_http               | 94.3 ms                                                             | 107 ms: 1.13x slower                                                           |
| typing_runtime_protocols   | 136 us                                                              | 153 us: 1.13x slower                                                           |
| python_startup_no_site     | 18.2 ms                                                             | 20.8 ms: 1.14x slower                                                          |
| hexiom                     | 4.23 ms                                                             | 4.84 ms: 1.14x slower                                                          |
| go                         | 101 ms                                                              | 115 ms: 1.15x slower                                                           |
| coroutines                 | 15.5 ms                                                             | 17.8 ms: 1.15x slower                                                          |
| generators                 | 21.2 ms                                                             | 24.7 ms: 1.17x slower                                                          |
| richards_super             | 35.5 ms                                                             | 41.7 ms: 1.18x slower                                                          |
| asyncio_tcp                | 662 ms                                                              | 782 ms: 1.18x slower                                                           |
| pylint                     | 217 ms                                                              | 257 ms: 1.18x slower                                                           |
| raytrace                   | 189 ms                                                              | 227 ms: 1.20x slower                                                           |
| async_generators           | 266 ms                                                              | 320 ms: 1.20x slower                                                           |
| genshi_xml                 | 44.3 ms                                                             | 53.5 ms: 1.21x slower                                                          |
| genshi_text                | 20.1 ms                                                             | 24.5 ms: 1.22x slower                                                          |
| deltablue                  | 2.23 ms                                                             | 2.75 ms: 1.23x slower                                                          |
| Geometric mean             | (ref)                                                               | 1.03x faster                                                                   |

Benchmark hidden because not significant (6): telco, async_tree_memoization_tg, unpickle_pure_python, pickle_pure_python, xml_etree_generate, async_tree_none
Ignored benchmarks (8) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240802-3.14.0a0-7aca84e-JIT/bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json: dulwich_log

# HPT report

- Reliability score: 97.10% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown