# Results vs. base

- fork: kumaraditya303
- ref: fast_state
- machine: linux-x86_64
- commit hash: 7de6e22
- commit date: 2025-01-07
- overall geometric mean: 1.005x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250105-pythonperf2-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 3.13 sec                                                                     | 3.15 sec: 1.00x slower                                                     |
| html5lib       | 92.5 ms                                                                      | 93.8 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                        | 1.01x slower                                                               |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250105-pythonperf2-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 382 ms                                                                       | 379 ms: 1.01x faster                                                       |
| async_tree_io              | 767 ms                                                                       | 765 ms: 1.00x faster                                                       |
| async_tree_none_tg         | 314 ms                                                                       | 315 ms: 1.00x slower                                                       |
| async_tree_cpu_io_mixed    | 603 ms                                                                       | 605 ms: 1.00x slower                                                       |
| async_tree_cpu_io_mixed_tg | 563 ms                                                                       | 566 ms: 1.00x slower                                                       |
| coroutines                 | 23.2 ms                                                                      | 23.3 ms: 1.00x slower                                                      |
| async_tree_none            | 355 ms                                                                       | 357 ms: 1.01x slower                                                       |
| async_generators           | 509 ms                                                                       | 515 ms: 1.01x slower                                                       |
| Geometric mean             | (ref)                                                                        | 1.00x slower                                                               |

Benchmark hidden because not significant (3): async_tree_io_tg, async_tree_memoization_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250105-pythonperf2-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 106 ms                                                                       | 104 ms: 1.01x faster                                                       |
| pidigits       | 246 ms                                                                       | 248 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                               |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250105-pythonperf2-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 26.7 ms                                                                      | 26.3 ms: 1.01x faster                                                      |
| regex_compile  | 173 ms                                                                       | 172 ms: 1.00x faster                                                       |
| regex_dna      | 243 ms                                                                       | 251 ms: 1.03x slower                                                       |
| regex_effbot   | 3.20 ms                                                                      | 3.31 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                                        | 1.01x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250105-pythonperf2-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 137 ms                                                                       | 134 ms: 1.02x faster                                                       |
| xml_etree_iterparse  | 92.8 ms                                                                      | 91.3 ms: 1.02x faster                                                      |
| tomli_loads          | 2.60 sec                                                                     | 2.62 sec: 1.01x slower                                                     |
| json_loads           | 27.7 us                                                                      | 28.1 us: 1.01x slower                                                      |
| pickle_pure_python   | 506 us                                                                       | 514 us: 1.02x slower                                                       |
| unpickle_pure_python | 320 us                                                                       | 325 us: 1.02x slower                                                       |
| json_dumps           | 14.0 ms                                                                      | 14.4 ms: 1.03x slower                                                      |
| Geometric mean       | (ref)                                                                        | 1.01x slower                                                               |

Benchmark hidden because not significant (2): xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250105-pythonperf2-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 19.2 ms                                                                      | 19.1 ms: 1.00x faster                                                      |
| python_startup_no_site | 12.0 ms                                                                      | 12.0 ms: 1.00x faster                                                      |
| Geometric mean         | (ref)                                                                        | 1.00x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250105-pythonperf2-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|-----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 33.4 ms                                                                      | 33.0 ms: 1.01x faster                                                      |
| django_template | 52.1 ms                                                                      | 53.4 ms: 1.02x slower                                                      |
| Geometric mean  | (ref)                                                                        | 1.00x slower                                                               |

Benchmark hidden because not significant (2): mako, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20250105-pythonperf2-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| scimark_sparse_mat_mult    | 5.74 ms                                                                      | 5.51 ms: 1.04x faster                                                      |
| richards                   | 71.4 ms                                                                      | 70.0 ms: 1.02x faster                                                      |
| xml_etree_parse            | 137 ms                                                                       | 134 ms: 1.02x faster                                                       |
| xml_etree_iterparse        | 92.8 ms                                                                      | 91.3 ms: 1.02x faster                                                      |
| bench_thread_pool          | 1.57 ms                                                                      | 1.55 ms: 1.02x faster                                                      |
| regex_v8                   | 26.7 ms                                                                      | 26.3 ms: 1.01x faster                                                      |
| coverage                   | 107 ms                                                                       | 106 ms: 1.01x faster                                                       |
| genshi_text                | 33.4 ms                                                                      | 33.0 ms: 1.01x faster                                                      |
| raytrace                   | 476 ms                                                                       | 471 ms: 1.01x faster                                                       |
| float                      | 106 ms                                                                       | 104 ms: 1.01x faster                                                       |
| scimark_lu                 | 134 ms                                                                       | 133 ms: 1.01x faster                                                       |
| comprehensions             | 27.4 us                                                                      | 27.2 us: 1.01x faster                                                      |
| meteor_contest             | 157 ms                                                                       | 156 ms: 1.01x faster                                                       |
| asyncio_websockets         | 382 ms                                                                       | 379 ms: 1.01x faster                                                       |
| sympy_sum                  | 184 ms                                                                       | 183 ms: 1.00x faster                                                       |
| nqueens                    | 113 ms                                                                       | 113 ms: 1.00x faster                                                       |
| async_tree_io              | 767 ms                                                                       | 765 ms: 1.00x faster                                                       |
| python_startup             | 19.2 ms                                                                      | 19.1 ms: 1.00x faster                                                      |
| python_startup_no_site     | 12.0 ms                                                                      | 12.0 ms: 1.00x faster                                                      |
| regex_compile              | 173 ms                                                                       | 172 ms: 1.00x faster                                                       |
| shortest_path              | 536 ms                                                                       | 537 ms: 1.00x slower                                                       |
| scimark_fft                | 344 ms                                                                       | 345 ms: 1.00x slower                                                       |
| async_tree_none_tg         | 314 ms                                                                       | 315 ms: 1.00x slower                                                       |
| sqlglot_normalize          | 145 ms                                                                       | 145 ms: 1.00x slower                                                       |
| many_optionals             | 1.16 ms                                                                      | 1.16 ms: 1.00x slower                                                      |
| connected_components       | 500 ms                                                                       | 502 ms: 1.00x slower                                                       |
| async_tree_cpu_io_mixed    | 603 ms                                                                       | 605 ms: 1.00x slower                                                       |
| docutils                   | 3.13 sec                                                                     | 3.15 sec: 1.00x slower                                                     |
| async_tree_cpu_io_mixed_tg | 563 ms                                                                       | 566 ms: 1.00x slower                                                       |
| coroutines                 | 23.2 ms                                                                      | 23.3 ms: 1.00x slower                                                      |
| mypy2                      | 1.30 sec                                                                     | 1.31 sec: 1.01x slower                                                     |
| async_tree_none            | 355 ms                                                                       | 357 ms: 1.01x slower                                                       |
| sympy_expand               | 596 ms                                                                       | 599 ms: 1.01x slower                                                       |
| go                         | 244 ms                                                                       | 245 ms: 1.01x slower                                                       |
| fannkuch                   | 513 ms                                                                       | 516 ms: 1.01x slower                                                       |
| sympy_str                  | 357 ms                                                                       | 359 ms: 1.01x slower                                                       |
| sqlglot_parse              | 2.33 ms                                                                      | 2.35 ms: 1.01x slower                                                      |
| pidigits                   | 246 ms                                                                       | 248 ms: 1.01x slower                                                       |
| crypto_pyaes               | 98.5 ms                                                                      | 99.2 ms: 1.01x slower                                                      |
| thrift                     | 1.10 ms                                                                      | 1.11 ms: 1.01x slower                                                      |
| pprint_safe_repr           | 1.03 sec                                                                     | 1.04 sec: 1.01x slower                                                     |
| sqlalchemy_declarative     | 199 ms                                                                       | 201 ms: 1.01x slower                                                       |
| bpe_tokeniser              | 5.59 sec                                                                     | 5.63 sec: 1.01x slower                                                     |
| k_core                     | 2.44 sec                                                                     | 2.46 sec: 1.01x slower                                                     |
| subparsers                 | 28.1 ms                                                                      | 28.3 ms: 1.01x slower                                                      |
| tomli_loads                | 2.60 sec                                                                     | 2.62 sec: 1.01x slower                                                     |
| logging_format             | 9.49 us                                                                      | 9.59 us: 1.01x slower                                                      |
| sqlglot_transpile          | 2.79 ms                                                                      | 2.82 ms: 1.01x slower                                                      |
| logging_silent             | 162 ns                                                                       | 164 ns: 1.01x slower                                                       |
| logging_simple             | 8.62 us                                                                      | 8.72 us: 1.01x slower                                                      |
| json_loads                 | 27.7 us                                                                      | 28.1 us: 1.01x slower                                                      |
| async_generators           | 509 ms                                                                       | 515 ms: 1.01x slower                                                       |
| deepcopy_memo              | 38.7 us                                                                      | 39.2 us: 1.01x slower                                                      |
| html5lib                   | 92.5 ms                                                                      | 93.8 ms: 1.01x slower                                                      |
| json                       | 5.51 ms                                                                      | 5.59 ms: 1.01x slower                                                      |
| pprint_pformat             | 2.14 sec                                                                     | 2.17 sec: 1.01x slower                                                     |
| pickle_pure_python         | 506 us                                                                       | 514 us: 1.02x slower                                                       |
| unpickle_pure_python       | 320 us                                                                       | 325 us: 1.02x slower                                                       |
| typing_runtime_protocols   | 227 us                                                                       | 231 us: 1.02x slower                                                       |
| scimark_sor                | 191 ms                                                                       | 194 ms: 1.02x slower                                                       |
| deepcopy                   | 342 us                                                                       | 348 us: 1.02x slower                                                       |
| deepcopy_reduce            | 3.69 us                                                                      | 3.78 us: 1.02x slower                                                      |
| django_template            | 52.1 ms                                                                      | 53.4 ms: 1.02x slower                                                      |
| chaos                      | 94.1 ms                                                                      | 96.4 ms: 1.02x slower                                                      |
| scimark_monte_carlo        | 106 ms                                                                       | 109 ms: 1.03x slower                                                       |
| pycparser                  | 1.41 sec                                                                     | 1.45 sec: 1.03x slower                                                     |
| json_dumps                 | 14.0 ms                                                                      | 14.4 ms: 1.03x slower                                                      |
| regex_dna                  | 243 ms                                                                       | 251 ms: 1.03x slower                                                       |
| regex_effbot               | 3.20 ms                                                                      | 3.31 ms: 1.03x slower                                                      |
| spectral_norm              | 101 ms                                                                       | 105 ms: 1.04x slower                                                       |
| create_gc_cycles           | 2.71 ms                                                                      | 2.84 ms: 1.05x slower                                                      |
| Geometric mean             | (ref)                                                                        | 1.00x slower                                                               |

Benchmark hidden because not significant (26): gc_traversal, async_tree_io_tg, richards_super, generators, bench_mp_pool, xml_etree_process, mako, sympy_integrate, telco, deltablue, mdp, async_tree_memoization_tg, pathlib, hexiom, dulwich_log, xml_etree_generate, pylint, sqlite_synth, pyflate, async_tree_memoization, 2to3, genshi_xml, sqlglot_optimize, sphinx, sqlalchemy_imperative, nbody

- Geometric mean (including insignificant results): 1.005x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x