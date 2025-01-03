# Results vs. 3.13.0

- fork: python
- ref: e1baa778f602ede66831
- machine: linux-aarch64
- commit hash: e1baa77
- commit date: 2025-01-02
- overall geometric mean: 1.038x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-arminc-aarch64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.02 sec: 1.02x slower                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-arminc-aarch64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 471 ms: 1.41x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 502 ms: 1.32x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 894 ms: 1.30x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 375 ms: 1.29x faster                                                     |
| async_tree_none            | 504 ms                                                   | 393 ms: 1.28x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 904 ms: 1.26x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 663 ms: 1.21x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 677 ms: 1.17x faster                                                     |
| Geometric mean             | (ref)                                                    | 1.20x faster                                                             |

Benchmark hidden because not significant (3): asyncio_websockets, coroutines, async_generators

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-arminc-aarch64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.99 ms: 1.28x faster                                                    |
| regex_dna      | 263 ms                                                   | 250 ms: 1.05x faster                                                     |
| Geometric mean | (ref)                                                    | 1.09x faster                                                             |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-arminc-aarch64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_iterparse | 159 ms                                                   | 141 ms: 1.13x faster                                                     |
| xml_etree_parse     | 203 ms                                                   | 182 ms: 1.11x faster                                                     |
| tomli_loads         | 2.67 sec                                                 | 2.59 sec: 1.03x faster                                                   |
| Geometric mean      | (ref)                                                    | 1.02x faster                                                             |

Benchmark hidden because not significant (6): json_loads, xml_etree_generate, unpickle_pure_python, xml_etree_process, json_dumps, pickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-arminc-aarch64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 28.6 ms                                                  | 27.4 ms: 1.04x faster                                                    |
| django_template | 39.4 ms                                                  | 41.2 ms: 1.04x slower                                                    |
| Geometric mean  | (ref)                                                    | 1.02x slower                                                             |

Benchmark hidden because not significant (2): mako, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-arminc-aarch64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy                   | 479 us                                                   | 337 us: 1.42x faster                                                     |
| async_tree_memoization_tg  | 663 ms                                                   | 471 ms: 1.41x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 502 ms: 1.32x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 894 ms: 1.30x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 375 ms: 1.29x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 41.3 us: 1.28x faster                                                    |
| async_tree_none            | 504 ms                                                   | 393 ms: 1.28x faster                                                     |
| regex_effbot               | 5.10 ms                                                  | 3.99 ms: 1.28x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 904 ms: 1.26x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 663 ms: 1.21x faster                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 3.59 us: 1.18x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 677 ms: 1.17x faster                                                     |
| go                         | 164 ms                                                   | 143 ms: 1.15x faster                                                     |
| xml_etree_iterparse        | 159 ms                                                   | 141 ms: 1.13x faster                                                     |
| pylint                     | 345 ms                                                   | 307 ms: 1.12x faster                                                     |
| pathlib                    | 24.3 ms                                                  | 21.7 ms: 1.12x faster                                                    |
| spectral_norm              | 143 ms                                                   | 129 ms: 1.12x faster                                                     |
| xml_etree_parse            | 203 ms                                                   | 182 ms: 1.11x faster                                                     |
| telco                      | 10.5 ms                                                  | 9.56 ms: 1.09x faster                                                    |
| thrift                     | 1.01 ms                                                  | 936 us: 1.08x faster                                                     |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 6.20 ms: 1.07x faster                                                    |
| scimark_fft                | 463 ms                                                   | 437 ms: 1.06x faster                                                     |
| sqlalchemy_declarative     | 154 ms                                                   | 145 ms: 1.06x faster                                                     |
| regex_dna                  | 263 ms                                                   | 250 ms: 1.05x faster                                                     |
| pycparser                  | 1.34 sec                                                 | 1.28 sec: 1.05x faster                                                   |
| richards                   | 54.5 ms                                                  | 52.0 ms: 1.05x faster                                                    |
| scimark_lu                 | 146 ms                                                   | 140 ms: 1.05x faster                                                     |
| coverage                   | 106 ms                                                   | 101 ms: 1.05x faster                                                     |
| genshi_text                | 28.6 ms                                                  | 27.4 ms: 1.04x faster                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 5.80 sec: 1.04x faster                                                   |
| tomli_loads                | 2.67 sec                                                 | 2.59 sec: 1.03x faster                                                   |
| k_core                     | 2.99 sec                                                 | 2.90 sec: 1.03x faster                                                   |
| docutils                   | 2.96 sec                                                 | 3.02 sec: 1.02x slower                                                   |
| comprehensions             | 20.8 us                                                  | 21.5 us: 1.03x slower                                                    |
| sympy_str                  | 265 ms                                                   | 275 ms: 1.04x slower                                                     |
| raytrace                   | 310 ms                                                   | 323 ms: 1.04x slower                                                     |
| django_template            | 39.4 ms                                                  | 41.2 ms: 1.04x slower                                                    |
| logging_silent             | 135 ns                                                   | 142 ns: 1.05x slower                                                     |
| create_gc_cycles           | 3.39 ms                                                  | 3.59 ms: 1.06x slower                                                    |
| many_optionals             | 626 us                                                   | 703 us: 1.12x slower                                                     |
| gc_traversal               | 5.92 ms                                                  | 7.00 ms: 1.18x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 26.1 ms: 1.28x slower                                                    |
| bench_mp_pool              | 8.07 ms                                                  | 4.93 sec: 610.63x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.03x slower                                                             |

Benchmark hidden because not significant (53): generators, regex_compile, json, float, sqlglot_optimize, scimark_sor, sympy_sum, logging_format, sqlalchemy_imperative, sphinx, sqlglot_transpile, 2to3, pyflate, scimark_monte_carlo, json_loads, pprint_pformat, mdp, sqlite_synth, asyncio_websockets, nqueens, coroutines, html5lib, async_generators, deltablue, pprint_safe_repr, python_startup, logging_simple, connected_components, djangocms, meteor_contest, fannkuch, crypto_pyaes, typing_runtime_protocols, bench_thread_pool, sqlglot_parse, chaos, xml_etree_generate, unpickle_pure_python, regex_v8, sympy_expand, sqlglot_normalize, xml_etree_process, shortest_path, sympy_integrate, richards_super, json_dumps, python_startup_no_site, pickle_pure_python, hexiom, nbody, mako, pidigits, genshi_xml
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (2) of results/bm-20250102-3.14.0a3+-e1baa77/bm-20250102-arminc-aarch64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77.json: dulwich_log, mypy2

- Geometric mean (including insignificant results): 1.038x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x