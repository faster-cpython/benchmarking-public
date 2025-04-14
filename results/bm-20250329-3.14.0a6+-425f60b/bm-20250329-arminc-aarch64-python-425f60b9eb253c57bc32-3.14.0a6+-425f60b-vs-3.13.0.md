# Results vs. 3.13.0

- fork: python
- ref: 425f60b9eb253c57bc32
- machine: linux-aarch64
- commit hash: 425f60b
- commit date: 2025-03-29
- overall geometric mean: 1.060x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 297 ms: 1.05x faster                                                     |
| html5lib       | 65.6 ms                                                  | 63.3 ms: 1.04x faster                                                    |
| sphinx         | 1.20 sec                                                 | 1.14 sec: 1.05x faster                                                   |
| Geometric mean | (ref)                                                    | 1.04x faster                                                             |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 465 ms: 1.43x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 470 ms: 1.41x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 890 ms: 1.31x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 876 ms: 1.30x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 374 ms: 1.30x faster                                                     |
| async_tree_none            | 504 ms                                                   | 392 ms: 1.29x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 642 ms: 1.25x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 660 ms: 1.20x faster                                                     |
| async_generators           | 500 ms                                                   | 441 ms: 1.14x faster                                                     |
| Geometric mean             | (ref)                                                    | 1.23x faster                                                             |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 85.6 ms: 1.12x faster                                                    |
| nbody          | 118 ms                                                   | 128 ms: 1.08x slower                                                     |
| Geometric mean | (ref)                                                    | 1.02x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.99 ms: 1.28x faster                                                    |
| regex_v8       | 32.5 ms                                                  | 28.4 ms: 1.14x faster                                                    |
| regex_compile  | 134 ms                                                   | 123 ms: 1.08x faster                                                     |
| regex_dna      | 263 ms                                                   | 246 ms: 1.07x faster                                                     |
| Geometric mean | (ref)                                                    | 1.14x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 173 ms: 1.17x faster                                                     |
| xml_etree_iterparse | 159 ms                                                   | 141 ms: 1.13x faster                                                     |
| tomli_loads         | 2.67 sec                                                 | 2.46 sec: 1.08x faster                                                   |
| xml_etree_process   | 82.1 ms                                                  | 78.4 ms: 1.05x faster                                                    |
| json_loads          | 32.8 us                                                  | 35.0 us: 1.07x slower                                                    |
| Geometric mean      | (ref)                                                    | 1.03x faster                                                             |

Benchmark hidden because not significant (4): xml_etree_generate, unpickle_pure_python, pickle_pure_python, json_dumps

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
| genshi_xml     | 61.6 ms                                                  | 59.0 ms: 1.04x faster                                                    |
| mako           | 14.0 ms                                                  | 14.5 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.65 sec: 2.09x faster                                                   |
| async_tree_memoization_tg  | 663 ms                                                   | 465 ms: 1.43x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 470 ms: 1.41x faster                                                     |
| deepcopy                   | 479 us                                                   | 340 us: 1.41x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 39.5 us: 1.34x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 890 ms: 1.31x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 876 ms: 1.30x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 374 ms: 1.30x faster                                                     |
| async_tree_none            | 504 ms                                                   | 392 ms: 1.29x faster                                                     |
| regex_effbot               | 5.10 ms                                                  | 3.99 ms: 1.28x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 642 ms: 1.25x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 660 ms: 1.20x faster                                                     |
| go                         | 164 ms                                                   | 137 ms: 1.20x faster                                                     |
| xml_etree_parse            | 203 ms                                                   | 173 ms: 1.17x faster                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 3.68 us: 1.15x faster                                                    |
| spectral_norm              | 143 ms                                                   | 125 ms: 1.15x faster                                                     |
| regex_v8                   | 32.5 ms                                                  | 28.4 ms: 1.14x faster                                                    |
| async_generators           | 500 ms                                                   | 441 ms: 1.14x faster                                                     |
| generators                 | 40.3 ms                                                  | 35.7 ms: 1.13x faster                                                    |
| xml_etree_iterparse        | 159 ms                                                   | 141 ms: 1.13x faster                                                     |
| float                      | 95.8 ms                                                  | 85.6 ms: 1.12x faster                                                    |
| scimark_sor                | 164 ms                                                   | 147 ms: 1.12x faster                                                     |
| pylint                     | 345 ms                                                   | 310 ms: 1.11x faster                                                     |
| pathlib                    | 24.3 ms                                                  | 21.9 ms: 1.11x faster                                                    |
| scimark_fft                | 463 ms                                                   | 422 ms: 1.10x faster                                                     |
| telco                      | 10.5 ms                                                  | 9.58 ms: 1.09x faster                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 5.55 sec: 1.08x faster                                                   |
| tomli_loads                | 2.67 sec                                                 | 2.46 sec: 1.08x faster                                                   |
| regex_compile              | 134 ms                                                   | 123 ms: 1.08x faster                                                     |
| pycparser                  | 1.34 sec                                                 | 1.25 sec: 1.08x faster                                                   |
| k_core                     | 2.99 sec                                                 | 2.78 sec: 1.08x faster                                                   |
| richards                   | 54.5 ms                                                  | 50.7 ms: 1.07x faster                                                    |
| regex_dna                  | 263 ms                                                   | 246 ms: 1.07x faster                                                     |
| coverage                   | 106 ms                                                   | 99.0 ms: 1.07x faster                                                    |
| sympy_sum                  | 151 ms                                                   | 142 ms: 1.06x faster                                                     |
| sqlite_synth               | 4.08 us                                                  | 3.84 us: 1.06x faster                                                    |
| logging_format             | 8.10 us                                                  | 7.62 us: 1.06x faster                                                    |
| richards_super             | 60.8 ms                                                  | 57.3 ms: 1.06x faster                                                    |
| sqlalchemy_declarative     | 154 ms                                                   | 146 ms: 1.06x faster                                                     |
| 2to3                       | 313 ms                                                   | 297 ms: 1.05x faster                                                     |
| logging_silent             | 135 ns                                                   | 128 ns: 1.05x faster                                                     |
| pyflate                    | 582 ms                                                   | 554 ms: 1.05x faster                                                     |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 6.35 ms: 1.05x faster                                                    |
| sphinx                     | 1.20 sec                                                 | 1.14 sec: 1.05x faster                                                   |
| deltablue                  | 3.97 ms                                                  | 3.79 ms: 1.05x faster                                                    |
| xml_etree_process          | 82.1 ms                                                  | 78.4 ms: 1.05x faster                                                    |
| logging_simple             | 7.25 us                                                  | 6.93 us: 1.05x faster                                                    |
| genshi_xml                 | 61.6 ms                                                  | 59.0 ms: 1.04x faster                                                    |
| meteor_contest             | 117 ms                                                   | 113 ms: 1.04x faster                                                     |
| html5lib                   | 65.6 ms                                                  | 63.3 ms: 1.04x faster                                                    |
| pprint_pformat             | 1.99 sec                                                 | 1.94 sec: 1.03x faster                                                   |
| pprint_safe_repr           | 962 ms                                                   | 938 ms: 1.03x faster                                                     |
| typing_runtime_protocols   | 197 us                                                   | 194 us: 1.02x faster                                                     |
| connected_components       | 547 ms                                                   | 556 ms: 1.02x slower                                                     |
| shortest_path              | 565 ms                                                   | 577 ms: 1.02x slower                                                     |
| mako                       | 14.0 ms                                                  | 14.5 ms: 1.04x slower                                                    |
| fannkuch                   | 478 ms                                                   | 502 ms: 1.05x slower                                                     |
| json_loads                 | 32.8 us                                                  | 35.0 us: 1.07x slower                                                    |
| create_gc_cycles           | 3.39 ms                                                  | 3.63 ms: 1.07x slower                                                    |
| nbody                      | 118 ms                                                   | 128 ms: 1.08x slower                                                     |
| gc_traversal               | 5.92 ms                                                  | 6.65 ms: 1.12x slower                                                    |
| python_startup_no_site     | 8.79 ms                                                  | 10.2 ms: 1.16x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 25.6 ms: 1.26x slower                                                    |
| many_optionals             | 626 us                                                   | 836 us: 1.33x slower                                                     |
| bench_mp_pool              | 8.07 ms                                                  | 1.93 sec: 239.30x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (25): scimark_monte_carlo, genshi_text, scimark_lu, xml_etree_generate, sqlalchemy_imperative, sympy_integrate, json, chaos, nqueens, sympy_expand, unpickle_pure_python, pidigits, asyncio_websockets, sympy_str, hexiom, docutils, bench_thread_pool, crypto_pyaes, coroutines, raytrace, django_template, python_startup, comprehensions, pickle_pure_python, json_dumps
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (13) of results/bm-20250329-3.14.0a6+-425f60b/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.060x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.04x