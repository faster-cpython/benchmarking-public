# Results vs. 3.13.0

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: linux-x86_64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.034x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 287 ms: 1.02x faster                                                         |
| docutils       | 2.83 sec                                                     | 2.92 sec: 1.03x slower                                                       |
| html5lib       | 73.5 ms                                                      | 69.0 ms: 1.07x faster                                                        |
| sphinx         | 1.12 sec                                                     | 1.11 sec: 1.01x faster                                                       |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 332 ms: 1.40x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 343 ms: 1.32x faster                                                         |
| async_tree_io              | 843 ms                                                       | 653 ms: 1.29x faster                                                         |
| async_tree_none            | 376 ms                                                       | 295 ms: 1.28x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 660 ms: 1.26x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 275 ms: 1.26x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 520 ms: 1.16x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 501 ms: 1.16x faster                                                         |
| async_generators           | 457 ms                                                       | 423 ms: 1.08x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.02x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.20x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 71.7 ms: 1.13x faster                                                        |
| pidigits       | 252 ms                                                       | 254 ms: 1.01x slower                                                         |
| nbody          | 89.3 ms                                                      | 109 ms: 1.22x slower                                                         |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.02 ms: 1.22x faster                                                        |
| regex_v8       | 26.1 ms                                                      | 24.3 ms: 1.07x faster                                                        |
| regex_dna      | 247 ms                                                       | 235 ms: 1.05x faster                                                         |
| regex_compile  | 143 ms                                                       | 136 ms: 1.05x faster                                                         |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.22 sec: 1.11x faster                                                       |
| xml_etree_parse      | 150 ms                                                       | 138 ms: 1.09x faster                                                         |
| xml_etree_iterparse  | 103 ms                                                       | 98.0 ms: 1.05x faster                                                        |
| xml_etree_generate   | 86.5 ms                                                      | 85.2 ms: 1.02x faster                                                        |
| xml_etree_process    | 61.2 ms                                                      | 60.3 ms: 1.01x faster                                                        |
| unpickle_pure_python | 217 us                                                       | 220 us: 1.01x slower                                                         |
| json_dumps           | 11.1 ms                                                      | 11.5 ms: 1.03x slower                                                        |
| pickle_pure_python   | 323 us                                                       | 337 us: 1.04x slower                                                         |
| json_loads           | 24.7 us                                                      | 26.4 us: 1.07x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 16.4 ms: 1.03x slower                                                        |
| python_startup_no_site | 8.96 ms                                                      | 10.5 ms: 1.17x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 24.6 ms: 1.07x faster                                                        |
| genshi_xml      | 57.1 ms                                                      | 56.3 ms: 1.01x faster                                                        |
| django_template | 36.4 ms                                                      | 37.4 ms: 1.03x slower                                                        |
| mako            | 10.4 ms                                                      | 10.9 ms: 1.05x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.00x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 332 ms: 1.40x faster                                                         |
| deepcopy                   | 392 us                                                       | 294 us: 1.33x faster                                                         |
| deepcopy_memo              | 38.6 us                                                      | 29.1 us: 1.33x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 343 ms: 1.32x faster                                                         |
| async_tree_io              | 843 ms                                                       | 653 ms: 1.29x faster                                                         |
| async_tree_none            | 376 ms                                                       | 295 ms: 1.28x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 660 ms: 1.26x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 275 ms: 1.26x faster                                                         |
| regex_effbot               | 3.67 ms                                                      | 3.02 ms: 1.22x faster                                                        |
| go                         | 162 ms                                                       | 134 ms: 1.21x faster                                                         |
| deepcopy_reduce            | 3.54 us                                                      | 2.98 us: 1.19x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 520 ms: 1.16x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 501 ms: 1.16x faster                                                         |
| generators                 | 33.6 ms                                                      | 29.2 ms: 1.15x faster                                                        |
| float                      | 81.3 ms                                                      | 71.7 ms: 1.13x faster                                                        |
| scimark_sor                | 123 ms                                                       | 109 ms: 1.13x faster                                                         |
| tomli_loads                | 2.46 sec                                                     | 2.22 sec: 1.11x faster                                                       |
| dulwich_log                | 68.2 ms                                                      | 62.3 ms: 1.09x faster                                                        |
| xml_etree_parse            | 150 ms                                                       | 138 ms: 1.09x faster                                                         |
| pylint                     | 347 ms                                                       | 318 ms: 1.09x faster                                                         |
| richards                   | 52.9 ms                                                      | 48.7 ms: 1.09x faster                                                        |
| telco                      | 8.79 ms                                                      | 8.10 ms: 1.08x faster                                                        |
| spectral_norm              | 97.0 ms                                                      | 89.8 ms: 1.08x faster                                                        |
| async_generators           | 457 ms                                                       | 423 ms: 1.08x faster                                                         |
| richards_super             | 59.6 ms                                                      | 55.2 ms: 1.08x faster                                                        |
| regex_v8                   | 26.1 ms                                                      | 24.3 ms: 1.07x faster                                                        |
| pyflate                    | 503 ms                                                       | 468 ms: 1.07x faster                                                         |
| genshi_text                | 26.2 ms                                                      | 24.6 ms: 1.07x faster                                                        |
| html5lib                   | 73.5 ms                                                      | 69.0 ms: 1.07x faster                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 4.82 sec: 1.06x faster                                                       |
| json                       | 5.69 ms                                                      | 5.40 ms: 1.05x faster                                                        |
| regex_dna                  | 247 ms                                                       | 235 ms: 1.05x faster                                                         |
| logging_silent             | 97.9 ns                                                      | 93.2 ns: 1.05x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 98.0 ms: 1.05x faster                                                        |
| regex_compile              | 143 ms                                                       | 136 ms: 1.05x faster                                                         |
| scimark_fft                | 328 ms                                                       | 314 ms: 1.04x faster                                                         |
| thrift                     | 901 us                                                       | 865 us: 1.04x faster                                                         |
| pprint_pformat             | 1.72 sec                                                     | 1.65 sec: 1.04x faster                                                       |
| sympy_integrate            | 23.6 ms                                                      | 22.8 ms: 1.03x faster                                                        |
| pprint_safe_repr           | 843 ms                                                       | 817 ms: 1.03x faster                                                         |
| sqlite_synth               | 2.91 us                                                      | 2.83 us: 1.03x faster                                                        |
| pathlib                    | 17.5 ms                                                      | 17.1 ms: 1.02x faster                                                        |
| scimark_monte_carlo        | 66.1 ms                                                      | 64.7 ms: 1.02x faster                                                        |
| sympy_expand               | 509 ms                                                       | 499 ms: 1.02x faster                                                         |
| mdp                        | 2.54 sec                                                     | 2.49 sec: 1.02x faster                                                       |
| 2to3                       | 293 ms                                                       | 287 ms: 1.02x faster                                                         |
| sqlalchemy_declarative     | 148 ms                                                       | 146 ms: 1.02x faster                                                         |
| sympy_str                  | 298 ms                                                       | 293 ms: 1.02x faster                                                         |
| deltablue                  | 3.42 ms                                                      | 3.36 ms: 1.02x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.02x faster                                                        |
| xml_etree_generate         | 86.5 ms                                                      | 85.2 ms: 1.02x faster                                                        |
| xml_etree_process          | 61.2 ms                                                      | 60.3 ms: 1.01x faster                                                        |
| k_core                     | 2.17 sec                                                     | 2.14 sec: 1.01x faster                                                       |
| genshi_xml                 | 57.1 ms                                                      | 56.3 ms: 1.01x faster                                                        |
| sphinx                     | 1.12 sec                                                     | 1.11 sec: 1.01x faster                                                       |
| sqlalchemy_imperative      | 18.3 ms                                                      | 18.1 ms: 1.01x faster                                                        |
| meteor_contest             | 130 ms                                                       | 128 ms: 1.01x faster                                                         |
| hexiom                     | 6.55 ms                                                      | 6.49 ms: 1.01x faster                                                        |
| sympy_sum                  | 155 ms                                                       | 154 ms: 1.00x faster                                                         |
| pidigits                   | 252 ms                                                       | 254 ms: 1.01x slower                                                         |
| connected_components       | 432 ms                                                       | 437 ms: 1.01x slower                                                         |
| unpickle_pure_python       | 217 us                                                       | 220 us: 1.01x slower                                                         |
| scimark_lu                 | 98.7 ms                                                      | 101 ms: 1.02x slower                                                         |
| python_startup             | 15.9 ms                                                      | 16.4 ms: 1.03x slower                                                        |
| django_template            | 36.4 ms                                                      | 37.4 ms: 1.03x slower                                                        |
| json_dumps                 | 11.1 ms                                                      | 11.5 ms: 1.03x slower                                                        |
| pycparser                  | 1.24 sec                                                     | 1.28 sec: 1.03x slower                                                       |
| docutils                   | 2.83 sec                                                     | 2.92 sec: 1.03x slower                                                       |
| raytrace                   | 273 ms                                                       | 284 ms: 1.04x slower                                                         |
| logging_simple             | 6.39 us                                                      | 6.65 us: 1.04x slower                                                        |
| comprehensions             | 17.0 us                                                      | 17.7 us: 1.04x slower                                                        |
| pickle_pure_python         | 323 us                                                       | 337 us: 1.04x slower                                                         |
| logging_format             | 6.94 us                                                      | 7.27 us: 1.05x slower                                                        |
| create_gc_cycles           | 2.68 ms                                                      | 2.82 ms: 1.05x slower                                                        |
| nqueens                    | 90.7 ms                                                      | 95.3 ms: 1.05x slower                                                        |
| mako                       | 10.4 ms                                                      | 10.9 ms: 1.05x slower                                                        |
| typing_runtime_protocols   | 169 us                                                       | 178 us: 1.06x slower                                                         |
| fannkuch                   | 363 ms                                                       | 384 ms: 1.06x slower                                                         |
| chaos                      | 60.2 ms                                                      | 63.7 ms: 1.06x slower                                                        |
| json_loads                 | 24.7 us                                                      | 26.4 us: 1.07x slower                                                        |
| many_optionals             | 930 us                                                       | 1.04 ms: 1.12x slower                                                        |
| crypto_pyaes               | 73.3 ms                                                      | 84.6 ms: 1.15x slower                                                        |
| python_startup_no_site     | 8.96 ms                                                      | 10.5 ms: 1.17x slower                                                        |
| nbody                      | 89.3 ms                                                      | 109 ms: 1.22x slower                                                         |
| subparsers                 | 17.5 ms                                                      | 23.6 ms: 1.35x slower                                                        |
| gc_traversal               | 4.74 ms                                                      | 6.62 ms: 1.40x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 957 ms: 186.79x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                                 |

Benchmark hidden because not significant (5): asyncio_websockets, shortest_path, scimark_sparse_mat_mult, coverage, bench_thread_pool
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.034x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x