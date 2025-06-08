# Results vs. 3.13.0

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: linux-aarch64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.228x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 352 ms: 1.13x slower                                                    |
| docutils       | 2.96 sec                                                 | 3.44 sec: 1.16x slower                                                  |
| html5lib       | 65.6 ms                                                  | 67.4 ms: 1.03x slower                                                   |
| sphinx         | 1.20 sec                                                 | 1.34 sec: 1.11x slower                                                  |
| Geometric mean | (ref)                                                    | 1.11x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|---------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization    | 664 ms                                                   | 509 ms: 1.30x faster                                                    |
| async_tree_memoization_tg | 663 ms                                                   | 527 ms: 1.26x faster                                                    |
| async_tree_io             | 1.14 sec                                                 | 979 ms: 1.16x faster                                                    |
| async_tree_none           | 504 ms                                                   | 433 ms: 1.16x faster                                                    |
| async_tree_none_tg        | 484 ms                                                   | 418 ms: 1.16x faster                                                    |
| async_tree_io_tg          | 1.16 sec                                                 | 1.02 sec: 1.14x faster                                                  |
| async_generators          | 500 ms                                                   | 519 ms: 1.04x slower                                                    |
| coroutines                | 29.4 ms                                                  | 34.0 ms: 1.16x slower                                                   |
| Geometric mean            | (ref)                                                    | 1.08x faster                                                            |

Benchmark hidden because not significant (3): asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 118 ms                                                   | 138 ms: 1.17x slower                                                    |
| pidigits       | 238 ms                                                   | 281 ms: 1.18x slower                                                    |
| Geometric mean | (ref)                                                    | 1.12x slower                                                            |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.03 ms: 1.27x faster                                                   |
| regex_dna      | 263 ms                                                   | 231 ms: 1.14x faster                                                    |
| regex_v8       | 32.5 ms                                                  | 30.1 ms: 1.08x faster                                                   |
| regex_compile  | 134 ms                                                   | 152 ms: 1.14x slower                                                    |
| Geometric mean | (ref)                                                    | 1.08x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse  | 159 ms                                                   | 168 ms: 1.06x slower                                                    |
| tomli_loads          | 2.67 sec                                                 | 2.86 sec: 1.07x slower                                                  |
| xml_etree_parse      | 203 ms                                                   | 230 ms: 1.14x slower                                                    |
| json_loads           | 32.8 us                                                  | 38.6 us: 1.18x slower                                                   |
| unpickle_pure_python | 265 us                                                   | 321 us: 1.21x slower                                                    |
| json_dumps           | 14.2 ms                                                  | 17.4 ms: 1.22x slower                                                   |
| pickle_pure_python   | 374 us                                                   | 471 us: 1.26x slower                                                    |
| xml_etree_process    | 82.1 ms                                                  | 106 ms: 1.29x slower                                                    |
| xml_etree_generate   | 118 ms                                                   | 160 ms: 1.35x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.19x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 16.9 ms: 1.05x slower                                                   |
| python_startup_no_site | 8.79 ms                                                  | 9.58 ms: 1.09x slower                                                   |
| Geometric mean         | (ref)                                                    | 1.07x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 28.6 ms                                                  | 33.9 ms: 1.19x slower                                                   |
| genshi_xml      | 61.6 ms                                                  | 74.3 ms: 1.21x slower                                                   |
| mako            | 14.0 ms                                                  | 17.4 ms: 1.24x slower                                                   |
| django_template | 39.4 ms                                                  | 52.6 ms: 1.34x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.24x slower                                                            |

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|---------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                       | 3.45 sec                                                 | 1.98 sec: 1.74x faster                                                  |
| async_tree_memoization    | 664 ms                                                   | 509 ms: 1.30x faster                                                    |
| regex_effbot              | 5.10 ms                                                  | 4.03 ms: 1.27x faster                                                   |
| async_tree_memoization_tg | 663 ms                                                   | 527 ms: 1.26x faster                                                    |
| deepcopy_memo             | 53.0 us                                                  | 44.0 us: 1.20x faster                                                   |
| deepcopy                  | 479 us                                                   | 405 us: 1.18x faster                                                    |
| go                        | 164 ms                                                   | 141 ms: 1.17x faster                                                    |
| async_tree_io             | 1.14 sec                                                 | 979 ms: 1.16x faster                                                    |
| async_tree_none           | 504 ms                                                   | 433 ms: 1.16x faster                                                    |
| async_tree_none_tg        | 484 ms                                                   | 418 ms: 1.16x faster                                                    |
| async_tree_io_tg          | 1.16 sec                                                 | 1.02 sec: 1.14x faster                                                  |
| regex_dna                 | 263 ms                                                   | 231 ms: 1.14x faster                                                    |
| regex_v8                  | 32.5 ms                                                  | 30.1 ms: 1.08x faster                                                   |
| html5lib                  | 65.6 ms                                                  | 67.4 ms: 1.03x slower                                                   |
| async_generators          | 500 ms                                                   | 519 ms: 1.04x slower                                                    |
| python_startup            | 16.0 ms                                                  | 16.9 ms: 1.05x slower                                                   |
| xml_etree_iterparse       | 159 ms                                                   | 168 ms: 1.06x slower                                                    |
| connected_components      | 547 ms                                                   | 580 ms: 1.06x slower                                                    |
| scimark_sor               | 164 ms                                                   | 176 ms: 1.07x slower                                                    |
| tomli_loads               | 2.67 sec                                                 | 2.86 sec: 1.07x slower                                                  |
| pylint                    | 345 ms                                                   | 373 ms: 1.08x slower                                                    |
| shortest_path             | 565 ms                                                   | 612 ms: 1.08x slower                                                    |
| scimark_fft               | 463 ms                                                   | 501 ms: 1.08x slower                                                    |
| pycparser                 | 1.34 sec                                                 | 1.46 sec: 1.09x slower                                                  |
| spectral_norm             | 143 ms                                                   | 156 ms: 1.09x slower                                                    |
| python_startup_no_site    | 8.79 ms                                                  | 9.58 ms: 1.09x slower                                                   |
| meteor_contest            | 117 ms                                                   | 128 ms: 1.09x slower                                                    |
| pathlib                   | 24.3 ms                                                  | 26.6 ms: 1.09x slower                                                   |
| sympy_integrate           | 21.4 ms                                                  | 23.6 ms: 1.10x slower                                                   |
| comprehensions            | 20.8 us                                                  | 23.0 us: 1.10x slower                                                   |
| deepcopy_reduce           | 4.24 us                                                  | 4.70 us: 1.11x slower                                                   |
| bench_thread_pool         | 1.34 ms                                                  | 1.49 ms: 1.11x slower                                                   |
| sphinx                    | 1.20 sec                                                 | 1.34 sec: 1.11x slower                                                  |
| scimark_monte_carlo       | 87.8 ms                                                  | 98.2 ms: 1.12x slower                                                   |
| bpe_tokeniser             | 6.02 sec                                                 | 6.75 sec: 1.12x slower                                                  |
| 2to3                      | 313 ms                                                   | 352 ms: 1.13x slower                                                    |
| deltablue                 | 3.97 ms                                                  | 4.50 ms: 1.13x slower                                                   |
| xml_etree_parse           | 203 ms                                                   | 230 ms: 1.14x slower                                                    |
| regex_compile             | 134 ms                                                   | 152 ms: 1.14x slower                                                    |
| hexiom                    | 7.34 ms                                                  | 8.40 ms: 1.14x slower                                                   |
| coroutines                | 29.4 ms                                                  | 34.0 ms: 1.16x slower                                                   |
| docutils                  | 2.96 sec                                                 | 3.44 sec: 1.16x slower                                                  |
| richards                  | 54.5 ms                                                  | 63.5 ms: 1.17x slower                                                   |
| nbody                     | 118 ms                                                   | 138 ms: 1.17x slower                                                    |
| json_loads                | 32.8 us                                                  | 38.6 us: 1.18x slower                                                   |
| pidigits                  | 238 ms                                                   | 281 ms: 1.18x slower                                                    |
| richards_super            | 60.8 ms                                                  | 71.8 ms: 1.18x slower                                                   |
| json                      | 5.94 ms                                                  | 7.02 ms: 1.18x slower                                                   |
| scimark_sparse_mat_mult   | 6.66 ms                                                  | 7.88 ms: 1.18x slower                                                   |
| chaos                     | 70.7 ms                                                  | 83.9 ms: 1.19x slower                                                   |
| sympy_sum                 | 151 ms                                                   | 179 ms: 1.19x slower                                                    |
| genshi_text               | 28.6 ms                                                  | 33.9 ms: 1.19x slower                                                   |
| nqueens                   | 105 ms                                                   | 125 ms: 1.19x slower                                                    |
| create_gc_cycles          | 3.39 ms                                                  | 4.05 ms: 1.19x slower                                                   |
| sqlite_synth              | 4.08 us                                                  | 4.92 us: 1.21x slower                                                   |
| genshi_xml                | 61.6 ms                                                  | 74.3 ms: 1.21x slower                                                   |
| crypto_pyaes              | 84.9 ms                                                  | 103 ms: 1.21x slower                                                    |
| unpickle_pure_python      | 265 us                                                   | 321 us: 1.21x slower                                                    |
| json_dumps                | 14.2 ms                                                  | 17.4 ms: 1.22x slower                                                   |
| sympy_expand              | 472 ms                                                   | 585 ms: 1.24x slower                                                    |
| fannkuch                  | 478 ms                                                   | 593 ms: 1.24x slower                                                    |
| mako                      | 14.0 ms                                                  | 17.4 ms: 1.24x slower                                                   |
| sympy_str                 | 265 ms                                                   | 332 ms: 1.25x slower                                                    |
| logging_format            | 8.10 us                                                  | 10.2 us: 1.26x slower                                                   |
| pickle_pure_python        | 374 us                                                   | 471 us: 1.26x slower                                                    |
| gc_traversal              | 5.92 ms                                                  | 7.47 ms: 1.26x slower                                                   |
| telco                     | 10.5 ms                                                  | 13.4 ms: 1.28x slower                                                   |
| scimark_lu                | 146 ms                                                   | 188 ms: 1.29x slower                                                    |
| xml_etree_process         | 82.1 ms                                                  | 106 ms: 1.29x slower                                                    |
| logging_simple            | 7.25 us                                                  | 9.33 us: 1.29x slower                                                   |
| raytrace                  | 310 ms                                                   | 400 ms: 1.29x slower                                                    |
| typing_runtime_protocols  | 197 us                                                   | 259 us: 1.31x slower                                                    |
| pprint_pformat            | 1.99 sec                                                 | 2.64 sec: 1.33x slower                                                  |
| django_template           | 39.4 ms                                                  | 52.6 ms: 1.34x slower                                                   |
| xml_etree_generate        | 118 ms                                                   | 160 ms: 1.35x slower                                                    |
| pprint_safe_repr          | 962 ms                                                   | 1.30 sec: 1.35x slower                                                  |
| many_optionals            | 626 us                                                   | 1.11 ms: 1.78x slower                                                   |
| subparsers                | 20.3 ms                                                  | 36.5 ms: 1.79x slower                                                   |
| coverage                  | 106 ms                                                   | 695 ms: 6.58x slower                                                    |
| logging_silent            | 135 ns                                                   | 929 ns: 6.91x slower                                                    |
| thrift                    | 1.01 ms                                                  | 196 ms: 194.36x slower                                                  |
| bench_mp_pool             | 8.07 ms                                                  | 6.68 sec: 828.54x slower                                                |
| Geometric mean            | (ref)                                                    | 1.31x slower                                                            |

Benchmark hidden because not significant (7): asyncio_websockets, k_core, generators, pyflate, async_tree_cpu_io_mixed_tg, float, async_tree_cpu_io_mixed
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.228x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.10x
- 95% likely to have a slowdown of 1.10x
- 99% likely to have a slowdown of 1.09x

# Memory
- memory change: 1.08x