# Results vs. 3.13.0

- fork: python
- ref: 22a442181d5f1ac496da
- machine: linux-aarch64
- commit hash: 22a4421
- commit date: 2025-01-11
- overall geometric mean: 1.041x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 303 ms: 1.03x faster                                                     |
| docutils       | 2.96 sec                                                 | 3.02 sec: 1.02x slower                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 474 ms: 1.40x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 495 ms: 1.34x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 367 ms: 1.32x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 883 ms: 1.32x faster                                                     |
| async_tree_none            | 504 ms                                                   | 389 ms: 1.30x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 889 ms: 1.28x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 667 ms: 1.20x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 679 ms: 1.16x faster                                                     |
| Geometric mean             | (ref)                                                    | 1.21x faster                                                             |

Benchmark hidden because not significant (3): coroutines, async_generators, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 89.1 ms: 1.07x faster                                                    |
| Geometric mean | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.11 ms: 1.24x faster                                                    |
| regex_compile  | 134 ms                                                   | 125 ms: 1.07x faster                                                     |
| regex_dna      | 263 ms                                                   | 250 ms: 1.05x faster                                                     |
| Geometric mean | (ref)                                                    | 1.09x faster                                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 180 ms: 1.13x faster                                                     |
| xml_etree_iterparse | 159 ms                                                   | 143 ms: 1.11x faster                                                     |
| tomli_loads         | 2.67 sec                                                 | 2.60 sec: 1.02x faster                                                   |
| Geometric mean      | (ref)                                                    | 1.02x faster                                                             |

Benchmark hidden because not significant (6): json_loads, xml_etree_generate, unpickle_pure_python, xml_etree_process, pickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 9.01 ms: 1.02x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.02x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 39.4 ms                                                  | 41.2 ms: 1.05x slower                                                    |
| Geometric mean  | (ref)                                                    | 1.03x slower                                                             |

Benchmark hidden because not significant (3): genshi_text, mako, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 474 ms: 1.40x faster                                                     |
| deepcopy                   | 479 us                                                   | 350 us: 1.37x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 495 ms: 1.34x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 367 ms: 1.32x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 883 ms: 1.32x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 40.2 us: 1.32x faster                                                    |
| async_tree_none            | 504 ms                                                   | 389 ms: 1.30x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 889 ms: 1.28x faster                                                     |
| regex_effbot               | 5.10 ms                                                  | 4.11 ms: 1.24x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 667 ms: 1.20x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 679 ms: 1.16x faster                                                     |
| go                         | 164 ms                                                   | 144 ms: 1.14x faster                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 3.74 us: 1.13x faster                                                    |
| xml_etree_parse            | 203 ms                                                   | 180 ms: 1.13x faster                                                     |
| spectral_norm              | 143 ms                                                   | 129 ms: 1.11x faster                                                     |
| xml_etree_iterparse        | 159 ms                                                   | 143 ms: 1.11x faster                                                     |
| generators                 | 40.3 ms                                                  | 36.6 ms: 1.10x faster                                                    |
| pathlib                    | 24.3 ms                                                  | 22.2 ms: 1.09x faster                                                    |
| scimark_fft                | 463 ms                                                   | 429 ms: 1.08x faster                                                     |
| scimark_sor                | 164 ms                                                   | 152 ms: 1.08x faster                                                     |
| float                      | 95.8 ms                                                  | 89.1 ms: 1.07x faster                                                    |
| regex_compile              | 134 ms                                                   | 125 ms: 1.07x faster                                                     |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 6.24 ms: 1.07x faster                                                    |
| pylint                     | 345 ms                                                   | 324 ms: 1.07x faster                                                     |
| coverage                   | 106 ms                                                   | 99.7 ms: 1.06x faster                                                    |
| pycparser                  | 1.34 sec                                                 | 1.28 sec: 1.05x faster                                                   |
| sqlalchemy_declarative     | 154 ms                                                   | 146 ms: 1.05x faster                                                     |
| regex_dna                  | 263 ms                                                   | 250 ms: 1.05x faster                                                     |
| richards                   | 54.5 ms                                                  | 52.1 ms: 1.05x faster                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 5.75 sec: 1.05x faster                                                   |
| k_core                     | 2.99 sec                                                 | 2.87 sec: 1.04x faster                                                   |
| 2to3                       | 313 ms                                                   | 303 ms: 1.03x faster                                                     |
| tomli_loads                | 2.67 sec                                                 | 2.60 sec: 1.02x faster                                                   |
| docutils                   | 2.96 sec                                                 | 3.02 sec: 1.02x slower                                                   |
| typing_runtime_protocols   | 197 us                                                   | 201 us: 1.02x slower                                                     |
| python_startup_no_site     | 8.79 ms                                                  | 9.01 ms: 1.02x slower                                                    |
| comprehensions             | 20.8 us                                                  | 21.7 us: 1.04x slower                                                    |
| django_template            | 39.4 ms                                                  | 41.2 ms: 1.05x slower                                                    |
| create_gc_cycles           | 3.39 ms                                                  | 3.60 ms: 1.06x slower                                                    |
| many_optionals             | 626 us                                                   | 694 us: 1.11x slower                                                     |
| gc_traversal               | 5.92 ms                                                  | 6.85 ms: 1.16x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 26.9 ms: 1.32x slower                                                    |
| bench_mp_pool              | 8.07 ms                                                  | 4.18 sec: 518.44x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.03x slower                                                             |

Benchmark hidden because not significant (52): json, telco, sqlalchemy_imperative, scimark_lu, coroutines, sqlglot_optimize, html5lib, sympy_sum, pyflate, crypto_pyaes, meteor_contest, nqueens, json_loads, sphinx, logging_format, async_generators, sqlglot_transpile, mdp, asyncio_websockets, scimark_monte_carlo, xml_etree_generate, regex_v8, connected_components, genshi_text, pprint_pformat, fannkuch, unpickle_pure_python, pprint_safe_repr, thrift, deltablue, sqlglot_normalize, bench_thread_pool, sympy_integrate, richards_super, sympy_str, python_startup, shortest_path, mako, pidigits, sympy_expand, xml_etree_process, sqlite_synth, logging_simple, sqlglot_parse, pickle_pure_python, logging_silent, nbody, chaos, raytrace, genshi_xml, hexiom, json_dumps
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (9) of results/bm-20250111-3.14.0a3+-22a4421/bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.041x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.02x