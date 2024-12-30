# Results vs. 3.13.0

- fork: python
- ref: f9a5a3a3ef34e63dc197
- machine: linux-aarch64
- commit hash: f9a5a3a
- commit date: 2024-12-28
- overall geometric mean: 1.032x faster
- HPT reliability: 99.39%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.04 sec: 1.03x slower                                                   |
| Geometric mean | (ref)                                                    | 1.00x faster                                                             |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 486 ms: 1.36x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 910 ms: 1.28x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 519 ms: 1.28x faster                                                     |
| async_tree_none            | 504 ms                                                   | 407 ms: 1.24x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 391 ms: 1.24x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 929 ms: 1.23x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 679 ms: 1.18x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 694 ms: 1.14x faster                                                     |
| async_generators           | 500 ms                                                   | 488 ms: 1.03x faster                                                     |
| Geometric mean             | (ref)                                                    | 1.17x faster                                                             |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.07 ms: 1.25x faster                                                    |
| regex_dna      | 263 ms                                                   | 247 ms: 1.07x faster                                                     |
| Geometric mean | (ref)                                                    | 1.07x faster                                                             |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_iterparse | 159 ms                                                   | 143 ms: 1.11x faster                                                     |
| xml_etree_parse     | 203 ms                                                   | 190 ms: 1.07x faster                                                     |
| tomli_loads         | 2.67 sec                                                 | 2.61 sec: 1.02x faster                                                   |
| Geometric mean      | (ref)                                                    | 1.00x faster                                                             |

Benchmark hidden because not significant (6): xml_etree_generate, xml_etree_process, json_loads, unpickle_pure_python, json_dumps, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 9.03 ms: 1.03x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.02x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 39.4 ms                                                  | 40.5 ms: 1.03x slower                                                    |
| Geometric mean  | (ref)                                                    | 1.02x slower                                                             |

Benchmark hidden because not significant (3): genshi_text, mako, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy                   | 479 us                                                   | 344 us: 1.39x faster                                                     |
| async_tree_memoization_tg  | 663 ms                                                   | 486 ms: 1.36x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 41.1 us: 1.29x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 910 ms: 1.28x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 519 ms: 1.28x faster                                                     |
| regex_effbot               | 5.10 ms                                                  | 4.07 ms: 1.25x faster                                                    |
| async_tree_none            | 504 ms                                                   | 407 ms: 1.24x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 391 ms: 1.24x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 929 ms: 1.23x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 679 ms: 1.18x faster                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 3.67 us: 1.16x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 694 ms: 1.14x faster                                                     |
| go                         | 164 ms                                                   | 145 ms: 1.14x faster                                                     |
| xml_etree_iterparse        | 159 ms                                                   | 143 ms: 1.11x faster                                                     |
| generators                 | 40.3 ms                                                  | 36.6 ms: 1.10x faster                                                    |
| pathlib                    | 24.3 ms                                                  | 22.3 ms: 1.09x faster                                                    |
| telco                      | 10.5 ms                                                  | 9.65 ms: 1.08x faster                                                    |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 6.16 ms: 1.08x faster                                                    |
| spectral_norm              | 143 ms                                                   | 133 ms: 1.08x faster                                                     |
| scimark_fft                | 463 ms                                                   | 429 ms: 1.08x faster                                                     |
| xml_etree_parse            | 203 ms                                                   | 190 ms: 1.07x faster                                                     |
| regex_dna                  | 263 ms                                                   | 247 ms: 1.07x faster                                                     |
| scimark_lu                 | 146 ms                                                   | 139 ms: 1.05x faster                                                     |
| k_core                     | 2.99 sec                                                 | 2.86 sec: 1.05x faster                                                   |
| pycparser                  | 1.34 sec                                                 | 1.29 sec: 1.04x faster                                                   |
| bpe_tokeniser              | 6.02 sec                                                 | 5.79 sec: 1.04x faster                                                   |
| richards                   | 54.5 ms                                                  | 52.6 ms: 1.04x faster                                                    |
| async_generators           | 500 ms                                                   | 488 ms: 1.03x faster                                                     |
| tomli_loads                | 2.67 sec                                                 | 2.61 sec: 1.02x faster                                                   |
| pprint_pformat             | 1.99 sec                                                 | 2.03 sec: 1.02x slower                                                   |
| typing_runtime_protocols   | 197 us                                                   | 202 us: 1.02x slower                                                     |
| python_startup_no_site     | 8.79 ms                                                  | 9.03 ms: 1.03x slower                                                    |
| docutils                   | 2.96 sec                                                 | 3.04 sec: 1.03x slower                                                   |
| django_template            | 39.4 ms                                                  | 40.5 ms: 1.03x slower                                                    |
| pprint_safe_repr           | 962 ms                                                   | 996 ms: 1.04x slower                                                     |
| logging_silent             | 135 ns                                                   | 141 ns: 1.05x slower                                                     |
| sympy_str                  | 265 ms                                                   | 277 ms: 1.05x slower                                                     |
| create_gc_cycles           | 3.39 ms                                                  | 3.57 ms: 1.05x slower                                                    |
| comprehensions             | 20.8 us                                                  | 22.4 us: 1.08x slower                                                    |
| many_optionals             | 626 us                                                   | 724 us: 1.16x slower                                                     |
| gc_traversal               | 5.92 ms                                                  | 6.90 ms: 1.17x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 26.8 ms: 1.32x slower                                                    |
| bench_mp_pool              | 8.07 ms                                                  | 6.30 sec: 781.41x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.04x slower                                                             |

Benchmark hidden because not significant (53): pylint, json, scimark_sor, coverage, sqlalchemy_declarative, sympy_sum, genshi_text, scimark_monte_carlo, thrift, logging_format, regex_compile, xml_etree_generate, 2to3, sphinx, sqlalchemy_imperative, sqlglot_optimize, mdp, coroutines, float, bench_thread_pool, logging_simple, html5lib, richards_super, nqueens, sqlite_synth, asyncio_websockets, meteor_contest, crypto_pyaes, deltablue, sqlglot_normalize, fannkuch, shortest_path, connected_components, sqlglot_transpile, xml_etree_process, json_loads, pyflate, python_startup, djangocms, sympy_expand, pidigits, mako, chaos, sqlglot_parse, hexiom, sympy_integrate, regex_v8, unpickle_pure_python, raytrace, genshi_xml, json_dumps, pickle_pure_python, nbody
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (2) of results/bm-20241228-3.14.0a3+-f9a5a3a/bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json: dulwich_log, mypy2

- Geometric mean (including insignificant results): 1.032x faster

# HPT report

- Reliability score: 99.39% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x