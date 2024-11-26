# Results vs. base

- fork: brandtbucher
- ref: justin_no_externs
- machine: windows-x86
- commit hash: 5791853
- commit date: 2024-10-25
- overall geometric mean: 1.021x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241022-pythonperf1_win32-x86-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                                          | 267 ms: 1.01x slower                                                               |
| docutils       | 2.04 sec                                                                        | 2.05 sec: 1.01x slower                                                             |
| html5lib       | 45.7 ms                                                                         | 46.9 ms: 1.03x slower                                                              |
| sphinx         | 842 ms                                                                          | 851 ms: 1.01x slower                                                               |
| tornado_http   | 108 ms                                                                          | 110 ms: 1.02x slower                                                               |
| Geometric mean | (ref)                                                                           | 1.01x slower                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241022-pythonperf1_win32-x86-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|------------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| coroutines       | 17.8 ms                                                                         | 17.5 ms: 1.02x faster                                                              |
| async_tree_io_tg | 549 ms                                                                          | 552 ms: 1.01x slower                                                               |
| async_generators | 310 ms                                                                          | 320 ms: 1.03x slower                                                               |
| Geometric mean   | (ref)                                                                           | 1.00x faster                                                                       |

Benchmark hidden because not significant (7): async_tree_none, async_tree_memoization, async_tree_memoization_tg, async_tree_io, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241022-pythonperf1_win32-x86-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| pidigits       | 205 ms                                                                          | 207 ms: 1.01x slower                                                               |
| nbody          | 63.7 ms                                                                         | 67.2 ms: 1.05x slower                                                              |
| float          | 45.9 ms                                                                         | 49.7 ms: 1.08x slower                                                              |
| Geometric mean | (ref)                                                                           | 1.05x slower                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241022-pythonperf1_win32-x86-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_dna      | 118 ms                                                                          | 120 ms: 1.01x slower                                                               |
| regex_v8       | 15.6 ms                                                                         | 15.9 ms: 1.02x slower                                                              |
| regex_compile  | 105 ms                                                                          | 108 ms: 1.03x slower                                                               |
| Geometric mean | (ref)                                                                           | 1.01x slower                                                                       |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241022-pythonperf1_win32-x86-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| pickle_pure_python   | 243 us                                                                          | 244 us: 1.01x slower                                                               |
| tomli_loads          | 1.54 sec                                                                        | 1.56 sec: 1.01x slower                                                             |
| json_loads           | 20.6 us                                                                         | 20.9 us: 1.02x slower                                                              |
| xml_etree_parse      | 110 ms                                                                          | 112 ms: 1.02x slower                                                               |
| unpickle_pure_python | 160 us                                                                          | 166 us: 1.04x slower                                                               |
| xml_etree_iterparse  | 64.1 ms                                                                         | 66.6 ms: 1.04x slower                                                              |
| xml_etree_generate   | 55.5 ms                                                                         | 60.5 ms: 1.09x slower                                                              |
| xml_etree_process    | 40.7 ms                                                                         | 47.2 ms: 1.16x slower                                                              |
| Geometric mean       | (ref)                                                                           | 1.04x slower                                                                       |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241022-pythonperf1_win32-x86-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup | 26.7 ms                                                                         | 26.9 ms: 1.01x slower                                                              |
| Geometric mean | (ref)                                                                           | 1.00x slower                                                                       |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241022-pythonperf1_win32-x86-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|-----------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| django_template | 33.1 ms                                                                         | 32.4 ms: 1.02x faster                                                              |
| genshi_text     | 23.5 ms                                                                         | 23.2 ms: 1.01x faster                                                              |
| genshi_xml      | 54.0 ms                                                                         | 56.3 ms: 1.04x slower                                                              |
| mako            | 5.77 ms                                                                         | 6.29 ms: 1.09x slower                                                              |
| Geometric mean  | (ref)                                                                           | 1.02x slower                                                                       |

All benchmarks:
===============

| Benchmark                | bm-20241022-pythonperf1_win32-x86-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|--------------------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| sqlglot_normalize        | 238 ms                                                                          | 102 ms: 2.33x faster                                                               |
| raytrace                 | 265 ms                                                                          | 250 ms: 1.06x faster                                                               |
| richards_super           | 42.4 ms                                                                         | 40.0 ms: 1.06x faster                                                              |
| richards                 | 36.9 ms                                                                         | 35.4 ms: 1.04x faster                                                              |
| coverage                 | 54.0 ms                                                                         | 52.0 ms: 1.04x faster                                                              |
| django_template          | 33.1 ms                                                                         | 32.4 ms: 1.02x faster                                                              |
| coroutines               | 17.8 ms                                                                         | 17.5 ms: 1.02x faster                                                              |
| genshi_text              | 23.5 ms                                                                         | 23.2 ms: 1.01x faster                                                              |
| thrift                   | 775 us                                                                          | 767 us: 1.01x faster                                                               |
| sympy_expand             | 397 ms                                                                          | 400 ms: 1.01x slower                                                               |
| pickle_pure_python       | 243 us                                                                          | 244 us: 1.01x slower                                                               |
| async_tree_io_tg         | 549 ms                                                                          | 552 ms: 1.01x slower                                                               |
| pidigits                 | 205 ms                                                                          | 207 ms: 1.01x slower                                                               |
| 2to3                     | 265 ms                                                                          | 267 ms: 1.01x slower                                                               |
| sympy_str                | 230 ms                                                                          | 232 ms: 1.01x slower                                                               |
| python_startup           | 26.7 ms                                                                         | 26.9 ms: 1.01x slower                                                              |
| docutils                 | 2.04 sec                                                                        | 2.05 sec: 1.01x slower                                                             |
| sphinx                   | 842 ms                                                                          | 851 ms: 1.01x slower                                                               |
| telco                    | 6.08 ms                                                                         | 6.14 ms: 1.01x slower                                                              |
| regex_dna                | 118 ms                                                                          | 120 ms: 1.01x slower                                                               |
| tomli_loads              | 1.54 sec                                                                        | 1.56 sec: 1.01x slower                                                             |
| dulwich_log              | 49.7 ms                                                                         | 50.4 ms: 1.01x slower                                                              |
| regex_v8                 | 15.6 ms                                                                         | 15.9 ms: 1.02x slower                                                              |
| tornado_http             | 108 ms                                                                          | 110 ms: 1.02x slower                                                               |
| json_loads               | 20.6 us                                                                         | 20.9 us: 1.02x slower                                                              |
| sqlglot_parse            | 1.04 ms                                                                         | 1.06 ms: 1.02x slower                                                              |
| sqlglot_optimize         | 49.4 ms                                                                         | 50.3 ms: 1.02x slower                                                              |
| sqlglot_transpile        | 1.35 ms                                                                         | 1.37 ms: 1.02x slower                                                              |
| xml_etree_parse          | 110 ms                                                                          | 112 ms: 1.02x slower                                                               |
| go                       | 97.7 ms                                                                         | 99.8 ms: 1.02x slower                                                              |
| html5lib                 | 45.7 ms                                                                         | 46.9 ms: 1.03x slower                                                              |
| deepcopy_reduce          | 2.44 us                                                                         | 2.50 us: 1.03x slower                                                              |
| deepcopy                 | 237 us                                                                          | 244 us: 1.03x slower                                                               |
| logging_simple           | 7.46 us                                                                         | 7.70 us: 1.03x slower                                                              |
| typing_runtime_protocols | 137 us                                                                          | 142 us: 1.03x slower                                                               |
| regex_compile            | 105 ms                                                                          | 108 ms: 1.03x slower                                                               |
| async_generators         | 310 ms                                                                          | 320 ms: 1.03x slower                                                               |
| unpickle_pure_python     | 160 us                                                                          | 166 us: 1.04x slower                                                               |
| xml_etree_iterparse      | 64.1 ms                                                                         | 66.6 ms: 1.04x slower                                                              |
| logging_format           | 8.06 us                                                                         | 8.40 us: 1.04x slower                                                              |
| genshi_xml               | 54.0 ms                                                                         | 56.3 ms: 1.04x slower                                                              |
| pprint_safe_repr         | 575 ms                                                                          | 602 ms: 1.05x slower                                                               |
| pprint_pformat           | 1.18 sec                                                                        | 1.23 sec: 1.05x slower                                                             |
| meteor_contest           | 71.9 ms                                                                         | 75.3 ms: 1.05x slower                                                              |
| sympy_integrate          | 17.2 ms                                                                         | 18.1 ms: 1.05x slower                                                              |
| nbody                    | 63.7 ms                                                                         | 67.2 ms: 1.05x slower                                                              |
| deltablue                | 2.57 ms                                                                         | 2.71 ms: 1.06x slower                                                              |
| nqueens                  | 75.6 ms                                                                         | 80.3 ms: 1.06x slower                                                              |
| pyflate                  | 315 ms                                                                          | 335 ms: 1.06x slower                                                               |
| hexiom                   | 5.53 ms                                                                         | 5.90 ms: 1.07x slower                                                              |
| comprehensions           | 13.1 us                                                                         | 14.0 us: 1.07x slower                                                              |
| chaos                    | 54.8 ms                                                                         | 59.1 ms: 1.08x slower                                                              |
| float                    | 45.9 ms                                                                         | 49.7 ms: 1.08x slower                                                              |
| xml_etree_generate       | 55.5 ms                                                                         | 60.5 ms: 1.09x slower                                                              |
| crypto_pyaes             | 50.1 ms                                                                         | 54.6 ms: 1.09x slower                                                              |
| mako                     | 5.77 ms                                                                         | 6.29 ms: 1.09x slower                                                              |
| generators               | 24.2 ms                                                                         | 26.6 ms: 1.10x slower                                                              |
| deepcopy_memo            | 16.3 us                                                                         | 18.0 us: 1.10x slower                                                              |
| scimark_sparse_mat_mult  | 2.44 ms                                                                         | 2.73 ms: 1.12x slower                                                              |
| scimark_lu               | 60.7 ms                                                                         | 68.9 ms: 1.14x slower                                                              |
| scimark_sor              | 68.1 ms                                                                         | 78.0 ms: 1.15x slower                                                              |
| scimark_monte_carlo      | 39.4 ms                                                                         | 45.2 ms: 1.15x slower                                                              |
| spectral_norm            | 59.1 ms                                                                         | 68.5 ms: 1.16x slower                                                              |
| xml_etree_process        | 40.7 ms                                                                         | 47.2 ms: 1.16x slower                                                              |
| scimark_fft              | 177 ms                                                                          | 206 ms: 1.16x slower                                                               |
| fannkuch                 | 245 ms                                                                          | 286 ms: 1.17x slower                                                               |
| logging_silent           | 52.6 ns                                                                         | 63.6 ns: 1.21x slower                                                              |
| Geometric mean           | (ref)                                                                           | 1.02x slower                                                                       |

Benchmark hidden because not significant (20): json, bench_thread_pool, async_tree_none, async_tree_memoization, async_tree_memoization_tg, async_tree_io, pathlib, async_tree_cpu_io_mixed, regex_effbot, sympy_sum, bench_mp_pool, python_startup_no_site, mdp, async_tree_cpu_io_mixed_tg, json_dumps, create_gc_cycles, pycparser, gc_traversal, pylint, async_tree_none_tg

- Geometric mean (including insignificant results): 1.021x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown