# Results vs. 3.13.0

- fork: kumaraditya303
- ref: fast_state
- machine: linux-aarch64
- commit hash: 7de6e22
- commit date: 2025-01-07
- overall geometric mean: 1.036x faster
- HPT reliability: 99.77%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.04 sec: 1.02x slower                                                 |
| Geometric mean | (ref)                                                    | 1.00x slower                                                           |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------------|:--------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 473 ms: 1.40x faster                                                   |
| async_tree_memoization     | 664 ms                                                   | 495 ms: 1.34x faster                                                   |
| async_tree_io_tg           | 1.16 sec                                                 | 884 ms: 1.32x faster                                                   |
| async_tree_none_tg         | 484 ms                                                   | 372 ms: 1.30x faster                                                   |
| async_tree_none            | 504 ms                                                   | 387 ms: 1.30x faster                                                   |
| async_tree_io              | 1.14 sec                                                 | 888 ms: 1.28x faster                                                   |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 655 ms: 1.22x faster                                                   |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 674 ms: 1.17x faster                                                   |
| Geometric mean             | (ref)                                                    | 1.21x faster                                                           |

Benchmark hidden because not significant (3): async_generators, asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.09 ms: 1.25x faster                                                  |
| regex_dna      | 263 ms                                                   | 251 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                    | 1.07x faster                                                           |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|---------------------|:--------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 182 ms: 1.11x faster                                                   |
| xml_etree_iterparse | 159 ms                                                   | 143 ms: 1.11x faster                                                   |
| tomli_loads         | 2.67 sec                                                 | 2.60 sec: 1.02x faster                                                 |
| Geometric mean      | (ref)                                                    | 1.03x faster                                                           |

Benchmark hidden because not significant (6): json_loads, xml_etree_generate, json_dumps, xml_etree_process, unpickle_pure_python, pickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|-----------------|:--------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 39.4 ms                                                  | 40.5 ms: 1.03x slower                                                  |
| Geometric mean  | (ref)                                                    | 1.02x slower                                                           |

Benchmark hidden because not significant (3): genshi_text, mako, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------------|:--------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy                   | 479 us                                                   | 338 us: 1.42x faster                                                   |
| async_tree_memoization_tg  | 663 ms                                                   | 473 ms: 1.40x faster                                                   |
| async_tree_memoization     | 664 ms                                                   | 495 ms: 1.34x faster                                                   |
| async_tree_io_tg           | 1.16 sec                                                 | 884 ms: 1.32x faster                                                   |
| async_tree_none_tg         | 484 ms                                                   | 372 ms: 1.30x faster                                                   |
| async_tree_none            | 504 ms                                                   | 387 ms: 1.30x faster                                                   |
| deepcopy_memo              | 53.0 us                                                  | 41.1 us: 1.29x faster                                                  |
| async_tree_io              | 1.14 sec                                                 | 888 ms: 1.28x faster                                                   |
| regex_effbot               | 5.10 ms                                                  | 4.09 ms: 1.25x faster                                                  |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 655 ms: 1.22x faster                                                   |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 674 ms: 1.17x faster                                                   |
| deepcopy_reduce            | 4.24 us                                                  | 3.69 us: 1.15x faster                                                  |
| pylint                     | 345 ms                                                   | 307 ms: 1.12x faster                                                   |
| go                         | 164 ms                                                   | 146 ms: 1.12x faster                                                   |
| xml_etree_parse            | 203 ms                                                   | 182 ms: 1.11x faster                                                   |
| xml_etree_iterparse        | 159 ms                                                   | 143 ms: 1.11x faster                                                   |
| pathlib                    | 24.3 ms                                                  | 22.2 ms: 1.10x faster                                                  |
| generators                 | 40.3 ms                                                  | 37.1 ms: 1.09x faster                                                  |
| scimark_fft                | 463 ms                                                   | 427 ms: 1.08x faster                                                   |
| spectral_norm              | 143 ms                                                   | 133 ms: 1.08x faster                                                   |
| telco                      | 10.5 ms                                                  | 9.68 ms: 1.08x faster                                                  |
| sqlalchemy_declarative     | 154 ms                                                   | 145 ms: 1.06x faster                                                   |
| json                       | 5.94 ms                                                  | 5.62 ms: 1.06x faster                                                  |
| scimark_lu                 | 146 ms                                                   | 139 ms: 1.05x faster                                                   |
| richards                   | 54.5 ms                                                  | 52.1 ms: 1.05x faster                                                  |
| regex_dna                  | 263 ms                                                   | 251 ms: 1.05x faster                                                   |
| pycparser                  | 1.34 sec                                                 | 1.29 sec: 1.04x faster                                                 |
| bpe_tokeniser              | 6.02 sec                                                 | 5.79 sec: 1.04x faster                                                 |
| tomli_loads                | 2.67 sec                                                 | 2.60 sec: 1.02x faster                                                 |
| sympy_str                  | 265 ms                                                   | 270 ms: 1.02x slower                                                   |
| docutils                   | 2.96 sec                                                 | 3.04 sec: 1.02x slower                                                 |
| django_template            | 39.4 ms                                                  | 40.5 ms: 1.03x slower                                                  |
| raytrace                   | 310 ms                                                   | 326 ms: 1.05x slower                                                   |
| typing_runtime_protocols   | 197 us                                                   | 207 us: 1.05x slower                                                   |
| comprehensions             | 20.8 us                                                  | 22.1 us: 1.06x slower                                                  |
| create_gc_cycles           | 3.39 ms                                                  | 3.68 ms: 1.08x slower                                                  |
| many_optionals             | 626 us                                                   | 726 us: 1.16x slower                                                   |
| gc_traversal               | 5.92 ms                                                  | 6.99 ms: 1.18x slower                                                  |
| subparsers                 | 20.3 ms                                                  | 26.0 ms: 1.28x slower                                                  |
| bench_mp_pool              | 8.07 ms                                                  | 5.70 sec: 706.07x slower                                               |
| Geometric mean             | (ref)                                                    | 1.03x slower                                                           |

Benchmark hidden because not significant (55): regex_compile, sympy_sum, coverage, scimark_sor, json_loads, float, sqlalchemy_imperative, xml_etree_generate, genshi_text, sqlglot_optimize, logging_format, 2to3, async_generators, sphinx, logging_simple, json_dumps, k_core, scimark_sparse_mat_mult, thrift, richards_super, xml_etree_process, pprint_pformat, mdp, unpickle_pure_python, scimark_monte_carlo, asyncio_websockets, deltablue, coroutines, pprint_safe_repr, python_startup, sqlglot_transpile, crypto_pyaes, shortest_path, connected_components, sqlglot_normalize, python_startup_no_site, meteor_contest, bench_thread_pool, pidigits, sqlglot_parse, chaos, nqueens, sympy_integrate, sympy_expand, sqlite_synth, pyflate, hexiom, regex_v8, mako, nbody, fannkuch, html5lib, logging_silent, genshi_xml, pickle_pure_python
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (2) of results/bm-20250107-3.14.0a3+-7de6e22/bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22.json: dulwich_log, mypy2

- Geometric mean (including insignificant results): 1.036x faster

# HPT report

- Reliability score: 99.77% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x