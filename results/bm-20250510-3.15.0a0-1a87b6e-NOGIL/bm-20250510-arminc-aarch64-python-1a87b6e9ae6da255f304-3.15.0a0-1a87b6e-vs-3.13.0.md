# Results vs. 3.13.0

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: linux-aarch64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.070x slower
- HPT reliability: 99.93%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 359 ms: 1.15x slower                                                    |
| docutils       | 2.96 sec                                                 | 3.26 sec: 1.10x slower                                                  |
| html5lib       | 65.6 ms                                                  | 69.0 ms: 1.05x slower                                                   |
| sphinx         | 1.20 sec                                                 | 1.30 sec: 1.08x slower                                                  |
| Geometric mean | (ref)                                                    | 1.09x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 460 ms: 1.44x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 837 ms: 1.39x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 484 ms: 1.37x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 869 ms: 1.31x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 375 ms: 1.29x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 647 ms: 1.24x faster                                                    |
| async_tree_none            | 504 ms                                                   | 416 ms: 1.21x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 681 ms: 1.16x faster                                                    |
| Geometric mean             | (ref)                                                    | 1.21x faster                                                            |

Benchmark hidden because not significant (3): asyncio_websockets, async_generators, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 238 ms                                                   | 232 ms: 1.03x faster                                                    |
| nbody          | 118 ms                                                   | 168 ms: 1.42x slower                                                    |
| Geometric mean | (ref)                                                    | 1.11x slower                                                            |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.06 ms: 1.26x faster                                                   |
| regex_v8       | 32.5 ms                                                  | 27.7 ms: 1.18x faster                                                   |
| regex_dna      | 263 ms                                                   | 238 ms: 1.10x faster                                                    |
| regex_compile  | 134 ms                                                   | 150 ms: 1.12x slower                                                    |
| Geometric mean | (ref)                                                    | 1.10x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse  | 159 ms                                                   | 130 ms: 1.23x faster                                                    |
| xml_etree_parse      | 203 ms                                                   | 176 ms: 1.15x faster                                                    |
| tomli_loads          | 2.67 sec                                                 | 2.88 sec: 1.08x slower                                                  |
| unpickle_pure_python | 265 us                                                   | 302 us: 1.14x slower                                                    |
| json_dumps           | 14.2 ms                                                  | 16.3 ms: 1.14x slower                                                   |
| pickle_pure_python   | 374 us                                                   | 438 us: 1.17x slower                                                    |
| json_loads           | 32.8 us                                                  | 39.0 us: 1.19x slower                                                   |
| xml_etree_generate   | 118 ms                                                   | 144 ms: 1.22x slower                                                    |
| xml_etree_process    | 82.1 ms                                                  | 101 ms: 1.23x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.08x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 20.0 ms: 1.25x slower                                                   |
| python_startup_no_site | 8.79 ms                                                  | 12.2 ms: 1.39x slower                                                   |
| Geometric mean         | (ref)                                                    | 1.32x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 61.6 ms                                                  | 75.7 ms: 1.23x slower                                                   |
| genshi_text     | 28.6 ms                                                  | 35.8 ms: 1.25x slower                                                   |
| django_template | 39.4 ms                                                  | 51.1 ms: 1.30x slower                                                   |
| mako            | 14.0 ms                                                  | 21.4 ms: 1.54x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.32x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| gc_traversal               | 5.92 ms                                                  | 2.93 ms: 2.02x faster                                                   |
| mdp                        | 3.45 sec                                                 | 1.96 sec: 1.76x faster                                                  |
| create_gc_cycles           | 3.39 ms                                                  | 2.33 ms: 1.46x faster                                                   |
| async_tree_memoization_tg  | 663 ms                                                   | 460 ms: 1.44x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 837 ms: 1.39x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 484 ms: 1.37x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 869 ms: 1.31x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 375 ms: 1.29x faster                                                    |
| regex_effbot               | 5.10 ms                                                  | 4.06 ms: 1.26x faster                                                   |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 647 ms: 1.24x faster                                                    |
| xml_etree_iterparse        | 159 ms                                                   | 130 ms: 1.23x faster                                                    |
| async_tree_none            | 504 ms                                                   | 416 ms: 1.21x faster                                                    |
| deepcopy                   | 479 us                                                   | 401 us: 1.19x faster                                                    |
| regex_v8                   | 32.5 ms                                                  | 27.7 ms: 1.18x faster                                                   |
| sqlite_synth               | 4.08 us                                                  | 3.50 us: 1.17x faster                                                   |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 681 ms: 1.16x faster                                                    |
| xml_etree_parse            | 203 ms                                                   | 176 ms: 1.15x faster                                                    |
| deepcopy_memo              | 53.0 us                                                  | 47.7 us: 1.11x faster                                                   |
| regex_dna                  | 263 ms                                                   | 238 ms: 1.10x faster                                                    |
| pathlib                    | 24.3 ms                                                  | 23.1 ms: 1.06x faster                                                   |
| spectral_norm              | 143 ms                                                   | 138 ms: 1.04x faster                                                    |
| pidigits                   | 238 ms                                                   | 232 ms: 1.03x faster                                                    |
| pycparser                  | 1.34 sec                                                 | 1.39 sec: 1.03x slower                                                  |
| pyflate                    | 582 ms                                                   | 608 ms: 1.05x slower                                                    |
| html5lib                   | 65.6 ms                                                  | 69.0 ms: 1.05x slower                                                   |
| k_core                     | 2.99 sec                                                 | 3.21 sec: 1.07x slower                                                  |
| telco                      | 10.5 ms                                                  | 11.2 ms: 1.08x slower                                                   |
| tomli_loads                | 2.67 sec                                                 | 2.88 sec: 1.08x slower                                                  |
| sphinx                     | 1.20 sec                                                 | 1.30 sec: 1.08x slower                                                  |
| pylint                     | 345 ms                                                   | 374 ms: 1.08x slower                                                    |
| json                       | 5.94 ms                                                  | 6.48 ms: 1.09x slower                                                   |
| hexiom                     | 7.34 ms                                                  | 8.03 ms: 1.09x slower                                                   |
| docutils                   | 2.96 sec                                                 | 3.26 sec: 1.10x slower                                                  |
| pprint_pformat             | 1.99 sec                                                 | 2.20 sec: 1.11x slower                                                  |
| pprint_safe_repr           | 962 ms                                                   | 1.07 sec: 1.11x slower                                                  |
| regex_compile              | 134 ms                                                   | 150 ms: 1.12x slower                                                    |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 7.52 ms: 1.13x slower                                                   |
| chaos                      | 70.7 ms                                                  | 80.1 ms: 1.13x slower                                                   |
| unpickle_pure_python       | 265 us                                                   | 302 us: 1.14x slower                                                    |
| json_dumps                 | 14.2 ms                                                  | 16.3 ms: 1.14x slower                                                   |
| 2to3                       | 313 ms                                                   | 359 ms: 1.15x slower                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 6.93 sec: 1.15x slower                                                  |
| nqueens                    | 105 ms                                                   | 121 ms: 1.15x slower                                                    |
| pickle_pure_python         | 374 us                                                   | 438 us: 1.17x slower                                                    |
| thrift                     | 1.01 ms                                                  | 1.19 ms: 1.17x slower                                                   |
| shortest_path              | 565 ms                                                   | 669 ms: 1.18x slower                                                    |
| json_loads                 | 32.8 us                                                  | 39.0 us: 1.19x slower                                                   |
| scimark_lu                 | 146 ms                                                   | 174 ms: 1.19x slower                                                    |
| sympy_integrate            | 21.4 ms                                                  | 25.7 ms: 1.20x slower                                                   |
| deltablue                  | 3.97 ms                                                  | 4.78 ms: 1.21x slower                                                   |
| connected_components       | 547 ms                                                   | 661 ms: 1.21x slower                                                    |
| xml_etree_generate         | 118 ms                                                   | 144 ms: 1.22x slower                                                    |
| scimark_monte_carlo        | 87.8 ms                                                  | 107 ms: 1.22x slower                                                    |
| xml_etree_process          | 82.1 ms                                                  | 101 ms: 1.23x slower                                                    |
| genshi_xml                 | 61.6 ms                                                  | 75.7 ms: 1.23x slower                                                   |
| comprehensions             | 20.8 us                                                  | 25.6 us: 1.23x slower                                                   |
| sympy_sum                  | 151 ms                                                   | 188 ms: 1.24x slower                                                    |
| logging_format             | 8.10 us                                                  | 10.1 us: 1.24x slower                                                   |
| python_startup             | 16.0 ms                                                  | 20.0 ms: 1.25x slower                                                   |
| genshi_text                | 28.6 ms                                                  | 35.8 ms: 1.25x slower                                                   |
| richards                   | 54.5 ms                                                  | 68.5 ms: 1.26x slower                                                   |
| sympy_expand               | 472 ms                                                   | 597 ms: 1.26x slower                                                    |
| sympy_str                  | 265 ms                                                   | 338 ms: 1.28x slower                                                    |
| raytrace                   | 310 ms                                                   | 396 ms: 1.28x slower                                                    |
| logging_simple             | 7.25 us                                                  | 9.29 us: 1.28x slower                                                   |
| meteor_contest             | 117 ms                                                   | 150 ms: 1.29x slower                                                    |
| richards_super             | 60.8 ms                                                  | 78.5 ms: 1.29x slower                                                   |
| fannkuch                   | 478 ms                                                   | 619 ms: 1.29x slower                                                    |
| django_template            | 39.4 ms                                                  | 51.1 ms: 1.30x slower                                                   |
| crypto_pyaes               | 84.9 ms                                                  | 111 ms: 1.30x slower                                                    |
| typing_runtime_protocols   | 197 us                                                   | 261 us: 1.33x slower                                                    |
| bench_thread_pool          | 1.34 ms                                                  | 1.84 ms: 1.37x slower                                                   |
| python_startup_no_site     | 8.79 ms                                                  | 12.2 ms: 1.39x slower                                                   |
| nbody                      | 118 ms                                                   | 168 ms: 1.42x slower                                                    |
| coverage                   | 106 ms                                                   | 150 ms: 1.42x slower                                                    |
| mako                       | 14.0 ms                                                  | 21.4 ms: 1.54x slower                                                   |
| subparsers                 | 20.3 ms                                                  | 33.7 ms: 1.66x slower                                                   |
| many_optionals             | 626 us                                                   | 1.05 ms: 1.67x slower                                                   |
| logging_silent             | 135 ns                                                   | 763 ns: 5.67x slower                                                    |
| bench_mp_pool              | 8.07 ms                                                  | 61.6 ms: 7.64x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.11x slower                                                            |

Benchmark hidden because not significant (9): go, generators, scimark_sor, asyncio_websockets, float, async_generators, scimark_fft, deepcopy_reduce, coroutines
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250510-3.15.0a0-1a87b6e-NOGIL/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.070x slower

# HPT report

- Reliability score: 99.93% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.28x