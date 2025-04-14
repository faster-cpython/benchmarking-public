# Results vs. 3.13.0

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: linux-x86_64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.032x faster
- HPT reliability: 99.51%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 293 ms: 1.00x slower                                                         |
| docutils       | 2.83 sec                                                     | 3.00 sec: 1.06x slower                                                       |
| html5lib       | 73.5 ms                                                      | 71.0 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 333 ms: 1.40x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 341 ms: 1.33x faster                                                         |
| async_tree_io              | 843 ms                                                       | 654 ms: 1.29x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 652 ms: 1.27x faster                                                         |
| async_tree_none            | 376 ms                                                       | 299 ms: 1.26x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 281 ms: 1.23x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 520 ms: 1.16x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 510 ms: 1.14x faster                                                         |
| async_generators           | 457 ms                                                       | 446 ms: 1.02x faster                                                         |
| asyncio_websockets         | 388 ms                                                       | 385 ms: 1.01x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.19x faster                                                                 |

Benchmark hidden because not significant (1): coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 66.0 ms: 1.23x faster                                                        |
| pidigits       | 252 ms                                                       | 253 ms: 1.00x slower                                                         |
| nbody          | 89.3 ms                                                      | 94.5 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 2.98 ms: 1.23x faster                                                        |
| regex_v8       | 26.1 ms                                                      | 23.1 ms: 1.13x faster                                                        |
| regex_dna      | 247 ms                                                       | 230 ms: 1.07x faster                                                         |
| regex_compile  | 143 ms                                                       | 141 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                        | 1.11x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.12 sec: 1.16x faster                                                       |
| xml_etree_parse      | 150 ms                                                       | 135 ms: 1.11x faster                                                         |
| xml_etree_iterparse  | 103 ms                                                       | 96.8 ms: 1.06x faster                                                        |
| xml_etree_generate   | 86.5 ms                                                      | 81.5 ms: 1.06x faster                                                        |
| xml_etree_process    | 61.2 ms                                                      | 58.0 ms: 1.06x faster                                                        |
| unpickle_pure_python | 217 us                                                       | 222 us: 1.02x slower                                                         |
| json_dumps           | 11.1 ms                                                      | 11.5 ms: 1.03x slower                                                        |
| json_loads           | 24.7 us                                                      | 26.8 us: 1.09x slower                                                        |
| pickle_pure_python   | 323 us                                                       | 352 us: 1.09x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 16.5 ms: 1.03x slower                                                        |
| python_startup_no_site | 8.96 ms                                                      | 10.5 ms: 1.18x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.9 ms: 1.10x faster                                                        |
| mako            | 10.4 ms                                                      | 10.5 ms: 1.01x slower                                                        |
| django_template | 36.4 ms                                                      | 37.2 ms: 1.02x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.02x faster                                                                 |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 333 ms: 1.40x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 341 ms: 1.33x faster                                                         |
| deepcopy_memo              | 38.6 us                                                      | 29.5 us: 1.31x faster                                                        |
| richards                   | 52.9 ms                                                      | 40.7 ms: 1.30x faster                                                        |
| deepcopy                   | 392 us                                                       | 303 us: 1.30x faster                                                         |
| async_tree_io              | 843 ms                                                       | 654 ms: 1.29x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 652 ms: 1.27x faster                                                         |
| richards_super             | 59.6 ms                                                      | 46.8 ms: 1.27x faster                                                        |
| async_tree_none            | 376 ms                                                       | 299 ms: 1.26x faster                                                         |
| float                      | 81.3 ms                                                      | 66.0 ms: 1.23x faster                                                        |
| regex_effbot               | 3.67 ms                                                      | 2.98 ms: 1.23x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 281 ms: 1.23x faster                                                         |
| generators                 | 33.6 ms                                                      | 28.8 ms: 1.17x faster                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 3.04 us: 1.16x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 520 ms: 1.16x faster                                                         |
| tomli_loads                | 2.46 sec                                                     | 2.12 sec: 1.16x faster                                                       |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 510 ms: 1.14x faster                                                         |
| regex_v8                   | 26.1 ms                                                      | 23.1 ms: 1.13x faster                                                        |
| spectral_norm              | 97.0 ms                                                      | 86.0 ms: 1.13x faster                                                        |
| pyflate                    | 503 ms                                                       | 447 ms: 1.12x faster                                                         |
| scimark_sor                | 123 ms                                                       | 111 ms: 1.11x faster                                                         |
| xml_etree_parse            | 150 ms                                                       | 135 ms: 1.11x faster                                                         |
| genshi_text                | 26.2 ms                                                      | 23.9 ms: 1.10x faster                                                        |
| deltablue                  | 3.42 ms                                                      | 3.12 ms: 1.10x faster                                                        |
| telco                      | 8.79 ms                                                      | 8.09 ms: 1.09x faster                                                        |
| go                         | 162 ms                                                       | 150 ms: 1.08x faster                                                         |
| dulwich_log                | 68.2 ms                                                      | 63.2 ms: 1.08x faster                                                        |
| regex_dna                  | 247 ms                                                       | 230 ms: 1.07x faster                                                         |
| pylint                     | 347 ms                                                       | 325 ms: 1.07x faster                                                         |
| xml_etree_iterparse        | 103 ms                                                       | 96.8 ms: 1.06x faster                                                        |
| xml_etree_generate         | 86.5 ms                                                      | 81.5 ms: 1.06x faster                                                        |
| xml_etree_process          | 61.2 ms                                                      | 58.0 ms: 1.06x faster                                                        |
| json                       | 5.69 ms                                                      | 5.41 ms: 1.05x faster                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 4.85 sec: 1.05x faster                                                       |
| k_core                     | 2.17 sec                                                     | 2.07 sec: 1.05x faster                                                       |
| logging_silent             | 97.9 ns                                                      | 93.6 ns: 1.05x faster                                                        |
| sqlite_synth               | 2.91 us                                                      | 2.79 us: 1.04x faster                                                        |
| scimark_fft                | 328 ms                                                       | 316 ms: 1.04x faster                                                         |
| connected_components       | 432 ms                                                       | 417 ms: 1.04x faster                                                         |
| html5lib                   | 73.5 ms                                                      | 71.0 ms: 1.03x faster                                                        |
| pprint_pformat             | 1.72 sec                                                     | 1.67 sec: 1.03x faster                                                       |
| thrift                     | 901 us                                                       | 877 us: 1.03x faster                                                         |
| async_generators           | 457 ms                                                       | 446 ms: 1.02x faster                                                         |
| shortest_path              | 460 ms                                                       | 450 ms: 1.02x faster                                                         |
| coverage                   | 80.0 ms                                                      | 78.2 ms: 1.02x faster                                                        |
| regex_compile              | 143 ms                                                       | 141 ms: 1.01x faster                                                         |
| pprint_safe_repr           | 843 ms                                                       | 832 ms: 1.01x faster                                                         |
| asyncio_websockets         | 388 ms                                                       | 385 ms: 1.01x faster                                                         |
| sympy_integrate            | 23.6 ms                                                      | 23.4 ms: 1.01x faster                                                        |
| 2to3                       | 293 ms                                                       | 293 ms: 1.00x slower                                                         |
| sympy_str                  | 298 ms                                                       | 299 ms: 1.00x slower                                                         |
| pidigits                   | 252 ms                                                       | 253 ms: 1.00x slower                                                         |
| mdp                        | 2.54 sec                                                     | 2.56 sec: 1.01x slower                                                       |
| sqlalchemy_declarative     | 148 ms                                                       | 150 ms: 1.01x slower                                                         |
| mako                       | 10.4 ms                                                      | 10.5 ms: 1.01x slower                                                        |
| sympy_sum                  | 155 ms                                                       | 156 ms: 1.01x slower                                                         |
| sympy_expand               | 509 ms                                                       | 517 ms: 1.02x slower                                                         |
| create_gc_cycles           | 2.68 ms                                                      | 2.73 ms: 1.02x slower                                                        |
| unpickle_pure_python       | 217 us                                                       | 222 us: 1.02x slower                                                         |
| django_template            | 36.4 ms                                                      | 37.2 ms: 1.02x slower                                                        |
| logging_simple             | 6.39 us                                                      | 6.60 us: 1.03x slower                                                        |
| json_dumps                 | 11.1 ms                                                      | 11.5 ms: 1.03x slower                                                        |
| python_startup             | 15.9 ms                                                      | 16.5 ms: 1.03x slower                                                        |
| meteor_contest             | 130 ms                                                       | 134 ms: 1.04x slower                                                         |
| logging_format             | 6.94 us                                                      | 7.20 us: 1.04x slower                                                        |
| bench_thread_pool          | 942 us                                                       | 983 us: 1.04x slower                                                         |
| scimark_lu                 | 98.7 ms                                                      | 103 ms: 1.04x slower                                                         |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 5.00 ms: 1.05x slower                                                        |
| nqueens                    | 90.7 ms                                                      | 95.0 ms: 1.05x slower                                                        |
| pycparser                  | 1.24 sec                                                     | 1.31 sec: 1.06x slower                                                       |
| nbody                      | 89.3 ms                                                      | 94.5 ms: 1.06x slower                                                        |
| docutils                   | 2.83 sec                                                     | 3.00 sec: 1.06x slower                                                       |
| hexiom                     | 6.55 ms                                                      | 6.97 ms: 1.06x slower                                                        |
| typing_runtime_protocols   | 169 us                                                       | 181 us: 1.07x slower                                                         |
| scimark_monte_carlo        | 66.1 ms                                                      | 71.1 ms: 1.07x slower                                                        |
| raytrace                   | 273 ms                                                       | 293 ms: 1.08x slower                                                         |
| json_loads                 | 24.7 us                                                      | 26.8 us: 1.09x slower                                                        |
| pickle_pure_python         | 323 us                                                       | 352 us: 1.09x slower                                                         |
| chaos                      | 60.2 ms                                                      | 67.0 ms: 1.11x slower                                                        |
| fannkuch                   | 363 ms                                                       | 413 ms: 1.14x slower                                                         |
| many_optionals             | 930 us                                                       | 1.07 ms: 1.15x slower                                                        |
| python_startup_no_site     | 8.96 ms                                                      | 10.5 ms: 1.18x slower                                                        |
| crypto_pyaes               | 73.3 ms                                                      | 87.2 ms: 1.19x slower                                                        |
| comprehensions             | 17.0 us                                                      | 21.1 us: 1.24x slower                                                        |
| gc_traversal               | 4.74 ms                                                      | 6.37 ms: 1.34x slower                                                        |
| subparsers                 | 17.5 ms                                                      | 24.0 ms: 1.37x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 1.11 sec: 215.95x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                                 |

Benchmark hidden because not significant (5): genshi_xml, coroutines, pathlib, sphinx, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.032x faster

# HPT report

- Reliability score: 99.51% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x