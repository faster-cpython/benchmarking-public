# Results vs. base

- fork: brandtbucher
- ref: justin_no_externs
- machine: windows-x86
- commit hash: 9698931
- commit date: 2024-10-24
- overall geometric mean: 1.055x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241022-pythonperf1_win32-x86-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                                          | 274 ms: 1.03x slower                                                               |
| docutils       | 2.04 sec                                                                        | 2.10 sec: 1.03x slower                                                             |
| html5lib       | 45.7 ms                                                                         | 48.7 ms: 1.07x slower                                                              |
| sphinx         | 842 ms                                                                          | 870 ms: 1.03x slower                                                               |
| tornado_http   | 108 ms                                                                          | 110 ms: 1.01x slower                                                               |
| Geometric mean | (ref)                                                                           | 1.04x slower                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241022-pythonperf1_win32-x86-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| coroutines                 | 17.8 ms                                                                         | 17.9 ms: 1.01x slower                                                              |
| async_tree_cpu_io_mixed    | 466 ms                                                                          | 474 ms: 1.02x slower                                                               |
| async_tree_cpu_io_mixed_tg | 462 ms                                                                          | 471 ms: 1.02x slower                                                               |
| async_tree_io_tg           | 549 ms                                                                          | 559 ms: 1.02x slower                                                               |
| async_tree_memoization     | 279 ms                                                                          | 287 ms: 1.03x slower                                                               |
| async_tree_io              | 524 ms                                                                          | 540 ms: 1.03x slower                                                               |
| async_tree_none            | 221 ms                                                                          | 228 ms: 1.03x slower                                                               |
| async_tree_memoization_tg  | 255 ms                                                                          | 264 ms: 1.04x slower                                                               |
| async_generators           | 310 ms                                                                          | 326 ms: 1.05x slower                                                               |
| async_tree_none_tg         | 201 ms                                                                          | 212 ms: 1.05x slower                                                               |
| Geometric mean             | (ref)                                                                           | 1.03x slower                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241022-pythonperf1_win32-x86-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| pidigits       | 205 ms                                                                          | 207 ms: 1.01x slower                                                               |
| nbody          | 63.7 ms                                                                         | 70.3 ms: 1.10x slower                                                              |
| float          | 45.9 ms                                                                         | 52.2 ms: 1.14x slower                                                              |
| Geometric mean | (ref)                                                                           | 1.08x slower                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241022-pythonperf1_win32-x86-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_effbot   | 1.81 ms                                                                         | 1.79 ms: 1.01x faster                                                              |
| regex_v8       | 15.6 ms                                                                         | 15.7 ms: 1.01x slower                                                              |
| regex_compile  | 105 ms                                                                          | 113 ms: 1.08x slower                                                               |
| Geometric mean | (ref)                                                                           | 1.02x slower                                                                       |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241022-pythonperf1_win32-x86-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| xml_etree_parse      | 110 ms                                                                          | 113 ms: 1.03x slower                                                               |
| json_dumps           | 8.11 ms                                                                         | 8.50 ms: 1.05x slower                                                              |
| json_loads           | 20.6 us                                                                         | 21.7 us: 1.05x slower                                                              |
| pickle_pure_python   | 243 us                                                                          | 258 us: 1.06x slower                                                               |
| xml_etree_iterparse  | 64.1 ms                                                                         | 68.2 ms: 1.06x slower                                                              |
| tomli_loads          | 1.54 sec                                                                        | 1.64 sec: 1.07x slower                                                             |
| unpickle_pure_python | 160 us                                                                          | 173 us: 1.08x slower                                                               |
| xml_etree_generate   | 55.5 ms                                                                         | 63.8 ms: 1.15x slower                                                              |
| xml_etree_process    | 40.7 ms                                                                         | 47.7 ms: 1.17x slower                                                              |
| Geometric mean       | (ref)                                                                           | 1.08x slower                                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241022-pythonperf1_win32-x86-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup | 26.7 ms                                                                         | 26.4 ms: 1.01x faster                                                              |
| Geometric mean | (ref)                                                                           | 1.01x faster                                                                       |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241022-pythonperf1_win32-x86-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|-----------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| django_template | 33.1 ms                                                                         | 34.7 ms: 1.05x slower                                                              |
| genshi_text     | 23.5 ms                                                                         | 24.9 ms: 1.06x slower                                                              |
| genshi_xml      | 54.0 ms                                                                         | 58.0 ms: 1.07x slower                                                              |
| mako            | 5.77 ms                                                                         | 6.83 ms: 1.18x slower                                                              |
| Geometric mean  | (ref)                                                                           | 1.09x slower                                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20241022-pythonperf1_win32-x86-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| sqlglot_normalize          | 238 ms                                                                          | 102 ms: 2.33x faster                                                               |
| regex_effbot               | 1.81 ms                                                                         | 1.79 ms: 1.01x faster                                                              |
| python_startup             | 26.7 ms                                                                         | 26.4 ms: 1.01x faster                                                              |
| regex_v8                   | 15.6 ms                                                                         | 15.7 ms: 1.01x slower                                                              |
| coroutines                 | 17.8 ms                                                                         | 17.9 ms: 1.01x slower                                                              |
| pidigits                   | 205 ms                                                                          | 207 ms: 1.01x slower                                                               |
| dulwich_log                | 49.7 ms                                                                         | 50.1 ms: 1.01x slower                                                              |
| tornado_http               | 108 ms                                                                          | 110 ms: 1.01x slower                                                               |
| thrift                     | 775 us                                                                          | 788 us: 1.02x slower                                                               |
| async_tree_cpu_io_mixed    | 466 ms                                                                          | 474 ms: 1.02x slower                                                               |
| async_tree_cpu_io_mixed_tg | 462 ms                                                                          | 471 ms: 1.02x slower                                                               |
| async_tree_io_tg           | 549 ms                                                                          | 559 ms: 1.02x slower                                                               |
| mdp                        | 1.75 sec                                                                        | 1.79 sec: 1.02x slower                                                             |
| sqlglot_optimize           | 49.4 ms                                                                         | 50.6 ms: 1.02x slower                                                              |
| async_tree_memoization     | 279 ms                                                                          | 287 ms: 1.03x slower                                                               |
| xml_etree_parse            | 110 ms                                                                          | 113 ms: 1.03x slower                                                               |
| sympy_sum                  | 118 ms                                                                          | 122 ms: 1.03x slower                                                               |
| deepcopy                   | 237 us                                                                          | 244 us: 1.03x slower                                                               |
| async_tree_io              | 524 ms                                                                          | 540 ms: 1.03x slower                                                               |
| sphinx                     | 842 ms                                                                          | 870 ms: 1.03x slower                                                               |
| sympy_expand               | 397 ms                                                                          | 410 ms: 1.03x slower                                                               |
| deepcopy_reduce            | 2.44 us                                                                         | 2.52 us: 1.03x slower                                                              |
| async_tree_none            | 221 ms                                                                          | 228 ms: 1.03x slower                                                               |
| 2to3                       | 265 ms                                                                          | 274 ms: 1.03x slower                                                               |
| docutils                   | 2.04 sec                                                                        | 2.10 sec: 1.03x slower                                                             |
| async_tree_memoization_tg  | 255 ms                                                                          | 264 ms: 1.04x slower                                                               |
| sympy_str                  | 230 ms                                                                          | 239 ms: 1.04x slower                                                               |
| telco                      | 6.08 ms                                                                         | 6.32 ms: 1.04x slower                                                              |
| raytrace                   | 265 ms                                                                          | 277 ms: 1.04x slower                                                               |
| json_dumps                 | 8.11 ms                                                                         | 8.50 ms: 1.05x slower                                                              |
| django_template            | 33.1 ms                                                                         | 34.7 ms: 1.05x slower                                                              |
| pycparser                  | 821 ms                                                                          | 862 ms: 1.05x slower                                                               |
| richards_super             | 42.4 ms                                                                         | 44.6 ms: 1.05x slower                                                              |
| json_loads                 | 20.6 us                                                                         | 21.7 us: 1.05x slower                                                              |
| async_generators           | 310 ms                                                                          | 326 ms: 1.05x slower                                                               |
| sqlglot_transpile          | 1.35 ms                                                                         | 1.42 ms: 1.05x slower                                                              |
| async_tree_none_tg         | 201 ms                                                                          | 212 ms: 1.05x slower                                                               |
| sqlglot_parse              | 1.04 ms                                                                         | 1.10 ms: 1.06x slower                                                              |
| sympy_integrate            | 17.2 ms                                                                         | 18.3 ms: 1.06x slower                                                              |
| pickle_pure_python         | 243 us                                                                          | 258 us: 1.06x slower                                                               |
| genshi_text                | 23.5 ms                                                                         | 24.9 ms: 1.06x slower                                                              |
| logging_format             | 8.06 us                                                                         | 8.57 us: 1.06x slower                                                              |
| xml_etree_iterparse        | 64.1 ms                                                                         | 68.2 ms: 1.06x slower                                                              |
| html5lib                   | 45.7 ms                                                                         | 48.7 ms: 1.07x slower                                                              |
| tomli_loads                | 1.54 sec                                                                        | 1.64 sec: 1.07x slower                                                             |
| logging_simple             | 7.46 us                                                                         | 7.96 us: 1.07x slower                                                              |
| richards                   | 36.9 ms                                                                         | 39.5 ms: 1.07x slower                                                              |
| chaos                      | 54.8 ms                                                                         | 58.7 ms: 1.07x slower                                                              |
| genshi_xml                 | 54.0 ms                                                                         | 58.0 ms: 1.07x slower                                                              |
| regex_compile              | 105 ms                                                                          | 113 ms: 1.08x slower                                                               |
| unpickle_pure_python       | 160 us                                                                          | 173 us: 1.08x slower                                                               |
| scimark_lu                 | 60.7 ms                                                                         | 65.7 ms: 1.08x slower                                                              |
| nqueens                    | 75.6 ms                                                                         | 82.6 ms: 1.09x slower                                                              |
| nbody                      | 63.7 ms                                                                         | 70.3 ms: 1.10x slower                                                              |
| typing_runtime_protocols   | 137 us                                                                          | 152 us: 1.11x slower                                                               |
| pprint_safe_repr           | 575 ms                                                                          | 642 ms: 1.12x slower                                                               |
| go                         | 97.7 ms                                                                         | 109 ms: 1.12x slower                                                               |
| pprint_pformat             | 1.18 sec                                                                        | 1.33 sec: 1.13x slower                                                             |
| meteor_contest             | 71.9 ms                                                                         | 81.3 ms: 1.13x slower                                                              |
| deltablue                  | 2.57 ms                                                                         | 2.91 ms: 1.13x slower                                                              |
| pyflate                    | 315 ms                                                                          | 358 ms: 1.13x slower                                                               |
| float                      | 45.9 ms                                                                         | 52.2 ms: 1.14x slower                                                              |
| xml_etree_generate         | 55.5 ms                                                                         | 63.8 ms: 1.15x slower                                                              |
| hexiom                     | 5.53 ms                                                                         | 6.40 ms: 1.16x slower                                                              |
| generators                 | 24.2 ms                                                                         | 28.1 ms: 1.16x slower                                                              |
| comprehensions             | 13.1 us                                                                         | 15.3 us: 1.16x slower                                                              |
| xml_etree_process          | 40.7 ms                                                                         | 47.7 ms: 1.17x slower                                                              |
| scimark_sparse_mat_mult    | 2.44 ms                                                                         | 2.89 ms: 1.18x slower                                                              |
| mako                       | 5.77 ms                                                                         | 6.83 ms: 1.18x slower                                                              |
| scimark_fft                | 177 ms                                                                          | 210 ms: 1.19x slower                                                               |
| fannkuch                   | 245 ms                                                                          | 291 ms: 1.19x slower                                                               |
| crypto_pyaes               | 50.1 ms                                                                         | 59.7 ms: 1.19x slower                                                              |
| deepcopy_memo              | 16.3 us                                                                         | 19.6 us: 1.20x slower                                                              |
| scimark_sor                | 68.1 ms                                                                         | 83.3 ms: 1.22x slower                                                              |
| spectral_norm              | 59.1 ms                                                                         | 72.5 ms: 1.23x slower                                                              |
| scimark_monte_carlo        | 39.4 ms                                                                         | 51.0 ms: 1.30x slower                                                              |
| logging_silent             | 52.6 ns                                                                         | 76.8 ns: 1.46x slower                                                              |
| Geometric mean             | (ref)                                                                           | 1.06x slower                                                                       |

Benchmark hidden because not significant (10): bench_thread_pool, python_startup_no_site, pathlib, gc_traversal, bench_mp_pool, create_gc_cycles, coverage, regex_dna, pylint, json

- Geometric mean (including insignificant results): 1.055x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown