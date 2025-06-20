# Results vs. 3.13.0

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-x86_64
- commit hash: 2850d72
- commit date: 2025-06-19
- overall geometric mean: 1.117x slower
- HPT reliability: 99.93%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 333 ms: 1.14x slower                                                                |
| docutils       | 2.83 sec                                                     | 3.17 sec: 1.12x slower                                                              |
| html5lib       | 73.5 ms                                                      | 70.8 ms: 1.04x faster                                                               |
| sphinx         | 1.12 sec                                                     | 1.14 sec: 1.02x slower                                                              |
| Geometric mean | (ref)                                                        | 1.06x slower                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 360 ms: 1.29x faster                                                                |
| async_tree_memoization     | 453 ms                                                       | 361 ms: 1.26x faster                                                                |
| async_tree_io              | 843 ms                                                       | 675 ms: 1.25x faster                                                                |
| async_tree_io_tg           | 831 ms                                                       | 681 ms: 1.22x faster                                                                |
| async_tree_none            | 376 ms                                                       | 312 ms: 1.21x faster                                                                |
| async_tree_none_tg         | 346 ms                                                       | 295 ms: 1.17x faster                                                                |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 536 ms: 1.13x faster                                                                |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 534 ms: 1.09x faster                                                                |
| asyncio_websockets         | 388 ms                                                       | 384 ms: 1.01x faster                                                                |
| async_generators           | 457 ms                                                       | 462 ms: 1.01x slower                                                                |
| coroutines                 | 21.6 ms                                                      | 22.3 ms: 1.03x slower                                                               |
| Geometric mean             | (ref)                                                        | 1.14x faster                                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| pidigits       | 252 ms                                                       | 259 ms: 1.03x slower                                                                |
| float          | 81.3 ms                                                      | 113 ms: 1.39x slower                                                                |
| nbody          | 89.3 ms                                                      | 218 ms: 2.44x slower                                                                |
| Geometric mean | (ref)                                                        | 1.51x slower                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_dna      | 247 ms                                                       | 220 ms: 1.12x faster                                                                |
| regex_v8       | 26.1 ms                                                      | 23.9 ms: 1.09x faster                                                               |
| regex_effbot   | 3.67 ms                                                      | 3.53 ms: 1.04x faster                                                               |
| regex_compile  | 143 ms                                                       | 164 ms: 1.15x slower                                                                |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| xml_etree_parse      | 150 ms                                                       | 147 ms: 1.02x faster                                                                |
| json_loads           | 24.7 us                                                      | 25.3 us: 1.03x slower                                                               |
| xml_etree_iterparse  | 103 ms                                                       | 113 ms: 1.10x slower                                                                |
| tomli_loads          | 2.46 sec                                                     | 3.17 sec: 1.29x slower                                                              |
| pickle_pure_python   | 323 us                                                       | 429 us: 1.33x slower                                                                |
| xml_etree_process    | 61.2 ms                                                      | 82.4 ms: 1.35x slower                                                               |
| xml_etree_generate   | 86.5 ms                                                      | 119 ms: 1.37x slower                                                                |
| unpickle_pure_python | 217 us                                                       | 428 us: 1.97x slower                                                                |
| Geometric mean       | (ref)                                                        | 1.24x slower                                                                        |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 15.3 ms: 1.04x faster                                                               |
| python_startup_no_site | 8.96 ms                                                      | 8.83 ms: 1.01x faster                                                               |
| Geometric mean         | (ref)                                                        | 1.03x faster                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.7 ms: 1.11x faster                                                               |
| django_template | 36.4 ms                                                      | 36.7 ms: 1.01x slower                                                               |
| mako            | 10.4 ms                                                      | 20.8 ms: 2.01x slower                                                               |
| Geometric mean  | (ref)                                                        | 1.16x slower                                                                        |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.52 sec: 1.67x faster                                                              |
| deepcopy                   | 392 us                                                       | 279 us: 1.40x faster                                                                |
| deepcopy_memo              | 38.6 us                                                      | 28.1 us: 1.38x faster                                                               |
| async_tree_memoization_tg  | 466 ms                                                       | 360 ms: 1.29x faster                                                                |
| async_tree_memoization     | 453 ms                                                       | 361 ms: 1.26x faster                                                                |
| async_tree_io              | 843 ms                                                       | 675 ms: 1.25x faster                                                                |
| async_tree_io_tg           | 831 ms                                                       | 681 ms: 1.22x faster                                                                |
| async_tree_none            | 376 ms                                                       | 312 ms: 1.21x faster                                                                |
| scimark_sor                | 123 ms                                                       | 103 ms: 1.20x faster                                                                |
| deepcopy_reduce            | 3.54 us                                                      | 2.98 us: 1.19x faster                                                               |
| async_tree_none_tg         | 346 ms                                                       | 295 ms: 1.17x faster                                                                |
| generators                 | 33.6 ms                                                      | 29.1 ms: 1.15x faster                                                               |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 536 ms: 1.13x faster                                                                |
| regex_dna                  | 247 ms                                                       | 220 ms: 1.12x faster                                                                |
| genshi_text                | 26.2 ms                                                      | 23.7 ms: 1.11x faster                                                               |
| regex_v8                   | 26.1 ms                                                      | 23.9 ms: 1.09x faster                                                               |
| thrift                     | 901 us                                                       | 828 us: 1.09x faster                                                                |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 534 ms: 1.09x faster                                                                |
| dulwich_log                | 68.2 ms                                                      | 62.9 ms: 1.08x faster                                                               |
| scimark_lu                 | 98.7 ms                                                      | 92.9 ms: 1.06x faster                                                               |
| json                       | 5.69 ms                                                      | 5.36 ms: 1.06x faster                                                               |
| pathlib                    | 17.5 ms                                                      | 16.9 ms: 1.04x faster                                                               |
| regex_effbot               | 3.67 ms                                                      | 3.53 ms: 1.04x faster                                                               |
| python_startup             | 15.9 ms                                                      | 15.3 ms: 1.04x faster                                                               |
| html5lib                   | 73.5 ms                                                      | 70.8 ms: 1.04x faster                                                               |
| coverage                   | 80.0 ms                                                      | 77.8 ms: 1.03x faster                                                               |
| xml_etree_parse            | 150 ms                                                       | 147 ms: 1.02x faster                                                                |
| python_startup_no_site     | 8.96 ms                                                      | 8.83 ms: 1.01x faster                                                               |
| asyncio_websockets         | 388 ms                                                       | 384 ms: 1.01x faster                                                                |
| sympy_integrate            | 23.6 ms                                                      | 23.7 ms: 1.01x slower                                                               |
| django_template            | 36.4 ms                                                      | 36.7 ms: 1.01x slower                                                               |
| async_generators           | 457 ms                                                       | 462 ms: 1.01x slower                                                                |
| logging_simple             | 6.39 us                                                      | 6.49 us: 1.02x slower                                                               |
| sphinx                     | 1.12 sec                                                     | 1.14 sec: 1.02x slower                                                              |
| logging_format             | 6.94 us                                                      | 7.11 us: 1.02x slower                                                               |
| pidigits                   | 252 ms                                                       | 259 ms: 1.03x slower                                                                |
| json_loads                 | 24.7 us                                                      | 25.3 us: 1.03x slower                                                               |
| coroutines                 | 21.6 ms                                                      | 22.3 ms: 1.03x slower                                                               |
| chaos                      | 60.2 ms                                                      | 63.4 ms: 1.05x slower                                                               |
| sqlite_synth               | 2.91 us                                                      | 3.06 us: 1.05x slower                                                               |
| sympy_sum                  | 155 ms                                                       | 164 ms: 1.06x slower                                                                |
| create_gc_cycles           | 2.68 ms                                                      | 2.88 ms: 1.07x slower                                                               |
| sympy_str                  | 298 ms                                                       | 321 ms: 1.08x slower                                                                |
| k_core                     | 2.17 sec                                                     | 2.35 sec: 1.09x slower                                                              |
| richards_super             | 59.6 ms                                                      | 64.7 ms: 1.09x slower                                                               |
| richards                   | 52.9 ms                                                      | 57.5 ms: 1.09x slower                                                               |
| xml_etree_iterparse        | 103 ms                                                       | 113 ms: 1.10x slower                                                                |
| sympy_expand               | 509 ms                                                       | 562 ms: 1.10x slower                                                                |
| telco                      | 8.79 ms                                                      | 9.73 ms: 1.11x slower                                                               |
| docutils                   | 2.83 sec                                                     | 3.17 sec: 1.12x slower                                                              |
| 2to3                       | 293 ms                                                       | 333 ms: 1.14x slower                                                                |
| shortest_path              | 460 ms                                                       | 525 ms: 1.14x slower                                                                |
| regex_compile              | 143 ms                                                       | 164 ms: 1.15x slower                                                                |
| nqueens                    | 90.7 ms                                                      | 107 ms: 1.19x slower                                                                |
| connected_components       | 432 ms                                                       | 518 ms: 1.20x slower                                                                |
| many_optionals             | 930 us                                                       | 1.12 ms: 1.20x slower                                                               |
| raytrace                   | 273 ms                                                       | 343 ms: 1.26x slower                                                                |
| pycparser                  | 1.24 sec                                                     | 1.56 sec: 1.26x slower                                                              |
| typing_runtime_protocols   | 169 us                                                       | 214 us: 1.26x slower                                                                |
| tomli_loads                | 2.46 sec                                                     | 3.17 sec: 1.29x slower                                                              |
| meteor_contest             | 130 ms                                                       | 169 ms: 1.30x slower                                                                |
| pickle_pure_python         | 323 us                                                       | 429 us: 1.33x slower                                                                |
| pyflate                    | 503 ms                                                       | 671 ms: 1.33x slower                                                                |
| xml_etree_process          | 61.2 ms                                                      | 82.4 ms: 1.35x slower                                                               |
| xml_etree_generate         | 86.5 ms                                                      | 119 ms: 1.37x slower                                                                |
| float                      | 81.3 ms                                                      | 113 ms: 1.39x slower                                                                |
| bpe_tokeniser              | 5.09 sec                                                     | 7.06 sec: 1.39x slower                                                              |
| gc_traversal               | 4.74 ms                                                      | 6.72 ms: 1.42x slower                                                               |
| scimark_monte_carlo        | 66.1 ms                                                      | 95.0 ms: 1.44x slower                                                               |
| subparsers                 | 17.5 ms                                                      | 26.0 ms: 1.49x slower                                                               |
| go                         | 162 ms                                                       | 246 ms: 1.51x slower                                                                |
| pprint_pformat             | 1.72 sec                                                     | 2.69 sec: 1.56x slower                                                              |
| scimark_fft                | 328 ms                                                       | 513 ms: 1.57x slower                                                                |
| pprint_safe_repr           | 843 ms                                                       | 1.33 sec: 1.57x slower                                                              |
| crypto_pyaes               | 73.3 ms                                                      | 118 ms: 1.60x slower                                                                |
| hexiom                     | 6.55 ms                                                      | 11.7 ms: 1.79x slower                                                               |
| deltablue                  | 3.42 ms                                                      | 6.35 ms: 1.86x slower                                                               |
| fannkuch                   | 363 ms                                                       | 690 ms: 1.90x slower                                                                |
| comprehensions             | 17.0 us                                                      | 32.4 us: 1.90x slower                                                               |
| spectral_norm              | 97.0 ms                                                      | 189 ms: 1.95x slower                                                                |
| unpickle_pure_python       | 217 us                                                       | 428 us: 1.97x slower                                                                |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 9.49 ms: 1.99x slower                                                               |
| mako                       | 10.4 ms                                                      | 20.8 ms: 2.01x slower                                                               |
| nbody                      | 89.3 ms                                                      | 218 ms: 2.44x slower                                                                |
| logging_silent             | 97.9 ns                                                      | 504 ns: 5.15x slower                                                                |
| Geometric mean             | (ref)                                                        | 1.15x slower                                                                        |

Benchmark hidden because not significant (4): pylint, djangocms, genshi_xml, json_dumps
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250619-3.15.0a0-2850d72-PYTHON_UOPS/bm-20250619-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.117x slower

# HPT report

- Reliability score: 99.93% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.10x