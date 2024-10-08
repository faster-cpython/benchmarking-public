# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0rc1
- machine: windows-x86
- commit hash: e4a3e78
- commit date: 2024-07-31
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 244 ms: 1.04x slower                                                  |
| chameleon      | 5.71 ms                                                             | 5.80 ms: 1.01x slower                                                 |
| docutils       | 1.81 sec                                                            | 1.88 sec: 1.04x slower                                                |
| html5lib       | 45.4 ms                                                             | 47.2 ms: 1.04x slower                                                 |
| tornado_http   | 94.3 ms                                                             | 104 ms: 1.11x slower                                                  |
| Geometric mean | (ref)                                                               | 1.05x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 456 ms: 1.02x slower                                                  |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 485 ms: 1.03x slower                                                  |
| async_tree_io_tg           | 529 ms                                                              | 549 ms: 1.04x slower                                                  |
| async_tree_io              | 530 ms                                                              | 550 ms: 1.04x slower                                                  |
| async_tree_none            | 228 ms                                                              | 237 ms: 1.04x slower                                                  |
| async_tree_memoization_tg  | 254 ms                                                              | 266 ms: 1.05x slower                                                  |
| async_tree_none_tg         | 203 ms                                                              | 213 ms: 1.05x slower                                                  |
| async_tree_memoization     | 275 ms                                                              | 290 ms: 1.06x slower                                                  |
| Geometric mean             | (ref)                                                               | 1.04x slower                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 199 ms                                                              | 198 ms: 1.00x faster                                                  |
| float          | 52.4 ms                                                             | 54.2 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                               | 1.01x slower                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 99.9 ms                                                             | 99.2 ms: 1.01x faster                                                 |
| regex_effbot   | 1.88 ms                                                             | 1.90 ms: 1.01x slower                                                 |
| regex_v8       | 15.7 ms                                                             | 16.1 ms: 1.02x slower                                                 |
| regex_dna      | 118 ms                                                              | 123 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                               | 1.02x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 147 us                                                              | 148 us: 1.01x slower                                                  |
| xml_etree_generate   | 59.6 ms                                                             | 60.5 ms: 1.02x slower                                                 |
| xml_etree_process    | 42.1 ms                                                             | 42.8 ms: 1.02x slower                                                 |
| json_loads           | 20.5 us                                                             | 21.0 us: 1.02x slower                                                 |
| tomli_loads          | 1.65 sec                                                            | 1.68 sec: 1.02x slower                                                |
| xml_etree_iterparse  | 64.2 ms                                                             | 65.7 ms: 1.02x slower                                                 |
| pickle_pure_python   | 213 us                                                              | 226 us: 1.06x slower                                                  |
| json_dumps           | 6.84 ms                                                             | 7.61 ms: 1.11x slower                                                 |
| Geometric mean       | (ref)                                                               | 1.03x slower                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 18.2 ms                                                             | 19.3 ms: 1.06x slower                                                 |
| python_startup         | 22.2 ms                                                             | 23.7 ms: 1.07x slower                                                 |
| Geometric mean         | (ref)                                                               | 1.06x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|-----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 20.1 ms                                                             | 20.4 ms: 1.01x slower                                                 |
| genshi_xml      | 44.3 ms                                                             | 45.2 ms: 1.02x slower                                                 |
| django_template | 30.1 ms                                                             | 31.3 ms: 1.04x slower                                                 |
| Geometric mean  | (ref)                                                               | 1.02x slower                                                          |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nqueens                    | 68.7 ms                                                             | 67.1 ms: 1.02x faster                                                 |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 2.82 ms: 1.02x faster                                                 |
| create_gc_cycles           | 756 us                                                              | 744 us: 1.02x faster                                                  |
| sympy_expand               | 375 ms                                                              | 371 ms: 1.01x faster                                                  |
| pprint_safe_repr           | 607 ms                                                              | 602 ms: 1.01x faster                                                  |
| regex_compile              | 99.9 ms                                                             | 99.2 ms: 1.01x faster                                                 |
| pprint_pformat             | 1.24 sec                                                            | 1.23 sec: 1.00x faster                                                |
| pidigits                   | 199 ms                                                              | 198 ms: 1.00x faster                                                  |
| go                         | 101 ms                                                              | 101 ms: 1.01x slower                                                  |
| unpickle_pure_python       | 147 us                                                              | 148 us: 1.01x slower                                                  |
| chaos                      | 48.0 ms                                                             | 48.3 ms: 1.01x slower                                                 |
| regex_effbot               | 1.88 ms                                                             | 1.90 ms: 1.01x slower                                                 |
| logging_simple             | 7.47 us                                                             | 7.53 us: 1.01x slower                                                 |
| comprehensions             | 11.9 us                                                             | 12.0 us: 1.01x slower                                                 |
| coroutines                 | 15.5 ms                                                             | 15.7 ms: 1.01x slower                                                 |
| hexiom                     | 4.23 ms                                                             | 4.28 ms: 1.01x slower                                                 |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.1 sec: 1.01x slower                                                |
| chameleon                  | 5.71 ms                                                             | 5.80 ms: 1.01x slower                                                 |
| logging_format             | 8.13 us                                                             | 8.25 us: 1.01x slower                                                 |
| genshi_text                | 20.1 ms                                                             | 20.4 ms: 1.01x slower                                                 |
| xml_etree_generate         | 59.6 ms                                                             | 60.5 ms: 1.02x slower                                                 |
| xml_etree_process          | 42.1 ms                                                             | 42.8 ms: 1.02x slower                                                 |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 456 ms: 1.02x slower                                                  |
| deltablue                  | 2.23 ms                                                             | 2.27 ms: 1.02x slower                                                 |
| sympy_sum                  | 105 ms                                                              | 107 ms: 1.02x slower                                                  |
| gc_traversal               | 1.43 ms                                                             | 1.46 ms: 1.02x slower                                                 |
| sympy_integrate            | 14.6 ms                                                             | 14.9 ms: 1.02x slower                                                 |
| richards_super             | 35.5 ms                                                             | 36.1 ms: 1.02x slower                                                 |
| json_loads                 | 20.5 us                                                             | 21.0 us: 1.02x slower                                                 |
| sqlglot_normalize          | 206 ms                                                              | 211 ms: 1.02x slower                                                  |
| sqlglot_parse              | 964 us                                                              | 985 us: 1.02x slower                                                  |
| genshi_xml                 | 44.3 ms                                                             | 45.2 ms: 1.02x slower                                                 |
| tomli_loads                | 1.65 sec                                                            | 1.68 sec: 1.02x slower                                                |
| sqlglot_transpile          | 1.19 ms                                                             | 1.22 ms: 1.02x slower                                                 |
| deepcopy_memo              | 23.5 us                                                             | 24.0 us: 1.02x slower                                                 |
| json                       | 4.10 ms                                                             | 4.19 ms: 1.02x slower                                                 |
| xml_etree_iterparse        | 64.2 ms                                                             | 65.7 ms: 1.02x slower                                                 |
| raytrace                   | 189 ms                                                              | 193 ms: 1.02x slower                                                  |
| scimark_lu                 | 59.4 ms                                                             | 60.8 ms: 1.02x slower                                                 |
| regex_v8                   | 15.7 ms                                                             | 16.1 ms: 1.02x slower                                                 |
| coverage                   | 307 ms                                                              | 315 ms: 1.03x slower                                                  |
| mdp                        | 1.60 sec                                                            | 1.65 sec: 1.03x slower                                                |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 485 ms: 1.03x slower                                                  |
| richards                   | 31.2 ms                                                             | 32.2 ms: 1.03x slower                                                 |
| scimark_sor                | 81.0 ms                                                             | 83.5 ms: 1.03x slower                                                 |
| generators                 | 21.2 ms                                                             | 21.8 ms: 1.03x slower                                                 |
| scimark_fft                | 198 ms                                                              | 205 ms: 1.03x slower                                                  |
| sqlglot_optimize           | 39.7 ms                                                             | 41.0 ms: 1.03x slower                                                 |
| float                      | 52.4 ms                                                             | 54.2 ms: 1.03x slower                                                 |
| fannkuch                   | 270 ms                                                              | 280 ms: 1.04x slower                                                  |
| docutils                   | 1.81 sec                                                            | 1.88 sec: 1.04x slower                                                |
| async_tree_io_tg           | 529 ms                                                              | 549 ms: 1.04x slower                                                  |
| async_tree_io              | 530 ms                                                              | 550 ms: 1.04x slower                                                  |
| html5lib                   | 45.4 ms                                                             | 47.2 ms: 1.04x slower                                                 |
| regex_dna                  | 118 ms                                                              | 123 ms: 1.04x slower                                                  |
| django_template            | 30.1 ms                                                             | 31.3 ms: 1.04x slower                                                 |
| async_tree_none            | 228 ms                                                              | 237 ms: 1.04x slower                                                  |
| thrift                     | 9.73 ms                                                             | 10.1 ms: 1.04x slower                                                 |
| deepcopy                   | 280 us                                                              | 292 us: 1.04x slower                                                  |
| 2to3                       | 233 ms                                                              | 244 ms: 1.04x slower                                                  |
| spectral_norm              | 68.0 ms                                                             | 71.1 ms: 1.05x slower                                                 |
| async_tree_memoization_tg  | 254 ms                                                              | 266 ms: 1.05x slower                                                  |
| bench_mp_pool              | 69.4 ms                                                             | 72.8 ms: 1.05x slower                                                 |
| pycparser                  | 777 ms                                                              | 815 ms: 1.05x slower                                                  |
| async_tree_none_tg         | 203 ms                                                              | 213 ms: 1.05x slower                                                  |
| deepcopy_reduce            | 2.59 us                                                             | 2.72 us: 1.05x slower                                                 |
| scimark_monte_carlo        | 45.2 ms                                                             | 47.6 ms: 1.05x slower                                                 |
| async_generators           | 266 ms                                                              | 280 ms: 1.05x slower                                                  |
| async_tree_memoization     | 275 ms                                                              | 290 ms: 1.06x slower                                                  |
| pickle_pure_python         | 213 us                                                              | 226 us: 1.06x slower                                                  |
| typing_runtime_protocols   | 136 us                                                              | 144 us: 1.06x slower                                                  |
| python_startup_no_site     | 18.2 ms                                                             | 19.3 ms: 1.06x slower                                                 |
| pylint                     | 217 ms                                                              | 231 ms: 1.07x slower                                                  |
| python_startup             | 22.2 ms                                                             | 23.7 ms: 1.07x slower                                                 |
| pathlib                    | 83.9 ms                                                             | 89.8 ms: 1.07x slower                                                 |
| tornado_http               | 94.3 ms                                                             | 104 ms: 1.11x slower                                                  |
| json_dumps                 | 6.84 ms                                                             | 7.61 ms: 1.11x slower                                                 |
| asyncio_tcp                | 662 ms                                                              | 816 ms: 1.23x slower                                                  |
| Geometric mean             | (ref)                                                               | 1.03x slower                                                          |

Benchmark hidden because not significant (10): bench_thread_pool, crypto_pyaes, xml_etree_parse, logging_silent, meteor_contest, mako, telco, nbody, sympy_str, pyflate
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240731-3.13.0rc1-e4a3e78/bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78.json: dulwich_log

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown