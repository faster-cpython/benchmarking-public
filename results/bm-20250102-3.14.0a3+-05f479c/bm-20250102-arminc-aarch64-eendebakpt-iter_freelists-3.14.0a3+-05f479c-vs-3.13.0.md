# Results vs. 3.13.0

- fork: eendebakpt
- ref: iter_freelists
- machine: linux-aarch64
- commit hash: 05f479c
- commit date: 2025-01-02
- overall geometric mean: 1.041x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-arminc-aarch64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------------:|
| sphinx         | 1.20 sec                                                 | 1.16 sec: 1.04x faster                                                 |
| Geometric mean | (ref)                                                    | 1.01x faster                                                           |

Benchmark hidden because not significant (3): 2to3, docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-arminc-aarch64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------------------|:--------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 467 ms: 1.42x faster                                                   |
| async_tree_memoization     | 664 ms                                                   | 486 ms: 1.37x faster                                                   |
| async_tree_none            | 504 ms                                                   | 383 ms: 1.32x faster                                                   |
| async_tree_io_tg           | 1.16 sec                                                 | 885 ms: 1.32x faster                                                   |
| async_tree_io              | 1.14 sec                                                 | 873 ms: 1.31x faster                                                   |
| async_tree_none_tg         | 484 ms                                                   | 378 ms: 1.28x faster                                                   |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 656 ms: 1.22x faster                                                   |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 671 ms: 1.18x faster                                                   |
| Geometric mean             | (ref)                                                    | 1.21x faster                                                           |

Benchmark hidden because not significant (3): coroutines, async_generators, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-arminc-aarch64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 90.6 ms: 1.06x faster                                                  |
| Geometric mean | (ref)                                                    | 1.01x faster                                                           |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-arminc-aarch64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.03 ms: 1.27x faster                                                  |
| regex_dna      | 263 ms                                                   | 248 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                    | 1.09x faster                                                           |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-arminc-aarch64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|---------------------|:--------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 180 ms: 1.13x faster                                                   |
| xml_etree_iterparse | 159 ms                                                   | 143 ms: 1.11x faster                                                   |
| tomli_loads         | 2.67 sec                                                 | 2.58 sec: 1.03x faster                                                 |
| pickle_pure_python  | 374 us                                                   | 399 us: 1.07x slower                                                   |
| Geometric mean      | (ref)                                                    | 1.03x faster                                                           |

Benchmark hidden because not significant (5): xml_etree_generate, xml_etree_process, json_loads, unpickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_text, genshi_xml, django_template, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-arminc-aarch64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------------------|:--------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 467 ms: 1.42x faster                                                   |
| deepcopy                   | 479 us                                                   | 345 us: 1.39x faster                                                   |
| async_tree_memoization     | 664 ms                                                   | 486 ms: 1.37x faster                                                   |
| async_tree_none            | 504 ms                                                   | 383 ms: 1.32x faster                                                   |
| async_tree_io_tg           | 1.16 sec                                                 | 885 ms: 1.32x faster                                                   |
| async_tree_io              | 1.14 sec                                                 | 873 ms: 1.31x faster                                                   |
| async_tree_none_tg         | 484 ms                                                   | 378 ms: 1.28x faster                                                   |
| deepcopy_memo              | 53.0 us                                                  | 41.5 us: 1.28x faster                                                  |
| regex_effbot               | 5.10 ms                                                  | 4.03 ms: 1.27x faster                                                  |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 656 ms: 1.22x faster                                                   |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 671 ms: 1.18x faster                                                   |
| deepcopy_reduce            | 4.24 us                                                  | 3.65 us: 1.16x faster                                                  |
| xml_etree_parse            | 203 ms                                                   | 180 ms: 1.13x faster                                                   |
| go                         | 164 ms                                                   | 146 ms: 1.12x faster                                                   |
| xml_etree_iterparse        | 159 ms                                                   | 143 ms: 1.11x faster                                                   |
| pathlib                    | 24.3 ms                                                  | 21.9 ms: 1.11x faster                                                  |
| pylint                     | 345 ms                                                   | 312 ms: 1.11x faster                                                   |
| spectral_norm              | 143 ms                                                   | 130 ms: 1.10x faster                                                   |
| generators                 | 40.3 ms                                                  | 36.6 ms: 1.10x faster                                                  |
| scimark_fft                | 463 ms                                                   | 423 ms: 1.09x faster                                                   |
| telco                      | 10.5 ms                                                  | 9.70 ms: 1.08x faster                                                  |
| thrift                     | 1.01 ms                                                  | 938 us: 1.08x faster                                                   |
| bpe_tokeniser              | 6.02 sec                                                 | 5.62 sec: 1.07x faster                                                 |
| sqlglot_optimize           | 65.2 ms                                                  | 61.2 ms: 1.07x faster                                                  |
| regex_dna                  | 263 ms                                                   | 248 ms: 1.06x faster                                                   |
| float                      | 95.8 ms                                                  | 90.6 ms: 1.06x faster                                                  |
| sqlglot_normalize          | 131 ms                                                   | 124 ms: 1.06x faster                                                   |
| k_core                     | 2.99 sec                                                 | 2.86 sec: 1.05x faster                                                 |
| richards                   | 54.5 ms                                                  | 52.3 ms: 1.04x faster                                                  |
| pycparser                  | 1.34 sec                                                 | 1.29 sec: 1.04x faster                                                 |
| sphinx                     | 1.20 sec                                                 | 1.16 sec: 1.04x faster                                                 |
| tomli_loads                | 2.67 sec                                                 | 2.58 sec: 1.03x faster                                                 |
| mdp                        | 3.45 sec                                                 | 3.40 sec: 1.01x faster                                                 |
| sympy_str                  | 265 ms                                                   | 262 ms: 1.01x faster                                                   |
| connected_components       | 547 ms                                                   | 567 ms: 1.04x slower                                                   |
| shortest_path              | 565 ms                                                   | 588 ms: 1.04x slower                                                   |
| create_gc_cycles           | 3.39 ms                                                  | 3.53 ms: 1.04x slower                                                  |
| logging_silent             | 135 ns                                                   | 142 ns: 1.06x slower                                                   |
| raytrace                   | 310 ms                                                   | 330 ms: 1.07x slower                                                   |
| pickle_pure_python         | 374 us                                                   | 399 us: 1.07x slower                                                   |
| many_optionals             | 626 us                                                   | 720 us: 1.15x slower                                                   |
| gc_traversal               | 5.92 ms                                                  | 7.03 ms: 1.19x slower                                                  |
| subparsers                 | 20.3 ms                                                  | 25.5 ms: 1.26x slower                                                  |
| bench_mp_pool              | 8.07 ms                                                  | 5.00 sec: 619.22x slower                                               |
| Geometric mean             | (ref)                                                    | 1.03x slower                                                           |

Benchmark hidden because not significant (52): sympy_sum, scimark_lu, regex_compile, coverage, scimark_sparse_mat_mult, xml_etree_generate, 2to3, nqueens, json, sympy_expand, scimark_monte_carlo, logging_format, sqlite_synth, xml_etree_process, genshi_text, sqlglot_transpile, sqlalchemy_declarative, json_loads, sympy_integrate, scimark_sor, coroutines, async_generators, meteor_contest, unpickle_pure_python, deltablue, crypto_pyaes, bench_thread_pool, regex_v8, asyncio_websockets, fannkuch, djangocms, pidigits, pprint_pformat, sqlglot_parse, pprint_safe_repr, sqlalchemy_imperative, docutils, richards_super, python_startup_no_site, pyflate, hexiom, comprehensions, logging_simple, nbody, python_startup, html5lib, chaos, typing_runtime_protocols, json_dumps, genshi_xml, django_template, mako
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (2) of results/bm-20250102-3.14.0a3+-05f479c/bm-20250102-arminc-aarch64-eendebakpt-iter_freelists-3.14.0a3+-05f479c.json: dulwich_log, mypy2

- Geometric mean (including insignificant results): 1.041x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.02x