# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: no_cold_exits
- machine: windows-x86
- commit hash: a1bdb94
- commit date: 2024-06-18
- overall geometric mean: 1.05x faster
- HPT reliability: 98.01%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 249 ms: 1.07x slower                                                          |
| docutils       | 1.81 sec                                                            | 1.92 sec: 1.06x slower                                                        |
| html5lib       | 45.4 ms                                                             | 48.9 ms: 1.08x slower                                                         |
| tornado_http   | 94.3 ms                                                             | 97.8 ms: 1.04x slower                                                         |
| Geometric mean | (ref)                                                               | 1.06x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 460 ms: 1.03x slower                                                          |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 488 ms: 1.04x slower                                                          |
| async_tree_memoization_tg  | 254 ms                                                              | 263 ms: 1.04x slower                                                          |
| async_tree_io_tg           | 529 ms                                                              | 549 ms: 1.04x slower                                                          |
| async_tree_none            | 228 ms                                                              | 238 ms: 1.05x slower                                                          |
| async_tree_io              | 530 ms                                                              | 555 ms: 1.05x slower                                                          |
| async_tree_none_tg         | 203 ms                                                              | 213 ms: 1.05x slower                                                          |
| async_tree_memoization     | 275 ms                                                              | 289 ms: 1.05x slower                                                          |
| Geometric mean             | (ref)                                                               | 1.04x slower                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 52.5 ms: 1.46x faster                                                         |
| float          | 52.4 ms                                                             | 43.0 ms: 1.22x faster                                                         |
| pidigits       | 199 ms                                                              | 197 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                               | 1.22x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 99.9 ms                                                             | 94.7 ms: 1.05x faster                                                         |
| regex_v8       | 15.7 ms                                                             | 16.0 ms: 1.02x slower                                                         |
| regex_effbot   | 1.88 ms                                                             | 2.07 ms: 1.10x slower                                                         |
| regex_dna      | 118 ms                                                              | 132 ms: 1.11x slower                                                          |
| Geometric mean | (ref)                                                               | 1.04x slower                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 1.65 sec                                                            | 1.48 sec: 1.11x faster                                                        |
| xml_etree_iterparse  | 64.2 ms                                                             | 61.3 ms: 1.05x faster                                                         |
| unpickle_pure_python | 147 us                                                              | 143 us: 1.03x faster                                                          |
| xml_etree_parse      | 104 ms                                                              | 102 ms: 1.02x faster                                                          |
| xml_etree_generate   | 59.6 ms                                                             | 58.3 ms: 1.02x faster                                                         |
| pickle_pure_python   | 213 us                                                              | 210 us: 1.02x faster                                                          |
| unpickle_list        | 2.93 us                                                             | 2.89 us: 1.01x faster                                                         |
| pickle_dict          | 20.8 us                                                             | 20.6 us: 1.01x faster                                                         |
| json_dumps           | 6.84 ms                                                             | 7.01 ms: 1.02x slower                                                         |
| xml_etree_process    | 42.1 ms                                                             | 43.2 ms: 1.03x slower                                                         |
| unpickle             | 9.79 us                                                             | 10.1 us: 1.03x slower                                                         |
| pickle               | 8.07 us                                                             | 8.35 us: 1.03x slower                                                         |
| Geometric mean       | (ref)                                                               | 1.01x faster                                                                  |

Benchmark hidden because not significant (2): json_loads, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 18.2 ms                                                             | 18.6 ms: 1.02x slower                                                         |
| python_startup         | 22.2 ms                                                             | 22.8 ms: 1.02x slower                                                         |
| Geometric mean         | (ref)                                                               | 1.02x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|-----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 6.94 ms                                                             | 5.50 ms: 1.26x faster                                                         |
| genshi_text     | 20.1 ms                                                             | 21.1 ms: 1.05x slower                                                         |
| django_template | 30.1 ms                                                             | 32.9 ms: 1.09x slower                                                         |
| genshi_xml      | 44.3 ms                                                             | 51.7 ms: 1.17x slower                                                         |
| Geometric mean  | (ref)                                                               | 1.01x slower                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 764 us: 12.74x faster                                                         |
| coverage                   | 307 ms                                                              | 50.9 ms: 6.04x faster                                                         |
| deepcopy_memo              | 23.5 us                                                             | 15.4 us: 1.52x faster                                                         |
| nbody                      | 76.9 ms                                                             | 52.5 ms: 1.46x faster                                                         |
| spectral_norm              | 68.0 ms                                                             | 49.3 ms: 1.38x faster                                                         |
| mako                       | 6.94 ms                                                             | 5.50 ms: 1.26x faster                                                         |
| fannkuch                   | 270 ms                                                              | 215 ms: 1.25x faster                                                          |
| float                      | 52.4 ms                                                             | 43.0 ms: 1.22x faster                                                         |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 2.40 ms: 1.20x faster                                                         |
| deepcopy                   | 280 us                                                              | 234 us: 1.19x faster                                                          |
| scimark_fft                | 198 ms                                                              | 169 ms: 1.17x faster                                                          |
| crypto_pyaes               | 55.8 ms                                                             | 48.1 ms: 1.16x faster                                                         |
| scimark_monte_carlo        | 45.2 ms                                                             | 39.7 ms: 1.14x faster                                                         |
| tomli_loads                | 1.65 sec                                                            | 1.48 sec: 1.11x faster                                                        |
| pprint_safe_repr           | 607 ms                                                              | 553 ms: 1.10x faster                                                          |
| pyflate                    | 308 ms                                                              | 283 ms: 1.09x faster                                                          |
| pprint_pformat             | 1.24 sec                                                            | 1.14 sec: 1.09x faster                                                        |
| deepcopy_reduce            | 2.59 us                                                             | 2.39 us: 1.08x faster                                                         |
| asyncio_tcp                | 662 ms                                                              | 617 ms: 1.07x faster                                                          |
| telco                      | 6.03 ms                                                             | 5.64 ms: 1.07x faster                                                         |
| comprehensions             | 11.9 us                                                             | 11.2 us: 1.06x faster                                                         |
| regex_compile              | 99.9 ms                                                             | 94.7 ms: 1.05x faster                                                         |
| xml_etree_iterparse        | 64.2 ms                                                             | 61.3 ms: 1.05x faster                                                         |
| sqlite_synth               | 1.96 us                                                             | 1.90 us: 1.03x faster                                                         |
| unpickle_pure_python       | 147 us                                                              | 143 us: 1.03x faster                                                          |
| sqlglot_parse              | 964 us                                                              | 939 us: 1.03x faster                                                          |
| xml_etree_parse            | 104 ms                                                              | 102 ms: 1.02x faster                                                          |
| xml_etree_generate         | 59.6 ms                                                             | 58.3 ms: 1.02x faster                                                         |
| meteor_contest             | 74.1 ms                                                             | 72.6 ms: 1.02x faster                                                         |
| pickle_pure_python         | 213 us                                                              | 210 us: 1.02x faster                                                          |
| unpickle_list              | 2.93 us                                                             | 2.89 us: 1.01x faster                                                         |
| pathlib                    | 83.9 ms                                                             | 82.8 ms: 1.01x faster                                                         |
| pidigits                   | 199 ms                                                              | 197 ms: 1.01x faster                                                          |
| logging_silent             | 57.9 ns                                                             | 57.4 ns: 1.01x faster                                                         |
| pickle_dict                | 20.8 us                                                             | 20.6 us: 1.01x faster                                                         |
| sqlglot_transpile          | 1.19 ms                                                             | 1.20 ms: 1.01x slower                                                         |
| logging_format             | 8.13 us                                                             | 8.21 us: 1.01x slower                                                         |
| json                       | 4.10 ms                                                             | 4.14 ms: 1.01x slower                                                         |
| logging_simple             | 7.47 us                                                             | 7.56 us: 1.01x slower                                                         |
| sympy_expand               | 375 ms                                                              | 381 ms: 1.01x slower                                                          |
| sympy_str                  | 211 ms                                                              | 214 ms: 1.02x slower                                                          |
| regex_v8                   | 15.7 ms                                                             | 16.0 ms: 1.02x slower                                                         |
| python_startup_no_site     | 18.2 ms                                                             | 18.6 ms: 1.02x slower                                                         |
| sympy_sum                  | 105 ms                                                              | 108 ms: 1.02x slower                                                          |
| json_dumps                 | 6.84 ms                                                             | 7.01 ms: 1.02x slower                                                         |
| python_startup             | 22.2 ms                                                             | 22.8 ms: 1.02x slower                                                         |
| xml_etree_process          | 42.1 ms                                                             | 43.2 ms: 1.03x slower                                                         |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 460 ms: 1.03x slower                                                          |
| unpickle                   | 9.79 us                                                             | 10.1 us: 1.03x slower                                                         |
| pickle                     | 8.07 us                                                             | 8.35 us: 1.03x slower                                                         |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 488 ms: 1.04x slower                                                          |
| async_tree_memoization_tg  | 254 ms                                                              | 263 ms: 1.04x slower                                                          |
| async_tree_io_tg           | 529 ms                                                              | 549 ms: 1.04x slower                                                          |
| tornado_http               | 94.3 ms                                                             | 97.8 ms: 1.04x slower                                                         |
| mdp                        | 1.60 sec                                                            | 1.67 sec: 1.04x slower                                                        |
| richards                   | 31.2 ms                                                             | 32.6 ms: 1.05x slower                                                         |
| async_tree_none            | 228 ms                                                              | 238 ms: 1.05x slower                                                          |
| nqueens                    | 68.7 ms                                                             | 71.9 ms: 1.05x slower                                                         |
| async_tree_io              | 530 ms                                                              | 555 ms: 1.05x slower                                                          |
| async_tree_none_tg         | 203 ms                                                              | 213 ms: 1.05x slower                                                          |
| async_tree_memoization     | 275 ms                                                              | 289 ms: 1.05x slower                                                          |
| genshi_text                | 20.1 ms                                                             | 21.1 ms: 1.05x slower                                                         |
| typing_runtime_protocols   | 136 us                                                              | 142 us: 1.05x slower                                                          |
| docutils                   | 1.81 sec                                                            | 1.92 sec: 1.06x slower                                                        |
| bench_mp_pool              | 69.4 ms                                                             | 73.5 ms: 1.06x slower                                                         |
| pycparser                  | 777 ms                                                              | 827 ms: 1.06x slower                                                          |
| richards_super             | 35.5 ms                                                             | 37.8 ms: 1.07x slower                                                         |
| 2to3                       | 233 ms                                                              | 249 ms: 1.07x slower                                                          |
| html5lib                   | 45.4 ms                                                             | 48.9 ms: 1.08x slower                                                         |
| hexiom                     | 4.23 ms                                                             | 4.55 ms: 1.08x slower                                                         |
| sympy_integrate            | 14.6 ms                                                             | 15.8 ms: 1.08x slower                                                         |
| sqlglot_optimize           | 39.7 ms                                                             | 43.2 ms: 1.09x slower                                                         |
| django_template            | 30.1 ms                                                             | 32.9 ms: 1.09x slower                                                         |
| regex_effbot               | 1.88 ms                                                             | 2.07 ms: 1.10x slower                                                         |
| go                         | 101 ms                                                              | 111 ms: 1.10x slower                                                          |
| chaos                      | 48.0 ms                                                             | 53.1 ms: 1.11x slower                                                         |
| regex_dna                  | 118 ms                                                              | 132 ms: 1.11x slower                                                          |
| pylint                     | 217 ms                                                              | 243 ms: 1.12x slower                                                          |
| async_generators           | 266 ms                                                              | 302 ms: 1.14x slower                                                          |
| coroutines                 | 15.5 ms                                                             | 17.7 ms: 1.14x slower                                                         |
| sqlglot_normalize          | 206 ms                                                              | 236 ms: 1.14x slower                                                          |
| genshi_xml                 | 44.3 ms                                                             | 51.7 ms: 1.17x slower                                                         |
| scimark_sor                | 81.0 ms                                                             | 96.2 ms: 1.19x slower                                                         |
| raytrace                   | 189 ms                                                              | 227 ms: 1.20x slower                                                          |
| deltablue                  | 2.23 ms                                                             | 2.74 ms: 1.23x slower                                                         |
| scimark_lu                 | 59.4 ms                                                             | 74.8 ms: 1.26x slower                                                         |
| generators                 | 21.2 ms                                                             | 27.9 ms: 1.32x slower                                                         |
| Geometric mean             | (ref)                                                               | 1.05x faster                                                                  |

Benchmark hidden because not significant (6): bench_thread_pool, asyncio_tcp_ssl, json_loads, gc_traversal, create_gc_cycles, pickle_list
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging

# HPT report

- Reliability score: 98.01% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown