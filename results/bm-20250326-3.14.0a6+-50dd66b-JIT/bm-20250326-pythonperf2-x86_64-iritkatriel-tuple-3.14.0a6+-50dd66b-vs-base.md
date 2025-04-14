# Results vs. base

- fork: iritkatriel
- ref: tuple
- machine: linux-x86_64
- commit hash: 50dd66b
- commit date: 2025-03-26
- overall geometric mean: 1.002x slower
- HPT reliability: 58.18%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250326-pythonperf2-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 | bm-20250326-pythonperf2-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|----------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 289 ms                                                                       | 293 ms: 1.01x slower                                               |
| docutils       | 2.98 sec                                                                     | 2.98 sec: 1.00x slower                                             |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                       |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250326-pythonperf2-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 | bm-20250326-pythonperf2-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|----------------------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 524 ms                                                                       | 518 ms: 1.01x faster                                               |
| async_tree_cpu_io_mixed_tg | 505 ms                                                                       | 501 ms: 1.01x faster                                               |
| async_tree_memoization     | 341 ms                                                                       | 339 ms: 1.01x faster                                               |
| coroutines                 | 21.4 ms                                                                      | 21.6 ms: 1.01x slower                                              |
| Geometric mean             | (ref)                                                                        | 1.00x faster                                                       |

Benchmark hidden because not significant (7): async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, async_tree_io_tg, async_tree_none, async_tree_io, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250326-pythonperf2-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 | bm-20250326-pythonperf2-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|----------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 64.6 ms                                                                      | 63.8 ms: 1.01x faster                                              |
| nbody          | 93.0 ms                                                                      | 94.7 ms: 1.02x slower                                              |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                       |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250326-pythonperf2-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 | bm-20250326-pythonperf2-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|----------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 3.12 ms                                                                      | 3.11 ms: 1.00x faster                                              |
| regex_compile  | 137 ms                                                                       | 138 ms: 1.01x slower                                               |
| regex_dna      | 233 ms                                                                       | 239 ms: 1.02x slower                                               |
| regex_v8       | 23.2 ms                                                                      | 23.9 ms: 1.03x slower                                              |
| Geometric mean | (ref)                                                                        | 1.01x slower                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250326-pythonperf2-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 | bm-20250326-pythonperf2-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|---------------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| json_loads          | 26.7 us                                                                      | 26.0 us: 1.02x faster                                              |
| json_dumps          | 11.6 ms                                                                      | 11.5 ms: 1.01x faster                                              |
| xml_etree_parse     | 137 ms                                                                       | 136 ms: 1.01x faster                                               |
| xml_etree_iterparse | 96.0 ms                                                                      | 95.7 ms: 1.00x faster                                              |
| tomli_loads         | 2.07 sec                                                                     | 2.09 sec: 1.01x slower                                             |
| xml_etree_generate  | 81.4 ms                                                                      | 82.4 ms: 1.01x slower                                              |
| xml_etree_process   | 57.2 ms                                                                      | 57.9 ms: 1.01x slower                                              |
| Geometric mean      | (ref)                                                                        | 1.00x faster                                                       |

Benchmark hidden because not significant (2): unpickle_pure_python, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250326-pythonperf2-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 | bm-20250326-pythonperf2-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|------------------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 10.5 ms                                                                      | 10.5 ms: 1.00x faster                                              |
| Geometric mean         | (ref)                                                                        | 1.00x faster                                                       |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250326-pythonperf2-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 | bm-20250326-pythonperf2-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|----------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text    | 24.8 ms                                                                      | 24.6 ms: 1.01x faster                                              |
| mako           | 10.6 ms                                                                      | 10.8 ms: 1.01x slower                                              |
| genshi_xml     | 55.9 ms                                                                      | 58.3 ms: 1.04x slower                                              |
| Geometric mean | (ref)                                                                        | 1.01x slower                                                       |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20250326-pythonperf2-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 | bm-20250326-pythonperf2-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|----------------------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| bench_mp_pool              | 1.28 sec                                                                     | 713 ms: 1.80x faster                                               |
| coverage                   | 82.1 ms                                                                      | 78.0 ms: 1.05x faster                                              |
| pyflate                    | 451 ms                                                                       | 435 ms: 1.04x faster                                               |
| fannkuch                   | 408 ms                                                                       | 395 ms: 1.03x faster                                               |
| chaos                      | 66.5 ms                                                                      | 64.4 ms: 1.03x faster                                              |
| json_loads                 | 26.7 us                                                                      | 26.0 us: 1.02x faster                                              |
| pprint_pformat             | 1.67 sec                                                                     | 1.63 sec: 1.02x faster                                             |
| raytrace                   | 297 ms                                                                       | 292 ms: 1.02x faster                                               |
| thrift                     | 886 us                                                                       | 872 us: 1.02x faster                                               |
| comprehensions             | 20.4 us                                                                      | 20.1 us: 1.02x faster                                              |
| crypto_pyaes               | 83.6 ms                                                                      | 82.3 ms: 1.02x faster                                              |
| go                         | 146 ms                                                                       | 144 ms: 1.01x faster                                               |
| pprint_safe_repr           | 821 ms                                                                       | 809 ms: 1.01x faster                                               |
| generators                 | 29.2 ms                                                                      | 28.8 ms: 1.01x faster                                              |
| json                       | 5.40 ms                                                                      | 5.33 ms: 1.01x faster                                              |
| float                      | 64.6 ms                                                                      | 63.8 ms: 1.01x faster                                              |
| async_tree_cpu_io_mixed    | 524 ms                                                                       | 518 ms: 1.01x faster                                               |
| json_dumps                 | 11.6 ms                                                                      | 11.5 ms: 1.01x faster                                              |
| scimark_fft                | 313 ms                                                                       | 310 ms: 1.01x faster                                               |
| deltablue                  | 3.09 ms                                                                      | 3.06 ms: 1.01x faster                                              |
| xml_etree_parse            | 137 ms                                                                       | 136 ms: 1.01x faster                                               |
| async_tree_cpu_io_mixed_tg | 505 ms                                                                       | 501 ms: 1.01x faster                                               |
| genshi_text                | 24.8 ms                                                                      | 24.6 ms: 1.01x faster                                              |
| async_tree_memoization     | 341 ms                                                                       | 339 ms: 1.01x faster                                               |
| mdp                        | 2.52 sec                                                                     | 2.51 sec: 1.00x faster                                             |
| python_startup_no_site     | 10.5 ms                                                                      | 10.5 ms: 1.00x faster                                              |
| bpe_tokeniser              | 4.83 sec                                                                     | 4.81 sec: 1.00x faster                                             |
| xml_etree_iterparse        | 96.0 ms                                                                      | 95.7 ms: 1.00x faster                                              |
| regex_effbot               | 3.12 ms                                                                      | 3.11 ms: 1.00x faster                                              |
| meteor_contest             | 131 ms                                                                       | 131 ms: 1.00x faster                                               |
| connected_components       | 409 ms                                                                       | 411 ms: 1.00x slower                                               |
| docutils                   | 2.98 sec                                                                     | 2.98 sec: 1.00x slower                                             |
| sympy_sum                  | 154 ms                                                                       | 155 ms: 1.01x slower                                               |
| sympy_integrate            | 23.3 ms                                                                      | 23.4 ms: 1.01x slower                                              |
| tomli_loads                | 2.07 sec                                                                     | 2.09 sec: 1.01x slower                                             |
| sympy_expand               | 515 ms                                                                       | 519 ms: 1.01x slower                                               |
| sqlglot_v2_parse           | 1.43 ms                                                                      | 1.44 ms: 1.01x slower                                              |
| regex_compile              | 137 ms                                                                       | 138 ms: 1.01x slower                                               |
| scimark_sor                | 108 ms                                                                       | 109 ms: 1.01x slower                                               |
| coroutines                 | 21.4 ms                                                                      | 21.6 ms: 1.01x slower                                              |
| sqlalchemy_declarative     | 147 ms                                                                       | 149 ms: 1.01x slower                                               |
| sqlglot_v2_transpile       | 1.81 ms                                                                      | 1.83 ms: 1.01x slower                                              |
| sympy_str                  | 296 ms                                                                       | 299 ms: 1.01x slower                                               |
| xml_etree_generate         | 81.4 ms                                                                      | 82.4 ms: 1.01x slower                                              |
| dulwich_log                | 62.1 ms                                                                      | 62.9 ms: 1.01x slower                                              |
| xml_etree_process          | 57.2 ms                                                                      | 57.9 ms: 1.01x slower                                              |
| shortest_path              | 439 ms                                                                       | 445 ms: 1.01x slower                                               |
| 2to3                       | 289 ms                                                                       | 293 ms: 1.01x slower                                               |
| mako                       | 10.6 ms                                                                      | 10.8 ms: 1.01x slower                                              |
| sqlglot_v2_normalize       | 120 ms                                                                       | 122 ms: 1.02x slower                                               |
| sqlglot_v2_optimize        | 59.7 ms                                                                      | 60.7 ms: 1.02x slower                                              |
| nbody                      | 93.0 ms                                                                      | 94.7 ms: 1.02x slower                                              |
| typing_runtime_protocols   | 177 us                                                                       | 180 us: 1.02x slower                                               |
| subparsers                 | 23.3 ms                                                                      | 23.8 ms: 1.02x slower                                              |
| regex_dna                  | 233 ms                                                                       | 239 ms: 1.02x slower                                               |
| logging_simple             | 6.42 us                                                                      | 6.60 us: 1.03x slower                                              |
| regex_v8                   | 23.2 ms                                                                      | 23.9 ms: 1.03x slower                                              |
| logging_format             | 7.07 us                                                                      | 7.28 us: 1.03x slower                                              |
| scimark_monte_carlo        | 68.8 ms                                                                      | 70.9 ms: 1.03x slower                                              |
| scimark_sparse_mat_mult    | 4.93 ms                                                                      | 5.08 ms: 1.03x slower                                              |
| deepcopy                   | 289 us                                                                       | 299 us: 1.03x slower                                               |
| richards                   | 39.3 ms                                                                      | 40.7 ms: 1.04x slower                                              |
| genshi_xml                 | 55.9 ms                                                                      | 58.3 ms: 1.04x slower                                              |
| richards_super             | 45.2 ms                                                                      | 47.3 ms: 1.05x slower                                              |
| Geometric mean             | (ref)                                                                        | 1.00x faster                                                       |

Benchmark hidden because not significant (32): spectral_norm, telco, html5lib, async_tree_memoization_tg, django_template, async_tree_none_tg, sqlite_synth, sqlalchemy_imperative, pathlib, asyncio_websockets, nqueens, unpickle_pure_python, gc_traversal, python_startup, async_tree_io_tg, many_optionals, pidigits, k_core, async_tree_none, deepcopy_memo, pycparser, deepcopy_reduce, async_tree_io, async_generators, hexiom, pickle_pure_python, scimark_lu, create_gc_cycles, logging_silent, bench_thread_pool, sphinx, pylint

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 58.18% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x