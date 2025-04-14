# Results vs. 3.13.0

- fork: python
- ref: 52b5eb95b770fa00ebbd
- machine: linux-x86_64
- commit hash: 52b5eb9
- commit date: 2025-03-26
- overall geometric mean: 1.042x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-pythonperf2-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 289 ms: 1.01x faster                                                         |
| docutils       | 2.83 sec                                                     | 2.98 sec: 1.05x slower                                                       |
| html5lib       | 73.5 ms                                                      | 69.9 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                 |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-pythonperf2-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 330 ms: 1.41x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 341 ms: 1.33x faster                                                         |
| async_tree_io              | 843 ms                                                       | 639 ms: 1.32x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 646 ms: 1.29x faster                                                         |
| async_tree_none            | 376 ms                                                       | 294 ms: 1.28x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 277 ms: 1.25x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 505 ms: 1.15x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 524 ms: 1.15x faster                                                         |
| async_generators           | 457 ms                                                       | 443 ms: 1.03x faster                                                         |
| asyncio_websockets         | 388 ms                                                       | 384 ms: 1.01x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 21.4 ms: 1.01x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.20x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-pythonperf2-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 64.6 ms: 1.26x faster                                                        |
| pidigits       | 252 ms                                                       | 253 ms: 1.00x slower                                                         |
| nbody          | 89.3 ms                                                      | 93.0 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-pythonperf2-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.12 ms: 1.17x faster                                                        |
| regex_v8       | 26.1 ms                                                      | 23.2 ms: 1.13x faster                                                        |
| regex_dna      | 247 ms                                                       | 233 ms: 1.06x faster                                                         |
| regex_compile  | 143 ms                                                       | 137 ms: 1.04x faster                                                         |
| Geometric mean | (ref)                                                        | 1.10x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-pythonperf2-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|---------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads         | 2.46 sec                                                     | 2.07 sec: 1.19x faster                                                       |
| xml_etree_parse     | 150 ms                                                       | 137 ms: 1.10x faster                                                         |
| xml_etree_iterparse | 103 ms                                                       | 96.0 ms: 1.07x faster                                                        |
| xml_etree_process   | 61.2 ms                                                      | 57.2 ms: 1.07x faster                                                        |
| xml_etree_generate  | 86.5 ms                                                      | 81.4 ms: 1.06x faster                                                        |
| json_dumps          | 11.1 ms                                                      | 11.6 ms: 1.04x slower                                                        |
| pickle_pure_python  | 323 us                                                       | 344 us: 1.07x slower                                                         |
| json_loads          | 24.7 us                                                      | 26.7 us: 1.08x slower                                                        |
| Geometric mean      | (ref)                                                        | 1.03x faster                                                                 |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-pythonperf2-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 16.4 ms: 1.03x slower                                                        |
| python_startup_no_site | 8.96 ms                                                      | 10.5 ms: 1.17x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-pythonperf2-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 24.8 ms: 1.06x faster                                                        |
| genshi_xml      | 57.1 ms                                                      | 55.9 ms: 1.02x faster                                                        |
| django_template | 36.4 ms                                                      | 37.3 ms: 1.02x slower                                                        |
| mako            | 10.4 ms                                                      | 10.6 ms: 1.03x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-pythonperf2-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 330 ms: 1.41x faster                                                         |
| deepcopy_memo              | 38.6 us                                                      | 28.5 us: 1.36x faster                                                        |
| deepcopy                   | 392 us                                                       | 289 us: 1.35x faster                                                         |
| richards                   | 52.9 ms                                                      | 39.3 ms: 1.35x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 341 ms: 1.33x faster                                                         |
| async_tree_io              | 843 ms                                                       | 639 ms: 1.32x faster                                                         |
| richards_super             | 59.6 ms                                                      | 45.2 ms: 1.32x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 646 ms: 1.29x faster                                                         |
| async_tree_none            | 376 ms                                                       | 294 ms: 1.28x faster                                                         |
| float                      | 81.3 ms                                                      | 64.6 ms: 1.26x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 277 ms: 1.25x faster                                                         |
| deepcopy_reduce            | 3.54 us                                                      | 2.97 us: 1.19x faster                                                        |
| tomli_loads                | 2.46 sec                                                     | 2.07 sec: 1.19x faster                                                       |
| regex_effbot               | 3.67 ms                                                      | 3.12 ms: 1.17x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 505 ms: 1.15x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 524 ms: 1.15x faster                                                         |
| generators                 | 33.6 ms                                                      | 29.2 ms: 1.15x faster                                                        |
| scimark_sor                | 123 ms                                                       | 108 ms: 1.14x faster                                                         |
| regex_v8                   | 26.1 ms                                                      | 23.2 ms: 1.13x faster                                                        |
| pyflate                    | 503 ms                                                       | 451 ms: 1.11x faster                                                         |
| go                         | 162 ms                                                       | 146 ms: 1.11x faster                                                         |
| deltablue                  | 3.42 ms                                                      | 3.09 ms: 1.11x faster                                                        |
| telco                      | 8.79 ms                                                      | 7.94 ms: 1.11x faster                                                        |
| xml_etree_parse            | 150 ms                                                       | 137 ms: 1.10x faster                                                         |
| dulwich_log                | 68.2 ms                                                      | 62.1 ms: 1.10x faster                                                        |
| spectral_norm              | 97.0 ms                                                      | 89.5 ms: 1.08x faster                                                        |
| pylint                     | 347 ms                                                       | 323 ms: 1.07x faster                                                         |
| xml_etree_iterparse        | 103 ms                                                       | 96.0 ms: 1.07x faster                                                        |
| xml_etree_process          | 61.2 ms                                                      | 57.2 ms: 1.07x faster                                                        |
| xml_etree_generate         | 86.5 ms                                                      | 81.4 ms: 1.06x faster                                                        |
| genshi_text                | 26.2 ms                                                      | 24.8 ms: 1.06x faster                                                        |
| regex_dna                  | 247 ms                                                       | 233 ms: 1.06x faster                                                         |
| connected_components       | 432 ms                                                       | 409 ms: 1.06x faster                                                         |
| bpe_tokeniser              | 5.09 sec                                                     | 4.83 sec: 1.05x faster                                                       |
| json                       | 5.69 ms                                                      | 5.40 ms: 1.05x faster                                                        |
| html5lib                   | 73.5 ms                                                      | 69.9 ms: 1.05x faster                                                        |
| scimark_fft                | 328 ms                                                       | 313 ms: 1.05x faster                                                         |
| shortest_path              | 460 ms                                                       | 439 ms: 1.05x faster                                                         |
| logging_silent             | 97.9 ns                                                      | 93.5 ns: 1.05x faster                                                        |
| regex_compile              | 143 ms                                                       | 137 ms: 1.04x faster                                                         |
| k_core                     | 2.17 sec                                                     | 2.09 sec: 1.04x faster                                                       |
| sqlite_synth               | 2.91 us                                                      | 2.80 us: 1.04x faster                                                        |
| pprint_pformat             | 1.72 sec                                                     | 1.67 sec: 1.03x faster                                                       |
| async_generators           | 457 ms                                                       | 443 ms: 1.03x faster                                                         |
| pprint_safe_repr           | 843 ms                                                       | 821 ms: 1.03x faster                                                         |
| genshi_xml                 | 57.1 ms                                                      | 55.9 ms: 1.02x faster                                                        |
| thrift                     | 901 us                                                       | 886 us: 1.02x faster                                                         |
| 2to3                       | 293 ms                                                       | 289 ms: 1.01x faster                                                         |
| sympy_integrate            | 23.6 ms                                                      | 23.3 ms: 1.01x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 384 ms: 1.01x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 21.4 ms: 1.01x faster                                                        |
| sqlalchemy_declarative     | 148 ms                                                       | 147 ms: 1.01x faster                                                         |
| mdp                        | 2.54 sec                                                     | 2.52 sec: 1.01x faster                                                       |
| pathlib                    | 17.5 ms                                                      | 17.4 ms: 1.01x faster                                                        |
| sympy_str                  | 298 ms                                                       | 296 ms: 1.01x faster                                                         |
| pidigits                   | 252 ms                                                       | 253 ms: 1.00x slower                                                         |
| logging_simple             | 6.39 us                                                      | 6.42 us: 1.00x slower                                                        |
| scimark_lu                 | 98.7 ms                                                      | 99.3 ms: 1.01x slower                                                        |
| sympy_expand               | 509 ms                                                       | 515 ms: 1.01x slower                                                         |
| meteor_contest             | 130 ms                                                       | 131 ms: 1.01x slower                                                         |
| logging_format             | 6.94 us                                                      | 7.07 us: 1.02x slower                                                        |
| pycparser                  | 1.24 sec                                                     | 1.27 sec: 1.02x slower                                                       |
| django_template            | 36.4 ms                                                      | 37.3 ms: 1.02x slower                                                        |
| coverage                   | 80.0 ms                                                      | 82.1 ms: 1.03x slower                                                        |
| mako                       | 10.4 ms                                                      | 10.6 ms: 1.03x slower                                                        |
| python_startup             | 15.9 ms                                                      | 16.4 ms: 1.03x slower                                                        |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.93 ms: 1.03x slower                                                        |
| nqueens                    | 90.7 ms                                                      | 94.1 ms: 1.04x slower                                                        |
| hexiom                     | 6.55 ms                                                      | 6.80 ms: 1.04x slower                                                        |
| bench_thread_pool          | 942 us                                                       | 980 us: 1.04x slower                                                         |
| nbody                      | 89.3 ms                                                      | 93.0 ms: 1.04x slower                                                        |
| scimark_monte_carlo        | 66.1 ms                                                      | 68.8 ms: 1.04x slower                                                        |
| json_dumps                 | 11.1 ms                                                      | 11.6 ms: 1.04x slower                                                        |
| typing_runtime_protocols   | 169 us                                                       | 177 us: 1.04x slower                                                         |
| docutils                   | 2.83 sec                                                     | 2.98 sec: 1.05x slower                                                       |
| pickle_pure_python         | 323 us                                                       | 344 us: 1.07x slower                                                         |
| json_loads                 | 24.7 us                                                      | 26.7 us: 1.08x slower                                                        |
| raytrace                   | 273 ms                                                       | 297 ms: 1.09x slower                                                         |
| chaos                      | 60.2 ms                                                      | 66.5 ms: 1.10x slower                                                        |
| fannkuch                   | 363 ms                                                       | 408 ms: 1.12x slower                                                         |
| crypto_pyaes               | 73.3 ms                                                      | 83.6 ms: 1.14x slower                                                        |
| many_optionals             | 930 us                                                       | 1.06 ms: 1.14x slower                                                        |
| python_startup_no_site     | 8.96 ms                                                      | 10.5 ms: 1.17x slower                                                        |
| comprehensions             | 17.0 us                                                      | 20.4 us: 1.20x slower                                                        |
| gc_traversal               | 4.74 ms                                                      | 6.14 ms: 1.30x slower                                                        |
| subparsers                 | 17.5 ms                                                      | 23.3 ms: 1.33x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 1.28 sec: 250.67x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                                 |

Benchmark hidden because not significant (5): sphinx, sympy_sum, sqlalchemy_imperative, unpickle_pure_python, create_gc_cycles
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250326-3.14.0a6+-52b5eb9-JIT/bm-20250326-pythonperf2-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.042x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.05x