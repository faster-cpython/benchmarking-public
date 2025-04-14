# Results vs. 3.13.0

- fork: mdboom
- ref: tuple_hash_cache_emp
- machine: linux-x86_64
- commit hash: 40ad9fc
- commit date: 2025-03-21
- overall geometric mean: 1.038x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250321-pythonperf2-x86_64-mdboom-tuple_hash_cache_emp-3.14.0a6+-40ad9fc |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 287 ms: 1.02x faster                                                         |
| docutils       | 2.83 sec                                                     | 2.90 sec: 1.02x slower                                                       |
| html5lib       | 73.5 ms                                                      | 70.7 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250321-pythonperf2-x86_64-mdboom-tuple_hash_cache_emp-3.14.0a6+-40ad9fc |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io              | 843 ms                                                       | 642 ms: 1.31x faster                                                         |
| async_tree_memoization_tg  | 466 ms                                                       | 356 ms: 1.31x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 354 ms: 1.28x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 653 ms: 1.27x faster                                                         |
| async_tree_none            | 376 ms                                                       | 297 ms: 1.27x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 282 ms: 1.23x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 525 ms: 1.15x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 521 ms: 1.12x faster                                                         |
| async_generators           | 457 ms                                                       | 415 ms: 1.10x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 21.3 ms: 1.01x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.18x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250321-pythonperf2-x86_64-mdboom-tuple_hash_cache_emp-3.14.0a6+-40ad9fc |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 72.1 ms: 1.13x faster                                                        |
| pidigits       | 252 ms                                                       | 254 ms: 1.01x slower                                                         |
| nbody          | 89.3 ms                                                      | 105 ms: 1.18x slower                                                         |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250321-pythonperf2-x86_64-mdboom-tuple_hash_cache_emp-3.14.0a6+-40ad9fc |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.12 ms: 1.18x faster                                                        |
| regex_v8       | 26.1 ms                                                      | 24.4 ms: 1.07x faster                                                        |
| regex_dna      | 247 ms                                                       | 239 ms: 1.03x faster                                                         |
| regex_compile  | 143 ms                                                       | 139 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250321-pythonperf2-x86_64-mdboom-tuple_hash_cache_emp-3.14.0a6+-40ad9fc |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.20 sec: 1.12x faster                                                       |
| xml_etree_parse      | 150 ms                                                       | 137 ms: 1.10x faster                                                         |
| xml_etree_iterparse  | 103 ms                                                       | 97.7 ms: 1.05x faster                                                        |
| xml_etree_generate   | 86.5 ms                                                      | 85.6 ms: 1.01x faster                                                        |
| xml_etree_process    | 61.2 ms                                                      | 61.5 ms: 1.01x slower                                                        |
| unpickle_pure_python | 217 us                                                       | 222 us: 1.02x slower                                                         |
| json_dumps           | 11.1 ms                                                      | 11.5 ms: 1.03x slower                                                        |
| pickle_pure_python   | 323 us                                                       | 340 us: 1.05x slower                                                         |
| json_loads           | 24.7 us                                                      | 26.2 us: 1.06x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250321-pythonperf2-x86_64-mdboom-tuple_hash_cache_emp-3.14.0a6+-40ad9fc |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 16.4 ms: 1.03x slower                                                        |
| python_startup_no_site | 8.96 ms                                                      | 10.5 ms: 1.17x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250321-pythonperf2-x86_64-mdboom-tuple_hash_cache_emp-3.14.0a6+-40ad9fc |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text    | 26.2 ms                                                      | 23.7 ms: 1.11x faster                                                        |
| genshi_xml     | 57.1 ms                                                      | 54.9 ms: 1.04x faster                                                        |
| mako           | 10.4 ms                                                      | 11.4 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250321-pythonperf2-x86_64-mdboom-tuple_hash_cache_emp-3.14.0a6+-40ad9fc |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.31 sec: 1.93x faster                                                       |
| deepcopy                   | 392 us                                                       | 287 us: 1.37x faster                                                         |
| async_tree_io              | 843 ms                                                       | 642 ms: 1.31x faster                                                         |
| async_tree_memoization_tg  | 466 ms                                                       | 356 ms: 1.31x faster                                                         |
| deepcopy_memo              | 38.6 us                                                      | 29.7 us: 1.30x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 354 ms: 1.28x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 653 ms: 1.27x faster                                                         |
| async_tree_none            | 376 ms                                                       | 297 ms: 1.27x faster                                                         |
| go                         | 162 ms                                                       | 132 ms: 1.23x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 282 ms: 1.23x faster                                                         |
| regex_effbot               | 3.67 ms                                                      | 3.12 ms: 1.18x faster                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 3.03 us: 1.17x faster                                                        |
| generators                 | 33.6 ms                                                      | 28.8 ms: 1.17x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 525 ms: 1.15x faster                                                         |
| float                      | 81.3 ms                                                      | 72.1 ms: 1.13x faster                                                        |
| scimark_sor                | 123 ms                                                       | 110 ms: 1.12x faster                                                         |
| tomli_loads                | 2.46 sec                                                     | 2.20 sec: 1.12x faster                                                       |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 521 ms: 1.12x faster                                                         |
| richards_super             | 59.6 ms                                                      | 53.5 ms: 1.11x faster                                                        |
| genshi_text                | 26.2 ms                                                      | 23.7 ms: 1.11x faster                                                        |
| async_generators           | 457 ms                                                       | 415 ms: 1.10x faster                                                         |
| xml_etree_parse            | 150 ms                                                       | 137 ms: 1.10x faster                                                         |
| richards                   | 52.9 ms                                                      | 48.3 ms: 1.10x faster                                                        |
| pylint                     | 347 ms                                                       | 320 ms: 1.08x faster                                                         |
| dulwich_log                | 68.2 ms                                                      | 63.0 ms: 1.08x faster                                                        |
| spectral_norm              | 97.0 ms                                                      | 90.3 ms: 1.07x faster                                                        |
| telco                      | 8.79 ms                                                      | 8.19 ms: 1.07x faster                                                        |
| regex_v8                   | 26.1 ms                                                      | 24.4 ms: 1.07x faster                                                        |
| pyflate                    | 503 ms                                                       | 471 ms: 1.07x faster                                                         |
| bpe_tokeniser              | 5.09 sec                                                     | 4.79 sec: 1.06x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 97.7 ms: 1.05x faster                                                        |
| genshi_xml                 | 57.1 ms                                                      | 54.9 ms: 1.04x faster                                                        |
| logging_silent             | 97.9 ns                                                      | 94.1 ns: 1.04x faster                                                        |
| html5lib                   | 73.5 ms                                                      | 70.7 ms: 1.04x faster                                                        |
| json                       | 5.69 ms                                                      | 5.48 ms: 1.04x faster                                                        |
| scimark_fft                | 328 ms                                                       | 316 ms: 1.04x faster                                                         |
| regex_dna                  | 247 ms                                                       | 239 ms: 1.03x faster                                                         |
| regex_compile              | 143 ms                                                       | 139 ms: 1.03x faster                                                         |
| sqlite_synth               | 2.91 us                                                      | 2.82 us: 1.03x faster                                                        |
| pprint_pformat             | 1.72 sec                                                     | 1.67 sec: 1.03x faster                                                       |
| pathlib                    | 17.5 ms                                                      | 17.1 ms: 1.03x faster                                                        |
| k_core                     | 2.17 sec                                                     | 2.12 sec: 1.02x faster                                                       |
| pprint_safe_repr           | 843 ms                                                       | 825 ms: 1.02x faster                                                         |
| 2to3                       | 293 ms                                                       | 287 ms: 1.02x faster                                                         |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.69 ms: 1.02x faster                                                        |
| sqlalchemy_declarative     | 148 ms                                                       | 146 ms: 1.02x faster                                                         |
| shortest_path              | 460 ms                                                       | 454 ms: 1.01x faster                                                         |
| meteor_contest             | 130 ms                                                       | 128 ms: 1.01x faster                                                         |
| sqlalchemy_imperative      | 18.3 ms                                                      | 18.1 ms: 1.01x faster                                                        |
| connected_components       | 432 ms                                                       | 427 ms: 1.01x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 21.3 ms: 1.01x faster                                                        |
| xml_etree_generate         | 86.5 ms                                                      | 85.6 ms: 1.01x faster                                                        |
| sympy_integrate            | 23.6 ms                                                      | 23.4 ms: 1.01x faster                                                        |
| sympy_str                  | 298 ms                                                       | 296 ms: 1.01x faster                                                         |
| hexiom                     | 6.55 ms                                                      | 6.51 ms: 1.01x faster                                                        |
| sympy_expand               | 509 ms                                                       | 507 ms: 1.00x faster                                                         |
| sympy_sum                  | 155 ms                                                       | 154 ms: 1.00x faster                                                         |
| xml_etree_process          | 61.2 ms                                                      | 61.5 ms: 1.01x slower                                                        |
| scimark_lu                 | 98.7 ms                                                      | 99.3 ms: 1.01x slower                                                        |
| pidigits                   | 252 ms                                                       | 254 ms: 1.01x slower                                                         |
| typing_runtime_protocols   | 169 us                                                       | 172 us: 1.02x slower                                                         |
| bench_thread_pool          | 942 us                                                       | 961 us: 1.02x slower                                                         |
| unpickle_pure_python       | 217 us                                                       | 222 us: 1.02x slower                                                         |
| docutils                   | 2.83 sec                                                     | 2.90 sec: 1.02x slower                                                       |
| python_startup             | 15.9 ms                                                      | 16.4 ms: 1.03x slower                                                        |
| coverage                   | 80.0 ms                                                      | 82.4 ms: 1.03x slower                                                        |
| logging_simple             | 6.39 us                                                      | 6.59 us: 1.03x slower                                                        |
| json_dumps                 | 11.1 ms                                                      | 11.5 ms: 1.03x slower                                                        |
| scimark_monte_carlo        | 66.1 ms                                                      | 68.8 ms: 1.04x slower                                                        |
| logging_format             | 6.94 us                                                      | 7.26 us: 1.05x slower                                                        |
| pickle_pure_python         | 323 us                                                       | 340 us: 1.05x slower                                                         |
| comprehensions             | 17.0 us                                                      | 18.0 us: 1.06x slower                                                        |
| json_loads                 | 24.7 us                                                      | 26.2 us: 1.06x slower                                                        |
| nqueens                    | 90.7 ms                                                      | 96.7 ms: 1.07x slower                                                        |
| chaos                      | 60.2 ms                                                      | 64.2 ms: 1.07x slower                                                        |
| fannkuch                   | 363 ms                                                       | 388 ms: 1.07x slower                                                         |
| create_gc_cycles           | 2.68 ms                                                      | 2.87 ms: 1.07x slower                                                        |
| raytrace                   | 273 ms                                                       | 298 ms: 1.09x slower                                                         |
| mako                       | 10.4 ms                                                      | 11.4 ms: 1.10x slower                                                        |
| many_optionals             | 930 us                                                       | 1.04 ms: 1.12x slower                                                        |
| crypto_pyaes               | 73.3 ms                                                      | 84.2 ms: 1.15x slower                                                        |
| python_startup_no_site     | 8.96 ms                                                      | 10.5 ms: 1.17x slower                                                        |
| nbody                      | 89.3 ms                                                      | 105 ms: 1.18x slower                                                         |
| subparsers                 | 17.5 ms                                                      | 23.7 ms: 1.36x slower                                                        |
| gc_traversal               | 4.74 ms                                                      | 6.61 ms: 1.40x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 1.65 sec: 322.40x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                                 |

Benchmark hidden because not significant (5): sphinx, deltablue, pycparser, django_template, asyncio_websockets
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250321-3.14.0a6+-40ad9fc/bm-20250321-pythonperf2-x86_64-mdboom-tuple_hash_cache_emp-3.14.0a6+-40ad9fc.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.038x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x