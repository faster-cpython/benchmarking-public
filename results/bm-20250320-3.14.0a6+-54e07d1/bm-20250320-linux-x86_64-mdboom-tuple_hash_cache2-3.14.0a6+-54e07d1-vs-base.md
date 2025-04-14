# Results vs. base

- fork: mdboom
- ref: tuple_hash_cache2
- machine: linux-x86_64
- commit hash: 54e07d1
- commit date: 2025-03-20
- overall geometric mean: 1.005x faster
- HPT reliability: 99.93%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250319-linux-x86_64-python-6146295a5b8e9286ccb8-3.14.0a6+-6146295 | bm-20250320-linux-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-54e07d1 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 256 ms                                                                 | 258 ms: 1.01x slower                                                |
| docutils       | 2.59 sec                                                               | 2.61 sec: 1.01x slower                                              |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250319-linux-x86_64-python-6146295a5b8e9286ccb8-3.14.0a6+-6146295 | bm-20250320-linux-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-54e07d1 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| coroutines                 | 23.8 ms                                                                | 23.6 ms: 1.01x faster                                               |
| async_tree_cpu_io_mixed    | 492 ms                                                                 | 495 ms: 1.01x slower                                                |
| async_tree_cpu_io_mixed_tg | 475 ms                                                                 | 484 ms: 1.02x slower                                                |
| async_generators           | 396 ms                                                                 | 403 ms: 1.02x slower                                                |
| async_tree_memoization_tg  | 316 ms                                                                 | 321 ms: 1.02x slower                                                |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (6): asyncio_websockets, async_tree_io_tg, async_tree_io, async_tree_memoization, async_tree_none, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250319-linux-x86_64-python-6146295a5b8e9286ccb8-3.14.0a6+-6146295 | bm-20250320-linux-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-54e07d1 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 98.6 ms                                                                | 101 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250319-linux-x86_64-python-6146295a5b8e9286ccb8-3.14.0a6+-6146295 | bm-20250320-linux-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-54e07d1 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 127 ms                                                                 | 127 ms: 1.00x faster                                                |
| regex_dna      | 215 ms                                                                 | 216 ms: 1.00x slower                                                |
| regex_effbot   | 3.15 ms                                                                | 3.21 ms: 1.02x slower                                               |
| regex_v8       | 23.1 ms                                                                | 24.0 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250319-linux-x86_64-python-6146295a5b8e9286ccb8-3.14.0a6+-6146295 | bm-20250320-linux-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-54e07d1 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_pure_python | 222 us                                                                 | 221 us: 1.00x faster                                                |
| pickle_pure_python   | 316 us                                                                 | 318 us: 1.01x slower                                                |
| json_dumps           | 11.4 ms                                                                | 11.5 ms: 1.01x slower                                               |
| xml_etree_iterparse  | 97.8 ms                                                                | 98.7 ms: 1.01x slower                                               |
| xml_etree_generate   | 83.7 ms                                                                | 84.7 ms: 1.01x slower                                               |
| tomli_loads          | 1.96 sec                                                               | 1.99 sec: 1.01x slower                                              |
| xml_etree_process    | 58.1 ms                                                                | 59.2 ms: 1.02x slower                                               |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (2): json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250319-linux-x86_64-python-6146295a5b8e9286ccb8-3.14.0a6+-6146295 | bm-20250320-linux-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-54e07d1 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup | 13.1 ms                                                                | 13.1 ms: 1.00x slower                                               |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250319-linux-x86_64-python-6146295a5b8e9286ccb8-3.14.0a6+-6146295 | bm-20250320-linux-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-54e07d1 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                                | 49.1 ms: 1.02x faster                                               |
| genshi_text     | 22.0 ms                                                                | 21.6 ms: 1.02x faster                                               |
| mako            | 11.4 ms                                                                | 11.5 ms: 1.01x slower                                               |
| django_template | 31.2 ms                                                                | 31.6 ms: 1.01x slower                                               |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20250319-linux-x86_64-python-6146295a5b8e9286ccb8-3.14.0a6+-6146295 | bm-20250320-linux-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-54e07d1 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                        | 2.47 sec                                                               | 1.25 sec: 1.98x faster                                              |
| coverage                   | 90.8 ms                                                                | 84.7 ms: 1.07x faster                                               |
| logging_silent             | 100.0 ns                                                               | 97.5 ns: 1.03x faster                                               |
| pyflate                    | 465 ms                                                                 | 455 ms: 1.02x faster                                                |
| genshi_xml                 | 50.1 ms                                                                | 49.1 ms: 1.02x faster                                               |
| shortest_path              | 502 ms                                                                 | 492 ms: 1.02x faster                                                |
| gc_traversal               | 4.92 ms                                                                | 4.82 ms: 1.02x faster                                               |
| genshi_text                | 22.0 ms                                                                | 21.6 ms: 1.02x faster                                               |
| generators                 | 28.6 ms                                                                | 28.1 ms: 1.02x faster                                               |
| scimark_sparse_mat_mult    | 4.76 ms                                                                | 4.69 ms: 1.02x faster                                               |
| connected_components       | 461 ms                                                                 | 454 ms: 1.01x faster                                                |
| json                       | 5.31 ms                                                                | 5.24 ms: 1.01x faster                                               |
| create_gc_cycles           | 2.51 ms                                                                | 2.49 ms: 1.01x faster                                               |
| telco                      | 7.91 ms                                                                | 7.82 ms: 1.01x faster                                               |
| deepcopy_reduce            | 2.70 us                                                                | 2.67 us: 1.01x faster                                               |
| coroutines                 | 23.8 ms                                                                | 23.6 ms: 1.01x faster                                               |
| scimark_sor                | 120 ms                                                                 | 119 ms: 1.01x faster                                                |
| sqlalchemy_imperative      | 16.6 ms                                                                | 16.6 ms: 1.00x faster                                               |
| sqlglot_v2_parse           | 1.29 ms                                                                | 1.28 ms: 1.00x faster                                               |
| many_optionals             | 948 us                                                                 | 944 us: 1.00x faster                                                |
| sqlglot_v2_transpile       | 1.60 ms                                                                | 1.59 ms: 1.00x faster                                               |
| regex_compile              | 127 ms                                                                 | 127 ms: 1.00x faster                                                |
| unpickle_pure_python       | 222 us                                                                 | 221 us: 1.00x faster                                                |
| nqueens                    | 83.9 ms                                                                | 83.6 ms: 1.00x faster                                               |
| python_startup             | 13.1 ms                                                                | 13.1 ms: 1.00x slower                                               |
| regex_dna                  | 215 ms                                                                 | 216 ms: 1.00x slower                                                |
| bench_thread_pool          | 872 us                                                                 | 875 us: 1.00x slower                                                |
| sympy_integrate            | 19.9 ms                                                                | 20.0 ms: 1.00x slower                                               |
| dulwich_log                | 58.4 ms                                                                | 58.7 ms: 1.01x slower                                               |
| pickle_pure_python         | 316 us                                                                 | 318 us: 1.01x slower                                                |
| crypto_pyaes               | 75.5 ms                                                                | 75.9 ms: 1.01x slower                                               |
| fannkuch                   | 433 ms                                                                 | 436 ms: 1.01x slower                                                |
| bench_mp_pool              | 82.7 ms                                                                | 83.2 ms: 1.01x slower                                               |
| 2to3                       | 256 ms                                                                 | 258 ms: 1.01x slower                                                |
| async_tree_cpu_io_mixed    | 492 ms                                                                 | 495 ms: 1.01x slower                                                |
| sqlglot_v2_optimize        | 52.8 ms                                                                | 53.1 ms: 1.01x slower                                               |
| json_dumps                 | 11.4 ms                                                                | 11.5 ms: 1.01x slower                                               |
| mako                       | 11.4 ms                                                                | 11.5 ms: 1.01x slower                                               |
| xml_etree_iterparse        | 97.8 ms                                                                | 98.7 ms: 1.01x slower                                               |
| docutils                   | 2.59 sec                                                               | 2.61 sec: 1.01x slower                                              |
| scimark_lu                 | 117 ms                                                                 | 118 ms: 1.01x slower                                                |
| scimark_fft                | 352 ms                                                                 | 355 ms: 1.01x slower                                                |
| django_template            | 31.2 ms                                                                | 31.6 ms: 1.01x slower                                               |
| sqlglot_v2_normalize       | 106 ms                                                                 | 107 ms: 1.01x slower                                                |
| xml_etree_generate         | 83.7 ms                                                                | 84.7 ms: 1.01x slower                                               |
| hexiom                     | 6.25 ms                                                                | 6.33 ms: 1.01x slower                                               |
| raytrace                   | 267 ms                                                                 | 271 ms: 1.01x slower                                                |
| scimark_monte_carlo        | 68.3 ms                                                                | 69.2 ms: 1.01x slower                                               |
| tomli_loads                | 1.96 sec                                                               | 1.99 sec: 1.01x slower                                              |
| sympy_sum                  | 148 ms                                                                 | 151 ms: 1.02x slower                                                |
| sympy_expand               | 452 ms                                                                 | 460 ms: 1.02x slower                                                |
| deepcopy_memo              | 29.7 us                                                                | 30.2 us: 1.02x slower                                               |
| async_tree_cpu_io_mixed_tg | 475 ms                                                                 | 484 ms: 1.02x slower                                                |
| regex_effbot               | 3.15 ms                                                                | 3.21 ms: 1.02x slower                                               |
| async_generators           | 396 ms                                                                 | 403 ms: 1.02x slower                                                |
| async_tree_memoization_tg  | 316 ms                                                                 | 321 ms: 1.02x slower                                                |
| comprehensions             | 16.7 us                                                                | 17.0 us: 1.02x slower                                               |
| xml_etree_process          | 58.1 ms                                                                | 59.2 ms: 1.02x slower                                               |
| meteor_contest             | 107 ms                                                                 | 109 ms: 1.02x slower                                                |
| nbody                      | 98.6 ms                                                                | 101 ms: 1.02x slower                                                |
| richards_super             | 49.1 ms                                                                | 50.2 ms: 1.02x slower                                               |
| richards                   | 42.8 ms                                                                | 43.9 ms: 1.03x slower                                               |
| regex_v8                   | 23.1 ms                                                                | 24.0 ms: 1.04x slower                                               |
| spectral_norm              | 98.0 ms                                                                | 103 ms: 1.05x slower                                                |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (31): logging_simple, logging_format, json_loads, sqlalchemy_declarative, deepcopy, bpe_tokeniser, go, k_core, chaos, deltablue, asyncio_websockets, html5lib, python_startup_no_site, pidigits, sqlite_synth, xml_etree_parse, pprint_safe_repr, async_tree_io_tg, pathlib, float, pprint_pformat, subparsers, sympy_str, async_tree_io, async_tree_memoization, typing_runtime_protocols, sphinx, pylint, async_tree_none, async_tree_none_tg, pycparser
Ignored benchmarks (1) of results/bm-20250319-3.14.0a6+-6146295/bm-20250319-linux-x86_64-python-6146295a5b8e9286ccb8-3.14.0a6+-6146295.json: thrift

- Geometric mean (including insignificant results): 1.005x faster

# HPT report

- Reliability score: 99.93% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x