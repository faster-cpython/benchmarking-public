# Results vs. base

- fork: mdboom
- ref: tuple_hash_cache2
- machine: linux-x86_64
- commit hash: d2c521a
- commit date: 2025-03-24
- overall geometric mean: 1.008x faster
- HPT reliability: 54.73%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250324-pythonperf2-x86_64-python-6226edc48baa888b413f-3.14.0a6+-6226edc | bm-20250324-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-d2c521a |
|----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 326 ms                                                                       | 325 ms: 1.00x faster                                                      |
| docutils       | 2.91 sec                                                                     | 2.94 sec: 1.01x slower                                                    |
| html5lib       | 72.8 ms                                                                      | 73.4 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                              |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250324-pythonperf2-x86_64-python-6226edc48baa888b413f-3.14.0a6+-6226edc | bm-20250324-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-d2c521a |
|----------------------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_generators           | 495 ms                                                                       | 465 ms: 1.06x faster                                                      |
| async_tree_cpu_io_mixed_tg | 474 ms                                                                       | 477 ms: 1.01x slower                                                      |
| async_tree_memoization_tg  | 307 ms                                                                       | 310 ms: 1.01x slower                                                      |
| async_tree_none_tg         | 243 ms                                                                       | 246 ms: 1.01x slower                                                      |
| async_tree_io              | 579 ms                                                                       | 587 ms: 1.01x slower                                                      |
| asyncio_websockets         | 375 ms                                                                       | 381 ms: 1.02x slower                                                      |
| async_tree_memoization     | 337 ms                                                                       | 342 ms: 1.02x slower                                                      |
| async_tree_none            | 278 ms                                                                       | 283 ms: 1.02x slower                                                      |
| Geometric mean             | (ref)                                                                        | 1.00x slower                                                              |

Benchmark hidden because not significant (3): coroutines, async_tree_io_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250324-pythonperf2-x86_64-python-6226edc48baa888b413f-3.14.0a6+-6226edc | bm-20250324-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-d2c521a |
|----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 133 ms                                                                       | 131 ms: 1.02x faster                                                      |
| pidigits       | 249 ms                                                                       | 249 ms: 1.00x slower                                                      |
| Geometric mean | (ref)                                                                        | 1.01x faster                                                              |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250324-pythonperf2-x86_64-python-6226edc48baa888b413f-3.14.0a6+-6226edc | bm-20250324-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-d2c521a |
|----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 25.2 ms                                                                      | 23.1 ms: 1.09x faster                                                     |
| regex_dna      | 246 ms                                                                       | 234 ms: 1.05x faster                                                      |
| regex_effbot   | 3.12 ms                                                                      | 3.09 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                                        | 1.04x faster                                                              |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250324-pythonperf2-x86_64-python-6226edc48baa888b413f-3.14.0a6+-6226edc | bm-20250324-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-d2c521a |
|----------------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 13.3 ms                                                                      | 13.2 ms: 1.01x faster                                                     |
| xml_etree_parse      | 137 ms                                                                       | 136 ms: 1.01x faster                                                      |
| xml_etree_iterparse  | 89.7 ms                                                                      | 88.8 ms: 1.01x faster                                                     |
| xml_etree_process    | 70.0 ms                                                                      | 69.7 ms: 1.00x faster                                                     |
| xml_etree_generate   | 97.5 ms                                                                      | 97.2 ms: 1.00x faster                                                     |
| unpickle_pure_python | 244 us                                                                       | 247 us: 1.01x slower                                                      |
| pickle_pure_python   | 367 us                                                                       | 372 us: 1.01x slower                                                      |
| tomli_loads          | 2.39 sec                                                                     | 2.44 sec: 1.02x slower                                                    |
| Geometric mean       | (ref)                                                                        | 1.00x slower                                                              |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250324-pythonperf2-x86_64-python-6226edc48baa888b413f-3.14.0a6+-6226edc | bm-20250324-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-d2c521a |
|------------------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 13.8 ms                                                                      | 13.8 ms: 1.00x slower                                                     |
| python_startup         | 19.4 ms                                                                      | 19.5 ms: 1.00x slower                                                     |
| Geometric mean         | (ref)                                                                        | 1.00x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250324-pythonperf2-x86_64-python-6226edc48baa888b413f-3.14.0a6+-6226edc | bm-20250324-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-d2c521a |
|----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako           | 17.7 ms                                                                      | 17.6 ms: 1.00x faster                                                     |
| genshi_text    | 30.2 ms                                                                      | 30.4 ms: 1.01x slower                                                     |
| genshi_xml     | 62.8 ms                                                                      | 63.5 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                              |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20250324-pythonperf2-x86_64-python-6226edc48baa888b413f-3.14.0a6+-6226edc | bm-20250324-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-d2c521a |
|----------------------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mdp                        | 2.80 sec                                                                     | 1.57 sec: 1.78x faster                                                    |
| regex_v8                   | 25.2 ms                                                                      | 23.1 ms: 1.09x faster                                                     |
| async_generators           | 495 ms                                                                       | 465 ms: 1.06x faster                                                      |
| regex_dna                  | 246 ms                                                                       | 234 ms: 1.05x faster                                                      |
| coverage                   | 121 ms                                                                       | 116 ms: 1.04x faster                                                      |
| scimark_monte_carlo        | 86.7 ms                                                                      | 83.8 ms: 1.03x faster                                                     |
| richards_super             | 66.8 ms                                                                      | 65.7 ms: 1.02x faster                                                     |
| sqlglot_v2_normalize       | 129 ms                                                                       | 127 ms: 1.02x faster                                                      |
| nbody                      | 133 ms                                                                       | 131 ms: 1.02x faster                                                      |
| logging_format             | 8.07 us                                                                      | 7.95 us: 1.02x faster                                                     |
| go                         | 153 ms                                                                       | 151 ms: 1.02x faster                                                      |
| shortest_path              | 531 ms                                                                       | 523 ms: 1.01x faster                                                      |
| connected_components       | 502 ms                                                                       | 495 ms: 1.01x faster                                                      |
| json_dumps                 | 13.3 ms                                                                      | 13.2 ms: 1.01x faster                                                     |
| xml_etree_parse            | 137 ms                                                                       | 136 ms: 1.01x faster                                                      |
| xml_etree_iterparse        | 89.7 ms                                                                      | 88.8 ms: 1.01x faster                                                     |
| sqlglot_v2_optimize        | 65.5 ms                                                                      | 64.8 ms: 1.01x faster                                                     |
| generators                 | 30.6 ms                                                                      | 30.3 ms: 1.01x faster                                                     |
| scimark_lu                 | 124 ms                                                                       | 123 ms: 1.01x faster                                                      |
| regex_effbot               | 3.12 ms                                                                      | 3.09 ms: 1.01x faster                                                     |
| pprint_pformat             | 1.86 sec                                                                     | 1.85 sec: 1.01x faster                                                    |
| logging_simple             | 7.24 us                                                                      | 7.18 us: 1.01x faster                                                     |
| richards                   | 57.3 ms                                                                      | 56.9 ms: 1.01x faster                                                     |
| telco                      | 9.51 ms                                                                      | 9.46 ms: 1.01x faster                                                     |
| sqlalchemy_declarative     | 173 ms                                                                       | 172 ms: 1.01x faster                                                      |
| xml_etree_process          | 70.0 ms                                                                      | 69.7 ms: 1.00x faster                                                     |
| mako                       | 17.7 ms                                                                      | 17.6 ms: 1.00x faster                                                     |
| k_core                     | 2.39 sec                                                                     | 2.38 sec: 1.00x faster                                                    |
| dulwich_log                | 64.6 ms                                                                      | 64.3 ms: 1.00x faster                                                     |
| pprint_safe_repr           | 904 ms                                                                       | 900 ms: 1.00x faster                                                      |
| sympy_integrate            | 26.6 ms                                                                      | 26.5 ms: 1.00x faster                                                     |
| 2to3                       | 326 ms                                                                       | 325 ms: 1.00x faster                                                      |
| xml_etree_generate         | 97.5 ms                                                                      | 97.2 ms: 1.00x faster                                                     |
| python_startup_no_site     | 13.8 ms                                                                      | 13.8 ms: 1.00x slower                                                     |
| pidigits                   | 249 ms                                                                       | 249 ms: 1.00x slower                                                      |
| python_startup             | 19.4 ms                                                                      | 19.5 ms: 1.00x slower                                                     |
| sympy_expand               | 564 ms                                                                       | 566 ms: 1.00x slower                                                      |
| pyflate                    | 495 ms                                                                       | 497 ms: 1.00x slower                                                      |
| bpe_tokeniser              | 5.31 sec                                                                     | 5.33 sec: 1.01x slower                                                    |
| hexiom                     | 7.44 ms                                                                      | 7.48 ms: 1.01x slower                                                     |
| sympy_str                  | 334 ms                                                                       | 336 ms: 1.01x slower                                                      |
| many_optionals             | 1.11 ms                                                                      | 1.12 ms: 1.01x slower                                                     |
| async_tree_cpu_io_mixed_tg | 474 ms                                                                       | 477 ms: 1.01x slower                                                      |
| raytrace                   | 328 ms                                                                       | 330 ms: 1.01x slower                                                      |
| meteor_contest             | 154 ms                                                                       | 155 ms: 1.01x slower                                                      |
| genshi_text                | 30.2 ms                                                                      | 30.4 ms: 1.01x slower                                                     |
| chaos                      | 69.2 ms                                                                      | 69.8 ms: 1.01x slower                                                     |
| scimark_sparse_mat_mult    | 5.73 ms                                                                      | 5.78 ms: 1.01x slower                                                     |
| docutils                   | 2.91 sec                                                                     | 2.94 sec: 1.01x slower                                                    |
| html5lib                   | 72.8 ms                                                                      | 73.4 ms: 1.01x slower                                                     |
| async_tree_memoization_tg  | 307 ms                                                                       | 310 ms: 1.01x slower                                                      |
| async_tree_none_tg         | 243 ms                                                                       | 246 ms: 1.01x slower                                                      |
| genshi_xml                 | 62.8 ms                                                                      | 63.5 ms: 1.01x slower                                                     |
| scimark_sor                | 120 ms                                                                       | 121 ms: 1.01x slower                                                      |
| sqlglot_v2_parse           | 1.63 ms                                                                      | 1.65 ms: 1.01x slower                                                     |
| nqueens                    | 110 ms                                                                       | 111 ms: 1.01x slower                                                      |
| unpickle_pure_python       | 244 us                                                                       | 247 us: 1.01x slower                                                      |
| async_tree_io              | 579 ms                                                                       | 587 ms: 1.01x slower                                                      |
| scimark_fft                | 347 ms                                                                       | 352 ms: 1.01x slower                                                      |
| pickle_pure_python         | 367 us                                                                       | 372 us: 1.01x slower                                                      |
| asyncio_websockets         | 375 ms                                                                       | 381 ms: 1.02x slower                                                      |
| async_tree_memoization     | 337 ms                                                                       | 342 ms: 1.02x slower                                                      |
| deepcopy_reduce            | 3.51 us                                                                      | 3.56 us: 1.02x slower                                                     |
| typing_runtime_protocols   | 214 us                                                                       | 218 us: 1.02x slower                                                      |
| deepcopy_memo              | 36.2 us                                                                      | 36.9 us: 1.02x slower                                                     |
| async_tree_none            | 278 ms                                                                       | 283 ms: 1.02x slower                                                      |
| fannkuch                   | 473 ms                                                                       | 483 ms: 1.02x slower                                                      |
| tomli_loads                | 2.39 sec                                                                     | 2.44 sec: 1.02x slower                                                    |
| spectral_norm              | 97.3 ms                                                                      | 102 ms: 1.04x slower                                                      |
| crypto_pyaes               | 91.9 ms                                                                      | 96.0 ms: 1.04x slower                                                     |
| Geometric mean             | (ref)                                                                        | 1.01x faster                                                              |

Benchmark hidden because not significant (25): create_gc_cycles, float, json, sqlite_synth, deltablue, json_loads, pathlib, sqlalchemy_imperative, regex_compile, pylint, coroutines, deepcopy, bench_mp_pool, comprehensions, sphinx, sympy_sum, pycparser, django_template, bench_thread_pool, logging_silent, async_tree_io_tg, async_tree_cpu_io_mixed, gc_traversal, subparsers, sqlglot_v2_transpile
Ignored benchmarks (1) of results/bm-20250324-3.14.0a6+-6226edc-NOGIL/bm-20250324-pythonperf2-x86_64-python-6226edc48baa888b413f-3.14.0a6+-6226edc.json: thrift

- Geometric mean (including insignificant results): 1.008x faster

# HPT report

- Reliability score: 54.73% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x