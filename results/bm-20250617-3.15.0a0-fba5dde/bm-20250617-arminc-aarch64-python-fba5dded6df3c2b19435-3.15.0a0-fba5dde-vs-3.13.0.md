# Results vs. 3.13.0

- fork: python
- ref: fba5dded6df3c2b19435
- machine: linux-aarch64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.167x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 357 ms: 1.14x slower                                                    |
| docutils       | 2.96 sec                                                 | 3.44 sec: 1.16x slower                                                  |
| html5lib       | 65.6 ms                                                  | 67.3 ms: 1.03x slower                                                   |
| sphinx         | 1.20 sec                                                 | 1.36 sec: 1.13x slower                                                  |
| Geometric mean | (ref)                                                    | 1.11x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|---------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization    | 664 ms                                                   | 532 ms: 1.25x faster                                                    |
| async_tree_memoization_tg | 663 ms                                                   | 534 ms: 1.24x faster                                                    |
| async_tree_io             | 1.14 sec                                                 | 1.01 sec: 1.13x faster                                                  |
| async_tree_io_tg          | 1.16 sec                                                 | 1.04 sec: 1.12x faster                                                  |
| async_tree_none           | 504 ms                                                   | 449 ms: 1.12x faster                                                    |
| async_tree_none_tg        | 484 ms                                                   | 434 ms: 1.12x faster                                                    |
| async_generators          | 500 ms                                                   | 515 ms: 1.03x slower                                                    |
| async_tree_cpu_io_mixed   | 789 ms                                                   | 823 ms: 1.04x slower                                                    |
| coroutines                | 29.4 ms                                                  | 33.0 ms: 1.12x slower                                                   |
| Geometric mean            | (ref)                                                    | 1.07x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 238 ms                                                   | 282 ms: 1.18x slower                                                    |
| nbody          | 118 ms                                                   | 141 ms: 1.19x slower                                                    |
| Geometric mean | (ref)                                                    | 1.13x slower                                                            |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.08 ms: 1.25x faster                                                   |
| regex_dna      | 263 ms                                                   | 225 ms: 1.17x faster                                                    |
| regex_v8       | 32.5 ms                                                  | 30.3 ms: 1.07x faster                                                   |
| regex_compile  | 134 ms                                                   | 155 ms: 1.16x slower                                                    |
| Geometric mean | (ref)                                                    | 1.08x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse  | 159 ms                                                   | 170 ms: 1.07x slower                                                    |
| tomli_loads          | 2.67 sec                                                 | 2.93 sec: 1.10x slower                                                  |
| xml_etree_parse      | 203 ms                                                   | 227 ms: 1.12x slower                                                    |
| json_loads           | 32.8 us                                                  | 38.5 us: 1.17x slower                                                   |
| json_dumps           | 14.2 ms                                                  | 17.4 ms: 1.22x slower                                                   |
| unpickle_pure_python | 265 us                                                   | 329 us: 1.24x slower                                                    |
| pickle_pure_python   | 374 us                                                   | 468 us: 1.25x slower                                                    |
| xml_etree_process    | 82.1 ms                                                  | 110 ms: 1.33x slower                                                    |
| xml_etree_generate   | 118 ms                                                   | 163 ms: 1.38x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.21x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 17.1 ms: 1.07x slower                                                   |
| python_startup_no_site | 8.79 ms                                                  | 9.73 ms: 1.11x slower                                                   |
| Geometric mean         | (ref)                                                    | 1.09x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 28.6 ms                                                  | 33.3 ms: 1.16x slower                                                   |
| mako            | 14.0 ms                                                  | 17.0 ms: 1.22x slower                                                   |
| genshi_xml      | 61.6 ms                                                  | 75.1 ms: 1.22x slower                                                   |
| django_template | 39.4 ms                                                  | 53.6 ms: 1.36x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.24x slower                                                            |

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|---------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                       | 3.45 sec                                                 | 1.97 sec: 1.75x faster                                                  |
| regex_effbot              | 5.10 ms                                                  | 4.08 ms: 1.25x faster                                                   |
| async_tree_memoization    | 664 ms                                                   | 532 ms: 1.25x faster                                                    |
| async_tree_memoization_tg | 663 ms                                                   | 534 ms: 1.24x faster                                                    |
| deepcopy_memo             | 53.0 us                                                  | 43.3 us: 1.22x faster                                                   |
| deepcopy                  | 479 us                                                   | 406 us: 1.18x faster                                                    |
| go                        | 164 ms                                                   | 141 ms: 1.17x faster                                                    |
| regex_dna                 | 263 ms                                                   | 225 ms: 1.17x faster                                                    |
| async_tree_io             | 1.14 sec                                                 | 1.01 sec: 1.13x faster                                                  |
| async_tree_io_tg          | 1.16 sec                                                 | 1.04 sec: 1.12x faster                                                  |
| async_tree_none           | 504 ms                                                   | 449 ms: 1.12x faster                                                    |
| async_tree_none_tg        | 484 ms                                                   | 434 ms: 1.12x faster                                                    |
| regex_v8                  | 32.5 ms                                                  | 30.3 ms: 1.07x faster                                                   |
| html5lib                  | 65.6 ms                                                  | 67.3 ms: 1.03x slower                                                   |
| async_generators          | 500 ms                                                   | 515 ms: 1.03x slower                                                    |
| scimark_sor               | 164 ms                                                   | 169 ms: 1.03x slower                                                    |
| connected_components      | 547 ms                                                   | 565 ms: 1.03x slower                                                    |
| async_tree_cpu_io_mixed   | 789 ms                                                   | 823 ms: 1.04x slower                                                    |
| pylint                    | 345 ms                                                   | 367 ms: 1.06x slower                                                    |
| python_startup            | 16.0 ms                                                  | 17.1 ms: 1.07x slower                                                   |
| xml_etree_iterparse       | 159 ms                                                   | 170 ms: 1.07x slower                                                    |
| shortest_path             | 565 ms                                                   | 608 ms: 1.08x slower                                                    |
| scimark_fft               | 463 ms                                                   | 498 ms: 1.08x slower                                                    |
| deepcopy_reduce           | 4.24 us                                                  | 4.59 us: 1.08x slower                                                   |
| spectral_norm             | 143 ms                                                   | 156 ms: 1.09x slower                                                    |
| meteor_contest            | 117 ms                                                   | 128 ms: 1.09x slower                                                    |
| scimark_monte_carlo       | 87.8 ms                                                  | 95.9 ms: 1.09x slower                                                   |
| sympy_integrate           | 21.4 ms                                                  | 23.5 ms: 1.10x slower                                                   |
| tomli_loads               | 2.67 sec                                                 | 2.93 sec: 1.10x slower                                                  |
| pathlib                   | 24.3 ms                                                  | 26.8 ms: 1.10x slower                                                   |
| python_startup_no_site    | 8.79 ms                                                  | 9.73 ms: 1.11x slower                                                   |
| pycparser                 | 1.34 sec                                                 | 1.49 sec: 1.11x slower                                                  |
| comprehensions            | 20.8 us                                                  | 23.1 us: 1.11x slower                                                   |
| bpe_tokeniser             | 6.02 sec                                                 | 6.73 sec: 1.12x slower                                                  |
| xml_etree_parse           | 203 ms                                                   | 227 ms: 1.12x slower                                                    |
| hexiom                    | 7.34 ms                                                  | 8.23 ms: 1.12x slower                                                   |
| coroutines                | 29.4 ms                                                  | 33.0 ms: 1.12x slower                                                   |
| sphinx                    | 1.20 sec                                                 | 1.36 sec: 1.13x slower                                                  |
| create_gc_cycles          | 3.39 ms                                                  | 3.86 ms: 1.14x slower                                                   |
| bench_thread_pool         | 1.34 ms                                                  | 1.52 ms: 1.14x slower                                                   |
| 2to3                      | 313 ms                                                   | 357 ms: 1.14x slower                                                    |
| deltablue                 | 3.97 ms                                                  | 4.54 ms: 1.14x slower                                                   |
| json                      | 5.94 ms                                                  | 6.86 ms: 1.16x slower                                                   |
| docutils                  | 2.96 sec                                                 | 3.44 sec: 1.16x slower                                                  |
| regex_compile             | 134 ms                                                   | 155 ms: 1.16x slower                                                    |
| genshi_text               | 28.6 ms                                                  | 33.3 ms: 1.16x slower                                                   |
| scimark_sparse_mat_mult   | 6.66 ms                                                  | 7.76 ms: 1.17x slower                                                   |
| chaos                     | 70.7 ms                                                  | 82.7 ms: 1.17x slower                                                   |
| json_loads                | 32.8 us                                                  | 38.5 us: 1.17x slower                                                   |
| richards                  | 54.5 ms                                                  | 64.0 ms: 1.17x slower                                                   |
| sqlite_synth              | 4.08 us                                                  | 4.82 us: 1.18x slower                                                   |
| pidigits                  | 238 ms                                                   | 282 ms: 1.18x slower                                                    |
| richards_super            | 60.8 ms                                                  | 72.2 ms: 1.19x slower                                                   |
| nqueens                   | 105 ms                                                   | 125 ms: 1.19x slower                                                    |
| sympy_sum                 | 151 ms                                                   | 180 ms: 1.19x slower                                                    |
| nbody                     | 118 ms                                                   | 141 ms: 1.19x slower                                                    |
| mako                      | 14.0 ms                                                  | 17.0 ms: 1.22x slower                                                   |
| genshi_xml                | 61.6 ms                                                  | 75.1 ms: 1.22x slower                                                   |
| json_dumps                | 14.2 ms                                                  | 17.4 ms: 1.22x slower                                                   |
| gc_traversal              | 5.92 ms                                                  | 7.30 ms: 1.23x slower                                                   |
| fannkuch                  | 478 ms                                                   | 590 ms: 1.23x slower                                                    |
| crypto_pyaes              | 84.9 ms                                                  | 105 ms: 1.24x slower                                                    |
| thrift                    | 1.01 ms                                                  | 1.25 ms: 1.24x slower                                                   |
| unpickle_pure_python      | 265 us                                                   | 329 us: 1.24x slower                                                    |
| pickle_pure_python        | 374 us                                                   | 468 us: 1.25x slower                                                    |
| raytrace                  | 310 ms                                                   | 390 ms: 1.26x slower                                                    |
| logging_format            | 8.10 us                                                  | 10.3 us: 1.27x slower                                                   |
| scimark_lu                | 146 ms                                                   | 186 ms: 1.27x slower                                                    |
| sympy_str                 | 265 ms                                                   | 339 ms: 1.28x slower                                                    |
| sympy_expand              | 472 ms                                                   | 606 ms: 1.28x slower                                                    |
| logging_simple            | 7.25 us                                                  | 9.40 us: 1.30x slower                                                   |
| telco                     | 10.5 ms                                                  | 13.6 ms: 1.30x slower                                                   |
| typing_runtime_protocols  | 197 us                                                   | 259 us: 1.31x slower                                                    |
| coverage                  | 106 ms                                                   | 141 ms: 1.33x slower                                                    |
| xml_etree_process         | 82.1 ms                                                  | 110 ms: 1.33x slower                                                    |
| pprint_pformat            | 1.99 sec                                                 | 2.70 sec: 1.36x slower                                                  |
| django_template           | 39.4 ms                                                  | 53.6 ms: 1.36x slower                                                   |
| xml_etree_generate        | 118 ms                                                   | 163 ms: 1.38x slower                                                    |
| pprint_safe_repr          | 962 ms                                                   | 1.34 sec: 1.39x slower                                                  |
| many_optionals            | 626 us                                                   | 957 us: 1.53x slower                                                    |
| subparsers                | 20.3 ms                                                  | 36.2 ms: 1.78x slower                                                   |
| logging_silent            | 135 ns                                                   | 946 ns: 7.03x slower                                                    |
| bench_mp_pool             | 8.07 ms                                                  | 5.40 sec: 669.85x slower                                                |
| Geometric mean            | (ref)                                                    | 1.22x slower                                                            |

Benchmark hidden because not significant (7): k_core, generators, djangocms, pyflate, asyncio_websockets, float, async_tree_cpu_io_mixed_tg
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.167x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.11x
- 95% likely to have a slowdown of 1.10x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: 1.08x