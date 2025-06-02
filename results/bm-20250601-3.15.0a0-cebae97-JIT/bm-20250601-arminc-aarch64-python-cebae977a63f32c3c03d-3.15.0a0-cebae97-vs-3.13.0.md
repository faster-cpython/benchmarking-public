# Results vs. 3.13.0

- fork: python
- ref: cebae977a63f32c3c03d
- machine: linux-aarch64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.062x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 366 ms: 1.17x slower                                                    |
| docutils       | 2.96 sec                                                 | 3.61 sec: 1.22x slower                                                  |
| html5lib       | 65.6 ms                                                  | 69.6 ms: 1.06x slower                                                   |
| sphinx         | 1.20 sec                                                 | 1.38 sec: 1.15x slower                                                  |
| Geometric mean | (ref)                                                    | 1.15x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|---------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization    | 664 ms                                                   | 528 ms: 1.26x faster                                                    |
| async_tree_memoization_tg | 663 ms                                                   | 527 ms: 1.26x faster                                                    |
| async_tree_none_tg        | 484 ms                                                   | 427 ms: 1.13x faster                                                    |
| async_tree_io_tg          | 1.16 sec                                                 | 1.03 sec: 1.13x faster                                                  |
| async_tree_io             | 1.14 sec                                                 | 1.01 sec: 1.13x faster                                                  |
| async_tree_none           | 504 ms                                                   | 449 ms: 1.12x faster                                                    |
| async_tree_cpu_io_mixed   | 789 ms                                                   | 825 ms: 1.05x slower                                                    |
| async_generators          | 500 ms                                                   | 542 ms: 1.08x slower                                                    |
| coroutines                | 29.4 ms                                                  | 33.9 ms: 1.15x slower                                                   |
| Geometric mean            | (ref)                                                    | 1.06x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 91.6 ms: 1.05x faster                                                   |
| pidigits       | 238 ms                                                   | 276 ms: 1.16x slower                                                    |
| nbody          | 118 ms                                                   | 138 ms: 1.17x slower                                                    |
| Geometric mean | (ref)                                                    | 1.09x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.08 ms: 1.25x faster                                                   |
| regex_dna      | 263 ms                                                   | 226 ms: 1.16x faster                                                    |
| regex_v8       | 32.5 ms                                                  | 30.7 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                    | 1.16x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse  | 159 ms                                                   | 171 ms: 1.07x slower                                                    |
| xml_etree_parse      | 203 ms                                                   | 227 ms: 1.12x slower                                                    |
| json_loads           | 32.8 us                                                  | 38.0 us: 1.16x slower                                                   |
| unpickle_pure_python | 265 us                                                   | 311 us: 1.17x slower                                                    |
| json_dumps           | 14.2 ms                                                  | 16.7 ms: 1.18x slower                                                   |
| xml_etree_generate   | 118 ms                                                   | 149 ms: 1.26x slower                                                    |
| xml_etree_process    | 82.1 ms                                                  | 105 ms: 1.28x slower                                                    |
| pickle_pure_python   | 374 us                                                   | 488 us: 1.31x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.17x slower                                                            |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 17.0 ms: 1.06x slower                                                   |
| python_startup_no_site | 8.79 ms                                                  | 9.68 ms: 1.10x slower                                                   |
| Geometric mean         | (ref)                                                    | 1.08x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 28.6 ms                                                  | 32.9 ms: 1.15x slower                                                   |
| genshi_xml      | 61.6 ms                                                  | 75.9 ms: 1.23x slower                                                   |
| mako            | 14.0 ms                                                  | 17.5 ms: 1.25x slower                                                   |
| django_template | 39.4 ms                                                  | 53.4 ms: 1.35x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.25x slower                                                            |

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|---------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pprint_pformat            | 1.99 sec                                                 | 2.43 us: 816837.04x faster                                              |
| pprint_safe_repr          | 962 ms                                                   | 1.50 us: 640241.58x faster                                              |
| mdp                       | 3.45 sec                                                 | 1.98 sec: 1.74x faster                                                  |
| async_tree_memoization    | 664 ms                                                   | 528 ms: 1.26x faster                                                    |
| async_tree_memoization_tg | 663 ms                                                   | 527 ms: 1.26x faster                                                    |
| regex_effbot              | 5.10 ms                                                  | 4.08 ms: 1.25x faster                                                   |
| deepcopy_memo             | 53.0 us                                                  | 43.1 us: 1.23x faster                                                   |
| deepcopy                  | 479 us                                                   | 400 us: 1.20x faster                                                    |
| regex_dna                 | 263 ms                                                   | 226 ms: 1.16x faster                                                    |
| async_tree_none_tg        | 484 ms                                                   | 427 ms: 1.13x faster                                                    |
| async_tree_io_tg          | 1.16 sec                                                 | 1.03 sec: 1.13x faster                                                  |
| async_tree_io             | 1.14 sec                                                 | 1.01 sec: 1.13x faster                                                  |
| async_tree_none           | 504 ms                                                   | 449 ms: 1.12x faster                                                    |
| regex_v8                  | 32.5 ms                                                  | 30.7 ms: 1.06x faster                                                   |
| richards                  | 54.5 ms                                                  | 51.6 ms: 1.06x faster                                                   |
| float                     | 95.8 ms                                                  | 91.6 ms: 1.05x faster                                                   |
| pyflate                   | 582 ms                                                   | 598 ms: 1.03x slower                                                    |
| connected_components      | 547 ms                                                   | 569 ms: 1.04x slower                                                    |
| async_tree_cpu_io_mixed   | 789 ms                                                   | 825 ms: 1.05x slower                                                    |
| spectral_norm             | 143 ms                                                   | 150 ms: 1.05x slower                                                    |
| go                        | 164 ms                                                   | 172 ms: 1.05x slower                                                    |
| shortest_path             | 565 ms                                                   | 594 ms: 1.05x slower                                                    |
| scimark_fft               | 463 ms                                                   | 489 ms: 1.06x slower                                                    |
| html5lib                  | 65.6 ms                                                  | 69.6 ms: 1.06x slower                                                   |
| python_startup            | 16.0 ms                                                  | 17.0 ms: 1.06x slower                                                   |
| deepcopy_reduce           | 4.24 us                                                  | 4.51 us: 1.06x slower                                                   |
| xml_etree_iterparse       | 159 ms                                                   | 171 ms: 1.07x slower                                                    |
| scimark_sor               | 164 ms                                                   | 176 ms: 1.07x slower                                                    |
| bpe_tokeniser             | 6.02 sec                                                 | 6.48 sec: 1.08x slower                                                  |
| deltablue                 | 3.97 ms                                                  | 4.28 ms: 1.08x slower                                                   |
| async_generators          | 500 ms                                                   | 542 ms: 1.08x slower                                                    |
| pylint                    | 345 ms                                                   | 375 ms: 1.09x slower                                                    |
| python_startup_no_site    | 8.79 ms                                                  | 9.68 ms: 1.10x slower                                                   |
| scimark_monte_carlo       | 87.8 ms                                                  | 97.3 ms: 1.11x slower                                                   |
| meteor_contest            | 117 ms                                                   | 130 ms: 1.12x slower                                                    |
| pathlib                   | 24.3 ms                                                  | 27.3 ms: 1.12x slower                                                   |
| xml_etree_parse           | 203 ms                                                   | 227 ms: 1.12x slower                                                    |
| sympy_integrate           | 21.4 ms                                                  | 24.2 ms: 1.13x slower                                                   |
| create_gc_cycles          | 3.39 ms                                                  | 3.88 ms: 1.14x slower                                                   |
| sphinx                    | 1.20 sec                                                 | 1.38 sec: 1.15x slower                                                  |
| bench_thread_pool         | 1.34 ms                                                  | 1.53 ms: 1.15x slower                                                   |
| coroutines                | 29.4 ms                                                  | 33.9 ms: 1.15x slower                                                   |
| json                      | 5.94 ms                                                  | 6.84 ms: 1.15x slower                                                   |
| genshi_text               | 28.6 ms                                                  | 32.9 ms: 1.15x slower                                                   |
| json_loads                | 32.8 us                                                  | 38.0 us: 1.16x slower                                                   |
| pidigits                  | 238 ms                                                   | 276 ms: 1.16x slower                                                    |
| nbody                     | 118 ms                                                   | 138 ms: 1.17x slower                                                    |
| 2to3                      | 313 ms                                                   | 366 ms: 1.17x slower                                                    |
| unpickle_pure_python      | 265 us                                                   | 311 us: 1.17x slower                                                    |
| json_dumps                | 14.2 ms                                                  | 16.7 ms: 1.18x slower                                                   |
| sqlite_synth              | 4.08 us                                                  | 4.81 us: 1.18x slower                                                   |
| chaos                     | 70.7 ms                                                  | 83.9 ms: 1.19x slower                                                   |
| sympy_sum                 | 151 ms                                                   | 180 ms: 1.19x slower                                                    |
| hexiom                    | 7.34 ms                                                  | 8.76 ms: 1.19x slower                                                   |
| scimark_sparse_mat_mult   | 6.66 ms                                                  | 7.98 ms: 1.20x slower                                                   |
| pycparser                 | 1.34 sec                                                 | 1.63 sec: 1.21x slower                                                  |
| docutils                  | 2.96 sec                                                 | 3.61 sec: 1.22x slower                                                  |
| fannkuch                  | 478 ms                                                   | 588 ms: 1.23x slower                                                    |
| genshi_xml                | 61.6 ms                                                  | 75.9 ms: 1.23x slower                                                   |
| mako                      | 14.0 ms                                                  | 17.5 ms: 1.25x slower                                                   |
| xml_etree_generate        | 118 ms                                                   | 149 ms: 1.26x slower                                                    |
| logging_format            | 8.10 us                                                  | 10.2 us: 1.26x slower                                                   |
| gc_traversal              | 5.92 ms                                                  | 7.50 ms: 1.27x slower                                                   |
| comprehensions            | 20.8 us                                                  | 26.5 us: 1.27x slower                                                   |
| crypto_pyaes              | 84.9 ms                                                  | 108 ms: 1.27x slower                                                    |
| xml_etree_process         | 82.1 ms                                                  | 105 ms: 1.28x slower                                                    |
| sympy_str                 | 265 ms                                                   | 340 ms: 1.28x slower                                                    |
| scimark_lu                | 146 ms                                                   | 187 ms: 1.28x slower                                                    |
| nqueens                   | 105 ms                                                   | 135 ms: 1.28x slower                                                    |
| raytrace                  | 310 ms                                                   | 399 ms: 1.29x slower                                                    |
| telco                     | 10.5 ms                                                  | 13.5 ms: 1.30x slower                                                   |
| logging_simple            | 7.25 us                                                  | 9.46 us: 1.31x slower                                                   |
| pickle_pure_python        | 374 us                                                   | 488 us: 1.31x slower                                                    |
| sympy_expand              | 472 ms                                                   | 622 ms: 1.32x slower                                                    |
| typing_runtime_protocols  | 197 us                                                   | 262 us: 1.33x slower                                                    |
| django_template           | 39.4 ms                                                  | 53.4 ms: 1.35x slower                                                   |
| many_optionals            | 626 us                                                   | 1.13 ms: 1.81x slower                                                   |
| subparsers                | 20.3 ms                                                  | 37.2 ms: 1.83x slower                                                   |
| logging_silent            | 135 ns                                                   | 898 ns: 6.67x slower                                                    |
| coverage                  | 106 ms                                                   | 729 ms: 6.90x slower                                                    |
| thrift                    | 1.01 ms                                                  | 200 ms: 197.96x slower                                                  |
| bench_mp_pool             | 8.07 ms                                                  | 2.87 sec: 355.40x slower                                                |
| Geometric mean            | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (6): asyncio_websockets, generators, k_core, richards_super, tomli_loads, async_tree_cpu_io_mixed_tg
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, regex_compile, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.062x faster

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: 1.09x