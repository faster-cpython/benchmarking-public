# Results vs. 3.13.0

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: linux-x86_64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.046x slower
- HPT reliability: 99.85%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 326 ms: 1.11x slower                                                         |
| docutils       | 2.83 sec                                                     | 2.95 sec: 1.04x slower                                                       |
| html5lib       | 73.5 ms                                                      | 74.1 ms: 1.01x slower                                                        |
| sphinx         | 1.12 sec                                                     | 1.17 sec: 1.05x slower                                                       |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 306 ms: 1.52x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 547 ms: 1.52x faster                                                         |
| async_tree_io              | 843 ms                                                       | 579 ms: 1.46x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 242 ms: 1.43x faster                                                         |
| async_tree_none            | 376 ms                                                       | 278 ms: 1.35x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 337 ms: 1.35x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 472 ms: 1.23x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 507 ms: 1.19x faster                                                         |
| asyncio_websockets         | 388 ms                                                       | 375 ms: 1.04x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 21.3 ms: 1.01x faster                                                        |
| async_generators           | 457 ms                                                       | 480 ms: 1.05x slower                                                         |
| Geometric mean             | (ref)                                                        | 1.26x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 76.8 ms: 1.06x faster                                                        |
| pidigits       | 252 ms                                                       | 249 ms: 1.01x faster                                                         |
| nbody          | 89.3 ms                                                      | 132 ms: 1.48x slower                                                         |
| Geometric mean | (ref)                                                        | 1.11x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.18 ms: 1.15x faster                                                        |
| regex_dna      | 247 ms                                                       | 249 ms: 1.01x slower                                                         |
| regex_compile  | 143 ms                                                       | 160 ms: 1.12x slower                                                         |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 88.1 ms: 1.17x faster                                                        |
| xml_etree_parse      | 150 ms                                                       | 134 ms: 1.12x faster                                                         |
| tomli_loads          | 2.46 sec                                                     | 2.42 sec: 1.02x faster                                                       |
| xml_etree_generate   | 86.5 ms                                                      | 96.3 ms: 1.11x slower                                                        |
| unpickle_pure_python | 217 us                                                       | 244 us: 1.12x slower                                                         |
| xml_etree_process    | 61.2 ms                                                      | 69.5 ms: 1.14x slower                                                        |
| pickle_pure_python   | 323 us                                                       | 370 us: 1.15x slower                                                         |
| json_dumps           | 11.1 ms                                                      | 13.3 ms: 1.19x slower                                                        |
| json_loads           | 24.7 us                                                      | 29.7 us: 1.20x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.06x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 19.4 ms: 1.22x slower                                                        |
| python_startup_no_site | 8.96 ms                                                      | 13.8 ms: 1.54x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.37x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 57.1 ms                                                      | 63.8 ms: 1.12x slower                                                        |
| genshi_text     | 26.2 ms                                                      | 30.5 ms: 1.16x slower                                                        |
| django_template | 36.4 ms                                                      | 45.5 ms: 1.25x slower                                                        |
| mako            | 10.4 ms                                                      | 17.7 ms: 1.71x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.29x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| gc_traversal               | 4.74 ms                                                      | 2.18 ms: 2.17x faster                                                        |
| async_tree_memoization_tg  | 466 ms                                                       | 306 ms: 1.52x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 547 ms: 1.52x faster                                                         |
| async_tree_io              | 843 ms                                                       | 579 ms: 1.46x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 242 ms: 1.43x faster                                                         |
| create_gc_cycles           | 2.68 ms                                                      | 1.95 ms: 1.38x faster                                                        |
| async_tree_none            | 376 ms                                                       | 278 ms: 1.35x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 337 ms: 1.35x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 472 ms: 1.23x faster                                                         |
| deepcopy                   | 392 us                                                       | 328 us: 1.19x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 507 ms: 1.19x faster                                                         |
| xml_etree_iterparse        | 103 ms                                                       | 88.1 ms: 1.17x faster                                                        |
| regex_effbot               | 3.67 ms                                                      | 3.18 ms: 1.15x faster                                                        |
| sqlite_synth               | 2.91 us                                                      | 2.57 us: 1.13x faster                                                        |
| generators                 | 33.6 ms                                                      | 29.9 ms: 1.13x faster                                                        |
| xml_etree_parse            | 150 ms                                                       | 134 ms: 1.12x faster                                                         |
| go                         | 162 ms                                                       | 151 ms: 1.08x faster                                                         |
| deepcopy_memo              | 38.6 us                                                      | 36.1 us: 1.07x faster                                                        |
| float                      | 81.3 ms                                                      | 76.8 ms: 1.06x faster                                                        |
| dulwich_log                | 68.2 ms                                                      | 64.5 ms: 1.06x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 375 ms: 1.04x faster                                                         |
| pyflate                    | 503 ms                                                       | 489 ms: 1.03x faster                                                         |
| tomli_loads                | 2.46 sec                                                     | 2.42 sec: 1.02x faster                                                       |
| scimark_sor                | 123 ms                                                       | 121 ms: 1.02x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 21.3 ms: 1.01x faster                                                        |
| pidigits                   | 252 ms                                                       | 249 ms: 1.01x faster                                                         |
| deepcopy_reduce            | 3.54 us                                                      | 3.51 us: 1.01x faster                                                        |
| pathlib                    | 17.5 ms                                                      | 17.4 ms: 1.01x faster                                                        |
| regex_dna                  | 247 ms                                                       | 249 ms: 1.01x slower                                                         |
| pycparser                  | 1.24 sec                                                     | 1.25 sec: 1.01x slower                                                       |
| html5lib                   | 73.5 ms                                                      | 74.1 ms: 1.01x slower                                                        |
| logging_silent             | 97.9 ns                                                      | 101 ns: 1.03x slower                                                         |
| bpe_tokeniser              | 5.09 sec                                                     | 5.27 sec: 1.04x slower                                                       |
| spectral_norm              | 97.0 ms                                                      | 101 ms: 1.04x slower                                                         |
| docutils                   | 2.83 sec                                                     | 2.95 sec: 1.04x slower                                                       |
| sphinx                     | 1.12 sec                                                     | 1.17 sec: 1.05x slower                                                       |
| async_generators           | 457 ms                                                       | 480 ms: 1.05x slower                                                         |
| richards                   | 52.9 ms                                                      | 57.0 ms: 1.08x slower                                                        |
| scimark_fft                | 328 ms                                                       | 353 ms: 1.08x slower                                                         |
| pprint_safe_repr           | 843 ms                                                       | 909 ms: 1.08x slower                                                         |
| thrift                     | 901 us                                                       | 973 us: 1.08x slower                                                         |
| pprint_pformat             | 1.72 sec                                                     | 1.88 sec: 1.09x slower                                                       |
| mdp                        | 2.54 sec                                                     | 2.77 sec: 1.09x slower                                                       |
| telco                      | 8.79 ms                                                      | 9.62 ms: 1.09x slower                                                        |
| richards_super             | 59.6 ms                                                      | 65.6 ms: 1.10x slower                                                        |
| k_core                     | 2.17 sec                                                     | 2.39 sec: 1.10x slower                                                       |
| sympy_expand               | 509 ms                                                       | 565 ms: 1.11x slower                                                         |
| xml_etree_generate         | 86.5 ms                                                      | 96.3 ms: 1.11x slower                                                        |
| 2to3                       | 293 ms                                                       | 326 ms: 1.11x slower                                                         |
| genshi_xml                 | 57.1 ms                                                      | 63.8 ms: 1.12x slower                                                        |
| unpickle_pure_python       | 217 us                                                       | 244 us: 1.12x slower                                                         |
| regex_compile              | 143 ms                                                       | 160 ms: 1.12x slower                                                         |
| sympy_integrate            | 23.6 ms                                                      | 26.5 ms: 1.12x slower                                                        |
| sympy_str                  | 298 ms                                                       | 336 ms: 1.13x slower                                                         |
| sqlalchemy_imperative      | 18.3 ms                                                      | 20.6 ms: 1.13x slower                                                        |
| hexiom                     | 6.55 ms                                                      | 7.39 ms: 1.13x slower                                                        |
| sympy_sum                  | 155 ms                                                       | 175 ms: 1.13x slower                                                         |
| xml_etree_process          | 61.2 ms                                                      | 69.5 ms: 1.14x slower                                                        |
| shortest_path              | 460 ms                                                       | 523 ms: 1.14x slower                                                         |
| logging_simple             | 6.39 us                                                      | 7.31 us: 1.14x slower                                                        |
| pickle_pure_python         | 323 us                                                       | 370 us: 1.15x slower                                                         |
| connected_components       | 432 ms                                                       | 499 ms: 1.15x slower                                                         |
| chaos                      | 60.2 ms                                                      | 69.5 ms: 1.15x slower                                                        |
| genshi_text                | 26.2 ms                                                      | 30.5 ms: 1.16x slower                                                        |
| sqlalchemy_declarative     | 148 ms                                                       | 172 ms: 1.16x slower                                                         |
| logging_format             | 6.94 us                                                      | 8.12 us: 1.17x slower                                                        |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 5.62 ms: 1.18x slower                                                        |
| deltablue                  | 3.42 ms                                                      | 4.02 ms: 1.18x slower                                                        |
| json_dumps                 | 11.1 ms                                                      | 13.3 ms: 1.19x slower                                                        |
| meteor_contest             | 130 ms                                                       | 155 ms: 1.20x slower                                                         |
| many_optionals             | 930 us                                                       | 1.11 ms: 1.20x slower                                                        |
| comprehensions             | 17.0 us                                                      | 20.5 us: 1.20x slower                                                        |
| json_loads                 | 24.7 us                                                      | 29.7 us: 1.20x slower                                                        |
| python_startup             | 15.9 ms                                                      | 19.4 ms: 1.22x slower                                                        |
| raytrace                   | 273 ms                                                       | 333 ms: 1.22x slower                                                         |
| nqueens                    | 90.7 ms                                                      | 111 ms: 1.22x slower                                                         |
| scimark_lu                 | 98.7 ms                                                      | 122 ms: 1.23x slower                                                         |
| django_template            | 36.4 ms                                                      | 45.5 ms: 1.25x slower                                                        |
| typing_runtime_protocols   | 169 us                                                       | 217 us: 1.29x slower                                                         |
| scimark_monte_carlo        | 66.1 ms                                                      | 85.4 ms: 1.29x slower                                                        |
| crypto_pyaes               | 73.3 ms                                                      | 95.0 ms: 1.30x slower                                                        |
| fannkuch                   | 363 ms                                                       | 474 ms: 1.30x slower                                                         |
| subparsers                 | 17.5 ms                                                      | 25.6 ms: 1.46x slower                                                        |
| coverage                   | 80.0 ms                                                      | 118 ms: 1.48x slower                                                         |
| nbody                      | 89.3 ms                                                      | 132 ms: 1.48x slower                                                         |
| bench_thread_pool          | 942 us                                                       | 1.45 ms: 1.54x slower                                                        |
| python_startup_no_site     | 8.96 ms                                                      | 13.8 ms: 1.54x slower                                                        |
| mako                       | 10.4 ms                                                      | 17.7 ms: 1.71x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 50.4 ms: 9.83x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.08x slower                                                                 |

Benchmark hidden because not significant (3): regex_v8, json, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250322-3.14.0a6+-bc26f95-NOGIL/bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.046x slower

# HPT report

- Reliability score: 99.85% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.25x