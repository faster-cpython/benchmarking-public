# Results vs. 3.13.0

- fork: python
- ref: cebae977a63f32c3c03d
- machine: linux-aarch64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.261x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x slower
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 443 ms: 1.42x slower                                                    |
| docutils       | 2.96 sec                                                 | 3.90 sec: 1.32x slower                                                  |
| html5lib       | 65.6 ms                                                  | 82.9 ms: 1.26x slower                                                   |
| sphinx         | 1.20 sec                                                 | 1.59 sec: 1.33x slower                                                  |
| Geometric mean | (ref)                                                    | 1.33x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|---------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg | 663 ms                                                   | 523 ms: 1.27x faster                                                    |
| async_tree_memoization    | 664 ms                                                   | 560 ms: 1.19x faster                                                    |
| async_tree_io_tg          | 1.16 sec                                                 | 992 ms: 1.17x faster                                                    |
| async_tree_none_tg        | 484 ms                                                   | 430 ms: 1.13x faster                                                    |
| async_tree_io             | 1.14 sec                                                 | 1.01 sec: 1.12x faster                                                  |
| async_tree_none           | 504 ms                                                   | 469 ms: 1.07x faster                                                    |
| async_tree_cpu_io_mixed   | 789 ms                                                   | 863 ms: 1.09x slower                                                    |
| async_generators          | 500 ms                                                   | 632 ms: 1.26x slower                                                    |
| coroutines                | 29.4 ms                                                  | 38.2 ms: 1.30x slower                                                   |
| Geometric mean            | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 106 ms: 1.10x slower                                                    |
| pidigits       | 238 ms                                                   | 279 ms: 1.17x slower                                                    |
| nbody          | 118 ms                                                   | 191 ms: 1.61x slower                                                    |
| Geometric mean | (ref)                                                    | 1.28x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.12 ms: 1.24x faster                                                   |
| regex_dna      | 263 ms                                                   | 231 ms: 1.14x faster                                                    |
| regex_v8       | 32.5 ms                                                  | 30.0 ms: 1.08x faster                                                   |
| regex_compile  | 134 ms                                                   | 197 ms: 1.48x slower                                                    |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 203 ms                                                   | 232 ms: 1.14x slower                                                    |
| tomli_loads          | 2.67 sec                                                 | 3.61 sec: 1.35x slower                                                  |
| json_loads           | 32.8 us                                                  | 44.6 us: 1.36x slower                                                   |
| json_dumps           | 14.2 ms                                                  | 19.8 ms: 1.39x slower                                                   |
| unpickle_pure_python | 265 us                                                   | 402 us: 1.52x slower                                                    |
| pickle_pure_python   | 374 us                                                   | 569 us: 1.52x slower                                                    |
| xml_etree_process    | 82.1 ms                                                  | 129 ms: 1.57x slower                                                    |
| xml_etree_generate   | 118 ms                                                   | 193 ms: 1.63x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.37x slower                                                            |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 22.9 ms: 1.43x slower                                                   |
| python_startup_no_site | 8.79 ms                                                  | 13.7 ms: 1.56x slower                                                   |
| Geometric mean         | (ref)                                                    | 1.49x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 61.6 ms                                                  | 97.2 ms: 1.58x slower                                                   |
| genshi_text     | 28.6 ms                                                  | 45.5 ms: 1.59x slower                                                   |
| mako            | 14.0 ms                                                  | 23.7 ms: 1.69x slower                                                   |
| django_template | 39.4 ms                                                  | 74.2 ms: 1.88x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.68x slower                                                            |

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|---------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| gc_traversal              | 5.92 ms                                                  | 3.68 ms: 1.61x faster                                                   |
| create_gc_cycles          | 3.39 ms                                                  | 2.45 ms: 1.39x faster                                                   |
| mdp                       | 3.45 sec                                                 | 2.55 sec: 1.35x faster                                                  |
| async_tree_memoization_tg | 663 ms                                                   | 523 ms: 1.27x faster                                                    |
| regex_effbot              | 5.10 ms                                                  | 4.12 ms: 1.24x faster                                                   |
| async_tree_memoization    | 664 ms                                                   | 560 ms: 1.19x faster                                                    |
| async_tree_io_tg          | 1.16 sec                                                 | 992 ms: 1.17x faster                                                    |
| regex_dna                 | 263 ms                                                   | 231 ms: 1.14x faster                                                    |
| async_tree_none_tg        | 484 ms                                                   | 430 ms: 1.13x faster                                                    |
| async_tree_io             | 1.14 sec                                                 | 1.01 sec: 1.12x faster                                                  |
| regex_v8                  | 32.5 ms                                                  | 30.0 ms: 1.08x faster                                                   |
| async_tree_none           | 504 ms                                                   | 469 ms: 1.07x faster                                                    |
| go                        | 164 ms                                                   | 176 ms: 1.07x slower                                                    |
| deepcopy_memo             | 53.0 us                                                  | 57.2 us: 1.08x slower                                                   |
| sqlite_synth              | 4.08 us                                                  | 4.43 us: 1.09x slower                                                   |
| async_tree_cpu_io_mixed   | 789 ms                                                   | 863 ms: 1.09x slower                                                    |
| float                     | 95.8 ms                                                  | 106 ms: 1.10x slower                                                    |
| k_core                    | 2.99 sec                                                 | 3.31 sec: 1.11x slower                                                  |
| deepcopy                  | 479 us                                                   | 530 us: 1.11x slower                                                    |
| xml_etree_parse           | 203 ms                                                   | 232 ms: 1.14x slower                                                    |
| pidigits                  | 238 ms                                                   | 279 ms: 1.17x slower                                                    |
| pyflate                   | 582 ms                                                   | 682 ms: 1.17x slower                                                    |
| generators                | 40.3 ms                                                  | 47.8 ms: 1.18x slower                                                   |
| pathlib                   | 24.3 ms                                                  | 29.2 ms: 1.20x slower                                                   |
| scimark_sor               | 164 ms                                                   | 200 ms: 1.22x slower                                                    |
| connected_components      | 547 ms                                                   | 673 ms: 1.23x slower                                                    |
| async_generators          | 500 ms                                                   | 632 ms: 1.26x slower                                                    |
| html5lib                  | 65.6 ms                                                  | 82.9 ms: 1.26x slower                                                   |
| shortest_path             | 565 ms                                                   | 717 ms: 1.27x slower                                                    |
| pycparser                 | 1.34 sec                                                 | 1.71 sec: 1.27x slower                                                  |
| scimark_fft               | 463 ms                                                   | 590 ms: 1.27x slower                                                    |
| coroutines                | 29.4 ms                                                  | 38.2 ms: 1.30x slower                                                   |
| docutils                  | 2.96 sec                                                 | 3.90 sec: 1.32x slower                                                  |
| spectral_norm             | 143 ms                                                   | 190 ms: 1.32x slower                                                    |
| sphinx                    | 1.20 sec                                                 | 1.59 sec: 1.33x slower                                                  |
| pylint                    | 345 ms                                                   | 459 ms: 1.33x slower                                                    |
| hexiom                    | 7.34 ms                                                  | 9.83 ms: 1.34x slower                                                   |
| meteor_contest            | 117 ms                                                   | 157 ms: 1.34x slower                                                    |
| tomli_loads               | 2.67 sec                                                 | 3.61 sec: 1.35x slower                                                  |
| json_loads                | 32.8 us                                                  | 44.6 us: 1.36x slower                                                   |
| scimark_sparse_mat_mult   | 6.66 ms                                                  | 9.08 ms: 1.36x slower                                                   |
| json                      | 5.94 ms                                                  | 8.12 ms: 1.37x slower                                                   |
| json_dumps                | 14.2 ms                                                  | 19.8 ms: 1.39x slower                                                   |
| deltablue                 | 3.97 ms                                                  | 5.57 ms: 1.41x slower                                                   |
| deepcopy_reduce           | 4.24 us                                                  | 6.01 us: 1.41x slower                                                   |
| 2to3                      | 313 ms                                                   | 443 ms: 1.42x slower                                                    |
| python_startup            | 16.0 ms                                                  | 22.9 ms: 1.43x slower                                                   |
| bpe_tokeniser             | 6.02 sec                                                 | 8.69 sec: 1.44x slower                                                  |
| comprehensions            | 20.8 us                                                  | 30.2 us: 1.45x slower                                                   |
| chaos                     | 70.7 ms                                                  | 103 ms: 1.45x slower                                                    |
| fannkuch                  | 478 ms                                                   | 701 ms: 1.47x slower                                                    |
| nqueens                   | 105 ms                                                   | 155 ms: 1.47x slower                                                    |
| sympy_integrate           | 21.4 ms                                                  | 31.6 ms: 1.47x slower                                                   |
| regex_compile             | 134 ms                                                   | 197 ms: 1.48x slower                                                    |
| bench_thread_pool         | 1.34 ms                                                  | 2.00 ms: 1.50x slower                                                   |
| scimark_monte_carlo       | 87.8 ms                                                  | 133 ms: 1.51x slower                                                    |
| unpickle_pure_python      | 265 us                                                   | 402 us: 1.52x slower                                                    |
| pickle_pure_python        | 374 us                                                   | 569 us: 1.52x slower                                                    |
| scimark_lu                | 146 ms                                                   | 225 ms: 1.54x slower                                                    |
| python_startup_no_site    | 8.79 ms                                                  | 13.7 ms: 1.56x slower                                                   |
| xml_etree_process         | 82.1 ms                                                  | 129 ms: 1.57x slower                                                    |
| genshi_xml                | 61.6 ms                                                  | 97.2 ms: 1.58x slower                                                   |
| logging_format            | 8.10 us                                                  | 12.8 us: 1.58x slower                                                   |
| sympy_sum                 | 151 ms                                                   | 240 ms: 1.59x slower                                                    |
| logging_simple            | 7.25 us                                                  | 11.5 us: 1.59x slower                                                   |
| genshi_text               | 28.6 ms                                                  | 45.5 ms: 1.59x slower                                                   |
| richards                  | 54.5 ms                                                  | 87.3 ms: 1.60x slower                                                   |
| raytrace                  | 310 ms                                                   | 498 ms: 1.61x slower                                                    |
| nbody                     | 118 ms                                                   | 191 ms: 1.61x slower                                                    |
| thrift                    | 1.01 ms                                                  | 1.63 ms: 1.62x slower                                                   |
| xml_etree_generate        | 118 ms                                                   | 193 ms: 1.63x slower                                                    |
| pprint_pformat            | 1.99 sec                                                 | 3.27 sec: 1.65x slower                                                  |
| richards_super            | 60.8 ms                                                  | 100 ms: 1.65x slower                                                    |
| pprint_safe_repr          | 962 ms                                                   | 1.59 sec: 1.66x slower                                                  |
| sympy_expand              | 472 ms                                                   | 785 ms: 1.66x slower                                                    |
| mako                      | 14.0 ms                                                  | 23.7 ms: 1.69x slower                                                   |
| sympy_str                 | 265 ms                                                   | 450 ms: 1.70x slower                                                    |
| telco                     | 10.5 ms                                                  | 17.9 ms: 1.71x slower                                                   |
| crypto_pyaes              | 84.9 ms                                                  | 147 ms: 1.73x slower                                                    |
| coverage                  | 106 ms                                                   | 184 ms: 1.74x slower                                                    |
| typing_runtime_protocols  | 197 us                                                   | 354 us: 1.80x slower                                                    |
| django_template           | 39.4 ms                                                  | 74.2 ms: 1.88x slower                                                   |
| many_optionals            | 626 us                                                   | 1.37 ms: 2.19x slower                                                   |
| subparsers                | 20.3 ms                                                  | 46.2 ms: 2.27x slower                                                   |
| logging_silent            | 135 ns                                                   | 1.20 us: 8.89x slower                                                   |
| bench_mp_pool             | 8.07 ms                                                  | 72.0 ms: 8.92x slower                                                   |
| Geometric mean            | (ref)                                                    | 1.37x slower                                                            |

Benchmark hidden because not significant (3): xml_etree_iterparse, asyncio_websockets, async_tree_cpu_io_mixed_tg
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250601-3.15.0a0-cebae97-NOGIL/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.261x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.29x
- 95% likely to have a slowdown of 1.27x
- 99% likely to have a slowdown of 1.24x

# Memory
- memory change: 1.32x