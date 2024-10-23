# Results vs. base

- fork: nick-arm
- ref: codecache_rwx
- machine: windows-x86
- commit hash: 7b3da21
- commit date: 2024-10-21
- overall geometric mean: 1.01x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 264 ms                                                                          | 251 ms: 1.05x faster                                                         |
| docutils       | 2.06 sec                                                                        | 1.94 sec: 1.06x faster                                                       |
| html5lib       | 46.2 ms                                                                         | 45.1 ms: 1.02x faster                                                        |
| sphinx         | 851 ms                                                                          | 795 ms: 1.07x faster                                                         |
| Geometric mean | (ref)                                                                           | 1.04x faster                                                                 |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 269 ms                                                                          | 256 ms: 1.05x faster                                                         |
| async_tree_cpu_io_mixed_tg | 470 ms                                                                          | 462 ms: 1.02x faster                                                         |
| async_tree_cpu_io_mixed    | 476 ms                                                                          | 468 ms: 1.02x faster                                                         |
| async_tree_none_tg         | 206 ms                                                                          | 203 ms: 1.01x faster                                                         |
| coroutines                 | 17.3 ms                                                                         | 17.6 ms: 1.01x slower                                                        |
| async_generators           | 314 ms                                                                          | 324 ms: 1.03x slower                                                         |
| Geometric mean             | (ref)                                                                           | 1.01x faster                                                                 |

Benchmark hidden because not significant (4): async_tree_io_tg, async_tree_none, async_tree_memoization, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 64.6 ms                                                                         | 56.4 ms: 1.15x faster                                                        |
| float          | 46.6 ms                                                                         | 45.8 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                                           | 1.05x faster                                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 105 ms                                                                          | 98.5 ms: 1.07x faster                                                        |
| regex_dna      | 124 ms                                                                          | 116 ms: 1.06x faster                                                         |
| regex_effbot   | 1.89 ms                                                                         | 1.79 ms: 1.06x faster                                                        |
| regex_v8       | 15.4 ms                                                                         | 15.6 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                           | 1.04x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_process    | 42.1 ms                                                                         | 41.0 ms: 1.03x faster                                                        |
| pickle_pure_python   | 246 us                                                                          | 241 us: 1.02x faster                                                         |
| unpickle_pure_python | 160 us                                                                          | 158 us: 1.01x faster                                                         |
| xml_etree_iterparse  | 65.1 ms                                                                         | 64.1 ms: 1.01x faster                                                        |
| tomli_loads          | 1.53 sec                                                                        | 1.52 sec: 1.01x faster                                                       |
| xml_etree_generate   | 55.1 ms                                                                         | 55.5 ms: 1.01x slower                                                        |
| Geometric mean       | (ref)                                                                           | 1.01x faster                                                                 |

Benchmark hidden because not significant (3): xml_etree_parse, json_dumps, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup | 26.7 ms                                                                         | 27.0 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                           | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|-----------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 23.4 ms                                                                         | 22.3 ms: 1.05x faster                                                        |
| genshi_xml      | 54.3 ms                                                                         | 52.2 ms: 1.04x faster                                                        |
| django_template | 32.7 ms                                                                         | 33.5 ms: 1.03x slower                                                        |
| Geometric mean  | (ref)                                                                           | 1.02x faster                                                                 |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody                      | 64.6 ms                                                                         | 56.4 ms: 1.15x faster                                                        |
| hexiom                     | 5.32 ms                                                                         | 4.75 ms: 1.12x faster                                                        |
| comprehensions             | 13.0 us                                                                         | 11.7 us: 1.11x faster                                                        |
| telco                      | 6.33 ms                                                                         | 5.72 ms: 1.11x faster                                                        |
| generators                 | 23.9 ms                                                                         | 21.8 ms: 1.10x faster                                                        |
| richards_super             | 45.3 ms                                                                         | 41.6 ms: 1.09x faster                                                        |
| pylint                     | 283 ms                                                                          | 261 ms: 1.08x faster                                                         |
| fannkuch                   | 237 ms                                                                          | 219 ms: 1.08x faster                                                         |
| sphinx                     | 851 ms                                                                          | 795 ms: 1.07x faster                                                         |
| regex_compile              | 105 ms                                                                          | 98.5 ms: 1.07x faster                                                        |
| richards                   | 39.2 ms                                                                         | 36.7 ms: 1.07x faster                                                        |
| sqlglot_optimize           | 49.9 ms                                                                         | 46.9 ms: 1.06x faster                                                        |
| regex_dna                  | 124 ms                                                                          | 116 ms: 1.06x faster                                                         |
| regex_effbot               | 1.89 ms                                                                         | 1.79 ms: 1.06x faster                                                        |
| sympy_sum                  | 116 ms                                                                          | 109 ms: 1.06x faster                                                         |
| docutils                   | 2.06 sec                                                                        | 1.94 sec: 1.06x faster                                                       |
| 2to3                       | 264 ms                                                                          | 251 ms: 1.05x faster                                                         |
| pyflate                    | 312 ms                                                                          | 296 ms: 1.05x faster                                                         |
| async_tree_memoization_tg  | 269 ms                                                                          | 256 ms: 1.05x faster                                                         |
| genshi_text                | 23.4 ms                                                                         | 22.3 ms: 1.05x faster                                                        |
| go                         | 96.7 ms                                                                         | 92.2 ms: 1.05x faster                                                        |
| scimark_monte_carlo        | 40.0 ms                                                                         | 38.3 ms: 1.04x faster                                                        |
| sympy_str                  | 230 ms                                                                          | 220 ms: 1.04x faster                                                         |
| sqlglot_parse              | 1.05 ms                                                                         | 1.01 ms: 1.04x faster                                                        |
| genshi_xml                 | 54.3 ms                                                                         | 52.2 ms: 1.04x faster                                                        |
| deepcopy                   | 236 us                                                                          | 227 us: 1.04x faster                                                         |
| scimark_lu                 | 61.8 ms                                                                         | 59.6 ms: 1.04x faster                                                        |
| meteor_contest             | 72.3 ms                                                                         | 69.9 ms: 1.03x faster                                                        |
| sqlglot_transpile          | 1.35 ms                                                                         | 1.31 ms: 1.03x faster                                                        |
| sympy_expand               | 399 ms                                                                          | 387 ms: 1.03x faster                                                         |
| sympy_integrate            | 17.3 ms                                                                         | 16.8 ms: 1.03x faster                                                        |
| xml_etree_process          | 42.1 ms                                                                         | 41.0 ms: 1.03x faster                                                        |
| html5lib                   | 46.2 ms                                                                         | 45.1 ms: 1.02x faster                                                        |
| bench_mp_pool              | 94.1 ms                                                                         | 91.8 ms: 1.02x faster                                                        |
| dulwich_log                | 49.5 ms                                                                         | 48.3 ms: 1.02x faster                                                        |
| deepcopy_memo              | 16.6 us                                                                         | 16.3 us: 1.02x faster                                                        |
| pickle_pure_python         | 246 us                                                                          | 241 us: 1.02x faster                                                         |
| async_tree_cpu_io_mixed_tg | 470 ms                                                                          | 462 ms: 1.02x faster                                                         |
| async_tree_cpu_io_mixed    | 476 ms                                                                          | 468 ms: 1.02x faster                                                         |
| float                      | 46.6 ms                                                                         | 45.8 ms: 1.02x faster                                                        |
| mdp                        | 1.70 sec                                                                        | 1.68 sec: 1.02x faster                                                       |
| deepcopy_reduce            | 2.44 us                                                                         | 2.41 us: 1.02x faster                                                        |
| unpickle_pure_python       | 160 us                                                                          | 158 us: 1.01x faster                                                         |
| xml_etree_iterparse        | 65.1 ms                                                                         | 64.1 ms: 1.01x faster                                                        |
| pycparser                  | 809 ms                                                                          | 798 ms: 1.01x faster                                                         |
| async_tree_none_tg         | 206 ms                                                                          | 203 ms: 1.01x faster                                                         |
| gc_traversal               | 1.82 ms                                                                         | 1.80 ms: 1.01x faster                                                        |
| scimark_sparse_mat_mult    | 2.48 ms                                                                         | 2.46 ms: 1.01x faster                                                        |
| tomli_loads                | 1.53 sec                                                                        | 1.52 sec: 1.01x faster                                                       |
| nqueens                    | 76.3 ms                                                                         | 75.9 ms: 1.01x faster                                                        |
| scimark_fft                | 183 ms                                                                          | 184 ms: 1.00x slower                                                         |
| logging_format             | 8.23 us                                                                         | 8.28 us: 1.01x slower                                                        |
| pprint_safe_repr           | 567 ms                                                                          | 570 ms: 1.01x slower                                                         |
| deltablue                  | 2.52 ms                                                                         | 2.54 ms: 1.01x slower                                                        |
| xml_etree_generate         | 55.1 ms                                                                         | 55.5 ms: 1.01x slower                                                        |
| python_startup             | 26.7 ms                                                                         | 27.0 ms: 1.01x slower                                                        |
| spectral_norm              | 57.8 ms                                                                         | 58.4 ms: 1.01x slower                                                        |
| thrift                     | 780 us                                                                          | 789 us: 1.01x slower                                                         |
| pprint_pformat             | 1.16 sec                                                                        | 1.17 sec: 1.01x slower                                                       |
| typing_runtime_protocols   | 141 us                                                                          | 143 us: 1.01x slower                                                         |
| regex_v8                   | 15.4 ms                                                                         | 15.6 ms: 1.01x slower                                                        |
| coroutines                 | 17.3 ms                                                                         | 17.6 ms: 1.01x slower                                                        |
| django_template            | 32.7 ms                                                                         | 33.5 ms: 1.03x slower                                                        |
| async_generators           | 314 ms                                                                          | 324 ms: 1.03x slower                                                         |
| sqlglot_normalize          | 101 ms                                                                          | 236 ms: 2.34x slower                                                         |
| Geometric mean             | (ref)                                                                           | 1.01x faster                                                                 |

Benchmark hidden because not significant (22): xml_etree_parse, coverage, raytrace, json_dumps, crypto_pyaes, async_tree_io_tg, async_tree_none, mako, async_tree_memoization, logging_simple, json_loads, python_startup_no_site, pathlib, chaos, json, pidigits, async_tree_io, scimark_sor, logging_silent, tornado_http, create_gc_cycles, bench_thread_pool

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown