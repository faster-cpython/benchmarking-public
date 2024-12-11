# Results vs. base

- fork: eendebakpt
- ref: int_freelist
- machine: linux-x86_64
- commit hash: b034948
- commit date: 2024-12-07
- overall geometric mean: 1.006x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241207-linux-x86_64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab | bm-20241207-linux-x86_64-eendebakpt-int_freelist-3.14.0a2+-b034948 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| docutils       | 2.57 sec                                                               | 2.56 sec: 1.00x faster                                             |
| html5lib       | 63.7 ms                                                                | 63.0 ms: 1.01x faster                                              |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                       |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241207-linux-x86_64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab | bm-20241207-linux-x86_64-eendebakpt-int_freelist-3.14.0a2+-b034948 |
|----------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_generators           | 427 ms                                                                 | 416 ms: 1.03x faster                                               |
| async_tree_cpu_io_mixed_tg | 496 ms                                                                 | 485 ms: 1.02x faster                                               |
| async_tree_cpu_io_mixed    | 499 ms                                                                 | 491 ms: 1.02x faster                                               |
| async_tree_memoization_tg  | 332 ms                                                                 | 329 ms: 1.01x faster                                               |
| coroutines                 | 23.5 ms                                                                | 23.3 ms: 1.01x faster                                              |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                       |

Benchmark hidden because not significant (6): async_tree_none_tg, async_tree_none, async_tree_memoization, async_tree_io_tg, async_tree_io, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241207-linux-x86_64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab | bm-20241207-linux-x86_64-eendebakpt-int_freelist-3.14.0a2+-b034948 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 78.6 ms                                                                | 77.2 ms: 1.02x faster                                              |
| pidigits       | 187 ms                                                                 | 186 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                       |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241207-linux-x86_64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab | bm-20241207-linux-x86_64-eendebakpt-int_freelist-3.14.0a2+-b034948 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 3.39 ms                                                                | 3.30 ms: 1.03x faster                                              |
| regex_v8       | 26.0 ms                                                                | 25.5 ms: 1.02x faster                                              |
| regex_compile  | 129 ms                                                                 | 127 ms: 1.02x faster                                               |
| regex_dna      | 213 ms                                                                 | 217 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241207-linux-x86_64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab | bm-20241207-linux-x86_64-eendebakpt-int_freelist-3.14.0a2+-b034948 |
|----------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 2.13 sec                                                               | 2.03 sec: 1.05x faster                                             |
| json_dumps           | 11.5 ms                                                                | 11.5 ms: 1.01x slower                                              |
| xml_etree_parse      | 145 ms                                                                 | 146 ms: 1.01x slower                                               |
| unpickle_pure_python | 218 us                                                                 | 222 us: 1.02x slower                                               |
| pickle_pure_python   | 320 us                                                                 | 327 us: 1.02x slower                                               |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                       |

Benchmark hidden because not significant (4): xml_etree_process, xml_etree_generate, xml_etree_iterparse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241207-linux-x86_64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab | bm-20241207-linux-x86_64-eendebakpt-int_freelist-3.14.0a2+-b034948 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 7.06 ms                                                                | 7.04 ms: 1.00x faster                                              |
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                              |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241207-linux-x86_64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab | bm-20241207-linux-x86_64-eendebakpt-int_freelist-3.14.0a2+-b034948 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text    | 22.9 ms                                                                | 22.6 ms: 1.01x faster                                              |
| mako           | 11.4 ms                                                                | 11.4 ms: 1.00x slower                                              |
| genshi_xml     | 50.1 ms                                                                | 50.5 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                       |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241207-linux-x86_64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab | bm-20241207-linux-x86_64-eendebakpt-int_freelist-3.14.0a2+-b034948 |
|----------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| scimark_sparse_mat_mult    | 5.02 ms                                                                | 4.63 ms: 1.08x faster                                              |
| tomli_loads                | 2.13 sec                                                               | 2.03 sec: 1.05x faster                                             |
| gc_traversal               | 4.72 ms                                                                | 4.50 ms: 1.05x faster                                              |
| spectral_norm              | 112 ms                                                                 | 108 ms: 1.04x faster                                               |
| scimark_fft                | 369 ms                                                                 | 356 ms: 1.04x faster                                               |
| regex_effbot               | 3.39 ms                                                                | 3.30 ms: 1.03x faster                                              |
| async_generators           | 427 ms                                                                 | 416 ms: 1.03x faster                                               |
| create_gc_cycles           | 2.27 ms                                                                | 2.22 ms: 1.02x faster                                              |
| pathlib                    | 16.6 ms                                                                | 16.2 ms: 1.02x faster                                              |
| logging_silent             | 108 ns                                                                 | 105 ns: 1.02x faster                                               |
| async_tree_cpu_io_mixed_tg | 496 ms                                                                 | 485 ms: 1.02x faster                                               |
| regex_v8                   | 26.0 ms                                                                | 25.5 ms: 1.02x faster                                              |
| float                      | 78.6 ms                                                                | 77.2 ms: 1.02x faster                                              |
| raytrace                   | 273 ms                                                                 | 268 ms: 1.02x faster                                               |
| richards                   | 46.5 ms                                                                | 45.7 ms: 1.02x faster                                              |
| telco                      | 7.95 ms                                                                | 7.81 ms: 1.02x faster                                              |
| json                       | 4.86 ms                                                                | 4.78 ms: 1.02x faster                                              |
| async_tree_cpu_io_mixed    | 499 ms                                                                 | 491 ms: 1.02x faster                                               |
| subparsers                 | 21.0 ms                                                                | 20.7 ms: 1.02x faster                                              |
| regex_compile              | 129 ms                                                                 | 127 ms: 1.02x faster                                               |
| sqlglot_parse              | 1.30 ms                                                                | 1.28 ms: 1.02x faster                                              |
| mdp                        | 2.72 sec                                                               | 2.68 sec: 1.01x faster                                             |
| genshi_text                | 22.9 ms                                                                | 22.6 ms: 1.01x faster                                              |
| k_core                     | 2.22 sec                                                               | 2.19 sec: 1.01x faster                                             |
| crypto_pyaes               | 72.9 ms                                                                | 72.0 ms: 1.01x faster                                              |
| deltablue                  | 3.28 ms                                                                | 3.24 ms: 1.01x faster                                              |
| scimark_sor                | 126 ms                                                                 | 125 ms: 1.01x faster                                               |
| richards_super             | 52.6 ms                                                                | 52.0 ms: 1.01x faster                                              |
| html5lib                   | 63.7 ms                                                                | 63.0 ms: 1.01x faster                                              |
| sqlglot_transpile          | 1.61 ms                                                                | 1.59 ms: 1.01x faster                                              |
| sqlglot_normalize          | 108 ms                                                                 | 107 ms: 1.01x faster                                               |
| dulwich_log                | 64.9 ms                                                                | 64.3 ms: 1.01x faster                                              |
| fannkuch                   | 411 ms                                                                 | 408 ms: 1.01x faster                                               |
| many_optionals             | 955 us                                                                 | 947 us: 1.01x faster                                               |
| async_tree_memoization_tg  | 332 ms                                                                 | 329 ms: 1.01x faster                                               |
| coroutines                 | 23.5 ms                                                                | 23.3 ms: 1.01x faster                                              |
| sympy_sum                  | 148 ms                                                                 | 147 ms: 1.01x faster                                               |
| sqlglot_optimize           | 53.9 ms                                                                | 53.6 ms: 1.01x faster                                              |
| hexiom                     | 6.34 ms                                                                | 6.30 ms: 1.01x faster                                              |
| pidigits                   | 187 ms                                                                 | 186 ms: 1.01x faster                                               |
| docutils                   | 2.57 sec                                                               | 2.56 sec: 1.00x faster                                             |
| nqueens                    | 81.4 ms                                                                | 81.1 ms: 1.00x faster                                              |
| python_startup_no_site     | 7.06 ms                                                                | 7.04 ms: 1.00x faster                                              |
| pyflate                    | 453 ms                                                                 | 452 ms: 1.00x faster                                               |
| go                         | 119 ms                                                                 | 119 ms: 1.00x faster                                               |
| python_startup             | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                              |
| mako                       | 11.4 ms                                                                | 11.4 ms: 1.00x slower                                              |
| sympy_integrate            | 19.9 ms                                                                | 20.0 ms: 1.00x slower                                              |
| meteor_contest             | 106 ms                                                                 | 107 ms: 1.00x slower                                               |
| pprint_pformat             | 1.50 sec                                                               | 1.51 sec: 1.00x slower                                             |
| json_dumps                 | 11.5 ms                                                                | 11.5 ms: 1.01x slower                                              |
| chaos                      | 60.7 ms                                                                | 61.1 ms: 1.01x slower                                              |
| xml_etree_parse            | 145 ms                                                                 | 146 ms: 1.01x slower                                               |
| logging_format             | 6.14 us                                                                | 6.19 us: 1.01x slower                                              |
| genshi_xml                 | 50.1 ms                                                                | 50.5 ms: 1.01x slower                                              |
| unpickle_pure_python       | 218 us                                                                 | 222 us: 1.02x slower                                               |
| deepcopy_memo              | 30.8 us                                                                | 31.3 us: 1.02x slower                                              |
| regex_dna                  | 213 ms                                                                 | 217 ms: 1.02x slower                                               |
| pickle_pure_python         | 320 us                                                                 | 327 us: 1.02x slower                                               |
| djangocms                  | 21.8 us                                                                | 22.3 us: 1.02x slower                                              |
| pycparser                  | 1.11 sec                                                               | 1.15 sec: 1.04x slower                                             |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                       |

Benchmark hidden because not significant (37): async_tree_none_tg, sphinx, sqlite_synth, async_tree_none, connected_components, xml_etree_process, async_tree_memoization, django_template, sqlalchemy_imperative, pylint, bench_mp_pool, sympy_expand, mypy2, comprehensions, deepcopy, sqlalchemy_declarative, xml_etree_generate, scimark_monte_carlo, coverage, 2to3, bpe_tokeniser, thrift, sympy_str, generators, bench_thread_pool, xml_etree_iterparse, async_tree_io_tg, deepcopy_reduce, json_loads, typing_runtime_protocols, async_tree_io, shortest_path, asyncio_websockets, pprint_safe_repr, nbody, scimark_lu, logging_simple

- Geometric mean (including insignificant results): 1.006x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x