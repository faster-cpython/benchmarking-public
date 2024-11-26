# Results vs. base

- fork: brandtbucher
- ref: justin_no_externs
- machine: linux-x86_64
- commit hash: 9698931
- commit date: 2024-10-24
- overall geometric mean: 1.063x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241022-pythonperf2-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 316 ms                                                                       | 335 ms: 1.06x slower                                                            |
| docutils       | 3.22 sec                                                                     | 3.25 sec: 1.01x slower                                                          |
| html5lib       | 71.4 ms                                                                      | 73.9 ms: 1.04x slower                                                           |
| sphinx         | 1.27 sec                                                                     | 1.30 sec: 1.03x slower                                                          |
| Geometric mean | (ref)                                                                        | 1.03x slower                                                                    |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241022-pythonperf2-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| coroutines                 | 21.2 ms                                                                      | 21.3 ms: 1.00x slower                                                           |
| async_tree_io_tg           | 872 ms                                                                       | 878 ms: 1.01x slower                                                            |
| async_tree_cpu_io_mixed_tg | 566 ms                                                                       | 575 ms: 1.02x slower                                                            |
| async_generators           | 384 ms                                                                       | 390 ms: 1.02x slower                                                            |
| async_tree_memoization_tg  | 380 ms                                                                       | 389 ms: 1.02x slower                                                            |
| async_tree_io              | 847 ms                                                                       | 868 ms: 1.02x slower                                                            |
| async_tree_none_tg         | 325 ms                                                                       | 333 ms: 1.03x slower                                                            |
| async_tree_cpu_io_mixed    | 580 ms                                                                       | 598 ms: 1.03x slower                                                            |
| async_tree_memoization     | 414 ms                                                                       | 430 ms: 1.04x slower                                                            |
| async_tree_none            | 342 ms                                                                       | 358 ms: 1.05x slower                                                            |
| Geometric mean             | (ref)                                                                        | 1.02x slower                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241022-pythonperf2-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 251 ms                                                                       | 253 ms: 1.01x slower                                                            |
| nbody          | 83.8 ms                                                                      | 101 ms: 1.21x slower                                                            |
| Geometric mean | (ref)                                                                        | 1.07x slower                                                                    |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241022-pythonperf2-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.55 ms                                                                      | 3.65 ms: 1.03x slower                                                           |
| regex_v8       | 25.4 ms                                                                      | 26.3 ms: 1.04x slower                                                           |
| regex_compile  | 146 ms                                                                       | 157 ms: 1.08x slower                                                            |
| Geometric mean | (ref)                                                                        | 1.04x slower                                                                    |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241022-pythonperf2-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 99.0 ms                                                                      | 100 ms: 1.01x slower                                                            |
| xml_etree_parse      | 143 ms                                                                       | 146 ms: 1.02x slower                                                            |
| json_loads           | 24.5 us                                                                      | 25.4 us: 1.04x slower                                                           |
| json_dumps           | 11.2 ms                                                                      | 11.8 ms: 1.06x slower                                                           |
| xml_etree_generate   | 81.2 ms                                                                      | 87.7 ms: 1.08x slower                                                           |
| unpickle_pure_python | 218 us                                                                       | 236 us: 1.09x slower                                                            |
| tomli_loads          | 2.10 sec                                                                     | 2.29 sec: 1.09x slower                                                          |
| xml_etree_process    | 58.7 ms                                                                      | 64.8 ms: 1.10x slower                                                           |
| pickle_pure_python   | 336 us                                                                       | 375 us: 1.12x slower                                                            |
| Geometric mean       | (ref)                                                                        | 1.07x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241022-pythonperf2-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|------------------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.9 ms                                                                      | 14.9 ms: 1.00x faster                                                           |
| python_startup_no_site | 9.02 ms                                                                      | 9.01 ms: 1.00x faster                                                           |
| Geometric mean         | (ref)                                                                        | 1.00x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241022-pythonperf2-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|-----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 42.4 ms                                                                      | 44.4 ms: 1.05x slower                                                           |
| mako            | 9.58 ms                                                                      | 10.3 ms: 1.07x slower                                                           |
| genshi_text     | 29.2 ms                                                                      | 32.6 ms: 1.12x slower                                                           |
| Geometric mean  | (ref)                                                                        | 1.06x slower                                                                    |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241022-pythonperf2-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| gc_traversal               | 5.51 ms                                                                      | 5.36 ms: 1.03x faster                                                           |
| thrift                     | 946 us                                                                       | 925 us: 1.02x faster                                                            |
| logging_format             | 7.38 us                                                                      | 7.31 us: 1.01x faster                                                           |
| logging_simple             | 6.76 us                                                                      | 6.72 us: 1.01x faster                                                           |
| create_gc_cycles           | 2.90 ms                                                                      | 2.88 ms: 1.00x faster                                                           |
| python_startup             | 14.9 ms                                                                      | 14.9 ms: 1.00x faster                                                           |
| python_startup_no_site     | 9.02 ms                                                                      | 9.01 ms: 1.00x faster                                                           |
| mdp                        | 2.67 sec                                                                     | 2.67 sec: 1.00x slower                                                          |
| coroutines                 | 21.2 ms                                                                      | 21.3 ms: 1.00x slower                                                           |
| pidigits                   | 251 ms                                                                       | 253 ms: 1.01x slower                                                            |
| async_tree_io_tg           | 872 ms                                                                       | 878 ms: 1.01x slower                                                            |
| docutils                   | 3.22 sec                                                                     | 3.25 sec: 1.01x slower                                                          |
| xml_etree_iterparse        | 99.0 ms                                                                      | 100 ms: 1.01x slower                                                            |
| async_tree_cpu_io_mixed_tg | 566 ms                                                                       | 575 ms: 1.02x slower                                                            |
| sympy_sum                  | 176 ms                                                                       | 179 ms: 1.02x slower                                                            |
| async_generators           | 384 ms                                                                       | 390 ms: 1.02x slower                                                            |
| raytrace                   | 328 ms                                                                       | 335 ms: 1.02x slower                                                            |
| coverage                   | 79.1 ms                                                                      | 80.8 ms: 1.02x slower                                                           |
| xml_etree_parse            | 143 ms                                                                       | 146 ms: 1.02x slower                                                            |
| async_tree_memoization_tg  | 380 ms                                                                       | 389 ms: 1.02x slower                                                            |
| async_tree_io              | 847 ms                                                                       | 868 ms: 1.02x slower                                                            |
| sphinx                     | 1.27 sec                                                                     | 1.30 sec: 1.03x slower                                                          |
| async_tree_none_tg         | 325 ms                                                                       | 333 ms: 1.03x slower                                                            |
| sympy_expand               | 535 ms                                                                       | 549 ms: 1.03x slower                                                            |
| dulwich_log                | 62.6 ms                                                                      | 64.4 ms: 1.03x slower                                                           |
| regex_effbot               | 3.55 ms                                                                      | 3.65 ms: 1.03x slower                                                           |
| async_tree_cpu_io_mixed    | 580 ms                                                                       | 598 ms: 1.03x slower                                                            |
| pathlib                    | 15.8 ms                                                                      | 16.3 ms: 1.03x slower                                                           |
| sympy_str                  | 323 ms                                                                       | 334 ms: 1.03x slower                                                            |
| sympy_integrate            | 27.4 ms                                                                      | 28.4 ms: 1.04x slower                                                           |
| regex_v8                   | 25.4 ms                                                                      | 26.3 ms: 1.04x slower                                                           |
| html5lib                   | 71.4 ms                                                                      | 73.9 ms: 1.04x slower                                                           |
| sqlglot_transpile          | 1.98 ms                                                                      | 2.05 ms: 1.04x slower                                                           |
| sqlglot_parse              | 1.50 ms                                                                      | 1.56 ms: 1.04x slower                                                           |
| json_loads                 | 24.5 us                                                                      | 25.4 us: 1.04x slower                                                           |
| async_tree_memoization     | 414 ms                                                                       | 430 ms: 1.04x slower                                                            |
| bench_thread_pool          | 945 us                                                                       | 984 us: 1.04x slower                                                            |
| scimark_lu                 | 94.4 ms                                                                      | 98.3 ms: 1.04x slower                                                           |
| async_tree_none            | 342 ms                                                                       | 358 ms: 1.05x slower                                                            |
| django_template            | 42.4 ms                                                                      | 44.4 ms: 1.05x slower                                                           |
| json                       | 5.07 ms                                                                      | 5.34 ms: 1.05x slower                                                           |
| json_dumps                 | 11.2 ms                                                                      | 11.8 ms: 1.06x slower                                                           |
| pycparser                  | 1.29 sec                                                                     | 1.36 sec: 1.06x slower                                                          |
| 2to3                       | 316 ms                                                                       | 335 ms: 1.06x slower                                                            |
| sqlglot_optimize           | 69.7 ms                                                                      | 73.9 ms: 1.06x slower                                                           |
| logging_silent             | 97.8 ns                                                                      | 104 ns: 1.07x slower                                                            |
| spectral_norm              | 93.4 ms                                                                      | 100 ms: 1.07x slower                                                            |
| sqlglot_normalize          | 133 ms                                                                       | 143 ms: 1.07x slower                                                            |
| mako                       | 9.58 ms                                                                      | 10.3 ms: 1.07x slower                                                           |
| regex_compile              | 146 ms                                                                       | 157 ms: 1.08x slower                                                            |
| deepcopy_memo              | 29.9 us                                                                      | 32.3 us: 1.08x slower                                                           |
| xml_etree_generate         | 81.2 ms                                                                      | 87.7 ms: 1.08x slower                                                           |
| unpickle_pure_python       | 218 us                                                                       | 236 us: 1.09x slower                                                            |
| deltablue                  | 3.30 ms                                                                      | 3.58 ms: 1.09x slower                                                           |
| telco                      | 7.68 ms                                                                      | 8.37 ms: 1.09x slower                                                           |
| bpe_tokeniser              | 4.74 sec                                                                     | 5.17 sec: 1.09x slower                                                          |
| scimark_sparse_mat_mult    | 4.41 ms                                                                      | 4.81 ms: 1.09x slower                                                           |
| tomli_loads                | 2.10 sec                                                                     | 2.29 sec: 1.09x slower                                                          |
| typing_runtime_protocols   | 182 us                                                                       | 200 us: 1.10x slower                                                            |
| xml_etree_process          | 58.7 ms                                                                      | 64.8 ms: 1.10x slower                                                           |
| meteor_contest             | 133 ms                                                                       | 148 ms: 1.11x slower                                                            |
| deepcopy                   | 315 us                                                                       | 350 us: 1.11x slower                                                            |
| genshi_text                | 29.2 ms                                                                      | 32.6 ms: 1.12x slower                                                           |
| scimark_fft                | 290 ms                                                                       | 324 ms: 1.12x slower                                                            |
| pickle_pure_python         | 336 us                                                                       | 375 us: 1.12x slower                                                            |
| deepcopy_reduce            | 3.09 us                                                                      | 3.47 us: 1.12x slower                                                           |
| generators                 | 39.2 ms                                                                      | 44.3 ms: 1.13x slower                                                           |
| pyflate                    | 477 ms                                                                       | 548 ms: 1.15x slower                                                            |
| richards_super             | 54.4 ms                                                                      | 64.3 ms: 1.18x slower                                                           |
| crypto_pyaes               | 73.0 ms                                                                      | 86.7 ms: 1.19x slower                                                           |
| go                         | 152 ms                                                                       | 181 ms: 1.19x slower                                                            |
| scimark_sor                | 104 ms                                                                       | 124 ms: 1.19x slower                                                            |
| comprehensions             | 19.0 us                                                                      | 22.7 us: 1.19x slower                                                           |
| nqueens                    | 101 ms                                                                       | 121 ms: 1.20x slower                                                            |
| chaos                      | 66.9 ms                                                                      | 80.3 ms: 1.20x slower                                                           |
| pprint_pformat             | 1.66 sec                                                                     | 1.99 sec: 1.20x slower                                                          |
| pprint_safe_repr           | 805 ms                                                                       | 967 ms: 1.20x slower                                                            |
| nbody                      | 83.8 ms                                                                      | 101 ms: 1.21x slower                                                            |
| hexiom                     | 7.23 ms                                                                      | 8.92 ms: 1.23x slower                                                           |
| richards                   | 48.2 ms                                                                      | 60.1 ms: 1.25x slower                                                           |
| fannkuch                   | 369 ms                                                                       | 461 ms: 1.25x slower                                                            |
| scimark_monte_carlo        | 68.1 ms                                                                      | 87.4 ms: 1.28x slower                                                           |
| Geometric mean             | (ref)                                                                        | 1.06x slower                                                                    |

Benchmark hidden because not significant (9): bench_mp_pool, asyncio_websockets, sqlalchemy_declarative, genshi_xml, sqlalchemy_imperative, regex_dna, float, tornado_http, pylint

- Geometric mean (including insignificant results): 1.063x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.00x