# Results vs. 3.13.0

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: linux-aarch64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.096x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 363 ms: 1.16x slower                                                     |
| docutils       | 2.96 sec                                                 | 3.25 sec: 1.10x slower                                                   |
| html5lib       | 65.6 ms                                                  | 74.1 ms: 1.13x slower                                                    |
| sphinx         | 1.20 sec                                                 | 1.32 sec: 1.10x slower                                                   |
| Geometric mean | (ref)                                                    | 1.12x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 455 ms: 1.46x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 844 ms: 1.38x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 499 ms: 1.33x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 369 ms: 1.31x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 885 ms: 1.29x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 647 ms: 1.24x faster                                                     |
| async_tree_none            | 504 ms                                                   | 415 ms: 1.21x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 679 ms: 1.16x faster                                                     |
| async_generators           | 500 ms                                                   | 525 ms: 1.05x slower                                                     |
| Geometric mean             | (ref)                                                    | 1.20x faster                                                             |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 102 ms: 1.07x slower                                                     |
| nbody          | 118 ms                                                   | 186 ms: 1.57x slower                                                     |
| Geometric mean | (ref)                                                    | 1.18x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.96 ms: 1.29x faster                                                    |
| regex_v8       | 32.5 ms                                                  | 27.6 ms: 1.18x faster                                                    |
| regex_dna      | 263 ms                                                   | 246 ms: 1.07x faster                                                     |
| regex_compile  | 134 ms                                                   | 161 ms: 1.21x slower                                                     |
| Geometric mean | (ref)                                                    | 1.08x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_iterparse  | 159 ms                                                   | 130 ms: 1.22x faster                                                     |
| xml_etree_parse      | 203 ms                                                   | 176 ms: 1.15x faster                                                     |
| json_dumps           | 14.2 ms                                                  | 16.0 ms: 1.13x slower                                                    |
| xml_etree_generate   | 118 ms                                                   | 135 ms: 1.14x slower                                                     |
| tomli_loads          | 2.67 sec                                                 | 3.09 sec: 1.16x slower                                                   |
| json_loads           | 32.8 us                                                  | 38.2 us: 1.16x slower                                                    |
| unpickle_pure_python | 265 us                                                   | 308 us: 1.17x slower                                                     |
| pickle_pure_python   | 374 us                                                   | 441 us: 1.18x slower                                                     |
| xml_etree_process    | 82.1 ms                                                  | 98.0 ms: 1.19x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.08x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 19.5 ms: 1.21x slower                                                    |
| python_startup_no_site | 8.79 ms                                                  | 14.4 ms: 1.64x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.41x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 61.6 ms                                                  | 76.7 ms: 1.25x slower                                                    |
| genshi_text     | 28.6 ms                                                  | 36.1 ms: 1.26x slower                                                    |
| django_template | 39.4 ms                                                  | 53.7 ms: 1.36x slower                                                    |
| mako            | 14.0 ms                                                  | 22.1 ms: 1.58x slower                                                    |
| Geometric mean  | (ref)                                                    | 1.36x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| gc_traversal               | 5.92 ms                                                  | 2.72 ms: 2.18x faster                                                    |
| create_gc_cycles           | 3.39 ms                                                  | 2.10 ms: 1.61x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 455 ms: 1.46x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 844 ms: 1.38x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 499 ms: 1.33x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 369 ms: 1.31x faster                                                     |
| regex_effbot               | 5.10 ms                                                  | 3.96 ms: 1.29x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 885 ms: 1.29x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 647 ms: 1.24x faster                                                     |
| xml_etree_iterparse        | 159 ms                                                   | 130 ms: 1.22x faster                                                     |
| async_tree_none            | 504 ms                                                   | 415 ms: 1.21x faster                                                     |
| regex_v8                   | 32.5 ms                                                  | 27.6 ms: 1.18x faster                                                    |
| sqlite_synth               | 4.08 us                                                  | 3.49 us: 1.17x faster                                                    |
| deepcopy                   | 479 us                                                   | 412 us: 1.16x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 679 ms: 1.16x faster                                                     |
| xml_etree_parse            | 203 ms                                                   | 176 ms: 1.15x faster                                                     |
| regex_dna                  | 263 ms                                                   | 246 ms: 1.07x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 50.4 us: 1.05x faster                                                    |
| pycparser                  | 1.34 sec                                                 | 1.39 sec: 1.04x slower                                                   |
| scimark_fft                | 463 ms                                                   | 482 ms: 1.04x slower                                                     |
| go                         | 164 ms                                                   | 171 ms: 1.04x slower                                                     |
| scimark_sor                | 164 ms                                                   | 172 ms: 1.05x slower                                                     |
| async_generators           | 500 ms                                                   | 525 ms: 1.05x slower                                                     |
| k_core                     | 2.99 sec                                                 | 3.17 sec: 1.06x slower                                                   |
| float                      | 95.8 ms                                                  | 102 ms: 1.07x slower                                                     |
| pyflate                    | 582 ms                                                   | 622 ms: 1.07x slower                                                     |
| logging_silent             | 135 ns                                                   | 146 ns: 1.08x slower                                                     |
| mdp                        | 3.45 sec                                                 | 3.74 sec: 1.09x slower                                                   |
| pylint                     | 345 ms                                                   | 375 ms: 1.09x slower                                                     |
| docutils                   | 2.96 sec                                                 | 3.25 sec: 1.10x slower                                                   |
| sphinx                     | 1.20 sec                                                 | 1.32 sec: 1.10x slower                                                   |
| json                       | 5.94 ms                                                  | 6.58 ms: 1.11x slower                                                    |
| telco                      | 10.5 ms                                                  | 11.7 ms: 1.12x slower                                                    |
| json_dumps                 | 14.2 ms                                                  | 16.0 ms: 1.13x slower                                                    |
| html5lib                   | 65.6 ms                                                  | 74.1 ms: 1.13x slower                                                    |
| pprint_pformat             | 1.99 sec                                                 | 2.26 sec: 1.14x slower                                                   |
| xml_etree_generate         | 118 ms                                                   | 135 ms: 1.14x slower                                                     |
| thrift                     | 1.01 ms                                                  | 1.16 ms: 1.14x slower                                                    |
| pprint_safe_repr           | 962 ms                                                   | 1.10 sec: 1.14x slower                                                   |
| tomli_loads                | 2.67 sec                                                 | 3.09 sec: 1.16x slower                                                   |
| 2to3                       | 313 ms                                                   | 363 ms: 1.16x slower                                                     |
| json_loads                 | 32.8 us                                                  | 38.2 us: 1.16x slower                                                    |
| unpickle_pure_python       | 265 us                                                   | 308 us: 1.17x slower                                                     |
| logging_simple             | 7.25 us                                                  | 8.54 us: 1.18x slower                                                    |
| pickle_pure_python         | 374 us                                                   | 441 us: 1.18x slower                                                     |
| logging_format             | 8.10 us                                                  | 9.57 us: 1.18x slower                                                    |
| xml_etree_process          | 82.1 ms                                                  | 98.0 ms: 1.19x slower                                                    |
| shortest_path              | 565 ms                                                   | 675 ms: 1.19x slower                                                     |
| connected_components       | 547 ms                                                   | 656 ms: 1.20x slower                                                     |
| chaos                      | 70.7 ms                                                  | 85.1 ms: 1.20x slower                                                    |
| regex_compile              | 134 ms                                                   | 161 ms: 1.21x slower                                                     |
| bpe_tokeniser              | 6.02 sec                                                 | 7.26 sec: 1.21x slower                                                   |
| python_startup             | 16.0 ms                                                  | 19.5 ms: 1.21x slower                                                    |
| nqueens                    | 105 ms                                                   | 129 ms: 1.23x slower                                                     |
| sympy_sum                  | 151 ms                                                   | 187 ms: 1.24x slower                                                     |
| sympy_integrate            | 21.4 ms                                                  | 26.6 ms: 1.24x slower                                                    |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 8.27 ms: 1.24x slower                                                    |
| genshi_xml                 | 61.6 ms                                                  | 76.7 ms: 1.25x slower                                                    |
| sympy_expand               | 472 ms                                                   | 592 ms: 1.25x slower                                                     |
| deltablue                  | 3.97 ms                                                  | 4.98 ms: 1.26x slower                                                    |
| scimark_monte_carlo        | 87.8 ms                                                  | 110 ms: 1.26x slower                                                     |
| sqlalchemy_declarative     | 154 ms                                                   | 194 ms: 1.26x slower                                                     |
| genshi_text                | 28.6 ms                                                  | 36.1 ms: 1.26x slower                                                    |
| hexiom                     | 7.34 ms                                                  | 9.31 ms: 1.27x slower                                                    |
| scimark_lu                 | 146 ms                                                   | 187 ms: 1.28x slower                                                     |
| meteor_contest             | 117 ms                                                   | 151 ms: 1.29x slower                                                     |
| comprehensions             | 20.8 us                                                  | 26.9 us: 1.29x slower                                                    |
| richards                   | 54.5 ms                                                  | 70.6 ms: 1.30x slower                                                    |
| crypto_pyaes               | 84.9 ms                                                  | 111 ms: 1.31x slower                                                     |
| raytrace                   | 310 ms                                                   | 406 ms: 1.31x slower                                                     |
| sqlalchemy_imperative      | 16.1 ms                                                  | 21.2 ms: 1.32x slower                                                    |
| typing_runtime_protocols   | 197 us                                                   | 262 us: 1.33x slower                                                     |
| sympy_str                  | 265 ms                                                   | 354 ms: 1.34x slower                                                     |
| coverage                   | 106 ms                                                   | 142 ms: 1.34x slower                                                     |
| richards_super             | 60.8 ms                                                  | 82.8 ms: 1.36x slower                                                    |
| django_template            | 39.4 ms                                                  | 53.7 ms: 1.36x slower                                                    |
| fannkuch                   | 478 ms                                                   | 652 ms: 1.36x slower                                                     |
| bench_thread_pool          | 1.34 ms                                                  | 1.84 ms: 1.37x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 31.7 ms: 1.56x slower                                                    |
| nbody                      | 118 ms                                                   | 186 ms: 1.57x slower                                                     |
| mako                       | 14.0 ms                                                  | 22.1 ms: 1.58x slower                                                    |
| many_optionals             | 626 us                                                   | 1.02 ms: 1.62x slower                                                    |
| python_startup_no_site     | 8.79 ms                                                  | 14.4 ms: 1.64x slower                                                    |
| bench_mp_pool              | 8.07 ms                                                  | 57.7 ms: 7.16x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.12x slower                                                             |

Benchmark hidden because not significant (7): pathlib, spectral_norm, pidigits, asyncio_websockets, coroutines, generators, deepcopy_reduce
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250322-3.14.0a6+-bc26f95-NOGIL/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.096x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: 1.25x