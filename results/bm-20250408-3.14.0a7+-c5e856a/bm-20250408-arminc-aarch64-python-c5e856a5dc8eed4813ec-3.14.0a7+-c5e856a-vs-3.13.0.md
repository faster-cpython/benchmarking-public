# Results vs. 3.13.0

- fork: python
- ref: c5e856a5dc8eed4813ec
- machine: linux-aarch64
- commit hash: c5e856a
- commit date: 2025-04-08
- overall geometric mean: 1.070x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-arminc-aarch64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 291 ms: 1.08x faster                                                     |
| docutils       | 2.96 sec                                                 | 2.93 sec: 1.01x faster                                                   |
| html5lib       | 65.6 ms                                                  | 62.9 ms: 1.04x faster                                                    |
| sphinx         | 1.20 sec                                                 | 1.14 sec: 1.06x faster                                                   |
| Geometric mean | (ref)                                                    | 1.05x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-arminc-aarch64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 664 ms                                                   | 457 ms: 1.45x faster                                                     |
| async_tree_memoization_tg  | 663 ms                                                   | 459 ms: 1.44x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 874 ms: 1.33x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 365 ms: 1.33x faster                                                     |
| async_tree_none            | 504 ms                                                   | 385 ms: 1.31x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 875 ms: 1.30x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 642 ms: 1.25x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 658 ms: 1.20x faster                                                     |
| async_generators           | 500 ms                                                   | 450 ms: 1.11x faster                                                     |
| Geometric mean             | (ref)                                                    | 1.24x faster                                                             |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-arminc-aarch64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 83.8 ms: 1.14x faster                                                    |
| Geometric mean | (ref)                                                    | 1.04x faster                                                             |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-arminc-aarch64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.95 ms: 1.29x faster                                                    |
| regex_v8       | 32.5 ms                                                  | 28.0 ms: 1.16x faster                                                    |
| regex_compile  | 134 ms                                                   | 122 ms: 1.10x faster                                                     |
| regex_dna      | 263 ms                                                   | 251 ms: 1.05x faster                                                     |
| Geometric mean | (ref)                                                    | 1.15x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-arminc-aarch64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 173 ms: 1.17x faster                                                     |
| xml_etree_iterparse | 159 ms                                                   | 139 ms: 1.14x faster                                                     |
| tomli_loads         | 2.67 sec                                                 | 2.43 sec: 1.10x faster                                                   |
| xml_etree_generate  | 118 ms                                                   | 110 ms: 1.07x faster                                                     |
| xml_etree_process   | 82.1 ms                                                  | 78.9 ms: 1.04x faster                                                    |
| Geometric mean      | (ref)                                                    | 1.05x faster                                                             |

Benchmark hidden because not significant (4): json_dumps, unpickle_pure_python, json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-arminc-aarch64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 10.2 ms: 1.16x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.08x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-arminc-aarch64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text    | 28.6 ms                                                  | 26.2 ms: 1.09x faster                                                    |
| genshi_xml     | 61.6 ms                                                  | 59.6 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                    | 1.03x faster                                                             |

Benchmark hidden because not significant (2): mako, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-arminc-aarch64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.61 sec: 2.14x faster                                                   |
| deepcopy                   | 479 us                                                   | 320 us: 1.49x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 457 ms: 1.45x faster                                                     |
| async_tree_memoization_tg  | 663 ms                                                   | 459 ms: 1.44x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 37.5 us: 1.41x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 874 ms: 1.33x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 365 ms: 1.33x faster                                                     |
| async_tree_none            | 504 ms                                                   | 385 ms: 1.31x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 875 ms: 1.30x faster                                                     |
| regex_effbot               | 5.10 ms                                                  | 3.95 ms: 1.29x faster                                                    |
| go                         | 164 ms                                                   | 129 ms: 1.27x faster                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 3.38 us: 1.25x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 642 ms: 1.25x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 658 ms: 1.20x faster                                                     |
| xml_etree_parse            | 203 ms                                                   | 173 ms: 1.17x faster                                                     |
| regex_v8                   | 32.5 ms                                                  | 28.0 ms: 1.16x faster                                                    |
| spectral_norm              | 143 ms                                                   | 124 ms: 1.15x faster                                                     |
| telco                      | 10.5 ms                                                  | 9.08 ms: 1.15x faster                                                    |
| float                      | 95.8 ms                                                  | 83.8 ms: 1.14x faster                                                    |
| xml_etree_iterparse        | 159 ms                                                   | 139 ms: 1.14x faster                                                     |
| pylint                     | 345 ms                                                   | 307 ms: 1.13x faster                                                     |
| pathlib                    | 24.3 ms                                                  | 21.6 ms: 1.13x faster                                                    |
| scimark_fft                | 463 ms                                                   | 412 ms: 1.12x faster                                                     |
| async_generators           | 500 ms                                                   | 450 ms: 1.11x faster                                                     |
| generators                 | 40.3 ms                                                  | 36.5 ms: 1.10x faster                                                    |
| scimark_monte_carlo        | 87.8 ms                                                  | 79.8 ms: 1.10x faster                                                    |
| tomli_loads                | 2.67 sec                                                 | 2.43 sec: 1.10x faster                                                   |
| regex_compile              | 134 ms                                                   | 122 ms: 1.10x faster                                                     |
| scimark_sor                | 164 ms                                                   | 150 ms: 1.09x faster                                                     |
| genshi_text                | 28.6 ms                                                  | 26.2 ms: 1.09x faster                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 5.53 sec: 1.09x faster                                                   |
| pycparser                  | 1.34 sec                                                 | 1.25 sec: 1.08x faster                                                   |
| 2to3                       | 313 ms                                                   | 291 ms: 1.08x faster                                                     |
| pprint_pformat             | 1.99 sec                                                 | 1.85 sec: 1.07x faster                                                   |
| k_core                     | 2.99 sec                                                 | 2.79 sec: 1.07x faster                                                   |
| xml_etree_generate         | 118 ms                                                   | 110 ms: 1.07x faster                                                     |
| pyflate                    | 582 ms                                                   | 547 ms: 1.06x faster                                                     |
| chaos                      | 70.7 ms                                                  | 66.8 ms: 1.06x faster                                                    |
| nqueens                    | 105 ms                                                   | 99.2 ms: 1.06x faster                                                    |
| sphinx                     | 1.20 sec                                                 | 1.14 sec: 1.06x faster                                                   |
| pprint_safe_repr           | 962 ms                                                   | 910 ms: 1.06x faster                                                     |
| hexiom                     | 7.34 ms                                                  | 6.99 ms: 1.05x faster                                                    |
| regex_dna                  | 263 ms                                                   | 251 ms: 1.05x faster                                                     |
| coverage                   | 106 ms                                                   | 101 ms: 1.05x faster                                                     |
| meteor_contest             | 117 ms                                                   | 112 ms: 1.05x faster                                                     |
| richards                   | 54.5 ms                                                  | 52.1 ms: 1.05x faster                                                    |
| deltablue                  | 3.97 ms                                                  | 3.79 ms: 1.05x faster                                                    |
| logging_silent             | 135 ns                                                   | 129 ns: 1.05x faster                                                     |
| sqlite_synth               | 4.08 us                                                  | 3.91 us: 1.04x faster                                                    |
| html5lib                   | 65.6 ms                                                  | 62.9 ms: 1.04x faster                                                    |
| xml_etree_process          | 82.1 ms                                                  | 78.9 ms: 1.04x faster                                                    |
| logging_format             | 8.10 us                                                  | 7.79 us: 1.04x faster                                                    |
| genshi_xml                 | 61.6 ms                                                  | 59.6 ms: 1.03x faster                                                    |
| docutils                   | 2.96 sec                                                 | 2.93 sec: 1.01x faster                                                   |
| create_gc_cycles           | 3.39 ms                                                  | 3.49 ms: 1.03x slower                                                    |
| shortest_path              | 565 ms                                                   | 587 ms: 1.04x slower                                                     |
| gc_traversal               | 5.92 ms                                                  | 6.73 ms: 1.14x slower                                                    |
| python_startup_no_site     | 8.79 ms                                                  | 10.2 ms: 1.16x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 26.0 ms: 1.28x slower                                                    |
| many_optionals             | 626 us                                                   | 835 us: 1.33x slower                                                     |
| bench_mp_pool              | 8.07 ms                                                  | 2.07 sec: 256.15x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (29): sympy_integrate, sympy_sum, sqlalchemy_declarative, richards_super, sqlalchemy_imperative, logging_simple, json_dumps, sympy_expand, crypto_pyaes, asyncio_websockets, json, sympy_str, pidigits, unpickle_pure_python, fannkuch, mako, typing_runtime_protocols, scimark_sparse_mat_mult, bench_thread_pool, connected_components, python_startup, nbody, raytrace, django_template, coroutines, json_loads, pickle_pure_python, comprehensions, scimark_lu
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (5) of results/bm-20250408-3.14.0a7+-c5e856a/bm-20250408-arminc-aarch64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.070x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.04x