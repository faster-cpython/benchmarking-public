# Results vs. 3.13.0

- fork: python
- ref: 718d234e4086a65d78c8
- machine: linux-aarch64
- commit hash: 718d234
- commit date: 2025-04-12
- overall geometric mean: 1.085x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7+-718d234 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 291 ms: 1.07x faster                                                     |
| docutils       | 2.96 sec                                                 | 2.87 sec: 1.03x faster                                                   |
| html5lib       | 65.6 ms                                                  | 59.6 ms: 1.10x faster                                                    |
| sphinx         | 1.20 sec                                                 | 1.11 sec: 1.08x faster                                                   |
| Geometric mean | (ref)                                                    | 1.07x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7+-718d234 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 449 ms: 1.47x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 455 ms: 1.46x faster                                                     |
| async_tree_none            | 504 ms                                                   | 366 ms: 1.38x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 854 ms: 1.36x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 355 ms: 1.36x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 859 ms: 1.33x faster                                                     |
| async_generators           | 500 ms                                                   | 410 ms: 1.22x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 708 ms: 1.13x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 709 ms: 1.11x faster                                                     |
| Geometric mean             | (ref)                                                    | 1.25x faster                                                             |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7+-718d234 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 84.8 ms: 1.13x faster                                                    |
| nbody          | 118 ms                                                   | 124 ms: 1.05x slower                                                     |
| pidigits       | 238 ms                                                   | 291 ms: 1.22x slower                                                     |
| Geometric mean | (ref)                                                    | 1.04x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7+-718d234 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.04 ms: 1.26x faster                                                    |
| regex_dna      | 263 ms                                                   | 236 ms: 1.11x faster                                                     |
| regex_compile  | 134 ms                                                   | 121 ms: 1.11x faster                                                     |
| regex_v8       | 32.5 ms                                                  | 29.4 ms: 1.10x faster                                                    |
| Geometric mean | (ref)                                                    | 1.14x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7+-718d234 |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads         | 2.67 sec                                                 | 2.31 sec: 1.16x faster                                                   |
| xml_etree_generate  | 118 ms                                                   | 105 ms: 1.13x faster                                                     |
| xml_etree_process   | 82.1 ms                                                  | 74.5 ms: 1.10x faster                                                    |
| xml_etree_iterparse | 159 ms                                                   | 148 ms: 1.07x faster                                                     |
| Geometric mean      | (ref)                                                    | 1.05x faster                                                             |

Benchmark hidden because not significant (5): unpickle_pure_python, json_dumps, pickle_pure_python, xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7+-718d234 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 10.2 ms: 1.16x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.08x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7+-718d234 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text    | 28.6 ms                                                  | 25.7 ms: 1.11x faster                                                    |
| genshi_xml     | 61.6 ms                                                  | 57.0 ms: 1.08x faster                                                    |
| Geometric mean | (ref)                                                    | 1.05x faster                                                             |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7+-718d234 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.61 sec: 2.14x faster                                                   |
| deepcopy                   | 479 us                                                   | 294 us: 1.63x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 35.0 us: 1.51x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 449 ms: 1.47x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 455 ms: 1.46x faster                                                     |
| async_tree_none            | 504 ms                                                   | 366 ms: 1.38x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 854 ms: 1.36x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 355 ms: 1.36x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 859 ms: 1.33x faster                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 3.34 us: 1.27x faster                                                    |
| go                         | 164 ms                                                   | 130 ms: 1.27x faster                                                     |
| regex_effbot               | 5.10 ms                                                  | 4.04 ms: 1.26x faster                                                    |
| spectral_norm              | 143 ms                                                   | 116 ms: 1.24x faster                                                     |
| async_generators           | 500 ms                                                   | 410 ms: 1.22x faster                                                     |
| logging_silent             | 135 ns                                                   | 112 ns: 1.20x faster                                                     |
| scimark_fft                | 463 ms                                                   | 393 ms: 1.18x faster                                                     |
| telco                      | 10.5 ms                                                  | 8.90 ms: 1.18x faster                                                    |
| scimark_sor                | 164 ms                                                   | 141 ms: 1.16x faster                                                     |
| tomli_loads                | 2.67 sec                                                 | 2.31 sec: 1.16x faster                                                   |
| pathlib                    | 24.3 ms                                                  | 21.4 ms: 1.14x faster                                                    |
| generators                 | 40.3 ms                                                  | 35.5 ms: 1.13x faster                                                    |
| scimark_monte_carlo        | 87.8 ms                                                  | 77.5 ms: 1.13x faster                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 5.32 sec: 1.13x faster                                                   |
| pyflate                    | 582 ms                                                   | 515 ms: 1.13x faster                                                     |
| richards                   | 54.5 ms                                                  | 48.2 ms: 1.13x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 708 ms: 1.13x faster                                                     |
| float                      | 95.8 ms                                                  | 84.8 ms: 1.13x faster                                                    |
| xml_etree_generate         | 118 ms                                                   | 105 ms: 1.13x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 709 ms: 1.11x faster                                                     |
| regex_dna                  | 263 ms                                                   | 236 ms: 1.11x faster                                                     |
| genshi_text                | 28.6 ms                                                  | 25.7 ms: 1.11x faster                                                    |
| richards_super             | 60.8 ms                                                  | 54.9 ms: 1.11x faster                                                    |
| regex_compile              | 134 ms                                                   | 121 ms: 1.11x faster                                                     |
| pylint                     | 345 ms                                                   | 313 ms: 1.11x faster                                                     |
| regex_v8                   | 32.5 ms                                                  | 29.4 ms: 1.10x faster                                                    |
| pycparser                  | 1.34 sec                                                 | 1.22 sec: 1.10x faster                                                   |
| xml_etree_process          | 82.1 ms                                                  | 74.5 ms: 1.10x faster                                                    |
| html5lib                   | 65.6 ms                                                  | 59.6 ms: 1.10x faster                                                    |
| coverage                   | 106 ms                                                   | 96.7 ms: 1.09x faster                                                    |
| sympy_sum                  | 151 ms                                                   | 138 ms: 1.09x faster                                                     |
| k_core                     | 2.99 sec                                                 | 2.75 sec: 1.09x faster                                                   |
| sympy_integrate            | 21.4 ms                                                  | 19.8 ms: 1.09x faster                                                    |
| logging_format             | 8.10 us                                                  | 7.47 us: 1.08x faster                                                    |
| logging_simple             | 7.25 us                                                  | 6.70 us: 1.08x faster                                                    |
| sphinx                     | 1.20 sec                                                 | 1.11 sec: 1.08x faster                                                   |
| genshi_xml                 | 61.6 ms                                                  | 57.0 ms: 1.08x faster                                                    |
| chaos                      | 70.7 ms                                                  | 65.6 ms: 1.08x faster                                                    |
| pprint_pformat             | 1.99 sec                                                 | 1.84 sec: 1.08x faster                                                   |
| nqueens                    | 105 ms                                                   | 97.7 ms: 1.07x faster                                                    |
| 2to3                       | 313 ms                                                   | 291 ms: 1.07x faster                                                     |
| xml_etree_iterparse        | 159 ms                                                   | 148 ms: 1.07x faster                                                     |
| pprint_safe_repr           | 962 ms                                                   | 900 ms: 1.07x faster                                                     |
| scimark_lu                 | 146 ms                                                   | 137 ms: 1.07x faster                                                     |
| hexiom                     | 7.34 ms                                                  | 6.90 ms: 1.06x faster                                                    |
| sqlite_synth               | 4.08 us                                                  | 3.84 us: 1.06x faster                                                    |
| sympy_expand               | 472 ms                                                   | 446 ms: 1.06x faster                                                     |
| comprehensions             | 20.8 us                                                  | 19.7 us: 1.06x faster                                                    |
| deltablue                  | 3.97 ms                                                  | 3.76 ms: 1.05x faster                                                    |
| typing_runtime_protocols   | 197 us                                                   | 187 us: 1.05x faster                                                     |
| sympy_str                  | 265 ms                                                   | 253 ms: 1.05x faster                                                     |
| docutils                   | 2.96 sec                                                 | 2.87 sec: 1.03x faster                                                   |
| shortest_path              | 565 ms                                                   | 584 ms: 1.03x slower                                                     |
| nbody                      | 118 ms                                                   | 124 ms: 1.05x slower                                                     |
| create_gc_cycles           | 3.39 ms                                                  | 3.62 ms: 1.07x slower                                                    |
| gc_traversal               | 5.92 ms                                                  | 6.56 ms: 1.11x slower                                                    |
| python_startup_no_site     | 8.79 ms                                                  | 10.2 ms: 1.16x slower                                                    |
| pidigits                   | 238 ms                                                   | 291 ms: 1.22x slower                                                     |
| subparsers                 | 20.3 ms                                                  | 25.6 ms: 1.26x slower                                                    |
| many_optionals             | 626 us                                                   | 810 us: 1.29x slower                                                     |
| bench_mp_pool              | 8.07 ms                                                  | 2.97 sec: 368.40x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.03x faster                                                             |

Benchmark hidden because not significant (20): unpickle_pure_python, sqlalchemy_declarative, coroutines, sqlalchemy_imperative, django_template, json_dumps, json, bench_thread_pool, pickle_pure_python, meteor_contest, scimark_sparse_mat_mult, crypto_pyaes, asyncio_websockets, mako, python_startup, xml_etree_parse, connected_components, raytrace, fannkuch, json_loads
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (13) of results/bm-20250412-3.14.0a7+-718d234-CLANG/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7+-718d234.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.085x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.07x