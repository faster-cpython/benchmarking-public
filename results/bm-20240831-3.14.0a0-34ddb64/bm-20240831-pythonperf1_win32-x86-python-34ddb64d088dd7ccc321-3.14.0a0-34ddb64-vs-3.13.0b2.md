# Results vs. 3.13.0b2

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: windows-x86
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 250 ms: 1.07x slower                                                           |
| docutils       | 1.81 sec                                                            | 1.85 sec: 1.02x slower                                                         |
| html5lib       | 45.4 ms                                                             | 45.1 ms: 1.01x faster                                                          |
| tornado_http   | 94.3 ms                                                             | 105 ms: 1.12x slower                                                           |
| Geometric mean | (ref)                                                               | 1.05x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none            | 228 ms                                                              | 221 ms: 1.03x faster                                                           |
| async_tree_io_tg           | 529 ms                                                              | 518 ms: 1.02x faster                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 464 ms: 1.04x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.00x faster                                                                   |

Benchmark hidden because not significant (5): async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 199 ms                                                              | 200 ms: 1.01x slower                                                           |
| float          | 52.4 ms                                                             | 60.6 ms: 1.16x slower                                                          |
| nbody          | 76.9 ms                                                             | 96.5 ms: 1.25x slower                                                          |
| Geometric mean | (ref)                                                               | 1.14x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 15.7 ms                                                             | 16.2 ms: 1.03x slower                                                          |
| regex_effbot   | 1.88 ms                                                             | 2.00 ms: 1.06x slower                                                          |
| regex_compile  | 99.9 ms                                                             | 107 ms: 1.07x slower                                                           |
| regex_dna      | 118 ms                                                              | 127 ms: 1.08x slower                                                           |
| Geometric mean | (ref)                                                               | 1.06x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_loads           | 20.5 us                                                             | 20.4 us: 1.01x faster                                                          |
| xml_etree_parse      | 104 ms                                                              | 109 ms: 1.04x slower                                                           |
| json_dumps           | 6.84 ms                                                             | 7.21 ms: 1.05x slower                                                          |
| xml_etree_iterparse  | 64.2 ms                                                             | 68.5 ms: 1.07x slower                                                          |
| tomli_loads          | 1.65 sec                                                            | 1.90 sec: 1.15x slower                                                         |
| xml_etree_generate   | 59.6 ms                                                             | 69.1 ms: 1.16x slower                                                          |
| pickle_pure_python   | 213 us                                                              | 254 us: 1.19x slower                                                           |
| unpickle_pure_python | 147 us                                                              | 176 us: 1.19x slower                                                           |
| xml_etree_process    | 42.1 ms                                                             | 50.8 ms: 1.21x slower                                                          |
| Geometric mean       | (ref)                                                               | 1.12x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 24.1 ms: 1.08x slower                                                          |
| python_startup_no_site | 18.2 ms                                                             | 19.9 ms: 1.09x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.09x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 44.3 ms                                                             | 46.4 ms: 1.05x slower                                                          |
| genshi_text     | 20.1 ms                                                             | 21.2 ms: 1.06x slower                                                          |
| django_template | 30.1 ms                                                             | 33.3 ms: 1.11x slower                                                          |
| mako            | 6.94 ms                                                             | 8.10 ms: 1.17x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.09x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 738 us: 13.19x faster                                                          |
| coverage                   | 307 ms                                                              | 52.5 ms: 5.85x faster                                                          |
| deepcopy                   | 280 us                                                              | 243 us: 1.15x faster                                                           |
| deepcopy_memo              | 23.5 us                                                             | 21.6 us: 1.09x faster                                                          |
| deepcopy_reduce            | 2.59 us                                                             | 2.50 us: 1.03x faster                                                          |
| async_tree_none            | 228 ms                                                              | 221 ms: 1.03x faster                                                           |
| async_tree_io_tg           | 529 ms                                                              | 518 ms: 1.02x faster                                                           |
| create_gc_cycles           | 756 us                                                              | 741 us: 1.02x faster                                                           |
| html5lib                   | 45.4 ms                                                             | 45.1 ms: 1.01x faster                                                          |
| gc_traversal               | 1.43 ms                                                             | 1.42 ms: 1.01x faster                                                          |
| json_loads                 | 20.5 us                                                             | 20.4 us: 1.01x faster                                                          |
| pidigits                   | 199 ms                                                              | 200 ms: 1.01x slower                                                           |
| sympy_str                  | 211 ms                                                              | 214 ms: 1.01x slower                                                           |
| sympy_sum                  | 105 ms                                                              | 107 ms: 1.02x slower                                                           |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.2 sec: 1.02x slower                                                         |
| json                       | 4.10 ms                                                             | 4.18 ms: 1.02x slower                                                          |
| docutils                   | 1.81 sec                                                            | 1.85 sec: 1.02x slower                                                         |
| go                         | 101 ms                                                              | 103 ms: 1.03x slower                                                           |
| regex_v8                   | 15.7 ms                                                             | 16.2 ms: 1.03x slower                                                          |
| crypto_pyaes               | 55.8 ms                                                             | 57.8 ms: 1.04x slower                                                          |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 464 ms: 1.04x slower                                                           |
| pathlib                    | 83.9 ms                                                             | 87.2 ms: 1.04x slower                                                          |
| xml_etree_parse            | 104 ms                                                              | 109 ms: 1.04x slower                                                           |
| sympy_integrate            | 14.6 ms                                                             | 15.3 ms: 1.04x slower                                                          |
| genshi_xml                 | 44.3 ms                                                             | 46.4 ms: 1.05x slower                                                          |
| json_dumps                 | 6.84 ms                                                             | 7.21 ms: 1.05x slower                                                          |
| logging_format             | 8.13 us                                                             | 8.58 us: 1.05x slower                                                          |
| genshi_text                | 20.1 ms                                                             | 21.2 ms: 1.06x slower                                                          |
| bench_mp_pool              | 69.4 ms                                                             | 73.5 ms: 1.06x slower                                                          |
| regex_effbot               | 1.88 ms                                                             | 2.00 ms: 1.06x slower                                                          |
| pprint_safe_repr           | 607 ms                                                              | 645 ms: 1.06x slower                                                           |
| typing_runtime_protocols   | 136 us                                                              | 144 us: 1.06x slower                                                           |
| logging_simple             | 7.47 us                                                             | 7.94 us: 1.06x slower                                                          |
| regex_compile              | 99.9 ms                                                             | 107 ms: 1.07x slower                                                           |
| xml_etree_iterparse        | 64.2 ms                                                             | 68.5 ms: 1.07x slower                                                          |
| pprint_pformat             | 1.24 sec                                                            | 1.33 sec: 1.07x slower                                                         |
| 2to3                       | 233 ms                                                              | 250 ms: 1.07x slower                                                           |
| mdp                        | 1.60 sec                                                            | 1.72 sec: 1.07x slower                                                         |
| regex_dna                  | 118 ms                                                              | 127 ms: 1.08x slower                                                           |
| python_startup             | 22.2 ms                                                             | 24.1 ms: 1.08x slower                                                          |
| python_startup_no_site     | 18.2 ms                                                             | 19.9 ms: 1.09x slower                                                          |
| meteor_contest             | 74.1 ms                                                             | 81.3 ms: 1.10x slower                                                          |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 3.17 ms: 1.10x slower                                                          |
| pylint                     | 217 ms                                                              | 239 ms: 1.10x slower                                                           |
| asyncio_tcp                | 662 ms                                                              | 731 ms: 1.10x slower                                                           |
| django_template            | 30.1 ms                                                             | 33.3 ms: 1.11x slower                                                          |
| sqlglot_transpile          | 1.19 ms                                                             | 1.32 ms: 1.11x slower                                                          |
| bench_thread_pool          | 985 us                                                              | 1.09 ms: 1.11x slower                                                          |
| spectral_norm              | 68.0 ms                                                             | 75.5 ms: 1.11x slower                                                          |
| pycparser                  | 777 ms                                                              | 864 ms: 1.11x slower                                                           |
| sqlglot_optimize           | 39.7 ms                                                             | 44.2 ms: 1.11x slower                                                          |
| sqlglot_normalize          | 206 ms                                                              | 229 ms: 1.11x slower                                                           |
| tornado_http               | 94.3 ms                                                             | 105 ms: 1.12x slower                                                           |
| sqlglot_parse              | 964 us                                                              | 1.08 ms: 1.12x slower                                                          |
| telco                      | 6.03 ms                                                             | 6.78 ms: 1.12x slower                                                          |
| coroutines                 | 15.5 ms                                                             | 17.4 ms: 1.13x slower                                                          |
| async_generators           | 266 ms                                                              | 300 ms: 1.13x slower                                                           |
| chaos                      | 48.0 ms                                                             | 54.6 ms: 1.14x slower                                                          |
| nqueens                    | 68.7 ms                                                             | 79.0 ms: 1.15x slower                                                          |
| comprehensions             | 11.9 us                                                             | 13.6 us: 1.15x slower                                                          |
| tomli_loads                | 1.65 sec                                                            | 1.90 sec: 1.15x slower                                                         |
| float                      | 52.4 ms                                                             | 60.6 ms: 1.16x slower                                                          |
| xml_etree_generate         | 59.6 ms                                                             | 69.1 ms: 1.16x slower                                                          |
| pyflate                    | 308 ms                                                              | 358 ms: 1.16x slower                                                           |
| scimark_fft                | 198 ms                                                              | 231 ms: 1.17x slower                                                           |
| mako                       | 6.94 ms                                                             | 8.10 ms: 1.17x slower                                                          |
| scimark_lu                 | 59.4 ms                                                             | 70.3 ms: 1.18x slower                                                          |
| pickle_pure_python         | 213 us                                                              | 254 us: 1.19x slower                                                           |
| unpickle_pure_python       | 147 us                                                              | 176 us: 1.19x slower                                                           |
| raytrace                   | 189 ms                                                              | 227 ms: 1.20x slower                                                           |
| xml_etree_process          | 42.1 ms                                                             | 50.8 ms: 1.21x slower                                                          |
| deltablue                  | 2.23 ms                                                             | 2.70 ms: 1.21x slower                                                          |
| scimark_sor                | 81.0 ms                                                             | 98.2 ms: 1.21x slower                                                          |
| fannkuch                   | 270 ms                                                              | 332 ms: 1.23x slower                                                           |
| scimark_monte_carlo        | 45.2 ms                                                             | 55.8 ms: 1.24x slower                                                          |
| richards_super             | 35.5 ms                                                             | 44.3 ms: 1.25x slower                                                          |
| hexiom                     | 4.23 ms                                                             | 5.29 ms: 1.25x slower                                                          |
| nbody                      | 76.9 ms                                                             | 96.5 ms: 1.25x slower                                                          |
| logging_silent             | 57.9 ns                                                             | 72.8 ns: 1.26x slower                                                          |
| generators                 | 21.2 ms                                                             | 26.7 ms: 1.26x slower                                                          |
| richards                   | 31.2 ms                                                             | 39.8 ms: 1.27x slower                                                          |
| Geometric mean             | (ref)                                                               | 1.03x slower                                                                   |

Benchmark hidden because not significant (6): async_tree_none_tg, async_tree_memoization_tg, sympy_expand, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_io
Ignored benchmarks (8) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json: dulwich_log

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown