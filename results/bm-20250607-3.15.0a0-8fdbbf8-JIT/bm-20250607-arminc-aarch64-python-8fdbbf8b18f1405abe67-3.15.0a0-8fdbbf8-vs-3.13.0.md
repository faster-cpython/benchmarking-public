# Results vs. 3.13.0

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: linux-aarch64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.236x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 369 ms: 1.18x slower                                                    |
| docutils       | 2.96 sec                                                 | 3.67 sec: 1.24x slower                                                  |
| html5lib       | 65.6 ms                                                  | 70.5 ms: 1.07x slower                                                   |
| sphinx         | 1.20 sec                                                 | 1.39 sec: 1.16x slower                                                  |
| Geometric mean | (ref)                                                    | 1.16x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|---------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization    | 664 ms                                                   | 532 ms: 1.25x faster                                                    |
| async_tree_memoization_tg | 663 ms                                                   | 534 ms: 1.24x faster                                                    |
| async_tree_none           | 504 ms                                                   | 445 ms: 1.13x faster                                                    |
| async_tree_none_tg        | 484 ms                                                   | 430 ms: 1.13x faster                                                    |
| async_tree_io_tg          | 1.16 sec                                                 | 1.04 sec: 1.12x faster                                                  |
| async_tree_io             | 1.14 sec                                                 | 1.02 sec: 1.12x faster                                                  |
| async_tree_cpu_io_mixed   | 789 ms                                                   | 823 ms: 1.04x slower                                                    |
| async_generators          | 500 ms                                                   | 540 ms: 1.08x slower                                                    |
| coroutines                | 29.4 ms                                                  | 34.0 ms: 1.16x slower                                                   |
| Geometric mean            | (ref)                                                    | 1.06x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 92.8 ms: 1.03x faster                                                   |
| pidigits       | 238 ms                                                   | 279 ms: 1.17x slower                                                    |
| nbody          | 118 ms                                                   | 143 ms: 1.21x slower                                                    |
| Geometric mean | (ref)                                                    | 1.11x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.01 ms: 1.27x faster                                                   |
| regex_dna      | 263 ms                                                   | 227 ms: 1.16x faster                                                    |
| regex_v8       | 32.5 ms                                                  | 30.9 ms: 1.05x faster                                                   |
| regex_compile  | 134 ms                                                   | 157 ms: 1.17x slower                                                    |
| Geometric mean | (ref)                                                    | 1.07x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.67 sec                                                 | 2.72 sec: 1.02x slower                                                  |
| xml_etree_iterparse  | 159 ms                                                   | 170 ms: 1.07x slower                                                    |
| xml_etree_parse      | 203 ms                                                   | 227 ms: 1.12x slower                                                    |
| json_loads           | 32.8 us                                                  | 37.9 us: 1.16x slower                                                   |
| unpickle_pure_python | 265 us                                                   | 307 us: 1.16x slower                                                    |
| json_dumps           | 14.2 ms                                                  | 17.2 ms: 1.21x slower                                                   |
| xml_etree_process    | 82.1 ms                                                  | 104 ms: 1.26x slower                                                    |
| pickle_pure_python   | 374 us                                                   | 478 us: 1.28x slower                                                    |
| xml_etree_generate   | 118 ms                                                   | 154 ms: 1.31x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.17x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 17.0 ms: 1.06x slower                                                   |
| python_startup_no_site | 8.79 ms                                                  | 9.71 ms: 1.10x slower                                                   |
| Geometric mean         | (ref)                                                    | 1.08x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 14.0 ms                                                  | 16.5 ms: 1.18x slower                                                   |
| genshi_text     | 28.6 ms                                                  | 33.8 ms: 1.18x slower                                                   |
| genshi_xml      | 61.6 ms                                                  | 79.4 ms: 1.29x slower                                                   |
| django_template | 39.4 ms                                                  | 53.8 ms: 1.37x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.25x slower                                                            |

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|---------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                       | 3.45 sec                                                 | 1.99 sec: 1.73x faster                                                  |
| regex_effbot              | 5.10 ms                                                  | 4.01 ms: 1.27x faster                                                   |
| async_tree_memoization    | 664 ms                                                   | 532 ms: 1.25x faster                                                    |
| async_tree_memoization_tg | 663 ms                                                   | 534 ms: 1.24x faster                                                    |
| deepcopy_memo             | 53.0 us                                                  | 44.8 us: 1.18x faster                                                   |
| deepcopy                  | 479 us                                                   | 410 us: 1.17x faster                                                    |
| regex_dna                 | 263 ms                                                   | 227 ms: 1.16x faster                                                    |
| async_tree_none           | 504 ms                                                   | 445 ms: 1.13x faster                                                    |
| async_tree_none_tg        | 484 ms                                                   | 430 ms: 1.13x faster                                                    |
| async_tree_io_tg          | 1.16 sec                                                 | 1.04 sec: 1.12x faster                                                  |
| async_tree_io             | 1.14 sec                                                 | 1.02 sec: 1.12x faster                                                  |
| richards                  | 54.5 ms                                                  | 51.7 ms: 1.05x faster                                                   |
| regex_v8                  | 32.5 ms                                                  | 30.9 ms: 1.05x faster                                                   |
| float                     | 95.8 ms                                                  | 92.8 ms: 1.03x faster                                                   |
| tomli_loads               | 2.67 sec                                                 | 2.72 sec: 1.02x slower                                                  |
| go                        | 164 ms                                                   | 170 ms: 1.04x slower                                                    |
| scimark_fft               | 463 ms                                                   | 482 ms: 1.04x slower                                                    |
| async_tree_cpu_io_mixed   | 789 ms                                                   | 823 ms: 1.04x slower                                                    |
| connected_components      | 547 ms                                                   | 578 ms: 1.06x slower                                                    |
| python_startup            | 16.0 ms                                                  | 17.0 ms: 1.06x slower                                                   |
| scimark_sor               | 164 ms                                                   | 175 ms: 1.07x slower                                                    |
| xml_etree_iterparse       | 159 ms                                                   | 170 ms: 1.07x slower                                                    |
| deepcopy_reduce           | 4.24 us                                                  | 4.55 us: 1.07x slower                                                   |
| shortest_path             | 565 ms                                                   | 606 ms: 1.07x slower                                                    |
| html5lib                  | 65.6 ms                                                  | 70.5 ms: 1.07x slower                                                   |
| async_generators          | 500 ms                                                   | 540 ms: 1.08x slower                                                    |
| bpe_tokeniser             | 6.02 sec                                                 | 6.56 sec: 1.09x slower                                                  |
| spectral_norm             | 143 ms                                                   | 157 ms: 1.10x slower                                                    |
| pylint                    | 345 ms                                                   | 380 ms: 1.10x slower                                                    |
| python_startup_no_site    | 8.79 ms                                                  | 9.71 ms: 1.10x slower                                                   |
| deltablue                 | 3.97 ms                                                  | 4.44 ms: 1.12x slower                                                   |
| xml_etree_parse           | 203 ms                                                   | 227 ms: 1.12x slower                                                    |
| scimark_monte_carlo       | 87.8 ms                                                  | 98.5 ms: 1.12x slower                                                   |
| sympy_integrate           | 21.4 ms                                                  | 24.2 ms: 1.13x slower                                                   |
| bench_thread_pool         | 1.34 ms                                                  | 1.52 ms: 1.13x slower                                                   |
| meteor_contest            | 117 ms                                                   | 134 ms: 1.14x slower                                                    |
| pathlib                   | 24.3 ms                                                  | 27.8 ms: 1.14x slower                                                   |
| sqlite_synth              | 4.08 us                                                  | 4.70 us: 1.15x slower                                                   |
| coroutines                | 29.4 ms                                                  | 34.0 ms: 1.16x slower                                                   |
| sphinx                    | 1.20 sec                                                 | 1.39 sec: 1.16x slower                                                  |
| json_loads                | 32.8 us                                                  | 37.9 us: 1.16x slower                                                   |
| unpickle_pure_python      | 265 us                                                   | 307 us: 1.16x slower                                                    |
| scimark_sparse_mat_mult   | 6.66 ms                                                  | 7.77 ms: 1.17x slower                                                   |
| json                      | 5.94 ms                                                  | 6.93 ms: 1.17x slower                                                   |
| pidigits                  | 238 ms                                                   | 279 ms: 1.17x slower                                                    |
| regex_compile             | 134 ms                                                   | 157 ms: 1.17x slower                                                    |
| 2to3                      | 313 ms                                                   | 369 ms: 1.18x slower                                                    |
| mako                      | 14.0 ms                                                  | 16.5 ms: 1.18x slower                                                   |
| genshi_text               | 28.6 ms                                                  | 33.8 ms: 1.18x slower                                                   |
| hexiom                    | 7.34 ms                                                  | 8.74 ms: 1.19x slower                                                   |
| create_gc_cycles          | 3.39 ms                                                  | 4.04 ms: 1.19x slower                                                   |
| sympy_sum                 | 151 ms                                                   | 181 ms: 1.20x slower                                                    |
| pycparser                 | 1.34 sec                                                 | 1.61 sec: 1.20x slower                                                  |
| nbody                     | 118 ms                                                   | 143 ms: 1.21x slower                                                    |
| comprehensions            | 20.8 us                                                  | 25.2 us: 1.21x slower                                                   |
| json_dumps                | 14.2 ms                                                  | 17.2 ms: 1.21x slower                                                   |
| fannkuch                  | 478 ms                                                   | 581 ms: 1.21x slower                                                    |
| chaos                     | 70.7 ms                                                  | 86.2 ms: 1.22x slower                                                   |
| docutils                  | 2.96 sec                                                 | 3.67 sec: 1.24x slower                                                  |
| gc_traversal              | 5.92 ms                                                  | 7.39 ms: 1.25x slower                                                   |
| telco                     | 10.5 ms                                                  | 13.2 ms: 1.26x slower                                                   |
| xml_etree_process         | 82.1 ms                                                  | 104 ms: 1.26x slower                                                    |
| crypto_pyaes              | 84.9 ms                                                  | 108 ms: 1.27x slower                                                    |
| scimark_lu                | 146 ms                                                   | 186 ms: 1.27x slower                                                    |
| pickle_pure_python        | 374 us                                                   | 478 us: 1.28x slower                                                    |
| logging_format            | 8.10 us                                                  | 10.4 us: 1.29x slower                                                   |
| genshi_xml                | 61.6 ms                                                  | 79.4 ms: 1.29x slower                                                   |
| raytrace                  | 310 ms                                                   | 401 ms: 1.29x slower                                                    |
| nqueens                   | 105 ms                                                   | 136 ms: 1.29x slower                                                    |
| xml_etree_generate        | 118 ms                                                   | 154 ms: 1.31x slower                                                    |
| sympy_str                 | 265 ms                                                   | 348 ms: 1.31x slower                                                    |
| logging_simple            | 7.25 us                                                  | 9.57 us: 1.32x slower                                                   |
| sympy_expand              | 472 ms                                                   | 628 ms: 1.33x slower                                                    |
| django_template           | 39.4 ms                                                  | 53.8 ms: 1.37x slower                                                   |
| typing_runtime_protocols  | 197 us                                                   | 280 us: 1.42x slower                                                    |
| pprint_pformat            | 1.99 sec                                                 | 3.26 sec: 1.64x slower                                                  |
| pprint_safe_repr          | 962 ms                                                   | 1.59 sec: 1.65x slower                                                  |
| subparsers                | 20.3 ms                                                  | 36.5 ms: 1.79x slower                                                   |
| many_optionals            | 626 us                                                   | 1.14 ms: 1.83x slower                                                   |
| coverage                  | 106 ms                                                   | 720 ms: 6.82x slower                                                    |
| logging_silent            | 135 ns                                                   | 948 ns: 7.04x slower                                                    |
| thrift                    | 1.01 ms                                                  | 197 ms: 195.24x slower                                                  |
| bench_mp_pool             | 8.07 ms                                                  | 3.45 sec: 427.32x slower                                                |
| Geometric mean            | (ref)                                                    | 1.32x slower                                                            |

Benchmark hidden because not significant (6): generators, k_core, asyncio_websockets, richards_super, async_tree_cpu_io_mixed_tg, pyflate
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.236x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.10x
- 95% likely to have a slowdown of 1.09x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: 1.09x