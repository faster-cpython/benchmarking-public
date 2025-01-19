# Results vs. 3.13.0

- fork: python
- ref: 61b35f74aa4a6ac60663
- machine: linux-aarch64
- commit hash: 61b35f7
- commit date: 2025-01-18
- overall geometric mean: 1.044x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.01 sec: 1.01x slower                                                   |
| html5lib       | 65.6 ms                                                  | 62.9 ms: 1.04x faster                                                    |
| Geometric mean | (ref)                                                    | 1.02x faster                                                             |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 474 ms: 1.40x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 490 ms: 1.35x faster                                                     |
| async_tree_none            | 504 ms                                                   | 385 ms: 1.31x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 897 ms: 1.30x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 374 ms: 1.30x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 895 ms: 1.27x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 662 ms: 1.21x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 678 ms: 1.16x faster                                                     |
| async_generators           | 500 ms                                                   | 454 ms: 1.10x faster                                                     |
| Geometric mean             | (ref)                                                    | 1.21x faster                                                             |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 86.7 ms: 1.10x faster                                                    |
| Geometric mean | (ref)                                                    | 1.02x faster                                                             |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.99 ms: 1.28x faster                                                    |
| Geometric mean | (ref)                                                    | 1.07x faster                                                             |

Benchmark hidden because not significant (3): regex_compile, regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 184 ms: 1.10x faster                                                     |
| xml_etree_iterparse | 159 ms                                                   | 146 ms: 1.08x faster                                                     |
| tomli_loads         | 2.67 sec                                                 | 2.57 sec: 1.04x faster                                                   |
| Geometric mean      | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (6): xml_etree_generate, xml_etree_process, unpickle_pure_python, json_loads, pickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 9.15 ms: 1.04x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.03x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text    | 28.6 ms                                                  | 27.1 ms: 1.05x faster                                                    |
| Geometric mean | (ref)                                                    | 1.00x faster                                                             |

Benchmark hidden because not significant (3): django_template, genshi_xml, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 474 ms: 1.40x faster                                                     |
| deepcopy                   | 479 us                                                   | 349 us: 1.37x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 490 ms: 1.35x faster                                                     |
| async_tree_none            | 504 ms                                                   | 385 ms: 1.31x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 897 ms: 1.30x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 374 ms: 1.30x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 41.0 us: 1.29x faster                                                    |
| regex_effbot               | 5.10 ms                                                  | 3.99 ms: 1.28x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 895 ms: 1.27x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 662 ms: 1.21x faster                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 3.55 us: 1.19x faster                                                    |
| spectral_norm              | 143 ms                                                   | 121 ms: 1.18x faster                                                     |
| go                         | 164 ms                                                   | 140 ms: 1.17x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 678 ms: 1.16x faster                                                     |
| generators                 | 40.3 ms                                                  | 36.1 ms: 1.12x faster                                                    |
| pathlib                    | 24.3 ms                                                  | 21.8 ms: 1.11x faster                                                    |
| scimark_fft                | 463 ms                                                   | 418 ms: 1.11x faster                                                     |
| float                      | 95.8 ms                                                  | 86.7 ms: 1.10x faster                                                    |
| async_generators           | 500 ms                                                   | 454 ms: 1.10x faster                                                     |
| xml_etree_parse            | 203 ms                                                   | 184 ms: 1.10x faster                                                     |
| telco                      | 10.5 ms                                                  | 9.53 ms: 1.10x faster                                                    |
| scimark_sor                | 164 ms                                                   | 150 ms: 1.09x faster                                                     |
| pylint                     | 345 ms                                                   | 318 ms: 1.09x faster                                                     |
| xml_etree_iterparse        | 159 ms                                                   | 146 ms: 1.08x faster                                                     |
| scimark_lu                 | 146 ms                                                   | 137 ms: 1.07x faster                                                     |
| bpe_tokeniser              | 6.02 sec                                                 | 5.68 sec: 1.06x faster                                                   |
| genshi_text                | 28.6 ms                                                  | 27.1 ms: 1.05x faster                                                    |
| nqueens                    | 105 ms                                                   | 99.7 ms: 1.05x faster                                                    |
| richards                   | 54.5 ms                                                  | 51.9 ms: 1.05x faster                                                    |
| k_core                     | 2.99 sec                                                 | 2.86 sec: 1.05x faster                                                   |
| chaos                      | 70.7 ms                                                  | 67.8 ms: 1.04x faster                                                    |
| html5lib                   | 65.6 ms                                                  | 62.9 ms: 1.04x faster                                                    |
| pycparser                  | 1.34 sec                                                 | 1.29 sec: 1.04x faster                                                   |
| tomli_loads                | 2.67 sec                                                 | 2.57 sec: 1.04x faster                                                   |
| docutils                   | 2.96 sec                                                 | 3.01 sec: 1.01x slower                                                   |
| python_startup_no_site     | 8.79 ms                                                  | 9.15 ms: 1.04x slower                                                    |
| typing_runtime_protocols   | 197 us                                                   | 207 us: 1.05x slower                                                     |
| comprehensions             | 20.8 us                                                  | 22.0 us: 1.06x slower                                                    |
| create_gc_cycles           | 3.39 ms                                                  | 3.61 ms: 1.07x slower                                                    |
| many_optionals             | 626 us                                                   | 699 us: 1.12x slower                                                     |
| gc_traversal               | 5.92 ms                                                  | 6.96 ms: 1.18x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 26.0 ms: 1.28x slower                                                    |
| bench_mp_pool              | 8.07 ms                                                  | 7.08 sec: 877.81x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.03x slower                                                             |

Benchmark hidden because not significant (52): logging_format, coverage, sqlalchemy_declarative, logging_simple, sympy_sum, xml_etree_generate, regex_compile, sqlalchemy_imperative, scimark_monte_carlo, scimark_sparse_mat_mult, sqlglot_optimize, deltablue, pyflate, regex_dna, json, 2to3, sphinx, pprint_safe_repr, thrift, mdp, crypto_pyaes, pprint_pformat, sympy_expand, sqlglot_normalize, bench_thread_pool, django_template, asyncio_websockets, genshi_xml, xml_etree_process, coroutines, pidigits, unpickle_pure_python, connected_components, sqlite_synth, sqlglot_transpile, shortest_path, sympy_integrate, fannkuch, richards_super, sqlglot_parse, raytrace, regex_v8, python_startup, sympy_str, hexiom, logging_silent, json_loads, nbody, meteor_contest, mako, pickle_pure_python, json_dumps
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (9) of results/bm-20250118-3.14.0a4+-61b35f7/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.044x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.02x