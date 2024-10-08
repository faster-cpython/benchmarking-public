# Results vs. 3.13.0b2

- fork: python
- ref: a9d56e38a08ec198a228
- machine: windows-x86
- commit hash: a9d56e3
- commit date: 2024-08-01
- overall geometric mean: 1.04x faster
- HPT reliability: 88.97%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 258 ms: 1.11x slower                                                           |
| docutils       | 1.81 sec                                                            | 1.94 sec: 1.07x slower                                                         |
| html5lib       | 45.4 ms                                                             | 46.8 ms: 1.03x slower                                                          |
| tornado_http   | 94.3 ms                                                             | 107 ms: 1.13x slower                                                           |
| Geometric mean | (ref)                                                               | 1.09x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg           | 529 ms                                                              | 504 ms: 1.05x faster                                                           |
| async_tree_none_tg         | 203 ms                                                              | 195 ms: 1.04x faster                                                           |
| async_tree_none            | 228 ms                                                              | 223 ms: 1.02x faster                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 466 ms: 1.01x faster                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 454 ms: 1.01x slower                                                           |
| async_tree_io              | 530 ms                                                              | 544 ms: 1.03x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.01x faster                                                                   |

Benchmark hidden because not significant (2): async_tree_memoization_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 52.2 ms: 1.47x faster                                                          |
| float          | 52.4 ms                                                             | 42.8 ms: 1.22x faster                                                          |
| pidigits       | 199 ms                                                              | 200 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                               | 1.21x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 99.9 ms                                                             | 94.5 ms: 1.06x faster                                                          |
| regex_dna      | 118 ms                                                              | 116 ms: 1.01x faster                                                           |
| regex_v8       | 15.7 ms                                                             | 16.0 ms: 1.02x slower                                                          |
| regex_effbot   | 1.88 ms                                                             | 1.99 ms: 1.05x slower                                                          |
| Geometric mean | (ref)                                                               | 1.00x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 1.65 sec                                                            | 1.51 sec: 1.09x faster                                                         |
| pickle_pure_python   | 213 us                                                              | 209 us: 1.02x faster                                                           |
| unpickle_pure_python | 147 us                                                              | 145 us: 1.01x faster                                                           |
| xml_etree_iterparse  | 64.2 ms                                                             | 63.6 ms: 1.01x faster                                                          |
| xml_etree_generate   | 59.6 ms                                                             | 59.1 ms: 1.01x faster                                                          |
| json_loads           | 20.5 us                                                             | 20.8 us: 1.01x slower                                                          |
| xml_etree_parse      | 104 ms                                                              | 107 ms: 1.02x slower                                                           |
| json_dumps           | 6.84 ms                                                             | 7.06 ms: 1.03x slower                                                          |
| xml_etree_process    | 42.1 ms                                                             | 44.0 ms: 1.05x slower                                                          |
| Geometric mean       | (ref)                                                               | 1.00x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 18.2 ms                                                             | 19.6 ms: 1.08x slower                                                          |
| python_startup         | 22.2 ms                                                             | 24.0 ms: 1.08x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.08x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 6.94 ms                                                             | 5.38 ms: 1.29x faster                                                          |
| django_template | 30.1 ms                                                             | 32.8 ms: 1.09x slower                                                          |
| genshi_text     | 20.1 ms                                                             | 22.9 ms: 1.14x slower                                                          |
| genshi_xml      | 44.3 ms                                                             | 50.8 ms: 1.15x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.03x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 769 us: 12.65x faster                                                          |
| coverage                   | 307 ms                                                              | 51.0 ms: 6.03x faster                                                          |
| nbody                      | 76.9 ms                                                             | 52.2 ms: 1.47x faster                                                          |
| deepcopy_memo              | 23.5 us                                                             | 16.0 us: 1.47x faster                                                          |
| spectral_norm              | 68.0 ms                                                             | 47.3 ms: 1.44x faster                                                          |
| mako                       | 6.94 ms                                                             | 5.38 ms: 1.29x faster                                                          |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 2.31 ms: 1.24x faster                                                          |
| float                      | 52.4 ms                                                             | 42.8 ms: 1.22x faster                                                          |
| crypto_pyaes               | 55.8 ms                                                             | 45.9 ms: 1.22x faster                                                          |
| fannkuch                   | 270 ms                                                              | 224 ms: 1.21x faster                                                           |
| scimark_fft                | 198 ms                                                              | 166 ms: 1.20x faster                                                           |
| pyflate                    | 308 ms                                                              | 260 ms: 1.19x faster                                                           |
| deepcopy                   | 280 us                                                              | 251 us: 1.12x faster                                                           |
| scimark_monte_carlo        | 45.2 ms                                                             | 41.2 ms: 1.10x faster                                                          |
| tomli_loads                | 1.65 sec                                                            | 1.51 sec: 1.09x faster                                                         |
| regex_compile              | 99.9 ms                                                             | 94.5 ms: 1.06x faster                                                          |
| comprehensions             | 11.9 us                                                             | 11.3 us: 1.05x faster                                                          |
| meteor_contest             | 74.1 ms                                                             | 70.4 ms: 1.05x faster                                                          |
| async_tree_io_tg           | 529 ms                                                              | 504 ms: 1.05x faster                                                           |
| deepcopy_reduce            | 2.59 us                                                             | 2.49 us: 1.04x faster                                                          |
| async_tree_none_tg         | 203 ms                                                              | 195 ms: 1.04x faster                                                           |
| telco                      | 6.03 ms                                                             | 5.88 ms: 1.03x faster                                                          |
| async_tree_none            | 228 ms                                                              | 223 ms: 1.02x faster                                                           |
| pprint_pformat             | 1.24 sec                                                            | 1.22 sec: 1.02x faster                                                         |
| logging_silent             | 57.9 ns                                                             | 56.8 ns: 1.02x faster                                                          |
| pickle_pure_python         | 213 us                                                              | 209 us: 1.02x faster                                                           |
| pprint_safe_repr           | 607 ms                                                              | 597 ms: 1.02x faster                                                           |
| unpickle_pure_python       | 147 us                                                              | 145 us: 1.01x faster                                                           |
| regex_dna                  | 118 ms                                                              | 116 ms: 1.01x faster                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 466 ms: 1.01x faster                                                           |
| xml_etree_iterparse        | 64.2 ms                                                             | 63.6 ms: 1.01x faster                                                          |
| xml_etree_generate         | 59.6 ms                                                             | 59.1 ms: 1.01x faster                                                          |
| pidigits                   | 199 ms                                                              | 200 ms: 1.01x slower                                                           |
| create_gc_cycles           | 756 us                                                              | 764 us: 1.01x slower                                                           |
| json_loads                 | 20.5 us                                                             | 20.8 us: 1.01x slower                                                          |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 454 ms: 1.01x slower                                                           |
| regex_v8                   | 15.7 ms                                                             | 16.0 ms: 1.02x slower                                                          |
| xml_etree_parse            | 104 ms                                                              | 107 ms: 1.02x slower                                                           |
| pycparser                  | 777 ms                                                              | 794 ms: 1.02x slower                                                           |
| gc_traversal               | 1.43 ms                                                             | 1.47 ms: 1.02x slower                                                          |
| sqlglot_parse              | 964 us                                                              | 988 us: 1.03x slower                                                           |
| async_tree_io              | 530 ms                                                              | 544 ms: 1.03x slower                                                           |
| html5lib                   | 45.4 ms                                                             | 46.8 ms: 1.03x slower                                                          |
| json_dumps                 | 6.84 ms                                                             | 7.06 ms: 1.03x slower                                                          |
| logging_simple             | 7.47 us                                                             | 7.72 us: 1.03x slower                                                          |
| logging_format             | 8.13 us                                                             | 8.44 us: 1.04x slower                                                          |
| sympy_str                  | 211 ms                                                              | 220 ms: 1.04x slower                                                           |
| sympy_expand               | 375 ms                                                              | 392 ms: 1.04x slower                                                           |
| xml_etree_process          | 42.1 ms                                                             | 44.0 ms: 1.05x slower                                                          |
| richards                   | 31.2 ms                                                             | 32.7 ms: 1.05x slower                                                          |
| regex_effbot               | 1.88 ms                                                             | 1.99 ms: 1.05x slower                                                          |
| richards_super             | 35.5 ms                                                             | 37.4 ms: 1.06x slower                                                          |
| sympy_sum                  | 105 ms                                                              | 111 ms: 1.06x slower                                                           |
| pathlib                    | 83.9 ms                                                             | 88.6 ms: 1.06x slower                                                          |
| sqlglot_transpile          | 1.19 ms                                                             | 1.27 ms: 1.06x slower                                                          |
| nqueens                    | 68.7 ms                                                             | 73.1 ms: 1.06x slower                                                          |
| docutils                   | 1.81 sec                                                            | 1.94 sec: 1.07x slower                                                         |
| python_startup_no_site     | 18.2 ms                                                             | 19.6 ms: 1.08x slower                                                          |
| mdp                        | 1.60 sec                                                            | 1.73 sec: 1.08x slower                                                         |
| python_startup             | 22.2 ms                                                             | 24.0 ms: 1.08x slower                                                          |
| sqlglot_normalize          | 206 ms                                                              | 222 ms: 1.08x slower                                                           |
| json                       | 4.10 ms                                                             | 4.44 ms: 1.08x slower                                                          |
| generators                 | 21.2 ms                                                             | 22.9 ms: 1.08x slower                                                          |
| sqlglot_optimize           | 39.7 ms                                                             | 43.1 ms: 1.08x slower                                                          |
| django_template            | 30.1 ms                                                             | 32.8 ms: 1.09x slower                                                          |
| chaos                      | 48.0 ms                                                             | 52.5 ms: 1.10x slower                                                          |
| go                         | 101 ms                                                              | 111 ms: 1.10x slower                                                           |
| 2to3                       | 233 ms                                                              | 258 ms: 1.11x slower                                                           |
| hexiom                     | 4.23 ms                                                             | 4.69 ms: 1.11x slower                                                          |
| bench_mp_pool              | 69.4 ms                                                             | 77.3 ms: 1.11x slower                                                          |
| sympy_integrate            | 14.6 ms                                                             | 16.4 ms: 1.12x slower                                                          |
| typing_runtime_protocols   | 136 us                                                              | 153 us: 1.13x slower                                                           |
| tornado_http               | 94.3 ms                                                             | 107 ms: 1.13x slower                                                           |
| genshi_text                | 20.1 ms                                                             | 22.9 ms: 1.14x slower                                                          |
| coroutines                 | 15.5 ms                                                             | 17.8 ms: 1.15x slower                                                          |
| genshi_xml                 | 44.3 ms                                                             | 50.8 ms: 1.15x slower                                                          |
| pylint                     | 217 ms                                                              | 253 ms: 1.17x slower                                                           |
| async_generators           | 266 ms                                                              | 313 ms: 1.18x slower                                                           |
| deltablue                  | 2.23 ms                                                             | 2.71 ms: 1.21x slower                                                          |
| raytrace                   | 189 ms                                                              | 229 ms: 1.21x slower                                                           |
| scimark_sor                | 81.0 ms                                                             | 99.7 ms: 1.23x slower                                                          |
| scimark_lu                 | 59.4 ms                                                             | 73.9 ms: 1.24x slower                                                          |
| Geometric mean             | (ref)                                                               | 1.04x faster                                                                   |

Benchmark hidden because not significant (5): async_tree_memoization_tg, bench_thread_pool, asyncio_tcp_ssl, async_tree_memoization, asyncio_tcp
Ignored benchmarks (8) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240801-3.14.0a0-a9d56e3-JIT/bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3.json: dulwich_log

# HPT report

- Reliability score: 88.97% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown