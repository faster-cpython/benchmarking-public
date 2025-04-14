# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: clang_hot
- machine: linux-aarch64
- commit hash: 37fb620
- commit date: 2025-03-06
- overall geometric mean: 1.058x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250306-arminc-aarch64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 296 ms: 1.06x faster                                                    |
| html5lib       | 65.6 ms                                                  | 60.4 ms: 1.09x faster                                                   |
| sphinx         | 1.20 sec                                                 | 1.13 sec: 1.06x faster                                                  |
| Geometric mean | (ref)                                                    | 1.05x faster                                                            |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250306-arminc-aarch64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 470 ms: 1.41x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 479 ms: 1.38x faster                                                    |
| async_tree_none            | 504 ms                                                   | 374 ms: 1.35x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 890 ms: 1.31x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 376 ms: 1.29x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 902 ms: 1.26x faster                                                    |
| async_generators           | 500 ms                                                   | 418 ms: 1.20x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 731 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 744 ms: 1.06x faster                                                    |
| Geometric mean             | (ref)                                                    | 1.21x faster                                                            |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250306-arminc-aarch64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 88.2 ms: 1.09x faster                                                   |
| pidigits       | 238 ms                                                   | 305 ms: 1.28x slower                                                    |
| Geometric mean | (ref)                                                    | 1.05x slower                                                            |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250306-arminc-aarch64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.41 ms: 1.16x faster                                                   |
| regex_compile  | 134 ms                                                   | 125 ms: 1.07x faster                                                    |
| regex_v8       | 32.5 ms                                                  | 34.4 ms: 1.06x slower                                                   |
| Geometric mean | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250306-arminc-aarch64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|--------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate | 118 ms                                                   | 107 ms: 1.11x faster                                                    |
| tomli_loads        | 2.67 sec                                                 | 2.43 sec: 1.10x faster                                                  |
| xml_etree_process  | 82.1 ms                                                  | 77.0 ms: 1.07x faster                                                   |
| xml_etree_parse    | 203 ms                                                   | 224 ms: 1.11x slower                                                    |
| Geometric mean     | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (5): json_dumps, xml_etree_iterparse, unpickle_pure_python, pickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250306-arminc-aarch64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 9.33 ms: 1.06x slower                                                   |
| Geometric mean         | (ref)                                                    | 1.05x slower                                                            |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250306-arminc-aarch64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 28.6 ms                                                  | 26.9 ms: 1.06x faster                                                   |
| django_template | 39.4 ms                                                  | 38.2 ms: 1.03x faster                                                   |
| Geometric mean  | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (2): genshi_xml, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250306-arminc-aarch64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 479 us                                                   | 315 us: 1.52x faster                                                    |
| deepcopy_memo              | 53.0 us                                                  | 36.4 us: 1.46x faster                                                   |
| async_tree_memoization_tg  | 663 ms                                                   | 470 ms: 1.41x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 479 ms: 1.38x faster                                                    |
| async_tree_none            | 504 ms                                                   | 374 ms: 1.35x faster                                                    |
| spectral_norm              | 143 ms                                                   | 109 ms: 1.31x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 890 ms: 1.31x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 376 ms: 1.29x faster                                                    |
| deepcopy_reduce            | 4.24 us                                                  | 3.31 us: 1.28x faster                                                   |
| async_tree_io              | 1.14 sec                                                 | 902 ms: 1.26x faster                                                    |
| go                         | 164 ms                                                   | 133 ms: 1.24x faster                                                    |
| async_generators           | 500 ms                                                   | 418 ms: 1.20x faster                                                    |
| scimark_fft                | 463 ms                                                   | 391 ms: 1.18x faster                                                    |
| regex_effbot               | 5.10 ms                                                  | 4.41 ms: 1.16x faster                                                   |
| pylint                     | 345 ms                                                   | 302 ms: 1.14x faster                                                    |
| pathlib                    | 24.3 ms                                                  | 21.3 ms: 1.14x faster                                                   |
| scimark_sor                | 164 ms                                                   | 144 ms: 1.14x faster                                                    |
| generators                 | 40.3 ms                                                  | 35.7 ms: 1.13x faster                                                   |
| coverage                   | 106 ms                                                   | 93.9 ms: 1.12x faster                                                   |
| bpe_tokeniser              | 6.02 sec                                                 | 5.42 sec: 1.11x faster                                                  |
| xml_etree_generate         | 118 ms                                                   | 107 ms: 1.11x faster                                                    |
| logging_silent             | 135 ns                                                   | 122 ns: 1.10x faster                                                    |
| logging_format             | 8.10 us                                                  | 7.37 us: 1.10x faster                                                   |
| tomli_loads                | 2.67 sec                                                 | 2.43 sec: 1.10x faster                                                  |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 731 ms: 1.09x faster                                                    |
| richards                   | 54.5 ms                                                  | 49.8 ms: 1.09x faster                                                   |
| sqlglot_transpile          | 1.84 ms                                                  | 1.69 ms: 1.09x faster                                                   |
| float                      | 95.8 ms                                                  | 88.2 ms: 1.09x faster                                                   |
| html5lib                   | 65.6 ms                                                  | 60.4 ms: 1.09x faster                                                   |
| scimark_monte_carlo        | 87.8 ms                                                  | 81.2 ms: 1.08x faster                                                   |
| sqlglot_optimize           | 65.2 ms                                                  | 60.5 ms: 1.08x faster                                                   |
| telco                      | 10.5 ms                                                  | 9.73 ms: 1.07x faster                                                   |
| pyflate                    | 582 ms                                                   | 542 ms: 1.07x faster                                                    |
| typing_runtime_protocols   | 197 us                                                   | 184 us: 1.07x faster                                                    |
| pycparser                  | 1.34 sec                                                 | 1.26 sec: 1.07x faster                                                  |
| regex_compile              | 134 ms                                                   | 125 ms: 1.07x faster                                                    |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 6.23 ms: 1.07x faster                                                   |
| xml_etree_process          | 82.1 ms                                                  | 77.0 ms: 1.07x faster                                                   |
| genshi_text                | 28.6 ms                                                  | 26.9 ms: 1.06x faster                                                   |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 744 ms: 1.06x faster                                                    |
| sphinx                     | 1.20 sec                                                 | 1.13 sec: 1.06x faster                                                  |
| 2to3                       | 313 ms                                                   | 296 ms: 1.06x faster                                                    |
| sqlglot_normalize          | 131 ms                                                   | 124 ms: 1.06x faster                                                    |
| k_core                     | 2.99 sec                                                 | 2.84 sec: 1.05x faster                                                  |
| sympy_expand               | 472 ms                                                   | 453 ms: 1.04x faster                                                    |
| mdp                        | 3.45 sec                                                 | 3.31 sec: 1.04x faster                                                  |
| pprint_pformat             | 1.99 sec                                                 | 1.92 sec: 1.04x faster                                                  |
| django_template            | 39.4 ms                                                  | 38.2 ms: 1.03x faster                                                   |
| regex_v8                   | 32.5 ms                                                  | 34.4 ms: 1.06x slower                                                   |
| python_startup_no_site     | 8.79 ms                                                  | 9.33 ms: 1.06x slower                                                   |
| create_gc_cycles           | 3.39 ms                                                  | 3.68 ms: 1.09x slower                                                   |
| xml_etree_parse            | 203 ms                                                   | 224 ms: 1.11x slower                                                    |
| gc_traversal               | 5.92 ms                                                  | 6.73 ms: 1.14x slower                                                   |
| subparsers                 | 20.3 ms                                                  | 25.8 ms: 1.27x slower                                                   |
| pidigits                   | 238 ms                                                   | 305 ms: 1.28x slower                                                    |
| many_optionals             | 626 us                                                   | 827 us: 1.32x slower                                                    |
| bench_mp_pool              | 8.07 ms                                                  | 7.27 sec: 900.93x slower                                                |
| Geometric mean             | (ref)                                                    | 1.01x slower                                                            |

Benchmark hidden because not significant (38): sympy_sum, chaos, thrift, sqlalchemy_declarative, nqueens, sqlalchemy_imperative, richards_super, logging_simple, scimark_lu, comprehensions, sympy_integrate, sqlglot_parse, coroutines, sqlite_synth, bench_thread_pool, genshi_xml, pprint_safe_repr, hexiom, deltablue, mako, json_dumps, nbody, connected_components, regex_dna, docutils, asyncio_websockets, shortest_path, xml_etree_iterparse, unpickle_pure_python, json, raytrace, pickle_pure_python, sympy_str, python_startup, meteor_contest, fannkuch, crypto_pyaes, json_loads
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20250306-3.14.0a5+-37fb620-CLANG/bm-20250306-arminc-aarch64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620.json: dulwich_log

- Geometric mean (including insignificant results): 1.058x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.06x