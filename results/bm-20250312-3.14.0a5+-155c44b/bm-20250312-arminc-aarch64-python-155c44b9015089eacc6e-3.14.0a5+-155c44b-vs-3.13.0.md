# Results vs. 3.13.0

- fork: python
- ref: 155c44b9015089eacc6e
- machine: linux-aarch64
- commit hash: 155c44b
- commit date: 2025-03-12
- overall geometric mean: 1.051x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-arminc-aarch64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 294 ms: 1.06x faster                                                     |
| docutils       | 2.96 sec                                                 | 2.91 sec: 1.02x faster                                                   |
| html5lib       | 65.6 ms                                                  | 63.7 ms: 1.03x faster                                                    |
| sphinx         | 1.20 sec                                                 | 1.14 sec: 1.05x faster                                                   |
| Geometric mean | (ref)                                                    | 1.04x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-arminc-aarch64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 664 ms                                                   | 467 ms: 1.42x faster                                                     |
| async_tree_memoization_tg  | 663 ms                                                   | 469 ms: 1.41x faster                                                     |
| async_tree_none            | 504 ms                                                   | 379 ms: 1.33x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 887 ms: 1.31x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 372 ms: 1.30x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 879 ms: 1.30x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 642 ms: 1.25x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 653 ms: 1.21x faster                                                     |
| async_generators           | 500 ms                                                   | 434 ms: 1.15x faster                                                     |
| asyncio_websockets         | 674 ms                                                   | 658 ms: 1.02x faster                                                     |
| Geometric mean             | (ref)                                                    | 1.24x faster                                                             |

Benchmark hidden because not significant (1): coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-arminc-aarch64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 87.1 ms: 1.10x faster                                                    |
| nbody          | 118 ms                                                   | 124 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                    | 1.02x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-arminc-aarch64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.87 ms: 1.32x faster                                                    |
| regex_v8       | 32.5 ms                                                  | 29.0 ms: 1.12x faster                                                    |
| regex_compile  | 134 ms                                                   | 125 ms: 1.06x faster                                                     |
| regex_dna      | 263 ms                                                   | 247 ms: 1.06x faster                                                     |
| Geometric mean | (ref)                                                    | 1.14x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-arminc-aarch64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 175 ms: 1.16x faster                                                     |
| xml_etree_iterparse | 159 ms                                                   | 140 ms: 1.13x faster                                                     |
| tomli_loads         | 2.67 sec                                                 | 2.44 sec: 1.09x faster                                                   |
| xml_etree_generate  | 118 ms                                                   | 112 ms: 1.06x faster                                                     |
| Geometric mean      | (ref)                                                    | 1.04x faster                                                             |

Benchmark hidden because not significant (5): xml_etree_process, unpickle_pure_python, json_dumps, pickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-arminc-aarch64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 10.1 ms: 1.15x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.07x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-arminc-aarch64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml     | 61.6 ms                                                  | 59.9 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (3): genshi_text, mako, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-arminc-aarch64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy                   | 479 us                                                   | 334 us: 1.43x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 467 ms: 1.42x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 37.3 us: 1.42x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 469 ms: 1.41x faster                                                     |
| async_tree_none            | 504 ms                                                   | 379 ms: 1.33x faster                                                     |
| regex_effbot               | 5.10 ms                                                  | 3.87 ms: 1.32x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 887 ms: 1.31x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 372 ms: 1.30x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 879 ms: 1.30x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 642 ms: 1.25x faster                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 3.44 us: 1.24x faster                                                    |
| go                         | 164 ms                                                   | 135 ms: 1.22x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 653 ms: 1.21x faster                                                     |
| spectral_norm              | 143 ms                                                   | 121 ms: 1.18x faster                                                     |
| xml_etree_parse            | 203 ms                                                   | 175 ms: 1.16x faster                                                     |
| async_generators           | 500 ms                                                   | 434 ms: 1.15x faster                                                     |
| xml_etree_iterparse        | 159 ms                                                   | 140 ms: 1.13x faster                                                     |
| regex_v8                   | 32.5 ms                                                  | 29.0 ms: 1.12x faster                                                    |
| generators                 | 40.3 ms                                                  | 36.2 ms: 1.11x faster                                                    |
| pylint                     | 345 ms                                                   | 312 ms: 1.11x faster                                                     |
| pathlib                    | 24.3 ms                                                  | 22.0 ms: 1.11x faster                                                    |
| float                      | 95.8 ms                                                  | 87.1 ms: 1.10x faster                                                    |
| tomli_loads                | 2.67 sec                                                 | 2.44 sec: 1.09x faster                                                   |
| scimark_sor                | 164 ms                                                   | 151 ms: 1.09x faster                                                     |
| telco                      | 10.5 ms                                                  | 9.63 ms: 1.09x faster                                                    |
| scimark_fft                | 463 ms                                                   | 427 ms: 1.08x faster                                                     |
| bpe_tokeniser              | 6.02 sec                                                 | 5.59 sec: 1.08x faster                                                   |
| sqlite_synth               | 4.08 us                                                  | 3.80 us: 1.07x faster                                                    |
| sympy_sum                  | 151 ms                                                   | 142 ms: 1.07x faster                                                     |
| pycparser                  | 1.34 sec                                                 | 1.26 sec: 1.07x faster                                                   |
| regex_compile              | 134 ms                                                   | 125 ms: 1.06x faster                                                     |
| regex_dna                  | 263 ms                                                   | 247 ms: 1.06x faster                                                     |
| 2to3                       | 313 ms                                                   | 294 ms: 1.06x faster                                                     |
| pyflate                    | 582 ms                                                   | 547 ms: 1.06x faster                                                     |
| sqlalchemy_declarative     | 154 ms                                                   | 145 ms: 1.06x faster                                                     |
| xml_etree_generate         | 118 ms                                                   | 112 ms: 1.06x faster                                                     |
| thrift                     | 1.01 ms                                                  | 956 us: 1.06x faster                                                     |
| logging_format             | 8.10 us                                                  | 7.67 us: 1.06x faster                                                    |
| coverage                   | 106 ms                                                   | 100 ms: 1.05x faster                                                     |
| nqueens                    | 105 ms                                                   | 99.7 ms: 1.05x faster                                                    |
| k_core                     | 2.99 sec                                                 | 2.84 sec: 1.05x faster                                                   |
| sphinx                     | 1.20 sec                                                 | 1.14 sec: 1.05x faster                                                   |
| meteor_contest             | 117 ms                                                   | 112 ms: 1.04x faster                                                     |
| logging_simple             | 7.25 us                                                  | 6.97 us: 1.04x faster                                                    |
| pprint_pformat             | 1.99 sec                                                 | 1.92 sec: 1.04x faster                                                   |
| richards_super             | 60.8 ms                                                  | 59.0 ms: 1.03x faster                                                    |
| html5lib                   | 65.6 ms                                                  | 63.7 ms: 1.03x faster                                                    |
| genshi_xml                 | 61.6 ms                                                  | 59.9 ms: 1.03x faster                                                    |
| pprint_safe_repr           | 962 ms                                                   | 938 ms: 1.03x faster                                                     |
| asyncio_websockets         | 674 ms                                                   | 658 ms: 1.02x faster                                                     |
| typing_runtime_protocols   | 197 us                                                   | 193 us: 1.02x faster                                                     |
| mdp                        | 3.45 sec                                                 | 3.38 sec: 1.02x faster                                                   |
| docutils                   | 2.96 sec                                                 | 2.91 sec: 1.02x faster                                                   |
| connected_components       | 547 ms                                                   | 556 ms: 1.02x slower                                                     |
| shortest_path              | 565 ms                                                   | 576 ms: 1.02x slower                                                     |
| crypto_pyaes               | 84.9 ms                                                  | 88.3 ms: 1.04x slower                                                    |
| nbody                      | 118 ms                                                   | 124 ms: 1.04x slower                                                     |
| create_gc_cycles           | 3.39 ms                                                  | 3.66 ms: 1.08x slower                                                    |
| gc_traversal               | 5.92 ms                                                  | 6.72 ms: 1.13x slower                                                    |
| python_startup_no_site     | 8.79 ms                                                  | 10.1 ms: 1.15x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 25.4 ms: 1.25x slower                                                    |
| many_optionals             | 626 us                                                   | 833 us: 1.33x slower                                                     |
| bench_mp_pool              | 8.07 ms                                                  | 3.91 sec: 484.85x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.01x slower                                                             |

Benchmark hidden because not significant (28): genshi_text, scimark_monte_carlo, sqlalchemy_imperative, xml_etree_process, sympy_integrate, scimark_sparse_mat_mult, chaos, sympy_expand, hexiom, logging_silent, unpickle_pure_python, json, deltablue, pidigits, python_startup, json_dumps, comprehensions, mako, bench_thread_pool, coroutines, sympy_str, pickle_pure_python, fannkuch, raytrace, django_template, richards, scimark_lu, json_loads
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250312-3.14.0a5+-155c44b/bm-20250312-arminc-aarch64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.051x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.03x