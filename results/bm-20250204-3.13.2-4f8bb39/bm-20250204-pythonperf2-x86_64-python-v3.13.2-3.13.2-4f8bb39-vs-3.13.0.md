# Results vs. 3.13.0

- fork: python
- ref: v3.13.2
- machine: linux-x86_64
- commit hash: 4f8bb39
- commit date: 2025-02-04
- overall geometric mean: 1.004x faster
- HPT reliability: 99.04%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-pythonperf2-x86_64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 294 ms: 1.00x slower                                         |
| chameleon      | 7.55 ms                                                      | 7.48 ms: 1.01x faster                                        |
| docutils       | 2.83 sec                                                     | 2.81 sec: 1.00x faster                                       |
| html5lib       | 73.5 ms                                                      | 73.7 ms: 1.00x slower                                        |
| sphinx         | 1.12 sec                                                     | 1.11 sec: 1.01x faster                                       |
| Geometric mean | (ref)                                                        | 1.00x faster                                                 |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-pythonperf2-x86_64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| async_generators           | 457 ms                                                       | 427 ms: 1.07x faster                                         |
| asyncio_websockets         | 388 ms                                                       | 382 ms: 1.01x faster                                         |
| coroutines                 | 21.6 ms                                                      | 21.4 ms: 1.01x faster                                        |
| async_tree_memoization_tg  | 466 ms                                                       | 463 ms: 1.01x faster                                         |
| async_tree_io              | 843 ms                                                       | 856 ms: 1.01x slower                                         |
| async_tree_none            | 376 ms                                                       | 382 ms: 1.02x slower                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 614 ms: 1.02x slower                                         |
| async_tree_memoization     | 453 ms                                                       | 476 ms: 1.05x slower                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 617 ms: 1.06x slower                                         |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                 |

Benchmark hidden because not significant (2): async_tree_none_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-pythonperf2-x86_64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 80.3 ms: 1.01x faster                                        |
| pidigits       | 252 ms                                                       | 261 ms: 1.03x slower                                         |
| Geometric mean | (ref)                                                        | 1.00x slower                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-pythonperf2-x86_64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.26 ms: 1.13x faster                                        |
| regex_v8       | 26.1 ms                                                      | 25.4 ms: 1.03x faster                                        |
| regex_dna      | 247 ms                                                       | 240 ms: 1.03x faster                                         |
| regex_compile  | 143 ms                                                       | 141 ms: 1.01x faster                                         |
| Geometric mean | (ref)                                                        | 1.05x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-pythonperf2-x86_64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| xml_etree_process    | 61.2 ms                                                      | 60.1 ms: 1.02x faster                                        |
| unpickle_pure_python | 217 us                                                       | 214 us: 1.01x faster                                         |
| json_dumps           | 11.1 ms                                                      | 11.0 ms: 1.01x faster                                        |
| tomli_loads          | 2.46 sec                                                     | 2.45 sec: 1.00x faster                                       |
| pickle_pure_python   | 323 us                                                       | 327 us: 1.01x slower                                         |
| json_loads           | 24.7 us                                                      | 25.0 us: 1.01x slower                                        |
| xml_etree_iterparse  | 103 ms                                                       | 104 ms: 1.01x slower                                         |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                 |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-pythonperf2-x86_64-python-v3.13.2-3.13.2-4f8bb39 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 8.96 ms                                                      | 9.03 ms: 1.01x slower                                        |
| python_startup         | 15.9 ms                                                      | 16.1 ms: 1.01x slower                                        |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-pythonperf2-x86_64-python-v3.13.2-3.13.2-4f8bb39 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 36.4 ms                                                      | 35.5 ms: 1.02x faster                                        |
| genshi_xml      | 57.1 ms                                                      | 56.6 ms: 1.01x faster                                        |
| genshi_text     | 26.2 ms                                                      | 26.0 ms: 1.01x faster                                        |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                 |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-pythonperf2-x86_64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_effbot               | 3.67 ms                                                      | 3.26 ms: 1.13x faster                                        |
| async_generators           | 457 ms                                                       | 427 ms: 1.07x faster                                         |
| pyflate                    | 503 ms                                                       | 475 ms: 1.06x faster                                         |
| json                       | 5.69 ms                                                      | 5.45 ms: 1.04x faster                                        |
| scimark_fft                | 328 ms                                                       | 315 ms: 1.04x faster                                         |
| pprint_safe_repr           | 843 ms                                                       | 812 ms: 1.04x faster                                         |
| pprint_pformat             | 1.72 sec                                                     | 1.66 sec: 1.04x faster                                       |
| bench_mp_pool              | 5.12 ms                                                      | 4.95 ms: 1.03x faster                                        |
| regex_v8                   | 26.1 ms                                                      | 25.4 ms: 1.03x faster                                        |
| hexiom                     | 6.55 ms                                                      | 6.37 ms: 1.03x faster                                        |
| bench_thread_pool          | 942 us                                                       | 917 us: 1.03x faster                                         |
| regex_dna                  | 247 ms                                                       | 240 ms: 1.03x faster                                         |
| django_template            | 36.4 ms                                                      | 35.5 ms: 1.02x faster                                        |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.68 ms: 1.02x faster                                        |
| logging_silent             | 97.9 ns                                                      | 96.0 ns: 1.02x faster                                        |
| deltablue                  | 3.42 ms                                                      | 3.36 ms: 1.02x faster                                        |
| scimark_monte_carlo        | 66.1 ms                                                      | 65.0 ms: 1.02x faster                                        |
| thrift                     | 901 us                                                       | 885 us: 1.02x faster                                         |
| xml_etree_process          | 61.2 ms                                                      | 60.1 ms: 1.02x faster                                        |
| crypto_pyaes               | 73.3 ms                                                      | 72.1 ms: 1.02x faster                                        |
| go                         | 162 ms                                                       | 160 ms: 1.02x faster                                         |
| chaos                      | 60.2 ms                                                      | 59.3 ms: 1.02x faster                                        |
| unpickle_pure_python       | 217 us                                                       | 214 us: 1.01x faster                                         |
| asyncio_websockets         | 388 ms                                                       | 382 ms: 1.01x faster                                         |
| json_dumps                 | 11.1 ms                                                      | 11.0 ms: 1.01x faster                                        |
| spectral_norm              | 97.0 ms                                                      | 95.6 ms: 1.01x faster                                        |
| float                      | 81.3 ms                                                      | 80.3 ms: 1.01x faster                                        |
| sphinx                     | 1.12 sec                                                     | 1.11 sec: 1.01x faster                                       |
| deepcopy                   | 392 us                                                       | 387 us: 1.01x faster                                         |
| nqueens                    | 90.7 ms                                                      | 89.7 ms: 1.01x faster                                        |
| richards                   | 52.9 ms                                                      | 52.3 ms: 1.01x faster                                        |
| coroutines                 | 21.6 ms                                                      | 21.4 ms: 1.01x faster                                        |
| chameleon                  | 7.55 ms                                                      | 7.48 ms: 1.01x faster                                        |
| sqlalchemy_declarative     | 148 ms                                                       | 147 ms: 1.01x faster                                         |
| regex_compile              | 143 ms                                                       | 141 ms: 1.01x faster                                         |
| genshi_xml                 | 57.1 ms                                                      | 56.6 ms: 1.01x faster                                        |
| subparsers                 | 17.5 ms                                                      | 17.3 ms: 1.01x faster                                        |
| genshi_text                | 26.2 ms                                                      | 26.0 ms: 1.01x faster                                        |
| deepcopy_reduce            | 3.54 us                                                      | 3.52 us: 1.01x faster                                        |
| pathlib                    | 17.5 ms                                                      | 17.4 ms: 1.01x faster                                        |
| sqlglot_parse              | 1.40 ms                                                      | 1.39 ms: 1.01x faster                                        |
| async_tree_memoization_tg  | 466 ms                                                       | 463 ms: 1.01x faster                                         |
| dulwich_log                | 68.2 ms                                                      | 67.8 ms: 1.01x faster                                        |
| many_optionals             | 930 us                                                       | 926 us: 1.00x faster                                         |
| sqlglot_optimize           | 59.3 ms                                                      | 59.0 ms: 1.00x faster                                        |
| tomli_loads                | 2.46 sec                                                     | 2.45 sec: 1.00x faster                                       |
| sympy_integrate            | 23.6 ms                                                      | 23.5 ms: 1.00x faster                                        |
| richards_super             | 59.6 ms                                                      | 59.3 ms: 1.00x faster                                        |
| deepcopy_memo              | 38.6 us                                                      | 38.5 us: 1.00x faster                                        |
| docutils                   | 2.83 sec                                                     | 2.81 sec: 1.00x faster                                       |
| scimark_lu                 | 98.7 ms                                                      | 98.3 ms: 1.00x faster                                        |
| sympy_expand               | 509 ms                                                       | 508 ms: 1.00x faster                                         |
| meteor_contest             | 130 ms                                                       | 129 ms: 1.00x faster                                         |
| html5lib                   | 73.5 ms                                                      | 73.7 ms: 1.00x slower                                        |
| 2to3                       | 293 ms                                                       | 294 ms: 1.00x slower                                         |
| connected_components       | 432 ms                                                       | 434 ms: 1.00x slower                                         |
| fannkuch                   | 363 ms                                                       | 365 ms: 1.01x slower                                         |
| telco                      | 8.79 ms                                                      | 8.84 ms: 1.01x slower                                        |
| python_startup_no_site     | 8.96 ms                                                      | 9.03 ms: 1.01x slower                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 5.14 sec: 1.01x slower                                       |
| pycparser                  | 1.24 sec                                                     | 1.26 sec: 1.01x slower                                       |
| python_startup             | 15.9 ms                                                      | 16.1 ms: 1.01x slower                                        |
| pickle_pure_python         | 323 us                                                       | 327 us: 1.01x slower                                         |
| create_gc_cycles           | 2.68 ms                                                      | 2.72 ms: 1.01x slower                                        |
| json_loads                 | 24.7 us                                                      | 25.0 us: 1.01x slower                                        |
| xml_etree_iterparse        | 103 ms                                                       | 104 ms: 1.01x slower                                         |
| async_tree_io              | 843 ms                                                       | 856 ms: 1.01x slower                                         |
| async_tree_none            | 376 ms                                                       | 382 ms: 1.02x slower                                         |
| raytrace                   | 273 ms                                                       | 277 ms: 1.02x slower                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 614 ms: 1.02x slower                                         |
| typing_runtime_protocols   | 169 us                                                       | 173 us: 1.02x slower                                         |
| comprehensions             | 17.0 us                                                      | 17.6 us: 1.03x slower                                        |
| pidigits                   | 252 ms                                                       | 261 ms: 1.03x slower                                         |
| gc_traversal               | 4.74 ms                                                      | 4.92 ms: 1.04x slower                                        |
| async_tree_memoization     | 453 ms                                                       | 476 ms: 1.05x slower                                         |
| coverage                   | 80.0 ms                                                      | 84.7 ms: 1.06x slower                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 617 ms: 1.06x slower                                         |
| Geometric mean             | (ref)                                                        | 1.00x faster                                                 |

Benchmark hidden because not significant (24): nbody, async_tree_none_tg, sqlglot_transpile, scimark_sor, pylint, sqlite_synth, mdp, xml_etree_parse, shortest_path, sqlalchemy_imperative, k_core, sympy_sum, logging_format, sympy_str, generators, sqlglot_normalize, xml_etree_generate, gunicorn, gevent_hub, logging_simple, mako, djangocms, tornado_http, async_tree_io_tg

- Geometric mean (including insignificant results): 1.004x faster

# HPT report

- Reliability score: 99.04% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x