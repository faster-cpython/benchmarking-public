# Results vs. 3.13.0

- fork: python
- ref: e119526edface001ad7d
- machine: linux-x86_64
- commit hash: e119526
- commit date: 2025-01-25
- overall geometric mean: 1.055x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250125-pythonperf2-x86_64-python-e119526edface001ad7d-3.14.0a4+-e119526 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 282 ms: 1.04x faster                                                         |
| docutils       | 2.83 sec                                                     | 2.89 sec: 1.02x slower                                                       |
| html5lib       | 73.5 ms                                                      | 66.3 ms: 1.11x faster                                                        |
| sphinx         | 1.12 sec                                                     | 1.11 sec: 1.01x faster                                                       |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250125-pythonperf2-x86_64-python-e119526edface001ad7d-3.14.0a4+-e119526 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 336 ms: 1.39x faster                                                         |
| async_tree_io              | 843 ms                                                       | 642 ms: 1.31x faster                                                         |
| async_tree_none            | 376 ms                                                       | 290 ms: 1.30x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 350 ms: 1.29x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 647 ms: 1.29x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 279 ms: 1.24x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 518 ms: 1.16x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 507 ms: 1.15x faster                                                         |
| async_generators           | 457 ms                                                       | 421 ms: 1.08x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 20.7 ms: 1.04x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 384 ms: 1.01x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.20x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250125-pythonperf2-x86_64-python-e119526edface001ad7d-3.14.0a4+-e119526 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 69.5 ms: 1.17x faster                                                        |
| pidigits       | 252 ms                                                       | 254 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250125-pythonperf2-x86_64-python-e119526edface001ad7d-3.14.0a4+-e119526 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.06 ms: 1.20x faster                                                        |
| regex_compile  | 143 ms                                                       | 135 ms: 1.06x faster                                                         |
| regex_dna      | 247 ms                                                       | 237 ms: 1.04x faster                                                         |
| regex_v8       | 26.1 ms                                                      | 25.2 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250125-pythonperf2-x86_64-python-e119526edface001ad7d-3.14.0a4+-e119526 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.03 sec: 1.21x faster                                                       |
| xml_etree_parse      | 150 ms                                                       | 136 ms: 1.11x faster                                                         |
| unpickle_pure_python | 217 us                                                       | 209 us: 1.04x faster                                                         |
| xml_etree_generate   | 86.5 ms                                                      | 83.9 ms: 1.03x faster                                                        |
| xml_etree_process    | 61.2 ms                                                      | 59.5 ms: 1.03x faster                                                        |
| pickle_pure_python   | 323 us                                                       | 328 us: 1.02x slower                                                         |
| json_dumps           | 11.1 ms                                                      | 11.6 ms: 1.05x slower                                                        |
| json_loads           | 24.7 us                                                      | 37.5 us: 1.52x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250125-pythonperf2-x86_64-python-e119526edface001ad7d-3.14.0a4+-e119526 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup | 15.9 ms                                                      | 16.0 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                 |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250125-pythonperf2-x86_64-python-e119526edface001ad7d-3.14.0a4+-e119526 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.6 ms: 1.11x faster                                                        |
| genshi_xml      | 57.1 ms                                                      | 53.0 ms: 1.08x faster                                                        |
| django_template | 36.4 ms                                                      | 36.0 ms: 1.01x faster                                                        |
| mako            | 10.4 ms                                                      | 10.9 ms: 1.06x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.03x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250125-pythonperf2-x86_64-python-e119526edface001ad7d-3.14.0a4+-e119526 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 336 ms: 1.39x faster                                                         |
| deepcopy                   | 392 us                                                       | 283 us: 1.39x faster                                                         |
| deepcopy_memo              | 38.6 us                                                      | 29.4 us: 1.32x faster                                                        |
| async_tree_io              | 843 ms                                                       | 642 ms: 1.31x faster                                                         |
| async_tree_none            | 376 ms                                                       | 290 ms: 1.30x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 350 ms: 1.29x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 647 ms: 1.29x faster                                                         |
| go                         | 162 ms                                                       | 126 ms: 1.28x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 279 ms: 1.24x faster                                                         |
| tomli_loads                | 2.46 sec                                                     | 2.03 sec: 1.21x faster                                                       |
| regex_effbot               | 3.67 ms                                                      | 3.06 ms: 1.20x faster                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 2.97 us: 1.19x faster                                                        |
| float                      | 81.3 ms                                                      | 69.5 ms: 1.17x faster                                                        |
| spectral_norm              | 97.0 ms                                                      | 83.1 ms: 1.17x faster                                                        |
| generators                 | 33.6 ms                                                      | 28.8 ms: 1.17x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 518 ms: 1.16x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 507 ms: 1.15x faster                                                         |
| richards                   | 52.9 ms                                                      | 46.3 ms: 1.14x faster                                                        |
| richards_super             | 59.6 ms                                                      | 52.4 ms: 1.14x faster                                                        |
| pathlib                    | 17.5 ms                                                      | 15.7 ms: 1.12x faster                                                        |
| pyflate                    | 503 ms                                                       | 452 ms: 1.11x faster                                                         |
| genshi_text                | 26.2 ms                                                      | 23.6 ms: 1.11x faster                                                        |
| html5lib                   | 73.5 ms                                                      | 66.3 ms: 1.11x faster                                                        |
| xml_etree_parse            | 150 ms                                                       | 136 ms: 1.11x faster                                                         |
| pylint                     | 347 ms                                                       | 316 ms: 1.10x faster                                                         |
| bpe_tokeniser              | 5.09 sec                                                     | 4.66 sec: 1.09x faster                                                       |
| hexiom                     | 6.55 ms                                                      | 6.02 ms: 1.09x faster                                                        |
| async_generators           | 457 ms                                                       | 421 ms: 1.08x faster                                                         |
| scimark_sor                | 123 ms                                                       | 114 ms: 1.08x faster                                                         |
| telco                      | 8.79 ms                                                      | 8.12 ms: 1.08x faster                                                        |
| genshi_xml                 | 57.1 ms                                                      | 53.0 ms: 1.08x faster                                                        |
| pprint_pformat             | 1.72 sec                                                     | 1.61 sec: 1.07x faster                                                       |
| pprint_safe_repr           | 843 ms                                                       | 789 ms: 1.07x faster                                                         |
| scimark_fft                | 328 ms                                                       | 307 ms: 1.07x faster                                                         |
| sqlglot_parse              | 1.40 ms                                                      | 1.32 ms: 1.06x faster                                                        |
| logging_simple             | 6.39 us                                                      | 6.05 us: 1.06x faster                                                        |
| regex_compile              | 143 ms                                                       | 135 ms: 1.06x faster                                                         |
| sqlglot_transpile          | 1.79 ms                                                      | 1.71 ms: 1.05x faster                                                        |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.56 ms: 1.05x faster                                                        |
| shortest_path              | 460 ms                                                       | 440 ms: 1.05x faster                                                         |
| coverage                   | 80.0 ms                                                      | 76.5 ms: 1.04x faster                                                        |
| deltablue                  | 3.42 ms                                                      | 3.27 ms: 1.04x faster                                                        |
| sqlglot_normalize          | 119 ms                                                       | 114 ms: 1.04x faster                                                         |
| regex_dna                  | 247 ms                                                       | 237 ms: 1.04x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 20.7 ms: 1.04x faster                                                        |
| unpickle_pure_python       | 217 us                                                       | 209 us: 1.04x faster                                                         |
| k_core                     | 2.17 sec                                                     | 2.09 sec: 1.04x faster                                                       |
| logging_format             | 6.94 us                                                      | 6.68 us: 1.04x faster                                                        |
| connected_components       | 432 ms                                                       | 416 ms: 1.04x faster                                                         |
| sympy_expand               | 509 ms                                                       | 491 ms: 1.04x faster                                                         |
| sqlalchemy_declarative     | 148 ms                                                       | 143 ms: 1.04x faster                                                         |
| 2to3                       | 293 ms                                                       | 282 ms: 1.04x faster                                                         |
| sqlalchemy_imperative      | 18.3 ms                                                      | 17.6 ms: 1.04x faster                                                        |
| thrift                     | 901 us                                                       | 869 us: 1.04x faster                                                         |
| regex_v8                   | 26.1 ms                                                      | 25.2 ms: 1.04x faster                                                        |
| dulwich_log                | 68.2 ms                                                      | 65.9 ms: 1.03x faster                                                        |
| sympy_str                  | 298 ms                                                       | 288 ms: 1.03x faster                                                         |
| sqlglot_optimize           | 59.3 ms                                                      | 57.4 ms: 1.03x faster                                                        |
| xml_etree_generate         | 86.5 ms                                                      | 83.9 ms: 1.03x faster                                                        |
| scimark_lu                 | 98.7 ms                                                      | 95.7 ms: 1.03x faster                                                        |
| pycparser                  | 1.24 sec                                                     | 1.21 sec: 1.03x faster                                                       |
| xml_etree_process          | 61.2 ms                                                      | 59.5 ms: 1.03x faster                                                        |
| sqlite_synth               | 2.91 us                                                      | 2.83 us: 1.03x faster                                                        |
| mdp                        | 2.54 sec                                                     | 2.48 sec: 1.03x faster                                                       |
| scimark_monte_carlo        | 66.1 ms                                                      | 64.7 ms: 1.02x faster                                                        |
| sympy_integrate            | 23.6 ms                                                      | 23.1 ms: 1.02x faster                                                        |
| meteor_contest             | 130 ms                                                       | 127 ms: 1.02x faster                                                         |
| nqueens                    | 90.7 ms                                                      | 89.0 ms: 1.02x faster                                                        |
| sympy_sum                  | 155 ms                                                       | 152 ms: 1.02x faster                                                         |
| sphinx                     | 1.12 sec                                                     | 1.11 sec: 1.01x faster                                                       |
| chaos                      | 60.2 ms                                                      | 59.6 ms: 1.01x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 384 ms: 1.01x faster                                                         |
| raytrace                   | 273 ms                                                       | 270 ms: 1.01x faster                                                         |
| django_template            | 36.4 ms                                                      | 36.0 ms: 1.01x faster                                                        |
| python_startup             | 15.9 ms                                                      | 16.0 ms: 1.01x slower                                                        |
| pidigits                   | 252 ms                                                       | 254 ms: 1.01x slower                                                         |
| typing_runtime_protocols   | 169 us                                                       | 171 us: 1.01x slower                                                         |
| create_gc_cycles           | 2.68 ms                                                      | 2.72 ms: 1.01x slower                                                        |
| pickle_pure_python         | 323 us                                                       | 328 us: 1.02x slower                                                         |
| fannkuch                   | 363 ms                                                       | 370 ms: 1.02x slower                                                         |
| docutils                   | 2.83 sec                                                     | 2.89 sec: 1.02x slower                                                       |
| comprehensions             | 17.0 us                                                      | 17.8 us: 1.04x slower                                                        |
| json_dumps                 | 11.1 ms                                                      | 11.6 ms: 1.05x slower                                                        |
| mako                       | 10.4 ms                                                      | 10.9 ms: 1.06x slower                                                        |
| many_optionals             | 930 us                                                       | 1.01 ms: 1.08x slower                                                        |
| json                       | 5.69 ms                                                      | 6.82 ms: 1.20x slower                                                        |
| subparsers                 | 17.5 ms                                                      | 22.8 ms: 1.31x slower                                                        |
| gc_traversal               | 4.74 ms                                                      | 6.34 ms: 1.34x slower                                                        |
| json_loads                 | 24.7 us                                                      | 37.5 us: 1.52x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 1.17 sec: 228.11x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.00x slower                                                                 |

Benchmark hidden because not significant (6): bench_thread_pool, logging_silent, python_startup_no_site, crypto_pyaes, xml_etree_iterparse, nbody
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.055x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.27x