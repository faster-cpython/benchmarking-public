# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: justin_compact
- machine: windows-x86
- commit hash: 34e6994
- commit date: 2024-06-20
- overall geometric mean: 1.03x faster
- HPT reliability: 99.32%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 257 ms: 1.10x slower                                                           |
| docutils       | 1.81 sec                                                            | 1.93 sec: 1.06x slower                                                         |
| html5lib       | 45.4 ms                                                             | 48.6 ms: 1.07x slower                                                          |
| tornado_http   | 94.3 ms                                                             | 97.8 ms: 1.04x slower                                                          |
| Geometric mean | (ref)                                                               | 1.07x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg           | 529 ms                                                              | 541 ms: 1.02x slower                                                           |
| async_tree_io              | 530 ms                                                              | 559 ms: 1.05x slower                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 498 ms: 1.06x slower                                                           |
| async_tree_memoization_tg  | 254 ms                                                              | 269 ms: 1.06x slower                                                           |
| async_tree_none            | 228 ms                                                              | 242 ms: 1.06x slower                                                           |
| async_tree_none_tg         | 203 ms                                                              | 217 ms: 1.07x slower                                                           |
| async_tree_memoization     | 275 ms                                                              | 295 ms: 1.07x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 481 ms: 1.08x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.06x slower                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 54.4 ms: 1.41x faster                                                          |
| float          | 52.4 ms                                                             | 43.1 ms: 1.22x faster                                                          |
| pidigits       | 199 ms                                                              | 195 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                               | 1.20x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 99.9 ms                                                             | 93.6 ms: 1.07x faster                                                          |
| regex_v8       | 15.7 ms                                                             | 16.0 ms: 1.01x slower                                                          |
| regex_dna      | 118 ms                                                              | 129 ms: 1.09x slower                                                           |
| regex_effbot   | 1.88 ms                                                             | 2.07 ms: 1.10x slower                                                          |
| Geometric mean | (ref)                                                               | 1.03x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 1.65 sec                                                            | 1.50 sec: 1.10x faster                                                         |
| unpickle_list        | 2.93 us                                                             | 2.78 us: 1.06x faster                                                          |
| xml_etree_iterparse  | 64.2 ms                                                             | 61.9 ms: 1.04x faster                                                          |
| xml_etree_generate   | 59.6 ms                                                             | 57.8 ms: 1.03x faster                                                          |
| unpickle_pure_python | 147 us                                                              | 146 us: 1.01x faster                                                           |
| pickle_pure_python   | 213 us                                                              | 211 us: 1.01x faster                                                           |
| json_loads           | 20.5 us                                                             | 20.7 us: 1.01x slower                                                          |
| xml_etree_process    | 42.1 ms                                                             | 42.8 ms: 1.02x slower                                                          |
| pickle               | 8.07 us                                                             | 8.28 us: 1.03x slower                                                          |
| unpickle             | 9.79 us                                                             | 10.3 us: 1.05x slower                                                          |
| pickle_list          | 3.57 us                                                             | 4.10 us: 1.15x slower                                                          |
| Geometric mean       | (ref)                                                               | 1.00x slower                                                                   |

Benchmark hidden because not significant (3): xml_etree_parse, pickle_dict, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 25.1 ms: 1.13x slower                                                          |
| python_startup_no_site | 18.2 ms                                                             | 21.0 ms: 1.15x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.14x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 6.94 ms                                                             | 5.34 ms: 1.30x faster                                                          |
| genshi_text     | 20.1 ms                                                             | 21.4 ms: 1.06x slower                                                          |
| django_template | 30.1 ms                                                             | 34.1 ms: 1.14x slower                                                          |
| genshi_xml      | 44.3 ms                                                             | 51.0 ms: 1.15x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.02x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 756 us: 12.86x faster                                                          |
| coverage                   | 307 ms                                                              | 49.6 ms: 6.20x faster                                                          |
| deepcopy_memo              | 23.5 us                                                             | 15.8 us: 1.49x faster                                                          |
| nbody                      | 76.9 ms                                                             | 54.4 ms: 1.41x faster                                                          |
| spectral_norm              | 68.0 ms                                                             | 49.0 ms: 1.39x faster                                                          |
| mako                       | 6.94 ms                                                             | 5.34 ms: 1.30x faster                                                          |
| fannkuch                   | 270 ms                                                              | 213 ms: 1.27x faster                                                           |
| float                      | 52.4 ms                                                             | 43.1 ms: 1.22x faster                                                          |
| deepcopy                   | 280 us                                                              | 238 us: 1.18x faster                                                           |
| scimark_fft                | 198 ms                                                              | 170 ms: 1.16x faster                                                           |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 2.48 ms: 1.16x faster                                                          |
| crypto_pyaes               | 55.8 ms                                                             | 48.5 ms: 1.15x faster                                                          |
| pyflate                    | 308 ms                                                              | 277 ms: 1.11x faster                                                           |
| deepcopy_reduce            | 2.59 us                                                             | 2.35 us: 1.10x faster                                                          |
| scimark_monte_carlo        | 45.2 ms                                                             | 41.2 ms: 1.10x faster                                                          |
| tomli_loads                | 1.65 sec                                                            | 1.50 sec: 1.10x faster                                                         |
| regex_compile              | 99.9 ms                                                             | 93.6 ms: 1.07x faster                                                          |
| unpickle_list              | 2.93 us                                                             | 2.78 us: 1.06x faster                                                          |
| asyncio_tcp                | 662 ms                                                              | 629 ms: 1.05x faster                                                           |
| sqlglot_parse              | 964 us                                                              | 922 us: 1.05x faster                                                           |
| pprint_safe_repr           | 607 ms                                                              | 584 ms: 1.04x faster                                                           |
| comprehensions             | 11.9 us                                                             | 11.4 us: 1.04x faster                                                          |
| xml_etree_iterparse        | 64.2 ms                                                             | 61.9 ms: 1.04x faster                                                          |
| pprint_pformat             | 1.24 sec                                                            | 1.20 sec: 1.03x faster                                                         |
| xml_etree_generate         | 59.6 ms                                                             | 57.8 ms: 1.03x faster                                                          |
| sqlite_synth               | 1.96 us                                                             | 1.92 us: 1.02x faster                                                          |
| pidigits                   | 199 ms                                                              | 195 ms: 1.02x faster                                                           |
| unpickle_pure_python       | 147 us                                                              | 146 us: 1.01x faster                                                           |
| pickle_pure_python         | 213 us                                                              | 211 us: 1.01x faster                                                           |
| meteor_contest             | 74.1 ms                                                             | 73.4 ms: 1.01x faster                                                          |
| pathlib                    | 83.9 ms                                                             | 83.3 ms: 1.01x faster                                                          |
| logging_silent             | 57.9 ns                                                             | 58.3 ns: 1.01x slower                                                          |
| json_loads                 | 20.5 us                                                             | 20.7 us: 1.01x slower                                                          |
| regex_v8                   | 15.7 ms                                                             | 16.0 ms: 1.01x slower                                                          |
| xml_etree_process          | 42.1 ms                                                             | 42.8 ms: 1.02x slower                                                          |
| gc_traversal               | 1.43 ms                                                             | 1.46 ms: 1.02x slower                                                          |
| logging_format             | 8.13 us                                                             | 8.31 us: 1.02x slower                                                          |
| hexiom                     | 4.23 ms                                                             | 4.32 ms: 1.02x slower                                                          |
| mdp                        | 1.60 sec                                                            | 1.64 sec: 1.02x slower                                                         |
| async_tree_io_tg           | 529 ms                                                              | 541 ms: 1.02x slower                                                           |
| logging_simple             | 7.47 us                                                             | 7.65 us: 1.02x slower                                                          |
| pickle                     | 8.07 us                                                             | 8.28 us: 1.03x slower                                                          |
| sympy_str                  | 211 ms                                                              | 217 ms: 1.03x slower                                                           |
| tornado_http               | 94.3 ms                                                             | 97.8 ms: 1.04x slower                                                          |
| nqueens                    | 68.7 ms                                                             | 71.2 ms: 1.04x slower                                                          |
| sympy_expand               | 375 ms                                                              | 389 ms: 1.04x slower                                                           |
| sympy_sum                  | 105 ms                                                              | 109 ms: 1.04x slower                                                           |
| async_tree_io              | 530 ms                                                              | 559 ms: 1.05x slower                                                           |
| unpickle                   | 9.79 us                                                             | 10.3 us: 1.05x slower                                                          |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 498 ms: 1.06x slower                                                           |
| async_tree_memoization_tg  | 254 ms                                                              | 269 ms: 1.06x slower                                                           |
| async_tree_none            | 228 ms                                                              | 242 ms: 1.06x slower                                                           |
| genshi_text                | 20.1 ms                                                             | 21.4 ms: 1.06x slower                                                          |
| docutils                   | 1.81 sec                                                            | 1.93 sec: 1.06x slower                                                         |
| async_tree_none_tg         | 203 ms                                                              | 217 ms: 1.07x slower                                                           |
| pycparser                  | 777 ms                                                              | 831 ms: 1.07x slower                                                           |
| html5lib                   | 45.4 ms                                                             | 48.6 ms: 1.07x slower                                                          |
| async_tree_memoization     | 275 ms                                                              | 295 ms: 1.07x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 481 ms: 1.08x slower                                                           |
| sqlglot_optimize           | 39.7 ms                                                             | 43.2 ms: 1.09x slower                                                          |
| typing_runtime_protocols   | 136 us                                                              | 148 us: 1.09x slower                                                           |
| sympy_integrate            | 14.6 ms                                                             | 16.0 ms: 1.09x slower                                                          |
| regex_dna                  | 118 ms                                                              | 129 ms: 1.09x slower                                                           |
| bench_mp_pool              | 69.4 ms                                                             | 76.1 ms: 1.10x slower                                                          |
| regex_effbot               | 1.88 ms                                                             | 2.07 ms: 1.10x slower                                                          |
| 2to3                       | 233 ms                                                              | 257 ms: 1.10x slower                                                           |
| json                       | 4.10 ms                                                             | 4.52 ms: 1.10x slower                                                          |
| richards_super             | 35.5 ms                                                             | 39.3 ms: 1.11x slower                                                          |
| pylint                     | 217 ms                                                              | 244 ms: 1.12x slower                                                           |
| richards                   | 31.2 ms                                                             | 35.2 ms: 1.13x slower                                                          |
| python_startup             | 22.2 ms                                                             | 25.1 ms: 1.13x slower                                                          |
| sqlglot_normalize          | 206 ms                                                              | 233 ms: 1.13x slower                                                           |
| coroutines                 | 15.5 ms                                                             | 17.5 ms: 1.13x slower                                                          |
| go                         | 101 ms                                                              | 114 ms: 1.13x slower                                                           |
| django_template            | 30.1 ms                                                             | 34.1 ms: 1.14x slower                                                          |
| async_generators           | 266 ms                                                              | 305 ms: 1.15x slower                                                           |
| pickle_list                | 3.57 us                                                             | 4.10 us: 1.15x slower                                                          |
| python_startup_no_site     | 18.2 ms                                                             | 21.0 ms: 1.15x slower                                                          |
| genshi_xml                 | 44.3 ms                                                             | 51.0 ms: 1.15x slower                                                          |
| chaos                      | 48.0 ms                                                             | 56.1 ms: 1.17x slower                                                          |
| scimark_sor                | 81.0 ms                                                             | 99.5 ms: 1.23x slower                                                          |
| deltablue                  | 2.23 ms                                                             | 2.78 ms: 1.24x slower                                                          |
| raytrace                   | 189 ms                                                              | 241 ms: 1.28x slower                                                           |
| scimark_lu                 | 59.4 ms                                                             | 75.9 ms: 1.28x slower                                                          |
| generators                 | 21.2 ms                                                             | 27.7 ms: 1.31x slower                                                          |
| Geometric mean             | (ref)                                                               | 1.03x faster                                                                   |

Benchmark hidden because not significant (8): bench_thread_pool, create_gc_cycles, sqlglot_transpile, xml_etree_parse, asyncio_tcp_ssl, pickle_dict, telco, json_dumps
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging

# HPT report

- Reliability score: 99.32% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown