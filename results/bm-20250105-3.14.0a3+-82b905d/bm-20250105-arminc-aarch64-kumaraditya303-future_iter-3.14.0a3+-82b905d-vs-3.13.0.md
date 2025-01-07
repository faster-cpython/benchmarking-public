# Results vs. 3.13.0

- fork: kumaraditya303
- ref: future_iter
- machine: linux-aarch64
- commit hash: 82b905d
- commit date: 2025-01-05
- overall geometric mean: 1.040x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250105-arminc-aarch64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.01 sec: 1.01x slower                                                  |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250105-arminc-aarch64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 461 ms: 1.44x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 486 ms: 1.37x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 862 ms: 1.35x faster                                                    |
| async_tree_none            | 504 ms                                                   | 386 ms: 1.31x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 875 ms: 1.30x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 376 ms: 1.29x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 651 ms: 1.23x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 670 ms: 1.18x faster                                                    |
| Geometric mean             | (ref)                                                    | 1.22x faster                                                            |

Benchmark hidden because not significant (3): coroutines, async_generators, asyncio_websockets

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250105-arminc-aarch64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.06 ms: 1.26x faster                                                   |
| regex_dna      | 263 ms                                                   | 245 ms: 1.07x faster                                                    |
| Geometric mean | (ref)                                                    | 1.09x faster                                                            |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250105-arminc-aarch64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse | 159 ms                                                   | 140 ms: 1.14x faster                                                    |
| xml_etree_parse     | 203 ms                                                   | 180 ms: 1.12x faster                                                    |
| tomli_loads         | 2.67 sec                                                 | 2.62 sec: 1.02x faster                                                  |
| Geometric mean      | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (6): json_loads, xml_etree_generate, unpickle_pure_python, xml_etree_process, json_dumps, pickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250105-arminc-aarch64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 39.4 ms                                                  | 42.0 ms: 1.07x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.04x slower                                                            |

Benchmark hidden because not significant (3): mako, genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250105-arminc-aarch64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 461 ms: 1.44x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 486 ms: 1.37x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 862 ms: 1.35x faster                                                    |
| deepcopy                   | 479 us                                                   | 356 us: 1.34x faster                                                    |
| async_tree_none            | 504 ms                                                   | 386 ms: 1.31x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 875 ms: 1.30x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 376 ms: 1.29x faster                                                    |
| deepcopy_memo              | 53.0 us                                                  | 41.3 us: 1.28x faster                                                   |
| regex_effbot               | 5.10 ms                                                  | 4.06 ms: 1.26x faster                                                   |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 651 ms: 1.23x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 670 ms: 1.18x faster                                                    |
| deepcopy_reduce            | 4.24 us                                                  | 3.72 us: 1.14x faster                                                   |
| go                         | 164 ms                                                   | 144 ms: 1.14x faster                                                    |
| xml_etree_iterparse        | 159 ms                                                   | 140 ms: 1.14x faster                                                    |
| xml_etree_parse            | 203 ms                                                   | 180 ms: 1.12x faster                                                    |
| pylint                     | 345 ms                                                   | 308 ms: 1.12x faster                                                    |
| pathlib                    | 24.3 ms                                                  | 21.8 ms: 1.12x faster                                                   |
| generators                 | 40.3 ms                                                  | 36.3 ms: 1.11x faster                                                   |
| spectral_norm              | 143 ms                                                   | 129 ms: 1.11x faster                                                    |
| scimark_sor                | 164 ms                                                   | 151 ms: 1.09x faster                                                    |
| json                       | 5.94 ms                                                  | 5.52 ms: 1.08x faster                                                   |
| scimark_fft                | 463 ms                                                   | 430 ms: 1.08x faster                                                    |
| regex_dna                  | 263 ms                                                   | 245 ms: 1.07x faster                                                    |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 6.22 ms: 1.07x faster                                                   |
| scimark_lu                 | 146 ms                                                   | 137 ms: 1.06x faster                                                    |
| pycparser                  | 1.34 sec                                                 | 1.28 sec: 1.05x faster                                                  |
| k_core                     | 2.99 sec                                                 | 2.85 sec: 1.05x faster                                                  |
| bpe_tokeniser              | 6.02 sec                                                 | 5.78 sec: 1.04x faster                                                  |
| tomli_loads                | 2.67 sec                                                 | 2.62 sec: 1.02x faster                                                  |
| docutils                   | 2.96 sec                                                 | 3.01 sec: 1.01x slower                                                  |
| typing_runtime_protocols   | 197 us                                                   | 206 us: 1.04x slower                                                    |
| create_gc_cycles           | 3.39 ms                                                  | 3.60 ms: 1.06x slower                                                   |
| django_template            | 39.4 ms                                                  | 42.0 ms: 1.07x slower                                                   |
| comprehensions             | 20.8 us                                                  | 22.3 us: 1.07x slower                                                   |
| sympy_str                  | 265 ms                                                   | 286 ms: 1.08x slower                                                    |
| many_optionals             | 626 us                                                   | 695 us: 1.11x slower                                                    |
| gc_traversal               | 5.92 ms                                                  | 6.69 ms: 1.13x slower                                                   |
| subparsers                 | 20.3 ms                                                  | 25.4 ms: 1.25x slower                                                   |
| bench_mp_pool              | 8.07 ms                                                  | 4.57 sec: 565.88x slower                                                |
| Geometric mean             | (ref)                                                    | 1.03x slower                                                            |

Benchmark hidden because not significant (56): json_loads, telco, sympy_sum, thrift, regex_compile, float, coverage, sqlalchemy_imperative, sqlalchemy_declarative, xml_etree_generate, sphinx, logging_format, sqlglot_transpile, richards, 2to3, coroutines, unpickle_pure_python, nqueens, xml_etree_process, sqlglot_optimize, sqlite_synth, pprint_pformat, mdp, async_generators, regex_v8, bench_thread_pool, pyflate, scimark_monte_carlo, asyncio_websockets, sqlglot_parse, html5lib, pprint_safe_repr, shortest_path, richards_super, json_dumps, hexiom, crypto_pyaes, connected_components, deltablue, fannkuch, sqlglot_normalize, python_startup, sympy_expand, logging_simple, python_startup_no_site, logging_silent, chaos, pidigits, mako, genshi_text, sympy_integrate, genshi_xml, raytrace, meteor_contest, pickle_pure_python, nbody
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (2) of results/bm-20250105-3.14.0a3+-82b905d/bm-20250105-arminc-aarch64-kumaraditya303-future_iter-3.14.0a3+-82b905d.json: dulwich_log, mypy2

- Geometric mean (including insignificant results): 1.040x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x