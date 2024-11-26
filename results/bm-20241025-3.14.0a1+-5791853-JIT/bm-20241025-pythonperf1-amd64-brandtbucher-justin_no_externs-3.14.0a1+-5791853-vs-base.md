# Results vs. base

- fork: brandtbucher
- ref: justin_no_externs
- machine: windows-amd64
- commit hash: 5791853
- commit date: 2024-10-25
- overall geometric mean: 1.018x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241022-pythonperf1-amd64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 247 ms                                                                      | 253 ms: 1.03x slower                                                           |
| docutils       | 1.91 sec                                                                    | 1.94 sec: 1.01x slower                                                         |
| html5lib       | 38.9 ms                                                                     | 40.6 ms: 1.04x slower                                                          |
| tornado_http   | 99.5 ms                                                                     | 98.6 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                                       | 1.02x slower                                                                   |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241022-pythonperf1-amd64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_generators           | 263 ms                                                                      | 267 ms: 1.01x slower                                                           |
| async_tree_io              | 542 ms                                                                      | 550 ms: 1.02x slower                                                           |
| async_tree_cpu_io_mixed_tg | 399 ms                                                                      | 407 ms: 1.02x slower                                                           |
| async_tree_io_tg           | 631 ms                                                                      | 643 ms: 1.02x slower                                                           |
| async_tree_none_tg         | 210 ms                                                                      | 215 ms: 1.02x slower                                                           |
| coroutines                 | 13.6 ms                                                                     | 14.4 ms: 1.06x slower                                                          |
| Geometric mean             | (ref)                                                                       | 1.02x slower                                                                   |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_memoization, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241022-pythonperf1-amd64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 56.2 ms                                                                     | 51.9 ms: 1.08x faster                                                          |
| float          | 46.9 ms                                                                     | 48.1 ms: 1.03x slower                                                          |
| Geometric mean | (ref)                                                                       | 1.02x faster                                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241022-pythonperf1-amd64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 91.2 ms                                                                     | 92.7 ms: 1.02x slower                                                          |
| regex_effbot   | 1.56 ms                                                                     | 1.63 ms: 1.04x slower                                                          |
| regex_dna      | 116 ms                                                                      | 122 ms: 1.05x slower                                                           |
| regex_v8       | 14.7 ms                                                                     | 15.4 ms: 1.05x slower                                                          |
| Geometric mean | (ref)                                                                       | 1.04x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241022-pythonperf1-amd64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_loads           | 14.4 us                                                                     | 14.3 us: 1.00x faster                                                          |
| unpickle_pure_python | 144 us                                                                      | 145 us: 1.01x slower                                                           |
| xml_etree_generate   | 50.5 ms                                                                     | 51.2 ms: 1.01x slower                                                          |
| xml_etree_process    | 35.8 ms                                                                     | 36.5 ms: 1.02x slower                                                          |
| tomli_loads          | 1.28 sec                                                                    | 1.31 sec: 1.03x slower                                                         |
| json_dumps           | 6.22 ms                                                                     | 6.47 ms: 1.04x slower                                                          |
| Geometric mean       | (ref)                                                                       | 1.01x slower                                                                   |

Benchmark hidden because not significant (3): xml_etree_parse, pickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241022-pythonperf1-amd64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup | 24.4 ms                                                                     | 24.2 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241022-pythonperf1-amd64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|-----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| django_template | 28.0 ms                                                                     | 27.0 ms: 1.04x faster                                                          |
| genshi_text     | 19.2 ms                                                                     | 20.0 ms: 1.04x slower                                                          |
| genshi_xml      | 47.2 ms                                                                     | 49.1 ms: 1.04x slower                                                          |
| mako            | 4.96 ms                                                                     | 5.20 ms: 1.05x slower                                                          |
| Geometric mean  | (ref)                                                                       | 1.02x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241022-pythonperf1-amd64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody                      | 56.2 ms                                                                     | 51.9 ms: 1.08x faster                                                          |
| django_template            | 28.0 ms                                                                     | 27.0 ms: 1.04x faster                                                          |
| generators                 | 23.2 ms                                                                     | 22.5 ms: 1.03x faster                                                          |
| raytrace                   | 214 ms                                                                      | 208 ms: 1.03x faster                                                           |
| mdp                        | 1.58 sec                                                                    | 1.54 sec: 1.03x faster                                                         |
| logging_format             | 6.74 us                                                                     | 6.59 us: 1.02x faster                                                          |
| logging_simple             | 6.19 us                                                                     | 6.12 us: 1.01x faster                                                          |
| tornado_http               | 99.5 ms                                                                     | 98.6 ms: 1.01x faster                                                          |
| python_startup             | 24.4 ms                                                                     | 24.2 ms: 1.01x faster                                                          |
| json_loads                 | 14.4 us                                                                     | 14.3 us: 1.00x faster                                                          |
| unpickle_pure_python       | 144 us                                                                      | 145 us: 1.01x slower                                                           |
| bench_mp_pool              | 89.1 ms                                                                     | 89.9 ms: 1.01x slower                                                          |
| sqlglot_normalize          | 208 ms                                                                      | 210 ms: 1.01x slower                                                           |
| telco                      | 4.67 ms                                                                     | 4.72 ms: 1.01x slower                                                          |
| scimark_sparse_mat_mult    | 2.17 ms                                                                     | 2.20 ms: 1.01x slower                                                          |
| docutils                   | 1.91 sec                                                                    | 1.94 sec: 1.01x slower                                                         |
| sqlglot_optimize           | 43.3 ms                                                                     | 43.9 ms: 1.01x slower                                                          |
| pprint_pformat             | 928 ms                                                                      | 941 ms: 1.01x slower                                                           |
| async_generators           | 263 ms                                                                      | 267 ms: 1.01x slower                                                           |
| xml_etree_generate         | 50.5 ms                                                                     | 51.2 ms: 1.01x slower                                                          |
| dulwich_log                | 40.7 ms                                                                     | 41.3 ms: 1.02x slower                                                          |
| async_tree_io              | 542 ms                                                                      | 550 ms: 1.02x slower                                                           |
| nqueens                    | 63.7 ms                                                                     | 64.7 ms: 1.02x slower                                                          |
| regex_compile              | 91.2 ms                                                                     | 92.7 ms: 1.02x slower                                                          |
| sympy_str                  | 192 ms                                                                      | 195 ms: 1.02x slower                                                           |
| thrift                     | 513 us                                                                      | 521 us: 1.02x slower                                                           |
| sympy_expand               | 324 ms                                                                      | 330 ms: 1.02x slower                                                           |
| async_tree_cpu_io_mixed_tg | 399 ms                                                                      | 407 ms: 1.02x slower                                                           |
| pycparser                  | 730 ms                                                                      | 744 ms: 1.02x slower                                                           |
| async_tree_io_tg           | 631 ms                                                                      | 643 ms: 1.02x slower                                                           |
| scimark_monte_carlo        | 37.3 ms                                                                     | 38.0 ms: 1.02x slower                                                          |
| deepcopy_memo              | 16.5 us                                                                     | 16.9 us: 1.02x slower                                                          |
| xml_etree_process          | 35.8 ms                                                                     | 36.5 ms: 1.02x slower                                                          |
| json                       | 2.94 ms                                                                     | 3.01 ms: 1.02x slower                                                          |
| async_tree_none_tg         | 210 ms                                                                      | 215 ms: 1.02x slower                                                           |
| sympy_integrate            | 15.5 ms                                                                     | 15.8 ms: 1.02x slower                                                          |
| coverage                   | 46.6 ms                                                                     | 47.7 ms: 1.02x slower                                                          |
| float                      | 46.9 ms                                                                     | 48.1 ms: 1.03x slower                                                          |
| 2to3                       | 247 ms                                                                      | 253 ms: 1.03x slower                                                           |
| sqlglot_transpile          | 1.18 ms                                                                     | 1.21 ms: 1.03x slower                                                          |
| deltablue                  | 2.32 ms                                                                     | 2.38 ms: 1.03x slower                                                          |
| tomli_loads                | 1.28 sec                                                                    | 1.31 sec: 1.03x slower                                                         |
| sympy_sum                  | 103 ms                                                                      | 106 ms: 1.03x slower                                                           |
| comprehensions             | 11.8 us                                                                     | 12.1 us: 1.03x slower                                                          |
| richards_super             | 38.4 ms                                                                     | 39.5 ms: 1.03x slower                                                          |
| sqlglot_parse              | 903 us                                                                      | 931 us: 1.03x slower                                                           |
| scimark_fft                | 156 ms                                                                      | 161 ms: 1.03x slower                                                           |
| typing_runtime_protocols   | 114 us                                                                      | 118 us: 1.04x slower                                                           |
| genshi_text                | 19.2 ms                                                                     | 20.0 ms: 1.04x slower                                                          |
| meteor_contest             | 74.5 ms                                                                     | 77.5 ms: 1.04x slower                                                          |
| genshi_xml                 | 47.2 ms                                                                     | 49.1 ms: 1.04x slower                                                          |
| json_dumps                 | 6.22 ms                                                                     | 6.47 ms: 1.04x slower                                                          |
| regex_effbot               | 1.56 ms                                                                     | 1.63 ms: 1.04x slower                                                          |
| html5lib                   | 38.9 ms                                                                     | 40.6 ms: 1.04x slower                                                          |
| go                         | 90.0 ms                                                                     | 94.0 ms: 1.04x slower                                                          |
| pprint_safe_repr           | 450 ms                                                                      | 470 ms: 1.04x slower                                                           |
| crypto_pyaes               | 40.7 ms                                                                     | 42.5 ms: 1.05x slower                                                          |
| regex_dna                  | 116 ms                                                                      | 122 ms: 1.05x slower                                                           |
| mako                       | 4.96 ms                                                                     | 5.20 ms: 1.05x slower                                                          |
| chaos                      | 41.2 ms                                                                     | 43.3 ms: 1.05x slower                                                          |
| regex_v8                   | 14.7 ms                                                                     | 15.4 ms: 1.05x slower                                                          |
| richards                   | 33.7 ms                                                                     | 35.5 ms: 1.05x slower                                                          |
| hexiom                     | 5.15 ms                                                                     | 5.43 ms: 1.05x slower                                                          |
| coroutines                 | 13.6 ms                                                                     | 14.4 ms: 1.06x slower                                                          |
| fannkuch                   | 234 ms                                                                      | 248 ms: 1.06x slower                                                           |
| pyflate                    | 285 ms                                                                      | 303 ms: 1.06x slower                                                           |
| scimark_sor                | 62.9 ms                                                                     | 67.0 ms: 1.06x slower                                                          |
| logging_silent             | 52.3 ns                                                                     | 56.4 ns: 1.08x slower                                                          |
| scimark_lu                 | 52.8 ms                                                                     | 59.0 ms: 1.12x slower                                                          |
| Geometric mean             | (ref)                                                                       | 1.02x slower                                                                   |

Benchmark hidden because not significant (18): python_startup_no_site, xml_etree_parse, create_gc_cycles, spectral_norm, pickle_pure_python, deepcopy_reduce, pidigits, xml_etree_iterparse, gc_traversal, pathlib, bench_thread_pool, deepcopy, async_tree_cpu_io_mixed, pylint, sphinx, async_tree_memoization_tg, async_tree_memoization, async_tree_none

- Geometric mean (including insignificant results): 1.018x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown