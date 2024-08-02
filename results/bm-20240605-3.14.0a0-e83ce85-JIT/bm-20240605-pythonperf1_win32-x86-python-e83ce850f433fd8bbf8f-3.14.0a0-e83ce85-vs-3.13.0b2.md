# Results vs. 3.13.0b2

- fork: python
- ref: e83ce850f433fd8bbf8f
- machine: windows-x86
- commit hash: e83ce85
- commit date: 2024-06-05
- overall geometric mean: 1.06x faster
- HPT reliability: 66.96%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-pythonperf1_win32-x86-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 242 ms: 1.04x slower                                                           |
| docutils       | 1.81 sec                                                            | 1.85 sec: 1.02x slower                                                         |
| html5lib       | 45.4 ms                                                             | 46.0 ms: 1.01x slower                                                          |
| tornado_http   | 94.3 ms                                                             | 96.4 ms: 1.02x slower                                                          |
| Geometric mean | (ref)                                                               | 1.02x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-pythonperf1_win32-x86-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg           | 529 ms                                                              | 537 ms: 1.01x slower                                                           |
| async_tree_memoization     | 275 ms                                                              | 280 ms: 1.02x slower                                                           |
| async_tree_memoization_tg  | 254 ms                                                              | 261 ms: 1.03x slower                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 504 ms: 1.07x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 484 ms: 1.08x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.03x slower                                                                   |

Benchmark hidden because not significant (3): async_tree_io, async_tree_none, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-pythonperf1_win32-x86-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 52.9 ms: 1.45x faster                                                          |
| float          | 52.4 ms                                                             | 41.4 ms: 1.26x faster                                                          |
| pidigits       | 199 ms                                                              | 198 ms: 1.00x faster                                                           |
| Geometric mean | (ref)                                                               | 1.23x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-pythonperf1_win32-x86-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 99.9 ms                                                             | 96.7 ms: 1.03x faster                                                          |
| regex_v8       | 15.7 ms                                                             | 15.9 ms: 1.01x slower                                                          |
| regex_dna      | 118 ms                                                              | 123 ms: 1.04x slower                                                           |
| regex_effbot   | 1.88 ms                                                             | 1.98 ms: 1.05x slower                                                          |
| Geometric mean | (ref)                                                               | 1.02x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-pythonperf1_win32-x86-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 1.65 sec                                                            | 1.43 sec: 1.16x faster                                                         |
| unpickle_pure_python | 147 us                                                              | 135 us: 1.09x faster                                                           |
| xml_etree_generate   | 59.6 ms                                                             | 55.2 ms: 1.08x faster                                                          |
| pickle_pure_python   | 213 us                                                              | 199 us: 1.07x faster                                                           |
| json_dumps           | 6.84 ms                                                             | 6.51 ms: 1.05x faster                                                          |
| xml_etree_iterparse  | 64.2 ms                                                             | 61.2 ms: 1.05x faster                                                          |
| xml_etree_process    | 42.1 ms                                                             | 40.4 ms: 1.04x faster                                                          |
| xml_etree_parse      | 104 ms                                                              | 102 ms: 1.02x faster                                                           |
| unpickle_list        | 2.93 us                                                             | 2.90 us: 1.01x faster                                                          |
| json_loads           | 20.5 us                                                             | 20.7 us: 1.01x slower                                                          |
| pickle               | 8.07 us                                                             | 8.23 us: 1.02x slower                                                          |
| pickle_list          | 3.57 us                                                             | 3.72 us: 1.04x slower                                                          |
| unpickle             | 9.79 us                                                             | 10.5 us: 1.07x slower                                                          |
| Geometric mean       | (ref)                                                               | 1.03x faster                                                                   |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-pythonperf1_win32-x86-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 24.2 ms: 1.09x slower                                                          |
| python_startup_no_site | 18.2 ms                                                             | 20.2 ms: 1.11x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.10x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-pythonperf1_win32-x86-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 6.94 ms                                                             | 5.34 ms: 1.30x faster                                                          |
| genshi_text     | 20.1 ms                                                             | 21.0 ms: 1.04x slower                                                          |
| django_template | 30.1 ms                                                             | 31.7 ms: 1.05x slower                                                          |
| genshi_xml      | 44.3 ms                                                             | 51.6 ms: 1.17x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.00x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-pythonperf1_win32-x86-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 699 us: 13.92x faster                                                          |
| coverage                   | 307 ms                                                              | 50.6 ms: 6.07x faster                                                          |
| nbody                      | 76.9 ms                                                             | 52.9 ms: 1.45x faster                                                          |
| spectral_norm              | 68.0 ms                                                             | 47.6 ms: 1.43x faster                                                          |
| mako                       | 6.94 ms                                                             | 5.34 ms: 1.30x faster                                                          |
| float                      | 52.4 ms                                                             | 41.4 ms: 1.26x faster                                                          |
| fannkuch                   | 270 ms                                                              | 219 ms: 1.23x faster                                                           |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 2.34 ms: 1.23x faster                                                          |
| scimark_fft                | 198 ms                                                              | 164 ms: 1.20x faster                                                           |
| crypto_pyaes               | 55.8 ms                                                             | 47.9 ms: 1.17x faster                                                          |
| tomli_loads                | 1.65 sec                                                            | 1.43 sec: 1.16x faster                                                         |
| pyflate                    | 308 ms                                                              | 271 ms: 1.14x faster                                                           |
| deepcopy_memo              | 23.5 us                                                             | 20.7 us: 1.14x faster                                                          |
| scimark_monte_carlo        | 45.2 ms                                                             | 39.8 ms: 1.14x faster                                                          |
| pprint_safe_repr           | 607 ms                                                              | 546 ms: 1.11x faster                                                           |
| asyncio_tcp                | 662 ms                                                              | 600 ms: 1.10x faster                                                           |
| pprint_pformat             | 1.24 sec                                                            | 1.13 sec: 1.09x faster                                                         |
| unpickle_pure_python       | 147 us                                                              | 135 us: 1.09x faster                                                           |
| xml_etree_generate         | 59.6 ms                                                             | 55.2 ms: 1.08x faster                                                          |
| comprehensions             | 11.9 us                                                             | 11.0 us: 1.08x faster                                                          |
| logging_silent             | 57.9 ns                                                             | 53.9 ns: 1.07x faster                                                          |
| pickle_pure_python         | 213 us                                                              | 199 us: 1.07x faster                                                           |
| sqlglot_parse              | 964 us                                                              | 900 us: 1.07x faster                                                           |
| telco                      | 6.03 ms                                                             | 5.64 ms: 1.07x faster                                                          |
| json_dumps                 | 6.84 ms                                                             | 6.51 ms: 1.05x faster                                                          |
| xml_etree_iterparse        | 64.2 ms                                                             | 61.2 ms: 1.05x faster                                                          |
| xml_etree_process          | 42.1 ms                                                             | 40.4 ms: 1.04x faster                                                          |
| sqlite_synth               | 1.96 us                                                             | 1.90 us: 1.03x faster                                                          |
| regex_compile              | 99.9 ms                                                             | 96.7 ms: 1.03x faster                                                          |
| sqlglot_transpile          | 1.19 ms                                                             | 1.16 ms: 1.03x faster                                                          |
| logging_simple             | 7.47 us                                                             | 7.27 us: 1.03x faster                                                          |
| logging_format             | 8.13 us                                                             | 7.92 us: 1.03x faster                                                          |
| meteor_contest             | 74.1 ms                                                             | 72.3 ms: 1.02x faster                                                          |
| xml_etree_parse            | 104 ms                                                              | 102 ms: 1.02x faster                                                           |
| pathlib                    | 83.9 ms                                                             | 82.4 ms: 1.02x faster                                                          |
| sympy_str                  | 211 ms                                                              | 208 ms: 1.01x faster                                                           |
| sympy_expand               | 375 ms                                                              | 370 ms: 1.01x faster                                                           |
| richards_super             | 35.5 ms                                                             | 35.1 ms: 1.01x faster                                                          |
| unpickle_list              | 2.93 us                                                             | 2.90 us: 1.01x faster                                                          |
| pidigits                   | 199 ms                                                              | 198 ms: 1.00x faster                                                           |
| regex_v8                   | 15.7 ms                                                             | 15.9 ms: 1.01x slower                                                          |
| json_loads                 | 20.5 us                                                             | 20.7 us: 1.01x slower                                                          |
| sympy_sum                  | 105 ms                                                              | 106 ms: 1.01x slower                                                           |
| html5lib                   | 45.4 ms                                                             | 46.0 ms: 1.01x slower                                                          |
| async_tree_io_tg           | 529 ms                                                              | 537 ms: 1.01x slower                                                           |
| mdp                        | 1.60 sec                                                            | 1.63 sec: 1.01x slower                                                         |
| coroutines                 | 15.5 ms                                                             | 15.7 ms: 1.02x slower                                                          |
| async_tree_memoization     | 275 ms                                                              | 280 ms: 1.02x slower                                                           |
| pickle                     | 8.07 us                                                             | 8.23 us: 1.02x slower                                                          |
| docutils                   | 1.81 sec                                                            | 1.85 sec: 1.02x slower                                                         |
| tornado_http               | 94.3 ms                                                             | 96.4 ms: 1.02x slower                                                          |
| nqueens                    | 68.7 ms                                                             | 70.2 ms: 1.02x slower                                                          |
| async_tree_memoization_tg  | 254 ms                                                              | 261 ms: 1.03x slower                                                           |
| pycparser                  | 777 ms                                                              | 798 ms: 1.03x slower                                                           |
| json                       | 4.10 ms                                                             | 4.24 ms: 1.03x slower                                                          |
| 2to3                       | 233 ms                                                              | 242 ms: 1.04x slower                                                           |
| sqlglot_optimize           | 39.7 ms                                                             | 41.3 ms: 1.04x slower                                                          |
| regex_dna                  | 118 ms                                                              | 123 ms: 1.04x slower                                                           |
| pickle_list                | 3.57 us                                                             | 3.72 us: 1.04x slower                                                          |
| genshi_text                | 20.1 ms                                                             | 21.0 ms: 1.04x slower                                                          |
| chaos                      | 48.0 ms                                                             | 50.1 ms: 1.05x slower                                                          |
| regex_effbot               | 1.88 ms                                                             | 1.98 ms: 1.05x slower                                                          |
| django_template            | 30.1 ms                                                             | 31.7 ms: 1.05x slower                                                          |
| sympy_integrate            | 14.6 ms                                                             | 15.5 ms: 1.06x slower                                                          |
| deepcopy_reduce            | 2.59 us                                                             | 2.74 us: 1.06x slower                                                          |
| sqlglot_normalize          | 206 ms                                                              | 218 ms: 1.06x slower                                                           |
| bench_mp_pool              | 69.4 ms                                                             | 74.1 ms: 1.07x slower                                                          |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 504 ms: 1.07x slower                                                           |
| deepcopy                   | 280 us                                                              | 300 us: 1.07x slower                                                           |
| hexiom                     | 4.23 ms                                                             | 4.53 ms: 1.07x slower                                                          |
| unpickle                   | 9.79 us                                                             | 10.5 us: 1.07x slower                                                          |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 484 ms: 1.08x slower                                                           |
| pylint                     | 217 ms                                                              | 235 ms: 1.08x slower                                                           |
| generators                 | 21.2 ms                                                             | 23.0 ms: 1.09x slower                                                          |
| go                         | 101 ms                                                              | 109 ms: 1.09x slower                                                           |
| python_startup             | 22.2 ms                                                             | 24.2 ms: 1.09x slower                                                          |
| raytrace                   | 189 ms                                                              | 205 ms: 1.09x slower                                                           |
| python_startup_no_site     | 18.2 ms                                                             | 20.2 ms: 1.11x slower                                                          |
| scimark_sor                | 81.0 ms                                                             | 90.4 ms: 1.12x slower                                                          |
| deltablue                  | 2.23 ms                                                             | 2.54 ms: 1.14x slower                                                          |
| async_generators           | 266 ms                                                              | 305 ms: 1.15x slower                                                           |
| genshi_xml                 | 44.3 ms                                                             | 51.6 ms: 1.17x slower                                                          |
| scimark_lu                 | 59.4 ms                                                             | 71.1 ms: 1.20x slower                                                          |
| Geometric mean             | (ref)                                                               | 1.06x faster                                                                   |

Benchmark hidden because not significant (10): pickle_dict, asyncio_tcp_ssl, bench_thread_pool, typing_runtime_protocols, create_gc_cycles, gc_traversal, richards, async_tree_io, async_tree_none, async_tree_none_tg
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging

# HPT report

- Reliability score: 66.96% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown