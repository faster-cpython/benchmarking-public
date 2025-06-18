# Results vs. 3.13.0

- fork: python
- ref: fba5dded6df3c2b19435
- machine: linux-aarch64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.262x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x slower
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 446 ms: 1.42x slower                                                    |
| docutils       | 2.96 sec                                                 | 3.94 sec: 1.33x slower                                                  |
| html5lib       | 65.6 ms                                                  | 84.1 ms: 1.28x slower                                                   |
| sphinx         | 1.20 sec                                                 | 1.59 sec: 1.32x slower                                                  |
| Geometric mean | (ref)                                                    | 1.34x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|---------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg | 663 ms                                                   | 518 ms: 1.28x faster                                                    |
| async_tree_io_tg          | 1.16 sec                                                 | 977 ms: 1.19x faster                                                    |
| async_tree_memoization    | 664 ms                                                   | 557 ms: 1.19x faster                                                    |
| async_tree_none_tg        | 484 ms                                                   | 425 ms: 1.14x faster                                                    |
| async_tree_io             | 1.14 sec                                                 | 1.03 sec: 1.11x faster                                                  |
| async_tree_none           | 504 ms                                                   | 469 ms: 1.07x faster                                                    |
| async_tree_cpu_io_mixed   | 789 ms                                                   | 859 ms: 1.09x slower                                                    |
| async_generators          | 500 ms                                                   | 613 ms: 1.23x slower                                                    |
| coroutines                | 29.4 ms                                                  | 38.5 ms: 1.31x slower                                                   |
| Geometric mean            | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 106 ms: 1.10x slower                                                    |
| pidigits       | 238 ms                                                   | 282 ms: 1.18x slower                                                    |
| nbody          | 118 ms                                                   | 191 ms: 1.61x slower                                                    |
| Geometric mean | (ref)                                                    | 1.28x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.12 ms: 1.24x faster                                                   |
| regex_dna      | 263 ms                                                   | 235 ms: 1.12x faster                                                    |
| regex_v8       | 32.5 ms                                                  | 30.8 ms: 1.05x faster                                                   |
| regex_compile  | 134 ms                                                   | 201 ms: 1.50x slower                                                    |
| Geometric mean | (ref)                                                    | 1.01x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 203 ms                                                   | 239 ms: 1.18x slower                                                    |
| tomli_loads          | 2.67 sec                                                 | 3.61 sec: 1.35x slower                                                  |
| json_loads           | 32.8 us                                                  | 44.6 us: 1.36x slower                                                   |
| json_dumps           | 14.2 ms                                                  | 19.7 ms: 1.39x slower                                                   |
| xml_etree_process    | 82.1 ms                                                  | 128 ms: 1.56x slower                                                    |
| unpickle_pure_python | 265 us                                                   | 418 us: 1.58x slower                                                    |
| pickle_pure_python   | 374 us                                                   | 593 us: 1.59x slower                                                    |
| xml_etree_generate   | 118 ms                                                   | 189 ms: 1.60x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.39x slower                                                            |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 23.3 ms: 1.45x slower                                                   |
| python_startup_no_site | 8.79 ms                                                  | 13.8 ms: 1.57x slower                                                   |
| Geometric mean         | (ref)                                                    | 1.51x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 61.6 ms                                                  | 98.2 ms: 1.60x slower                                                   |
| genshi_text     | 28.6 ms                                                  | 46.5 ms: 1.63x slower                                                   |
| mako            | 14.0 ms                                                  | 23.8 ms: 1.70x slower                                                   |
| django_template | 39.4 ms                                                  | 75.2 ms: 1.91x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.70x slower                                                            |

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|---------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| gc_traversal              | 5.92 ms                                                  | 3.70 ms: 1.60x faster                                                   |
| mdp                       | 3.45 sec                                                 | 2.52 sec: 1.37x faster                                                  |
| create_gc_cycles          | 3.39 ms                                                  | 2.53 ms: 1.34x faster                                                   |
| async_tree_memoization_tg | 663 ms                                                   | 518 ms: 1.28x faster                                                    |
| regex_effbot              | 5.10 ms                                                  | 4.12 ms: 1.24x faster                                                   |
| async_tree_io_tg          | 1.16 sec                                                 | 977 ms: 1.19x faster                                                    |
| async_tree_memoization    | 664 ms                                                   | 557 ms: 1.19x faster                                                    |
| async_tree_none_tg        | 484 ms                                                   | 425 ms: 1.14x faster                                                    |
| regex_dna                 | 263 ms                                                   | 235 ms: 1.12x faster                                                    |
| async_tree_io             | 1.14 sec                                                 | 1.03 sec: 1.11x faster                                                  |
| async_tree_none           | 504 ms                                                   | 469 ms: 1.07x faster                                                    |
| regex_v8                  | 32.5 ms                                                  | 30.8 ms: 1.05x faster                                                   |
| deepcopy_memo             | 53.0 us                                                  | 56.7 us: 1.07x slower                                                   |
| sqlite_synth              | 4.08 us                                                  | 4.43 us: 1.08x slower                                                   |
| go                        | 164 ms                                                   | 178 ms: 1.09x slower                                                    |
| async_tree_cpu_io_mixed   | 789 ms                                                   | 859 ms: 1.09x slower                                                    |
| float                     | 95.8 ms                                                  | 106 ms: 1.10x slower                                                    |
| deepcopy                  | 479 us                                                   | 534 us: 1.12x slower                                                    |
| k_core                    | 2.99 sec                                                 | 3.39 sec: 1.13x slower                                                  |
| pyflate                   | 582 ms                                                   | 664 ms: 1.14x slower                                                    |
| generators                | 40.3 ms                                                  | 47.0 ms: 1.17x slower                                                   |
| xml_etree_parse           | 203 ms                                                   | 239 ms: 1.18x slower                                                    |
| pidigits                  | 238 ms                                                   | 282 ms: 1.18x slower                                                    |
| scimark_sor               | 164 ms                                                   | 194 ms: 1.18x slower                                                    |
| async_generators          | 500 ms                                                   | 613 ms: 1.23x slower                                                    |
| connected_components      | 547 ms                                                   | 674 ms: 1.23x slower                                                    |
| pathlib                   | 24.3 ms                                                  | 30.2 ms: 1.24x slower                                                   |
| scimark_fft               | 463 ms                                                   | 580 ms: 1.25x slower                                                    |
| shortest_path             | 565 ms                                                   | 710 ms: 1.26x slower                                                    |
| html5lib                  | 65.6 ms                                                  | 84.1 ms: 1.28x slower                                                   |
| pycparser                 | 1.34 sec                                                 | 1.76 sec: 1.31x slower                                                  |
| coroutines                | 29.4 ms                                                  | 38.5 ms: 1.31x slower                                                   |
| sphinx                    | 1.20 sec                                                 | 1.59 sec: 1.32x slower                                                  |
| spectral_norm             | 143 ms                                                   | 190 ms: 1.32x slower                                                    |
| pylint                    | 345 ms                                                   | 457 ms: 1.32x slower                                                    |
| docutils                  | 2.96 sec                                                 | 3.94 sec: 1.33x slower                                                  |
| meteor_contest            | 117 ms                                                   | 156 ms: 1.33x slower                                                    |
| json                      | 5.94 ms                                                  | 7.96 ms: 1.34x slower                                                   |
| tomli_loads               | 2.67 sec                                                 | 3.61 sec: 1.35x slower                                                  |
| hexiom                    | 7.34 ms                                                  | 9.96 ms: 1.36x slower                                                   |
| scimark_sparse_mat_mult   | 6.66 ms                                                  | 9.05 ms: 1.36x slower                                                   |
| json_loads                | 32.8 us                                                  | 44.6 us: 1.36x slower                                                   |
| json_dumps                | 14.2 ms                                                  | 19.7 ms: 1.39x slower                                                   |
| deltablue                 | 3.97 ms                                                  | 5.55 ms: 1.40x slower                                                   |
| chaos                     | 70.7 ms                                                  | 99.4 ms: 1.40x slower                                                   |
| 2to3                      | 313 ms                                                   | 446 ms: 1.42x slower                                                    |
| python_startup            | 16.0 ms                                                  | 23.3 ms: 1.45x slower                                                   |
| fannkuch                  | 478 ms                                                   | 693 ms: 1.45x slower                                                    |
| nqueens                   | 105 ms                                                   | 153 ms: 1.46x slower                                                    |
| deepcopy_reduce           | 4.24 us                                                  | 6.22 us: 1.46x slower                                                   |
| bench_thread_pool         | 1.34 ms                                                  | 1.96 ms: 1.47x slower                                                   |
| comprehensions            | 20.8 us                                                  | 30.8 us: 1.48x slower                                                   |
| bpe_tokeniser             | 6.02 sec                                                 | 8.94 sec: 1.49x slower                                                  |
| sympy_integrate           | 21.4 ms                                                  | 32.0 ms: 1.49x slower                                                   |
| regex_compile             | 134 ms                                                   | 201 ms: 1.50x slower                                                    |
| richards                  | 54.5 ms                                                  | 84.8 ms: 1.56x slower                                                   |
| xml_etree_process         | 82.1 ms                                                  | 128 ms: 1.56x slower                                                    |
| python_startup_no_site    | 8.79 ms                                                  | 13.8 ms: 1.57x slower                                                   |
| unpickle_pure_python      | 265 us                                                   | 418 us: 1.58x slower                                                    |
| sympy_sum                 | 151 ms                                                   | 239 ms: 1.58x slower                                                    |
| scimark_monte_carlo       | 87.8 ms                                                  | 139 ms: 1.58x slower                                                    |
| scimark_lu                | 146 ms                                                   | 232 ms: 1.58x slower                                                    |
| pickle_pure_python        | 374 us                                                   | 593 us: 1.59x slower                                                    |
| genshi_xml                | 61.6 ms                                                  | 98.2 ms: 1.60x slower                                                   |
| xml_etree_generate        | 118 ms                                                   | 189 ms: 1.60x slower                                                    |
| raytrace                  | 310 ms                                                   | 498 ms: 1.61x slower                                                    |
| nbody                     | 118 ms                                                   | 191 ms: 1.61x slower                                                    |
| logging_format            | 8.10 us                                                  | 13.1 us: 1.61x slower                                                   |
| logging_simple            | 7.25 us                                                  | 11.8 us: 1.63x slower                                                   |
| genshi_text               | 28.6 ms                                                  | 46.5 ms: 1.63x slower                                                   |
| pprint_pformat            | 1.99 sec                                                 | 3.27 sec: 1.65x slower                                                  |
| pprint_safe_repr          | 962 ms                                                   | 1.60 sec: 1.66x slower                                                  |
| richards_super            | 60.8 ms                                                  | 101 ms: 1.67x slower                                                    |
| thrift                    | 1.01 ms                                                  | 1.69 ms: 1.68x slower                                                   |
| coverage                  | 106 ms                                                   | 177 ms: 1.68x slower                                                    |
| sympy_str                 | 265 ms                                                   | 450 ms: 1.70x slower                                                    |
| mako                      | 14.0 ms                                                  | 23.8 ms: 1.70x slower                                                   |
| telco                     | 10.5 ms                                                  | 17.8 ms: 1.70x slower                                                   |
| sympy_expand              | 472 ms                                                   | 807 ms: 1.71x slower                                                    |
| crypto_pyaes              | 84.9 ms                                                  | 148 ms: 1.74x slower                                                    |
| typing_runtime_protocols  | 197 us                                                   | 358 us: 1.82x slower                                                    |
| django_template           | 39.4 ms                                                  | 75.2 ms: 1.91x slower                                                   |
| many_optionals            | 626 us                                                   | 1.23 ms: 1.97x slower                                                   |
| subparsers                | 20.3 ms                                                  | 45.6 ms: 2.24x slower                                                   |
| logging_silent            | 135 ns                                                   | 1.13 us: 8.43x slower                                                   |
| bench_mp_pool             | 8.07 ms                                                  | 72.7 ms: 9.01x slower                                                   |
| Geometric mean            | (ref)                                                    | 1.37x slower                                                            |

Benchmark hidden because not significant (3): asyncio_websockets, xml_etree_iterparse, async_tree_cpu_io_mixed_tg
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250617-3.15.0a0-fba5dde-NOGIL/bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.262x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.29x
- 95% likely to have a slowdown of 1.27x
- 99% likely to have a slowdown of 1.23x

# Memory
- memory change: 1.33x