# Results vs. 3.13.0

- fork: python
- ref: cebae977a63f32c3c03d
- machine: linux-aarch64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.224x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 356 ms: 1.14x slower                                                    |
| docutils       | 2.96 sec                                                 | 3.45 sec: 1.16x slower                                                  |
| html5lib       | 65.6 ms                                                  | 67.3 ms: 1.03x slower                                                   |
| sphinx         | 1.20 sec                                                 | 1.36 sec: 1.13x slower                                                  |
| Geometric mean | (ref)                                                    | 1.11x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|---------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg | 663 ms                                                   | 524 ms: 1.27x faster                                                    |
| async_tree_memoization    | 664 ms                                                   | 525 ms: 1.26x faster                                                    |
| async_tree_io             | 1.14 sec                                                 | 987 ms: 1.15x faster                                                    |
| async_tree_none           | 504 ms                                                   | 441 ms: 1.14x faster                                                    |
| async_tree_io_tg          | 1.16 sec                                                 | 1.02 sec: 1.14x faster                                                  |
| async_tree_none_tg        | 484 ms                                                   | 427 ms: 1.13x faster                                                    |
| async_tree_cpu_io_mixed   | 789 ms                                                   | 808 ms: 1.02x slower                                                    |
| async_generators          | 500 ms                                                   | 521 ms: 1.04x slower                                                    |
| coroutines                | 29.4 ms                                                  | 33.1 ms: 1.13x slower                                                   |
| Geometric mean            | (ref)                                                    | 1.08x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 238 ms                                                   | 277 ms: 1.16x slower                                                    |
| nbody          | 118 ms                                                   | 144 ms: 1.21x slower                                                    |
| Geometric mean | (ref)                                                    | 1.12x slower                                                            |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.08 ms: 1.25x faster                                                   |
| regex_dna      | 263 ms                                                   | 226 ms: 1.16x faster                                                    |
| regex_v8       | 32.5 ms                                                  | 30.1 ms: 1.08x faster                                                   |
| regex_compile  | 134 ms                                                   | 158 ms: 1.19x slower                                                    |
| Geometric mean | (ref)                                                    | 1.07x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse  | 159 ms                                                   | 167 ms: 1.05x slower                                                    |
| tomli_loads          | 2.67 sec                                                 | 2.93 sec: 1.10x slower                                                  |
| xml_etree_parse      | 203 ms                                                   | 229 ms: 1.13x slower                                                    |
| json_loads           | 32.8 us                                                  | 38.0 us: 1.16x slower                                                   |
| json_dumps           | 14.2 ms                                                  | 17.2 ms: 1.21x slower                                                   |
| unpickle_pure_python | 265 us                                                   | 328 us: 1.24x slower                                                    |
| pickle_pure_python   | 374 us                                                   | 474 us: 1.27x slower                                                    |
| xml_etree_process    | 82.1 ms                                                  | 108 ms: 1.31x slower                                                    |
| xml_etree_generate   | 118 ms                                                   | 161 ms: 1.36x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.20x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 17.2 ms: 1.07x slower                                                   |
| python_startup_no_site | 8.79 ms                                                  | 9.71 ms: 1.10x slower                                                   |
| Geometric mean         | (ref)                                                    | 1.09x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 28.6 ms                                                  | 34.4 ms: 1.20x slower                                                   |
| genshi_xml      | 61.6 ms                                                  | 74.7 ms: 1.21x slower                                                   |
| mako            | 14.0 ms                                                  | 17.9 ms: 1.28x slower                                                   |
| django_template | 39.4 ms                                                  | 52.5 ms: 1.33x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.26x slower                                                            |

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|---------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                       | 3.45 sec                                                 | 2.01 sec: 1.71x faster                                                  |
| async_tree_memoization_tg | 663 ms                                                   | 524 ms: 1.27x faster                                                    |
| async_tree_memoization    | 664 ms                                                   | 525 ms: 1.26x faster                                                    |
| regex_effbot              | 5.10 ms                                                  | 4.08 ms: 1.25x faster                                                   |
| deepcopy_memo             | 53.0 us                                                  | 43.7 us: 1.21x faster                                                   |
| deepcopy                  | 479 us                                                   | 401 us: 1.20x faster                                                    |
| go                        | 164 ms                                                   | 141 ms: 1.17x faster                                                    |
| regex_dna                 | 263 ms                                                   | 226 ms: 1.16x faster                                                    |
| async_tree_io             | 1.14 sec                                                 | 987 ms: 1.15x faster                                                    |
| async_tree_none           | 504 ms                                                   | 441 ms: 1.14x faster                                                    |
| async_tree_io_tg          | 1.16 sec                                                 | 1.02 sec: 1.14x faster                                                  |
| async_tree_none_tg        | 484 ms                                                   | 427 ms: 1.13x faster                                                    |
| regex_v8                  | 32.5 ms                                                  | 30.1 ms: 1.08x faster                                                   |
| k_core                    | 2.99 sec                                                 | 2.93 sec: 1.02x faster                                                  |
| async_tree_cpu_io_mixed   | 789 ms                                                   | 808 ms: 1.02x slower                                                    |
| html5lib                  | 65.6 ms                                                  | 67.3 ms: 1.03x slower                                                   |
| async_generators          | 500 ms                                                   | 521 ms: 1.04x slower                                                    |
| connected_components      | 547 ms                                                   | 570 ms: 1.04x slower                                                    |
| spectral_norm             | 143 ms                                                   | 151 ms: 1.05x slower                                                    |
| xml_etree_iterparse       | 159 ms                                                   | 167 ms: 1.05x slower                                                    |
| scimark_sor               | 164 ms                                                   | 173 ms: 1.06x slower                                                    |
| shortest_path             | 565 ms                                                   | 599 ms: 1.06x slower                                                    |
| python_startup            | 16.0 ms                                                  | 17.2 ms: 1.07x slower                                                   |
| scimark_fft               | 463 ms                                                   | 500 ms: 1.08x slower                                                    |
| scimark_monte_carlo       | 87.8 ms                                                  | 94.8 ms: 1.08x slower                                                   |
| pylint                    | 345 ms                                                   | 374 ms: 1.08x slower                                                    |
| deepcopy_reduce           | 4.24 us                                                  | 4.61 us: 1.09x slower                                                   |
| meteor_contest            | 117 ms                                                   | 127 ms: 1.09x slower                                                    |
| tomli_loads               | 2.67 sec                                                 | 2.93 sec: 1.10x slower                                                  |
| bpe_tokeniser             | 6.02 sec                                                 | 6.64 sec: 1.10x slower                                                  |
| python_startup_no_site    | 8.79 ms                                                  | 9.71 ms: 1.10x slower                                                   |
| bench_thread_pool         | 1.34 ms                                                  | 1.48 ms: 1.11x slower                                                   |
| pathlib                   | 24.3 ms                                                  | 26.9 ms: 1.11x slower                                                   |
| comprehensions            | 20.8 us                                                  | 23.1 us: 1.11x slower                                                   |
| pycparser                 | 1.34 sec                                                 | 1.49 sec: 1.11x slower                                                  |
| sympy_integrate           | 21.4 ms                                                  | 23.9 ms: 1.12x slower                                                   |
| coroutines                | 29.4 ms                                                  | 33.1 ms: 1.13x slower                                                   |
| sphinx                    | 1.20 sec                                                 | 1.36 sec: 1.13x slower                                                  |
| xml_etree_parse           | 203 ms                                                   | 229 ms: 1.13x slower                                                    |
| 2to3                      | 313 ms                                                   | 356 ms: 1.14x slower                                                    |
| hexiom                    | 7.34 ms                                                  | 8.37 ms: 1.14x slower                                                   |
| deltablue                 | 3.97 ms                                                  | 4.54 ms: 1.15x slower                                                   |
| richards                  | 54.5 ms                                                  | 62.9 ms: 1.15x slower                                                   |
| json_loads                | 32.8 us                                                  | 38.0 us: 1.16x slower                                                   |
| pidigits                  | 238 ms                                                   | 277 ms: 1.16x slower                                                    |
| docutils                  | 2.96 sec                                                 | 3.45 sec: 1.16x slower                                                  |
| scimark_sparse_mat_mult   | 6.66 ms                                                  | 7.78 ms: 1.17x slower                                                   |
| create_gc_cycles          | 3.39 ms                                                  | 3.97 ms: 1.17x slower                                                   |
| json                      | 5.94 ms                                                  | 6.95 ms: 1.17x slower                                                   |
| richards_super            | 60.8 ms                                                  | 71.2 ms: 1.17x slower                                                   |
| sympy_sum                 | 151 ms                                                   | 178 ms: 1.17x slower                                                    |
| sqlite_synth              | 4.08 us                                                  | 4.81 us: 1.18x slower                                                   |
| chaos                     | 70.7 ms                                                  | 83.8 ms: 1.18x slower                                                   |
| regex_compile             | 134 ms                                                   | 158 ms: 1.19x slower                                                    |
| nqueens                   | 105 ms                                                   | 125 ms: 1.20x slower                                                    |
| genshi_text               | 28.6 ms                                                  | 34.4 ms: 1.20x slower                                                   |
| json_dumps                | 14.2 ms                                                  | 17.2 ms: 1.21x slower                                                   |
| genshi_xml                | 61.6 ms                                                  | 74.7 ms: 1.21x slower                                                   |
| nbody                     | 118 ms                                                   | 144 ms: 1.21x slower                                                    |
| unpickle_pure_python      | 265 us                                                   | 328 us: 1.24x slower                                                    |
| crypto_pyaes              | 84.9 ms                                                  | 105 ms: 1.24x slower                                                    |
| fannkuch                  | 478 ms                                                   | 596 ms: 1.25x slower                                                    |
| raytrace                  | 310 ms                                                   | 390 ms: 1.26x slower                                                    |
| scimark_lu                | 146 ms                                                   | 184 ms: 1.26x slower                                                    |
| telco                     | 10.5 ms                                                  | 13.2 ms: 1.26x slower                                                   |
| sympy_expand              | 472 ms                                                   | 599 ms: 1.27x slower                                                    |
| logging_format            | 8.10 us                                                  | 10.3 us: 1.27x slower                                                   |
| pickle_pure_python        | 374 us                                                   | 474 us: 1.27x slower                                                    |
| sympy_str                 | 265 ms                                                   | 339 ms: 1.28x slower                                                    |
| logging_simple            | 7.25 us                                                  | 9.31 us: 1.28x slower                                                   |
| mako                      | 14.0 ms                                                  | 17.9 ms: 1.28x slower                                                   |
| gc_traversal              | 5.92 ms                                                  | 7.69 ms: 1.30x slower                                                   |
| xml_etree_process         | 82.1 ms                                                  | 108 ms: 1.31x slower                                                    |
| typing_runtime_protocols  | 197 us                                                   | 260 us: 1.32x slower                                                    |
| django_template           | 39.4 ms                                                  | 52.5 ms: 1.33x slower                                                   |
| xml_etree_generate        | 118 ms                                                   | 161 ms: 1.36x slower                                                    |
| pprint_pformat            | 1.99 sec                                                 | 2.76 sec: 1.39x slower                                                  |
| pprint_safe_repr          | 962 ms                                                   | 1.35 sec: 1.40x slower                                                  |
| many_optionals            | 626 us                                                   | 1.10 ms: 1.76x slower                                                   |
| subparsers                | 20.3 ms                                                  | 36.8 ms: 1.81x slower                                                   |
| logging_silent            | 135 ns                                                   | 914 ns: 6.79x slower                                                    |
| coverage                  | 106 ms                                                   | 739 ms: 7.00x slower                                                    |
| thrift                    | 1.01 ms                                                  | 199 ms: 197.08x slower                                                  |
| bench_mp_pool             | 8.07 ms                                                  | 5.59 sec: 692.50x slower                                                |
| Geometric mean            | (ref)                                                    | 1.32x slower                                                            |

Benchmark hidden because not significant (5): generators, asyncio_websockets, float, pyflate, async_tree_cpu_io_mixed_tg
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250601-3.15.0a0-cebae97/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.224x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.10x
- 95% likely to have a slowdown of 1.10x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: 1.08x