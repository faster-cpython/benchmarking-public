# Results vs. 3.13.0

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: linux-aarch64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.044x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 296 ms: 1.06x faster                                                     |
| sphinx         | 1.20 sec                                                 | 1.16 sec: 1.04x faster                                                   |
| Geometric mean | (ref)                                                    | 1.03x faster                                                             |

Benchmark hidden because not significant (2): docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 461 ms: 1.44x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 465 ms: 1.43x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 368 ms: 1.31x faster                                                     |
| async_tree_none            | 504 ms                                                   | 386 ms: 1.31x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 882 ms: 1.29x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 907 ms: 1.28x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 647 ms: 1.24x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 659 ms: 1.20x faster                                                     |
| async_generators           | 500 ms                                                   | 449 ms: 1.11x faster                                                     |
| Geometric mean             | (ref)                                                    | 1.23x faster                                                             |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 87.7 ms: 1.09x faster                                                    |
| Geometric mean | (ref)                                                    | 1.02x faster                                                             |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.95 ms: 1.29x faster                                                    |
| regex_v8       | 32.5 ms                                                  | 27.9 ms: 1.17x faster                                                    |
| regex_dna      | 263 ms                                                   | 245 ms: 1.07x faster                                                     |
| Geometric mean | (ref)                                                    | 1.14x faster                                                             |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 174 ms: 1.16x faster                                                     |
| xml_etree_iterparse | 159 ms                                                   | 141 ms: 1.13x faster                                                     |
| tomli_loads         | 2.67 sec                                                 | 2.46 sec: 1.08x faster                                                   |
| Geometric mean      | (ref)                                                    | 1.03x faster                                                             |

Benchmark hidden because not significant (6): xml_etree_generate, xml_etree_process, json_dumps, unpickle_pure_python, json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 10.2 ms: 1.16x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.09x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml     | 61.6 ms                                                  | 60.2 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                    | 1.00x faster                                                             |

Benchmark hidden because not significant (3): genshi_text, mako, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 461 ms: 1.44x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 465 ms: 1.43x faster                                                     |
| deepcopy                   | 479 us                                                   | 342 us: 1.40x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 39.3 us: 1.35x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 368 ms: 1.31x faster                                                     |
| async_tree_none            | 504 ms                                                   | 386 ms: 1.31x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 882 ms: 1.29x faster                                                     |
| regex_effbot               | 5.10 ms                                                  | 3.95 ms: 1.29x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 907 ms: 1.28x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 647 ms: 1.24x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 659 ms: 1.20x faster                                                     |
| go                         | 164 ms                                                   | 137 ms: 1.20x faster                                                     |
| spectral_norm              | 143 ms                                                   | 121 ms: 1.19x faster                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 3.59 us: 1.18x faster                                                    |
| regex_v8                   | 32.5 ms                                                  | 27.9 ms: 1.17x faster                                                    |
| xml_etree_parse            | 203 ms                                                   | 174 ms: 1.16x faster                                                     |
| xml_etree_iterparse        | 159 ms                                                   | 141 ms: 1.13x faster                                                     |
| async_generators           | 500 ms                                                   | 449 ms: 1.11x faster                                                     |
| telco                      | 10.5 ms                                                  | 9.50 ms: 1.10x faster                                                    |
| scimark_sor                | 164 ms                                                   | 150 ms: 1.10x faster                                                     |
| float                      | 95.8 ms                                                  | 87.7 ms: 1.09x faster                                                    |
| pylint                     | 345 ms                                                   | 317 ms: 1.09x faster                                                     |
| generators                 | 40.3 ms                                                  | 37.1 ms: 1.09x faster                                                    |
| sqlite_synth               | 4.08 us                                                  | 3.76 us: 1.09x faster                                                    |
| tomli_loads                | 2.67 sec                                                 | 2.46 sec: 1.08x faster                                                   |
| scimark_fft                | 463 ms                                                   | 429 ms: 1.08x faster                                                     |
| pathlib                    | 24.3 ms                                                  | 22.7 ms: 1.07x faster                                                    |
| regex_dna                  | 263 ms                                                   | 245 ms: 1.07x faster                                                     |
| coverage                   | 106 ms                                                   | 98.6 ms: 1.07x faster                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 5.64 sec: 1.07x faster                                                   |
| k_core                     | 2.99 sec                                                 | 2.81 sec: 1.06x faster                                                   |
| sqlalchemy_declarative     | 154 ms                                                   | 145 ms: 1.06x faster                                                     |
| 2to3                       | 313 ms                                                   | 296 ms: 1.06x faster                                                     |
| pycparser                  | 1.34 sec                                                 | 1.28 sec: 1.05x faster                                                   |
| logging_format             | 8.10 us                                                  | 7.75 us: 1.05x faster                                                    |
| logging_silent             | 135 ns                                                   | 129 ns: 1.04x faster                                                     |
| meteor_contest             | 117 ms                                                   | 113 ms: 1.04x faster                                                     |
| mdp                        | 3.45 sec                                                 | 3.32 sec: 1.04x faster                                                   |
| sphinx                     | 1.20 sec                                                 | 1.16 sec: 1.04x faster                                                   |
| genshi_xml                 | 61.6 ms                                                  | 60.2 ms: 1.02x faster                                                    |
| connected_components       | 547 ms                                                   | 562 ms: 1.03x slower                                                     |
| shortest_path              | 565 ms                                                   | 582 ms: 1.03x slower                                                     |
| crypto_pyaes               | 84.9 ms                                                  | 90.0 ms: 1.06x slower                                                    |
| fannkuch                   | 478 ms                                                   | 507 ms: 1.06x slower                                                     |
| create_gc_cycles           | 3.39 ms                                                  | 3.82 ms: 1.12x slower                                                    |
| gc_traversal               | 5.92 ms                                                  | 6.68 ms: 1.13x slower                                                    |
| python_startup_no_site     | 8.79 ms                                                  | 10.2 ms: 1.16x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 26.1 ms: 1.29x slower                                                    |
| many_optionals             | 626 us                                                   | 855 us: 1.37x slower                                                     |
| bench_mp_pool              | 8.07 ms                                                  | 2.75 sec: 340.38x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.01x slower                                                             |

Benchmark hidden because not significant (41): regex_compile, thrift, scimark_monte_carlo, sqlalchemy_imperative, genshi_text, sympy_integrate, logging_simple, nqueens, xml_etree_generate, scimark_lu, xml_etree_process, richards_super, json, pyflate, json_dumps, deltablue, sympy_expand, richards, typing_runtime_protocols, html5lib, pprint_pformat, asyncio_websockets, pidigits, docutils, pprint_safe_repr, chaos, sympy_str, hexiom, bench_thread_pool, coroutines, mako, python_startup, sympy_sum, comprehensions, nbody, raytrace, django_template, scimark_sparse_mat_mult, unpickle_pure_python, json_loads, pickle_pure_python
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.044x faster

# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x