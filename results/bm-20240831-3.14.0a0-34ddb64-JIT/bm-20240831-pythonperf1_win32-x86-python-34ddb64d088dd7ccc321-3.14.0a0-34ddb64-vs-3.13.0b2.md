# Results vs. 3.13.0b2

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: windows-x86
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.04x faster
- HPT reliability: 96.60%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 263 ms: 1.13x slower                                                           |
| docutils       | 1.81 sec                                                            | 2.00 sec: 1.10x slower                                                         |
| html5lib       | 45.4 ms                                                             | 47.5 ms: 1.04x slower                                                          |
| tornado_http   | 94.3 ms                                                             | 108 ms: 1.15x slower                                                           |
| Geometric mean | (ref)                                                               | 1.11x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none            | 228 ms                                                              | 215 ms: 1.06x faster                                                           |
| async_tree_io_tg           | 529 ms                                                              | 515 ms: 1.03x faster                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 464 ms: 1.04x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.01x faster                                                                   |

Benchmark hidden because not significant (5): async_tree_memoization_tg, async_tree_memoization, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 47.8 ms: 1.61x faster                                                          |
| float          | 52.4 ms                                                             | 43.9 ms: 1.19x faster                                                          |
| pidigits       | 199 ms                                                              | 195 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                               | 1.25x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 99.9 ms                                                             | 102 ms: 1.02x slower                                                           |
| regex_dna      | 118 ms                                                              | 122 ms: 1.03x slower                                                           |
| regex_effbot   | 1.88 ms                                                             | 1.95 ms: 1.04x slower                                                          |
| Geometric mean | (ref)                                                               | 1.02x slower                                                                   |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 1.65 sec                                                            | 1.48 sec: 1.11x faster                                                         |
| xml_etree_generate   | 59.6 ms                                                             | 54.5 ms: 1.09x faster                                                          |
| xml_etree_iterparse  | 64.2 ms                                                             | 62.5 ms: 1.03x faster                                                          |
| xml_etree_process    | 42.1 ms                                                             | 41.4 ms: 1.02x faster                                                          |
| json_loads           | 20.5 us                                                             | 20.9 us: 1.02x slower                                                          |
| pickle_pure_python   | 213 us                                                              | 233 us: 1.09x slower                                                           |
| unpickle_pure_python | 147 us                                                              | 162 us: 1.10x slower                                                           |
| Geometric mean       | (ref)                                                               | 1.00x faster                                                                   |

Benchmark hidden because not significant (2): xml_etree_parse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 24.9 ms: 1.12x slower                                                          |
| python_startup_no_site | 18.2 ms                                                             | 21.0 ms: 1.15x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.14x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 6.94 ms                                                             | 5.60 ms: 1.24x faster                                                          |
| django_template | 30.1 ms                                                             | 33.6 ms: 1.12x slower                                                          |
| genshi_text     | 20.1 ms                                                             | 24.9 ms: 1.24x slower                                                          |
| genshi_xml      | 44.3 ms                                                             | 56.4 ms: 1.28x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.09x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 788 us: 12.35x faster                                                          |
| coverage                   | 307 ms                                                              | 51.6 ms: 5.96x faster                                                          |
| nbody                      | 76.9 ms                                                             | 47.8 ms: 1.61x faster                                                          |
| deepcopy_memo              | 23.5 us                                                             | 15.0 us: 1.57x faster                                                          |
| spectral_norm              | 68.0 ms                                                             | 46.3 ms: 1.47x faster                                                          |
| mako                       | 6.94 ms                                                             | 5.60 ms: 1.24x faster                                                          |
| deepcopy                   | 280 us                                                              | 230 us: 1.21x faster                                                           |
| float                      | 52.4 ms                                                             | 43.9 ms: 1.19x faster                                                          |
| scimark_fft                | 198 ms                                                              | 168 ms: 1.18x faster                                                           |
| scimark_sor                | 81.0 ms                                                             | 69.4 ms: 1.17x faster                                                          |
| crypto_pyaes               | 55.8 ms                                                             | 48.2 ms: 1.16x faster                                                          |
| fannkuch                   | 270 ms                                                              | 237 ms: 1.14x faster                                                           |
| tomli_loads                | 1.65 sec                                                            | 1.48 sec: 1.11x faster                                                         |
| pyflate                    | 308 ms                                                              | 279 ms: 1.10x faster                                                           |
| xml_etree_generate         | 59.6 ms                                                             | 54.5 ms: 1.09x faster                                                          |
| deltablue                  | 2.23 ms                                                             | 2.06 ms: 1.09x faster                                                          |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 2.64 ms: 1.09x faster                                                          |
| async_tree_none            | 228 ms                                                              | 215 ms: 1.06x faster                                                           |
| deepcopy_reduce            | 2.59 us                                                             | 2.51 us: 1.03x faster                                                          |
| async_tree_io_tg           | 529 ms                                                              | 515 ms: 1.03x faster                                                           |
| xml_etree_iterparse        | 64.2 ms                                                             | 62.5 ms: 1.03x faster                                                          |
| pprint_safe_repr           | 607 ms                                                              | 596 ms: 1.02x faster                                                           |
| xml_etree_process          | 42.1 ms                                                             | 41.4 ms: 1.02x faster                                                          |
| pidigits                   | 199 ms                                                              | 195 ms: 1.02x faster                                                           |
| meteor_contest             | 74.1 ms                                                             | 73.2 ms: 1.01x faster                                                          |
| comprehensions             | 11.9 us                                                             | 11.8 us: 1.01x faster                                                          |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.0 sec: 1.01x slower                                                         |
| json                       | 4.10 ms                                                             | 4.14 ms: 1.01x slower                                                          |
| go                         | 101 ms                                                              | 102 ms: 1.01x slower                                                           |
| create_gc_cycles           | 756 us                                                              | 769 us: 1.02x slower                                                           |
| regex_compile              | 99.9 ms                                                             | 102 ms: 1.02x slower                                                           |
| json_loads                 | 20.5 us                                                             | 20.9 us: 1.02x slower                                                          |
| telco                      | 6.03 ms                                                             | 6.14 ms: 1.02x slower                                                          |
| gc_traversal               | 1.43 ms                                                             | 1.46 ms: 1.02x slower                                                          |
| logging_format             | 8.13 us                                                             | 8.34 us: 1.03x slower                                                          |
| logging_silent             | 57.9 ns                                                             | 59.4 ns: 1.03x slower                                                          |
| bench_thread_pool          | 985 us                                                              | 1.01 ms: 1.03x slower                                                          |
| logging_simple             | 7.47 us                                                             | 7.71 us: 1.03x slower                                                          |
| regex_dna                  | 118 ms                                                              | 122 ms: 1.03x slower                                                           |
| regex_effbot               | 1.88 ms                                                             | 1.95 ms: 1.04x slower                                                          |
| pathlib                    | 83.9 ms                                                             | 86.8 ms: 1.04x slower                                                          |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 464 ms: 1.04x slower                                                           |
| asyncio_tcp                | 662 ms                                                              | 687 ms: 1.04x slower                                                           |
| richards                   | 31.2 ms                                                             | 32.4 ms: 1.04x slower                                                          |
| html5lib                   | 45.4 ms                                                             | 47.5 ms: 1.04x slower                                                          |
| pycparser                  | 777 ms                                                              | 819 ms: 1.05x slower                                                           |
| sympy_str                  | 211 ms                                                              | 223 ms: 1.06x slower                                                           |
| typing_runtime_protocols   | 136 us                                                              | 144 us: 1.06x slower                                                           |
| sympy_expand               | 375 ms                                                              | 398 ms: 1.06x slower                                                           |
| sqlglot_parse              | 964 us                                                              | 1.04 ms: 1.08x slower                                                          |
| mdp                        | 1.60 sec                                                            | 1.73 sec: 1.08x slower                                                         |
| sympy_sum                  | 105 ms                                                              | 114 ms: 1.09x slower                                                           |
| pickle_pure_python         | 213 us                                                              | 233 us: 1.09x slower                                                           |
| unpickle_pure_python       | 147 us                                                              | 162 us: 1.10x slower                                                           |
| scimark_monte_carlo        | 45.2 ms                                                             | 49.8 ms: 1.10x slower                                                          |
| docutils                   | 1.81 sec                                                            | 2.00 sec: 1.10x slower                                                         |
| chaos                      | 48.0 ms                                                             | 53.6 ms: 1.12x slower                                                          |
| django_template            | 30.1 ms                                                             | 33.6 ms: 1.12x slower                                                          |
| python_startup             | 22.2 ms                                                             | 24.9 ms: 1.12x slower                                                          |
| sqlglot_transpile          | 1.19 ms                                                             | 1.34 ms: 1.13x slower                                                          |
| sqlglot_normalize          | 206 ms                                                              | 232 ms: 1.13x slower                                                           |
| 2to3                       | 233 ms                                                              | 263 ms: 1.13x slower                                                           |
| nqueens                    | 68.7 ms                                                             | 78.3 ms: 1.14x slower                                                          |
| sympy_integrate            | 14.6 ms                                                             | 16.8 ms: 1.14x slower                                                          |
| tornado_http               | 94.3 ms                                                             | 108 ms: 1.15x slower                                                           |
| python_startup_no_site     | 18.2 ms                                                             | 21.0 ms: 1.15x slower                                                          |
| coroutines                 | 15.5 ms                                                             | 17.9 ms: 1.16x slower                                                          |
| sqlglot_optimize           | 39.7 ms                                                             | 45.9 ms: 1.16x slower                                                          |
| generators                 | 21.2 ms                                                             | 24.5 ms: 1.16x slower                                                          |
| hexiom                     | 4.23 ms                                                             | 4.91 ms: 1.16x slower                                                          |
| async_generators           | 266 ms                                                              | 309 ms: 1.16x slower                                                           |
| bench_mp_pool              | 69.4 ms                                                             | 82.7 ms: 1.19x slower                                                          |
| genshi_text                | 20.1 ms                                                             | 24.9 ms: 1.24x slower                                                          |
| pylint                     | 217 ms                                                              | 269 ms: 1.24x slower                                                           |
| genshi_xml                 | 44.3 ms                                                             | 56.4 ms: 1.28x slower                                                          |
| raytrace                   | 189 ms                                                              | 245 ms: 1.30x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.04x faster                                                                   |

Benchmark hidden because not significant (11): async_tree_memoization_tg, async_tree_memoization, async_tree_none_tg, pprint_pformat, xml_etree_parse, richards_super, async_tree_cpu_io_mixed, json_dumps, scimark_lu, regex_v8, async_tree_io
Ignored benchmarks (8) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json: dulwich_log

# HPT report

- Reliability score: 96.60% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown