# Results vs. 3.13.0

- fork: python
- ref: 605022aeb69ae19cae1c
- machine: linux-aarch64
- commit hash: 605022a
- commit date: 2025-05-19
- overall geometric mean: 1.029x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-arminc-aarch64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 304 ms: 1.03x faster                                                    |
| html5lib       | 65.6 ms                                                  | 62.1 ms: 1.06x faster                                                   |
| sphinx         | 1.20 sec                                                 | 1.16 sec: 1.03x faster                                                  |
| Geometric mean | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-arminc-aarch64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 465 ms: 1.42x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 470 ms: 1.41x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 376 ms: 1.29x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 888 ms: 1.28x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 910 ms: 1.28x faster                                                    |
| async_tree_none            | 504 ms                                                   | 395 ms: 1.28x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 656 ms: 1.22x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 663 ms: 1.19x faster                                                    |
| async_generators           | 500 ms                                                   | 456 ms: 1.10x faster                                                    |
| Geometric mean             | (ref)                                                    | 1.21x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-arminc-aarch64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 86.9 ms: 1.10x faster                                                   |
| Geometric mean | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-arminc-aarch64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.81 ms: 1.34x faster                                                   |
| regex_v8       | 32.5 ms                                                  | 27.9 ms: 1.17x faster                                                   |
| regex_dna      | 263 ms                                                   | 236 ms: 1.11x faster                                                    |
| regex_compile  | 134 ms                                                   | 123 ms: 1.09x faster                                                    |
| Geometric mean | (ref)                                                    | 1.17x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-arminc-aarch64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 179 ms: 1.13x faster                                                    |
| xml_etree_iterparse | 159 ms                                                   | 143 ms: 1.11x faster                                                    |
| tomli_loads         | 2.67 sec                                                 | 2.43 sec: 1.10x faster                                                  |
| json_dumps          | 14.2 ms                                                  | 13.4 ms: 1.06x faster                                                   |
| xml_etree_generate  | 118 ms                                                   | 112 ms: 1.06x faster                                                    |
| xml_etree_process   | 82.1 ms                                                  | 79.2 ms: 1.04x faster                                                   |
| json_loads          | 32.8 us                                                  | 35.2 us: 1.07x slower                                                   |
| Geometric mean      | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (2): unpickle_pure_python, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-arminc-aarch64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 16.0 ms                                                  | 15.1 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_text, mako, django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-arminc-aarch64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.65 sec: 2.09x faster                                                  |
| async_tree_memoization_tg  | 663 ms                                                   | 465 ms: 1.42x faster                                                    |
| deepcopy                   | 479 us                                                   | 336 us: 1.42x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 470 ms: 1.41x faster                                                    |
| deepcopy_memo              | 53.0 us                                                  | 37.7 us: 1.41x faster                                                   |
| regex_effbot               | 5.10 ms                                                  | 3.81 ms: 1.34x faster                                                   |
| async_tree_none_tg         | 484 ms                                                   | 376 ms: 1.29x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 888 ms: 1.28x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 910 ms: 1.28x faster                                                    |
| async_tree_none            | 504 ms                                                   | 395 ms: 1.28x faster                                                    |
| go                         | 164 ms                                                   | 132 ms: 1.24x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 656 ms: 1.22x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 663 ms: 1.19x faster                                                    |
| regex_v8                   | 32.5 ms                                                  | 27.9 ms: 1.17x faster                                                   |
| deepcopy_reduce            | 4.24 us                                                  | 3.66 us: 1.16x faster                                                   |
| xml_etree_parse            | 203 ms                                                   | 179 ms: 1.13x faster                                                    |
| spectral_norm              | 143 ms                                                   | 128 ms: 1.12x faster                                                    |
| xml_etree_iterparse        | 159 ms                                                   | 143 ms: 1.11x faster                                                    |
| telco                      | 10.5 ms                                                  | 9.39 ms: 1.11x faster                                                   |
| regex_dna                  | 263 ms                                                   | 236 ms: 1.11x faster                                                    |
| scimark_sor                | 164 ms                                                   | 148 ms: 1.11x faster                                                    |
| generators                 | 40.3 ms                                                  | 36.3 ms: 1.11x faster                                                   |
| bpe_tokeniser              | 6.02 sec                                                 | 5.45 sec: 1.10x faster                                                  |
| pylint                     | 345 ms                                                   | 313 ms: 1.10x faster                                                    |
| float                      | 95.8 ms                                                  | 86.9 ms: 1.10x faster                                                   |
| tomli_loads                | 2.67 sec                                                 | 2.43 sec: 1.10x faster                                                  |
| async_generators           | 500 ms                                                   | 456 ms: 1.10x faster                                                    |
| scimark_monte_carlo        | 87.8 ms                                                  | 80.2 ms: 1.09x faster                                                   |
| pyflate                    | 582 ms                                                   | 532 ms: 1.09x faster                                                    |
| regex_compile              | 134 ms                                                   | 123 ms: 1.09x faster                                                    |
| pycparser                  | 1.34 sec                                                 | 1.24 sec: 1.08x faster                                                  |
| pprint_pformat             | 1.99 sec                                                 | 1.85 sec: 1.07x faster                                                  |
| json_dumps                 | 14.2 ms                                                  | 13.4 ms: 1.06x faster                                                   |
| python_startup             | 16.0 ms                                                  | 15.1 ms: 1.06x faster                                                   |
| xml_etree_generate         | 118 ms                                                   | 112 ms: 1.06x faster                                                    |
| html5lib                   | 65.6 ms                                                  | 62.1 ms: 1.06x faster                                                   |
| scimark_fft                | 463 ms                                                   | 439 ms: 1.05x faster                                                    |
| hexiom                     | 7.34 ms                                                  | 6.98 ms: 1.05x faster                                                   |
| pprint_safe_repr           | 962 ms                                                   | 915 ms: 1.05x faster                                                    |
| richards                   | 54.5 ms                                                  | 51.9 ms: 1.05x faster                                                   |
| deltablue                  | 3.97 ms                                                  | 3.79 ms: 1.05x faster                                                   |
| xml_etree_process          | 82.1 ms                                                  | 79.2 ms: 1.04x faster                                                   |
| k_core                     | 2.99 sec                                                 | 2.89 sec: 1.04x faster                                                  |
| sphinx                     | 1.20 sec                                                 | 1.16 sec: 1.03x faster                                                  |
| 2to3                       | 313 ms                                                   | 304 ms: 1.03x faster                                                    |
| connected_components       | 547 ms                                                   | 575 ms: 1.05x slower                                                    |
| raytrace                   | 310 ms                                                   | 328 ms: 1.06x slower                                                    |
| logging_simple             | 7.25 us                                                  | 7.68 us: 1.06x slower                                                   |
| json_loads                 | 32.8 us                                                  | 35.2 us: 1.07x slower                                                   |
| shortest_path              | 565 ms                                                   | 611 ms: 1.08x slower                                                    |
| create_gc_cycles           | 3.39 ms                                                  | 3.95 ms: 1.16x slower                                                   |
| gc_traversal               | 5.92 ms                                                  | 7.17 ms: 1.21x slower                                                   |
| many_optionals             | 626 us                                                   | 859 us: 1.37x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 28.4 ms: 1.40x slower                                                   |
| logging_silent             | 135 ns                                                   | 612 ns: 4.54x slower                                                    |
| coverage                   | 106 ms                                                   | 559 ms: 5.29x slower                                                    |
| thrift                     | 1.01 ms                                                  | 194 ms: 192.00x slower                                                  |
| bench_mp_pool              | 8.07 ms                                                  | 2.60 sec: 322.32x slower                                                |
| Geometric mean             | (ref)                                                    | 1.10x slower                                                            |

Benchmark hidden because not significant (31): pathlib, sympy_sum, nqueens, sympy_integrate, richards_super, genshi_text, sqlite_synth, fannkuch, python_startup_no_site, pidigits, chaos, unpickle_pure_python, asyncio_websockets, sympy_expand, meteor_contest, scimark_lu, crypto_pyaes, mako, django_template, docutils, genshi_xml, bench_thread_pool, comprehensions, json, typing_runtime_protocols, nbody, coroutines, logging_format, sympy_str, scimark_sparse_mat_mult, pickle_pure_python
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250519-3.15.0a0-605022a/bm-20250519-arminc-aarch64-python-605022aeb69ae19cae1c-3.15.0a0-605022a.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.029x slower

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.05x