# Results vs. 3.13.0

- fork: mdboom
- ref: tuple_hash_cache2
- machine: linux-x86_64
- commit hash: a31e8be
- commit date: 2025-03-20
- overall geometric mean: 1.036x faster
- HPT reliability: 99.94%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250320-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-a31e8be |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 288 ms: 1.02x faster                                                      |
| docutils       | 2.83 sec                                                     | 2.91 sec: 1.03x slower                                                    |
| html5lib       | 73.5 ms                                                      | 70.4 ms: 1.04x faster                                                     |
| Geometric mean | (ref)                                                        | 1.01x faster                                                              |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250320-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-a31e8be |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 359 ms: 1.30x faster                                                      |
| async_tree_io              | 843 ms                                                       | 660 ms: 1.28x faster                                                      |
| async_tree_memoization     | 453 ms                                                       | 359 ms: 1.26x faster                                                      |
| async_tree_none            | 376 ms                                                       | 299 ms: 1.26x faster                                                      |
| async_tree_io_tg           | 831 ms                                                       | 668 ms: 1.24x faster                                                      |
| async_tree_none_tg         | 346 ms                                                       | 284 ms: 1.22x faster                                                      |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 528 ms: 1.14x faster                                                      |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 521 ms: 1.12x faster                                                      |
| async_generators           | 457 ms                                                       | 424 ms: 1.08x faster                                                      |
| coroutines                 | 21.6 ms                                                      | 21.1 ms: 1.02x faster                                                     |
| Geometric mean             | (ref)                                                        | 1.17x faster                                                              |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250320-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-a31e8be |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 71.9 ms: 1.13x faster                                                     |
| pidigits       | 252 ms                                                       | 254 ms: 1.01x slower                                                      |
| nbody          | 89.3 ms                                                      | 103 ms: 1.15x slower                                                      |
| Geometric mean | (ref)                                                        | 1.01x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250320-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-a31e8be |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.01 ms: 1.22x faster                                                     |
| regex_v8       | 26.1 ms                                                      | 24.0 ms: 1.09x faster                                                     |
| regex_dna      | 247 ms                                                       | 237 ms: 1.04x faster                                                      |
| regex_compile  | 143 ms                                                       | 137 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                        | 1.10x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250320-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-a31e8be |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.19 sec: 1.13x faster                                                    |
| xml_etree_parse      | 150 ms                                                       | 137 ms: 1.09x faster                                                      |
| xml_etree_iterparse  | 103 ms                                                       | 98.8 ms: 1.04x faster                                                     |
| xml_etree_process    | 61.2 ms                                                      | 61.4 ms: 1.00x slower                                                     |
| unpickle_pure_python | 217 us                                                       | 224 us: 1.03x slower                                                      |
| json_dumps           | 11.1 ms                                                      | 11.6 ms: 1.04x slower                                                     |
| pickle_pure_python   | 323 us                                                       | 340 us: 1.05x slower                                                      |
| json_loads           | 24.7 us                                                      | 26.3 us: 1.07x slower                                                     |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                              |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250320-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-a31e8be |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 16.4 ms: 1.03x slower                                                     |
| python_startup_no_site | 8.96 ms                                                      | 10.5 ms: 1.17x slower                                                     |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250320-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-a31e8be |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 25.0 ms: 1.05x faster                                                     |
| genshi_xml      | 57.1 ms                                                      | 55.8 ms: 1.02x faster                                                     |
| django_template | 36.4 ms                                                      | 37.5 ms: 1.03x slower                                                     |
| mako            | 10.4 ms                                                      | 11.2 ms: 1.08x slower                                                     |
| Geometric mean  | (ref)                                                        | 1.01x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250320-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-a31e8be |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.34 sec: 1.89x faster                                                    |
| deepcopy                   | 392 us                                                       | 289 us: 1.36x faster                                                      |
| async_tree_memoization_tg  | 466 ms                                                       | 359 ms: 1.30x faster                                                      |
| async_tree_io              | 843 ms                                                       | 660 ms: 1.28x faster                                                      |
| deepcopy_memo              | 38.6 us                                                      | 30.4 us: 1.27x faster                                                     |
| async_tree_memoization     | 453 ms                                                       | 359 ms: 1.26x faster                                                      |
| async_tree_none            | 376 ms                                                       | 299 ms: 1.26x faster                                                      |
| async_tree_io_tg           | 831 ms                                                       | 668 ms: 1.24x faster                                                      |
| regex_effbot               | 3.67 ms                                                      | 3.01 ms: 1.22x faster                                                     |
| async_tree_none_tg         | 346 ms                                                       | 284 ms: 1.22x faster                                                      |
| go                         | 162 ms                                                       | 133 ms: 1.22x faster                                                      |
| deepcopy_reduce            | 3.54 us                                                      | 3.00 us: 1.18x faster                                                     |
| generators                 | 33.6 ms                                                      | 28.5 ms: 1.18x faster                                                     |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 528 ms: 1.14x faster                                                      |
| float                      | 81.3 ms                                                      | 71.9 ms: 1.13x faster                                                     |
| tomli_loads                | 2.46 sec                                                     | 2.19 sec: 1.13x faster                                                    |
| richards                   | 52.9 ms                                                      | 47.2 ms: 1.12x faster                                                     |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 521 ms: 1.12x faster                                                      |
| richards_super             | 59.6 ms                                                      | 53.4 ms: 1.12x faster                                                     |
| telco                      | 8.79 ms                                                      | 7.94 ms: 1.11x faster                                                     |
| scimark_sor                | 123 ms                                                       | 111 ms: 1.11x faster                                                      |
| xml_etree_parse            | 150 ms                                                       | 137 ms: 1.09x faster                                                      |
| regex_v8                   | 26.1 ms                                                      | 24.0 ms: 1.09x faster                                                     |
| pyflate                    | 503 ms                                                       | 464 ms: 1.08x faster                                                      |
| dulwich_log                | 68.2 ms                                                      | 63.2 ms: 1.08x faster                                                     |
| async_generators           | 457 ms                                                       | 424 ms: 1.08x faster                                                      |
| pylint                     | 347 ms                                                       | 323 ms: 1.07x faster                                                      |
| spectral_norm              | 97.0 ms                                                      | 91.6 ms: 1.06x faster                                                     |
| genshi_text                | 26.2 ms                                                      | 25.0 ms: 1.05x faster                                                     |
| bpe_tokeniser              | 5.09 sec                                                     | 4.87 sec: 1.05x faster                                                    |
| html5lib                   | 73.5 ms                                                      | 70.4 ms: 1.04x faster                                                     |
| regex_dna                  | 247 ms                                                       | 237 ms: 1.04x faster                                                      |
| regex_compile              | 143 ms                                                       | 137 ms: 1.04x faster                                                      |
| xml_etree_iterparse        | 103 ms                                                       | 98.8 ms: 1.04x faster                                                     |
| json                       | 5.69 ms                                                      | 5.50 ms: 1.03x faster                                                     |
| logging_silent             | 97.9 ns                                                      | 94.9 ns: 1.03x faster                                                     |
| coroutines                 | 21.6 ms                                                      | 21.1 ms: 1.02x faster                                                     |
| genshi_xml                 | 57.1 ms                                                      | 55.8 ms: 1.02x faster                                                     |
| pprint_pformat             | 1.72 sec                                                     | 1.69 sec: 1.02x faster                                                    |
| k_core                     | 2.17 sec                                                     | 2.13 sec: 1.02x faster                                                    |
| 2to3                       | 293 ms                                                       | 288 ms: 1.02x faster                                                      |
| sqlite_synth               | 2.91 us                                                      | 2.86 us: 1.02x faster                                                     |
| hexiom                     | 6.55 ms                                                      | 6.45 ms: 1.02x faster                                                     |
| coverage                   | 80.0 ms                                                      | 78.8 ms: 1.01x faster                                                     |
| shortest_path              | 460 ms                                                       | 454 ms: 1.01x faster                                                      |
| scimark_fft                | 328 ms                                                       | 324 ms: 1.01x faster                                                      |
| pathlib                    | 17.5 ms                                                      | 17.4 ms: 1.01x faster                                                     |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.72 ms: 1.01x faster                                                     |
| deltablue                  | 3.42 ms                                                      | 3.38 ms: 1.01x faster                                                     |
| scimark_monte_carlo        | 66.1 ms                                                      | 65.6 ms: 1.01x faster                                                     |
| sqlalchemy_declarative     | 148 ms                                                       | 148 ms: 1.01x faster                                                      |
| pprint_safe_repr           | 843 ms                                                       | 838 ms: 1.01x faster                                                      |
| connected_components       | 432 ms                                                       | 434 ms: 1.00x slower                                                      |
| xml_etree_process          | 61.2 ms                                                      | 61.4 ms: 1.00x slower                                                     |
| pidigits                   | 252 ms                                                       | 254 ms: 1.01x slower                                                      |
| meteor_contest             | 130 ms                                                       | 130 ms: 1.01x slower                                                      |
| logging_simple             | 6.39 us                                                      | 6.56 us: 1.03x slower                                                     |
| docutils                   | 2.83 sec                                                     | 2.91 sec: 1.03x slower                                                    |
| unpickle_pure_python       | 217 us                                                       | 224 us: 1.03x slower                                                      |
| django_template            | 36.4 ms                                                      | 37.5 ms: 1.03x slower                                                     |
| python_startup             | 15.9 ms                                                      | 16.4 ms: 1.03x slower                                                     |
| json_dumps                 | 11.1 ms                                                      | 11.6 ms: 1.04x slower                                                     |
| typing_runtime_protocols   | 169 us                                                       | 176 us: 1.04x slower                                                      |
| scimark_lu                 | 98.7 ms                                                      | 103 ms: 1.04x slower                                                      |
| pycparser                  | 1.24 sec                                                     | 1.30 sec: 1.04x slower                                                    |
| comprehensions             | 17.0 us                                                      | 17.9 us: 1.05x slower                                                     |
| logging_format             | 6.94 us                                                      | 7.31 us: 1.05x slower                                                     |
| pickle_pure_python         | 323 us                                                       | 340 us: 1.05x slower                                                      |
| create_gc_cycles           | 2.68 ms                                                      | 2.83 ms: 1.06x slower                                                     |
| json_loads                 | 24.7 us                                                      | 26.3 us: 1.07x slower                                                     |
| nqueens                    | 90.7 ms                                                      | 96.7 ms: 1.07x slower                                                     |
| fannkuch                   | 363 ms                                                       | 388 ms: 1.07x slower                                                      |
| mako                       | 10.4 ms                                                      | 11.2 ms: 1.08x slower                                                     |
| chaos                      | 60.2 ms                                                      | 65.9 ms: 1.10x slower                                                     |
| raytrace                   | 273 ms                                                       | 301 ms: 1.10x slower                                                      |
| crypto_pyaes               | 73.3 ms                                                      | 81.5 ms: 1.11x slower                                                     |
| many_optionals             | 930 us                                                       | 1.04 ms: 1.12x slower                                                     |
| nbody                      | 89.3 ms                                                      | 103 ms: 1.15x slower                                                      |
| python_startup_no_site     | 8.96 ms                                                      | 10.5 ms: 1.17x slower                                                     |
| gc_traversal               | 4.74 ms                                                      | 6.38 ms: 1.35x slower                                                     |
| subparsers                 | 17.5 ms                                                      | 23.5 ms: 1.35x slower                                                     |
| bench_mp_pool              | 5.12 ms                                                      | 1.07 sec: 209.40x slower                                                  |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                              |

Benchmark hidden because not significant (5): sphinx, sqlalchemy_imperative, asyncio_websockets, xml_etree_generate, bench_thread_pool
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250320-3.14.0a6+-a31e8be/bm-20250320-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-a31e8be.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.036x faster

# HPT report

- Reliability score: 99.94% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x