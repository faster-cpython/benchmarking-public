# Results vs. base

- fork: brandtbucher
- ref: justin_no_externs
- machine: linux-x86_64
- commit hash: 5791853
- commit date: 2024-10-25
- overall geometric mean: 1.010x slower
- HPT reliability: 97.40%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241022-pythonperf2-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 316 ms                                                                       | 318 ms: 1.01x slower                                                            |
| docutils       | 3.22 sec                                                                     | 3.20 sec: 1.01x faster                                                          |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                                    |

Benchmark hidden because not significant (3): html5lib, sphinx, tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (11): asyncio_websockets, async_tree_io, async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, coroutines, async_tree_cpu_io_mixed_tg, async_generators, async_tree_io_tg, async_tree_memoization, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241022-pythonperf2-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 251 ms                                                                       | 252 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                                    |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241022-pythonperf2-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 25.4 ms                                                                      | 25.9 ms: 1.02x slower                                                           |
| regex_dna      | 245 ms                                                                       | 253 ms: 1.03x slower                                                            |
| regex_effbot   | 3.55 ms                                                                      | 3.70 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                                        | 1.02x slower                                                                    |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241022-pythonperf2-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 143 ms                                                                       | 144 ms: 1.01x slower                                                            |
| xml_etree_iterparse  | 99.0 ms                                                                      | 99.8 ms: 1.01x slower                                                           |
| json_dumps           | 11.2 ms                                                                      | 11.3 ms: 1.01x slower                                                           |
| tomli_loads          | 2.10 sec                                                                     | 2.14 sec: 1.02x slower                                                          |
| unpickle_pure_python | 218 us                                                                       | 225 us: 1.03x slower                                                            |
| Geometric mean       | (ref)                                                                        | 1.01x slower                                                                    |

Benchmark hidden because not significant (4): xml_etree_generate, xml_etree_process, json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241022-pythonperf2-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup | 14.9 ms                                                                      | 14.8 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                                    |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241022-pythonperf2-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|-----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 68.2 ms                                                                      | 65.8 ms: 1.04x faster                                                           |
| mako            | 9.58 ms                                                                      | 9.65 ms: 1.01x slower                                                           |
| django_template | 42.4 ms                                                                      | 44.0 ms: 1.04x slower                                                           |
| genshi_text     | 29.2 ms                                                                      | 30.8 ms: 1.05x slower                                                           |
| Geometric mean  | (ref)                                                                        | 1.02x slower                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20241022-pythonperf2-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|--------------------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| bench_mp_pool            | 3.18 sec                                                                     | 1.90 sec: 1.67x faster                                                          |
| genshi_xml               | 68.2 ms                                                                      | 65.8 ms: 1.04x faster                                                           |
| scimark_sparse_mat_mult  | 4.41 ms                                                                      | 4.25 ms: 1.04x faster                                                           |
| richards                 | 48.2 ms                                                                      | 46.5 ms: 1.04x faster                                                           |
| pycparser                | 1.29 sec                                                                     | 1.26 sec: 1.02x faster                                                          |
| thrift                   | 946 us                                                                       | 930 us: 1.02x faster                                                            |
| coverage                 | 79.1 ms                                                                      | 78.1 ms: 1.01x faster                                                           |
| pprint_pformat           | 1.66 sec                                                                     | 1.63 sec: 1.01x faster                                                          |
| raytrace                 | 328 ms                                                                       | 324 ms: 1.01x faster                                                            |
| sympy_sum                | 176 ms                                                                       | 174 ms: 1.01x faster                                                            |
| sympy_str                | 323 ms                                                                       | 321 ms: 1.01x faster                                                            |
| sqlalchemy_declarative   | 170 ms                                                                       | 169 ms: 1.01x faster                                                            |
| mdp                      | 2.67 sec                                                                     | 2.65 sec: 1.01x faster                                                          |
| docutils                 | 3.22 sec                                                                     | 3.20 sec: 1.01x faster                                                          |
| python_startup           | 14.9 ms                                                                      | 14.8 ms: 1.01x faster                                                           |
| sympy_expand             | 535 ms                                                                       | 532 ms: 1.00x faster                                                            |
| pidigits                 | 251 ms                                                                       | 252 ms: 1.00x slower                                                            |
| gc_traversal             | 5.51 ms                                                                      | 5.53 ms: 1.00x slower                                                           |
| xml_etree_parse          | 143 ms                                                                       | 144 ms: 1.01x slower                                                            |
| 2to3                     | 316 ms                                                                       | 318 ms: 1.01x slower                                                            |
| logging_simple           | 6.76 us                                                                      | 6.80 us: 1.01x slower                                                           |
| sqlglot_normalize        | 133 ms                                                                       | 134 ms: 1.01x slower                                                            |
| mako                     | 9.58 ms                                                                      | 9.65 ms: 1.01x slower                                                           |
| logging_format           | 7.38 us                                                                      | 7.44 us: 1.01x slower                                                           |
| xml_etree_iterparse      | 99.0 ms                                                                      | 99.8 ms: 1.01x slower                                                           |
| json_dumps               | 11.2 ms                                                                      | 11.3 ms: 1.01x slower                                                           |
| deepcopy_reduce          | 3.09 us                                                                      | 3.13 us: 1.01x slower                                                           |
| deepcopy                 | 315 us                                                                       | 320 us: 1.02x slower                                                            |
| spectral_norm            | 93.4 ms                                                                      | 94.9 ms: 1.02x slower                                                           |
| regex_v8                 | 25.4 ms                                                                      | 25.9 ms: 1.02x slower                                                           |
| pathlib                  | 15.8 ms                                                                      | 16.1 ms: 1.02x slower                                                           |
| tomli_loads              | 2.10 sec                                                                     | 2.14 sec: 1.02x slower                                                          |
| deltablue                | 3.30 ms                                                                      | 3.36 ms: 1.02x slower                                                           |
| bpe_tokeniser            | 4.74 sec                                                                     | 4.87 sec: 1.03x slower                                                          |
| comprehensions           | 19.0 us                                                                      | 19.5 us: 1.03x slower                                                           |
| scimark_lu               | 94.4 ms                                                                      | 97.0 ms: 1.03x slower                                                           |
| json                     | 5.07 ms                                                                      | 5.21 ms: 1.03x slower                                                           |
| deepcopy_memo            | 29.9 us                                                                      | 30.8 us: 1.03x slower                                                           |
| meteor_contest           | 133 ms                                                                       | 137 ms: 1.03x slower                                                            |
| pyflate                  | 477 ms                                                                       | 491 ms: 1.03x slower                                                            |
| regex_dna                | 245 ms                                                                       | 253 ms: 1.03x slower                                                            |
| unpickle_pure_python     | 218 us                                                                       | 225 us: 1.03x slower                                                            |
| hexiom                   | 7.23 ms                                                                      | 7.46 ms: 1.03x slower                                                           |
| chaos                    | 66.9 ms                                                                      | 69.4 ms: 1.04x slower                                                           |
| django_template          | 42.4 ms                                                                      | 44.0 ms: 1.04x slower                                                           |
| regex_effbot             | 3.55 ms                                                                      | 3.70 ms: 1.04x slower                                                           |
| telco                    | 7.68 ms                                                                      | 8.02 ms: 1.04x slower                                                           |
| nqueens                  | 101 ms                                                                       | 106 ms: 1.04x slower                                                            |
| typing_runtime_protocols | 182 us                                                                       | 190 us: 1.04x slower                                                            |
| go                       | 152 ms                                                                       | 159 ms: 1.05x slower                                                            |
| logging_silent           | 97.8 ns                                                                      | 103 ns: 1.05x slower                                                            |
| genshi_text              | 29.2 ms                                                                      | 30.8 ms: 1.05x slower                                                           |
| fannkuch                 | 369 ms                                                                       | 389 ms: 1.06x slower                                                            |
| crypto_pyaes             | 73.0 ms                                                                      | 77.3 ms: 1.06x slower                                                           |
| scimark_monte_carlo      | 68.1 ms                                                                      | 72.2 ms: 1.06x slower                                                           |
| scimark_sor              | 104 ms                                                                       | 117 ms: 1.13x slower                                                            |
| Geometric mean           | (ref)                                                                        | 1.00x slower                                                                    |

Benchmark hidden because not significant (35): sqlalchemy_imperative, float, nbody, sqlglot_parse, asyncio_websockets, pprint_safe_repr, sqlglot_transpile, richards_super, html5lib, async_tree_io, async_tree_none_tg, sphinx, async_tree_memoization_tg, sqlglot_optimize, async_tree_cpu_io_mixed, python_startup_no_site, create_gc_cycles, xml_etree_generate, regex_compile, coroutines, async_tree_cpu_io_mixed_tg, xml_etree_process, async_generators, sympy_integrate, async_tree_io_tg, pylint, generators, async_tree_memoization, json_loads, dulwich_log, async_tree_none, scimark_fft, pickle_pure_python, tornado_http, bench_thread_pool

- Geometric mean (including insignificant results): 1.010x slower
# HPT report

- Reliability score: 97.40% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x