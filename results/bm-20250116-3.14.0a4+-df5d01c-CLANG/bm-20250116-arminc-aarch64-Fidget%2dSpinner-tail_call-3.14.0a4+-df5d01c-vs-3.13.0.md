# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: tail_call
- machine: linux-aarch64
- commit hash: df5d01c
- commit date: 2025-01-16
- overall geometric mean: 1.060x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 298 ms: 1.05x faster                                                    |
| html5lib       | 65.6 ms                                                  | 60.3 ms: 1.09x faster                                                   |
| sphinx         | 1.20 sec                                                 | 1.14 sec: 1.05x faster                                                  |
| Geometric mean | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 460 ms: 1.44x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 487 ms: 1.36x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 867 ms: 1.34x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 368 ms: 1.32x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 876 ms: 1.30x faster                                                    |
| async_tree_none            | 504 ms                                                   | 388 ms: 1.30x faster                                                    |
| async_generators           | 500 ms                                                   | 419 ms: 1.20x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 735 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 755 ms: 1.05x faster                                                    |
| coroutines                 | 29.4 ms                                                  | 28.2 ms: 1.04x faster                                                   |
| Geometric mean             | (ref)                                                    | 1.21x faster                                                            |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 83.8 ms: 1.14x faster                                                   |
| nbody          | 118 ms                                                   | 108 ms: 1.09x faster                                                    |
| pidigits       | 238 ms                                                   | 302 ms: 1.27x slower                                                    |
| Geometric mean | (ref)                                                    | 1.00x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.47 ms: 1.14x faster                                                   |
| regex_compile  | 134 ms                                                   | 125 ms: 1.07x faster                                                    |
| regex_v8       | 32.5 ms                                                  | 34.2 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark         | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|-------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads       | 2.67 sec                                                 | 2.46 sec: 1.08x faster                                                  |
| xml_etree_process | 82.1 ms                                                  | 77.2 ms: 1.06x faster                                                   |
| Geometric mean    | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (7): xml_etree_generate, xml_etree_iterparse, unpickle_pure_python, json_loads, xml_etree_parse, pickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 9.10 ms: 1.04x slower                                                   |
| Geometric mean         | (ref)                                                    | 1.03x slower                                                            |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text    | 28.6 ms                                                  | 26.8 ms: 1.07x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (3): genshi_xml, mako, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 53.0 us                                                  | 36.7 us: 1.44x faster                                                   |
| async_tree_memoization_tg  | 663 ms                                                   | 460 ms: 1.44x faster                                                    |
| deepcopy                   | 479 us                                                   | 335 us: 1.43x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 487 ms: 1.36x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 867 ms: 1.34x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 368 ms: 1.32x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 876 ms: 1.30x faster                                                    |
| async_tree_none            | 504 ms                                                   | 388 ms: 1.30x faster                                                    |
| go                         | 164 ms                                                   | 132 ms: 1.24x faster                                                    |
| spectral_norm              | 143 ms                                                   | 116 ms: 1.24x faster                                                    |
| scimark_fft                | 463 ms                                                   | 377 ms: 1.23x faster                                                    |
| deepcopy_reduce            | 4.24 us                                                  | 3.49 us: 1.22x faster                                                   |
| async_generators           | 500 ms                                                   | 419 ms: 1.20x faster                                                    |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 5.67 ms: 1.17x faster                                                   |
| scimark_monte_carlo        | 87.8 ms                                                  | 75.3 ms: 1.17x faster                                                   |
| pathlib                    | 24.3 ms                                                  | 20.9 ms: 1.16x faster                                                   |
| scimark_sor                | 164 ms                                                   | 141 ms: 1.16x faster                                                    |
| logging_silent             | 135 ns                                                   | 117 ns: 1.15x faster                                                    |
| float                      | 95.8 ms                                                  | 83.8 ms: 1.14x faster                                                   |
| regex_effbot               | 5.10 ms                                                  | 4.47 ms: 1.14x faster                                                   |
| telco                      | 10.5 ms                                                  | 9.16 ms: 1.14x faster                                                   |
| pylint                     | 345 ms                                                   | 303 ms: 1.14x faster                                                    |
| richards                   | 54.5 ms                                                  | 47.9 ms: 1.14x faster                                                   |
| generators                 | 40.3 ms                                                  | 36.6 ms: 1.10x faster                                                   |
| pyflate                    | 582 ms                                                   | 531 ms: 1.10x faster                                                    |
| nbody                      | 118 ms                                                   | 108 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 735 ms: 1.09x faster                                                    |
| html5lib                   | 65.6 ms                                                  | 60.3 ms: 1.09x faster                                                   |
| tomli_loads                | 2.67 sec                                                 | 2.46 sec: 1.08x faster                                                  |
| bpe_tokeniser              | 6.02 sec                                                 | 5.55 sec: 1.08x faster                                                  |
| coverage                   | 106 ms                                                   | 98.5 ms: 1.07x faster                                                   |
| regex_compile              | 134 ms                                                   | 125 ms: 1.07x faster                                                    |
| richards_super             | 60.8 ms                                                  | 56.7 ms: 1.07x faster                                                   |
| genshi_text                | 28.6 ms                                                  | 26.8 ms: 1.07x faster                                                   |
| k_core                     | 2.99 sec                                                 | 2.81 sec: 1.06x faster                                                  |
| xml_etree_process          | 82.1 ms                                                  | 77.2 ms: 1.06x faster                                                   |
| pycparser                  | 1.34 sec                                                 | 1.27 sec: 1.06x faster                                                  |
| logging_simple             | 7.25 us                                                  | 6.86 us: 1.06x faster                                                   |
| deltablue                  | 3.97 ms                                                  | 3.76 ms: 1.05x faster                                                   |
| mdp                        | 3.45 sec                                                 | 3.27 sec: 1.05x faster                                                  |
| sphinx                     | 1.20 sec                                                 | 1.14 sec: 1.05x faster                                                  |
| 2to3                       | 313 ms                                                   | 298 ms: 1.05x faster                                                    |
| chaos                      | 70.7 ms                                                  | 67.5 ms: 1.05x faster                                                   |
| sqlglot_parse              | 1.43 ms                                                  | 1.37 ms: 1.05x faster                                                   |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 755 ms: 1.05x faster                                                    |
| coroutines                 | 29.4 ms                                                  | 28.2 ms: 1.04x faster                                                   |
| connected_components       | 547 ms                                                   | 532 ms: 1.03x faster                                                    |
| sympy_str                  | 265 ms                                                   | 261 ms: 1.02x faster                                                    |
| python_startup_no_site     | 8.79 ms                                                  | 9.10 ms: 1.04x slower                                                   |
| regex_v8                   | 32.5 ms                                                  | 34.2 ms: 1.05x slower                                                   |
| create_gc_cycles           | 3.39 ms                                                  | 3.70 ms: 1.09x slower                                                   |
| gc_traversal               | 5.92 ms                                                  | 6.67 ms: 1.13x slower                                                   |
| many_optionals             | 626 us                                                   | 725 us: 1.16x slower                                                    |
| pidigits                   | 238 ms                                                   | 302 ms: 1.27x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 26.7 ms: 1.31x slower                                                   |
| bench_mp_pool              | 8.07 ms                                                  | 6.83 sec: 847.06x slower                                                |
| Geometric mean             | (ref)                                                    | 1.01x slower                                                            |

Benchmark hidden because not significant (39): xml_etree_generate, scimark_lu, sympy_sum, xml_etree_iterparse, logging_format, unpickle_pure_python, sqlalchemy_imperative, thrift, nqueens, hexiom, sqlglot_optimize, comprehensions, sqlalchemy_declarative, sqlglot_transpile, sympy_integrate, genshi_xml, json, typing_runtime_protocols, bench_thread_pool, pprint_pformat, crypto_pyaes, asyncio_websockets, sqlglot_normalize, raytrace, mako, sympy_expand, pprint_safe_repr, shortest_path, sqlite_synth, json_loads, docutils, regex_dna, meteor_contest, fannkuch, xml_etree_parse, python_startup, pickle_pure_python, django_template, json_dumps
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20250116-3.14.0a4+-df5d01c-CLANG/bm-20250116-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c.json: dulwich_log

- Geometric mean (including insignificant results): 1.060x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.06x