# Results vs. base

- fork: mdboom
- ref: tuple_hash_cache_emp
- machine: linux-x86_64
- commit hash: 40ad9fc
- commit date: 2025-03-21
- overall geometric mean: 1.003x faster
- HPT reliability: 99.30%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250320-pythonperf2-x86_64-python-ce79274e9f093bd06d22-3.14.0a6+-ce79274 | bm-20250321-pythonperf2-x86_64-mdboom-tuple_hash_cache_emp-3.14.0a6+-40ad9fc |
|----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                                       | 287 ms: 1.01x slower                                                         |
| docutils       | 2.92 sec                                                                     | 2.90 sec: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                                 |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250320-pythonperf2-x86_64-python-ce79274e9f093bd06d22-3.14.0a6+-ce79274 | bm-20250321-pythonperf2-x86_64-mdboom-tuple_hash_cache_emp-3.14.0a6+-40ad9fc |
|----------------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_generators           | 421 ms                                                                       | 415 ms: 1.02x faster                                                         |
| async_tree_cpu_io_mixed    | 520 ms                                                                       | 525 ms: 1.01x slower                                                         |
| async_tree_memoization     | 349 ms                                                                       | 354 ms: 1.01x slower                                                         |
| coroutines                 | 21.1 ms                                                                      | 21.3 ms: 1.01x slower                                                        |
| async_tree_none            | 291 ms                                                                       | 297 ms: 1.02x slower                                                         |
| async_tree_none_tg         | 275 ms                                                                       | 282 ms: 1.03x slower                                                         |
| async_tree_cpu_io_mixed_tg | 505 ms                                                                       | 521 ms: 1.03x slower                                                         |
| async_tree_memoization_tg  | 339 ms                                                                       | 356 ms: 1.05x slower                                                         |
| Geometric mean             | (ref)                                                                        | 1.01x slower                                                                 |

Benchmark hidden because not significant (3): async_tree_io, asyncio_websockets, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250320-pythonperf2-x86_64-python-ce79274e9f093bd06d22-3.14.0a6+-ce79274 | bm-20250321-pythonperf2-x86_64-mdboom-tuple_hash_cache_emp-3.14.0a6+-40ad9fc |
|----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 71.7 ms                                                                      | 72.1 ms: 1.01x slower                                                        |
| nbody          | 100 ms                                                                       | 105 ms: 1.05x slower                                                         |
| Geometric mean | (ref)                                                                        | 1.02x slower                                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250320-pythonperf2-x86_64-python-ce79274e9f093bd06d22-3.14.0a6+-ce79274 | bm-20250321-pythonperf2-x86_64-mdboom-tuple_hash_cache_emp-3.14.0a6+-40ad9fc |
|----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.11 ms                                                                      | 3.12 ms: 1.00x slower                                                        |
| regex_compile  | 138 ms                                                                       | 139 ms: 1.00x slower                                                         |
| regex_dna      | 236 ms                                                                       | 239 ms: 1.01x slower                                                         |
| regex_v8       | 23.8 ms                                                                      | 24.4 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250320-pythonperf2-x86_64-python-ce79274e9f093bd06d22-3.14.0a6+-ce79274 | bm-20250321-pythonperf2-x86_64-mdboom-tuple_hash_cache_emp-3.14.0a6+-40ad9fc |
|----------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 228 us                                                                       | 222 us: 1.02x faster                                                         |
| json_dumps           | 11.4 ms                                                                      | 11.5 ms: 1.01x slower                                                        |
| xml_etree_generate   | 84.4 ms                                                                      | 85.6 ms: 1.01x slower                                                        |
| xml_etree_process    | 60.3 ms                                                                      | 61.5 ms: 1.02x slower                                                        |
| pickle_pure_python   | 332 us                                                                       | 340 us: 1.02x slower                                                         |
| Geometric mean       | (ref)                                                                        | 1.01x slower                                                                 |

Benchmark hidden because not significant (4): json_loads, xml_etree_iterparse, xml_etree_parse, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250320-pythonperf2-x86_64-python-ce79274e9f093bd06d22-3.14.0a6+-ce79274 | bm-20250321-pythonperf2-x86_64-mdboom-tuple_hash_cache_emp-3.14.0a6+-40ad9fc |
|------------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 16.4 ms                                                                      | 16.4 ms: 1.00x faster                                                        |
| python_startup_no_site | 10.5 ms                                                                      | 10.5 ms: 1.00x faster                                                        |
| Geometric mean         | (ref)                                                                        | 1.00x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250320-pythonperf2-x86_64-python-ce79274e9f093bd06d22-3.14.0a6+-ce79274 | bm-20250321-pythonperf2-x86_64-mdboom-tuple_hash_cache_emp-3.14.0a6+-40ad9fc |
|----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml     | 57.0 ms                                                                      | 54.9 ms: 1.04x faster                                                        |
| genshi_text    | 24.6 ms                                                                      | 23.7 ms: 1.04x faster                                                        |
| mako           | 11.1 ms                                                                      | 11.4 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                                        | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20250320-pythonperf2-x86_64-python-ce79274e9f093bd06d22-3.14.0a6+-ce79274 | bm-20250321-pythonperf2-x86_64-mdboom-tuple_hash_cache_emp-3.14.0a6+-40ad9fc |
|----------------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mdp                        | 2.51 sec                                                                     | 1.31 sec: 1.91x faster                                                       |
| genshi_xml                 | 57.0 ms                                                                      | 54.9 ms: 1.04x faster                                                        |
| genshi_text                | 24.6 ms                                                                      | 23.7 ms: 1.04x faster                                                        |
| fannkuch                   | 400 ms                                                                       | 388 ms: 1.03x faster                                                         |
| richards_super             | 55.1 ms                                                                      | 53.5 ms: 1.03x faster                                                        |
| unpickle_pure_python       | 228 us                                                                       | 222 us: 1.02x faster                                                         |
| chaos                      | 65.5 ms                                                                      | 64.2 ms: 1.02x faster                                                        |
| scimark_sor                | 112 ms                                                                       | 110 ms: 1.02x faster                                                         |
| async_generators           | 421 ms                                                                       | 415 ms: 1.02x faster                                                         |
| sqlite_synth               | 2.86 us                                                                      | 2.82 us: 1.01x faster                                                        |
| sympy_sum                  | 156 ms                                                                       | 154 ms: 1.01x faster                                                         |
| pycparser                  | 1.26 sec                                                                     | 1.25 sec: 1.01x faster                                                       |
| shortest_path              | 458 ms                                                                       | 454 ms: 1.01x faster                                                         |
| docutils                   | 2.92 sec                                                                     | 2.90 sec: 1.01x faster                                                       |
| sqlalchemy_declarative     | 147 ms                                                                       | 146 ms: 1.01x faster                                                         |
| connected_components       | 430 ms                                                                       | 427 ms: 1.01x faster                                                         |
| sqlalchemy_imperative      | 18.1 ms                                                                      | 18.1 ms: 1.01x faster                                                        |
| sympy_integrate            | 23.5 ms                                                                      | 23.4 ms: 1.00x faster                                                        |
| python_startup             | 16.4 ms                                                                      | 16.4 ms: 1.00x faster                                                        |
| python_startup_no_site     | 10.5 ms                                                                      | 10.5 ms: 1.00x faster                                                        |
| bpe_tokeniser              | 4.80 sec                                                                     | 4.79 sec: 1.00x faster                                                       |
| regex_effbot               | 3.11 ms                                                                      | 3.12 ms: 1.00x slower                                                        |
| deepcopy                   | 285 us                                                                       | 287 us: 1.00x slower                                                         |
| regex_compile              | 138 ms                                                                       | 139 ms: 1.00x slower                                                         |
| pyflate                    | 468 ms                                                                       | 471 ms: 1.01x slower                                                         |
| float                      | 71.7 ms                                                                      | 72.1 ms: 1.01x slower                                                        |
| nqueens                    | 96.0 ms                                                                      | 96.7 ms: 1.01x slower                                                        |
| subparsers                 | 23.5 ms                                                                      | 23.7 ms: 1.01x slower                                                        |
| json                       | 5.44 ms                                                                      | 5.48 ms: 1.01x slower                                                        |
| 2to3                       | 285 ms                                                                       | 287 ms: 1.01x slower                                                         |
| async_tree_cpu_io_mixed    | 520 ms                                                                       | 525 ms: 1.01x slower                                                         |
| crypto_pyaes               | 83.4 ms                                                                      | 84.2 ms: 1.01x slower                                                        |
| scimark_sparse_mat_mult    | 4.65 ms                                                                      | 4.69 ms: 1.01x slower                                                        |
| sympy_expand               | 502 ms                                                                       | 507 ms: 1.01x slower                                                         |
| json_dumps                 | 11.4 ms                                                                      | 11.5 ms: 1.01x slower                                                        |
| scimark_fft                | 313 ms                                                                       | 316 ms: 1.01x slower                                                         |
| deepcopy_memo              | 29.3 us                                                                      | 29.7 us: 1.01x slower                                                        |
| async_tree_memoization     | 349 ms                                                                       | 354 ms: 1.01x slower                                                         |
| sqlglot_v2_normalize       | 118 ms                                                                       | 120 ms: 1.01x slower                                                         |
| regex_dna                  | 236 ms                                                                       | 239 ms: 1.01x slower                                                         |
| coroutines                 | 21.1 ms                                                                      | 21.3 ms: 1.01x slower                                                        |
| xml_etree_generate         | 84.4 ms                                                                      | 85.6 ms: 1.01x slower                                                        |
| coverage                   | 81.2 ms                                                                      | 82.4 ms: 1.01x slower                                                        |
| generators                 | 28.4 ms                                                                      | 28.8 ms: 1.02x slower                                                        |
| deepcopy_reduce            | 2.98 us                                                                      | 3.03 us: 1.02x slower                                                        |
| hexiom                     | 6.39 ms                                                                      | 6.51 ms: 1.02x slower                                                        |
| xml_etree_process          | 60.3 ms                                                                      | 61.5 ms: 1.02x slower                                                        |
| async_tree_none            | 291 ms                                                                       | 297 ms: 1.02x slower                                                         |
| comprehensions             | 17.6 us                                                                      | 18.0 us: 1.02x slower                                                        |
| scimark_monte_carlo        | 67.3 ms                                                                      | 68.8 ms: 1.02x slower                                                        |
| sqlglot_v2_parse           | 1.39 ms                                                                      | 1.42 ms: 1.02x slower                                                        |
| pickle_pure_python         | 332 us                                                                       | 340 us: 1.02x slower                                                         |
| sqlglot_v2_transpile       | 1.79 ms                                                                      | 1.83 ms: 1.02x slower                                                        |
| regex_v8                   | 23.8 ms                                                                      | 24.4 ms: 1.02x slower                                                        |
| telco                      | 8.00 ms                                                                      | 8.19 ms: 1.02x slower                                                        |
| async_tree_none_tg         | 275 ms                                                                       | 282 ms: 1.03x slower                                                         |
| logging_simple             | 6.40 us                                                                      | 6.59 us: 1.03x slower                                                        |
| async_tree_cpu_io_mixed_tg | 505 ms                                                                       | 521 ms: 1.03x slower                                                         |
| logging_format             | 7.04 us                                                                      | 7.26 us: 1.03x slower                                                        |
| mako                       | 11.1 ms                                                                      | 11.4 ms: 1.03x slower                                                        |
| async_tree_memoization_tg  | 339 ms                                                                       | 356 ms: 1.05x slower                                                         |
| nbody                      | 100 ms                                                                       | 105 ms: 1.05x slower                                                         |
| Geometric mean             | (ref)                                                                        | 1.00x faster                                                                 |

Benchmark hidden because not significant (33): typing_runtime_protocols, bench_mp_pool, bench_thread_pool, k_core, scimark_lu, async_tree_io, logging_silent, deltablue, pylint, richards, pidigits, json_loads, go, xml_etree_iterparse, meteor_contest, xml_etree_parse, sympy_str, spectral_norm, sqlglot_v2_optimize, many_optionals, pprint_pformat, pathlib, sphinx, raytrace, tomli_loads, django_template, dulwich_log, pprint_safe_repr, gc_traversal, asyncio_websockets, html5lib, async_tree_io_tg, create_gc_cycles
Ignored benchmarks (1) of results/bm-20250320-3.14.0a6+-ce79274/bm-20250320-pythonperf2-x86_64-python-ce79274e9f093bd06d22-3.14.0a6+-ce79274.json: thrift

- Geometric mean (including insignificant results): 1.003x faster

# HPT report

- Reliability score: 99.30% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x