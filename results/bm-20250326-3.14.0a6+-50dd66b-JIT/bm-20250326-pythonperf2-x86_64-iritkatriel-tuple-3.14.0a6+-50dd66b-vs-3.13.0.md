# Results vs. 3.13.0

- fork: iritkatriel
- ref: tuple
- machine: linux-x86_64
- commit hash: 50dd66b
- commit date: 2025-03-26
- overall geometric mean: 1.040x faster
- HPT reliability: 99.90%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-pythonperf2-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 293 ms: 1.00x slower                                               |
| docutils       | 2.83 sec                                                     | 2.98 sec: 1.06x slower                                             |
| html5lib       | 73.5 ms                                                      | 69.5 ms: 1.06x faster                                              |
| Geometric mean | (ref)                                                        | 1.00x slower                                                       |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-pythonperf2-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 328 ms: 1.42x faster                                               |
| async_tree_memoization     | 453 ms                                                       | 339 ms: 1.34x faster                                               |
| async_tree_io              | 843 ms                                                       | 640 ms: 1.32x faster                                               |
| async_tree_io_tg           | 831 ms                                                       | 646 ms: 1.29x faster                                               |
| async_tree_none            | 376 ms                                                       | 295 ms: 1.28x faster                                               |
| async_tree_none_tg         | 346 ms                                                       | 276 ms: 1.25x faster                                               |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 518 ms: 1.17x faster                                               |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 501 ms: 1.16x faster                                               |
| async_generators           | 457 ms                                                       | 443 ms: 1.03x faster                                               |
| asyncio_websockets         | 388 ms                                                       | 383 ms: 1.01x faster                                               |
| Geometric mean             | (ref)                                                        | 1.20x faster                                                       |

Benchmark hidden because not significant (1): coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-pythonperf2-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 63.8 ms: 1.27x faster                                              |
| pidigits       | 252 ms                                                       | 253 ms: 1.00x slower                                               |
| nbody          | 89.3 ms                                                      | 94.7 ms: 1.06x slower                                              |
| Geometric mean | (ref)                                                        | 1.06x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-pythonperf2-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.11 ms: 1.18x faster                                              |
| regex_v8       | 26.1 ms                                                      | 23.9 ms: 1.09x faster                                              |
| regex_compile  | 143 ms                                                       | 138 ms: 1.03x faster                                               |
| regex_dna      | 247 ms                                                       | 239 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                        | 1.08x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-pythonperf2-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|---------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads         | 2.46 sec                                                     | 2.09 sec: 1.18x faster                                             |
| xml_etree_parse     | 150 ms                                                       | 136 ms: 1.11x faster                                               |
| xml_etree_iterparse | 103 ms                                                       | 95.7 ms: 1.07x faster                                              |
| xml_etree_process   | 61.2 ms                                                      | 57.9 ms: 1.06x faster                                              |
| xml_etree_generate  | 86.5 ms                                                      | 82.4 ms: 1.05x faster                                              |
| json_dumps          | 11.1 ms                                                      | 11.5 ms: 1.03x slower                                              |
| json_loads          | 24.7 us                                                      | 26.0 us: 1.06x slower                                              |
| pickle_pure_python  | 323 us                                                       | 345 us: 1.07x slower                                               |
| Geometric mean      | (ref)                                                        | 1.03x faster                                                       |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-pythonperf2-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 16.4 ms: 1.03x slower                                              |
| python_startup_no_site | 8.96 ms                                                      | 10.5 ms: 1.17x slower                                              |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-pythonperf2-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 24.6 ms: 1.07x faster                                              |
| genshi_xml      | 57.1 ms                                                      | 58.3 ms: 1.02x slower                                              |
| django_template | 36.4 ms                                                      | 37.2 ms: 1.02x slower                                              |
| mako            | 10.4 ms                                                      | 10.8 ms: 1.04x slower                                              |
| Geometric mean  | (ref)                                                        | 1.00x slower                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-pythonperf2-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 328 ms: 1.42x faster                                               |
| deepcopy_memo              | 38.6 us                                                      | 28.5 us: 1.36x faster                                              |
| async_tree_memoization     | 453 ms                                                       | 339 ms: 1.34x faster                                               |
| async_tree_io              | 843 ms                                                       | 640 ms: 1.32x faster                                               |
| deepcopy                   | 392 us                                                       | 299 us: 1.31x faster                                               |
| richards                   | 52.9 ms                                                      | 40.7 ms: 1.30x faster                                              |
| async_tree_io_tg           | 831 ms                                                       | 646 ms: 1.29x faster                                               |
| async_tree_none            | 376 ms                                                       | 295 ms: 1.28x faster                                               |
| float                      | 81.3 ms                                                      | 63.8 ms: 1.27x faster                                              |
| richards_super             | 59.6 ms                                                      | 47.3 ms: 1.26x faster                                              |
| async_tree_none_tg         | 346 ms                                                       | 276 ms: 1.25x faster                                               |
| deepcopy_reduce            | 3.54 us                                                      | 2.98 us: 1.19x faster                                              |
| tomli_loads                | 2.46 sec                                                     | 2.09 sec: 1.18x faster                                             |
| regex_effbot               | 3.67 ms                                                      | 3.11 ms: 1.18x faster                                              |
| generators                 | 33.6 ms                                                      | 28.8 ms: 1.17x faster                                              |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 518 ms: 1.17x faster                                               |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 501 ms: 1.16x faster                                               |
| pyflate                    | 503 ms                                                       | 435 ms: 1.16x faster                                               |
| go                         | 162 ms                                                       | 144 ms: 1.13x faster                                               |
| scimark_sor                | 123 ms                                                       | 109 ms: 1.13x faster                                               |
| deltablue                  | 3.42 ms                                                      | 3.06 ms: 1.12x faster                                              |
| telco                      | 8.79 ms                                                      | 7.89 ms: 1.11x faster                                              |
| xml_etree_parse            | 150 ms                                                       | 136 ms: 1.11x faster                                               |
| regex_v8                   | 26.1 ms                                                      | 23.9 ms: 1.09x faster                                              |
| spectral_norm              | 97.0 ms                                                      | 88.7 ms: 1.09x faster                                              |
| dulwich_log                | 68.2 ms                                                      | 62.9 ms: 1.08x faster                                              |
| xml_etree_iterparse        | 103 ms                                                       | 95.7 ms: 1.07x faster                                              |
| json                       | 5.69 ms                                                      | 5.33 ms: 1.07x faster                                              |
| genshi_text                | 26.2 ms                                                      | 24.6 ms: 1.07x faster                                              |
| pylint                     | 347 ms                                                       | 327 ms: 1.06x faster                                               |
| bpe_tokeniser              | 5.09 sec                                                     | 4.81 sec: 1.06x faster                                             |
| scimark_fft                | 328 ms                                                       | 310 ms: 1.06x faster                                               |
| html5lib                   | 73.5 ms                                                      | 69.5 ms: 1.06x faster                                              |
| xml_etree_process          | 61.2 ms                                                      | 57.9 ms: 1.06x faster                                              |
| connected_components       | 432 ms                                                       | 411 ms: 1.05x faster                                               |
| pprint_pformat             | 1.72 sec                                                     | 1.63 sec: 1.05x faster                                             |
| xml_etree_generate         | 86.5 ms                                                      | 82.4 ms: 1.05x faster                                              |
| logging_silent             | 97.9 ns                                                      | 93.8 ns: 1.04x faster                                              |
| pprint_safe_repr           | 843 ms                                                       | 809 ms: 1.04x faster                                               |
| k_core                     | 2.17 sec                                                     | 2.09 sec: 1.04x faster                                             |
| sqlite_synth               | 2.91 us                                                      | 2.80 us: 1.04x faster                                              |
| regex_compile              | 143 ms                                                       | 138 ms: 1.03x faster                                               |
| regex_dna                  | 247 ms                                                       | 239 ms: 1.03x faster                                               |
| thrift                     | 901 us                                                       | 872 us: 1.03x faster                                               |
| shortest_path              | 460 ms                                                       | 445 ms: 1.03x faster                                               |
| async_generators           | 457 ms                                                       | 443 ms: 1.03x faster                                               |
| coverage                   | 80.0 ms                                                      | 78.0 ms: 1.03x faster                                              |
| asyncio_websockets         | 388 ms                                                       | 383 ms: 1.01x faster                                               |
| mdp                        | 2.54 sec                                                     | 2.51 sec: 1.01x faster                                             |
| pathlib                    | 17.5 ms                                                      | 17.4 ms: 1.01x faster                                              |
| sympy_integrate            | 23.6 ms                                                      | 23.4 ms: 1.00x faster                                              |
| sqlalchemy_imperative      | 18.3 ms                                                      | 18.2 ms: 1.00x faster                                              |
| 2to3                       | 293 ms                                                       | 293 ms: 1.00x slower                                               |
| pidigits                   | 252 ms                                                       | 253 ms: 1.00x slower                                               |
| sympy_str                  | 298 ms                                                       | 299 ms: 1.00x slower                                               |
| sympy_sum                  | 155 ms                                                       | 155 ms: 1.00x slower                                               |
| scimark_lu                 | 98.7 ms                                                      | 99.5 ms: 1.01x slower                                              |
| meteor_contest             | 130 ms                                                       | 131 ms: 1.01x slower                                               |
| sympy_expand               | 509 ms                                                       | 519 ms: 1.02x slower                                               |
| genshi_xml                 | 57.1 ms                                                      | 58.3 ms: 1.02x slower                                              |
| django_template            | 36.4 ms                                                      | 37.2 ms: 1.02x slower                                              |
| pycparser                  | 1.24 sec                                                     | 1.27 sec: 1.02x slower                                             |
| python_startup             | 15.9 ms                                                      | 16.4 ms: 1.03x slower                                              |
| json_dumps                 | 11.1 ms                                                      | 11.5 ms: 1.03x slower                                              |
| logging_simple             | 6.39 us                                                      | 6.60 us: 1.03x slower                                              |
| nqueens                    | 90.7 ms                                                      | 93.9 ms: 1.04x slower                                              |
| hexiom                     | 6.55 ms                                                      | 6.81 ms: 1.04x slower                                              |
| mako                       | 10.4 ms                                                      | 10.8 ms: 1.04x slower                                              |
| bench_thread_pool          | 942 us                                                       | 984 us: 1.05x slower                                               |
| logging_format             | 6.94 us                                                      | 7.28 us: 1.05x slower                                              |
| json_loads                 | 24.7 us                                                      | 26.0 us: 1.06x slower                                              |
| docutils                   | 2.83 sec                                                     | 2.98 sec: 1.06x slower                                             |
| nbody                      | 89.3 ms                                                      | 94.7 ms: 1.06x slower                                              |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 5.08 ms: 1.06x slower                                              |
| typing_runtime_protocols   | 169 us                                                       | 180 us: 1.07x slower                                               |
| pickle_pure_python         | 323 us                                                       | 345 us: 1.07x slower                                               |
| raytrace                   | 273 ms                                                       | 292 ms: 1.07x slower                                               |
| chaos                      | 60.2 ms                                                      | 64.4 ms: 1.07x slower                                              |
| scimark_monte_carlo        | 66.1 ms                                                      | 70.9 ms: 1.07x slower                                              |
| fannkuch                   | 363 ms                                                       | 395 ms: 1.09x slower                                               |
| crypto_pyaes               | 73.3 ms                                                      | 82.3 ms: 1.12x slower                                              |
| many_optionals             | 930 us                                                       | 1.06 ms: 1.14x slower                                              |
| python_startup_no_site     | 8.96 ms                                                      | 10.5 ms: 1.17x slower                                              |
| comprehensions             | 17.0 us                                                      | 20.1 us: 1.18x slower                                              |
| gc_traversal               | 4.74 ms                                                      | 6.14 ms: 1.30x slower                                              |
| subparsers                 | 17.5 ms                                                      | 23.8 ms: 1.36x slower                                              |
| bench_mp_pool              | 5.12 ms                                                      | 713 ms: 139.11x slower                                             |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                       |

Benchmark hidden because not significant (5): unpickle_pure_python, coroutines, sphinx, sqlalchemy_declarative, create_gc_cycles
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250326-3.14.0a6+-50dd66b-JIT/bm-20250326-pythonperf2-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.040x faster

# HPT report

- Reliability score: 99.90% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x