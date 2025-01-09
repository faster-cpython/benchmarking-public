# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: tail_call
- machine: linux-aarch64
- commit hash: f1d3190
- commit date: 2025-01-07
- overall geometric mean: 1.066x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 293 ms: 1.07x faster                                                    |
| docutils       | 2.96 sec                                                 | 3.01 sec: 1.01x slower                                                  |
| html5lib       | 65.6 ms                                                  | 60.6 ms: 1.08x faster                                                   |
| sphinx         | 1.20 sec                                                 | 1.16 sec: 1.03x faster                                                  |
| Geometric mean | (ref)                                                    | 1.04x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 446 ms: 1.48x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 472 ms: 1.41x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 848 ms: 1.37x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 361 ms: 1.34x faster                                                    |
| async_tree_none            | 504 ms                                                   | 377 ms: 1.34x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 869 ms: 1.31x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 722 ms: 1.11x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 728 ms: 1.08x faster                                                    |
| async_generators           | 500 ms                                                   | 465 ms: 1.08x faster                                                    |
| Geometric mean             | (ref)                                                    | 1.22x faster                                                            |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 83.8 ms: 1.14x faster                                                   |
| nbody          | 118 ms                                                   | 109 ms: 1.09x faster                                                    |
| pidigits       | 238 ms                                                   | 307 ms: 1.29x slower                                                    |
| Geometric mean | (ref)                                                    | 1.01x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.38 ms: 1.17x faster                                                   |
| regex_v8       | 32.5 ms                                                  | 34.4 ms: 1.06x slower                                                   |
| Geometric mean | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (2): regex_compile, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate   | 118 ms                                                   | 107 ms: 1.11x faster                                                    |
| tomli_loads          | 2.67 sec                                                 | 2.41 sec: 1.11x faster                                                  |
| unpickle_pure_python | 265 us                                                   | 248 us: 1.07x faster                                                    |
| Geometric mean       | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (6): xml_etree_process, xml_etree_iterparse, json_loads, json_dumps, xml_etree_parse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 9.09 ms: 1.03x slower                                                   |
| Geometric mean         | (ref)                                                    | 1.03x slower                                                            |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_text, genshi_xml, django_template, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 479 us                                                   | 315 us: 1.52x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 446 ms: 1.48x faster                                                    |
| deepcopy_memo              | 53.0 us                                                  | 36.9 us: 1.44x faster                                                   |
| async_tree_memoization     | 664 ms                                                   | 472 ms: 1.41x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 848 ms: 1.37x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 361 ms: 1.34x faster                                                    |
| async_tree_none            | 504 ms                                                   | 377 ms: 1.34x faster                                                    |
| spectral_norm              | 143 ms                                                   | 109 ms: 1.32x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 869 ms: 1.31x faster                                                    |
| scimark_fft                | 463 ms                                                   | 363 ms: 1.27x faster                                                    |
| go                         | 164 ms                                                   | 131 ms: 1.25x faster                                                    |
| deepcopy_reduce            | 4.24 us                                                  | 3.41 us: 1.24x faster                                                   |
| scimark_sor                | 164 ms                                                   | 138 ms: 1.19x faster                                                    |
| scimark_monte_carlo        | 87.8 ms                                                  | 74.7 ms: 1.17x faster                                                   |
| regex_effbot               | 5.10 ms                                                  | 4.38 ms: 1.17x faster                                                   |
| pathlib                    | 24.3 ms                                                  | 21.1 ms: 1.16x faster                                                   |
| pylint                     | 345 ms                                                   | 299 ms: 1.15x faster                                                    |
| scimark_lu                 | 146 ms                                                   | 127 ms: 1.15x faster                                                    |
| float                      | 95.8 ms                                                  | 83.8 ms: 1.14x faster                                                   |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 5.84 ms: 1.14x faster                                                   |
| logging_silent             | 135 ns                                                   | 118 ns: 1.14x faster                                                    |
| telco                      | 10.5 ms                                                  | 9.18 ms: 1.14x faster                                                   |
| generators                 | 40.3 ms                                                  | 35.8 ms: 1.13x faster                                                   |
| richards_super             | 60.8 ms                                                  | 54.4 ms: 1.12x faster                                                   |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 722 ms: 1.11x faster                                                    |
| xml_etree_generate         | 118 ms                                                   | 107 ms: 1.11x faster                                                    |
| tomli_loads                | 2.67 sec                                                 | 2.41 sec: 1.11x faster                                                  |
| richards                   | 54.5 ms                                                  | 49.4 ms: 1.10x faster                                                   |
| coverage                   | 106 ms                                                   | 96.1 ms: 1.10x faster                                                   |
| sqlglot_parse              | 1.43 ms                                                  | 1.31 ms: 1.09x faster                                                   |
| pyflate                    | 582 ms                                                   | 533 ms: 1.09x faster                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 5.52 sec: 1.09x faster                                                  |
| chaos                      | 70.7 ms                                                  | 65.0 ms: 1.09x faster                                                   |
| nbody                      | 118 ms                                                   | 109 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 728 ms: 1.08x faster                                                    |
| logging_format             | 8.10 us                                                  | 7.48 us: 1.08x faster                                                   |
| html5lib                   | 65.6 ms                                                  | 60.6 ms: 1.08x faster                                                   |
| pycparser                  | 1.34 sec                                                 | 1.24 sec: 1.08x faster                                                  |
| logging_simple             | 7.25 us                                                  | 6.71 us: 1.08x faster                                                   |
| async_generators           | 500 ms                                                   | 465 ms: 1.08x faster                                                    |
| 2to3                       | 313 ms                                                   | 293 ms: 1.07x faster                                                    |
| unpickle_pure_python       | 265 us                                                   | 248 us: 1.07x faster                                                    |
| sqlglot_normalize          | 131 ms                                                   | 124 ms: 1.06x faster                                                    |
| mdp                        | 3.45 sec                                                 | 3.27 sec: 1.05x faster                                                  |
| k_core                     | 2.99 sec                                                 | 2.85 sec: 1.05x faster                                                  |
| comprehensions             | 20.8 us                                                  | 20.0 us: 1.04x faster                                                   |
| sphinx                     | 1.20 sec                                                 | 1.16 sec: 1.03x faster                                                  |
| sympy_str                  | 265 ms                                                   | 261 ms: 1.02x faster                                                    |
| docutils                   | 2.96 sec                                                 | 3.01 sec: 1.01x slower                                                  |
| python_startup_no_site     | 8.79 ms                                                  | 9.09 ms: 1.03x slower                                                   |
| regex_v8                   | 32.5 ms                                                  | 34.4 ms: 1.06x slower                                                   |
| create_gc_cycles           | 3.39 ms                                                  | 3.82 ms: 1.13x slower                                                   |
| many_optionals             | 626 us                                                   | 718 us: 1.15x slower                                                    |
| gc_traversal               | 5.92 ms                                                  | 6.87 ms: 1.16x slower                                                   |
| pidigits                   | 238 ms                                                   | 307 ms: 1.29x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 26.5 ms: 1.30x slower                                                   |
| bench_mp_pool              | 8.07 ms                                                  | 4.51 sec: 559.52x slower                                                |
| Geometric mean             | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (38): sqlglot_transpile, thrift, sympy_sum, genshi_text, xml_etree_process, regex_compile, xml_etree_iterparse, bench_thread_pool, deltablue, nqueens, sqlalchemy_declarative, sqlglot_optimize, sympy_integrate, raytrace, genshi_xml, sympy_expand, json, hexiom, connected_components, coroutines, django_template, pprint_pformat, meteor_contest, sqlite_synth, asyncio_websockets, regex_dna, typing_runtime_protocols, fannkuch, json_loads, pprint_safe_repr, sqlalchemy_imperative, shortest_path, python_startup, mako, json_dumps, crypto_pyaes, xml_etree_parse, pickle_pure_python
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20250107-3.14.0a3+-f1d3190-CLANG/bm-20250107-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190.json: dulwich_log

- Geometric mean (including insignificant results): 1.066x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.06x