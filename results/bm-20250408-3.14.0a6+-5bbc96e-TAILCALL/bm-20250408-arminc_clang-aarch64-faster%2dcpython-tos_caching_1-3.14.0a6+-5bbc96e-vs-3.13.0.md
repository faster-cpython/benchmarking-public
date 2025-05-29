# Results vs. 3.13.0

- fork: faster-cpython
- ref: tos_caching_1
- machine: linux-aarch64
- commit hash: 5bbc96e
- commit date: 2025-04-08
- overall geometric mean: 1.078x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-arminc-aarch64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 285 ms: 1.10x faster                                                        |
| html5lib       | 65.6 ms                                                  | 60.0 ms: 1.09x faster                                                       |
| sphinx         | 1.20 sec                                                 | 1.11 sec: 1.08x faster                                                      |
| Geometric mean | (ref)                                                    | 1.07x faster                                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-arminc-aarch64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization     | 664 ms                                                   | 457 ms: 1.45x faster                                                        |
| async_tree_memoization_tg  | 663 ms                                                   | 459 ms: 1.44x faster                                                        |
| async_tree_io_tg           | 1.16 sec                                                 | 875 ms: 1.33x faster                                                        |
| async_tree_io              | 1.14 sec                                                 | 872 ms: 1.31x faster                                                        |
| async_tree_none_tg         | 484 ms                                                   | 372 ms: 1.30x faster                                                        |
| async_tree_none            | 504 ms                                                   | 391 ms: 1.29x faster                                                        |
| async_generators           | 500 ms                                                   | 408 ms: 1.23x faster                                                        |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 712 ms: 1.13x faster                                                        |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 724 ms: 1.09x faster                                                        |
| Geometric mean             | (ref)                                                    | 1.22x faster                                                                |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-arminc-aarch64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 82.1 ms: 1.17x faster                                                       |
| pidigits       | 238 ms                                                   | 291 ms: 1.22x slower                                                        |
| Geometric mean | (ref)                                                    | 1.03x slower                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-arminc-aarch64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.16 ms: 1.23x faster                                                       |
| regex_dna      | 263 ms                                                   | 238 ms: 1.10x faster                                                        |
| regex_v8       | 32.5 ms                                                  | 29.8 ms: 1.09x faster                                                       |
| regex_compile  | 134 ms                                                   | 123 ms: 1.09x faster                                                        |
| Geometric mean | (ref)                                                    | 1.13x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-arminc-aarch64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|---------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads         | 2.67 sec                                                 | 2.33 sec: 1.14x faster                                                      |
| xml_etree_generate  | 118 ms                                                   | 109 ms: 1.09x faster                                                        |
| xml_etree_process   | 82.1 ms                                                  | 77.0 ms: 1.07x faster                                                       |
| xml_etree_iterparse | 159 ms                                                   | 150 ms: 1.06x faster                                                        |
| Geometric mean      | (ref)                                                    | 1.04x faster                                                                |

Benchmark hidden because not significant (5): unpickle_pure_python, json_dumps, json_loads, pickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-arminc-aarch64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 10.2 ms: 1.16x slower                                                       |
| Geometric mean         | (ref)                                                    | 1.08x slower                                                                |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-arminc-aarch64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text    | 28.6 ms                                                  | 26.5 ms: 1.08x faster                                                       |
| genshi_xml     | 61.6 ms                                                  | 58.7 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                    | 1.03x faster                                                                |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-arminc-aarch64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.60 sec: 2.15x faster                                                      |
| deepcopy                   | 479 us                                                   | 312 us: 1.53x faster                                                        |
| async_tree_memoization     | 664 ms                                                   | 457 ms: 1.45x faster                                                        |
| deepcopy_memo              | 53.0 us                                                  | 36.6 us: 1.45x faster                                                       |
| async_tree_memoization_tg  | 663 ms                                                   | 459 ms: 1.44x faster                                                        |
| async_tree_io_tg           | 1.16 sec                                                 | 875 ms: 1.33x faster                                                        |
| async_tree_io              | 1.14 sec                                                 | 872 ms: 1.31x faster                                                        |
| async_tree_none_tg         | 484 ms                                                   | 372 ms: 1.30x faster                                                        |
| async_tree_none            | 504 ms                                                   | 391 ms: 1.29x faster                                                        |
| go                         | 164 ms                                                   | 132 ms: 1.25x faster                                                        |
| deepcopy_reduce            | 4.24 us                                                  | 3.45 us: 1.23x faster                                                       |
| regex_effbot               | 5.10 ms                                                  | 4.16 ms: 1.23x faster                                                       |
| async_generators           | 500 ms                                                   | 408 ms: 1.23x faster                                                        |
| spectral_norm              | 143 ms                                                   | 117 ms: 1.22x faster                                                        |
| scimark_sor                | 164 ms                                                   | 135 ms: 1.21x faster                                                        |
| scimark_fft                | 463 ms                                                   | 385 ms: 1.20x faster                                                        |
| generators                 | 40.3 ms                                                  | 34.3 ms: 1.17x faster                                                       |
| float                      | 95.8 ms                                                  | 82.1 ms: 1.17x faster                                                       |
| pathlib                    | 24.3 ms                                                  | 21.0 ms: 1.16x faster                                                       |
| pylint                     | 345 ms                                                   | 301 ms: 1.15x faster                                                        |
| telco                      | 10.5 ms                                                  | 9.12 ms: 1.15x faster                                                       |
| bpe_tokeniser              | 6.02 sec                                                 | 5.26 sec: 1.14x faster                                                      |
| logging_silent             | 135 ns                                                   | 118 ns: 1.14x faster                                                        |
| tomli_loads                | 2.67 sec                                                 | 2.33 sec: 1.14x faster                                                      |
| scimark_monte_carlo        | 87.8 ms                                                  | 76.9 ms: 1.14x faster                                                       |
| pyflate                    | 582 ms                                                   | 515 ms: 1.13x faster                                                        |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 712 ms: 1.13x faster                                                        |
| coverage                   | 106 ms                                                   | 94.6 ms: 1.12x faster                                                       |
| regex_dna                  | 263 ms                                                   | 238 ms: 1.10x faster                                                        |
| sympy_integrate            | 21.4 ms                                                  | 19.5 ms: 1.10x faster                                                       |
| 2to3                       | 313 ms                                                   | 285 ms: 1.10x faster                                                        |
| html5lib                   | 65.6 ms                                                  | 60.0 ms: 1.09x faster                                                       |
| regex_v8                   | 32.5 ms                                                  | 29.8 ms: 1.09x faster                                                       |
| regex_compile              | 134 ms                                                   | 123 ms: 1.09x faster                                                        |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 724 ms: 1.09x faster                                                        |
| xml_etree_generate         | 118 ms                                                   | 109 ms: 1.09x faster                                                        |
| pycparser                  | 1.34 sec                                                 | 1.24 sec: 1.08x faster                                                      |
| chaos                      | 70.7 ms                                                  | 65.4 ms: 1.08x faster                                                       |
| sphinx                     | 1.20 sec                                                 | 1.11 sec: 1.08x faster                                                      |
| genshi_text                | 28.6 ms                                                  | 26.5 ms: 1.08x faster                                                       |
| k_core                     | 2.99 sec                                                 | 2.78 sec: 1.08x faster                                                      |
| sqlalchemy_declarative     | 154 ms                                                   | 143 ms: 1.08x faster                                                        |
| deltablue                  | 3.97 ms                                                  | 3.69 ms: 1.07x faster                                                       |
| logging_format             | 8.10 us                                                  | 7.57 us: 1.07x faster                                                       |
| richards                   | 54.5 ms                                                  | 51.0 ms: 1.07x faster                                                       |
| xml_etree_process          | 82.1 ms                                                  | 77.0 ms: 1.07x faster                                                       |
| sqlite_synth               | 4.08 us                                                  | 3.84 us: 1.06x faster                                                       |
| xml_etree_iterparse        | 159 ms                                                   | 150 ms: 1.06x faster                                                        |
| comprehensions             | 20.8 us                                                  | 19.7 us: 1.06x faster                                                       |
| pprint_pformat             | 1.99 sec                                                 | 1.88 sec: 1.05x faster                                                      |
| meteor_contest             | 117 ms                                                   | 111 ms: 1.05x faster                                                        |
| logging_simple             | 7.25 us                                                  | 6.90 us: 1.05x faster                                                       |
| genshi_xml                 | 61.6 ms                                                  | 58.7 ms: 1.05x faster                                                       |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 6.36 ms: 1.05x faster                                                       |
| typing_runtime_protocols   | 197 us                                                   | 189 us: 1.04x faster                                                        |
| pprint_safe_repr           | 962 ms                                                   | 925 ms: 1.04x faster                                                        |
| sympy_expand               | 472 ms                                                   | 457 ms: 1.03x faster                                                        |
| sympy_str                  | 265 ms                                                   | 257 ms: 1.03x faster                                                        |
| create_gc_cycles           | 3.39 ms                                                  | 3.66 ms: 1.08x slower                                                       |
| gc_traversal               | 5.92 ms                                                  | 6.53 ms: 1.10x slower                                                       |
| python_startup_no_site     | 8.79 ms                                                  | 10.2 ms: 1.16x slower                                                       |
| pidigits                   | 238 ms                                                   | 291 ms: 1.22x slower                                                        |
| subparsers                 | 20.3 ms                                                  | 25.6 ms: 1.26x slower                                                       |
| many_optionals             | 626 us                                                   | 829 us: 1.32x slower                                                        |
| bench_mp_pool              | 8.07 ms                                                  | 2.97 sec: 368.01x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.02x faster                                                                |

Benchmark hidden because not significant (25): sympy_sum, richards_super, nqueens, unpickle_pure_python, bench_thread_pool, django_template, scimark_lu, crypto_pyaes, sqlalchemy_imperative, json_dumps, hexiom, json, asyncio_websockets, docutils, python_startup, raytrace, shortest_path, json_loads, coroutines, pickle_pure_python, connected_components, fannkuch, xml_etree_parse, mako, nbody
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (5) of results/bm-20250408-3.14.0a6+-5bbc96e-CLANG/bm-20250408-arminc-aarch64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.078x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.06x