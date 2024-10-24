# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: tier_two_improvement
- machine: windows-x86
- commit hash: bbb07e8
- commit date: 2024-07-13
- overall geometric mean: 1.05x faster
- HPT reliability: 64.77%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 251 ms: 1.08x slower                                                                 |
| docutils       | 1.81 sec                                                            | 1.91 sec: 1.05x slower                                                               |
| html5lib       | 45.4 ms                                                             | 47.5 ms: 1.05x slower                                                                |
| tornado_http   | 94.3 ms                                                             | 97.0 ms: 1.03x slower                                                                |
| Geometric mean | (ref)                                                               | 1.05x slower                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 529 ms                                                              | 498 ms: 1.06x faster                                                                 |
| async_tree_none_tg         | 203 ms                                                              | 194 ms: 1.05x faster                                                                 |
| async_tree_none            | 228 ms                                                              | 220 ms: 1.04x faster                                                                 |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 482 ms: 1.02x slower                                                                 |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 470 ms: 1.05x slower                                                                 |
| Geometric mean             | (ref)                                                               | 1.01x faster                                                                         |

Benchmark hidden because not significant (3): async_tree_memoization_tg, async_tree_memoization, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 61.2 ms: 1.26x faster                                                                |
| float          | 52.4 ms                                                             | 43.0 ms: 1.22x faster                                                                |
| pidigits       | 199 ms                                                              | 196 ms: 1.01x faster                                                                 |
| Geometric mean | (ref)                                                               | 1.16x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_compile  | 99.9 ms                                                             | 94.4 ms: 1.06x faster                                                                |
| Geometric mean | (ref)                                                               | 1.01x faster                                                                         |

Benchmark hidden because not significant (3): regex_dna, regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| tomli_loads          | 1.65 sec                                                            | 1.49 sec: 1.10x faster                                                               |
| xml_etree_iterparse  | 64.2 ms                                                             | 62.0 ms: 1.04x faster                                                                |
| xml_etree_generate   | 59.6 ms                                                             | 58.1 ms: 1.03x faster                                                                |
| unpickle_pure_python | 147 us                                                              | 146 us: 1.01x faster                                                                 |
| xml_etree_process    | 42.1 ms                                                             | 43.4 ms: 1.03x slower                                                                |
| json_dumps           | 6.84 ms                                                             | 7.17 ms: 1.05x slower                                                                |
| json_loads           | 20.5 us                                                             | 21.7 us: 1.06x slower                                                                |
| Geometric mean       | (ref)                                                               | 1.00x faster                                                                         |

Benchmark hidden because not significant (2): pickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 23.1 ms: 1.04x slower                                                                |
| python_startup_no_site | 18.2 ms                                                             | 19.3 ms: 1.06x slower                                                                |
| Geometric mean         | (ref)                                                               | 1.05x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 6.94 ms                                                             | 5.39 ms: 1.29x faster                                                                |
| django_template | 30.1 ms                                                             | 33.6 ms: 1.12x slower                                                                |
| genshi_text     | 20.1 ms                                                             | 22.9 ms: 1.14x slower                                                                |
| genshi_xml      | 44.3 ms                                                             | 52.9 ms: 1.20x slower                                                                |
| Geometric mean  | (ref)                                                               | 1.04x slower                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 760 us: 12.81x faster                                                                |
| coverage                   | 307 ms                                                              | 51.9 ms: 5.92x faster                                                                |
| deepcopy_memo              | 23.5 us                                                             | 15.8 us: 1.49x faster                                                                |
| spectral_norm              | 68.0 ms                                                             | 48.7 ms: 1.40x faster                                                                |
| mako                       | 6.94 ms                                                             | 5.39 ms: 1.29x faster                                                                |
| nbody                      | 76.9 ms                                                             | 61.2 ms: 1.26x faster                                                                |
| float                      | 52.4 ms                                                             | 43.0 ms: 1.22x faster                                                                |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 2.37 ms: 1.21x faster                                                                |
| fannkuch                   | 270 ms                                                              | 225 ms: 1.20x faster                                                                 |
| scimark_fft                | 198 ms                                                              | 166 ms: 1.20x faster                                                                 |
| crypto_pyaes               | 55.8 ms                                                             | 46.8 ms: 1.19x faster                                                                |
| pyflate                    | 308 ms                                                              | 263 ms: 1.17x faster                                                                 |
| deepcopy                   | 280 us                                                              | 240 us: 1.17x faster                                                                 |
| tomli_loads                | 1.65 sec                                                            | 1.49 sec: 1.10x faster                                                               |
| telco                      | 6.03 ms                                                             | 5.60 ms: 1.08x faster                                                                |
| pprint_safe_repr           | 607 ms                                                              | 563 ms: 1.08x faster                                                                 |
| deepcopy_reduce            | 2.59 us                                                             | 2.42 us: 1.07x faster                                                                |
| pprint_pformat             | 1.24 sec                                                            | 1.16 sec: 1.07x faster                                                               |
| async_tree_io_tg           | 529 ms                                                              | 498 ms: 1.06x faster                                                                 |
| asyncio_tcp                | 662 ms                                                              | 623 ms: 1.06x faster                                                                 |
| comprehensions             | 11.9 us                                                             | 11.2 us: 1.06x faster                                                                |
| regex_compile              | 99.9 ms                                                             | 94.4 ms: 1.06x faster                                                                |
| meteor_contest             | 74.1 ms                                                             | 70.1 ms: 1.06x faster                                                                |
| scimark_monte_carlo        | 45.2 ms                                                             | 42.8 ms: 1.05x faster                                                                |
| async_tree_none_tg         | 203 ms                                                              | 194 ms: 1.05x faster                                                                 |
| async_tree_none            | 228 ms                                                              | 220 ms: 1.04x faster                                                                 |
| xml_etree_iterparse        | 64.2 ms                                                             | 62.0 ms: 1.04x faster                                                                |
| xml_etree_generate         | 59.6 ms                                                             | 58.1 ms: 1.03x faster                                                                |
| sqlglot_parse              | 964 us                                                              | 942 us: 1.02x faster                                                                 |
| pidigits                   | 199 ms                                                              | 196 ms: 1.01x faster                                                                 |
| logging_format             | 8.13 us                                                             | 8.06 us: 1.01x faster                                                                |
| pathlib                    | 83.9 ms                                                             | 83.2 ms: 1.01x faster                                                                |
| logging_silent             | 57.9 ns                                                             | 57.4 ns: 1.01x faster                                                                |
| unpickle_pure_python       | 147 us                                                              | 146 us: 1.01x faster                                                                 |
| logging_simple             | 7.47 us                                                             | 7.44 us: 1.00x faster                                                                |
| sympy_expand               | 375 ms                                                              | 379 ms: 1.01x slower                                                                 |
| sympy_str                  | 211 ms                                                              | 214 ms: 1.01x slower                                                                 |
| sqlglot_transpile          | 1.19 ms                                                             | 1.21 ms: 1.02x slower                                                                |
| gc_traversal               | 1.43 ms                                                             | 1.46 ms: 1.02x slower                                                                |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 482 ms: 1.02x slower                                                                 |
| mdp                        | 1.60 sec                                                            | 1.64 sec: 1.02x slower                                                               |
| sympy_sum                  | 105 ms                                                              | 108 ms: 1.02x slower                                                                 |
| tornado_http               | 94.3 ms                                                             | 97.0 ms: 1.03x slower                                                                |
| xml_etree_process          | 42.1 ms                                                             | 43.4 ms: 1.03x slower                                                                |
| python_startup             | 22.2 ms                                                             | 23.1 ms: 1.04x slower                                                                |
| json                       | 4.10 ms                                                             | 4.27 ms: 1.04x slower                                                                |
| html5lib                   | 45.4 ms                                                             | 47.5 ms: 1.05x slower                                                                |
| json_dumps                 | 6.84 ms                                                             | 7.17 ms: 1.05x slower                                                                |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 470 ms: 1.05x slower                                                                 |
| docutils                   | 1.81 sec                                                            | 1.91 sec: 1.05x slower                                                               |
| json_loads                 | 20.5 us                                                             | 21.7 us: 1.06x slower                                                                |
| bench_mp_pool              | 69.4 ms                                                             | 73.4 ms: 1.06x slower                                                                |
| python_startup_no_site     | 18.2 ms                                                             | 19.3 ms: 1.06x slower                                                                |
| pycparser                  | 777 ms                                                              | 826 ms: 1.06x slower                                                                 |
| typing_runtime_protocols   | 136 us                                                              | 144 us: 1.06x slower                                                                 |
| nqueens                    | 68.7 ms                                                             | 73.7 ms: 1.07x slower                                                                |
| richards_super             | 35.5 ms                                                             | 38.2 ms: 1.08x slower                                                                |
| 2to3                       | 233 ms                                                              | 251 ms: 1.08x slower                                                                 |
| richards                   | 31.2 ms                                                             | 33.7 ms: 1.08x slower                                                                |
| sympy_integrate            | 14.6 ms                                                             | 15.9 ms: 1.08x slower                                                                |
| sqlglot_optimize           | 39.7 ms                                                             | 43.1 ms: 1.09x slower                                                                |
| pylint                     | 217 ms                                                              | 240 ms: 1.10x slower                                                                 |
| hexiom                     | 4.23 ms                                                             | 4.68 ms: 1.11x slower                                                                |
| coroutines                 | 15.5 ms                                                             | 17.1 ms: 1.11x slower                                                                |
| chaos                      | 48.0 ms                                                             | 53.3 ms: 1.11x slower                                                                |
| django_template            | 30.1 ms                                                             | 33.6 ms: 1.12x slower                                                                |
| go                         | 101 ms                                                              | 113 ms: 1.12x slower                                                                 |
| sqlglot_normalize          | 206 ms                                                              | 232 ms: 1.13x slower                                                                 |
| genshi_text                | 20.1 ms                                                             | 22.9 ms: 1.14x slower                                                                |
| deltablue                  | 2.23 ms                                                             | 2.67 ms: 1.19x slower                                                                |
| genshi_xml                 | 44.3 ms                                                             | 52.9 ms: 1.20x slower                                                                |
| generators                 | 21.2 ms                                                             | 25.5 ms: 1.20x slower                                                                |
| async_generators           | 266 ms                                                              | 321 ms: 1.21x slower                                                                 |
| raytrace                   | 189 ms                                                              | 229 ms: 1.22x slower                                                                 |
| scimark_sor                | 81.0 ms                                                             | 99.9 ms: 1.23x slower                                                                |
| scimark_lu                 | 59.4 ms                                                             | 80.4 ms: 1.35x slower                                                                |
| Geometric mean             | (ref)                                                               | 1.05x faster                                                                         |

Benchmark hidden because not significant (11): async_tree_memoization_tg, async_tree_memoization, bench_thread_pool, asyncio_tcp_ssl, pickle_pure_python, regex_dna, create_gc_cycles, regex_v8, xml_etree_parse, async_tree_io, regex_effbot
Ignored benchmarks (8) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 64.77% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown