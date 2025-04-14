# Results vs. base

- fork: iritkatriel
- ref: tuple
- machine: linux-x86_64
- commit hash: 50dd66b
- commit date: 2025-03-26
- overall geometric mean: 1.009x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250326-linux-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 | bm-20250326-linux-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 258 ms                                                                 | 256 ms: 1.01x faster                                         |
| docutils       | 2.63 sec                                                               | 2.58 sec: 1.02x faster                                       |
| html5lib       | 61.9 ms                                                                | 62.3 ms: 1.01x slower                                        |
| sphinx         | 1.02 sec                                                               | 1.01 sec: 1.01x faster                                       |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20250326-linux-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 | bm-20250326-linux-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|-------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_memoization  | 311 ms                                                                 | 310 ms: 1.00x faster                                         |
| async_generators        | 389 ms                                                                 | 391 ms: 1.01x slower                                         |
| async_tree_cpu_io_mixed | 487 ms                                                                 | 489 ms: 1.01x slower                                         |
| coroutines              | 23.5 ms                                                                | 23.7 ms: 1.01x slower                                        |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                 |

Benchmark hidden because not significant (7): async_tree_memoization_tg, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_none, asyncio_websockets, async_tree_none_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250326-linux-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 | bm-20250326-linux-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 97.3 ms                                                                | 93.8 ms: 1.04x faster                                        |
| float          | 70.5 ms                                                                | 69.5 ms: 1.01x faster                                        |
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x slower                                         |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250326-linux-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 | bm-20250326-linux-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_effbot   | 3.47 ms                                                                | 3.09 ms: 1.12x faster                                        |
| regex_dna      | 224 ms                                                                 | 211 ms: 1.06x faster                                         |
| regex_compile  | 127 ms                                                                 | 126 ms: 1.01x faster                                         |
| Geometric mean | (ref)                                                                  | 1.05x faster                                                 |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250326-linux-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 | bm-20250326-linux-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|---------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| tomli_loads         | 1.97 sec                                                               | 1.94 sec: 1.01x faster                                       |
| json_dumps          | 11.7 ms                                                                | 11.6 ms: 1.01x faster                                        |
| xml_etree_generate  | 85.2 ms                                                                | 84.5 ms: 1.01x faster                                        |
| xml_etree_process   | 59.3 ms                                                                | 58.9 ms: 1.01x faster                                        |
| xml_etree_iterparse | 99.0 ms                                                                | 98.5 ms: 1.01x faster                                        |
| json_loads          | 30.0 us                                                                | 30.5 us: 1.02x slower                                        |
| Geometric mean      | (ref)                                                                  | 1.00x faster                                                 |

Benchmark hidden because not significant (3): pickle_pure_python, xml_etree_parse, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250326-linux-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 | bm-20250326-linux-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 13.1 ms                                                                | 13.0 ms: 1.00x faster                                        |
| python_startup_no_site | 8.19 ms                                                                | 8.17 ms: 1.00x faster                                        |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250326-linux-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 | bm-20250326-linux-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_xml     | 50.0 ms                                                                | 49.1 ms: 1.02x faster                                        |
| genshi_text    | 21.4 ms                                                                | 21.7 ms: 1.01x slower                                        |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                 |

Benchmark hidden because not significant (2): mako, django_template

All benchmarks:
===============

| Benchmark                | bm-20250326-linux-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 | bm-20250326-linux-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|--------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_effbot             | 3.47 ms                                                                | 3.09 ms: 1.12x faster                                        |
| regex_dna                | 224 ms                                                                 | 211 ms: 1.06x faster                                         |
| logging_silent           | 99.9 ns                                                                | 94.2 ns: 1.06x faster                                        |
| pycparser                | 1.18 sec                                                               | 1.12 sec: 1.05x faster                                       |
| gc_traversal             | 4.84 ms                                                                | 4.65 ms: 1.04x faster                                        |
| nbody                    | 97.3 ms                                                                | 93.8 ms: 1.04x faster                                        |
| richards_super           | 51.0 ms                                                                | 49.4 ms: 1.03x faster                                        |
| richards                 | 44.5 ms                                                                | 43.3 ms: 1.03x faster                                        |
| go                       | 117 ms                                                                 | 114 ms: 1.02x faster                                         |
| scimark_fft              | 355 ms                                                                 | 348 ms: 1.02x faster                                         |
| docutils                 | 2.63 sec                                                               | 2.58 sec: 1.02x faster                                       |
| genshi_xml               | 50.0 ms                                                                | 49.1 ms: 1.02x faster                                        |
| scimark_sor              | 120 ms                                                                 | 118 ms: 1.02x faster                                         |
| comprehensions           | 16.9 us                                                                | 16.6 us: 1.02x faster                                        |
| logging_format           | 6.16 us                                                                | 6.05 us: 1.02x faster                                        |
| nqueens                  | 82.7 ms                                                                | 81.3 ms: 1.02x faster                                        |
| scimark_sparse_mat_mult  | 4.72 ms                                                                | 4.65 ms: 1.02x faster                                        |
| generators               | 28.6 ms                                                                | 28.2 ms: 1.01x faster                                        |
| pathlib                  | 16.7 ms                                                                | 16.5 ms: 1.01x faster                                        |
| tomli_loads              | 1.97 sec                                                               | 1.94 sec: 1.01x faster                                       |
| float                    | 70.5 ms                                                                | 69.5 ms: 1.01x faster                                        |
| chaos                    | 58.8 ms                                                                | 58.1 ms: 1.01x faster                                        |
| spectral_norm            | 99.0 ms                                                                | 97.8 ms: 1.01x faster                                        |
| create_gc_cycles         | 2.50 ms                                                                | 2.47 ms: 1.01x faster                                        |
| json_dumps               | 11.7 ms                                                                | 11.6 ms: 1.01x faster                                        |
| sphinx                   | 1.02 sec                                                               | 1.01 sec: 1.01x faster                                       |
| typing_runtime_protocols | 161 us                                                                 | 160 us: 1.01x faster                                         |
| sqlglot_v2_parse         | 1.27 ms                                                                | 1.25 ms: 1.01x faster                                        |
| sympy_sum                | 149 ms                                                                 | 147 ms: 1.01x faster                                         |
| raytrace                 | 265 ms                                                                 | 263 ms: 1.01x faster                                         |
| sympy_integrate          | 19.5 ms                                                                | 19.3 ms: 1.01x faster                                        |
| 2to3                     | 258 ms                                                                 | 256 ms: 1.01x faster                                         |
| hexiom                   | 6.25 ms                                                                | 6.19 ms: 1.01x faster                                        |
| sqlglot_v2_transpile     | 1.58 ms                                                                | 1.56 ms: 1.01x faster                                        |
| json                     | 5.32 ms                                                                | 5.27 ms: 1.01x faster                                        |
| sqlalchemy_imperative    | 16.7 ms                                                                | 16.6 ms: 1.01x faster                                        |
| deepcopy                 | 259 us                                                                 | 257 us: 1.01x faster                                         |
| sympy_str                | 268 ms                                                                 | 266 ms: 1.01x faster                                         |
| xml_etree_generate       | 85.2 ms                                                                | 84.5 ms: 1.01x faster                                        |
| scimark_lu               | 117 ms                                                                 | 116 ms: 1.01x faster                                         |
| scimark_monte_carlo      | 68.0 ms                                                                | 67.5 ms: 1.01x faster                                        |
| deltablue                | 3.16 ms                                                                | 3.13 ms: 1.01x faster                                        |
| xml_etree_process        | 59.3 ms                                                                | 58.9 ms: 1.01x faster                                        |
| crypto_pyaes             | 74.5 ms                                                                | 73.9 ms: 1.01x faster                                        |
| sqlglot_v2_optimize      | 53.0 ms                                                                | 52.6 ms: 1.01x faster                                        |
| regex_compile            | 127 ms                                                                 | 126 ms: 1.01x faster                                         |
| xml_etree_iterparse      | 99.0 ms                                                                | 98.5 ms: 1.01x faster                                        |
| thrift                   | 772 us                                                                 | 768 us: 1.01x faster                                         |
| sqlalchemy_declarative   | 131 ms                                                                 | 130 ms: 1.01x faster                                         |
| pprint_pformat           | 1.49 sec                                                               | 1.48 sec: 1.00x faster                                       |
| python_startup           | 13.1 ms                                                                | 13.0 ms: 1.00x faster                                        |
| async_tree_memoization   | 311 ms                                                                 | 310 ms: 1.00x faster                                         |
| dulwich_log              | 58.1 ms                                                                | 57.9 ms: 1.00x faster                                        |
| python_startup_no_site   | 8.19 ms                                                                | 8.17 ms: 1.00x faster                                        |
| pidigits                 | 186 ms                                                                 | 186 ms: 1.00x slower                                         |
| pprint_safe_repr         | 727 ms                                                                 | 730 ms: 1.00x slower                                         |
| sqlglot_v2_normalize     | 105 ms                                                                 | 106 ms: 1.00x slower                                         |
| deepcopy_memo            | 29.3 us                                                                | 29.4 us: 1.00x slower                                        |
| async_generators         | 389 ms                                                                 | 391 ms: 1.01x slower                                         |
| async_tree_cpu_io_mixed  | 487 ms                                                                 | 489 ms: 1.01x slower                                         |
| subparsers               | 20.8 ms                                                                | 20.9 ms: 1.01x slower                                        |
| fannkuch                 | 418 ms                                                                 | 420 ms: 1.01x slower                                         |
| mdp                      | 2.48 sec                                                               | 2.50 sec: 1.01x slower                                       |
| pyflate                  | 442 ms                                                                 | 445 ms: 1.01x slower                                         |
| deepcopy_reduce          | 2.69 us                                                                | 2.72 us: 1.01x slower                                        |
| html5lib                 | 61.9 ms                                                                | 62.3 ms: 1.01x slower                                        |
| connected_components     | 449 ms                                                                 | 452 ms: 1.01x slower                                         |
| coroutines               | 23.5 ms                                                                | 23.7 ms: 1.01x slower                                        |
| genshi_text              | 21.4 ms                                                                | 21.7 ms: 1.01x slower                                        |
| json_loads               | 30.0 us                                                                | 30.5 us: 1.02x slower                                        |
| Geometric mean           | (ref)                                                                  | 1.01x faster                                                 |

Benchmark hidden because not significant (26): async_tree_memoization_tg, async_tree_io, logging_simple, pylint, async_tree_cpu_io_mixed_tg, async_tree_none, asyncio_websockets, coverage, sympy_expand, mako, bench_mp_pool, meteor_contest, pickle_pure_python, xml_etree_parse, regex_v8, shortest_path, bench_thread_pool, async_tree_none_tg, bpe_tokeniser, many_optionals, django_template, unpickle_pure_python, sqlite_synth, telco, async_tree_io_tg, k_core

- Geometric mean (including insignificant results): 1.009x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x