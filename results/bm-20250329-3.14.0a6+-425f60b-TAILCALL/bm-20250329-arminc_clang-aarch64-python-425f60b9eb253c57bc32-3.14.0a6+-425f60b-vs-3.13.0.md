# Results vs. 3.13.0

- fork: python
- ref: 425f60b9eb253c57bc32
- machine: linux-aarch64
- commit hash: 425f60b
- commit date: 2025-03-29
- overall geometric mean: 1.075x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 292 ms: 1.07x faster                                                     |
| html5lib       | 65.6 ms                                                  | 59.7 ms: 1.10x faster                                                    |
| sphinx         | 1.20 sec                                                 | 1.11 sec: 1.09x faster                                                   |
| Geometric mean | (ref)                                                    | 1.07x faster                                                             |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 453 ms: 1.46x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 455 ms: 1.46x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 364 ms: 1.33x faster                                                     |
| async_tree_none            | 504 ms                                                   | 382 ms: 1.32x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 870 ms: 1.31x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 898 ms: 1.30x faster                                                     |
| async_generators           | 500 ms                                                   | 414 ms: 1.21x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 709 ms: 1.13x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 721 ms: 1.10x faster                                                     |
| Geometric mean             | (ref)                                                    | 1.23x faster                                                             |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 83.2 ms: 1.15x faster                                                    |
| nbody          | 118 ms                                                   | 113 ms: 1.05x faster                                                     |
| pidigits       | 238 ms                                                   | 293 ms: 1.23x slower                                                     |
| Geometric mean | (ref)                                                    | 1.01x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.17 ms: 1.22x faster                                                    |
| regex_dna      | 263 ms                                                   | 243 ms: 1.08x faster                                                     |
| regex_compile  | 134 ms                                                   | 123 ms: 1.08x faster                                                     |
| regex_v8       | 32.5 ms                                                  | 30.3 ms: 1.07x faster                                                    |
| Geometric mean | (ref)                                                    | 1.11x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads         | 2.67 sec                                                 | 2.39 sec: 1.12x faster                                                   |
| xml_etree_process   | 82.1 ms                                                  | 74.2 ms: 1.11x faster                                                    |
| xml_etree_generate  | 118 ms                                                   | 107 ms: 1.11x faster                                                     |
| xml_etree_iterparse | 159 ms                                                   | 148 ms: 1.07x faster                                                     |
| Geometric mean      | (ref)                                                    | 1.05x faster                                                             |

Benchmark hidden because not significant (5): unpickle_pure_python, json_dumps, xml_etree_parse, json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 10.2 ms: 1.16x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.08x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text    | 28.6 ms                                                  | 26.3 ms: 1.09x faster                                                    |
| genshi_xml     | 61.6 ms                                                  | 58.9 ms: 1.04x faster                                                    |
| Geometric mean | (ref)                                                    | 1.03x faster                                                             |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.59 sec: 2.16x faster                                                   |
| deepcopy                   | 479 us                                                   | 309 us: 1.55x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 36.2 us: 1.46x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 453 ms: 1.46x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 455 ms: 1.46x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 364 ms: 1.33x faster                                                     |
| async_tree_none            | 504 ms                                                   | 382 ms: 1.32x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 870 ms: 1.31x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 898 ms: 1.30x faster                                                     |
| spectral_norm              | 143 ms                                                   | 112 ms: 1.28x faster                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 3.40 us: 1.25x faster                                                    |
| regex_effbot               | 5.10 ms                                                  | 4.17 ms: 1.22x faster                                                    |
| scimark_fft                | 463 ms                                                   | 382 ms: 1.21x faster                                                     |
| async_generators           | 500 ms                                                   | 414 ms: 1.21x faster                                                     |
| go                         | 164 ms                                                   | 136 ms: 1.21x faster                                                     |
| scimark_sor                | 164 ms                                                   | 138 ms: 1.19x faster                                                     |
| logging_silent             | 135 ns                                                   | 115 ns: 1.17x faster                                                     |
| generators                 | 40.3 ms                                                  | 34.7 ms: 1.16x faster                                                    |
| telco                      | 10.5 ms                                                  | 9.05 ms: 1.16x faster                                                    |
| float                      | 95.8 ms                                                  | 83.2 ms: 1.15x faster                                                    |
| pathlib                    | 24.3 ms                                                  | 21.2 ms: 1.15x faster                                                    |
| scimark_monte_carlo        | 87.8 ms                                                  | 76.5 ms: 1.15x faster                                                    |
| pylint                     | 345 ms                                                   | 303 ms: 1.14x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 709 ms: 1.13x faster                                                     |
| bpe_tokeniser              | 6.02 sec                                                 | 5.33 sec: 1.13x faster                                                   |
| richards                   | 54.5 ms                                                  | 48.3 ms: 1.13x faster                                                    |
| tomli_loads                | 2.67 sec                                                 | 2.39 sec: 1.12x faster                                                   |
| pyflate                    | 582 ms                                                   | 521 ms: 1.12x faster                                                     |
| richards_super             | 60.8 ms                                                  | 54.9 ms: 1.11x faster                                                    |
| xml_etree_process          | 82.1 ms                                                  | 74.2 ms: 1.11x faster                                                    |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 6.02 ms: 1.11x faster                                                    |
| xml_etree_generate         | 118 ms                                                   | 107 ms: 1.11x faster                                                     |
| coverage                   | 106 ms                                                   | 95.6 ms: 1.10x faster                                                    |
| html5lib                   | 65.6 ms                                                  | 59.7 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 721 ms: 1.10x faster                                                     |
| scimark_lu                 | 146 ms                                                   | 134 ms: 1.09x faster                                                     |
| sphinx                     | 1.20 sec                                                 | 1.11 sec: 1.09x faster                                                   |
| genshi_text                | 28.6 ms                                                  | 26.3 ms: 1.09x faster                                                    |
| regex_dna                  | 263 ms                                                   | 243 ms: 1.08x faster                                                     |
| regex_compile              | 134 ms                                                   | 123 ms: 1.08x faster                                                     |
| chaos                      | 70.7 ms                                                  | 65.8 ms: 1.08x faster                                                    |
| pycparser                  | 1.34 sec                                                 | 1.25 sec: 1.08x faster                                                   |
| k_core                     | 2.99 sec                                                 | 2.78 sec: 1.07x faster                                                   |
| regex_v8                   | 32.5 ms                                                  | 30.3 ms: 1.07x faster                                                    |
| logging_format             | 8.10 us                                                  | 7.55 us: 1.07x faster                                                    |
| xml_etree_iterparse        | 159 ms                                                   | 148 ms: 1.07x faster                                                     |
| 2to3                       | 313 ms                                                   | 292 ms: 1.07x faster                                                     |
| sympy_integrate            | 21.4 ms                                                  | 20.2 ms: 1.06x faster                                                    |
| sqlite_synth               | 4.08 us                                                  | 3.85 us: 1.06x faster                                                    |
| nbody                      | 118 ms                                                   | 113 ms: 1.05x faster                                                     |
| genshi_xml                 | 61.6 ms                                                  | 58.9 ms: 1.04x faster                                                    |
| pprint_pformat             | 1.99 sec                                                 | 1.90 sec: 1.04x faster                                                   |
| typing_runtime_protocols   | 197 us                                                   | 189 us: 1.04x faster                                                     |
| pprint_safe_repr           | 962 ms                                                   | 934 ms: 1.03x faster                                                     |
| connected_components       | 547 ms                                                   | 563 ms: 1.03x slower                                                     |
| create_gc_cycles           | 3.39 ms                                                  | 3.80 ms: 1.12x slower                                                    |
| gc_traversal               | 5.92 ms                                                  | 6.69 ms: 1.13x slower                                                    |
| python_startup_no_site     | 8.79 ms                                                  | 10.2 ms: 1.16x slower                                                    |
| pidigits                   | 238 ms                                                   | 293 ms: 1.23x slower                                                     |
| subparsers                 | 20.3 ms                                                  | 25.6 ms: 1.26x slower                                                    |
| many_optionals             | 626 us                                                   | 821 us: 1.31x slower                                                     |
| bench_mp_pool              | 8.07 ms                                                  | 2.90 sec: 359.42x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.02x faster                                                             |

Benchmark hidden because not significant (28): sympy_sum, sqlalchemy_declarative, comprehensions, deltablue, nqueens, logging_simple, unpickle_pure_python, coroutines, sympy_expand, meteor_contest, bench_thread_pool, hexiom, json_dumps, raytrace, docutils, django_template, json, asyncio_websockets, sympy_str, xml_etree_parse, sqlalchemy_imperative, python_startup, shortest_path, json_loads, pickle_pure_python, mako, crypto_pyaes, fannkuch
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (13) of results/bm-20250329-3.14.0a6+-425f60b-CLANG/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.075x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.07x