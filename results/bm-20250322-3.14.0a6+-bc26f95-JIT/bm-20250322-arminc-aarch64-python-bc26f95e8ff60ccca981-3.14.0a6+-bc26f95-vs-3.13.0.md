# Results vs. 3.13.0

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: linux-aarch64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.014x faster
- HPT reliability: 64.84%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.17 sec: 1.07x slower                                                   |
| html5lib       | 65.6 ms                                                  | 63.9 ms: 1.03x faster                                                    |
| sphinx         | 1.20 sec                                                 | 1.17 sec: 1.02x faster                                                   |
| Geometric mean | (ref)                                                    | 1.00x slower                                                             |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 464 ms: 1.43x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 471 ms: 1.41x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 371 ms: 1.31x faster                                                     |
| async_tree_none            | 504 ms                                                   | 387 ms: 1.30x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 880 ms: 1.29x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 919 ms: 1.27x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 656 ms: 1.22x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 663 ms: 1.19x faster                                                     |
| async_generators           | 500 ms                                                   | 478 ms: 1.05x faster                                                     |
| Geometric mean             | (ref)                                                    | 1.22x faster                                                             |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 85.3 ms: 1.12x faster                                                    |
| nbody          | 118 ms                                                   | 129 ms: 1.09x slower                                                     |
| Geometric mean | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.92 ms: 1.30x faster                                                    |
| regex_v8       | 32.5 ms                                                  | 28.1 ms: 1.16x faster                                                    |
| regex_dna      | 263 ms                                                   | 238 ms: 1.10x faster                                                     |
| Geometric mean | (ref)                                                    | 1.15x faster                                                             |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 203 ms                                                   | 178 ms: 1.14x faster                                                     |
| xml_etree_iterparse  | 159 ms                                                   | 141 ms: 1.12x faster                                                     |
| tomli_loads          | 2.67 sec                                                 | 2.46 sec: 1.09x faster                                                   |
| xml_etree_generate   | 118 ms                                                   | 110 ms: 1.08x faster                                                     |
| xml_etree_process    | 82.1 ms                                                  | 78.5 ms: 1.05x faster                                                    |
| unpickle_pure_python | 265 us                                                   | 288 us: 1.09x slower                                                     |
| pickle_pure_python   | 374 us                                                   | 406 us: 1.09x slower                                                     |
| Geometric mean       | (ref)                                                    | 1.03x faster                                                             |

Benchmark hidden because not significant (2): json_dumps, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 10.2 ms: 1.16x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.08x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 39.4 ms                                                  | 40.1 ms: 1.02x slower                                                    |
| Geometric mean  | (ref)                                                    | 1.00x faster                                                             |

Benchmark hidden because not significant (3): genshi_text, mako, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 464 ms: 1.43x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 37.4 us: 1.42x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 471 ms: 1.41x faster                                                     |
| deepcopy                   | 479 us                                                   | 349 us: 1.37x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 371 ms: 1.31x faster                                                     |
| regex_effbot               | 5.10 ms                                                  | 3.92 ms: 1.30x faster                                                    |
| async_tree_none            | 504 ms                                                   | 387 ms: 1.30x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 880 ms: 1.29x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 919 ms: 1.27x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 656 ms: 1.22x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 663 ms: 1.19x faster                                                     |
| regex_v8                   | 32.5 ms                                                  | 28.1 ms: 1.16x faster                                                    |
| xml_etree_parse            | 203 ms                                                   | 178 ms: 1.14x faster                                                     |
| xml_etree_iterparse        | 159 ms                                                   | 141 ms: 1.12x faster                                                     |
| float                      | 95.8 ms                                                  | 85.3 ms: 1.12x faster                                                    |
| scimark_sor                | 164 ms                                                   | 148 ms: 1.11x faster                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 3.83 us: 1.11x faster                                                    |
| regex_dna                  | 263 ms                                                   | 238 ms: 1.10x faster                                                     |
| richards_super             | 60.8 ms                                                  | 55.3 ms: 1.10x faster                                                    |
| sqlite_synth               | 4.08 us                                                  | 3.74 us: 1.09x faster                                                    |
| tomli_loads                | 2.67 sec                                                 | 2.46 sec: 1.09x faster                                                   |
| pathlib                    | 24.3 ms                                                  | 22.5 ms: 1.08x faster                                                    |
| xml_etree_generate         | 118 ms                                                   | 110 ms: 1.08x faster                                                     |
| coverage                   | 106 ms                                                   | 98.2 ms: 1.08x faster                                                    |
| generators                 | 40.3 ms                                                  | 37.5 ms: 1.07x faster                                                    |
| thrift                     | 1.01 ms                                                  | 941 us: 1.07x faster                                                     |
| spectral_norm              | 143 ms                                                   | 134 ms: 1.07x faster                                                     |
| richards                   | 54.5 ms                                                  | 51.0 ms: 1.07x faster                                                    |
| logging_format             | 8.10 us                                                  | 7.60 us: 1.07x faster                                                    |
| scimark_fft                | 463 ms                                                   | 435 ms: 1.06x faster                                                     |
| pylint                     | 345 ms                                                   | 325 ms: 1.06x faster                                                     |
| telco                      | 10.5 ms                                                  | 9.88 ms: 1.06x faster                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 5.73 sec: 1.05x faster                                                   |
| logging_simple             | 7.25 us                                                  | 6.92 us: 1.05x faster                                                    |
| async_generators           | 500 ms                                                   | 478 ms: 1.05x faster                                                     |
| xml_etree_process          | 82.1 ms                                                  | 78.5 ms: 1.05x faster                                                    |
| k_core                     | 2.99 sec                                                 | 2.88 sec: 1.04x faster                                                   |
| mdp                        | 3.45 sec                                                 | 3.33 sec: 1.03x faster                                                   |
| html5lib                   | 65.6 ms                                                  | 63.9 ms: 1.03x faster                                                    |
| sphinx                     | 1.20 sec                                                 | 1.17 sec: 1.02x faster                                                   |
| django_template            | 39.4 ms                                                  | 40.1 ms: 1.02x slower                                                    |
| pyflate                    | 582 ms                                                   | 594 ms: 1.02x slower                                                     |
| connected_components       | 547 ms                                                   | 562 ms: 1.03x slower                                                     |
| shortest_path              | 565 ms                                                   | 587 ms: 1.04x slower                                                     |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 6.98 ms: 1.05x slower                                                    |
| raytrace                   | 310 ms                                                   | 326 ms: 1.05x slower                                                     |
| sympy_expand               | 472 ms                                                   | 498 ms: 1.05x slower                                                     |
| meteor_contest             | 117 ms                                                   | 124 ms: 1.06x slower                                                     |
| pycparser                  | 1.34 sec                                                 | 1.43 sec: 1.06x slower                                                   |
| sympy_str                  | 265 ms                                                   | 283 ms: 1.07x slower                                                     |
| nqueens                    | 105 ms                                                   | 112 ms: 1.07x slower                                                     |
| docutils                   | 2.96 sec                                                 | 3.17 sec: 1.07x slower                                                   |
| create_gc_cycles           | 3.39 ms                                                  | 3.65 ms: 1.08x slower                                                    |
| unpickle_pure_python       | 265 us                                                   | 288 us: 1.09x slower                                                     |
| pickle_pure_python         | 374 us                                                   | 406 us: 1.09x slower                                                     |
| nbody                      | 118 ms                                                   | 129 ms: 1.09x slower                                                     |
| go                         | 164 ms                                                   | 180 ms: 1.09x slower                                                     |
| gc_traversal               | 5.92 ms                                                  | 6.58 ms: 1.11x slower                                                    |
| typing_runtime_protocols   | 197 us                                                   | 222 us: 1.13x slower                                                     |
| fannkuch                   | 478 ms                                                   | 551 ms: 1.15x slower                                                     |
| python_startup_no_site     | 8.79 ms                                                  | 10.2 ms: 1.16x slower                                                    |
| hexiom                     | 7.34 ms                                                  | 8.57 ms: 1.17x slower                                                    |
| crypto_pyaes               | 84.9 ms                                                  | 102 ms: 1.20x slower                                                     |
| comprehensions             | 20.8 us                                                  | 26.0 us: 1.25x slower                                                    |
| pprint_safe_repr           | 962 ms                                                   | 1.25 sec: 1.30x slower                                                   |
| pprint_pformat             | 1.99 sec                                                 | 2.58 sec: 1.30x slower                                                   |
| subparsers                 | 20.3 ms                                                  | 26.9 ms: 1.32x slower                                                    |
| many_optionals             | 626 us                                                   | 877 us: 1.40x slower                                                     |
| bench_mp_pool              | 8.07 ms                                                  | 814 ms: 100.89x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.03x slower                                                             |

Benchmark hidden because not significant (22): regex_compile, genshi_text, coroutines, mako, logging_silent, sqlalchemy_declarative, scimark_lu, json_dumps, 2to3, json, asyncio_websockets, pidigits, scimark_monte_carlo, bench_thread_pool, python_startup, deltablue, chaos, sympy_sum, genshi_xml, sympy_integrate, sqlalchemy_imperative, json_loads
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.014x faster

# HPT report

- Reliability score: 64.84% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x