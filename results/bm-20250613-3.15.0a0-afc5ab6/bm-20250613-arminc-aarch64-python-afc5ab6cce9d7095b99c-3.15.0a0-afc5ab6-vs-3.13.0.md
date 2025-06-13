# Results vs. 3.13.0

- fork: python
- ref: afc5ab6cce9d7095b99c
- machine: linux-aarch64
- commit hash: afc5ab6
- commit date: 2025-06-13
- overall geometric mean: 1.023x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-arminc-aarch64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 302 ms: 1.04x faster                                                    |
| docutils       | 2.96 sec                                                 | 2.89 sec: 1.03x faster                                                  |
| html5lib       | 65.6 ms                                                  | 61.0 ms: 1.08x faster                                                   |
| sphinx         | 1.20 sec                                                 | 1.13 sec: 1.06x faster                                                  |
| Geometric mean | (ref)                                                    | 1.05x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-arminc-aarch64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 463 ms: 1.43x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 472 ms: 1.41x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 903 ms: 1.29x faster                                                    |
| async_tree_none            | 504 ms                                                   | 394 ms: 1.28x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 379 ms: 1.28x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 908 ms: 1.25x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 649 ms: 1.23x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 657 ms: 1.20x faster                                                    |
| async_generators           | 500 ms                                                   | 447 ms: 1.12x faster                                                    |
| Geometric mean             | (ref)                                                    | 1.22x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-arminc-aarch64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 85.6 ms: 1.12x faster                                                   |
| Geometric mean | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-arminc-aarch64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.84 ms: 1.33x faster                                                   |
| regex_v8       | 32.5 ms                                                  | 26.3 ms: 1.24x faster                                                   |
| regex_dna      | 263 ms                                                   | 225 ms: 1.17x faster                                                    |
| regex_compile  | 134 ms                                                   | 124 ms: 1.08x faster                                                    |
| Geometric mean | (ref)                                                    | 1.20x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-arminc-aarch64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse | 159 ms                                                   | 141 ms: 1.12x faster                                                    |
| xml_etree_parse     | 203 ms                                                   | 181 ms: 1.12x faster                                                    |
| tomli_loads         | 2.67 sec                                                 | 2.48 sec: 1.08x faster                                                  |
| xml_etree_generate  | 118 ms                                                   | 110 ms: 1.08x faster                                                    |
| xml_etree_process   | 82.1 ms                                                  | 79.3 ms: 1.04x faster                                                   |
| Geometric mean      | (ref)                                                    | 1.05x faster                                                            |

Benchmark hidden because not significant (4): json_dumps, unpickle_pure_python, json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-arminc-aarch64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 15.0 ms: 1.07x faster                                                   |
| python_startup_no_site | 8.79 ms                                                  | 8.63 ms: 1.02x faster                                                   |
| Geometric mean         | (ref)                                                    | 1.04x faster                                                            |

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_text, mako, django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-arminc-aarch64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.69 sec: 2.04x faster                                                  |
| deepcopy                   | 479 us                                                   | 325 us: 1.47x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 463 ms: 1.43x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 472 ms: 1.41x faster                                                    |
| deepcopy_memo              | 53.0 us                                                  | 37.9 us: 1.40x faster                                                   |
| regex_effbot               | 5.10 ms                                                  | 3.84 ms: 1.33x faster                                                   |
| async_tree_io_tg           | 1.16 sec                                                 | 903 ms: 1.29x faster                                                    |
| go                         | 164 ms                                                   | 128 ms: 1.28x faster                                                    |
| async_tree_none            | 504 ms                                                   | 394 ms: 1.28x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 379 ms: 1.28x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 908 ms: 1.25x faster                                                    |
| regex_v8                   | 32.5 ms                                                  | 26.3 ms: 1.24x faster                                                   |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 649 ms: 1.23x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 657 ms: 1.20x faster                                                    |
| deepcopy_reduce            | 4.24 us                                                  | 3.63 us: 1.17x faster                                                   |
| regex_dna                  | 263 ms                                                   | 225 ms: 1.17x faster                                                    |
| generators                 | 40.3 ms                                                  | 35.2 ms: 1.15x faster                                                   |
| xml_etree_iterparse        | 159 ms                                                   | 141 ms: 1.12x faster                                                    |
| telco                      | 10.5 ms                                                  | 9.31 ms: 1.12x faster                                                   |
| xml_etree_parse            | 203 ms                                                   | 181 ms: 1.12x faster                                                    |
| async_generators           | 500 ms                                                   | 447 ms: 1.12x faster                                                    |
| float                      | 95.8 ms                                                  | 85.6 ms: 1.12x faster                                                   |
| spectral_norm              | 143 ms                                                   | 129 ms: 1.11x faster                                                    |
| scimark_sor                | 164 ms                                                   | 148 ms: 1.11x faster                                                    |
| pyflate                    | 582 ms                                                   | 525 ms: 1.11x faster                                                    |
| scimark_monte_carlo        | 87.8 ms                                                  | 79.3 ms: 1.11x faster                                                   |
| pylint                     | 345 ms                                                   | 313 ms: 1.10x faster                                                    |
| pycparser                  | 1.34 sec                                                 | 1.23 sec: 1.10x faster                                                  |
| bpe_tokeniser              | 6.02 sec                                                 | 5.52 sec: 1.09x faster                                                  |
| sqlite_synth               | 4.08 us                                                  | 3.78 us: 1.08x faster                                                   |
| regex_compile              | 134 ms                                                   | 124 ms: 1.08x faster                                                    |
| tomli_loads                | 2.67 sec                                                 | 2.48 sec: 1.08x faster                                                  |
| xml_etree_generate         | 118 ms                                                   | 110 ms: 1.08x faster                                                    |
| html5lib                   | 65.6 ms                                                  | 61.0 ms: 1.08x faster                                                   |
| python_startup             | 16.0 ms                                                  | 15.0 ms: 1.07x faster                                                   |
| sphinx                     | 1.20 sec                                                 | 1.13 sec: 1.06x faster                                                  |
| scimark_fft                | 463 ms                                                   | 438 ms: 1.06x faster                                                    |
| k_core                     | 2.99 sec                                                 | 2.83 sec: 1.06x faster                                                  |
| json                       | 5.94 ms                                                  | 5.67 ms: 1.05x faster                                                   |
| 2to3                       | 313 ms                                                   | 302 ms: 1.04x faster                                                    |
| xml_etree_process          | 82.1 ms                                                  | 79.3 ms: 1.04x faster                                                   |
| comprehensions             | 20.8 us                                                  | 20.2 us: 1.03x faster                                                   |
| docutils                   | 2.96 sec                                                 | 2.89 sec: 1.03x faster                                                  |
| python_startup_no_site     | 8.79 ms                                                  | 8.63 ms: 1.02x faster                                                   |
| connected_components       | 547 ms                                                   | 565 ms: 1.03x slower                                                    |
| logging_simple             | 7.25 us                                                  | 7.50 us: 1.03x slower                                                   |
| shortest_path              | 565 ms                                                   | 585 ms: 1.04x slower                                                    |
| pprint_pformat             | 1.99 sec                                                 | 2.07 sec: 1.04x slower                                                  |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 6.99 ms: 1.05x slower                                                   |
| raytrace                   | 310 ms                                                   | 326 ms: 1.05x slower                                                    |
| pprint_safe_repr           | 962 ms                                                   | 1.02 sec: 1.06x slower                                                  |
| create_gc_cycles           | 3.39 ms                                                  | 3.71 ms: 1.09x slower                                                   |
| gc_traversal               | 5.92 ms                                                  | 6.86 ms: 1.16x slower                                                   |
| many_optionals             | 626 us                                                   | 756 us: 1.21x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 28.0 ms: 1.38x slower                                                   |
| logging_silent             | 135 ns                                                   | 629 ns: 4.67x slower                                                    |
| coverage                   | 106 ms                                                   | 545 ms: 5.16x slower                                                    |
| thrift                     | 1.01 ms                                                  | 194 ms: 191.69x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.03x slower                                                            |

Benchmark hidden because not significant (29): sympy_sum, pathlib, json_dumps, nqueens, meteor_contest, genshi_text, hexiom, sympy_integrate, richards, crypto_pyaes, pidigits, unpickle_pure_python, sympy_expand, mako, json_loads, richards_super, django_template, asyncio_websockets, genshi_xml, typing_runtime_protocols, fannkuch, chaos, deltablue, scimark_lu, coroutines, logging_format, pickle_pure_python, sympy_str, nbody
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250613-3.15.0a0-afc5ab6/bm-20250613-arminc-aarch64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.023x slower

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.07x