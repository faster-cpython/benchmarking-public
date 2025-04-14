# Results vs. 3.13.0

- fork: mdboom
- ref: tuple_hash_cache2
- machine: linux-x86_64
- commit hash: d2c521a
- commit date: 2025-03-24
- overall geometric mean: 1.037x slower
- HPT reliability: 99.34%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250324-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-d2c521a |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 325 ms: 1.11x slower                                                      |
| docutils       | 2.83 sec                                                     | 2.94 sec: 1.04x slower                                                    |
| sphinx         | 1.12 sec                                                     | 1.17 sec: 1.04x slower                                                    |
| Geometric mean | (ref)                                                        | 1.05x slower                                                              |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250324-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-d2c521a |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io_tg           | 831 ms                                                       | 551 ms: 1.51x faster                                                      |
| async_tree_memoization_tg  | 466 ms                                                       | 310 ms: 1.51x faster                                                      |
| async_tree_io              | 843 ms                                                       | 587 ms: 1.44x faster                                                      |
| async_tree_none_tg         | 346 ms                                                       | 246 ms: 1.41x faster                                                      |
| async_tree_none            | 376 ms                                                       | 283 ms: 1.33x faster                                                      |
| async_tree_memoization     | 453 ms                                                       | 342 ms: 1.32x faster                                                      |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 477 ms: 1.22x faster                                                      |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 511 ms: 1.18x faster                                                      |
| asyncio_websockets         | 388 ms                                                       | 381 ms: 1.02x faster                                                      |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.02x faster                                                     |
| async_generators           | 457 ms                                                       | 465 ms: 1.02x slower                                                      |
| Geometric mean             | (ref)                                                        | 1.25x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250324-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-d2c521a |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 76.8 ms: 1.06x faster                                                     |
| pidigits       | 252 ms                                                       | 249 ms: 1.01x faster                                                      |
| nbody          | 89.3 ms                                                      | 131 ms: 1.47x slower                                                      |
| Geometric mean | (ref)                                                        | 1.11x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250324-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-d2c521a |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.09 ms: 1.19x faster                                                     |
| regex_v8       | 26.1 ms                                                      | 23.1 ms: 1.13x faster                                                     |
| regex_dna      | 247 ms                                                       | 234 ms: 1.05x faster                                                      |
| regex_compile  | 143 ms                                                       | 161 ms: 1.13x slower                                                      |
| Geometric mean | (ref)                                                        | 1.06x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250324-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-d2c521a |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 88.8 ms: 1.16x faster                                                     |
| xml_etree_parse      | 150 ms                                                       | 136 ms: 1.11x faster                                                      |
| tomli_loads          | 2.46 sec                                                     | 2.44 sec: 1.01x faster                                                    |
| xml_etree_generate   | 86.5 ms                                                      | 97.2 ms: 1.12x slower                                                     |
| unpickle_pure_python | 217 us                                                       | 247 us: 1.14x slower                                                      |
| xml_etree_process    | 61.2 ms                                                      | 69.7 ms: 1.14x slower                                                     |
| pickle_pure_python   | 323 us                                                       | 372 us: 1.15x slower                                                      |
| json_loads           | 24.7 us                                                      | 29.1 us: 1.18x slower                                                     |
| json_dumps           | 11.1 ms                                                      | 13.2 ms: 1.18x slower                                                     |
| Geometric mean       | (ref)                                                        | 1.07x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250324-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-d2c521a |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 19.5 ms: 1.22x slower                                                     |
| python_startup_no_site | 8.96 ms                                                      | 13.8 ms: 1.54x slower                                                     |
| Geometric mean         | (ref)                                                        | 1.37x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250324-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-d2c521a |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_xml      | 57.1 ms                                                      | 63.5 ms: 1.11x slower                                                     |
| genshi_text     | 26.2 ms                                                      | 30.4 ms: 1.16x slower                                                     |
| django_template | 36.4 ms                                                      | 45.8 ms: 1.26x slower                                                     |
| mako            | 10.4 ms                                                      | 17.6 ms: 1.70x slower                                                     |
| Geometric mean  | (ref)                                                        | 1.29x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250324-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-d2c521a |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| gc_traversal               | 4.74 ms                                                      | 2.12 ms: 2.24x faster                                                     |
| mdp                        | 2.54 sec                                                     | 1.57 sec: 1.62x faster                                                    |
| async_tree_io_tg           | 831 ms                                                       | 551 ms: 1.51x faster                                                      |
| async_tree_memoization_tg  | 466 ms                                                       | 310 ms: 1.51x faster                                                      |
| async_tree_io              | 843 ms                                                       | 587 ms: 1.44x faster                                                      |
| create_gc_cycles           | 2.68 ms                                                      | 1.90 ms: 1.41x faster                                                     |
| async_tree_none_tg         | 346 ms                                                       | 246 ms: 1.41x faster                                                      |
| async_tree_none            | 376 ms                                                       | 283 ms: 1.33x faster                                                      |
| async_tree_memoization     | 453 ms                                                       | 342 ms: 1.32x faster                                                      |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 477 ms: 1.22x faster                                                      |
| regex_effbot               | 3.67 ms                                                      | 3.09 ms: 1.19x faster                                                     |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 511 ms: 1.18x faster                                                      |
| deepcopy                   | 392 us                                                       | 333 us: 1.18x faster                                                      |
| xml_etree_iterparse        | 103 ms                                                       | 88.8 ms: 1.16x faster                                                     |
| regex_v8                   | 26.1 ms                                                      | 23.1 ms: 1.13x faster                                                     |
| sqlite_synth               | 2.91 us                                                      | 2.59 us: 1.12x faster                                                     |
| generators                 | 33.6 ms                                                      | 30.3 ms: 1.11x faster                                                     |
| xml_etree_parse            | 150 ms                                                       | 136 ms: 1.11x faster                                                      |
| go                         | 162 ms                                                       | 151 ms: 1.08x faster                                                      |
| float                      | 81.3 ms                                                      | 76.8 ms: 1.06x faster                                                     |
| dulwich_log                | 68.2 ms                                                      | 64.3 ms: 1.06x faster                                                     |
| regex_dna                  | 247 ms                                                       | 234 ms: 1.05x faster                                                      |
| deepcopy_memo              | 38.6 us                                                      | 36.9 us: 1.05x faster                                                     |
| asyncio_websockets         | 388 ms                                                       | 381 ms: 1.02x faster                                                      |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.02x faster                                                     |
| scimark_sor                | 123 ms                                                       | 121 ms: 1.02x faster                                                      |
| pidigits                   | 252 ms                                                       | 249 ms: 1.01x faster                                                      |
| pyflate                    | 503 ms                                                       | 497 ms: 1.01x faster                                                      |
| tomli_loads                | 2.46 sec                                                     | 2.44 sec: 1.01x faster                                                    |
| json                       | 5.69 ms                                                      | 5.64 ms: 1.01x faster                                                     |
| pathlib                    | 17.5 ms                                                      | 17.4 ms: 1.01x faster                                                     |
| deepcopy_reduce            | 3.54 us                                                      | 3.56 us: 1.01x slower                                                     |
| pycparser                  | 1.24 sec                                                     | 1.26 sec: 1.01x slower                                                    |
| async_generators           | 457 ms                                                       | 465 ms: 1.02x slower                                                      |
| logging_silent             | 97.9 ns                                                      | 101 ns: 1.03x slower                                                      |
| docutils                   | 2.83 sec                                                     | 2.94 sec: 1.04x slower                                                    |
| sphinx                     | 1.12 sec                                                     | 1.17 sec: 1.04x slower                                                    |
| spectral_norm              | 97.0 ms                                                      | 102 ms: 1.05x slower                                                      |
| bpe_tokeniser              | 5.09 sec                                                     | 5.33 sec: 1.05x slower                                                    |
| pprint_safe_repr           | 843 ms                                                       | 900 ms: 1.07x slower                                                      |
| scimark_fft                | 328 ms                                                       | 352 ms: 1.07x slower                                                      |
| pprint_pformat             | 1.72 sec                                                     | 1.85 sec: 1.07x slower                                                    |
| richards                   | 52.9 ms                                                      | 56.9 ms: 1.08x slower                                                     |
| telco                      | 8.79 ms                                                      | 9.46 ms: 1.08x slower                                                     |
| k_core                     | 2.17 sec                                                     | 2.38 sec: 1.10x slower                                                    |
| richards_super             | 59.6 ms                                                      | 65.7 ms: 1.10x slower                                                     |
| 2to3                       | 293 ms                                                       | 325 ms: 1.11x slower                                                      |
| sympy_expand               | 509 ms                                                       | 566 ms: 1.11x slower                                                      |
| genshi_xml                 | 57.1 ms                                                      | 63.5 ms: 1.11x slower                                                     |
| logging_simple             | 6.39 us                                                      | 7.18 us: 1.12x slower                                                     |
| sympy_integrate            | 23.6 ms                                                      | 26.5 ms: 1.12x slower                                                     |
| xml_etree_generate         | 86.5 ms                                                      | 97.2 ms: 1.12x slower                                                     |
| regex_compile              | 143 ms                                                       | 161 ms: 1.13x slower                                                      |
| sympy_str                  | 298 ms                                                       | 336 ms: 1.13x slower                                                      |
| sqlalchemy_imperative      | 18.3 ms                                                      | 20.6 ms: 1.13x slower                                                     |
| sympy_sum                  | 155 ms                                                       | 175 ms: 1.13x slower                                                      |
| shortest_path              | 460 ms                                                       | 523 ms: 1.14x slower                                                      |
| unpickle_pure_python       | 217 us                                                       | 247 us: 1.14x slower                                                      |
| xml_etree_process          | 61.2 ms                                                      | 69.7 ms: 1.14x slower                                                     |
| hexiom                     | 6.55 ms                                                      | 7.48 ms: 1.14x slower                                                     |
| logging_format             | 6.94 us                                                      | 7.95 us: 1.15x slower                                                     |
| connected_components       | 432 ms                                                       | 495 ms: 1.15x slower                                                      |
| pickle_pure_python         | 323 us                                                       | 372 us: 1.15x slower                                                      |
| sqlalchemy_declarative     | 148 ms                                                       | 172 ms: 1.16x slower                                                      |
| chaos                      | 60.2 ms                                                      | 69.8 ms: 1.16x slower                                                     |
| genshi_text                | 26.2 ms                                                      | 30.4 ms: 1.16x slower                                                     |
| deltablue                  | 3.42 ms                                                      | 4.04 ms: 1.18x slower                                                     |
| json_loads                 | 24.7 us                                                      | 29.1 us: 1.18x slower                                                     |
| json_dumps                 | 11.1 ms                                                      | 13.2 ms: 1.18x slower                                                     |
| comprehensions             | 17.0 us                                                      | 20.2 us: 1.19x slower                                                     |
| many_optionals             | 930 us                                                       | 1.12 ms: 1.20x slower                                                     |
| meteor_contest             | 130 ms                                                       | 155 ms: 1.20x slower                                                      |
| raytrace                   | 273 ms                                                       | 330 ms: 1.21x slower                                                      |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 5.78 ms: 1.21x slower                                                     |
| python_startup             | 15.9 ms                                                      | 19.5 ms: 1.22x slower                                                     |
| nqueens                    | 90.7 ms                                                      | 111 ms: 1.23x slower                                                      |
| scimark_lu                 | 98.7 ms                                                      | 123 ms: 1.24x slower                                                      |
| django_template            | 36.4 ms                                                      | 45.8 ms: 1.26x slower                                                     |
| scimark_monte_carlo        | 66.1 ms                                                      | 83.8 ms: 1.27x slower                                                     |
| typing_runtime_protocols   | 169 us                                                       | 218 us: 1.29x slower                                                      |
| crypto_pyaes               | 73.3 ms                                                      | 96.0 ms: 1.31x slower                                                     |
| fannkuch                   | 363 ms                                                       | 483 ms: 1.33x slower                                                      |
| subparsers                 | 17.5 ms                                                      | 25.4 ms: 1.45x slower                                                     |
| coverage                   | 80.0 ms                                                      | 116 ms: 1.46x slower                                                      |
| nbody                      | 89.3 ms                                                      | 131 ms: 1.47x slower                                                      |
| bench_thread_pool          | 942 us                                                       | 1.44 ms: 1.53x slower                                                     |
| python_startup_no_site     | 8.96 ms                                                      | 13.8 ms: 1.54x slower                                                     |
| mako                       | 10.4 ms                                                      | 17.6 ms: 1.70x slower                                                     |
| bench_mp_pool              | 5.12 ms                                                      | 50.4 ms: 9.84x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.07x slower                                                              |

Benchmark hidden because not significant (2): html5lib, pylint
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250324-3.14.0a6+-d2c521a-NOGIL/bm-20250324-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-d2c521a.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.037x slower

# HPT report

- Reliability score: 99.34% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.25x