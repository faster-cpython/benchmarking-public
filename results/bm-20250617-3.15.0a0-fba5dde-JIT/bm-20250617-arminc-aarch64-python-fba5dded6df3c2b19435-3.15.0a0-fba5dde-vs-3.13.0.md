# Results vs. 3.13.0

- fork: python
- ref: fba5dded6df3c2b19435
- machine: linux-aarch64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.158x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 369 ms: 1.18x slower                                                    |
| docutils       | 2.96 sec                                                 | 3.63 sec: 1.22x slower                                                  |
| html5lib       | 65.6 ms                                                  | 68.6 ms: 1.05x slower                                                   |
| sphinx         | 1.20 sec                                                 | 1.38 sec: 1.15x slower                                                  |
| Geometric mean | (ref)                                                    | 1.15x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|---------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg | 663 ms                                                   | 518 ms: 1.28x faster                                                    |
| async_tree_memoization    | 664 ms                                                   | 531 ms: 1.25x faster                                                    |
| async_tree_io_tg          | 1.16 sec                                                 | 1.02 sec: 1.14x faster                                                  |
| async_tree_none_tg        | 484 ms                                                   | 426 ms: 1.14x faster                                                    |
| async_tree_none           | 504 ms                                                   | 446 ms: 1.13x faster                                                    |
| async_tree_io             | 1.14 sec                                                 | 1.02 sec: 1.12x faster                                                  |
| async_tree_cpu_io_mixed   | 789 ms                                                   | 818 ms: 1.04x slower                                                    |
| async_generators          | 500 ms                                                   | 540 ms: 1.08x slower                                                    |
| coroutines                | 29.4 ms                                                  | 33.8 ms: 1.15x slower                                                   |
| Geometric mean            | (ref)                                                    | 1.07x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 118 ms                                                   | 132 ms: 1.12x slower                                                    |
| pidigits       | 238 ms                                                   | 282 ms: 1.18x slower                                                    |
| Geometric mean | (ref)                                                    | 1.09x slower                                                            |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.09 ms: 1.25x faster                                                   |
| regex_dna      | 263 ms                                                   | 229 ms: 1.15x faster                                                    |
| regex_v8       | 32.5 ms                                                  | 30.4 ms: 1.07x faster                                                   |
| regex_compile  | 134 ms                                                   | 154 ms: 1.15x slower                                                    |
| Geometric mean | (ref)                                                    | 1.07x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.67 sec                                                 | 2.72 sec: 1.02x slower                                                  |
| xml_etree_iterparse  | 159 ms                                                   | 173 ms: 1.09x slower                                                    |
| xml_etree_parse      | 203 ms                                                   | 229 ms: 1.13x slower                                                    |
| json_loads           | 32.8 us                                                  | 37.8 us: 1.15x slower                                                   |
| unpickle_pure_python | 265 us                                                   | 308 us: 1.16x slower                                                    |
| json_dumps           | 14.2 ms                                                  | 16.8 ms: 1.19x slower                                                   |
| xml_etree_process    | 82.1 ms                                                  | 103 ms: 1.25x slower                                                    |
| xml_etree_generate   | 118 ms                                                   | 150 ms: 1.27x slower                                                    |
| pickle_pure_python   | 374 us                                                   | 474 us: 1.27x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.17x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 17.1 ms: 1.07x slower                                                   |
| python_startup_no_site | 8.79 ms                                                  | 9.74 ms: 1.11x slower                                                   |
| Geometric mean         | (ref)                                                    | 1.09x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 28.6 ms                                                  | 33.0 ms: 1.15x slower                                                   |
| mako            | 14.0 ms                                                  | 17.0 ms: 1.21x slower                                                   |
| genshi_xml      | 61.6 ms                                                  | 76.5 ms: 1.24x slower                                                   |
| django_template | 39.4 ms                                                  | 53.1 ms: 1.35x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.24x slower                                                            |

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|---------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                       | 3.45 sec                                                 | 1.99 sec: 1.73x faster                                                  |
| async_tree_memoization_tg | 663 ms                                                   | 518 ms: 1.28x faster                                                    |
| async_tree_memoization    | 664 ms                                                   | 531 ms: 1.25x faster                                                    |
| regex_effbot              | 5.10 ms                                                  | 4.09 ms: 1.25x faster                                                   |
| deepcopy_memo             | 53.0 us                                                  | 43.7 us: 1.21x faster                                                   |
| deepcopy                  | 479 us                                                   | 408 us: 1.17x faster                                                    |
| regex_dna                 | 263 ms                                                   | 229 ms: 1.15x faster                                                    |
| async_tree_io_tg          | 1.16 sec                                                 | 1.02 sec: 1.14x faster                                                  |
| async_tree_none_tg        | 484 ms                                                   | 426 ms: 1.14x faster                                                    |
| async_tree_none           | 504 ms                                                   | 446 ms: 1.13x faster                                                    |
| async_tree_io             | 1.14 sec                                                 | 1.02 sec: 1.12x faster                                                  |
| regex_v8                  | 32.5 ms                                                  | 30.4 ms: 1.07x faster                                                   |
| k_core                    | 2.99 sec                                                 | 2.94 sec: 1.02x faster                                                  |
| djangocms                 | 66.2 us                                                  | 65.1 us: 1.02x faster                                                   |
| tomli_loads               | 2.67 sec                                                 | 2.72 sec: 1.02x slower                                                  |
| async_tree_cpu_io_mixed   | 789 ms                                                   | 818 ms: 1.04x slower                                                    |
| connected_components      | 547 ms                                                   | 568 ms: 1.04x slower                                                    |
| html5lib                  | 65.6 ms                                                  | 68.6 ms: 1.05x slower                                                   |
| go                        | 164 ms                                                   | 172 ms: 1.05x slower                                                    |
| scimark_sor               | 164 ms                                                   | 172 ms: 1.05x slower                                                    |
| spectral_norm             | 143 ms                                                   | 151 ms: 1.05x slower                                                    |
| shortest_path             | 565 ms                                                   | 597 ms: 1.06x slower                                                    |
| python_startup            | 16.0 ms                                                  | 17.1 ms: 1.07x slower                                                   |
| bpe_tokeniser             | 6.02 sec                                                 | 6.45 sec: 1.07x slower                                                  |
| async_generators          | 500 ms                                                   | 540 ms: 1.08x slower                                                    |
| deepcopy_reduce           | 4.24 us                                                  | 4.60 us: 1.08x slower                                                   |
| pylint                    | 345 ms                                                   | 376 ms: 1.09x slower                                                    |
| xml_etree_iterparse       | 159 ms                                                   | 173 ms: 1.09x slower                                                    |
| scimark_monte_carlo       | 87.8 ms                                                  | 95.8 ms: 1.09x slower                                                   |
| pathlib                   | 24.3 ms                                                  | 26.7 ms: 1.10x slower                                                   |
| deltablue                 | 3.97 ms                                                  | 4.37 ms: 1.10x slower                                                   |
| meteor_contest            | 117 ms                                                   | 129 ms: 1.11x slower                                                    |
| python_startup_no_site    | 8.79 ms                                                  | 9.74 ms: 1.11x slower                                                   |
| nbody                     | 118 ms                                                   | 132 ms: 1.12x slower                                                    |
| bench_thread_pool         | 1.34 ms                                                  | 1.51 ms: 1.13x slower                                                   |
| create_gc_cycles          | 3.39 ms                                                  | 3.83 ms: 1.13x slower                                                   |
| xml_etree_parse           | 203 ms                                                   | 229 ms: 1.13x slower                                                    |
| sympy_integrate           | 21.4 ms                                                  | 24.3 ms: 1.14x slower                                                   |
| sphinx                    | 1.20 sec                                                 | 1.38 sec: 1.15x slower                                                  |
| coroutines                | 29.4 ms                                                  | 33.8 ms: 1.15x slower                                                   |
| regex_compile             | 134 ms                                                   | 154 ms: 1.15x slower                                                    |
| genshi_text               | 28.6 ms                                                  | 33.0 ms: 1.15x slower                                                   |
| json_loads                | 32.8 us                                                  | 37.8 us: 1.15x slower                                                   |
| scimark_sparse_mat_mult   | 6.66 ms                                                  | 7.71 ms: 1.16x slower                                                   |
| unpickle_pure_python      | 265 us                                                   | 308 us: 1.16x slower                                                    |
| sqlite_synth              | 4.08 us                                                  | 4.76 us: 1.17x slower                                                   |
| json                      | 5.94 ms                                                  | 6.95 ms: 1.17x slower                                                   |
| 2to3                      | 313 ms                                                   | 369 ms: 1.18x slower                                                    |
| fannkuch                  | 478 ms                                                   | 564 ms: 1.18x slower                                                    |
| pidigits                  | 238 ms                                                   | 282 ms: 1.18x slower                                                    |
| json_dumps                | 14.2 ms                                                  | 16.8 ms: 1.19x slower                                                   |
| hexiom                    | 7.34 ms                                                  | 8.71 ms: 1.19x slower                                                   |
| comprehensions            | 20.8 us                                                  | 24.7 us: 1.19x slower                                                   |
| chaos                     | 70.7 ms                                                  | 84.9 ms: 1.20x slower                                                   |
| sympy_sum                 | 151 ms                                                   | 183 ms: 1.21x slower                                                    |
| mako                      | 14.0 ms                                                  | 17.0 ms: 1.21x slower                                                   |
| gc_traversal              | 5.92 ms                                                  | 7.22 ms: 1.22x slower                                                   |
| docutils                  | 2.96 sec                                                 | 3.63 sec: 1.22x slower                                                  |
| pycparser                 | 1.34 sec                                                 | 1.65 sec: 1.22x slower                                                  |
| thrift                    | 1.01 ms                                                  | 1.25 ms: 1.23x slower                                                   |
| nqueens                   | 105 ms                                                   | 130 ms: 1.24x slower                                                    |
| genshi_xml                | 61.6 ms                                                  | 76.5 ms: 1.24x slower                                                   |
| xml_etree_process         | 82.1 ms                                                  | 103 ms: 1.25x slower                                                    |
| logging_format            | 8.10 us                                                  | 10.2 us: 1.26x slower                                                   |
| crypto_pyaes              | 84.9 ms                                                  | 107 ms: 1.27x slower                                                    |
| xml_etree_generate        | 118 ms                                                   | 150 ms: 1.27x slower                                                    |
| pickle_pure_python        | 374 us                                                   | 474 us: 1.27x slower                                                    |
| coverage                  | 106 ms                                                   | 135 ms: 1.27x slower                                                    |
| logging_simple            | 7.25 us                                                  | 9.27 us: 1.28x slower                                                   |
| raytrace                  | 310 ms                                                   | 400 ms: 1.29x slower                                                    |
| scimark_lu                | 146 ms                                                   | 189 ms: 1.29x slower                                                    |
| telco                     | 10.5 ms                                                  | 13.6 ms: 1.30x slower                                                   |
| sympy_str                 | 265 ms                                                   | 345 ms: 1.30x slower                                                    |
| sympy_expand              | 472 ms                                                   | 624 ms: 1.32x slower                                                    |
| django_template           | 39.4 ms                                                  | 53.1 ms: 1.35x slower                                                   |
| typing_runtime_protocols  | 197 us                                                   | 275 us: 1.39x slower                                                    |
| many_optionals            | 626 us                                                   | 1.00 ms: 1.60x slower                                                   |
| pprint_pformat            | 1.99 sec                                                 | 3.24 sec: 1.63x slower                                                  |
| pprint_safe_repr          | 962 ms                                                   | 1.58 sec: 1.65x slower                                                  |
| subparsers                | 20.3 ms                                                  | 37.0 ms: 1.82x slower                                                   |
| logging_silent            | 135 ns                                                   | 912 ns: 6.77x slower                                                    |
| bench_mp_pool             | 8.07 ms                                                  | 3.00 sec: 371.64x slower                                                |
| Geometric mean            | (ref)                                                    | 1.21x slower                                                            |

Benchmark hidden because not significant (8): richards, generators, float, asyncio_websockets, pyflate, async_tree_cpu_io_mixed_tg, scimark_fft, richards_super
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.158x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: 1.10x