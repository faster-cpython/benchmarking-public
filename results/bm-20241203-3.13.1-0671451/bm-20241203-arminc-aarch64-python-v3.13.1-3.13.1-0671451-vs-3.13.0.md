# Results vs. 3.13.0

- fork: python
- ref: v3.13.1
- machine: linux-aarch64
- commit hash: 0671451
- commit date: 2024-12-03
- overall geometric mean: 1.015x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241203-arminc-aarch64-python-v3.13.1-3.13.1-0671451 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 319 ms: 1.05x slower                                     |
| chameleon      | 9.08 ms                                                  | 9.41 ms: 1.04x slower                                    |
| docutils       | 2.89 sec                                                 | 2.95 sec: 1.02x slower                                   |
| Geometric mean | (ref)                                                    | 1.02x slower                                             |

Benchmark hidden because not significant (3): html5lib, sphinx, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241203-arminc-aarch64-python-v3.13.1-3.13.1-0671451 |
|----------------------------|:--------------------------------------------------------:|:--------------------------------------------------------:|
| asyncio_websockets         | 659 ms                                                   | 677 ms: 1.03x slower                                     |
| async_tree_none            | 497 ms                                                   | 517 ms: 1.04x slower                                     |
| async_tree_io_tg           | 1.13 sec                                                 | 1.18 sec: 1.04x slower                                   |
| async_tree_io              | 1.11 sec                                                 | 1.16 sec: 1.05x slower                                   |
| async_generators           | 489 ms                                                   | 517 ms: 1.06x slower                                     |
| coroutines                 | 28.5 ms                                                  | 30.2 ms: 1.06x slower                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 825 ms: 1.07x slower                                     |
| Geometric mean             | (ref)                                                    | 1.04x slower                                             |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_none_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241203-arminc-aarch64-python-v3.13.1-3.13.1-0671451 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------:|
| float          | 93.3 ms                                                  | 97.4 ms: 1.04x slower                                    |
| nbody          | 114 ms                                                   | 121 ms: 1.06x slower                                     |
| Geometric mean | (ref)                                                    | 1.04x slower                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241203-arminc-aarch64-python-v3.13.1-3.13.1-0671451 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------:|
| regex_effbot   | 4.89 ms                                                  | 4.06 ms: 1.20x faster                                    |
| regex_compile  | 127 ms                                                   | 131 ms: 1.03x slower                                     |
| regex_dna      | 253 ms                                                   | 266 ms: 1.05x slower                                     |
| Geometric mean | (ref)                                                    | 1.02x faster                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241203-arminc-aarch64-python-v3.13.1-3.13.1-0671451 |
|----------------------|:--------------------------------------------------------:|:--------------------------------------------------------:|
| xml_etree_generate   | 113 ms                                                   | 116 ms: 1.02x slower                                     |
| unpickle_pure_python | 251 us                                                   | 261 us: 1.04x slower                                     |
| tomli_loads          | 2.54 sec                                                 | 2.65 sec: 1.04x slower                                   |
| pickle_pure_python   | 357 us                                                   | 375 us: 1.05x slower                                     |
| json_loads           | 31.7 us                                                  | 34.3 us: 1.08x slower                                    |
| Geometric mean       | (ref)                                                    | 1.04x slower                                             |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_iterparse, json_dumps, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241203-arminc-aarch64-python-v3.13.1-3.13.1-0671451 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 16.0 ms: 1.04x slower                                    |
| Geometric mean | (ref)                                                    | 1.03x slower                                             |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241203-arminc-aarch64-python-v3.13.1-3.13.1-0671451 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------:|
| mako           | 13.4 ms                                                  | 14.1 ms: 1.06x slower                                    |
| genshi_text    | 27.7 ms                                                  | 30.3 ms: 1.09x slower                                    |
| Geometric mean | (ref)                                                    | 1.05x slower                                             |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241203-arminc-aarch64-python-v3.13.1-3.13.1-0671451 |
|----------------------------|:--------------------------------------------------------:|:--------------------------------------------------------:|
| regex_effbot               | 4.89 ms                                                  | 4.06 ms: 1.20x faster                                    |
| sympy_str                  | 264 ms                                                   | 267 ms: 1.01x slower                                     |
| docutils                   | 2.89 sec                                                 | 2.95 sec: 1.02x slower                                   |
| xml_etree_generate         | 113 ms                                                   | 116 ms: 1.02x slower                                     |
| bpe_tokeniser              | 5.87 sec                                                 | 6.03 sec: 1.03x slower                                   |
| regex_compile              | 127 ms                                                   | 131 ms: 1.03x slower                                     |
| asyncio_websockets         | 659 ms                                                   | 677 ms: 1.03x slower                                     |
| richards_super             | 60.1 ms                                                  | 61.9 ms: 1.03x slower                                    |
| chaos                      | 68.0 ms                                                  | 70.2 ms: 1.03x slower                                    |
| gc_traversal               | 5.77 ms                                                  | 5.97 ms: 1.03x slower                                    |
| typing_runtime_protocols   | 193 us                                                   | 200 us: 1.03x slower                                     |
| mdp                        | 3.34 sec                                                 | 3.46 sec: 1.04x slower                                   |
| pycparser                  | 1.27 sec                                                 | 1.32 sec: 1.04x slower                                   |
| chameleon                  | 9.08 ms                                                  | 9.41 ms: 1.04x slower                                    |
| hexiom                     | 7.11 ms                                                  | 7.38 ms: 1.04x slower                                    |
| async_tree_none            | 497 ms                                                   | 517 ms: 1.04x slower                                     |
| async_tree_io_tg           | 1.13 sec                                                 | 1.18 sec: 1.04x slower                                   |
| json                       | 5.73 ms                                                  | 5.97 ms: 1.04x slower                                    |
| unpickle_pure_python       | 251 us                                                   | 261 us: 1.04x slower                                     |
| sqlglot_parse              | 1.38 ms                                                  | 1.44 ms: 1.04x slower                                    |
| python_startup             | 15.4 ms                                                  | 16.0 ms: 1.04x slower                                    |
| sqlglot_normalize          | 127 ms                                                   | 132 ms: 1.04x slower                                     |
| float                      | 93.3 ms                                                  | 97.4 ms: 1.04x slower                                    |
| go                         | 160 ms                                                   | 167 ms: 1.04x slower                                     |
| logging_simple             | 7.07 us                                                  | 7.38 us: 1.04x slower                                    |
| tomli_loads                | 2.54 sec                                                 | 2.65 sec: 1.04x slower                                   |
| fannkuch                   | 461 ms                                                   | 482 ms: 1.05x slower                                     |
| coverage                   | 99.1 ms                                                  | 104 ms: 1.05x slower                                     |
| deltablue                  | 3.82 ms                                                  | 4.01 ms: 1.05x slower                                    |
| deepcopy_reduce            | 4.07 us                                                  | 4.27 us: 1.05x slower                                    |
| async_tree_io              | 1.11 sec                                                 | 1.16 sec: 1.05x slower                                   |
| pickle_pure_python         | 357 us                                                   | 375 us: 1.05x slower                                     |
| 2to3                       | 304 ms                                                   | 319 ms: 1.05x slower                                     |
| regex_dna                  | 253 ms                                                   | 266 ms: 1.05x slower                                     |
| logging_silent             | 133 ns                                                   | 140 ns: 1.05x slower                                     |
| connected_components       | 533 ms                                                   | 562 ms: 1.05x slower                                     |
| sympy_expand               | 457 ms                                                   | 481 ms: 1.05x slower                                     |
| scimark_monte_carlo        | 83.6 ms                                                  | 88.1 ms: 1.05x slower                                    |
| scimark_fft                | 447 ms                                                   | 472 ms: 1.06x slower                                     |
| async_generators           | 489 ms                                                   | 517 ms: 1.06x slower                                     |
| pathlib                    | 22.7 ms                                                  | 24.0 ms: 1.06x slower                                    |
| mako                       | 13.4 ms                                                  | 14.1 ms: 1.06x slower                                    |
| nbody                      | 114 ms                                                   | 121 ms: 1.06x slower                                     |
| deepcopy_memo              | 50.4 us                                                  | 53.4 us: 1.06x slower                                    |
| pprint_pformat             | 1.90 sec                                                 | 2.01 sec: 1.06x slower                                   |
| coroutines                 | 28.5 ms                                                  | 30.2 ms: 1.06x slower                                    |
| comprehensions             | 20.4 us                                                  | 21.6 us: 1.06x slower                                    |
| deepcopy                   | 447 us                                                   | 476 us: 1.06x slower                                     |
| pprint_safe_repr           | 926 ms                                                   | 987 ms: 1.06x slower                                     |
| thrift                     | 968 us                                                   | 1.03 ms: 1.07x slower                                    |
| scimark_sor                | 160 ms                                                   | 171 ms: 1.07x slower                                     |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 825 ms: 1.07x slower                                     |
| meteor_contest             | 114 ms                                                   | 122 ms: 1.08x slower                                     |
| sqlglot_transpile          | 1.73 ms                                                  | 1.86 ms: 1.08x slower                                    |
| json_loads                 | 31.7 us                                                  | 34.3 us: 1.08x slower                                    |
| genshi_text                | 27.7 ms                                                  | 30.3 ms: 1.09x slower                                    |
| generators                 | 37.6 ms                                                  | 41.2 ms: 1.10x slower                                    |
| pyflate                    | 556 ms                                                   | 614 ms: 1.10x slower                                     |
| telco                      | 9.74 ms                                                  | 10.8 ms: 1.11x slower                                    |
| bench_mp_pool              | 7.68 ms                                                  | 8.56 ms: 1.11x slower                                    |
| Geometric mean             | (ref)                                                    | 1.04x slower                                             |

Benchmark hidden because not significant (35): async_tree_cpu_io_mixed, nqueens, django_template, html5lib, async_tree_memoization_tg, k_core, crypto_pyaes, shortest_path, richards, python_startup_no_site, pidigits, raytrace, sphinx, gevent_hub, tornado_http, bench_thread_pool, async_tree_none_tg, create_gc_cycles, async_tree_memoization, xml_etree_parse, xml_etree_iterparse, scimark_lu, sympy_integrate, spectral_norm, logging_format, sympy_sum, sqlalchemy_declarative, genshi_xml, sqlglot_optimize, regex_v8, pylint, json_dumps, xml_etree_process, sqlalchemy_imperative, scimark_sparse_mat_mult
Ignored benchmarks (1) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: mypy2
Ignored benchmarks (5) of results/bm-20241203-3.13.1-0671451/bm-20241203-arminc-aarch64-python-v3.13.1-3.13.1-0671451.json: djangocms, gunicorn, many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.015x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x