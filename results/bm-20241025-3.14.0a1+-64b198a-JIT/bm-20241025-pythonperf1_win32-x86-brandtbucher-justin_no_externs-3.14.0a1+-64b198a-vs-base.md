# Results vs. base

- fork: brandtbucher
- ref: justin_no_externs
- machine: windows-x86
- commit hash: 64b198a
- commit date: 2024-10-25
- overall geometric mean: 1.018x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241022-pythonperf1_win32-x86-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                                          | 270 ms: 1.02x slower                                                               |
| docutils       | 2.04 sec                                                                        | 2.08 sec: 1.02x slower                                                             |
| sphinx         | 842 ms                                                                          | 860 ms: 1.02x slower                                                               |
| Geometric mean | (ref)                                                                           | 1.01x slower                                                                       |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241022-pythonperf1_win32-x86-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|------------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| coroutines       | 17.8 ms                                                                         | 17.3 ms: 1.03x faster                                                              |
| async_generators | 310 ms                                                                          | 332 ms: 1.07x slower                                                               |
| Geometric mean   | (ref)                                                                           | 1.01x slower                                                                       |

Benchmark hidden because not significant (8): async_tree_memoization_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241022-pythonperf1_win32-x86-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| pidigits       | 205 ms                                                                          | 203 ms: 1.01x faster                                                               |
| nbody          | 63.7 ms                                                                         | 63.0 ms: 1.01x faster                                                              |
| float          | 45.9 ms                                                                         | 49.6 ms: 1.08x slower                                                              |
| Geometric mean | (ref)                                                                           | 1.02x slower                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241022-pythonperf1_win32-x86-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_effbot   | 1.81 ms                                                                         | 1.77 ms: 1.02x faster                                                              |
| regex_dna      | 118 ms                                                                          | 120 ms: 1.02x slower                                                               |
| regex_v8       | 15.6 ms                                                                         | 15.9 ms: 1.02x slower                                                              |
| regex_compile  | 105 ms                                                                          | 110 ms: 1.05x slower                                                               |
| Geometric mean | (ref)                                                                           | 1.02x slower                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241022-pythonperf1_win32-x86-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| json_dumps           | 8.11 ms                                                                         | 7.99 ms: 1.01x faster                                                              |
| pickle_pure_python   | 243 us                                                                          | 245 us: 1.01x slower                                                               |
| xml_etree_parse      | 110 ms                                                                          | 111 ms: 1.01x slower                                                               |
| json_loads           | 20.6 us                                                                         | 21.2 us: 1.03x slower                                                              |
| tomli_loads          | 1.54 sec                                                                        | 1.59 sec: 1.03x slower                                                             |
| xml_etree_generate   | 55.5 ms                                                                         | 58.2 ms: 1.05x slower                                                              |
| unpickle_pure_python | 160 us                                                                          | 169 us: 1.05x slower                                                               |
| xml_etree_iterparse  | 64.1 ms                                                                         | 67.7 ms: 1.06x slower                                                              |
| xml_etree_process    | 40.7 ms                                                                         | 45.4 ms: 1.12x slower                                                              |
| Geometric mean       | (ref)                                                                           | 1.04x slower                                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241022-pythonperf1_win32-x86-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|------------------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup_no_site | 20.2 ms                                                                         | 20.3 ms: 1.01x slower                                                              |
| Geometric mean         | (ref)                                                                           | 1.00x slower                                                                       |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241022-pythonperf1_win32-x86-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| genshi_text    | 23.5 ms                                                                         | 23.2 ms: 1.01x faster                                                              |
| genshi_xml     | 54.0 ms                                                                         | 55.0 ms: 1.02x slower                                                              |
| mako           | 5.77 ms                                                                         | 6.44 ms: 1.12x slower                                                              |
| Geometric mean | (ref)                                                                           | 1.03x slower                                                                       |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20241022-pythonperf1_win32-x86-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|--------------------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| sqlglot_normalize        | 238 ms                                                                          | 105 ms: 2.26x faster                                                               |
| raytrace                 | 265 ms                                                                          | 256 ms: 1.03x faster                                                               |
| richards_super           | 42.4 ms                                                                         | 41.0 ms: 1.03x faster                                                              |
| richards                 | 36.9 ms                                                                         | 35.9 ms: 1.03x faster                                                              |
| coroutines               | 17.8 ms                                                                         | 17.3 ms: 1.03x faster                                                              |
| regex_effbot             | 1.81 ms                                                                         | 1.77 ms: 1.02x faster                                                              |
| json_dumps               | 8.11 ms                                                                         | 7.99 ms: 1.01x faster                                                              |
| pidigits                 | 205 ms                                                                          | 203 ms: 1.01x faster                                                               |
| telco                    | 6.08 ms                                                                         | 6.01 ms: 1.01x faster                                                              |
| thrift                   | 775 us                                                                          | 766 us: 1.01x faster                                                               |
| nbody                    | 63.7 ms                                                                         | 63.0 ms: 1.01x faster                                                              |
| genshi_text              | 23.5 ms                                                                         | 23.2 ms: 1.01x faster                                                              |
| pathlib                  | 88.4 ms                                                                         | 87.8 ms: 1.01x faster                                                              |
| mdp                      | 1.75 sec                                                                        | 1.76 sec: 1.01x slower                                                             |
| python_startup_no_site   | 20.2 ms                                                                         | 20.3 ms: 1.01x slower                                                              |
| pickle_pure_python       | 243 us                                                                          | 245 us: 1.01x slower                                                               |
| dulwich_log              | 49.7 ms                                                                         | 50.2 ms: 1.01x slower                                                              |
| xml_etree_parse          | 110 ms                                                                          | 111 ms: 1.01x slower                                                               |
| sqlglot_transpile        | 1.35 ms                                                                         | 1.36 ms: 1.01x slower                                                              |
| regex_dna                | 118 ms                                                                          | 120 ms: 1.02x slower                                                               |
| 2to3                     | 265 ms                                                                          | 270 ms: 1.02x slower                                                               |
| chaos                    | 54.8 ms                                                                         | 55.8 ms: 1.02x slower                                                              |
| genshi_xml               | 54.0 ms                                                                         | 55.0 ms: 1.02x slower                                                              |
| regex_v8                 | 15.6 ms                                                                         | 15.9 ms: 1.02x slower                                                              |
| docutils                 | 2.04 sec                                                                        | 2.08 sec: 1.02x slower                                                             |
| sympy_expand             | 397 ms                                                                          | 406 ms: 1.02x slower                                                               |
| sphinx                   | 842 ms                                                                          | 860 ms: 1.02x slower                                                               |
| meteor_contest           | 71.9 ms                                                                         | 73.6 ms: 1.02x slower                                                              |
| sympy_str                | 230 ms                                                                          | 236 ms: 1.02x slower                                                               |
| sqlglot_optimize         | 49.4 ms                                                                         | 50.8 ms: 1.03x slower                                                              |
| json_loads               | 20.6 us                                                                         | 21.2 us: 1.03x slower                                                              |
| pycparser                | 821 ms                                                                          | 845 ms: 1.03x slower                                                               |
| go                       | 97.7 ms                                                                         | 101 ms: 1.03x slower                                                               |
| deepcopy                 | 237 us                                                                          | 245 us: 1.03x slower                                                               |
| tomli_loads              | 1.54 sec                                                                        | 1.59 sec: 1.03x slower                                                             |
| deepcopy_reduce          | 2.44 us                                                                         | 2.53 us: 1.04x slower                                                              |
| sympy_integrate          | 17.2 ms                                                                         | 18.0 ms: 1.04x slower                                                              |
| logging_simple           | 7.46 us                                                                         | 7.78 us: 1.04x slower                                                              |
| typing_runtime_protocols | 137 us                                                                          | 143 us: 1.04x slower                                                               |
| pprint_pformat           | 1.18 sec                                                                        | 1.23 sec: 1.04x slower                                                             |
| fannkuch                 | 245 ms                                                                          | 256 ms: 1.05x slower                                                               |
| pyflate                  | 315 ms                                                                          | 330 ms: 1.05x slower                                                               |
| pprint_safe_repr         | 575 ms                                                                          | 603 ms: 1.05x slower                                                               |
| logging_format           | 8.06 us                                                                         | 8.45 us: 1.05x slower                                                              |
| xml_etree_generate       | 55.5 ms                                                                         | 58.2 ms: 1.05x slower                                                              |
| regex_compile            | 105 ms                                                                          | 110 ms: 1.05x slower                                                               |
| unpickle_pure_python     | 160 us                                                                          | 169 us: 1.05x slower                                                               |
| generators               | 24.2 ms                                                                         | 25.5 ms: 1.06x slower                                                              |
| xml_etree_iterparse      | 64.1 ms                                                                         | 67.7 ms: 1.06x slower                                                              |
| deltablue                | 2.57 ms                                                                         | 2.73 ms: 1.06x slower                                                              |
| async_generators         | 310 ms                                                                          | 332 ms: 1.07x slower                                                               |
| scimark_lu               | 60.7 ms                                                                         | 65.2 ms: 1.07x slower                                                              |
| hexiom                   | 5.53 ms                                                                         | 5.94 ms: 1.07x slower                                                              |
| crypto_pyaes             | 50.1 ms                                                                         | 54.0 ms: 1.08x slower                                                              |
| comprehensions           | 13.1 us                                                                         | 14.2 us: 1.08x slower                                                              |
| float                    | 45.9 ms                                                                         | 49.6 ms: 1.08x slower                                                              |
| scimark_sparse_mat_mult  | 2.44 ms                                                                         | 2.65 ms: 1.08x slower                                                              |
| scimark_fft              | 177 ms                                                                          | 195 ms: 1.10x slower                                                               |
| deepcopy_memo            | 16.3 us                                                                         | 18.0 us: 1.11x slower                                                              |
| nqueens                  | 75.6 ms                                                                         | 83.7 ms: 1.11x slower                                                              |
| xml_etree_process        | 40.7 ms                                                                         | 45.4 ms: 1.12x slower                                                              |
| mako                     | 5.77 ms                                                                         | 6.44 ms: 1.12x slower                                                              |
| scimark_sor              | 68.1 ms                                                                         | 76.9 ms: 1.13x slower                                                              |
| spectral_norm            | 59.1 ms                                                                         | 67.5 ms: 1.14x slower                                                              |
| scimark_monte_carlo      | 39.4 ms                                                                         | 47.7 ms: 1.21x slower                                                              |
| logging_silent           | 52.6 ns                                                                         | 64.9 ns: 1.23x slower                                                              |
| Geometric mean           | (ref)                                                                           | 1.02x slower                                                                       |

Benchmark hidden because not significant (21): bench_thread_pool, async_tree_memoization_tg, json, create_gc_cycles, coverage, bench_mp_pool, python_startup, django_template, gc_traversal, tornado_http, async_tree_io, sqlglot_parse, html5lib, async_tree_io_tg, async_tree_memoization, sympy_sum, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_none, pylint

- Geometric mean (including insignificant results): 1.018x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown