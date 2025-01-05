# Results vs. 3.13.0

- fork: python
- ref: 0cafa97932c6574734bb
- machine: linux-aarch64
- commit hash: 0cafa97
- commit date: 2025-01-04
- overall geometric mean: 1.032x faster
- HPT reliability: 99.78%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.03 sec: 1.02x slower                                                   |
| html5lib       | 65.6 ms                                                  | 63.8 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 479 ms: 1.38x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 508 ms: 1.31x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 896 ms: 1.30x faster                                                     |
| async_tree_none            | 504 ms                                                   | 395 ms: 1.27x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 382 ms: 1.27x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 928 ms: 1.23x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 669 ms: 1.20x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 687 ms: 1.15x faster                                                     |
| async_generators           | 500 ms                                                   | 486 ms: 1.03x faster                                                     |
| Geometric mean             | (ref)                                                    | 1.19x faster                                                             |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.07 ms: 1.25x faster                                                    |
| Geometric mean | (ref)                                                    | 1.06x faster                                                             |

Benchmark hidden because not significant (3): regex_compile, regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 187 ms: 1.08x faster                                                     |
| xml_etree_iterparse | 159 ms                                                   | 148 ms: 1.08x faster                                                     |
| pickle_pure_python  | 374 us                                                   | 401 us: 1.07x slower                                                     |
| Geometric mean      | (ref)                                                    | 1.00x slower                                                             |

Benchmark hidden because not significant (6): tomli_loads, json_loads, unpickle_pure_python, json_dumps, xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 9.05 ms: 1.03x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.02x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 39.4 ms                                                  | 41.4 ms: 1.05x slower                                                    |
| Geometric mean  | (ref)                                                    | 1.03x slower                                                             |

Benchmark hidden because not significant (3): mako, genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy                   | 479 us                                                   | 342 us: 1.40x faster                                                     |
| async_tree_memoization_tg  | 663 ms                                                   | 479 ms: 1.38x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 508 ms: 1.31x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 896 ms: 1.30x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 41.1 us: 1.29x faster                                                    |
| async_tree_none            | 504 ms                                                   | 395 ms: 1.27x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 382 ms: 1.27x faster                                                     |
| regex_effbot               | 5.10 ms                                                  | 4.07 ms: 1.25x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 928 ms: 1.23x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 669 ms: 1.20x faster                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 3.60 us: 1.18x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 687 ms: 1.15x faster                                                     |
| pylint                     | 345 ms                                                   | 306 ms: 1.13x faster                                                     |
| pathlib                    | 24.3 ms                                                  | 21.7 ms: 1.12x faster                                                    |
| telco                      | 10.5 ms                                                  | 9.48 ms: 1.10x faster                                                    |
| go                         | 164 ms                                                   | 150 ms: 1.10x faster                                                     |
| generators                 | 40.3 ms                                                  | 36.9 ms: 1.09x faster                                                    |
| spectral_norm              | 143 ms                                                   | 132 ms: 1.08x faster                                                     |
| scimark_fft                | 463 ms                                                   | 427 ms: 1.08x faster                                                     |
| xml_etree_parse            | 203 ms                                                   | 187 ms: 1.08x faster                                                     |
| xml_etree_iterparse        | 159 ms                                                   | 148 ms: 1.08x faster                                                     |
| sqlalchemy_imperative      | 16.1 ms                                                  | 15.3 ms: 1.05x faster                                                    |
| pycparser                  | 1.34 sec                                                 | 1.29 sec: 1.05x faster                                                   |
| bpe_tokeniser              | 6.02 sec                                                 | 5.77 sec: 1.04x faster                                                   |
| async_generators           | 500 ms                                                   | 486 ms: 1.03x faster                                                     |
| html5lib                   | 65.6 ms                                                  | 63.8 ms: 1.03x faster                                                    |
| k_core                     | 2.99 sec                                                 | 2.93 sec: 1.02x faster                                                   |
| docutils                   | 2.96 sec                                                 | 3.03 sec: 1.02x slower                                                   |
| python_startup_no_site     | 8.79 ms                                                  | 9.05 ms: 1.03x slower                                                    |
| raytrace                   | 310 ms                                                   | 324 ms: 1.05x slower                                                     |
| django_template            | 39.4 ms                                                  | 41.4 ms: 1.05x slower                                                    |
| comprehensions             | 20.8 us                                                  | 21.9 us: 1.05x slower                                                    |
| typing_runtime_protocols   | 197 us                                                   | 210 us: 1.06x slower                                                     |
| create_gc_cycles           | 3.39 ms                                                  | 3.61 ms: 1.06x slower                                                    |
| pickle_pure_python         | 374 us                                                   | 401 us: 1.07x slower                                                     |
| many_optionals             | 626 us                                                   | 708 us: 1.13x slower                                                     |
| gc_traversal               | 5.92 ms                                                  | 6.83 ms: 1.15x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 25.6 ms: 1.26x slower                                                    |
| bench_mp_pool              | 8.07 ms                                                  | 4.34 sec: 537.86x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.04x slower                                                             |

Benchmark hidden because not significant (57): scimark_lu, float, coverage, json, scimark_sparse_mat_mult, logging_format, regex_compile, sqlglot_transpile, richards, sympy_sum, 2to3, thrift, sqlalchemy_declarative, pprint_pformat, scimark_sor, bench_thread_pool, meteor_contest, tomli_loads, json_loads, coroutines, richards_super, sphinx, scimark_monte_carlo, logging_simple, nqueens, sqlite_synth, crypto_pyaes, djangocms, mdp, pidigits, sympy_expand, pprint_safe_repr, hexiom, connected_components, asyncio_websockets, regex_dna, sympy_integrate, python_startup, deltablue, shortest_path, regex_v8, mako, unpickle_pure_python, json_dumps, sqlglot_normalize, sqlglot_optimize, pyflate, fannkuch, sqlglot_parse, genshi_text, genshi_xml, sympy_str, logging_silent, xml_etree_process, xml_etree_generate, chaos, nbody
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (2) of results/bm-20250104-3.14.0a3+-0cafa97/bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json: dulwich_log, mypy2

- Geometric mean (including insignificant results): 1.032x faster

# HPT report

- Reliability score: 99.78% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x