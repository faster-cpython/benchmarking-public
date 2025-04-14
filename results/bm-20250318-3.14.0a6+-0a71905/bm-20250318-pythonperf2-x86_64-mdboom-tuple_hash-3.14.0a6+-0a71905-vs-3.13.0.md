# Results vs. 3.13.0

- fork: mdboom
- ref: tuple_hash
- machine: linux-x86_64
- commit hash: 0a71905
- commit date: 2025-03-18
- overall geometric mean: 1.031x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-pythonperf2-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 286 ms: 1.03x faster                                               |
| docutils       | 2.83 sec                                                     | 2.91 sec: 1.03x slower                                             |
| html5lib       | 73.5 ms                                                      | 70.2 ms: 1.05x faster                                              |
| Geometric mean | (ref)                                                        | 1.01x faster                                                       |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-pythonperf2-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 342 ms: 1.36x faster                                               |
| async_tree_io              | 843 ms                                                       | 650 ms: 1.30x faster                                               |
| async_tree_memoization     | 453 ms                                                       | 350 ms: 1.29x faster                                               |
| async_tree_none            | 376 ms                                                       | 291 ms: 1.29x faster                                               |
| async_tree_io_tg           | 831 ms                                                       | 657 ms: 1.26x faster                                               |
| async_tree_none_tg         | 346 ms                                                       | 276 ms: 1.25x faster                                               |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 522 ms: 1.16x faster                                               |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 508 ms: 1.14x faster                                               |
| async_generators           | 457 ms                                                       | 421 ms: 1.09x faster                                               |
| coroutines                 | 21.6 ms                                                      | 20.9 ms: 1.03x faster                                              |
| Geometric mean             | (ref)                                                        | 1.19x faster                                                       |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-pythonperf2-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 72.5 ms: 1.12x faster                                              |
| pidigits       | 252 ms                                                       | 255 ms: 1.01x slower                                               |
| nbody          | 89.3 ms                                                      | 101 ms: 1.14x slower                                               |
| Geometric mean | (ref)                                                        | 1.01x slower                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-pythonperf2-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.17 ms: 1.16x faster                                              |
| regex_v8       | 26.1 ms                                                      | 23.9 ms: 1.09x faster                                              |
| regex_compile  | 143 ms                                                       | 138 ms: 1.03x faster                                               |
| regex_dna      | 247 ms                                                       | 246 ms: 1.00x faster                                               |
| Geometric mean | (ref)                                                        | 1.07x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-pythonperf2-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.14 sec: 1.15x faster                                             |
| xml_etree_parse      | 150 ms                                                       | 136 ms: 1.10x faster                                               |
| xml_etree_iterparse  | 103 ms                                                       | 98.9 ms: 1.04x faster                                              |
| xml_etree_process    | 61.2 ms                                                      | 60.5 ms: 1.01x faster                                              |
| xml_etree_generate   | 86.5 ms                                                      | 85.7 ms: 1.01x faster                                              |
| unpickle_pure_python | 217 us                                                       | 225 us: 1.03x slower                                               |
| json_dumps           | 11.1 ms                                                      | 11.5 ms: 1.03x slower                                              |
| pickle_pure_python   | 323 us                                                       | 338 us: 1.05x slower                                               |
| json_loads           | 24.7 us                                                      | 26.1 us: 1.06x slower                                              |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-pythonperf2-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 16.4 ms: 1.03x slower                                              |
| python_startup_no_site | 8.96 ms                                                      | 10.5 ms: 1.17x slower                                              |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-pythonperf2-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text    | 26.2 ms                                                      | 23.6 ms: 1.11x faster                                              |
| genshi_xml     | 57.1 ms                                                      | 55.8 ms: 1.02x faster                                              |
| mako           | 10.4 ms                                                      | 11.1 ms: 1.07x slower                                              |
| Geometric mean | (ref)                                                        | 1.01x faster                                                       |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-pythonperf2-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 342 ms: 1.36x faster                                               |
| deepcopy                   | 392 us                                                       | 296 us: 1.33x faster                                               |
| deepcopy_memo              | 38.6 us                                                      | 29.5 us: 1.31x faster                                              |
| async_tree_io              | 843 ms                                                       | 650 ms: 1.30x faster                                               |
| async_tree_memoization     | 453 ms                                                       | 350 ms: 1.29x faster                                               |
| async_tree_none            | 376 ms                                                       | 291 ms: 1.29x faster                                               |
| async_tree_io_tg           | 831 ms                                                       | 657 ms: 1.26x faster                                               |
| async_tree_none_tg         | 346 ms                                                       | 276 ms: 1.25x faster                                               |
| go                         | 162 ms                                                       | 134 ms: 1.21x faster                                               |
| regex_effbot               | 3.67 ms                                                      | 3.17 ms: 1.16x faster                                              |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 522 ms: 1.16x faster                                               |
| deepcopy_reduce            | 3.54 us                                                      | 3.08 us: 1.15x faster                                              |
| tomli_loads                | 2.46 sec                                                     | 2.14 sec: 1.15x faster                                             |
| generators                 | 33.6 ms                                                      | 29.3 ms: 1.15x faster                                              |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 508 ms: 1.14x faster                                               |
| float                      | 81.3 ms                                                      | 72.5 ms: 1.12x faster                                              |
| scimark_sor                | 123 ms                                                       | 111 ms: 1.11x faster                                               |
| genshi_text                | 26.2 ms                                                      | 23.6 ms: 1.11x faster                                              |
| xml_etree_parse            | 150 ms                                                       | 136 ms: 1.10x faster                                               |
| telco                      | 8.79 ms                                                      | 8.02 ms: 1.10x faster                                              |
| pylint                     | 347 ms                                                       | 317 ms: 1.09x faster                                               |
| regex_v8                   | 26.1 ms                                                      | 23.9 ms: 1.09x faster                                              |
| dulwich_log                | 68.2 ms                                                      | 62.8 ms: 1.09x faster                                              |
| async_generators           | 457 ms                                                       | 421 ms: 1.09x faster                                               |
| pyflate                    | 503 ms                                                       | 464 ms: 1.08x faster                                               |
| spectral_norm              | 97.0 ms                                                      | 90.2 ms: 1.08x faster                                              |
| richards                   | 52.9 ms                                                      | 49.5 ms: 1.07x faster                                              |
| richards_super             | 59.6 ms                                                      | 55.8 ms: 1.07x faster                                              |
| bpe_tokeniser              | 5.09 sec                                                     | 4.84 sec: 1.05x faster                                             |
| json                       | 5.69 ms                                                      | 5.42 ms: 1.05x faster                                              |
| html5lib                   | 73.5 ms                                                      | 70.2 ms: 1.05x faster                                              |
| scimark_fft                | 328 ms                                                       | 314 ms: 1.05x faster                                               |
| xml_etree_iterparse        | 103 ms                                                       | 98.9 ms: 1.04x faster                                              |
| regex_compile              | 143 ms                                                       | 138 ms: 1.03x faster                                               |
| coroutines                 | 21.6 ms                                                      | 20.9 ms: 1.03x faster                                              |
| thrift                     | 901 us                                                       | 875 us: 1.03x faster                                               |
| logging_silent             | 97.9 ns                                                      | 95.1 ns: 1.03x faster                                              |
| sqlite_synth               | 2.91 us                                                      | 2.83 us: 1.03x faster                                              |
| 2to3                       | 293 ms                                                       | 286 ms: 1.03x faster                                               |
| meteor_contest             | 130 ms                                                       | 126 ms: 1.02x faster                                               |
| genshi_xml                 | 57.1 ms                                                      | 55.8 ms: 1.02x faster                                              |
| pathlib                    | 17.5 ms                                                      | 17.2 ms: 1.02x faster                                              |
| pprint_pformat             | 1.72 sec                                                     | 1.69 sec: 1.02x faster                                             |
| deltablue                  | 3.42 ms                                                      | 3.36 ms: 1.02x faster                                              |
| sqlalchemy_declarative     | 148 ms                                                       | 146 ms: 1.01x faster                                               |
| k_core                     | 2.17 sec                                                     | 2.14 sec: 1.01x faster                                             |
| mdp                        | 2.54 sec                                                     | 2.51 sec: 1.01x faster                                             |
| sqlalchemy_imperative      | 18.3 ms                                                      | 18.0 ms: 1.01x faster                                              |
| xml_etree_process          | 61.2 ms                                                      | 60.5 ms: 1.01x faster                                              |
| xml_etree_generate         | 86.5 ms                                                      | 85.7 ms: 1.01x faster                                              |
| pprint_safe_repr           | 843 ms                                                       | 835 ms: 1.01x faster                                               |
| sympy_expand               | 509 ms                                                       | 505 ms: 1.01x faster                                               |
| sympy_integrate            | 23.6 ms                                                      | 23.4 ms: 1.01x faster                                              |
| hexiom                     | 6.55 ms                                                      | 6.51 ms: 1.01x faster                                              |
| connected_components       | 432 ms                                                       | 430 ms: 1.00x faster                                               |
| regex_dna                  | 247 ms                                                       | 246 ms: 1.00x faster                                               |
| shortest_path              | 460 ms                                                       | 458 ms: 1.00x faster                                               |
| coverage                   | 80.0 ms                                                      | 80.6 ms: 1.01x slower                                              |
| typing_runtime_protocols   | 169 us                                                       | 171 us: 1.01x slower                                               |
| pidigits                   | 252 ms                                                       | 255 ms: 1.01x slower                                               |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.85 ms: 1.02x slower                                              |
| logging_simple             | 6.39 us                                                      | 6.49 us: 1.02x slower                                              |
| docutils                   | 2.83 sec                                                     | 2.91 sec: 1.03x slower                                             |
| scimark_lu                 | 98.7 ms                                                      | 101 ms: 1.03x slower                                               |
| python_startup             | 15.9 ms                                                      | 16.4 ms: 1.03x slower                                              |
| comprehensions             | 17.0 us                                                      | 17.6 us: 1.03x slower                                              |
| unpickle_pure_python       | 217 us                                                       | 225 us: 1.03x slower                                               |
| json_dumps                 | 11.1 ms                                                      | 11.5 ms: 1.03x slower                                              |
| pycparser                  | 1.24 sec                                                     | 1.29 sec: 1.03x slower                                             |
| logging_format             | 6.94 us                                                      | 7.21 us: 1.04x slower                                              |
| create_gc_cycles           | 2.68 ms                                                      | 2.81 ms: 1.05x slower                                              |
| pickle_pure_python         | 323 us                                                       | 338 us: 1.05x slower                                               |
| json_loads                 | 24.7 us                                                      | 26.1 us: 1.06x slower                                              |
| nqueens                    | 90.7 ms                                                      | 96.1 ms: 1.06x slower                                              |
| fannkuch                   | 363 ms                                                       | 388 ms: 1.07x slower                                               |
| mako                       | 10.4 ms                                                      | 11.1 ms: 1.07x slower                                              |
| chaos                      | 60.2 ms                                                      | 65.2 ms: 1.08x slower                                              |
| raytrace                   | 273 ms                                                       | 298 ms: 1.09x slower                                               |
| many_optionals             | 930 us                                                       | 1.04 ms: 1.11x slower                                              |
| nbody                      | 89.3 ms                                                      | 101 ms: 1.14x slower                                               |
| crypto_pyaes               | 73.3 ms                                                      | 84.7 ms: 1.16x slower                                              |
| python_startup_no_site     | 8.96 ms                                                      | 10.5 ms: 1.17x slower                                              |
| subparsers                 | 17.5 ms                                                      | 23.9 ms: 1.37x slower                                              |
| gc_traversal               | 4.74 ms                                                      | 6.61 ms: 1.39x slower                                              |
| bench_mp_pool              | 5.12 ms                                                      | 1.22 sec: 238.95x slower                                           |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                       |

Benchmark hidden because not significant (7): sphinx, asyncio_websockets, sympy_str, sympy_sum, django_template, scimark_monte_carlo, bench_thread_pool
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250318-3.14.0a6+-0a71905/bm-20250318-pythonperf2-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.031x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.03x