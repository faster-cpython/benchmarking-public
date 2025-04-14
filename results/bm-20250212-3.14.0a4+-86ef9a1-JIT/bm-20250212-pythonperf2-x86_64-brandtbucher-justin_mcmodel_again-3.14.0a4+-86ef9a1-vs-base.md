# Results vs. base

- fork: brandtbucher
- ref: justin_mcmodel_again
- machine: linux-x86_64
- commit hash: 86ef9a1
- commit date: 2025-02-12
- overall geometric mean: 1.010x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250209-pythonperf2-x86_64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250212-pythonperf2-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 290 ms                                                                       | 287 ms: 1.01x faster                                                               |
| docutils       | 2.95 sec                                                                     | 2.93 sec: 1.01x faster                                                             |
| html5lib       | 67.3 ms                                                                      | 67.8 ms: 1.01x slower                                                              |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                                       |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20250209-pythonperf2-x86_64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250212-pythonperf2-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|--------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| asyncio_websockets | 395 ms                                                                       | 387 ms: 1.02x faster                                                               |
| coroutines         | 21.0 ms                                                                      | 21.0 ms: 1.00x faster                                                              |
| async_generators   | 433 ms                                                                       | 448 ms: 1.04x slower                                                               |
| Geometric mean     | (ref)                                                                        | 1.00x slower                                                                       |

Benchmark hidden because not significant (8): async_tree_io_tg, async_tree_io, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none, async_tree_memoization_tg, async_tree_none_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250209-pythonperf2-x86_64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250212-pythonperf2-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| nbody          | 103 ms                                                                       | 89.9 ms: 1.15x faster                                                              |
| float          | 72.3 ms                                                                      | 70.0 ms: 1.03x faster                                                              |
| Geometric mean | (ref)                                                                        | 1.06x faster                                                                       |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250209-pythonperf2-x86_64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250212-pythonperf2-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                       | 136 ms: 1.00x faster                                                               |
| regex_dna      | 237 ms                                                                       | 243 ms: 1.02x slower                                                               |
| regex_v8       | 25.3 ms                                                                      | 26.8 ms: 1.06x slower                                                              |
| Geometric mean | (ref)                                                                        | 1.02x slower                                                                       |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250209-pythonperf2-x86_64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250212-pythonperf2-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| unpickle_pure_python | 204 us                                                                       | 198 us: 1.03x faster                                                               |
| tomli_loads          | 2.04 sec                                                                     | 2.00 sec: 1.02x faster                                                             |
| json_dumps           | 11.9 ms                                                                      | 11.7 ms: 1.02x faster                                                              |
| pickle_pure_python   | 333 us                                                                       | 328 us: 1.01x faster                                                               |
| xml_etree_process    | 56.5 ms                                                                      | 55.7 ms: 1.01x faster                                                              |
| xml_etree_generate   | 79.7 ms                                                                      | 79.1 ms: 1.01x faster                                                              |
| xml_etree_iterparse  | 96.2 ms                                                                      | 97.3 ms: 1.01x slower                                                              |
| xml_etree_parse      | 134 ms                                                                       | 141 ms: 1.05x slower                                                               |
| Geometric mean       | (ref)                                                                        | 1.00x faster                                                                       |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250209-pythonperf2-x86_64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250212-pythonperf2-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup | 16.1 ms                                                                      | 16.1 ms: 1.00x faster                                                              |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                                       |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250209-pythonperf2-x86_64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250212-pythonperf2-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|-----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 9.70 ms                                                                      | 9.40 ms: 1.03x faster                                                              |
| genshi_text     | 24.3 ms                                                                      | 23.8 ms: 1.02x faster                                                              |
| django_template | 36.8 ms                                                                      | 36.2 ms: 1.02x faster                                                              |
| genshi_xml      | 54.9 ms                                                                      | 54.3 ms: 1.01x faster                                                              |
| Geometric mean  | (ref)                                                                        | 1.02x faster                                                                       |

All benchmarks:
===============

| Benchmark                | bm-20250209-pythonperf2-x86_64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250212-pythonperf2-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|--------------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| nbody                    | 103 ms                                                                       | 89.9 ms: 1.15x faster                                                              |
| comprehensions           | 19.6 us                                                                      | 18.5 us: 1.06x faster                                                              |
| crypto_pyaes             | 78.2 ms                                                                      | 74.5 ms: 1.05x faster                                                              |
| pprint_pformat           | 1.66 sec                                                                     | 1.59 sec: 1.05x faster                                                             |
| pprint_safe_repr         | 816 ms                                                                       | 783 ms: 1.04x faster                                                               |
| pycparser                | 1.25 sec                                                                     | 1.20 sec: 1.04x faster                                                             |
| typing_runtime_protocols | 178 us                                                                       | 171 us: 1.04x faster                                                               |
| thrift                   | 882 us                                                                       | 851 us: 1.04x faster                                                               |
| coverage                 | 81.4 ms                                                                      | 78.5 ms: 1.04x faster                                                              |
| deltablue                | 3.55 ms                                                                      | 3.42 ms: 1.04x faster                                                              |
| hexiom                   | 7.03 ms                                                                      | 6.80 ms: 1.03x faster                                                              |
| sqlglot_parse            | 1.40 ms                                                                      | 1.36 ms: 1.03x faster                                                              |
| float                    | 72.3 ms                                                                      | 70.0 ms: 1.03x faster                                                              |
| mako                     | 9.70 ms                                                                      | 9.40 ms: 1.03x faster                                                              |
| unpickle_pure_python     | 204 us                                                                       | 198 us: 1.03x faster                                                               |
| sqlglot_transpile        | 1.80 ms                                                                      | 1.75 ms: 1.03x faster                                                              |
| fannkuch                 | 383 ms                                                                       | 374 ms: 1.02x faster                                                               |
| go                       | 147 ms                                                                       | 143 ms: 1.02x faster                                                               |
| deepcopy                 | 287 us                                                                       | 280 us: 1.02x faster                                                               |
| nqueens                  | 99.5 ms                                                                      | 97.4 ms: 1.02x faster                                                              |
| scimark_monte_carlo      | 62.2 ms                                                                      | 61.0 ms: 1.02x faster                                                              |
| asyncio_websockets       | 395 ms                                                                       | 387 ms: 1.02x faster                                                               |
| pathlib                  | 16.7 ms                                                                      | 16.4 ms: 1.02x faster                                                              |
| genshi_text              | 24.3 ms                                                                      | 23.8 ms: 1.02x faster                                                              |
| logging_simple           | 6.35 us                                                                      | 6.23 us: 1.02x faster                                                              |
| tomli_loads              | 2.04 sec                                                                     | 2.00 sec: 1.02x faster                                                             |
| k_core                   | 2.06 sec                                                                     | 2.03 sec: 1.02x faster                                                             |
| json_dumps               | 11.9 ms                                                                      | 11.7 ms: 1.02x faster                                                              |
| sympy_expand             | 514 ms                                                                       | 505 ms: 1.02x faster                                                               |
| django_template          | 36.8 ms                                                                      | 36.2 ms: 1.02x faster                                                              |
| logging_format           | 6.91 us                                                                      | 6.80 us: 1.02x faster                                                              |
| shortest_path            | 437 ms                                                                       | 430 ms: 1.02x faster                                                               |
| pickle_pure_python       | 333 us                                                                       | 328 us: 1.01x faster                                                               |
| generators               | 29.1 ms                                                                      | 28.7 ms: 1.01x faster                                                              |
| sqlalchemy_imperative    | 18.3 ms                                                                      | 18.1 ms: 1.01x faster                                                              |
| telco                    | 7.69 ms                                                                      | 7.59 ms: 1.01x faster                                                              |
| xml_etree_process        | 56.5 ms                                                                      | 55.7 ms: 1.01x faster                                                              |
| sympy_str                | 300 ms                                                                       | 296 ms: 1.01x faster                                                               |
| deepcopy_reduce          | 2.95 us                                                                      | 2.92 us: 1.01x faster                                                              |
| bpe_tokeniser            | 4.66 sec                                                                     | 4.60 sec: 1.01x faster                                                             |
| dulwich_log              | 67.4 ms                                                                      | 66.6 ms: 1.01x faster                                                              |
| 2to3                     | 290 ms                                                                       | 287 ms: 1.01x faster                                                               |
| sqlalchemy_declarative   | 147 ms                                                                       | 145 ms: 1.01x faster                                                               |
| scimark_fft              | 306 ms                                                                       | 303 ms: 1.01x faster                                                               |
| genshi_xml               | 54.9 ms                                                                      | 54.3 ms: 1.01x faster                                                              |
| sympy_sum                | 156 ms                                                                       | 154 ms: 1.01x faster                                                               |
| many_optionals           | 1.03 ms                                                                      | 1.02 ms: 1.01x faster                                                              |
| sympy_integrate          | 23.8 ms                                                                      | 23.6 ms: 1.01x faster                                                              |
| xml_etree_generate       | 79.7 ms                                                                      | 79.1 ms: 1.01x faster                                                              |
| sqlglot_optimize         | 60.1 ms                                                                      | 59.7 ms: 1.01x faster                                                              |
| docutils                 | 2.95 sec                                                                     | 2.93 sec: 1.01x faster                                                             |
| connected_components     | 405 ms                                                                       | 402 ms: 1.01x faster                                                               |
| regex_compile            | 137 ms                                                                       | 136 ms: 1.00x faster                                                               |
| meteor_contest           | 133 ms                                                                       | 133 ms: 1.00x faster                                                               |
| coroutines               | 21.0 ms                                                                      | 21.0 ms: 1.00x faster                                                              |
| python_startup           | 16.1 ms                                                                      | 16.1 ms: 1.00x faster                                                              |
| subparsers               | 22.9 ms                                                                      | 23.1 ms: 1.01x slower                                                              |
| html5lib                 | 67.3 ms                                                                      | 67.8 ms: 1.01x slower                                                              |
| deepcopy_memo            | 29.2 us                                                                      | 29.5 us: 1.01x slower                                                              |
| richards                 | 45.1 ms                                                                      | 45.5 ms: 1.01x slower                                                              |
| mdp                      | 2.56 sec                                                                     | 2.58 sec: 1.01x slower                                                             |
| xml_etree_iterparse      | 96.2 ms                                                                      | 97.3 ms: 1.01x slower                                                              |
| logging_silent           | 96.8 ns                                                                      | 98.0 ns: 1.01x slower                                                              |
| chaos                    | 60.9 ms                                                                      | 61.7 ms: 1.01x slower                                                              |
| scimark_lu               | 95.2 ms                                                                      | 96.6 ms: 1.01x slower                                                              |
| scimark_sor              | 109 ms                                                                       | 111 ms: 1.02x slower                                                               |
| regex_dna                | 237 ms                                                                       | 243 ms: 1.02x slower                                                               |
| create_gc_cycles         | 2.66 ms                                                                      | 2.75 ms: 1.04x slower                                                              |
| async_generators         | 433 ms                                                                       | 448 ms: 1.04x slower                                                               |
| gc_traversal             | 6.25 ms                                                                      | 6.52 ms: 1.04x slower                                                              |
| xml_etree_parse          | 134 ms                                                                       | 141 ms: 1.05x slower                                                               |
| regex_v8                 | 25.3 ms                                                                      | 26.8 ms: 1.06x slower                                                              |
| Geometric mean           | (ref)                                                                        | 1.01x faster                                                                       |

Benchmark hidden because not significant (24): bench_mp_pool, pylint, async_tree_io_tg, bench_thread_pool, json, pyflate, sphinx, richards_super, spectral_norm, json_loads, async_tree_io, async_tree_cpu_io_mixed, python_startup_no_site, pidigits, sqlglot_normalize, async_tree_memoization, async_tree_none, scimark_sparse_mat_mult, async_tree_memoization_tg, async_tree_none_tg, async_tree_cpu_io_mixed_tg, raytrace, sqlite_synth, regex_effbot

- Geometric mean (including insignificant results): 1.010x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x