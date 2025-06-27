# Results vs. 3.13.0

- fork: python
- ref: fba5dded6df3c2b19435
- machine: linux-aarch64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.061x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 298 ms: 1.05x faster                                                    |
| html5lib       | 65.6 ms                                                  | 61.3 ms: 1.07x faster                                                   |
| sphinx         | 1.20 sec                                                 | 1.13 sec: 1.06x faster                                                  |
| Geometric mean | (ref)                                                    | 1.05x faster                                                            |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 664 ms                                                   | 470 ms: 1.41x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 472 ms: 1.40x faster                                                    |
| async_tree_none            | 504 ms                                                   | 395 ms: 1.28x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 915 ms: 1.27x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 897 ms: 1.27x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 383 ms: 1.26x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 662 ms: 1.21x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 662 ms: 1.19x faster                                                    |
| async_generators           | 500 ms                                                   | 442 ms: 1.13x faster                                                    |
| Geometric mean             | (ref)                                                    | 1.22x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 85.7 ms: 1.12x faster                                                   |
| Geometric mean | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.99 ms: 1.28x faster                                                   |
| regex_v8       | 32.5 ms                                                  | 26.5 ms: 1.23x faster                                                   |
| regex_dna      | 263 ms                                                   | 223 ms: 1.18x faster                                                    |
| regex_compile  | 134 ms                                                   | 122 ms: 1.09x faster                                                    |
| Geometric mean | (ref)                                                    | 1.19x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 180 ms: 1.12x faster                                                    |
| xml_etree_iterparse | 159 ms                                                   | 142 ms: 1.12x faster                                                    |
| tomli_loads         | 2.67 sec                                                 | 2.45 sec: 1.09x faster                                                  |
| xml_etree_process   | 82.1 ms                                                  | 79.2 ms: 1.04x faster                                                   |
| Geometric mean      | (ref)                                                    | 1.05x faster                                                            |

Benchmark hidden because not significant (5): xml_etree_generate, json_dumps, unpickle_pure_python, json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 15.0 ms: 1.07x faster                                                   |
| python_startup_no_site | 8.79 ms                                                  | 8.54 ms: 1.03x faster                                                   |
| Geometric mean         | (ref)                                                    | 1.05x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml     | 61.6 ms                                                  | 60.4 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (3): genshi_text, mako, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.68 sec: 2.05x faster                                                  |
| deepcopy                   | 479 us                                                   | 338 us: 1.41x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 470 ms: 1.41x faster                                                    |
| deepcopy_memo              | 53.0 us                                                  | 37.6 us: 1.41x faster                                                   |
| async_tree_memoization_tg  | 663 ms                                                   | 472 ms: 1.40x faster                                                    |
| regex_effbot               | 5.10 ms                                                  | 3.99 ms: 1.28x faster                                                   |
| async_tree_none            | 504 ms                                                   | 395 ms: 1.28x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 915 ms: 1.27x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 897 ms: 1.27x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 383 ms: 1.26x faster                                                    |
| go                         | 164 ms                                                   | 130 ms: 1.26x faster                                                    |
| regex_v8                   | 32.5 ms                                                  | 26.5 ms: 1.23x faster                                                   |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 662 ms: 1.21x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 662 ms: 1.19x faster                                                    |
| regex_dna                  | 263 ms                                                   | 223 ms: 1.18x faster                                                    |
| spectral_norm              | 143 ms                                                   | 125 ms: 1.15x faster                                                    |
| deepcopy_reduce            | 4.24 us                                                  | 3.75 us: 1.13x faster                                                   |
| telco                      | 10.5 ms                                                  | 9.23 ms: 1.13x faster                                                   |
| async_generators           | 500 ms                                                   | 442 ms: 1.13x faster                                                    |
| scimark_sor                | 164 ms                                                   | 145 ms: 1.13x faster                                                    |
| xml_etree_parse            | 203 ms                                                   | 180 ms: 1.12x faster                                                    |
| generators                 | 40.3 ms                                                  | 36.0 ms: 1.12x faster                                                   |
| float                      | 95.8 ms                                                  | 85.7 ms: 1.12x faster                                                   |
| xml_etree_iterparse        | 159 ms                                                   | 142 ms: 1.12x faster                                                    |
| scimark_monte_carlo        | 87.8 ms                                                  | 79.2 ms: 1.11x faster                                                   |
| pylint                     | 345 ms                                                   | 315 ms: 1.10x faster                                                    |
| pathlib                    | 24.3 ms                                                  | 22.2 ms: 1.10x faster                                                   |
| pyflate                    | 582 ms                                                   | 532 ms: 1.09x faster                                                    |
| regex_compile              | 134 ms                                                   | 122 ms: 1.09x faster                                                    |
| tomli_loads                | 2.67 sec                                                 | 2.45 sec: 1.09x faster                                                  |
| bpe_tokeniser              | 6.02 sec                                                 | 5.53 sec: 1.09x faster                                                  |
| pycparser                  | 1.34 sec                                                 | 1.24 sec: 1.09x faster                                                  |
| k_core                     | 2.99 sec                                                 | 2.79 sec: 1.07x faster                                                  |
| nqueens                    | 105 ms                                                   | 97.9 ms: 1.07x faster                                                   |
| scimark_fft                | 463 ms                                                   | 432 ms: 1.07x faster                                                    |
| hexiom                     | 7.34 ms                                                  | 6.86 ms: 1.07x faster                                                   |
| html5lib                   | 65.6 ms                                                  | 61.3 ms: 1.07x faster                                                   |
| sqlite_synth               | 4.08 us                                                  | 3.82 us: 1.07x faster                                                   |
| python_startup             | 16.0 ms                                                  | 15.0 ms: 1.07x faster                                                   |
| sphinx                     | 1.20 sec                                                 | 1.13 sec: 1.06x faster                                                  |
| sympy_integrate            | 21.4 ms                                                  | 20.4 ms: 1.05x faster                                                   |
| thrift                     | 1.01 ms                                                  | 961 us: 1.05x faster                                                    |
| 2to3                       | 313 ms                                                   | 298 ms: 1.05x faster                                                    |
| json                       | 5.94 ms                                                  | 5.65 ms: 1.05x faster                                                   |
| meteor_contest             | 117 ms                                                   | 112 ms: 1.04x faster                                                    |
| xml_etree_process          | 82.1 ms                                                  | 79.2 ms: 1.04x faster                                                   |
| richards                   | 54.5 ms                                                  | 52.6 ms: 1.04x faster                                                   |
| python_startup_no_site     | 8.79 ms                                                  | 8.54 ms: 1.03x faster                                                   |
| djangocms                  | 66.2 us                                                  | 65.0 us: 1.02x faster                                                   |
| genshi_xml                 | 61.6 ms                                                  | 60.4 ms: 1.02x faster                                                   |
| sympy_str                  | 265 ms                                                   | 263 ms: 1.01x faster                                                    |
| pprint_pformat             | 1.99 sec                                                 | 2.05 sec: 1.03x slower                                                  |
| shortest_path              | 565 ms                                                   | 583 ms: 1.03x slower                                                    |
| pprint_safe_repr           | 962 ms                                                   | 1.01 sec: 1.05x slower                                                  |
| raytrace                   | 310 ms                                                   | 328 ms: 1.06x slower                                                    |
| logging_simple             | 7.25 us                                                  | 7.70 us: 1.06x slower                                                   |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 7.13 ms: 1.07x slower                                                   |
| create_gc_cycles           | 3.39 ms                                                  | 3.84 ms: 1.13x slower                                                   |
| gc_traversal               | 5.92 ms                                                  | 7.00 ms: 1.18x slower                                                   |
| many_optionals             | 626 us                                                   | 772 us: 1.23x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 28.3 ms: 1.39x slower                                                   |
| logging_silent             | 135 ns                                                   | 643 ns: 4.78x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.05x faster                                                            |

Benchmark hidden because not significant (26): xml_etree_generate, json_dumps, genshi_text, chaos, sympy_sum, coverage, comprehensions, asyncio_websockets, mako, unpickle_pure_python, typing_runtime_protocols, docutils, crypto_pyaes, sympy_expand, json_loads, fannkuch, richards_super, coroutines, pidigits, django_template, nbody, connected_components, deltablue, logging_format, pickle_pure_python, scimark_lu
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.061x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.07x