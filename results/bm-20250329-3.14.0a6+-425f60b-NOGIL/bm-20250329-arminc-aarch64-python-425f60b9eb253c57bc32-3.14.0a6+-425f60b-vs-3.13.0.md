# Results vs. 3.13.0

- fork: python
- ref: 425f60b9eb253c57bc32
- machine: linux-aarch64
- commit hash: 425f60b
- commit date: 2025-03-29
- overall geometric mean: 1.089x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 359 ms: 1.15x slower                                                     |
| docutils       | 2.96 sec                                                 | 3.31 sec: 1.12x slower                                                   |
| html5lib       | 65.6 ms                                                  | 74.7 ms: 1.14x slower                                                    |
| sphinx         | 1.20 sec                                                 | 1.34 sec: 1.12x slower                                                   |
| Geometric mean | (ref)                                                    | 1.13x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 457 ms: 1.45x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 861 ms: 1.35x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 497 ms: 1.34x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 375 ms: 1.29x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 904 ms: 1.26x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 640 ms: 1.25x faster                                                     |
| async_tree_none            | 504 ms                                                   | 418 ms: 1.20x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 683 ms: 1.16x faster                                                     |
| async_generators           | 500 ms                                                   | 519 ms: 1.04x slower                                                     |
| Geometric mean             | (ref)                                                    | 1.19x faster                                                             |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 101 ms: 1.05x slower                                                     |
| nbody          | 118 ms                                                   | 182 ms: 1.54x slower                                                     |
| Geometric mean | (ref)                                                    | 1.17x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.95 ms: 1.29x faster                                                    |
| regex_v8       | 32.5 ms                                                  | 27.5 ms: 1.18x faster                                                    |
| regex_dna      | 263 ms                                                   | 253 ms: 1.04x faster                                                     |
| regex_compile  | 134 ms                                                   | 160 ms: 1.20x slower                                                     |
| Geometric mean | (ref)                                                    | 1.07x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_iterparse  | 159 ms                                                   | 130 ms: 1.22x faster                                                     |
| xml_etree_parse      | 203 ms                                                   | 177 ms: 1.14x faster                                                     |
| tomli_loads          | 2.67 sec                                                 | 3.05 sec: 1.14x slower                                                   |
| unpickle_pure_python | 265 us                                                   | 303 us: 1.15x slower                                                     |
| json_dumps           | 14.2 ms                                                  | 16.6 ms: 1.17x slower                                                    |
| json_loads           | 32.8 us                                                  | 38.4 us: 1.17x slower                                                    |
| xml_etree_generate   | 118 ms                                                   | 139 ms: 1.17x slower                                                     |
| pickle_pure_python   | 374 us                                                   | 448 us: 1.20x slower                                                     |
| xml_etree_process    | 82.1 ms                                                  | 100 ms: 1.22x slower                                                     |
| Geometric mean       | (ref)                                                    | 1.09x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 19.6 ms: 1.22x slower                                                    |
| python_startup_no_site | 8.79 ms                                                  | 14.0 ms: 1.59x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.40x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 61.6 ms                                                  | 74.0 ms: 1.20x slower                                                    |
| genshi_text     | 28.6 ms                                                  | 36.5 ms: 1.28x slower                                                    |
| django_template | 39.4 ms                                                  | 53.9 ms: 1.37x slower                                                    |
| mako            | 14.0 ms                                                  | 22.3 ms: 1.60x slower                                                    |
| Geometric mean  | (ref)                                                    | 1.35x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| gc_traversal               | 5.92 ms                                                  | 2.69 ms: 2.20x faster                                                    |
| mdp                        | 3.45 sec                                                 | 1.99 sec: 1.73x faster                                                   |
| create_gc_cycles           | 3.39 ms                                                  | 2.12 ms: 1.60x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 457 ms: 1.45x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 861 ms: 1.35x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 497 ms: 1.34x faster                                                     |
| regex_effbot               | 5.10 ms                                                  | 3.95 ms: 1.29x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 375 ms: 1.29x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 904 ms: 1.26x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 640 ms: 1.25x faster                                                     |
| xml_etree_iterparse        | 159 ms                                                   | 130 ms: 1.22x faster                                                     |
| async_tree_none            | 504 ms                                                   | 418 ms: 1.20x faster                                                     |
| deepcopy                   | 479 us                                                   | 401 us: 1.20x faster                                                     |
| regex_v8                   | 32.5 ms                                                  | 27.5 ms: 1.18x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 683 ms: 1.16x faster                                                     |
| xml_etree_parse            | 203 ms                                                   | 177 ms: 1.14x faster                                                     |
| sqlite_synth               | 4.08 us                                                  | 3.59 us: 1.14x faster                                                    |
| pathlib                    | 24.3 ms                                                  | 23.1 ms: 1.05x faster                                                    |
| deepcopy_memo              | 53.0 us                                                  | 50.7 us: 1.04x faster                                                    |
| regex_dna                  | 263 ms                                                   | 253 ms: 1.04x faster                                                     |
| pycparser                  | 1.34 sec                                                 | 1.39 sec: 1.03x slower                                                   |
| async_generators           | 500 ms                                                   | 519 ms: 1.04x slower                                                     |
| scimark_fft                | 463 ms                                                   | 480 ms: 1.04x slower                                                     |
| k_core                     | 2.99 sec                                                 | 3.11 sec: 1.04x slower                                                   |
| go                         | 164 ms                                                   | 171 ms: 1.04x slower                                                     |
| float                      | 95.8 ms                                                  | 101 ms: 1.05x slower                                                     |
| pyflate                    | 582 ms                                                   | 627 ms: 1.08x slower                                                     |
| pylint                     | 345 ms                                                   | 374 ms: 1.08x slower                                                     |
| json                       | 5.94 ms                                                  | 6.47 ms: 1.09x slower                                                    |
| logging_silent             | 135 ns                                                   | 148 ns: 1.10x slower                                                     |
| telco                      | 10.5 ms                                                  | 11.5 ms: 1.10x slower                                                    |
| docutils                   | 2.96 sec                                                 | 3.31 sec: 1.12x slower                                                   |
| sphinx                     | 1.20 sec                                                 | 1.34 sec: 1.12x slower                                                   |
| html5lib                   | 65.6 ms                                                  | 74.7 ms: 1.14x slower                                                    |
| tomli_loads                | 2.67 sec                                                 | 3.05 sec: 1.14x slower                                                   |
| unpickle_pure_python       | 265 us                                                   | 303 us: 1.15x slower                                                     |
| 2to3                       | 313 ms                                                   | 359 ms: 1.15x slower                                                     |
| pprint_safe_repr           | 962 ms                                                   | 1.10 sec: 1.15x slower                                                   |
| pprint_pformat             | 1.99 sec                                                 | 2.29 sec: 1.15x slower                                                   |
| nqueens                    | 105 ms                                                   | 121 ms: 1.15x slower                                                     |
| json_dumps                 | 14.2 ms                                                  | 16.6 ms: 1.17x slower                                                    |
| json_loads                 | 32.8 us                                                  | 38.4 us: 1.17x slower                                                    |
| hexiom                     | 7.34 ms                                                  | 8.61 ms: 1.17x slower                                                    |
| xml_etree_generate         | 118 ms                                                   | 139 ms: 1.17x slower                                                     |
| connected_components       | 547 ms                                                   | 647 ms: 1.18x slower                                                     |
| bpe_tokeniser              | 6.02 sec                                                 | 7.18 sec: 1.19x slower                                                   |
| shortest_path              | 565 ms                                                   | 676 ms: 1.20x slower                                                     |
| pickle_pure_python         | 374 us                                                   | 448 us: 1.20x slower                                                     |
| regex_compile              | 134 ms                                                   | 160 ms: 1.20x slower                                                     |
| genshi_xml                 | 61.6 ms                                                  | 74.0 ms: 1.20x slower                                                    |
| chaos                      | 70.7 ms                                                  | 85.1 ms: 1.20x slower                                                    |
| logging_format             | 8.10 us                                                  | 9.75 us: 1.20x slower                                                    |
| logging_simple             | 7.25 us                                                  | 8.80 us: 1.21x slower                                                    |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 8.11 ms: 1.22x slower                                                    |
| xml_etree_process          | 82.1 ms                                                  | 100 ms: 1.22x slower                                                     |
| python_startup             | 16.0 ms                                                  | 19.6 ms: 1.22x slower                                                    |
| sympy_sum                  | 151 ms                                                   | 191 ms: 1.26x slower                                                     |
| deltablue                  | 3.97 ms                                                  | 5.01 ms: 1.26x slower                                                    |
| scimark_lu                 | 146 ms                                                   | 186 ms: 1.27x slower                                                     |
| sqlalchemy_declarative     | 154 ms                                                   | 196 ms: 1.27x slower                                                     |
| sympy_expand               | 472 ms                                                   | 603 ms: 1.28x slower                                                     |
| genshi_text                | 28.6 ms                                                  | 36.5 ms: 1.28x slower                                                    |
| meteor_contest             | 117 ms                                                   | 150 ms: 1.28x slower                                                     |
| sympy_integrate            | 21.4 ms                                                  | 27.4 ms: 1.28x slower                                                    |
| scimark_monte_carlo        | 87.8 ms                                                  | 113 ms: 1.28x slower                                                     |
| comprehensions             | 20.8 us                                                  | 26.8 us: 1.29x slower                                                    |
| raytrace                   | 310 ms                                                   | 405 ms: 1.31x slower                                                     |
| fannkuch                   | 478 ms                                                   | 625 ms: 1.31x slower                                                     |
| sqlalchemy_imperative      | 16.1 ms                                                  | 21.2 ms: 1.32x slower                                                    |
| crypto_pyaes               | 84.9 ms                                                  | 113 ms: 1.33x slower                                                     |
| sympy_str                  | 265 ms                                                   | 353 ms: 1.33x slower                                                     |
| typing_runtime_protocols   | 197 us                                                   | 265 us: 1.34x slower                                                     |
| richards                   | 54.5 ms                                                  | 73.9 ms: 1.36x slower                                                    |
| bench_thread_pool          | 1.34 ms                                                  | 1.82 ms: 1.36x slower                                                    |
| django_template            | 39.4 ms                                                  | 53.9 ms: 1.37x slower                                                    |
| richards_super             | 60.8 ms                                                  | 83.8 ms: 1.38x slower                                                    |
| coverage                   | 106 ms                                                   | 149 ms: 1.41x slower                                                     |
| nbody                      | 118 ms                                                   | 182 ms: 1.54x slower                                                     |
| subparsers                 | 20.3 ms                                                  | 31.6 ms: 1.55x slower                                                    |
| python_startup_no_site     | 8.79 ms                                                  | 14.0 ms: 1.59x slower                                                    |
| mako                       | 14.0 ms                                                  | 22.3 ms: 1.60x slower                                                    |
| many_optionals             | 626 us                                                   | 1.02 ms: 1.63x slower                                                    |
| bench_mp_pool              | 8.07 ms                                                  | 57.2 ms: 7.09x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.11x slower                                                             |

Benchmark hidden because not significant (7): generators, spectral_norm, pidigits, asyncio_websockets, scimark_sor, deepcopy_reduce, coroutines
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (13) of results/bm-20250329-3.14.0a6+-425f60b-NOGIL/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.089x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 1.26x