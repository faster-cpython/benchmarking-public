# Results vs. base

- fork: brandtbucher
- ref: justin_no_externs
- machine: linux-x86_64
- commit hash: 64b198a
- commit date: 2024-10-25
- overall geometric mean: 1.011x slower
- HPT reliability: 99.97%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241022-pythonperf2-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 316 ms                                                                       | 318 ms: 1.00x slower                                                            |
| docutils       | 3.22 sec                                                                     | 3.21 sec: 1.00x faster                                                          |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                                    |

Benchmark hidden because not significant (3): html5lib, sphinx, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20241022-pythonperf2-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|--------------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| asyncio_websockets | 386 ms                                                                       | 381 ms: 1.01x faster                                                            |
| async_generators   | 384 ms                                                                       | 380 ms: 1.01x faster                                                            |
| async_tree_io_tg   | 872 ms                                                                       | 869 ms: 1.00x faster                                                            |
| async_tree_io      | 847 ms                                                                       | 855 ms: 1.01x slower                                                            |
| Geometric mean     | (ref)                                                                        | 1.00x slower                                                                    |

Benchmark hidden because not significant (7): async_tree_memoization_tg, coroutines, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241022-pythonperf2-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 79.9 ms                                                                      | 78.6 ms: 1.02x faster                                                           |
| nbody          | 83.8 ms                                                                      | 86.1 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241022-pythonperf2-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 146 ms                                                                       | 147 ms: 1.01x slower                                                            |
| regex_v8       | 25.4 ms                                                                      | 26.1 ms: 1.03x slower                                                           |
| regex_effbot   | 3.55 ms                                                                      | 3.66 ms: 1.03x slower                                                           |
| regex_dna      | 245 ms                                                                       | 256 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                                        | 1.03x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241022-pythonperf2-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_loads           | 24.5 us                                                                      | 24.7 us: 1.01x slower                                                           |
| xml_etree_generate   | 81.2 ms                                                                      | 81.9 ms: 1.01x slower                                                           |
| xml_etree_iterparse  | 99.0 ms                                                                      | 100.0 ms: 1.01x slower                                                          |
| json_dumps           | 11.2 ms                                                                      | 11.3 ms: 1.01x slower                                                           |
| xml_etree_parse      | 143 ms                                                                       | 146 ms: 1.02x slower                                                            |
| pickle_pure_python   | 336 us                                                                       | 349 us: 1.04x slower                                                            |
| tomli_loads          | 2.10 sec                                                                     | 2.18 sec: 1.04x slower                                                          |
| xml_etree_process    | 58.7 ms                                                                      | 61.0 ms: 1.04x slower                                                           |
| unpickle_pure_python | 218 us                                                                       | 227 us: 1.04x slower                                                            |
| Geometric mean       | (ref)                                                                        | 1.02x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241022-pythonperf2-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|------------------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 9.02 ms                                                                      | 9.05 ms: 1.00x slower                                                           |
| Geometric mean         | (ref)                                                                        | 1.00x slower                                                                    |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241022-pythonperf2-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml     | 68.2 ms                                                                      | 64.4 ms: 1.06x faster                                                           |
| genshi_text    | 29.2 ms                                                                      | 30.2 ms: 1.03x slower                                                           |
| mako           | 9.58 ms                                                                      | 9.98 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                                    |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20241022-pythonperf2-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|--------------------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| bench_mp_pool            | 3.18 sec                                                                     | 1.70 sec: 1.87x faster                                                          |
| genshi_xml               | 68.2 ms                                                                      | 64.4 ms: 1.06x faster                                                           |
| raytrace                 | 328 ms                                                                       | 312 ms: 1.05x faster                                                            |
| richards_super           | 54.4 ms                                                                      | 52.1 ms: 1.04x faster                                                           |
| thrift                   | 946 us                                                                       | 914 us: 1.04x faster                                                            |
| pycparser                | 1.29 sec                                                                     | 1.26 sec: 1.02x faster                                                          |
| logging_simple           | 6.76 us                                                                      | 6.63 us: 1.02x faster                                                           |
| sqlglot_parse            | 1.50 ms                                                                      | 1.47 ms: 1.02x faster                                                           |
| float                    | 79.9 ms                                                                      | 78.6 ms: 1.02x faster                                                           |
| sqlalchemy_declarative   | 170 ms                                                                       | 168 ms: 1.01x faster                                                            |
| asyncio_websockets       | 386 ms                                                                       | 381 ms: 1.01x faster                                                            |
| mdp                      | 2.67 sec                                                                     | 2.63 sec: 1.01x faster                                                          |
| sqlglot_transpile        | 1.98 ms                                                                      | 1.95 ms: 1.01x faster                                                           |
| logging_format           | 7.38 us                                                                      | 7.30 us: 1.01x faster                                                           |
| async_generators         | 384 ms                                                                       | 380 ms: 1.01x faster                                                            |
| docutils                 | 3.22 sec                                                                     | 3.21 sec: 1.00x faster                                                          |
| sympy_str                | 323 ms                                                                       | 322 ms: 1.00x faster                                                            |
| async_tree_io_tg         | 872 ms                                                                       | 869 ms: 1.00x faster                                                            |
| python_startup_no_site   | 9.02 ms                                                                      | 9.05 ms: 1.00x slower                                                           |
| 2to3                     | 316 ms                                                                       | 318 ms: 1.00x slower                                                            |
| sympy_integrate          | 27.4 ms                                                                      | 27.6 ms: 1.01x slower                                                           |
| regex_compile            | 146 ms                                                                       | 147 ms: 1.01x slower                                                            |
| deepcopy                 | 315 us                                                                       | 317 us: 1.01x slower                                                            |
| json_loads               | 24.5 us                                                                      | 24.7 us: 1.01x slower                                                           |
| async_tree_io            | 847 ms                                                                       | 855 ms: 1.01x slower                                                            |
| xml_etree_generate       | 81.2 ms                                                                      | 81.9 ms: 1.01x slower                                                           |
| xml_etree_iterparse      | 99.0 ms                                                                      | 100.0 ms: 1.01x slower                                                          |
| json_dumps               | 11.2 ms                                                                      | 11.3 ms: 1.01x slower                                                           |
| deepcopy_memo            | 29.9 us                                                                      | 30.3 us: 1.01x slower                                                           |
| meteor_contest           | 133 ms                                                                       | 135 ms: 1.01x slower                                                            |
| bench_thread_pool        | 945 us                                                                       | 961 us: 1.02x slower                                                            |
| pathlib                  | 15.8 ms                                                                      | 16.1 ms: 1.02x slower                                                           |
| sqlglot_normalize        | 133 ms                                                                       | 136 ms: 1.02x slower                                                            |
| xml_etree_parse          | 143 ms                                                                       | 146 ms: 1.02x slower                                                            |
| json                     | 5.07 ms                                                                      | 5.17 ms: 1.02x slower                                                           |
| deepcopy_reduce          | 3.09 us                                                                      | 3.17 us: 1.02x slower                                                           |
| logging_silent           | 97.8 ns                                                                      | 100 ns: 1.02x slower                                                            |
| typing_runtime_protocols | 182 us                                                                       | 186 us: 1.02x slower                                                            |
| chaos                    | 66.9 ms                                                                      | 68.6 ms: 1.03x slower                                                           |
| nbody                    | 83.8 ms                                                                      | 86.1 ms: 1.03x slower                                                           |
| regex_v8                 | 25.4 ms                                                                      | 26.1 ms: 1.03x slower                                                           |
| crypto_pyaes             | 73.0 ms                                                                      | 75.1 ms: 1.03x slower                                                           |
| scimark_fft              | 290 ms                                                                       | 299 ms: 1.03x slower                                                            |
| spectral_norm            | 93.4 ms                                                                      | 96.2 ms: 1.03x slower                                                           |
| regex_effbot             | 3.55 ms                                                                      | 3.66 ms: 1.03x slower                                                           |
| go                       | 152 ms                                                                       | 157 ms: 1.03x slower                                                            |
| fannkuch                 | 369 ms                                                                       | 381 ms: 1.03x slower                                                            |
| deltablue                | 3.30 ms                                                                      | 3.41 ms: 1.03x slower                                                           |
| genshi_text              | 29.2 ms                                                                      | 30.2 ms: 1.03x slower                                                           |
| generators               | 39.2 ms                                                                      | 40.6 ms: 1.04x slower                                                           |
| pyflate                  | 477 ms                                                                       | 494 ms: 1.04x slower                                                            |
| bpe_tokeniser            | 4.74 sec                                                                     | 4.92 sec: 1.04x slower                                                          |
| pickle_pure_python       | 336 us                                                                       | 349 us: 1.04x slower                                                            |
| tomli_loads              | 2.10 sec                                                                     | 2.18 sec: 1.04x slower                                                          |
| hexiom                   | 7.23 ms                                                                      | 7.51 ms: 1.04x slower                                                           |
| xml_etree_process        | 58.7 ms                                                                      | 61.0 ms: 1.04x slower                                                           |
| telco                    | 7.68 ms                                                                      | 7.99 ms: 1.04x slower                                                           |
| mako                     | 9.58 ms                                                                      | 9.98 ms: 1.04x slower                                                           |
| unpickle_pure_python     | 218 us                                                                       | 227 us: 1.04x slower                                                            |
| regex_dna                | 245 ms                                                                       | 256 ms: 1.04x slower                                                            |
| scimark_lu               | 94.4 ms                                                                      | 98.7 ms: 1.05x slower                                                           |
| nqueens                  | 101 ms                                                                       | 106 ms: 1.05x slower                                                            |
| comprehensions           | 19.0 us                                                                      | 19.9 us: 1.05x slower                                                           |
| coverage                 | 79.1 ms                                                                      | 83.5 ms: 1.05x slower                                                           |
| scimark_monte_carlo      | 68.1 ms                                                                      | 73.6 ms: 1.08x slower                                                           |
| scimark_sor              | 104 ms                                                                       | 120 ms: 1.16x slower                                                            |
| Geometric mean           | (ref)                                                                        | 1.01x slower                                                                    |

Benchmark hidden because not significant (25): tornado_http, sqlalchemy_imperative, django_template, create_gc_cycles, pylint, async_tree_memoization_tg, sympy_sum, python_startup, sympy_expand, pidigits, gc_traversal, scimark_sparse_mat_mult, dulwich_log, pprint_pformat, coroutines, sqlglot_optimize, html5lib, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_none, sphinx, pprint_safe_repr, richards

- Geometric mean (including insignificant results): 1.011x slower
# HPT report

- Reliability score: 99.97% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x