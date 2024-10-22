# Results vs. 3.13.0

- fork: brandtbucher
- ref: tier_two_improvement
- machine: windows-x86
- commit hash: bbb07e8
- commit date: 2024-07-13
- overall geometric mean: 1.11x faster
- HPT reliability: 99.86%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 251 ms: 1.01x faster                                                                 |
| docutils       | 1.82 sec                                                        | 1.91 sec: 1.05x slower                                                               |
| html5lib       | 48.3 ms                                                         | 47.5 ms: 1.02x faster                                                                |
| tornado_http   | 104 ms                                                          | 97.0 ms: 1.07x faster                                                                |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| asyncio_tcp                | 842 ms                                                          | 623 ms: 1.35x faster                                                                 |
| async_tree_memoization_tg  | 287 ms                                                          | 249 ms: 1.15x faster                                                                 |
| async_tree_none_tg         | 219 ms                                                          | 194 ms: 1.13x faster                                                                 |
| async_tree_none            | 246 ms                                                          | 220 ms: 1.12x faster                                                                 |
| async_tree_memoization     | 302 ms                                                          | 272 ms: 1.11x faster                                                                 |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 16.8 sec: 1.03x faster                                                               |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 482 ms: 1.03x faster                                                                 |
| async_tree_io_tg           | 509 ms                                                          | 498 ms: 1.02x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 470 ms: 1.01x slower                                                                 |
| coroutines                 | 15.7 ms                                                         | 17.1 ms: 1.09x slower                                                                |
| async_generators           | 274 ms                                                          | 321 ms: 1.17x slower                                                                 |
| Geometric mean             | (ref)                                                           | 1.05x faster                                                                         |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 57.8 ms                                                         | 43.0 ms: 1.34x faster                                                                |
| nbody          | 81.9 ms                                                         | 61.2 ms: 1.34x faster                                                                |
| pidigits       | 202 ms                                                          | 196 ms: 1.03x faster                                                                 |
| Geometric mean | (ref)                                                           | 1.23x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                          | 94.4 ms: 1.09x faster                                                                |
| regex_v8       | 15.6 ms                                                         | 15.7 ms: 1.01x slower                                                                |
| regex_dna      | 117 ms                                                          | 118 ms: 1.01x slower                                                                 |
| regex_effbot   | 1.81 ms                                                         | 1.89 ms: 1.05x slower                                                                |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| tomli_loads          | 1.73 sec                                                        | 1.49 sec: 1.16x faster                                                               |
| pickle_pure_python   | 238 us                                                          | 212 us: 1.12x faster                                                                 |
| unpickle_pure_python | 162 us                                                          | 146 us: 1.11x faster                                                                 |
| xml_etree_generate   | 62.6 ms                                                         | 58.1 ms: 1.08x faster                                                                |
| xml_etree_iterparse  | 65.1 ms                                                         | 62.0 ms: 1.05x faster                                                                |
| xml_etree_parse      | 109 ms                                                          | 105 ms: 1.04x faster                                                                 |
| xml_etree_process    | 45.0 ms                                                         | 43.4 ms: 1.04x faster                                                                |
| json_dumps           | 7.40 ms                                                         | 7.17 ms: 1.03x faster                                                                |
| json_loads           | 21.0 us                                                         | 21.7 us: 1.03x slower                                                                |
| Geometric mean       | (ref)                                                           | 1.06x faster                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 24.3 ms                                                         | 23.1 ms: 1.05x faster                                                                |
| python_startup_no_site | 19.9 ms                                                         | 19.3 ms: 1.03x faster                                                                |
| Geometric mean         | (ref)                                                           | 1.04x faster                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 7.31 ms                                                         | 5.39 ms: 1.36x faster                                                                |
| genshi_text     | 22.4 ms                                                         | 22.9 ms: 1.02x slower                                                                |
| django_template | 32.7 ms                                                         | 33.6 ms: 1.03x slower                                                                |
| genshi_xml      | 49.5 ms                                                         | 52.9 ms: 1.07x slower                                                                |
| Geometric mean  | (ref)                                                           | 1.05x faster                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| thrift                     | 10.1 ms                                                         | 760 us: 13.36x faster                                                                |
| coverage                   | 333 ms                                                          | 51.9 ms: 6.41x faster                                                                |
| deepcopy_memo              | 26.2 us                                                         | 15.8 us: 1.65x faster                                                                |
| spectral_norm              | 71.3 ms                                                         | 48.7 ms: 1.46x faster                                                                |
| mako                       | 7.31 ms                                                         | 5.39 ms: 1.36x faster                                                                |
| asyncio_tcp                | 842 ms                                                          | 623 ms: 1.35x faster                                                                 |
| float                      | 57.8 ms                                                         | 43.0 ms: 1.34x faster                                                                |
| nbody                      | 81.9 ms                                                         | 61.2 ms: 1.34x faster                                                                |
| fannkuch                   | 293 ms                                                          | 225 ms: 1.30x faster                                                                 |
| deepcopy                   | 307 us                                                          | 240 us: 1.28x faster                                                                 |
| scimark_fft                | 206 ms                                                          | 166 ms: 1.25x faster                                                                 |
| crypto_pyaes               | 58.2 ms                                                         | 46.8 ms: 1.24x faster                                                                |
| pyflate                    | 326 ms                                                          | 263 ms: 1.24x faster                                                                 |
| scimark_sparse_mat_mult    | 2.90 ms                                                         | 2.37 ms: 1.23x faster                                                                |
| telco                      | 6.67 ms                                                         | 5.60 ms: 1.19x faster                                                                |
| deepcopy_reduce            | 2.85 us                                                         | 2.42 us: 1.18x faster                                                                |
| scimark_monte_carlo        | 50.3 ms                                                         | 42.8 ms: 1.17x faster                                                                |
| tomli_loads                | 1.73 sec                                                        | 1.49 sec: 1.16x faster                                                               |
| async_tree_memoization_tg  | 287 ms                                                          | 249 ms: 1.15x faster                                                                 |
| pprint_safe_repr           | 644 ms                                                          | 563 ms: 1.14x faster                                                                 |
| comprehensions             | 12.7 us                                                         | 11.2 us: 1.14x faster                                                                |
| async_tree_none_tg         | 219 ms                                                          | 194 ms: 1.13x faster                                                                 |
| pickle_pure_python         | 238 us                                                          | 212 us: 1.12x faster                                                                 |
| async_tree_none            | 246 ms                                                          | 220 ms: 1.12x faster                                                                 |
| pprint_pformat             | 1.30 sec                                                        | 1.16 sec: 1.12x faster                                                               |
| sqlglot_parse              | 1.05 ms                                                         | 942 us: 1.11x faster                                                                 |
| async_tree_memoization     | 302 ms                                                          | 272 ms: 1.11x faster                                                                 |
| unpickle_pure_python       | 162 us                                                          | 146 us: 1.11x faster                                                                 |
| meteor_contest             | 77.0 ms                                                         | 70.1 ms: 1.10x faster                                                                |
| regex_compile              | 103 ms                                                          | 94.4 ms: 1.09x faster                                                                |
| xml_etree_generate         | 62.6 ms                                                         | 58.1 ms: 1.08x faster                                                                |
| pathlib                    | 89.4 ms                                                         | 83.2 ms: 1.07x faster                                                                |
| tornado_http               | 104 ms                                                          | 97.0 ms: 1.07x faster                                                                |
| logging_silent             | 61.6 ns                                                         | 57.4 ns: 1.07x faster                                                                |
| sqlglot_transpile          | 1.29 ms                                                         | 1.21 ms: 1.07x faster                                                                |
| logging_format             | 8.57 us                                                         | 8.06 us: 1.06x faster                                                                |
| logging_simple             | 7.87 us                                                         | 7.44 us: 1.06x faster                                                                |
| pycparser                  | 869 ms                                                          | 826 ms: 1.05x faster                                                                 |
| xml_etree_iterparse        | 65.1 ms                                                         | 62.0 ms: 1.05x faster                                                                |
| python_startup             | 24.3 ms                                                         | 23.1 ms: 1.05x faster                                                                |
| bench_thread_pool          | 1.02 ms                                                         | 980 us: 1.04x faster                                                                 |
| xml_etree_parse            | 109 ms                                                          | 105 ms: 1.04x faster                                                                 |
| xml_etree_process          | 45.0 ms                                                         | 43.4 ms: 1.04x faster                                                                |
| python_startup_no_site     | 19.9 ms                                                         | 19.3 ms: 1.03x faster                                                                |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 16.8 sec: 1.03x faster                                                               |
| pidigits                   | 202 ms                                                          | 196 ms: 1.03x faster                                                                 |
| json_dumps                 | 7.40 ms                                                         | 7.17 ms: 1.03x faster                                                                |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 482 ms: 1.03x faster                                                                 |
| async_tree_io_tg           | 509 ms                                                          | 498 ms: 1.02x faster                                                                 |
| mdp                        | 1.67 sec                                                        | 1.64 sec: 1.02x faster                                                               |
| nqueens                    | 75.1 ms                                                         | 73.7 ms: 1.02x faster                                                                |
| html5lib                   | 48.3 ms                                                         | 47.5 ms: 1.02x faster                                                                |
| bench_mp_pool              | 74.3 ms                                                         | 73.4 ms: 1.01x faster                                                                |
| 2to3                       | 253 ms                                                          | 251 ms: 1.01x faster                                                                 |
| gc_traversal               | 1.45 ms                                                         | 1.46 ms: 1.01x slower                                                                |
| richards_super             | 38.0 ms                                                         | 38.2 ms: 1.01x slower                                                                |
| regex_v8                   | 15.6 ms                                                         | 15.7 ms: 1.01x slower                                                                |
| hexiom                     | 4.64 ms                                                         | 4.68 ms: 1.01x slower                                                                |
| regex_dna                  | 117 ms                                                          | 118 ms: 1.01x slower                                                                 |
| sympy_expand               | 375 ms                                                          | 379 ms: 1.01x slower                                                                 |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 470 ms: 1.01x slower                                                                 |
| go                         | 111 ms                                                          | 113 ms: 1.01x slower                                                                 |
| sqlglot_optimize           | 42.5 ms                                                         | 43.1 ms: 1.02x slower                                                                |
| genshi_text                | 22.4 ms                                                         | 22.9 ms: 1.02x slower                                                                |
| django_template            | 32.7 ms                                                         | 33.6 ms: 1.03x slower                                                                |
| json_loads                 | 21.0 us                                                         | 21.7 us: 1.03x slower                                                                |
| chaos                      | 51.2 ms                                                         | 53.3 ms: 1.04x slower                                                                |
| regex_effbot               | 1.81 ms                                                         | 1.89 ms: 1.05x slower                                                                |
| sympy_integrate            | 15.2 ms                                                         | 15.9 ms: 1.05x slower                                                                |
| docutils                   | 1.82 sec                                                        | 1.91 sec: 1.05x slower                                                               |
| sqlglot_normalize          | 220 ms                                                          | 232 ms: 1.06x slower                                                                 |
| typing_runtime_protocols   | 136 us                                                          | 144 us: 1.06x slower                                                                 |
| create_gc_cycles           | 713 us                                                          | 755 us: 1.06x slower                                                                 |
| pylint                     | 225 ms                                                          | 240 ms: 1.07x slower                                                                 |
| genshi_xml                 | 49.5 ms                                                         | 52.9 ms: 1.07x slower                                                                |
| scimark_sor                | 91.8 ms                                                         | 99.9 ms: 1.09x slower                                                                |
| coroutines                 | 15.7 ms                                                         | 17.1 ms: 1.09x slower                                                                |
| deltablue                  | 2.41 ms                                                         | 2.67 ms: 1.11x slower                                                                |
| raytrace                   | 205 ms                                                          | 229 ms: 1.12x slower                                                                 |
| generators                 | 22.1 ms                                                         | 25.5 ms: 1.15x slower                                                                |
| async_generators           | 274 ms                                                          | 321 ms: 1.17x slower                                                                 |
| scimark_lu                 | 63.5 ms                                                         | 80.4 ms: 1.26x slower                                                                |
| Geometric mean             | (ref)                                                           | 1.11x faster                                                                         |

Benchmark hidden because not significant (5): async_tree_io, sympy_str, sympy_sum, richards, json
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, dulwich_log, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.86% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown