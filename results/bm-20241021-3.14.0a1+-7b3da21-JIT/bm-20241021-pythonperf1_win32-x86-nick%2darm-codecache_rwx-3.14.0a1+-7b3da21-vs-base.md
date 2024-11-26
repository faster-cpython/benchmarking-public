# Results vs. base

- fork: nick-arm
- ref: codecache_rwx
- machine: windows-x86
- commit hash: 7b3da21
- commit date: 2024-10-21
- overall geometric mean: 1.024x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 263 ms                                                                          | 251 ms: 1.05x faster                                                         |
| docutils       | 2.06 sec                                                                        | 1.94 sec: 1.06x faster                                                       |
| html5lib       | 46.4 ms                                                                         | 45.1 ms: 1.03x faster                                                        |
| sphinx         | 849 ms                                                                          | 795 ms: 1.07x faster                                                         |
| Geometric mean | (ref)                                                                           | 1.04x faster                                                                 |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 562 ms                                                                          | 549 ms: 1.02x faster                                                         |
| coroutines                 | 17.7 ms                                                                         | 17.6 ms: 1.01x faster                                                        |
| async_tree_cpu_io_mixed_tg | 466 ms                                                                          | 462 ms: 1.01x faster                                                         |
| async_generators           | 315 ms                                                                          | 324 ms: 1.03x slower                                                         |
| Geometric mean             | (ref)                                                                           | 1.00x faster                                                                 |

Benchmark hidden because not significant (6): async_tree_memoization, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 65.9 ms                                                                         | 56.4 ms: 1.17x faster                                                        |
| float          | 46.7 ms                                                                         | 45.8 ms: 1.02x faster                                                        |
| pidigits       | 205 ms                                                                          | 204 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                                           | 1.06x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 1.90 ms                                                                         | 1.79 ms: 1.06x faster                                                        |
| regex_compile  | 104 ms                                                                          | 98.5 ms: 1.06x faster                                                        |
| regex_dna      | 123 ms                                                                          | 116 ms: 1.06x faster                                                         |
| Geometric mean | (ref)                                                                           | 1.04x faster                                                                 |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|---------------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_loads          | 21.3 us                                                                         | 20.8 us: 1.02x faster                                                        |
| xml_etree_iterparse | 65.2 ms                                                                         | 64.1 ms: 1.02x faster                                                        |
| xml_etree_process   | 41.4 ms                                                                         | 41.0 ms: 1.01x faster                                                        |
| pickle_pure_python  | 239 us                                                                          | 241 us: 1.01x slower                                                         |
| tomli_loads         | 1.49 sec                                                                        | 1.52 sec: 1.02x slower                                                       |
| Geometric mean      | (ref)                                                                           | 1.00x faster                                                                 |

Benchmark hidden because not significant (4): json_dumps, unpickle_pure_python, xml_etree_generate, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|------------------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 20.2 ms                                                                         | 20.4 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                                           | 1.00x slower                                                                 |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text    | 23.1 ms                                                                         | 22.3 ms: 1.04x faster                                                        |
| genshi_xml     | 52.7 ms                                                                         | 52.2 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                                           | 1.01x faster                                                                 |

Benchmark hidden because not significant (2): mako, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody                      | 65.9 ms                                                                         | 56.4 ms: 1.17x faster                                                        |
| generators                 | 24.7 ms                                                                         | 21.8 ms: 1.13x faster                                                        |
| fannkuch                   | 248 ms                                                                          | 219 ms: 1.13x faster                                                         |
| comprehensions             | 13.2 us                                                                         | 11.7 us: 1.13x faster                                                        |
| hexiom                     | 5.27 ms                                                                         | 4.75 ms: 1.11x faster                                                        |
| mdp                        | 1.84 sec                                                                        | 1.68 sec: 1.10x faster                                                       |
| pylint                     | 283 ms                                                                          | 261 ms: 1.08x faster                                                         |
| pyflate                    | 319 ms                                                                          | 296 ms: 1.07x faster                                                         |
| sympy_sum                  | 117 ms                                                                          | 109 ms: 1.07x faster                                                         |
| richards_super             | 44.5 ms                                                                         | 41.6 ms: 1.07x faster                                                        |
| richards                   | 39.3 ms                                                                         | 36.7 ms: 1.07x faster                                                        |
| sphinx                     | 849 ms                                                                          | 795 ms: 1.07x faster                                                         |
| regex_effbot               | 1.90 ms                                                                         | 1.79 ms: 1.06x faster                                                        |
| sqlglot_optimize           | 49.8 ms                                                                         | 46.9 ms: 1.06x faster                                                        |
| regex_compile              | 104 ms                                                                          | 98.5 ms: 1.06x faster                                                        |
| telco                      | 6.06 ms                                                                         | 5.72 ms: 1.06x faster                                                        |
| docutils                   | 2.06 sec                                                                        | 1.94 sec: 1.06x faster                                                       |
| regex_dna                  | 123 ms                                                                          | 116 ms: 1.06x faster                                                         |
| sqlglot_parse              | 1.06 ms                                                                         | 1.01 ms: 1.06x faster                                                        |
| 2to3                       | 263 ms                                                                          | 251 ms: 1.05x faster                                                         |
| go                         | 96.7 ms                                                                         | 92.2 ms: 1.05x faster                                                        |
| meteor_contest             | 73.1 ms                                                                         | 69.9 ms: 1.05x faster                                                        |
| sqlglot_transpile          | 1.37 ms                                                                         | 1.31 ms: 1.04x faster                                                        |
| sympy_str                  | 229 ms                                                                          | 220 ms: 1.04x faster                                                         |
| genshi_text                | 23.1 ms                                                                         | 22.3 ms: 1.04x faster                                                        |
| sympy_expand               | 400 ms                                                                          | 387 ms: 1.03x faster                                                         |
| pycparser                  | 824 ms                                                                          | 798 ms: 1.03x faster                                                         |
| html5lib                   | 46.4 ms                                                                         | 45.1 ms: 1.03x faster                                                        |
| typing_runtime_protocols   | 147 us                                                                          | 143 us: 1.03x faster                                                         |
| sympy_integrate            | 17.3 ms                                                                         | 16.8 ms: 1.03x faster                                                        |
| bench_mp_pool              | 94.1 ms                                                                         | 91.8 ms: 1.02x faster                                                        |
| json_loads                 | 21.3 us                                                                         | 20.8 us: 1.02x faster                                                        |
| async_tree_io_tg           | 562 ms                                                                          | 549 ms: 1.02x faster                                                         |
| deepcopy                   | 231 us                                                                          | 227 us: 1.02x faster                                                         |
| dulwich_log                | 49.3 ms                                                                         | 48.3 ms: 1.02x faster                                                        |
| scimark_monte_carlo        | 39.0 ms                                                                         | 38.3 ms: 1.02x faster                                                        |
| coverage                   | 54.1 ms                                                                         | 53.1 ms: 1.02x faster                                                        |
| float                      | 46.7 ms                                                                         | 45.8 ms: 1.02x faster                                                        |
| xml_etree_iterparse        | 65.2 ms                                                                         | 64.1 ms: 1.02x faster                                                        |
| sqlglot_normalize          | 240 ms                                                                          | 236 ms: 1.02x faster                                                         |
| scimark_sparse_mat_mult    | 2.50 ms                                                                         | 2.46 ms: 1.01x faster                                                        |
| gc_traversal               | 1.82 ms                                                                         | 1.80 ms: 1.01x faster                                                        |
| genshi_xml                 | 52.7 ms                                                                         | 52.2 ms: 1.01x faster                                                        |
| xml_etree_process          | 41.4 ms                                                                         | 41.0 ms: 1.01x faster                                                        |
| coroutines                 | 17.7 ms                                                                         | 17.6 ms: 1.01x faster                                                        |
| async_tree_cpu_io_mixed_tg | 466 ms                                                                          | 462 ms: 1.01x faster                                                         |
| logging_simple             | 7.63 us                                                                         | 7.58 us: 1.01x faster                                                        |
| pidigits                   | 205 ms                                                                          | 204 ms: 1.01x faster                                                         |
| raytrace                   | 271 ms                                                                          | 274 ms: 1.01x slower                                                         |
| pickle_pure_python         | 239 us                                                                          | 241 us: 1.01x slower                                                         |
| scimark_fft                | 182 ms                                                                          | 184 ms: 1.01x slower                                                         |
| python_startup_no_site     | 20.2 ms                                                                         | 20.4 ms: 1.01x slower                                                        |
| tomli_loads                | 1.49 sec                                                                        | 1.52 sec: 1.02x slower                                                       |
| pprint_safe_repr           | 560 ms                                                                          | 570 ms: 1.02x slower                                                         |
| pprint_pformat             | 1.14 sec                                                                        | 1.17 sec: 1.02x slower                                                       |
| thrift                     | 770 us                                                                          | 789 us: 1.03x slower                                                         |
| nqueens                    | 73.9 ms                                                                         | 75.9 ms: 1.03x slower                                                        |
| async_generators           | 315 ms                                                                          | 324 ms: 1.03x slower                                                         |
| chaos                      | 52.8 ms                                                                         | 54.5 ms: 1.03x slower                                                        |
| logging_silent             | 53.8 ns                                                                         | 55.8 ns: 1.04x slower                                                        |
| scimark_sor                | 66.5 ms                                                                         | 70.4 ms: 1.06x slower                                                        |
| Geometric mean             | (ref)                                                                           | 1.02x faster                                                                 |

Benchmark hidden because not significant (26): async_tree_memoization, tornado_http, deltablue, create_gc_cycles, async_tree_none_tg, json_dumps, unpickle_pure_python, python_startup, mako, xml_etree_generate, logging_format, pathlib, regex_v8, async_tree_cpu_io_mixed, deepcopy_reduce, scimark_lu, crypto_pyaes, async_tree_io, xml_etree_parse, spectral_norm, json, async_tree_memoization_tg, django_template, deepcopy_memo, async_tree_none, bench_thread_pool

- Geometric mean (including insignificant results): 1.024x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown