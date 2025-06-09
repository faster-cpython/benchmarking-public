# Results vs. 3.13.0

- fork: python
- ref: v3.14.0b2
- machine: linux-aarch64
- commit hash: 12d3f88
- commit date: 2025-05-26
- overall geometric mean: 1.056x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250526-arminc-aarch64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| html5lib       | 65.6 ms                                                  | 61.0 ms: 1.08x faster                                        |
| sphinx         | 1.20 sec                                                 | 1.16 sec: 1.04x faster                                       |
| Geometric mean | (ref)                                                    | 1.03x faster                                                 |

Benchmark hidden because not significant (2): 2to3, docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250526-arminc-aarch64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 464 ms: 1.43x faster                                         |
| async_tree_memoization     | 664 ms                                                   | 467 ms: 1.42x faster                                         |
| async_tree_none_tg         | 484 ms                                                   | 372 ms: 1.30x faster                                         |
| async_tree_none            | 504 ms                                                   | 390 ms: 1.29x faster                                         |
| async_tree_io              | 1.14 sec                                                 | 883 ms: 1.29x faster                                         |
| async_tree_io_tg           | 1.16 sec                                                 | 916 ms: 1.27x faster                                         |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 659 ms: 1.22x faster                                         |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 658 ms: 1.20x faster                                         |
| async_generators           | 500 ms                                                   | 461 ms: 1.09x faster                                         |
| Geometric mean             | (ref)                                                    | 1.22x faster                                                 |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250526-arminc-aarch64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 87.0 ms: 1.10x faster                                        |
| Geometric mean | (ref)                                                    | 1.01x faster                                                 |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250526-arminc-aarch64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.88 ms: 1.31x faster                                        |
| regex_v8       | 32.5 ms                                                  | 28.0 ms: 1.16x faster                                        |
| regex_dna      | 263 ms                                                   | 233 ms: 1.13x faster                                         |
| regex_compile  | 134 ms                                                   | 120 ms: 1.12x faster                                         |
| Geometric mean | (ref)                                                    | 1.18x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250526-arminc-aarch64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 182 ms: 1.12x faster                                         |
| xml_etree_iterparse | 159 ms                                                   | 142 ms: 1.12x faster                                         |
| tomli_loads         | 2.67 sec                                                 | 2.45 sec: 1.09x faster                                       |
| json_dumps          | 14.2 ms                                                  | 13.3 ms: 1.07x faster                                        |
| json_loads          | 32.8 us                                                  | 35.9 us: 1.09x slower                                        |
| Geometric mean      | (ref)                                                    | 1.03x faster                                                 |

Benchmark hidden because not significant (4): xml_etree_generate, xml_etree_process, unpickle_pure_python, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250526-arminc-aarch64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 8.55 ms: 1.03x faster                                        |
| Geometric mean         | (ref)                                                    | 1.02x faster                                                 |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_text, genshi_xml, mako, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250526-arminc-aarch64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.69 sec: 2.04x faster                                       |
| deepcopy                   | 479 us                                                   | 328 us: 1.46x faster                                         |
| async_tree_memoization_tg  | 663 ms                                                   | 464 ms: 1.43x faster                                         |
| async_tree_memoization     | 664 ms                                                   | 467 ms: 1.42x faster                                         |
| deepcopy_memo              | 53.0 us                                                  | 38.9 us: 1.36x faster                                        |
| regex_effbot               | 5.10 ms                                                  | 3.88 ms: 1.31x faster                                        |
| async_tree_none_tg         | 484 ms                                                   | 372 ms: 1.30x faster                                         |
| async_tree_none            | 504 ms                                                   | 390 ms: 1.29x faster                                         |
| async_tree_io              | 1.14 sec                                                 | 883 ms: 1.29x faster                                         |
| async_tree_io_tg           | 1.16 sec                                                 | 916 ms: 1.27x faster                                         |
| go                         | 164 ms                                                   | 131 ms: 1.25x faster                                         |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 659 ms: 1.22x faster                                         |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 658 ms: 1.20x faster                                         |
| deepcopy_reduce            | 4.24 us                                                  | 3.63 us: 1.17x faster                                        |
| regex_v8                   | 32.5 ms                                                  | 28.0 ms: 1.16x faster                                        |
| regex_dna                  | 263 ms                                                   | 233 ms: 1.13x faster                                         |
| telco                      | 10.5 ms                                                  | 9.34 ms: 1.12x faster                                        |
| regex_compile              | 134 ms                                                   | 120 ms: 1.12x faster                                         |
| xml_etree_parse            | 203 ms                                                   | 182 ms: 1.12x faster                                         |
| xml_etree_iterparse        | 159 ms                                                   | 142 ms: 1.12x faster                                         |
| scimark_sor                | 164 ms                                                   | 148 ms: 1.11x faster                                         |
| pylint                     | 345 ms                                                   | 311 ms: 1.11x faster                                         |
| scimark_monte_carlo        | 87.8 ms                                                  | 79.4 ms: 1.11x faster                                        |
| bpe_tokeniser              | 6.02 sec                                                 | 5.46 sec: 1.10x faster                                       |
| float                      | 95.8 ms                                                  | 87.0 ms: 1.10x faster                                        |
| generators                 | 40.3 ms                                                  | 36.8 ms: 1.10x faster                                        |
| spectral_norm              | 143 ms                                                   | 131 ms: 1.09x faster                                         |
| tomli_loads                | 2.67 sec                                                 | 2.45 sec: 1.09x faster                                       |
| pyflate                    | 582 ms                                                   | 535 ms: 1.09x faster                                         |
| async_generators           | 500 ms                                                   | 461 ms: 1.09x faster                                         |
| html5lib                   | 65.6 ms                                                  | 61.0 ms: 1.08x faster                                        |
| scimark_fft                | 463 ms                                                   | 433 ms: 1.07x faster                                         |
| json_dumps                 | 14.2 ms                                                  | 13.3 ms: 1.07x faster                                        |
| pycparser                  | 1.34 sec                                                 | 1.26 sec: 1.07x faster                                       |
| pprint_pformat             | 1.99 sec                                                 | 1.86 sec: 1.07x faster                                       |
| pathlib                    | 24.3 ms                                                  | 22.9 ms: 1.06x faster                                        |
| sqlite_synth               | 4.08 us                                                  | 3.85 us: 1.06x faster                                        |
| nqueens                    | 105 ms                                                   | 99.1 ms: 1.06x faster                                        |
| k_core                     | 2.99 sec                                                 | 2.84 sec: 1.05x faster                                       |
| pprint_safe_repr           | 962 ms                                                   | 917 ms: 1.05x faster                                         |
| sphinx                     | 1.20 sec                                                 | 1.16 sec: 1.04x faster                                       |
| meteor_contest             | 117 ms                                                   | 113 ms: 1.03x faster                                         |
| python_startup_no_site     | 8.79 ms                                                  | 8.55 ms: 1.03x faster                                        |
| logging_format             | 8.10 us                                                  | 8.47 us: 1.05x slower                                        |
| logging_simple             | 7.25 us                                                  | 7.81 us: 1.08x slower                                        |
| create_gc_cycles           | 3.39 ms                                                  | 3.66 ms: 1.08x slower                                        |
| raytrace                   | 310 ms                                                   | 336 ms: 1.08x slower                                         |
| json_loads                 | 32.8 us                                                  | 35.9 us: 1.09x slower                                        |
| gc_traversal               | 5.92 ms                                                  | 6.53 ms: 1.10x slower                                        |
| many_optionals             | 626 us                                                   | 868 us: 1.39x slower                                         |
| subparsers                 | 20.3 ms                                                  | 28.7 ms: 1.41x slower                                        |
| logging_silent             | 135 ns                                                   | 633 ns: 4.70x slower                                         |
| Geometric mean             | (ref)                                                    | 1.04x faster                                                 |

Benchmark hidden because not significant (36): sympy_integrate, richards, hexiom, deltablue, xml_etree_generate, richards_super, coverage, fannkuch, genshi_text, sqlalchemy_declarative, sympy_sum, xml_etree_process, crypto_pyaes, 2to3, sympy_expand, asyncio_websockets, chaos, python_startup, genshi_xml, mako, sqlalchemy_imperative, docutils, connected_components, pidigits, unpickle_pure_python, django_template, json, shortest_path, comprehensions, scimark_lu, typing_runtime_protocols, sympy_str, scimark_sparse_mat_mult, coroutines, nbody, pickle_pure_python
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (5) of results/bm-20250526-3.14.0b2-12d3f88/bm-20250526-arminc-aarch64-python-v3.14.0b2-3.14.0b2-12d3f88.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.056x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.06x