# Results vs. 3.13.0

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: linux-aarch64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.264x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x slower
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 447 ms: 1.43x slower                                                    |
| docutils       | 2.96 sec                                                 | 3.92 sec: 1.32x slower                                                  |
| html5lib       | 65.6 ms                                                  | 82.9 ms: 1.26x slower                                                   |
| sphinx         | 1.20 sec                                                 | 1.60 sec: 1.33x slower                                                  |
| Geometric mean | (ref)                                                    | 1.34x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|---------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg | 663 ms                                                   | 521 ms: 1.27x faster                                                    |
| async_tree_io_tg          | 1.16 sec                                                 | 983 ms: 1.18x faster                                                    |
| async_tree_memoization    | 664 ms                                                   | 560 ms: 1.18x faster                                                    |
| async_tree_none_tg        | 484 ms                                                   | 430 ms: 1.13x faster                                                    |
| async_tree_io             | 1.14 sec                                                 | 1.01 sec: 1.12x faster                                                  |
| async_tree_none           | 504 ms                                                   | 466 ms: 1.08x faster                                                    |
| async_tree_cpu_io_mixed   | 789 ms                                                   | 847 ms: 1.07x slower                                                    |
| async_generators          | 500 ms                                                   | 626 ms: 1.25x slower                                                    |
| coroutines                | 29.4 ms                                                  | 38.4 ms: 1.30x slower                                                   |
| Geometric mean            | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 106 ms: 1.11x slower                                                    |
| pidigits       | 238 ms                                                   | 277 ms: 1.16x slower                                                    |
| nbody          | 118 ms                                                   | 192 ms: 1.62x slower                                                    |
| Geometric mean | (ref)                                                    | 1.28x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.20 ms: 1.22x faster                                                   |
| regex_dna      | 263 ms                                                   | 233 ms: 1.13x faster                                                    |
| regex_v8       | 32.5 ms                                                  | 30.8 ms: 1.06x faster                                                   |
| regex_compile  | 134 ms                                                   | 196 ms: 1.47x slower                                                    |
| Geometric mean | (ref)                                                    | 1.00x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 203 ms                                                   | 236 ms: 1.17x slower                                                    |
| tomli_loads          | 2.67 sec                                                 | 3.55 sec: 1.33x slower                                                  |
| json_loads           | 32.8 us                                                  | 44.9 us: 1.37x slower                                                   |
| json_dumps           | 14.2 ms                                                  | 19.7 ms: 1.39x slower                                                   |
| pickle_pure_python   | 374 us                                                   | 580 us: 1.55x slower                                                    |
| xml_etree_process    | 82.1 ms                                                  | 129 ms: 1.57x slower                                                    |
| unpickle_pure_python | 265 us                                                   | 420 us: 1.58x slower                                                    |
| xml_etree_generate   | 118 ms                                                   | 192 ms: 1.62x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.38x slower                                                            |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 22.9 ms: 1.43x slower                                                   |
| python_startup_no_site | 8.79 ms                                                  | 13.8 ms: 1.57x slower                                                   |
| Geometric mean         | (ref)                                                    | 1.50x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 61.6 ms                                                  | 97.3 ms: 1.58x slower                                                   |
| genshi_text     | 28.6 ms                                                  | 46.0 ms: 1.61x slower                                                   |
| mako            | 14.0 ms                                                  | 24.1 ms: 1.73x slower                                                   |
| django_template | 39.4 ms                                                  | 73.3 ms: 1.86x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.69x slower                                                            |

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|---------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| gc_traversal              | 5.92 ms                                                  | 3.58 ms: 1.65x faster                                                   |
| create_gc_cycles          | 3.39 ms                                                  | 2.49 ms: 1.36x faster                                                   |
| mdp                       | 3.45 sec                                                 | 2.54 sec: 1.36x faster                                                  |
| async_tree_memoization_tg | 663 ms                                                   | 521 ms: 1.27x faster                                                    |
| regex_effbot              | 5.10 ms                                                  | 4.20 ms: 1.22x faster                                                   |
| async_tree_io_tg          | 1.16 sec                                                 | 983 ms: 1.18x faster                                                    |
| async_tree_memoization    | 664 ms                                                   | 560 ms: 1.18x faster                                                    |
| regex_dna                 | 263 ms                                                   | 233 ms: 1.13x faster                                                    |
| async_tree_none_tg        | 484 ms                                                   | 430 ms: 1.13x faster                                                    |
| async_tree_io             | 1.14 sec                                                 | 1.01 sec: 1.12x faster                                                  |
| async_tree_none           | 504 ms                                                   | 466 ms: 1.08x faster                                                    |
| regex_v8                  | 32.5 ms                                                  | 30.8 ms: 1.06x faster                                                   |
| async_tree_cpu_io_mixed   | 789 ms                                                   | 847 ms: 1.07x slower                                                    |
| deepcopy_memo             | 53.0 us                                                  | 56.9 us: 1.07x slower                                                   |
| k_core                    | 2.99 sec                                                 | 3.25 sec: 1.09x slower                                                  |
| deepcopy                  | 479 us                                                   | 529 us: 1.10x slower                                                    |
| sqlite_synth              | 4.08 us                                                  | 4.51 us: 1.11x slower                                                   |
| go                        | 164 ms                                                   | 182 ms: 1.11x slower                                                    |
| float                     | 95.8 ms                                                  | 106 ms: 1.11x slower                                                    |
| pidigits                  | 238 ms                                                   | 277 ms: 1.16x slower                                                    |
| generators                | 40.3 ms                                                  | 46.9 ms: 1.16x slower                                                   |
| xml_etree_parse           | 203 ms                                                   | 236 ms: 1.17x slower                                                    |
| pyflate                   | 582 ms                                                   | 685 ms: 1.18x slower                                                    |
| pathlib                   | 24.3 ms                                                  | 29.9 ms: 1.23x slower                                                   |
| scimark_sor               | 164 ms                                                   | 204 ms: 1.24x slower                                                    |
| connected_components      | 547 ms                                                   | 682 ms: 1.25x slower                                                    |
| async_generators          | 500 ms                                                   | 626 ms: 1.25x slower                                                    |
| shortest_path             | 565 ms                                                   | 710 ms: 1.26x slower                                                    |
| scimark_fft               | 463 ms                                                   | 583 ms: 1.26x slower                                                    |
| html5lib                  | 65.6 ms                                                  | 82.9 ms: 1.26x slower                                                   |
| pycparser                 | 1.34 sec                                                 | 1.75 sec: 1.30x slower                                                  |
| coroutines                | 29.4 ms                                                  | 38.4 ms: 1.30x slower                                                   |
| meteor_contest            | 117 ms                                                   | 154 ms: 1.31x slower                                                    |
| docutils                  | 2.96 sec                                                 | 3.92 sec: 1.32x slower                                                  |
| sphinx                    | 1.20 sec                                                 | 1.60 sec: 1.33x slower                                                  |
| tomli_loads               | 2.67 sec                                                 | 3.55 sec: 1.33x slower                                                  |
| spectral_norm             | 143 ms                                                   | 193 ms: 1.35x slower                                                    |
| pylint                    | 345 ms                                                   | 468 ms: 1.35x slower                                                    |
| json                      | 5.94 ms                                                  | 8.06 ms: 1.36x slower                                                   |
| scimark_sparse_mat_mult   | 6.66 ms                                                  | 9.05 ms: 1.36x slower                                                   |
| hexiom                    | 7.34 ms                                                  | 10.0 ms: 1.37x slower                                                   |
| json_loads                | 32.8 us                                                  | 44.9 us: 1.37x slower                                                   |
| json_dumps                | 14.2 ms                                                  | 19.7 ms: 1.39x slower                                                   |
| deepcopy_reduce           | 4.24 us                                                  | 5.97 us: 1.41x slower                                                   |
| python_startup            | 16.0 ms                                                  | 22.9 ms: 1.43x slower                                                   |
| chaos                     | 70.7 ms                                                  | 101 ms: 1.43x slower                                                    |
| 2to3                      | 313 ms                                                   | 447 ms: 1.43x slower                                                    |
| deltablue                 | 3.97 ms                                                  | 5.68 ms: 1.43x slower                                                   |
| comprehensions            | 20.8 us                                                  | 30.2 us: 1.45x slower                                                   |
| sympy_integrate           | 21.4 ms                                                  | 31.3 ms: 1.46x slower                                                   |
| bpe_tokeniser             | 6.02 sec                                                 | 8.81 sec: 1.46x slower                                                  |
| regex_compile             | 134 ms                                                   | 196 ms: 1.47x slower                                                    |
| bench_thread_pool         | 1.34 ms                                                  | 1.98 ms: 1.48x slower                                                   |
| nqueens                   | 105 ms                                                   | 156 ms: 1.48x slower                                                    |
| fannkuch                  | 478 ms                                                   | 713 ms: 1.49x slower                                                    |
| pickle_pure_python        | 374 us                                                   | 580 us: 1.55x slower                                                    |
| python_startup_no_site    | 8.79 ms                                                  | 13.8 ms: 1.57x slower                                                   |
| xml_etree_process         | 82.1 ms                                                  | 129 ms: 1.57x slower                                                    |
| genshi_xml                | 61.6 ms                                                  | 97.3 ms: 1.58x slower                                                   |
| scimark_monte_carlo       | 87.8 ms                                                  | 139 ms: 1.58x slower                                                    |
| unpickle_pure_python      | 265 us                                                   | 420 us: 1.58x slower                                                    |
| richards                  | 54.5 ms                                                  | 86.8 ms: 1.59x slower                                                   |
| raytrace                  | 310 ms                                                   | 496 ms: 1.60x slower                                                    |
| logging_format            | 8.10 us                                                  | 13.0 us: 1.60x slower                                                   |
| scimark_lu                | 146 ms                                                   | 234 ms: 1.60x slower                                                    |
| thrift                    | 1.01 ms                                                  | 1.63 ms: 1.61x slower                                                   |
| genshi_text               | 28.6 ms                                                  | 46.0 ms: 1.61x slower                                                   |
| logging_simple            | 7.25 us                                                  | 11.7 us: 1.61x slower                                                   |
| nbody                     | 118 ms                                                   | 192 ms: 1.62x slower                                                    |
| xml_etree_generate        | 118 ms                                                   | 192 ms: 1.62x slower                                                    |
| sympy_sum                 | 151 ms                                                   | 246 ms: 1.63x slower                                                    |
| richards_super            | 60.8 ms                                                  | 101 ms: 1.66x slower                                                    |
| pprint_pformat            | 1.99 sec                                                 | 3.31 sec: 1.67x slower                                                  |
| sympy_expand              | 472 ms                                                   | 790 ms: 1.67x slower                                                    |
| pprint_safe_repr          | 962 ms                                                   | 1.62 sec: 1.68x slower                                                  |
| sympy_str                 | 265 ms                                                   | 449 ms: 1.69x slower                                                    |
| crypto_pyaes              | 84.9 ms                                                  | 145 ms: 1.71x slower                                                    |
| mako                      | 14.0 ms                                                  | 24.1 ms: 1.73x slower                                                   |
| telco                     | 10.5 ms                                                  | 18.1 ms: 1.73x slower                                                   |
| coverage                  | 106 ms                                                   | 184 ms: 1.74x slower                                                    |
| typing_runtime_protocols  | 197 us                                                   | 354 us: 1.79x slower                                                    |
| django_template           | 39.4 ms                                                  | 73.3 ms: 1.86x slower                                                   |
| many_optionals            | 626 us                                                   | 1.37 ms: 2.19x slower                                                   |
| subparsers                | 20.3 ms                                                  | 45.9 ms: 2.26x slower                                                   |
| logging_silent            | 135 ns                                                   | 1.13 us: 8.36x slower                                                   |
| bench_mp_pool             | 8.07 ms                                                  | 72.6 ms: 9.00x slower                                                   |
| Geometric mean            | (ref)                                                    | 1.37x slower                                                            |

Benchmark hidden because not significant (3): xml_etree_iterparse, asyncio_websockets, async_tree_cpu_io_mixed_tg
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250607-3.15.0a0-8fdbbf8-NOGIL/bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.264x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.29x
- 95% likely to have a slowdown of 1.28x
- 99% likely to have a slowdown of 1.24x

# Memory
- memory change: 1.32x