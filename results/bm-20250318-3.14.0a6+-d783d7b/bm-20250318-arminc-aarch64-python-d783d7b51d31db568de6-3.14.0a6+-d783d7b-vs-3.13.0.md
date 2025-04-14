# Results vs. 3.13.0

- fork: python
- ref: d783d7b51d31db568de6
- machine: linux-aarch64
- commit hash: d783d7b
- commit date: 2025-03-18
- overall geometric mean: 1.043x faster
- HPT reliability: 99.88%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-arminc-aarch64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 297 ms: 1.05x faster                                                     |
| html5lib       | 65.6 ms                                                  | 64.2 ms: 1.02x faster                                                    |
| sphinx         | 1.20 sec                                                 | 1.16 sec: 1.03x faster                                                   |
| Geometric mean | (ref)                                                    | 1.03x faster                                                             |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-arminc-aarch64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 664 ms                                                   | 468 ms: 1.42x faster                                                     |
| async_tree_memoization_tg  | 663 ms                                                   | 471 ms: 1.41x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 368 ms: 1.32x faster                                                     |
| async_tree_none            | 504 ms                                                   | 386 ms: 1.31x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 890 ms: 1.28x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 915 ms: 1.27x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 650 ms: 1.23x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 658 ms: 1.20x faster                                                     |
| async_generators           | 500 ms                                                   | 461 ms: 1.09x faster                                                     |
| Geometric mean             | (ref)                                                    | 1.22x faster                                                             |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-arminc-aarch64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 87.4 ms: 1.10x faster                                                    |
| nbody          | 118 ms                                                   | 128 ms: 1.08x slower                                                     |
| Geometric mean | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-arminc-aarch64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.98 ms: 1.28x faster                                                    |
| regex_v8       | 32.5 ms                                                  | 28.1 ms: 1.16x faster                                                    |
| regex_dna      | 263 ms                                                   | 244 ms: 1.08x faster                                                     |
| regex_compile  | 134 ms                                                   | 125 ms: 1.07x faster                                                     |
| Geometric mean | (ref)                                                    | 1.14x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-arminc-aarch64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 176 ms: 1.15x faster                                                     |
| xml_etree_iterparse | 159 ms                                                   | 141 ms: 1.12x faster                                                     |
| tomli_loads         | 2.67 sec                                                 | 2.48 sec: 1.08x faster                                                   |
| Geometric mean      | (ref)                                                    | 1.03x faster                                                             |

Benchmark hidden because not significant (6): xml_etree_generate, json_dumps, xml_etree_process, unpickle_pure_python, json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-arminc-aarch64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 10.2 ms: 1.16x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.08x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-arminc-aarch64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text    | 28.6 ms                                                  | 27.0 ms: 1.06x faster                                                    |
| Geometric mean | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (3): genshi_xml, mako, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-arminc-aarch64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy                   | 479 us                                                   | 331 us: 1.44x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 468 ms: 1.42x faster                                                     |
| async_tree_memoization_tg  | 663 ms                                                   | 471 ms: 1.41x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 38.2 us: 1.38x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 368 ms: 1.32x faster                                                     |
| async_tree_none            | 504 ms                                                   | 386 ms: 1.31x faster                                                     |
| regex_effbot               | 5.10 ms                                                  | 3.98 ms: 1.28x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 890 ms: 1.28x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 915 ms: 1.27x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 650 ms: 1.23x faster                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 3.53 us: 1.20x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 658 ms: 1.20x faster                                                     |
| go                         | 164 ms                                                   | 140 ms: 1.18x faster                                                     |
| regex_v8                   | 32.5 ms                                                  | 28.1 ms: 1.16x faster                                                    |
| xml_etree_parse            | 203 ms                                                   | 176 ms: 1.15x faster                                                     |
| spectral_norm              | 143 ms                                                   | 126 ms: 1.14x faster                                                     |
| generators                 | 40.3 ms                                                  | 35.7 ms: 1.13x faster                                                    |
| xml_etree_iterparse        | 159 ms                                                   | 141 ms: 1.12x faster                                                     |
| scimark_sor                | 164 ms                                                   | 149 ms: 1.10x faster                                                     |
| float                      | 95.8 ms                                                  | 87.4 ms: 1.10x faster                                                    |
| scimark_fft                | 463 ms                                                   | 424 ms: 1.09x faster                                                     |
| async_generators           | 500 ms                                                   | 461 ms: 1.09x faster                                                     |
| pathlib                    | 24.3 ms                                                  | 22.5 ms: 1.08x faster                                                    |
| regex_dna                  | 263 ms                                                   | 244 ms: 1.08x faster                                                     |
| k_core                     | 2.99 sec                                                 | 2.78 sec: 1.08x faster                                                   |
| tomli_loads                | 2.67 sec                                                 | 2.48 sec: 1.08x faster                                                   |
| coverage                   | 106 ms                                                   | 98.7 ms: 1.07x faster                                                    |
| regex_compile              | 134 ms                                                   | 125 ms: 1.07x faster                                                     |
| bpe_tokeniser              | 6.02 sec                                                 | 5.65 sec: 1.07x faster                                                   |
| thrift                     | 1.01 ms                                                  | 949 us: 1.06x faster                                                     |
| pycparser                  | 1.34 sec                                                 | 1.27 sec: 1.06x faster                                                   |
| pyflate                    | 582 ms                                                   | 548 ms: 1.06x faster                                                     |
| genshi_text                | 28.6 ms                                                  | 27.0 ms: 1.06x faster                                                    |
| telco                      | 10.5 ms                                                  | 9.89 ms: 1.06x faster                                                    |
| sqlite_synth               | 4.08 us                                                  | 3.87 us: 1.05x faster                                                    |
| 2to3                       | 313 ms                                                   | 297 ms: 1.05x faster                                                     |
| richards                   | 54.5 ms                                                  | 51.8 ms: 1.05x faster                                                    |
| mdp                        | 3.45 sec                                                 | 3.31 sec: 1.04x faster                                                   |
| meteor_contest             | 117 ms                                                   | 113 ms: 1.04x faster                                                     |
| sphinx                     | 1.20 sec                                                 | 1.16 sec: 1.03x faster                                                   |
| html5lib                   | 65.6 ms                                                  | 64.2 ms: 1.02x faster                                                    |
| sympy_str                  | 265 ms                                                   | 267 ms: 1.01x slower                                                     |
| shortest_path              | 565 ms                                                   | 579 ms: 1.02x slower                                                     |
| raytrace                   | 310 ms                                                   | 323 ms: 1.04x slower                                                     |
| fannkuch                   | 478 ms                                                   | 508 ms: 1.06x slower                                                     |
| nbody                      | 118 ms                                                   | 128 ms: 1.08x slower                                                     |
| create_gc_cycles           | 3.39 ms                                                  | 3.68 ms: 1.08x slower                                                    |
| gc_traversal               | 5.92 ms                                                  | 6.56 ms: 1.11x slower                                                    |
| python_startup_no_site     | 8.79 ms                                                  | 10.2 ms: 1.16x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 25.8 ms: 1.27x slower                                                    |
| many_optionals             | 626 us                                                   | 836 us: 1.33x slower                                                     |
| bench_mp_pool              | 8.07 ms                                                  | 2.47 sec: 306.31x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.01x slower                                                             |

Benchmark hidden because not significant (39): sympy_sum, sqlalchemy_declarative, pylint, logging_format, logging_simple, xml_etree_generate, json, logging_silent, richards_super, sqlalchemy_imperative, nqueens, coroutines, asyncio_websockets, scimark_sparse_mat_mult, genshi_xml, pprint_pformat, pidigits, sympy_expand, scimark_monte_carlo, pprint_safe_repr, json_dumps, hexiom, bench_thread_pool, xml_etree_process, deltablue, docutils, python_startup, sympy_integrate, typing_runtime_protocols, unpickle_pure_python, connected_components, mako, crypto_pyaes, scimark_lu, chaos, django_template, comprehensions, json_loads, pickle_pure_python
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250318-3.14.0a6+-d783d7b/bm-20250318-arminc-aarch64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.043x faster

# HPT report

- Reliability score: 99.88% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.03x